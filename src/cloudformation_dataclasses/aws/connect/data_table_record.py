"""PropertyTypes for AWS::Connect::DataTableRecord."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataTableRecord(PropertyType):
    PRIMARY_VALUES = "PrimaryValues"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_values": "PrimaryValues",
        "values": "Values",
    }

    primary_values: Optional[list[Value]] = None
    values: Optional[list[Value]] = None


@dataclass
class Value(PropertyType):
    ATTRIBUTE_VALUE = "AttributeValue"
    ATTRIBUTE_ID = "AttributeId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_value": "AttributeValue",
        "attribute_id": "AttributeId",
    }

    attribute_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

