"""Command-line interface for cfn-dataclasses.

This module provides the CLI for the cloudformation_dataclasses toolkit,
including three subcommands:

- **init**: Create a new project skeleton
- **import**: Convert CloudFormation YAML/JSON to Python dataclasses
- **lint**: Check and auto-fix common style issues

Example:
    Create a new project:
        $ cfn-dataclasses init -o my_stack/

    Import a CloudFormation template:
        $ cfn-dataclasses import template.yaml -o my_stack/

    Lint generated code:
        $ cfn-dataclasses lint my_stack/ --fix
"""

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


class CLIError(Exception):
    """CLI error with user-friendly message and optional suggestion.

    Use this exception to provide clear, actionable error messages to users.
    The suggestion field can provide guidance on how to resolve the error.

    Example:
        raise CLIError(
            "Template contains unsupported intrinsic function: !Transform",
            suggestion="Remove the !Transform macro or manually convert it after import."
        )
    """

    def __init__(self, message: str, suggestion: str | None = None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(message)


def _format_cli_error(error: CLIError) -> str:
    """Format a CLIError for display to the user.

    Args:
        error: The CLIError to format.

    Returns:
        Formatted error string ready for display.
    """
    result = f"Error: {error.message}"
    if error.suggestion:
        result += f"\n\nSuggestion: {error.suggestion}"
    return result


def _get_aws_module_names() -> set[str]:
    """Get the set of AWS module names to avoid package name collisions.

    Scans the cloudformation_dataclasses.aws package to find all AWS service
    module names. These names (like 'config', 's3', 'ec2') would cause import
    conflicts if used as generated package names.

    Returns:
        Set of AWS module names that should be avoided for package names.
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
    """Check if a package name would collide with an AWS module.

    Args:
        package_name: The proposed package name to check.

    Returns:
        True if the name collides with an AWS module, False otherwise.
    """
    global _AWS_MODULE_NAMES
    if _AWS_MODULE_NAMES is None:
        _AWS_MODULE_NAMES = _get_aws_module_names()
    return package_name in _AWS_MODULE_NAMES


@dataclass
class Attribution:
    """Attribution information extracted from a source directory.

    Used to generate README attribution sections when batch importing
    templates from external repositories.

    Attributes:
        source_url: URL to the source repository (GitHub, GitLab, etc.).
        project_name: Name of the source project (from README heading).
        license_type: License identifier (MIT, Apache-2.0, etc.).
    """

    source_url: str | None = None
    project_name: str | None = None
    license_type: str | None = None


def _get_git_remote_url(git_dir: Path) -> str | None:
    """Extract the origin remote URL from a .git/config file.

    Converts SSH URLs to HTTPS format and removes .git suffix.

    Args:
        git_dir: Path to the .git directory.

    Returns:
        The remote origin URL, or None if not found.
    """
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
    """Detect attribution information from a source directory.

    Walks up the directory tree (up to 5 levels) looking for:
    - .git/config: Remote origin URL
    - README.md: Project name and fallback URL
    - LICENSE: License type detection

    Git remote origin takes priority over URLs found in README.

    Args:
        source_dir: The directory to start searching from.

    Returns:
        Attribution dataclass with any discovered information.
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
    """Substitute {{variable}} placeholders in content.

    Args:
        content: Template string with {{variable}} placeholders.
        variables: Dictionary mapping variable names to values.

    Returns:
        Content with all known placeholders replaced.
    """

    def replace(match: re.Match[str]) -> str:
        var_name = match.group(1)
        if var_name in variables:
            return variables[var_name]
        return match.group(0)

    return re.sub(r"\{\{(\w+)\}\}", replace, content)


def _to_pascal_case(name: str) -> str:
    """Convert snake_case or kebab-case to PascalCase.

    Args:
        name: A string in snake_case or kebab-case.

    Returns:
        The string converted to PascalCase.

    Example:
        >>> _to_pascal_case("my_project")
        'MyProject'
    """
    words = name.replace("-", "_").split("_")
    return "".join(word.capitalize() for word in words)


def _process_package_templates(
    pkg: resources.abc.Traversable,
    output_dir: Path,
    variables: dict[str, str],
) -> list[Path]:
    """Recursively process package templates to generate IDE support files.

    Copies template files from the package_templates resource, substituting
    {{variable}} placeholders with provided values.

    Args:
        pkg: Traversable resource pointing to templates directory.
        output_dir: Destination directory for processed files.
        variables: Variable substitutions for template placeholders.

    Returns:
        List of paths to created files.
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
    """Main entry point for the cfn-dataclasses CLI.

    Parses command-line arguments and dispatches to the appropriate
    subcommand handler (init, import, or lint).

    Args:
        argv: Command-line arguments. Defaults to sys.argv[1:].

    Returns:
        Exit code: 0 for success, 1 for errors.

    Example:
        >>> main(["init", "-o", "my_stack/"])
        0
    """
    parser = argparse.ArgumentParser(
        prog="cfn-dataclasses",
        description="CloudFormation dataclasses toolkit.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # import subcommand
    import_parser = subparsers.add_parser(
        "import",
        help="Import CloudFormation template to Python",
        description="Convert CloudFormation YAML/JSON templates to Python dataclasses.",
    )
    import_parser.add_argument(
        "input",
        metavar="INPUT",
        help='Template file path, directory (batch mode), or "-" for stdin',
    )
    import_parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        help="Output path: directory for package, .py file for single file, omit for stdout",
    )
    import_parser.add_argument(
        "--project-name",
        metavar="NAME",
        help="Project name (defaults to output directory name)",
    )
    import_parser.add_argument(
        "--no-main",
        action="store_true",
        help="Omit if __name__ == '__main__' block (single-file mode only)",
    )
    import_parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip validation and linting",
    )

    # init subcommand
    init_parser = subparsers.add_parser(
        "init",
        help="Create new project skeleton",
        description="Create an empty project structure ready for development.",
    )
    init_parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        required=True,
        help="Output directory for the project",
    )
    init_parser.add_argument(
        "--project-name",
        metavar="NAME",
        help="Project name (defaults to output directory name)",
    )

    # lint subcommand
    lint_parser = subparsers.add_parser(
        "lint",
        help="Lint Python code for style issues",
        description="Check cloudformation_dataclasses code for style issues and suggest fixes.",
    )
    lint_parser.add_argument(
        "path",
        metavar="PATH",
        help="File or directory to lint",
    )
    lint_parser.add_argument(
        "--fix",
        action="store_true",
        help="Auto-fix issues in place (default in watch mode)",
    )
    lint_parser.add_argument(
        "--no-fix",
        action="store_true",
        help="Disable auto-fix in watch mode",
    )
    lint_parser.add_argument(
        "--watch", "-w",
        action="store_true",
        help="Watch for changes and re-lint automatically (auto-fix enabled by default)",
    )
    lint_parser.add_argument(
        "--debounce",
        type=int,
        default=500,
        metavar="MS",
        help="Debounce delay in milliseconds (default: 500)",
    )
    lint_parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only show errors, not successful lints",
    )

    # split subcommand
    split_parser = subparsers.add_parser(
        "split",
        help="Split resource file into category files",
        description="Split a large resource file into category-based files (network.py, security.py, etc.).",
    )
    split_parser.add_argument(
        "file",
        metavar="FILE",
        help="Resource file to split",
    )
    split_parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview split without writing files",
    )
    split_parser.add_argument(
        "-o", "--output",
        metavar="DIR",
        help="Output directory (default: same as input file)",
    )

    # stubs subcommand
    stubs_parser = subparsers.add_parser(
        "stubs",
        help="Generate .pyi stub files for IDE support",
        description="Generate type stub files so Pylance/mypy understands dynamic imports.",
    )
    stubs_parser.add_argument(
        "path",
        metavar="PATH",
        nargs="?",
        default=".",
        help="Directory to scan (default: current directory)",
    )
    stubs_parser.add_argument(
        "--watch", "-w",
        action="store_true",
        help="Watch for changes and regenerate (requires watchdog)",
    )
    stubs_parser.add_argument(
        "--debounce",
        type=int,
        default=500,
        metavar="MS",
        help="Debounce delay in milliseconds (default: 500)",
    )
    stubs_parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only show errors during watch mode",
    )

    args = parser.parse_args(argv)

    # Show help if no command provided
    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "import":
            return _run_import_command(args)
        elif args.command == "init":
            return _run_init_command(args)
        elif args.command == "lint":
            return _run_lint_command(args)
        elif args.command == "split":
            return _run_split_command(args)
        elif args.command == "stubs":
            return _run_stubs_command(args)
    except CLIError as e:
        print(_format_cli_error(e), file=sys.stderr)
        return 1

    return 0


def _run_import_command(args: argparse.Namespace) -> int:
    """Handle the import subcommand.

    Determines whether to run single or batch import based on input type.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
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
        project_name_override=args.project_name,
    )


