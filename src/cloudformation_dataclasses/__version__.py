"""
Version information for cloudformation_dataclasses package.

This module provides version information for:
- Package version (PyPI release version)
- CloudFormation spec version (AWS specification used)
- Generator version (code generator version)
"""

from cloudformation_dataclasses.codegen.config import (
    CLOUDFORMATION_SPEC_VERSION,
    GENERATOR_VERSION,
    COMBINED_VERSION,
)

# Package version (from pyproject.toml)
__version__ = "0.1.0"

# CloudFormation spec and generator versions
__cf_spec_version__ = CLOUDFORMATION_SPEC_VERSION
__generator_version__ = GENERATOR_VERSION
__combined_version__ = COMBINED_VERSION


def get_version_info() -> dict[str, str]:
    """
    Get comprehensive version information.

    Returns:
        Dictionary with version information
    """
    return {
        "package": __version__,
        "cf_spec": __cf_spec_version__,
        "generator": __generator_version__,
        "combined": __combined_version__,
    }


def print_version_info() -> None:
    """Print formatted version information."""
    print("cloudformation_dataclasses version information:")
    print(f"  Package version: {__version__}")
    print(f"  CloudFormation spec: {__cf_spec_version__}")
    print(f"  Generator version: {__generator_version__}")
    print(f"  Combined: {__combined_version__}")
    print(f"\nGenerated resources:")
    print(f"  - AWS S3 (10 resources)")
    print(f"\nTo generate more services:")
    print(f"  uv run python -m cloudformation_dataclasses.codegen.generator --service <SERVICE>")


if __name__ == "__main__":
    print_version_info()
