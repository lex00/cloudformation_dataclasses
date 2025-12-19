"""Core CloudFormation resource base classes and utilities."""

from cloudformation_dataclasses.core.base import (
    CloudFormationResource,
    DenyStatement,
    DeploymentContext,
    PolicyDocument,
    PolicyStatement,
    Tag,
)
from cloudformation_dataclasses.core.constants import (
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
from cloudformation_dataclasses.core.template import (
    Condition,
    Mapping,
    Output,
    Parameter,
    Template,
)
from cloudformation_dataclasses.core.wrapper import (
    cloudformation_dataclass,
    get_att,
    ref,
)

__all__ = [
    "ARN_EQUALS",
    "ARN_LIKE",
    "BOOL",
    "CloudFormationResource",
    "Condition",
    "ConditionOperator",
    "DenyStatement",
    "DeploymentContext",
    "IP_ADDRESS",
    "Mapping",
    "NUMBER",
    "Output",
    "Parameter",
    "ParameterType",
    "PolicyDocument",
    "PolicyStatement",
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
]
