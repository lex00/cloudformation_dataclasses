"""PropertyTypes for AWS::SecurityHub::SecurityControl."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ParameterConfiguration(PropertyType):
    VALUE_TYPE = "ValueType"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "value": "Value",
    }

    value_type: Optional[Union[str, ParameterValueType, Ref, GetAtt, Sub]] = None
    value: Optional[ParameterValue] = None


@dataclass
class ParameterValue(PropertyType):
    ENUM = "Enum"
    INTEGER = "Integer"
    STRING_LIST = "StringList"
    ENUM_LIST = "EnumList"
    INTEGER_LIST = "IntegerList"
    STRING = "String"
    BOOLEAN = "Boolean"
    DOUBLE = "Double"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enum": "Enum",
        "integer": "Integer",
        "string_list": "StringList",
        "enum_list": "EnumList",
        "integer_list": "IntegerList",
        "string": "String",
        "boolean": "Boolean",
        "double": "Double",
    }

    enum: Optional[Union[str, Ref, GetAtt, Sub]] = None
    integer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    string_list: Optional[Union[list[str], Ref]] = None
    enum_list: Optional[Union[list[str], Ref]] = None
    integer_list: Optional[Union[list[int], Ref]] = None
    string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    boolean: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    double: Optional[Union[float, Ref, GetAtt, Sub]] = None

