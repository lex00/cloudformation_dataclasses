"""
cloudformation_dataclasses - Python dataclasses for AWS CloudFormation template synthesis.

A pure Python library that uses dataclasses as a declarative interface for AWS CloudFormation
template generation. Zero runtime dependencies, fully type-safe, IDE-friendly.

To see version info:
  >>> from cloudformation_dataclasses import __version__, print_version_info
  >>> print(__version__)
  >>> print_version_info()
"""

from cloudformation_dataclasses.__version__ import (
    __version__,
    __cf_spec_date__,
    __cf_spec_version__,  # Legacy alias
    __generator_version__,
    __combined_version__,
    get_version_info,
    print_version_info,
)

__all__ = [
    "__version__",
    "__cf_spec_date__",
    "__cf_spec_version__",  # Legacy alias
    "__generator_version__",
    "__combined_version__",
    "get_version_info",
    "print_version_info",
]