def _run_init_command(args: argparse.Namespace) -> int:
    """Handle the init subcommand.

    Creates an empty project skeleton using run_single_import with init_mode.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
    return run_single_import(
        input_arg="-",  # Will be overridden by init_mode
        output_arg=args.output,
        no_main=False,
        skip_checks=False,
        init_mode=True,
        project_name_override=args.project_name,
    )


def _run_lint_command(args: argparse.Namespace) -> int:
    """Handle the lint subcommand.

    Lints Python files for cloudformation_dataclasses style issues.
    Can auto-fix issues with --fix flag (default in watch mode).

    Args:
        args: Parsed command-line arguments.

    Returns:
        Exit code: 0 if no issues (or all fixed), 1 if issues found.
    """
    from cloudformation_dataclasses.linter import lint_file, fix_file
    from cloudformation_dataclasses.linter.split import write_split_files

    path = Path(args.path)

    if not path.exists():
        print(f"Error: Path not found: {path}", file=sys.stderr)
        return 1

    # In watch mode, --fix is enabled by default unless --no-fix is specified
    if args.watch and not args.no_fix:
        args.fix = True

    # Watch mode
    if args.watch:
        return _run_lint_watch(args, path)

    # One-shot mode
    return _run_lint_oneshot(args, path)


def _run_lint_watch(args: argparse.Namespace, path: Path) -> int:
    """Run lint command in watch mode.

    Args:
        args: Parsed command-line arguments.
        path: Path to watch.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
    from cloudformation_dataclasses.linter import lint_file, fix_file
    from cloudformation_dataclasses.watch import WatchConfig, DebouncedWatcher

    # Determine watch paths
    if path.is_file():
        watch_paths = [path.parent]
    else:
        watch_paths = [path]

    # Initial lint
    print(f"Linting {path}...")
    initial_result = _run_lint_oneshot(args, path)
    print("\nWatching for changes... (Ctrl+C to stop)")

    def on_file_change(file_path: Path) -> None:
        """Lint or fix the changed file."""
        from cloudformation_dataclasses.stubs import generate_stub_file

        if args.fix:
            try:
                original = file_path.read_text()
                fixed = fix_file(file_path, write=True)
                if fixed != original:
                    print(f"\u2713 Fixed {file_path.name}")
                    # Update __init__.py with any new intrinsics
                    updated_inits = _update_init_with_missing_intrinsics([file_path])
                    # Regenerate stubs for the package
                    package_dir = file_path.parent
                    if (package_dir / "__init__.py").exists():
                        generate_stub_file(package_dir)
                        if not args.quiet:
                            print(f"  \u2713 Regenerated stubs")
                elif not args.quiet:
                    print(f"\u2713 {file_path.name}")
            except Exception as e:
                print(f"\u2717 {file_path.name}: {e}")
        else:
            try:
                issues = lint_file(file_path)
                if issues:
                    print(f"\u26a0 {file_path.name}: {len(issues)} issue(s)")
                    for issue in issues[:5]:  # Show first 5 issues
                        print(f"  {issue.line}:{issue.column} {issue.rule_id} {issue.message}")
                    if len(issues) > 5:
                        print(f"  ... and {len(issues) - 5} more")
                elif not args.quiet:
                    print(f"\u2713 {file_path.name}")
            except SyntaxError as e:
                print(f"\u26a0 {file_path.name}: Syntax error: {e}")
            except Exception as e:
                print(f"\u2717 {file_path.name}: {e}")

    def on_error(file_path: Path, error: Exception) -> None:
        """Handle errors during linting."""
        if isinstance(error, SyntaxError):
            print(f"\u26a0 {file_path.name}: Syntax error: {error}")
        else:
            print(f"\u2717 {file_path.name}: {error}")

    config = WatchConfig(
        paths=watch_paths,
        patterns=["*.py"],
        ignored_patterns=["*.pyi", "__pycache__/*", "*.pyc"],
        debounce_ms=args.debounce,
    )

    try:
        watcher = DebouncedWatcher(
            config,
            callback=on_file_change,
            error_handler=on_error,
            quiet=args.quiet,
        )
        watcher.start()
    except ImportError as e:
        print(
            f"Error: {e}\n\n"
            "Install watchdog with:\n"
            "  pip install watchdog\n"
            "  # or\n"
            "  pip install cloudformation_dataclasses[stubs]",
            file=sys.stderr,
        )
        return 1
    except KeyboardInterrupt:
        pass

    print("\nStopped watching.")
    return 0


