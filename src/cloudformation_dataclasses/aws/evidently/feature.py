"""PropertyTypes for AWS::Evidently::Feature."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EntityOverride(PropertyType):
    ENTITY_ID = "EntityId"
    VARIATION = "Variation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id": "EntityId",
        "variation": "Variation",
    }

    entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variation: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VariationObject(PropertyType):
    VARIATION_NAME = "VariationName"
    DOUBLE_VALUE = "DoubleValue"
    BOOLEAN_VALUE = "BooleanValue"
    LONG_VALUE = "LongValue"
    STRING_VALUE = "StringValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variation_name": "VariationName",
        "double_value": "DoubleValue",
        "boolean_value": "BooleanValue",
        "long_value": "LongValue",
        "string_value": "StringValue",
    }

    variation_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    double_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    boolean_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    long_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None

