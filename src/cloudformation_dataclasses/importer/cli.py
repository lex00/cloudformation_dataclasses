"""Command-line interface for cfn-dataclasses-import."""

from __future__ import annotations

import argparse
import logging
import os
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

from cloudformation_dataclasses.importer.ir import IRTemplate

from cloudformation_dataclasses import __version__
from cloudformation_dataclasses.importer.codegen import generate_code, generate_package
from cloudformation_dataclasses.importer.parser import parse_template


def _get_aws_module_names() -> set[str]:
    """Get the set of AWS module names to avoid package name collisions.

    Returns module names like 'config', 's3', 'ec2', etc. that would collide
    with cloudformation_dataclasses.aws.<name> if used as a package name.
    """
    import cloudformation_dataclasses.aws as aws_pkg

    aws_path = Path(aws_pkg.__file__).parent
    modules = set()
    for item in aws_path.iterdir():
        # AWS modules are stored as directories (packages), not .py files
        if item.is_dir() and not item.name.startswith("_"):
            name = item.name
            # lambda_ is stored with underscore to avoid Python keyword
            # but template named "lambda.yaml" would become "lambda" package
            if name == "lambda_":
                modules.add("lambda")
            else:
                modules.add(name)
    return modules


# Cache for AWS module names
_AWS_MODULE_NAMES: set[str] | None = None


def _collides_with_aws_module(package_name: str) -> bool:
    """Check if a package name would collide with an AWS module."""
    global _AWS_MODULE_NAMES
    if _AWS_MODULE_NAMES is None:
        _AWS_MODULE_NAMES = _get_aws_module_names()
    return package_name in _AWS_MODULE_NAMES


@dataclass
class Attribution:
    """Attribution info extracted from source directory."""

    source_url: str | None = None
    project_name: str | None = None
    license_type: str | None = None


def _get_git_remote_url(git_dir: Path) -> str | None:
    """Extract origin URL from .git/config file."""
    config_file = git_dir / "config"
    if not config_file.exists():
        return None

    try:
        content = config_file.read_text()
        # Look for [remote "origin"] section and extract url
        in_origin = False
        for line in content.splitlines():
            if line.strip() == '[remote "origin"]':
                in_origin = True
            elif line.startswith("[") and in_origin:
                break
            elif in_origin and line.strip().startswith("url ="):
                url = line.split("=", 1)[1].strip()
                # Convert git@ URLs to https://
                if url.startswith("git@github.com:"):
                    url = url.replace("git@github.com:", "https://github.com/")
                elif url.startswith("git@gitlab.com:"):
                    url = url.replace("git@gitlab.com:", "https://gitlab.com/")
                # Remove .git suffix
                if url.endswith(".git"):
                    url = url[:-4]
                return url
    except Exception:
        pass
    return None


def detect_attribution(source_dir: Path) -> Attribution:
    """Check source folder (and parent directories) for .git/README/LICENSE.

    Walks up the directory tree to find attribution files, stopping at
    the first directory that contains a .git folder, README.md, or LICENSE.
    Git remote origin takes priority over URLs found in README.
    """
    source_url = None
    project_name = None
    license_type = None

    # Walk up directory tree to find .git/README/LICENSE (up to 5 levels)
    current = source_dir.resolve()
    for _ in range(5):
        readme = current / "README.md"
        git_dir = current / ".git"

        # Check for LICENSE with various extensions
        license_file = None
        for name in ("LICENSE", "LICENSE.txt", "LICENSE.md"):
            candidate = current / name
            if candidate.exists():
                license_file = candidate
                break

        # Git remote origin takes priority for source URL
        if git_dir.exists():
            source_url = _get_git_remote_url(git_dir)

        if readme.exists():
            content = readme.read_text()
            # Only use README URL if no git remote found
            if not source_url:
                url_match = re.search(
                    r"https?://(?:github|gitlab)\.com/[^\s\)\]]+", content
                )
                if url_match:
                    source_url = url_match.group(0).rstrip("/.")

            # Try to extract project name from first heading
            heading_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if heading_match:
                project_name = heading_match.group(1).strip()

        if license_file:
            content = license_file.read_text()
            # Detect common license types
            if "Apache License" in content and "Version 2.0" in content:
                license_type = "Apache-2.0"
            elif "MIT License" in content or "Permission is hereby granted, free of charge" in content:
                license_type = "MIT"
            elif "GNU GENERAL PUBLIC LICENSE" in content:
                if "Version 3" in content:
                    license_type = "GPL-3.0"
                elif "Version 2" in content:
                    license_type = "GPL-2.0"
            elif "BSD" in content:
                license_type = "BSD"

        # If we found any attribution info, stop walking up
        if source_url or project_name or license_type:
            break

        # Move to parent directory
        parent = current.parent
        if parent == current:  # Reached filesystem root
            break
        current = parent

    return Attribution(
        source_url=source_url,
        project_name=project_name,
        license_type=license_type,
    )


