"""CLI for skeleton generator (cfn-dataclasses-init command)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .generator import generate_skeleton, list_skeletons


def main(argv: list[str] | None = None) -> int:
    """Main entry point for cfn-dataclasses-init CLI.

    Args:
        argv: Command line arguments (defaults to sys.argv[1:]).

    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    parser = argparse.ArgumentParser(
        prog="cfn-dataclasses-init",
        description="Generate a new cloudformation_dataclasses project skeleton.",
        epilog="Example: cfn-dataclasses-init s3-bucket -o my_project/",
    )

    parser.add_argument(
        "skeleton",
        nargs="?",
        help="Skeleton template to use (e.g., s3-bucket, s3_bucket)",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output directory (required unless --list)",
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List available skeleton templates",
    )

    parser.add_argument(
        "--project-name",
        default="my_project",
        help="Project name for naming pattern (default: my_project)",
    )

    parser.add_argument(
        "--component",
        default="MyComponent",
        help="Component name (default: MyComponent)",
    )

    parser.add_argument(
        "--stage",
        default="dev",
        help="Deployment stage (default: dev)",
    )

    parser.add_argument(
        "--region",
        default="us-east-1",
        help="AWS region (default: us-east-1)",
    )

    args = parser.parse_args(argv)

    # Handle --list
    if args.list:
        skeletons = list_skeletons()
        if not skeletons:
            print("No skeletons available.")
            return 0

        print("Available skeletons:\n")
        for skeleton in skeletons:
            print(f"  {skeleton.name}")
            print(f"      {skeleton.description}\n")
        return 0

    # Validate required arguments
    if not args.skeleton:
        parser.error("skeleton name is required (or use --list to see available)")

    if not args.output:
        parser.error("-o/--output is required")

    # Check if output directory exists and is not empty
    if args.output.exists():
        if any(args.output.iterdir()):
            print(f"Error: Output directory {args.output} is not empty.", file=sys.stderr)
            return 1

    # Generate skeleton
    try:
        created = generate_skeleton(
            skeleton_name=args.skeleton,
            output_dir=args.output,
            project_name=args.project_name,
            component=args.component,
            stage=args.stage,
            region=args.region,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Report success
    print(f"Created {args.output}/ with {len(created)} files:")
    for path in sorted(created):
        print(f"  {path.name}")

    print(f"\nNext steps:")
    print(f"  1. Edit {args.output}/context.py to configure your deployment")
    print(f"  2. Customize resources in {args.output}/bucket.py")
    print(f"  3. Run: python -m {args.output.name}.main")

    return 0


if __name__ == "__main__":
    sys.exit(main())
