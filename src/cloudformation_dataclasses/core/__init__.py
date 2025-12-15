"""Core CloudFormation resource base classes and utilities."""

from cloudformation_dataclasses.core.base import (
    CloudFormationResource,
    DenyStatement,
    DeploymentContext,
    PolicyDocument,
    PolicyStatement,
    Tag,
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
    "CloudFormationResource",
    "Condition",
    "DenyStatement",
    "DeploymentContext",
    "Mapping",
    "Output",
    "Parameter",
    "PolicyDocument",
    "PolicyStatement",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "get_att",
    "ref",
]
