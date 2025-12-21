"""Command-line interface for cfn-import."""

import argparse
import sys
from pathlib import Path

from cloudformation_dataclasses import __version__
from cloudformation_dataclasses.importer.codegen import generate_code, generate_package
from cloudformation_dataclasses.importer.parser import parse_template


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
