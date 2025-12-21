"""Command-line interface for cfn-import."""

import argparse
import re
import sys
from importlib import resources
from pathlib import Path

from cloudformation_dataclasses import __version__
from cloudformation_dataclasses.importer.codegen import generate_code, generate_package
from cloudformation_dataclasses.importer.parser import parse_template


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
    Main entry point for cfn-import command.

    Args:
        argv: Command line arguments (default: sys.argv[1:])

    Returns:
        Exit code (0 for success)
    """
    parser = argparse.ArgumentParser(
        prog="cfn-import",
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
        "-m",
        "--mode",
        choices=["block", "mixed"],
        default="block",
        help="Output mode: block (declarative classes), mixed (inline dicts for properties) (default: block)",
    )

    parser.add_argument(
        "--no-main",
        action="store_true",
        help="Omit if __name__ == '__main__' block (single-file mode only)",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args(argv)

    # Determine output mode from -o path
    # - No -o or "-": stdout -> single file
    # - Ends with .py: single file
    # - Otherwise: package (directory)
    if args.output is None or args.output == "-":
        use_package = False
    elif args.output.endswith(".py"):
        use_package = False
    else:
        use_package = True

    try:
        # Parse input
        if args.input == "-":
            content = sys.stdin.read()
            template = parse_template(content, source_name="<stdin>")
        else:
            input_path = Path(args.input)
            if not input_path.exists():
                print(f"Error: File not found: {args.input}", file=sys.stderr)
                return 1
            template = parse_template(input_path)

        if use_package:
            # Generate package (multiple files)
            files = generate_package(
                template,
                mode=args.mode,
            )

            # Write files to output directory
            output_dir = Path(args.output)
            output_dir.mkdir(parents=True, exist_ok=True)

            for filename, file_content in files.items():
                file_path = output_dir / filename
                # Create parent directories if needed (e.g., for resources/foo.py)
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(file_content)
                print(f"Generated: {file_path}", file=sys.stderr)

            # Generate IDE support files from shared package templates
            project_name = output_dir.name
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
                print(f"Generated: {file_path}", file=sys.stderr)

        else:
            # Generate single file
            code = generate_code(
                template, mode=args.mode, include_main=not args.no_main
            )

            # Output
            if args.output and args.output != "-":
                output_path = Path(args.output)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(code)
                print(f"Generated: {args.output}", file=sys.stderr)
            else:
                print(code)

        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
