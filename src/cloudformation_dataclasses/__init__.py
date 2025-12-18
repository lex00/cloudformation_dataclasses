"""
cloudformation_dataclasses - Python dataclasses for AWS CloudFormation template synthesis.

A pure Python library that uses dataclasses as a declarative interface for AWS CloudFormation
template generation. Zero runtime dependencies, fully type-safe, IDE-friendly.

Version Information:
  Package: 0.3.2
  CloudFormation Spec Date: 2025.12.11 (from AWS Last-Modified header)
  Generator: 1.0.0
  Combined: spec-2025.12.11_gen-1.0.0

Available Resources:
  - All 262 AWS services (1,502 resource types)

To see version info:
  >>> from cloudformation_dataclasses import __version__
  >>> print(__version__)
  '0.3.2'

  >>> from cloudformation_dataclasses.__version__ import print_version_info
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
