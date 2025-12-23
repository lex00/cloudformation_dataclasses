"""PropertyTypes for AWS::Connect::DataTableAttribute."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Enum(PropertyType):
    STRICT = "Strict"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "strict": "Strict",
        "values": "Values",
    }

    strict: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class LockVersion(PropertyType):
    DATA_TABLE = "DataTable"
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_table": "DataTable",
        "attribute": "Attribute",
    }

    data_table: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Validation(PropertyType):
    EXCLUSIVE_MINIMUM = "ExclusiveMinimum"
    ENUM = "Enum"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    EXCLUSIVE_MAXIMUM = "ExclusiveMaximum"
    MIN_LENGTH = "MinLength"
    MAX_VALUES = "MaxValues"
    MAX_LENGTH = "MaxLength"
    MIN_VALUES = "MinValues"
    MULTIPLE_OF = "MultipleOf"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclusive_minimum": "ExclusiveMinimum",
        "enum": "Enum",
        "minimum": "Minimum",
        "maximum": "Maximum",
        "exclusive_maximum": "ExclusiveMaximum",
        "min_length": "MinLength",
        "max_values": "MaxValues",
        "max_length": "MaxLength",
        "min_values": "MinValues",
        "multiple_of": "MultipleOf",
    }

    exclusive_minimum: Optional[Union[float, Ref, GetAtt, Sub]] = None
    enum: Optional[Enum] = None
    minimum: Optional[Union[float, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[float, Ref, GetAtt, Sub]] = None
    exclusive_maximum: Optional[Union[float, Ref, GetAtt, Sub]] = None
    min_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_values: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_values: Optional[Union[int, Ref, GetAtt, Sub]] = None
    multiple_of: Optional[Union[float, Ref, GetAtt, Sub]] = None

