"""PropertyTypes for AWS::Bedrock::AutomatedReasoningPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PolicyDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "types": "Types",
        "version": "Version",
        "rules": "Rules",
    }

    variables: Optional[list[PolicyDefinitionVariable]] = None
    types: Optional[list[PolicyDefinitionType]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[PolicyDefinitionRule]] = None


@dataclass
class PolicyDefinitionRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alternate_expression": "AlternateExpression",
        "expression": "Expression",
        "id": "Id",
    }

    alternate_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDefinitionType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "values": "Values",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[list[PolicyDefinitionTypeValue]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDefinitionTypeValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "value": "Value",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDefinitionVariable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

