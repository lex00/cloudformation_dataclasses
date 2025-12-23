"""PropertyTypes for AWS::CustomerProfiles::EventTrigger."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EventTriggerCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_trigger_dimensions": "EventTriggerDimensions",
        "logical_operator": "LogicalOperator",
    }

    event_trigger_dimensions: Optional[list[EventTriggerDimension]] = None
    logical_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventTriggerDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object_attributes": "ObjectAttributes",
    }

    object_attributes: Optional[list[ObjectAttribute]] = None


@dataclass
class EventTriggerLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "periods": "Periods",
        "event_expiration": "EventExpiration",
    }

    periods: Optional[list[Period]] = None
    event_expiration: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectAttribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "values": "Values",
        "field_name": "FieldName",
        "source": "Source",
    }

    comparison_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None
    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Period(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_invocations_per_profile": "MaxInvocationsPerProfile",
        "value": "Value",
        "unlimited": "Unlimited",
        "unit": "Unit",
    }

    max_invocations_per_profile: Optional[Union[int, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlimited: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None