def _run_lint_oneshot(args: argparse.Namespace, path: Path) -> int:
    """Run lint command in one-shot mode.

    Args:
        args: Parsed command-line arguments.
        path: Path to lint.

    Returns:
        Exit code: 0 if no issues (or all fixed), 1 if issues found.
    """
    from cloudformation_dataclasses.linter import lint_file, fix_file
    from cloudformation_dataclasses.linter.split import write_split_files

    if path.is_file():
        # Single file
        files = [path]
    elif path.is_dir():
        # Check if it's our package structure
        if _is_package_structure(path):
            # Lint resource files directly in the package directory
            package_dir = _find_package_dir(path)
            if package_dir:
                # Find all .py files in the package that match the resources pattern
                files = [
                    f for f in package_dir.glob("*.py")
                    if f.name not in ("__init__.py", "config.py", "__main__.py")
                ]
            else:
                files = []
        else:
            # Scan all Python files recursively
            files = list(path.rglob("*.py"))
    else:
        print(f"Error: Invalid path: {path}", file=sys.stderr)
        return 1

    if not files:
        print("No Python files found to lint", file=sys.stderr)
        return 0

    total_issues = 0
    fixed_files_count = 0
    fixed_file_paths: list[Path] = []  # Track actual files that were fixed
    files_to_remove: list[Path] = []

    for file in sorted(files):
        if args.fix:
            # First check for CFD012 (file should be split)
            issues = lint_file(file)
            split_issue = next((i for i in issues if i.rule_id == "CFD012"), None)

            if split_issue:
                # Split the file
                split_results = write_split_files(file)
                if len(split_results) > 1:
                    fixed_files_count += 1
                    new_files = [p.name for p in split_results.values()]
                    print(f"Split {file} -> {', '.join(new_files)}")
                    # Mark original file for removal (only if it was actually split)
                    if file.name not in [p.name for p in split_results.values()]:
                        files_to_remove.append(file)
                    # Track the new files as fixed
                    fixed_file_paths.extend(split_results.values())
                    continue

            # Apply regular fixes
            original = file.read_text()
            fixed = fix_file(file, write=True)
            if fixed != original:
                fixed_files_count += 1
                fixed_file_paths.append(file)
                # Count issues fixed (rough estimate from line changes)
                issue_count = abs(len(fixed.splitlines()) - len(original.splitlines())) or 1
                print(f"Fixed {file} ({issue_count} issue(s))")
        else:
            issues = lint_file(file)
            total_issues += len(issues)
            for issue in issues:
                print(f"{file}:{issue.line}:{issue.column}: {issue.rule_id} {issue.message}")

    # Remove original files that were split
    for file in files_to_remove:
        file.unlink()
        print(f"Removed {file}")

    # Summary
    if args.fix:
        if fixed_files_count > 0:
            print(f"\nFixed {fixed_files_count} file(s)")
            # Update __init__.py with any new intrinsics used by fixed files
            _update_init_with_missing_intrinsics(fixed_file_paths)
            # Regenerate stubs for affected packages
            _regenerate_stubs_for_path(path)
        else:
            print("No issues to fix")
        return 0
    else:
        if total_issues > 0:
            print(f"\nFound {total_issues} issue(s)")
            return 1
        else:
            print("No issues found")
            return 0


