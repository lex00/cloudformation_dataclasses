"""CloudFormation intrinsic functions and pseudo-parameters.

This module provides type-safe Python representations of CloudFormation intrinsic
functions and pseudo-parameters:

**Intrinsic Functions:**
- `Ref`, `GetAtt`: Reference resources and attributes
- `Sub`, `Join`: String manipulation
- `If`, `Equals`, `And`, `Or`, `Not`: Conditionals
- `Select`, `Split`, `FindInMap`: List and mapping operations
- `Base64`, `Cidr`, `GetAZs`: Utility functions

**Pseudo-Parameters:**
- `AWS_REGION`, `AWS_ACCOUNT_ID`, `AWS_STACK_NAME`, etc.

Example:
    >>> from cloudformation_dataclasses.intrinsics import Sub, Ref, AWS_REGION
    >>>
    >>> # String substitution with variable reference
    >>> arn = Sub("arn:aws:s3:::${BucketName}/*")
    >>> arn.to_dict()
    {'Fn::Sub': 'arn:aws:s3:::${BucketName}/*'}
    >>>
    >>> # Use pseudo-parameters
    >>> region_ref = Ref(AWS_REGION)
    >>> region_ref.to_dict()
    {'Ref': 'AWS::Region'}
"""

from cloudformation_dataclasses.intrinsics.functions import (
    And,
    Base64,
    Cidr,
    Condition,
    Equals,
    FindInMap,
    GetAtt,
    GetAZs,
    If,
    ImportValue,
    IntrinsicFunction,
    Join,
    Not,
    Or,
    Ref,
    Select,
    Split,
    Sub,
    Transform,
    ValueOf,
)
from cloudformation_dataclasses.intrinsics.pseudo import (
    AWS_ACCOUNT_ID,
    AWS_NO_VALUE,
    AWS_NOTIFICATION_ARNS,
    AWS_PARTITION,
    AWS_REGION,
    AWS_STACK_ID,
    AWS_STACK_NAME,
    AWS_URL_SUFFIX,
)

__all__ = [
    # Intrinsic functions
    "And",
    "Base64",
    "Cidr",
    "Condition",
    "Equals",
    "FindInMap",
    "GetAtt",
    "GetAZs",
    "If",
    "ImportValue",
    "IntrinsicFunction",
    "Join",
    "Not",
    "Or",
    "Ref",
    "Select",
    "Split",
    "Sub",
    "Transform",
    "ValueOf",
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
