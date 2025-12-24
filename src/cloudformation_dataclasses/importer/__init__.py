"""CloudFormation template importer - convert YAML/JSON to Python dataclasses.

This module provides tools to convert existing CloudFormation templates (YAML/JSON)
into Python code using cloudformation_dataclasses.

**Main Functions:**
- `parse_template`: Parse YAML/JSON into an intermediate representation (IR)
- `generate_code`: Generate Python code from a template or IR

**CLI Usage:**
    cfn-dataclasses import template.yaml -o output.py

Example:
    >>> from cloudformation_dataclasses.importer import parse_template, generate_code
    >>>
    >>> template_yaml = '''
    ... AWSTemplateFormatVersion: '2010-09-09'
    ... Resources:
    ...   MyBucket:
    ...     Type: AWS::S3::Bucket
    ...     Properties:
    ...       BucketName: my-bucket
    ... '''
    >>>
    >>> ir = parse_template(template_yaml)
    >>> code = generate_code(ir)
    >>> print(code)
"""

from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRCondition,
    IRIntrinsic,
    IRMapping,
    IROutput,
    IRParameter,
    IRProperty,
    IRResource,
    IRTemplate,
)
from cloudformation_dataclasses.importer.parser import parse_template
from cloudformation_dataclasses.importer.codegen import generate_code

__all__ = [
    "IntrinsicType",
    "IRCondition",
    "IRIntrinsic",
    "IRMapping",
    "IROutput",
    "IRParameter",
    "IRProperty",
    "IRResource",
    "IRTemplate",
    "generate_code",
    "parse_template",
]
