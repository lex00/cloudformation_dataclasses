"""Python code generation from IR.

This package provides functions to generate Python source code from
CloudFormation templates represented as IR (intermediate representation).

Public API:
- generate_code(): Generate a single Python file from a template
- generate_package(): Generate a multi-file Python package from a template
"""

from .package import generate_code, generate_package

__all__ = [
    "generate_code",
    "generate_package",
]
