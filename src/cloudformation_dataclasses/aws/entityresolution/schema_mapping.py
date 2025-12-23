"""PropertyTypes for AWS::EntityResolution::SchemaMapping."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SchemaInputAttribute(PropertyType):
    GROUP_NAME = "GroupName"
    TYPE = "Type"
    SUB_TYPE = "SubType"
    HASHED = "Hashed"
    MATCH_KEY = "MatchKey"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "type_": "Type",
        "sub_type": "SubType",
        "hashed": "Hashed",
        "match_key": "MatchKey",
        "field_name": "FieldName",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hashed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    match_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

