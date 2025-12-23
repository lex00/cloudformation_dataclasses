"""PropertyTypes for AWS::CustomerProfiles::ObjectType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FieldMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "object_type_field": "ObjectTypeField",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_type_field: Optional[ObjectTypeField] = None


@dataclass
class KeyMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object_type_key_list": "ObjectTypeKeyList",
        "name": "Name",
    }

    object_type_key_list: Optional[list[ObjectTypeKey]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectTypeField(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_names": "FieldNames",
        "standard_identifiers": "StandardIdentifiers",
    }

    field_names: Optional[Union[list[str], Ref]] = None
    standard_identifiers: Optional[Union[list[str], Ref]] = None