def _substitute_variables(content: str, variables: dict[str, str]) -> str:
    """Substitute {{variable}} placeholders in content."""

    def replace(match: re.Match[str]) -> str:
        var_name = match.group(1)
        if var_name in variables:
            return variables[var_name]
        return match.group(0)

    return re.sub(r"\{\{(\w+)\}\}", replace, content)


def _to_pascal_case(name: str) -> str:
    """Convert snake_case or kebab-case to PascalCase."""
    words = name.replace("-", "_").split("_")
    return "".join(word.capitalize() for word in words)


def _process_package_templates(
    pkg: resources.abc.Traversable,
    output_dir: Path,
    variables: dict[str, str],
) -> list[Path]:
    """Recursively process package templates directory.

    Returns:
        List of created file paths.
    """
    created_files: list[Path] = []
    output_dir.mkdir(parents=True, exist_ok=True)

    for item in pkg.iterdir():
        # Skip Python package infrastructure
        if item.name in ("__init__.py", "__pycache__"):
            continue

        if item.is_dir():
            created_files.extend(
                _process_package_templates(item, output_dir / item.name, variables)
            )
            continue

        # Read template content
        content = item.read_text()

        # Determine output filename (strip .template suffix if present)
        output_name = item.name
        if output_name.endswith(".template"):
            output_name = output_name[: -len(".template")]

        # Substitute variables
        content = _substitute_variables(content, variables)

        # Write output file
        output_path = output_dir / output_name
        output_path.write_text(content)
        created_files.append(output_path)

    return created_files


