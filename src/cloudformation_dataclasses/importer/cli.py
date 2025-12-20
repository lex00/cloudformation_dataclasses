"""Command-line interface for cfn-import."""

import argparse
import sys
from pathlib import Path

from cloudformation_dataclasses import __version__
from cloudformation_dataclasses.importer.codegen import generate_code
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
        help="Output file path (default: stdout)",
    )

    parser.add_argument(
        "-m",
        "--mode",
        choices=["block", "brief", "mixed"],
        default="block",
        help="Output mode: block (declarative classes), brief (imperative), mixed (default: block)",
    )

    parser.add_argument(
        "--no-main",
        action="store_true",
        help="Omit if __name__ == '__main__' block",
    )

    lint_group = parser.add_mutually_exclusive_group()
    lint_group.add_argument(
        "--lint",
        action="store_true",
        dest="lint",
        default=True,
        help="Run linter on generated code to use type-safe constants (default: enabled)",
    )
    lint_group.add_argument(
        "--no-lint",
        action="store_false",
        dest="lint",
        help="Disable linter (output raw generated code)",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args(argv)

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

        # Generate code
        code = generate_code(
            template, mode=args.mode, include_main=not args.no_main, lint=args.lint
        )

        # Output
        if args.output:
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
