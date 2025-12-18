"""
Version information for cloudformation_dataclasses package.

This module provides version information for:
- Package version (PyPI release version)
- CloudFormation spec date (YYYY.MM.DD from AWS Last-Modified header)
- Generator version (code generator version)
"""

from cloudformation_dataclasses.codegen.config import (
    CLOUDFORMATION_SPEC_DATE,
    GENERATOR_VERSION,
    COMBINED_VERSION,
)

# Package version (from pyproject.toml)
__version__ = "0.3.2"

# CloudFormation spec and generator versions
__cf_spec_date__ = CLOUDFORMATION_SPEC_DATE
__generator_version__ = GENERATOR_VERSION
__combined_version__ = COMBINED_VERSION

# Legacy alias for backwards compatibility
__cf_spec_version__ = CLOUDFORMATION_SPEC_DATE


def get_version_info() -> dict[str, str]:
    """
    Get comprehensive version information.

    Returns:
        Dictionary with version information
    """
    return {
        "package": __version__,
        "cf_spec_date": __cf_spec_date__,
        "generator": __generator_version__,
        "combined": __combined_version__,
    }


def print_version_info() -> None:
    """Print formatted version information."""
    print("cloudformation_dataclasses version information:")
    print(f"  Package version: {__version__}")
    print(f"  CloudFormation spec date: {__cf_spec_date__}")
    print(f"  Generator version: {__generator_version__}")
    print(f"  Combined: {__combined_version__}")
    print("\nGenerated resources:")
    print("  - All 262 AWS services (1,502 resource types)")


if __name__ == "__main__":
    print_version_info()
