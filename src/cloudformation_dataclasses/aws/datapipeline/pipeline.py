"""PropertyTypes for AWS::DataPipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Field(PropertyType):
    REF_VALUE = "RefValue"
    STRING_VALUE = "StringValue"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ref_value": "RefValue",
        "string_value": "StringValue",
        "key": "Key",
    }

    ref_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterAttribute(PropertyType):
    STRING_VALUE = "StringValue"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "string_value": "StringValue",
        "key": "Key",
    }

    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterObject(PropertyType):
    ATTRIBUTES = "Attributes"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes": "Attributes",
        "id": "Id",
    }

    attributes: Optional[list[ParameterAttribute]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterValue(PropertyType):
    ID = "Id"
    STRING_VALUE = "StringValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
        "string_value": "StringValue",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineObject(PropertyType):
    FIELDS = "Fields"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fields": "Fields",
        "id": "Id",
        "name": "Name",
    }

    fields: Optional[list[Field]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