def _regenerate_stubs_for_path(path: Path) -> None:
    """Regenerate .pyi stubs for packages under the given path.

    Args:
        path: Path to scan for stack packages.
    """
    from cloudformation_dataclasses.stubs import generate_stubs_for_path

    count = generate_stubs_for_path(path)
    if count > 0:
        print(f"Regenerated stubs for {count} package(s)")


def _update_init_with_missing_intrinsics(fixed_files: list[Path]) -> list[Path]:
    """Update __init__.py files with intrinsics used by fixed files.

    When CFD006 fixes files that use star imports (`from . import *`),
    it introduces intrinsic functions like GetAZs(), Select(), etc.
    These need to be exported from the package's __init__.py.

    This function scans fixed files for intrinsic function calls,
    checks if they're exported from __init__.py, and updates
    __init__.py to add the missing imports.

    Args:
        fixed_files: List of file paths that were fixed.

    Returns:
        List of __init__.py files that were updated.
    """
    import ast

    # Known intrinsic functions that might be introduced by CFD006
    KNOWN_INTRINSICS = {
        "Ref", "Sub", "Select", "Join", "GetAZs", "GetAtt", "If",
        "Equals", "And", "Or", "Not", "Base64", "Split", "ImportValue",
        "FindInMap", "Cidr",
    }

    updated_inits: list[Path] = []
    init_updates: dict[Path, set[str]] = {}  # __init__.py -> set of intrinsics to add

    for file_path in fixed_files:
        # Skip __init__.py files themselves
        if file_path.name == "__init__.py":
            continue

        # Check if file exists and uses star imports
        if not file_path.exists():
            continue

        source = file_path.read_text()
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue

        # Check for relative star imports
        has_star_import = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module is None and node.level > 0:
                    for alias in node.names:
                        if alias.name == "*":
                            has_star_import = True
                            break

        if not has_star_import:
            continue

        # Find intrinsic function calls in the file
        intrinsics_used: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in KNOWN_INTRINSICS:
                        intrinsics_used.add(node.func.id)

        if not intrinsics_used:
            continue

        # Find the package's __init__.py
        init_path = file_path.parent / "__init__.py"
        if not init_path.exists():
            continue

        # Check which intrinsics are already exported
        init_source = init_path.read_text()
        try:
            init_tree = ast.parse(init_source)
        except SyntaxError:
            continue

        # Get currently exported intrinsics from cloudformation_dataclasses.intrinsics
        current_exports: set[str] = set()
        for node in init_tree.body:
            if isinstance(node, ast.ImportFrom):
                if node.module == "cloudformation_dataclasses.intrinsics":
                    for alias in node.names:
                        current_exports.add(alias.name)

        # Find missing intrinsics
        missing = intrinsics_used - current_exports
        if missing:
            if init_path not in init_updates:
                init_updates[init_path] = set()
            init_updates[init_path].update(missing)

    # Apply updates to __init__.py files
    for init_path, missing_intrinsics in init_updates.items():
        _add_intrinsics_to_init(init_path, missing_intrinsics)
        updated_inits.append(init_path)
        print(f"Added {', '.join(sorted(missing_intrinsics))} to {init_path}")

    return updated_inits


