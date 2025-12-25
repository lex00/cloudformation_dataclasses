"""Core CloudFormation resource base classes and utilities.

This module provides the foundation for building CloudFormation templates:

- `Template`: The main container for CloudFormation resources
- `CloudFormationResource`: Base class for all AWS resources
- `Parameter`, `Output`, `Condition`, `Mapping`: Template components
- `Ref`, `GetAtt`: Resource reference helpers
- `@cloudformation_dataclass`: Decorator for defining resources

Example:
    >>> from cloudformation_dataclasses.core import Template, Parameter, Output
    >>> from cloudformation_dataclasses.aws.s3 import Bucket
    >>>
    >>> template = Template(description="My S3 Template")
    >>> template.add_parameter("BucketName", Parameter(type="String"))
    >>> template.add_resource("MyBucket", Bucket(bucket_name="my-bucket"))
    >>> print(template.to_yaml())
"""

from cloudformation_dataclasses.core.base import (
    CloudFormationResource,
    DenyStatement,
    PolicyDocument,
    PolicyStatement,
    Tag,
)
from cloudformation_dataclasses.core.constants import (
    ARN,
    ARN_EQUALS,
    ARN_LIKE,
    BOOL,
    IP_ADDRESS,
    NUMBER,
    STRING,
    STRING_EQUALS,
    STRING_LIKE,
    STRING_NOT_EQUALS,
    STRING_NOT_LIKE,
    ConditionOperator,
    ParameterType,
)
from cloudformation_dataclasses.core.registry import ResourceRegistry, registry
from cloudformation_dataclasses.core.template import (
    Condition,
    Mapping,
    Output,
    Parameter,
    Template,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.core.wrapper import (
    GetAtt,
    Ref,
    cloudformation_dataclass,
    get_att,
    ref,
)

__all__ = [
    "ARN",
    "ARN_EQUALS",
    "ARN_LIKE",
    "BOOL",
    "CloudFormationResource",
    "Condition",
    "ConditionOperator",
    "DenyStatement",
    "GetAtt",
    "IP_ADDRESS",
    "Mapping",
    "NUMBER",
    "Output",
    "Parameter",
    "ParameterType",
    "PolicyDocument",
    "PolicyStatement",
    "Ref",
    "ResourceRegistry",
    "STRING",
    "STRING_EQUALS",
    "STRING_LIKE",
    "STRING_NOT_EQUALS",
    "STRING_NOT_LIKE",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "get_att",
    "ref",
    "registry",
    "setup_resources",
]
