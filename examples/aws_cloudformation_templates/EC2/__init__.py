"""EC2 CloudFormation template examples."""

from cloudformation_dataclasses.aws.ec2 import (
    # Resources
    EIP,
    EIPAssociation,
    Instance,
    Ingress,
    SecurityGroup,
)
from cloudformation_dataclasses.aws.cloudformation import (
    WaitCondition,
    WaitConditionHandle,
)
from cloudformation_dataclasses.core import (
    # Parameter types
    STRING,
    ParameterType,
    # Core constructs
    Output,
    Parameter,
    Tag,
    Template,
    cloudformation_dataclass,
    ref,
    get_att,
)
from cloudformation_dataclasses.intrinsics import (
    Base64,
    Join,
    Select,
    Sub,
    AWS_REGION,
    AWS_STACK_ID,
    AWS_STACK_NAME,
)

__all__ = [
    # Resources
    "EIP",
    "EIPAssociation",
    "Instance",
    "Ingress",
    "SecurityGroup",
    "WaitCondition",
    "WaitConditionHandle",
    # Core
    "Output",
    "Parameter",
    "ParameterType",
    "STRING",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "get_att",
    "ref",
    # Intrinsics
    "Base64",
    "Join",
    "Select",
    "Sub",
    "AWS_REGION",
    "AWS_STACK_ID",
    "AWS_STACK_NAME",
]