def _add_intrinsics_to_init(init_path: Path, intrinsics: set[str]) -> None:
    """Add intrinsic function imports to an __init__.py file.

    Args:
        init_path: Path to __init__.py
        intrinsics: Set of intrinsic function names to add
    """
    import ast
    import re

    source = init_path.read_text()
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)

    # Find the existing import line from cloudformation_dataclasses.intrinsics
    existing_import_line = None
    existing_names: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            if node.module == "cloudformation_dataclasses.intrinsics":
                existing_import_line = node.lineno
                existing_names = [alias.name for alias in node.names]
                break

    if existing_import_line:
        # Update the existing import line
        old_line = lines[existing_import_line - 1]
        all_names = sorted(set(existing_names) | intrinsics)
        new_import = f"from cloudformation_dataclasses.intrinsics import {', '.join(all_names)}\n"
        lines[existing_import_line - 1] = new_import
    else:
        # Need to add a new import line
        # Find the last import line to insert after
        last_import_line = 0
        for node in tree.body:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                last_import_line = max(last_import_line, node.lineno)

        new_import = f"from cloudformation_dataclasses.intrinsics import {', '.join(sorted(intrinsics))}\n"
        if last_import_line > 0:
            lines.insert(last_import_line, new_import)
        else:
            lines.insert(0, new_import)

    # Also update __all__ if it exists
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, ast.List):
                        # Get current __all__ elements
                        current_all = []
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                current_all.append(elt.value)

                        # Add missing intrinsics to __all__
                        new_all = sorted(set(current_all) | intrinsics)
                        if new_all != current_all:
                            # Rebuild the __all__ line
                            # Try to preserve formatting
                            old_all_line = lines[node.lineno - 1]
                            all_items = ', '.join(f'"{name}"' for name in new_all)
                            if "\n" in old_all_line or len(all_items) > 60:
                                # Multi-line format
                                indent = "    "
                                all_lines = [f"{indent}\"{name}\",\n" for name in new_all]
                                new_all_str = f"__all__ = [\n{''.join(all_lines)}]\n"
                            else:
                                # Single line
                                new_all_str = f"__all__ = [{all_items}]\n"

                            # Replace the line(s) for __all__
                            end_line = node.end_lineno or node.lineno
                            # Remove old lines
                            del lines[node.lineno - 1:end_line]
                            # Insert new content
                            lines.insert(node.lineno - 1, new_all_str)
                    break

    init_path.write_text("".join(lines))


