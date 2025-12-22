"""PropertyTypes for AWS::CustomerProfiles::CalculatedAttributeDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeDetails(PropertyType):
    EXPRESSION = "Expression"
    ATTRIBUTES = "Attributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "attributes": "Attributes",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[list[AttributeItem]] = None


@dataclass
class AttributeItem(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Conditions(PropertyType):
    RANGE = "Range"
    OBJECT_COUNT = "ObjectCount"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "range": "Range",
        "object_count": "ObjectCount",
        "threshold": "Threshold",
    }

    range: Optional[Range] = None
    object_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    threshold: Optional[Threshold] = None


@dataclass
class Range(PropertyType):
    VALUE_RANGE = "ValueRange"
    TIMESTAMP_SOURCE = "TimestampSource"
    VALUE = "Value"
    TIMESTAMP_FORMAT = "TimestampFormat"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_range": "ValueRange",
        "timestamp_source": "TimestampSource",
        "value": "Value",
        "timestamp_format": "TimestampFormat",
        "unit": "Unit",
    }

    value_range: Optional[ValueRange] = None
    timestamp_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timestamp_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Readiness(PropertyType):
    MESSAGE = "Message"
    PROGRESS_PERCENTAGE = "ProgressPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "progress_percentage": "ProgressPercentage",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    progress_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Threshold(PropertyType):
    OPERATOR = "Operator"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValueRange(PropertyType):
    START = "Start"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end: Optional[Union[int, Ref, GetAtt, Sub]] = None

