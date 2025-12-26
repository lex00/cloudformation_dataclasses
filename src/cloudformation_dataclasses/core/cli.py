"""
CLI utilities for generated CloudFormation packages.

This module provides the `run_package_cli()` function for auto-building templates
from the registry and outputting JSON/YAML.
"""

from __future__ import annotations

import argparse
import importlib
import sys
from typing import Callable

from cloudformation_dataclasses.core.template import Template


def run_package_cli(
    package_name: str,
    description: str = "",
    build_fn: Callable[[], Template] | None = None,
) -> None:
    """
    Run a CLI for a CloudFormation package.

    This function provides a standard CLI for generated packages:
    - `python -m package_name` -> output JSON (default)
    - `python -m package_name --yaml` -> output YAML
    - `python -m package_name --validate` -> run validation checks

    The function auto-builds a template from the registry using `Template.from_registry()`
    unless a custom `build_fn` is provided.

    Args:
        package_name: Name of the package (typically `__name__`)
        description: Template description (passed to Template.from_registry)
        build_fn: Optional custom build function that returns a Template.
                  If None, uses `Template.from_registry(description=description)`

    Example (default behavior):
        ```python
        # In package/__main__.py
        from cloudformation_dataclasses import run_package_cli
        run_package_cli(__name__, description="My infrastructure")
        ```

    Example (custom build):
        ```python
        # In package/__main__.py
        from cloudformation_dataclasses import run_package_cli, Template

        def build_template() -> Template:
            template = Template.from_registry(description="My infrastructure")
            # Custom logic here
            return template

        run_package_cli(__name__, build_fn=build_template)
        ```

    Exit Codes:
        0: Success
        1: Validation errors found (when using --validate)
        2: Template build failed (import error, etc.)
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description=f"Build CloudFormation template for {package_name}",
    )
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "--json",
        action="store_true",
        default=True,
        help="Output JSON format (default)",
    )
    output_group.add_argument(
        "--yaml",
        action="store_true",
        help="Output YAML format",
    )
    output_group.add_argument(
        "--validate",
        action="store_true",
        help="Run validation checks only (no output)",
    )

    args = parser.parse_args()

    # Import the calling package to trigger setup_resources()
    # This ensures all resources are registered before building the template
    try:
        importlib.import_module(package_name)
    except ImportError as e:
        print(f"Error: Failed to import package '{package_name}': {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error: Failed to initialize package '{package_name}': {e}", file=sys.stderr)
        sys.exit(2)

    # Build the template
    try:
        if build_fn is not None:
            template = build_fn()
        else:
            template = Template.from_registry(
                description=description,
                scope_package=package_name,
            )
    except Exception as e:
        print(f"Error: Failed to build template: {e}", file=sys.stderr)
        sys.exit(2)

    # Handle validation mode
    if args.validate:
        errors = template.validate()
        if errors:
            print("Validation errors found:", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            sys.exit(1)
        else:
            print("Validation passed: No errors found")
            sys.exit(0)

    # Output JSON or YAML
    try:
        if args.yaml:
            # Lazy import YAML - only load if needed
            try:
                output = template.to_yaml()
            except ImportError:
                print(
                    "Error: YAML output requires pyyaml. "
                    "Install it with: pip install cloudformation_dataclasses[yaml]",
                    file=sys.stderr,
                )
                sys.exit(2)
        else:
            # JSON is the default
            output = template.to_json()

        print(output)
    except Exception as e:
        print(f"Error: Failed to serialize template: {e}", file=sys.stderr)
        sys.exit(2)