def _run_split_command(args: argparse.Namespace) -> int:
    """Handle the split subcommand.

    Splits a resource file into category-based files.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
    from cloudformation_dataclasses.linter.split import (
        print_split_preview,
        split_resource_file,
        write_split_files,
    )

    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        return 1

    if not file_path.is_file():
        print(f"Error: Not a file: {file_path}", file=sys.stderr)
        return 1

    source = file_path.read_text()

    if args.preview:
        print_split_preview(source, str(file_path))
        return 0

    # Determine output directory
    output_dir = Path(args.output) if args.output else file_path.parent

    # Split and write files
    split_files = split_resource_file(source)

    if len(split_files) == 1 and "main" in split_files:
        print(f"No split needed - file has few resources or all in same category")
        return 0

    # Write files
    for category, content in split_files.items():
        out_path = output_dir / f"{category}.py"
        out_path.write_text(content)
        print(f"Wrote {out_path}")

    # Regenerate stubs since exports may have changed
    from cloudformation_dataclasses.stubs import generate_stub_file

    if (output_dir / "__init__.py").exists():
        if generate_stub_file(output_dir):
            print(f"Regenerated {output_dir / '__init__.pyi'}")

    # Optionally remove original file if it was split
    if file_path.name not in [f"{cat}.py" for cat in split_files]:
        print(f"\nNote: Original file {file_path.name} can be removed if split is correct")

    return 0


def _run_stubs_command(args: argparse.Namespace) -> int:
    """Handle the stubs subcommand.

    Generates .pyi stub files for IDE type checking support.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
    from cloudformation_dataclasses.stubs import (
        generate_stubs_for_path,
        find_stack_packages,
        generate_stub_file,
    )

    path = Path(args.path).resolve()

    if not path.exists():
        print(f"Error: Path not found: {path}", file=sys.stderr)
        return 1

    if args.watch:
        # Watch mode - uses the reusable watch framework
        from cloudformation_dataclasses.watch import WatchConfig, DebouncedWatcher

        # Find all stack packages to watch
        stacks = find_stack_packages(path)
        if not stacks:
            print(f"No stack packages found in {path}", file=sys.stderr)
            return 1

        # Generate initial stubs
        count = generate_stubs_for_path(path)
        print(f"Generated stubs for {count} stack(s)")
        print("Watching for changes... (Ctrl+C to stop)")

        # Build list of directories to watch (parent of each stack)
        watch_paths = list({stack.parent for stack in stacks})

        def on_file_change(file_path: Path) -> None:
            """Regenerate stubs for the stack containing the changed file."""
            for stack in stacks:
                if stack in file_path.parents or file_path.parent == stack:
                    if generate_stub_file(stack):
                        if not args.quiet:
                            print(f"\u2713 {stack.parent.name}")
                    break

        def on_error(file_path: Path, error: Exception) -> None:
            """Handle errors during stub generation."""
            stack_name = file_path.parent.name
            if isinstance(error, SyntaxError):
                print(f"\u26a0 {stack_name}: Syntax error: {error}")
            else:
                print(f"\u2717 {stack_name}: {error}")

        config = WatchConfig(
            paths=watch_paths,
            patterns=["*.py"],
            ignored_patterns=["*.pyi", "__pycache__/*", "*.pyc"],
            debounce_ms=args.debounce,
        )

        try:
            watcher = DebouncedWatcher(
                config,
                callback=on_file_change,
                error_handler=on_error,
                quiet=args.quiet,
            )
            watcher.start()
        except ImportError as e:
            print(
                f"Error: {e}\n\n"
                "Install watchdog with:\n"
                "  pip install watchdog\n"
                "  # or\n"
                "  pip install cloudformation_dataclasses[stubs]",
                file=sys.stderr,
            )
            return 1
        except KeyboardInterrupt:
            pass

        print("\nStopped watching.")
        return 0

    else:
        # One-shot mode
        count = generate_stubs_for_path(path)
        if count == 0:
            print(f"No stack packages found in {path}", file=sys.stderr)
            return 1
        print(f"Generated stubs for {count} stack(s)")
        return 0


