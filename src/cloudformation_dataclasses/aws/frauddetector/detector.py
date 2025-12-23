"""PropertyTypes for AWS::FraudDetector::Detector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EntityType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "created_time": "CreatedTime",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_types": "EntityTypes",
        "description": "Description",
        "created_time": "CreatedTime",
        "last_updated_time": "LastUpdatedTime",
        "labels": "Labels",
        "inline": "Inline",
        "event_variables": "EventVariables",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    entity_types: Optional[list[EntityType]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    labels: Optional[list[Label]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    event_variables: Optional[list[EventVariable]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventVariable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "description": "Description",
        "created_time": "CreatedTime",
        "variable_type": "VariableType",
        "data_type": "DataType",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
        "data_source": "DataSource",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variable_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Label(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "created_time": "CreatedTime",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Model(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Outcome(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "created_time": "CreatedTime",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "created_time": "CreatedTime",
        "language": "Language",
        "expression": "Expression",
        "rule_id": "RuleId",
        "detector_id": "DetectorId",
        "rule_version": "RuleVersion",
        "last_updated_time": "LastUpdatedTime",
        "arn": "Arn",
        "outcomes": "Outcomes",
        "tags": "Tags",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    detector_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    outcomes: Optional[list[Outcome]] = None
    tags: Optional[list[Tag]] = None

