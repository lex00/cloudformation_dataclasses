"""
cloudformation_dataclasses - Python dataclasses for AWS CloudFormation template synthesis.

A pure Python library that uses dataclasses as a declarative interface for AWS CloudFormation
template generation. Zero runtime dependencies, fully type-safe, IDE-friendly.

Version Information:
  Package: 0.2.1
  CloudFormation Spec: 227.0.0
  Generator: 1.0.0
  Combined: spec-227.0.0_gen-1.0.0

Available Resources:
  - All 262 AWS services (1,502 resource types)

To see version info:
  >>> from cloudformation_dataclasses import __version__
  >>> print(__version__)
  '0.2.1'

  >>> from cloudformation_dataclasses.__version__ import print_version_info
  >>> print_version_info()
"""

from cloudformation_dataclasses.__version__ import (
    __version__,
    __cf_spec_version__,
    __generator_version__,
    __combined_version__,
    get_version_info,
    print_version_info,
)

__all__ = [
    "__version__",
    "__cf_spec_version__",
    "__generator_version__",
    "__combined_version__",
    "get_version_info",
    "print_version_info",
]