def _is_package_structure(path: Path) -> bool:
    """Check if path is a generated package structure.

    A valid package structure has pyproject.toml and a package directory
    containing an __init__.py with setup_resources pattern.

    Args:
        path: Directory path to check.

    Returns:
        True if path matches the generated package structure.
    """
    if not (path / "pyproject.toml").exists():
        return False
    for subdir in path.iterdir():
        if subdir.is_dir() and (subdir / "__init__.py").exists():
            init_file = subdir / "__init__.py"
            try:
                content = init_file.read_text()
                if "setup_resources" in content:
                    return True
            except Exception:
                pass
    return False


def _find_package_dir(path: Path) -> Path | None:
    """Find the package directory within a project structure.

    Args:
        path: Root project directory.

    Returns:
        Path to the package directory (containing __init__.py with setup_resources), or None.
    """
    for subdir in path.iterdir():
        if subdir.is_dir() and (subdir / "__init__.py").exists():
            init_file = subdir / "__init__.py"
            try:
                content = init_file.read_text()
                if "setup_resources" in content:
                    return subdir
            except Exception:
                pass
    return None


def run_single_import(
    input_arg: str,
    output_arg: str | None,
    no_main: bool = False,
    skip_checks: bool = False,
    attribution: Attribution | None = None,
    logger: logging.Logger | None = None,
    init_mode: bool = False,
    project_name_override: str | None = None,
) -> int:
    """Import a single CloudFormation template.

    Args:
        input_arg: Template file path or "-" for stdin
        output_arg: Output path (directory, .py file, or None for stdout)
        no_main: Omit if __name__ == '__main__' block
        skip_checks: Skip validation and linting
        attribution: Optional attribution info for README
        logger: Optional logger for batch mode
        init_mode: If True, create empty skeleton (ignore input_arg)
        project_name_override: Override project name (instead of deriving from output dir)

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
        if init_mode:
            # Create empty template for skeleton
            template = parse_template("{}", source_name="<init>")
        elif input_arg == "-":
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

            # Get project name (from override or output directory)
            project_name = project_name_override or output_dir.name

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

            # Copy original template to original/ subfolder (not in init mode)
            if not init_mode and input_arg != "-":
                original_dir = output_dir / "original"
                original_dir.mkdir(exist_ok=True)
                shutil.copy(input_path, original_dir / input_path.name)
                log(f"Generated: {original_dir / input_path.name}")

            # Always generate README with resource table
            if init_mode:
                source_file = None
            elif input_arg != "-":
                source_file = Path(input_arg).name
            else:
                source_file = "template"
            readme_path = output_dir / "README.md"
            readme_content = _generate_readme(
                project_name=project_name,
                source_file=source_file,
                template=template,
                attribution=attribution,
                init_mode=init_mode,
            )
            readme_path.write_text(readme_content)
            log(f"Generated: {readme_path}")

            # Generate .pyi stubs for IDE support
            from cloudformation_dataclasses.stubs import generate_stub_file

            package_dir = output_dir / project_name
            if generate_stub_file(package_dir):
                log(f"Generated: {package_dir / '__init__.pyi'}")

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
    source_file: str | None,
    template: IRTemplate,
    attribution: Attribution | None = None,
    init_mode: bool = False,
) -> str:
    """Generate README.md content for a generated package.

    Includes usage instructions, resource table, and optional attribution.

    Args:
        project_name: Name of the generated package.
        source_file: Original template filename (for attribution).
        template: Parsed IR template (for resource table).
        attribution: Optional attribution info from source repository.
        init_mode: If True, generate skeleton-appropriate text.

    Returns:
        Complete README.md content as a string.
    """
    lines = [f"# {_to_pascal_case(project_name)}", ""]

    # Attribution section
    if init_mode:
        lines.append("CloudFormation infrastructure as Python code.")
    elif attribution and attribution.source_url:
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
        "### Generate Template",
        "",
        "```bash",
        f"python -m {project_name}",
        "```",
        "",
        "### Validate Template",
        "",
        "```bash",
        f"python -m {project_name} --validate",
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


def run_batch_import(
    source_dir: Path,
    output_dir: Path,
    skip_checks: bool = False,
) -> int:
    """Import multiple CloudFormation templates from a directory.

    Args:
        source_dir: Directory containing template files
        output_dir: Output directory for generated packages
        skip_checks: Skip validation and linting

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
