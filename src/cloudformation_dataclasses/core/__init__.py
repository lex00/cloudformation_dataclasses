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
    IpProtocol,
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
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    AWS_NO_VALUE,
    AWS_NOTIFICATION_ARNS,
    AWS_PARTITION,
    AWS_REGION,
    AWS_STACK_ID,
    AWS_STACK_NAME,
    AWS_URL_SUFFIX,
    Base64,
    Cidr,
    FindInMap,
    GetAZs,
    If,
    ImportValue,
    Join,
    Select,
    Split,
    Sub,
    Transform,
)

__all__ = [
    # Constants
    "ARN",
    "ARN_EQUALS",
    "ARN_LIKE",
    "BOOL",
    "IP_ADDRESS",
    "NUMBER",
    "STRING",
    "STRING_EQUALS",
    "STRING_LIKE",
    "STRING_NOT_EQUALS",
    "STRING_NOT_LIKE",
    # Enums
    "ConditionOperator",
    "IpProtocol",
    "ParameterType",
    # Core classes
    "CloudFormationResource",
    "Condition",
    "DenyStatement",
    "Mapping",
    "Output",
    "Parameter",
    "PolicyDocument",
    "PolicyStatement",
    "ResourceRegistry",
    "Tag",
    "Template",
    # Decorators and helpers
    "cloudformation_dataclass",
    "get_att",
    "ref",
    "registry",
    "setup_resources",
    # Type wrappers
    "GetAtt",
    "Ref",
    # Intrinsic functions
    "Base64",
    "Cidr",
    "FindInMap",
    "GetAZs",
    "If",
    "ImportValue",
    "Join",
    "Select",
    "Split",
    "Sub",
    "Transform",
    # Pseudo-parameters
    "AWS_ACCOUNT_ID",
    "AWS_NO_VALUE",
    "AWS_NOTIFICATION_ARNS",
    "AWS_PARTITION",
    "AWS_REGION",
    "AWS_STACK_ID",
    "AWS_STACK_NAME",
    "AWS_URL_SUFFIX",
]
