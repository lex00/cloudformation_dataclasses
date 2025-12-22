"""PropertyTypes for AWS::CustomerProfiles::ObjectType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FieldMap(PropertyType):
    NAME = "Name"
    OBJECT_TYPE_FIELD = "ObjectTypeField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "object_type_field": "ObjectTypeField",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_type_field: Optional[ObjectTypeField] = None


@dataclass
class KeyMap(PropertyType):
    OBJECT_TYPE_KEY_LIST = "ObjectTypeKeyList"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_type_key_list": "ObjectTypeKeyList",
        "name": "Name",
    }

    object_type_key_list: Optional[list[ObjectTypeKey]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectTypeField(PropertyType):
    TARGET = "Target"
    CONTENT_TYPE = "ContentType"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "content_type": "ContentType",
        "source": "Source",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectTypeKey(PropertyType):
    FIELD_NAMES = "FieldNames"
    STANDARD_IDENTIFIERS = "StandardIdentifiers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_names": "FieldNames",
        "standard_identifiers": "StandardIdentifiers",
    }

    field_names: Optional[Union[list[str], Ref]] = None
    standard_identifiers: Optional[Union[list[str], Ref]] = None

