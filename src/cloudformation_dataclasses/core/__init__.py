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
    ALL,
    B,
    HASH,
    INCLUDE,
    KEYS_ONLY,
    N,
    NUMBER,
    RANGE,
    S,
    STRING,
    AttributeType,
    KeyType,
    ParameterType,
    ProjectionType,
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
    "ALL",
    "AttributeType",
    "B",
    "CloudFormationResource",
    "Condition",
    "DenyStatement",
    "DeploymentContext",
    "HASH",
    "INCLUDE",
    "KEYS_ONLY",
    "KeyType",
    "Mapping",
    "N",
    "NUMBER",
    "Output",
    "Parameter",
    "ParameterType",
    "PolicyDocument",
    "PolicyStatement",
    "ProjectionType",
    "RANGE",
    "S",
    "STRING",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "get_att",
    "ref",
]