def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for cfn-dataclasses-import command.

    Args:
        argv: Command line arguments (default: sys.argv[1:])

    Returns:
        Exit code (0 for success)
    """
    parser = argparse.ArgumentParser(
        prog="cfn-dataclasses-import",
        description="Convert CloudFormation templates to Python dataclasses.",
    )

    parser.add_argument(
        "input",
        metavar="INPUT",
        help='Template file path, or "-" for stdin',
    )

    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        help="Output path: directory for package (default), .py file for single file, omit for stdout",
    )

    parser.add_argument(
        "--no-main",
        action="store_true",
        help="Omit if __name__ == '__main__' block (single-file mode only)",
    )

    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip validation, linting, and test generation",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args(argv)

    input_path = Path(args.input) if args.input != "-" else None

    # Check if input is a directory (batch mode)
    if input_path and input_path.is_dir():
        if not args.output:
            print("Error: -o/--output is required for batch mode", file=sys.stderr)
            return 1
        return run_batch_import(
            source_dir=input_path,
            output_dir=Path(args.output),
            skip_checks=args.skip_checks,
        )

    # Single template mode
    return run_single_import(
        input_arg=args.input,
        output_arg=args.output,
        no_main=args.no_main,
        skip_checks=args.skip_checks,
    )


def run_single_import(
    input_arg: str,
    output_arg: str | None,
    no_main: bool = False,
    skip_checks: bool = False,
    attribution: Attribution | None = None,
    logger: logging.Logger | None = None,
) -> int:
    """Import a single CloudFormation template.

    Args:
        input_arg: Template file path or "-" for stdin
        output_arg: Output path (directory, .py file, or None for stdout)
        no_main: Omit if __name__ == '__main__' block
        skip_checks: Skip validation, linting, and test generation
        attribution: Optional attribution info for README
        logger: Optional logger for batch mode

    Returns:
        Exit code (0 for success)
    """
    # Determine output mode from -o path
    # - No -o or "-": stdout -> single file
    # - Ends with .py: single file
    # - Otherwise: package (directory)
    if output_arg is None or output_arg == "-":
        use_package = False
    elif output_arg.endswith(".py"):
        use_package = False
    else:
        use_package = True

    def log(msg: str) -> None:
        if logger:
            logger.info(msg)
        else:
            print(msg, file=sys.stderr)

    try:
        # Parse input
        if input_arg == "-":
            content = sys.stdin.read()
            template = parse_template(content, source_name="<stdin>")
        else:
            input_path = Path(input_arg)
            if not input_path.exists():
                msg = f"Error: File not found: {input_arg}"
                if logger:
                    logger.error(msg)
                else:
                    print(msg, file=sys.stderr)
                return 1
            template = parse_template(input_path)

        if use_package:
            # Write files to output directory
            assert output_arg is not None  # Guaranteed by use_package logic above
            output_dir = Path(output_arg)
            output_dir.mkdir(parents=True, exist_ok=True)

            # Get project name from output directory (used for nested package structure)
            project_name = output_dir.name

            # Generate package (multiple files) with nested structure
            files = generate_package(template, package_name=project_name)

            for filename, file_content in files.items():
                file_path = output_dir / filename
                # Create parent directories if needed (e.g., for package_name/resources/foo.py)
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(file_content)
                log(f"Generated: {file_path}")

            # Generate IDE support files from shared package templates
            variables = {
                "project_name": project_name,
                "ProjectName": _to_pascal_case(project_name),
            }
            package_templates_pkg = resources.files(
                "cloudformation_dataclasses.package_templates"
            )
            ide_files = _process_package_templates(
                package_templates_pkg, output_dir, variables
            )
            for file_path in ide_files:
                log(f"Generated: {file_path}")

            # Copy original template to original/ subfolder
            if input_arg != "-":
                original_dir = output_dir / "original"
                original_dir.mkdir(exist_ok=True)
                shutil.copy(input_path, original_dir / input_path.name)
                log(f"Generated: {original_dir / input_path.name}")

            # Always generate README with resource table
            source_file = Path(input_arg).name if input_arg != "-" else "template"
            readme_path = output_dir / "README.md"
            readme_content = _generate_readme(
                project_name=project_name,
                source_file=source_file,
                template=template,
                attribution=attribution,
            )
            readme_path.write_text(readme_content)
            log(f"Generated: {readme_path}")

            # Generate test files
            if not skip_checks:
                test_files = _generate_tests(project_name, template)
                for test_filename, test_content in test_files.items():
                    test_path = output_dir / test_filename
                    test_path.parent.mkdir(parents=True, exist_ok=True)
                    test_path.write_text(test_content)
                    log(f"Generated: {test_path}")

        else:
            # Generate single file
            code = generate_code(template, include_main=not no_main)

            # Output
            if output_arg and output_arg != "-":
                output_path = Path(output_arg)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(code)
                log(f"Generated: {output_arg}")
            else:
                print(code)

        return 0

    except ValueError as e:
        msg = f"Error: {e}"
        if logger:
            logger.error(msg)
        else:
            print(msg, file=sys.stderr)
        return 1
    except Exception as e:
        msg = f"Error: {e}"
        if logger:
            logger.error(msg)
        else:
            print(msg, file=sys.stderr)
        return 1


def _generate_readme(
    project_name: str,
    source_file: str,
    template: IRTemplate,
    attribution: Attribution | None = None,
) -> str:
    """Generate README.md with resource table and optional attribution."""
    lines = [f"# {_to_pascal_case(project_name)}", ""]

    # Attribution section
    if attribution and attribution.source_url:
        lines.append(f"Migrated from [{source_file}]({attribution.source_url}).")
    else:
        lines.append(f"Imported from `{source_file}`.")
    lines.append("")

    if attribution:
        if attribution.project_name:
            lines.append(f"**Source**: {attribution.project_name}")
        if attribution.license_type:
            lines.append(f"**License**: {attribution.license_type}")
        if attribution.project_name or attribution.license_type:
            lines.append("")

    # Usage section
    lines.extend([
        "**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**",
        "",
        "## Usage",
        "",
        "This is a portable Python package. You can copy this folder into another",
        "project and use it directly.",
        "",
        "### Run Tests",
        "",
        "```bash",
        "uv run pytest tests/ -v",
        "```",
        "",
        "### Generate Template",
        "",
        "```bash",
        f"uv run python -m {project_name}",
        "```",
        "",
        "### Install as Dependency",
        "",
        "```bash",
        "pip install .",
        "```",
        "",
    ])

    # Resource table
    if template.resources:
        lines.extend([
            "## Resources",
            "",
            "| Logical ID | Type |",
            "|------------|------|",
        ])
        for name, resource in template.resources.items():
            lines.append(f"| `{name}` | {resource.resource_type} |")
        lines.append("")

    return "\n".join(lines)


def _generate_tests(
    project_name: str,
    template: IRTemplate,
) -> dict[str, str]:
    """Generate test files for the package.

    Returns:
        Dictionary of filename -> content for test files.
    """
    pascal_name = _to_pascal_case(project_name)
    resource_count = len(template.resources)

    init_content = f'"""Tests for {project_name} example."""\n'

    test_content = f'''"""Tests for {project_name} example."""

import pytest

from {project_name}.main import build_template


class Test{pascal_name}:
    """Test {project_name} example."""

    @pytest.fixture
    def template(self):
        """Build template."""
        return build_template()

    def test_validates(self, template):
        """Template should pass validation."""
        errors = template.validate()
        assert errors == [], f"Validation errors: {{errors}}"

    def test_resource_count(self, template):
        """Verify expected number of resources."""
        output = template.to_dict()
        assert len(output["Resources"]) == {resource_count}
'''

    return {
        "tests/__init__.py": init_content,
        f"tests/test_{project_name}.py": test_content,
    }


def run_batch_import(
    source_dir: Path,
    output_dir: Path,
    skip_checks: bool = False,
) -> int:
    """Import multiple CloudFormation templates from a directory.

    Args:
        source_dir: Directory containing template files
        output_dir: Output directory for generated packages
        skip_checks: Skip validation, linting, and test generation

    Returns:
        Exit code (0 for success, 1 if any imports failed)
    """
    # Find all template files recursively
    templates: list[Path] = []
    for pattern in ("**/*.yaml", "**/*.yml", "**/*.json"):
        templates.extend(source_dir.glob(pattern))

    # Filter out non-CloudFormation files (e.g., package.json)
    templates = [
        t for t in templates
        if t.suffix in (".yaml", ".yml")
        or (t.suffix == ".json" and t.name != "package.json")
    ]

    # Prefer YAML over JSON when both exist (skip duplicate JSON files)
    yaml_stems = {t.stem for t in templates if t.suffix in (".yaml", ".yml")}
    templates = [
        t for t in templates
        if t.suffix in (".yaml", ".yml") or t.stem not in yaml_stems
    ]

    if not templates:
        print(f"No templates found in {source_dir}", file=sys.stderr)
        return 1

    # Create output directory and log file
    output_dir.mkdir(parents=True, exist_ok=True)
    log_file = output_dir / "import.log"

    # Set up logging
    logger = logging.getLogger("cfn-dataclasses-import-batch")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    logger.addHandler(file_handler)

    # Detect attribution from source directory
    attribution = detect_attribution(source_dir)
    if not attribution.source_url and not attribution.project_name:
        logger.warning("No attribution info found in source directory")
        print("Warning: No attribution info found in source directory", file=sys.stderr)

    # Track results
    succeeded: list[str] = []
    failed: list[tuple[str, str]] = []  # (filename, error message)

    print(f"Found {len(templates)} template(s) in {source_dir}", file=sys.stderr)
    logger.info(f"Starting batch import of {len(templates)} templates")

    # Prepare import tasks
    def _import_template(template_path: Path) -> tuple[str, int]:
        """Import a single template and return (name, result)."""
        template_name = template_path.stem
        # Convert to valid Python package name
        package_name = re.sub(r"[^a-zA-Z0-9_]", "_", template_name).lower()

        # Avoid collision with AWS module names (e.g., config, s3, iam)
        if _collides_with_aws_module(package_name):
            package_name = f"{package_name}_cfn"

        package_output = output_dir / package_name
        logger.info(f"Importing {template_path}")

        result = run_single_import(
            input_arg=str(template_path),
            output_arg=str(package_output),
            skip_checks=skip_checks,
            attribution=attribution,
            logger=logger,
        )
        return (template_path.name, result)

    # Run imports in parallel
    max_workers = min(os.cpu_count() or 4, 8)  # Cap to avoid overwhelming I/O
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(_import_template, t): t
            for t in sorted(templates)
        }

        for future in as_completed(futures):
            template_name, result = future.result()
            if result == 0:
                print(f"✓ {template_name}", file=sys.stderr)
                succeeded.append(template_name)
            else:
                print(f"✗ {template_name}", file=sys.stderr)
                failed.append((template_name, "Import failed (see log for details)"))

    # Print summary
    print(file=sys.stderr)
    print(f"Summary: {len(succeeded)}/{len(templates)} succeeded", file=sys.stderr)

    if failed:
        print("Failed:", file=sys.stderr)
        for name, error in failed:
            print(f"  - {name}: {error}", file=sys.stderr)

    print(f"\nLog: {log_file}", file=sys.stderr)
    logger.info(f"Batch import complete: {len(succeeded)}/{len(templates)} succeeded")

    # Clean up logger
    logger.removeHandler(file_handler)
    file_handler.close()

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
