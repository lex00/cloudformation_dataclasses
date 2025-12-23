"""PropertyTypes for AWS::Connect::TaskTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Constraints(PropertyType):
    READ_ONLY_FIELDS = "ReadOnlyFields"
    INVISIBLE_FIELDS = "InvisibleFields"
    REQUIRED_FIELDS = "RequiredFields"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only_fields": "ReadOnlyFields",
        "invisible_fields": "InvisibleFields",
        "required_fields": "RequiredFields",
    }

    read_only_fields: Optional[list[ReadOnlyFieldInfo]] = None
    invisible_fields: Optional[list[InvisibleFieldInfo]] = None
    required_fields: Optional[list[RequiredFieldInfo]] = None


@dataclass
class DefaultFieldValue(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "id": "Id",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[FieldIdentifier] = None


@dataclass
class Field(PropertyType):
    TYPE = "Type"
    DESCRIPTION = "Description"
    ID = "Id"
    SINGLE_SELECT_OPTIONS = "SingleSelectOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "id": "Id",
        "single_select_options": "SingleSelectOptions",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[FieldIdentifier] = None
    single_select_options: Optional[Union[list[str], Ref]] = None


@dataclass
class FieldIdentifier(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InvisibleFieldInfo(PropertyType):
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[FieldIdentifier] = None


@dataclass
class ReadOnlyFieldInfo(PropertyType):
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[FieldIdentifier] = None


@dataclass
class RequiredFieldInfo(PropertyType):
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[FieldIdentifier] = None

