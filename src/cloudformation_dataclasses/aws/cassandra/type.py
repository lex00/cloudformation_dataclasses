"""PropertyTypes for AWS::Cassandra::Type."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Field(PropertyType):
    FIELD_NAME = "FieldName"
    FIELD_TYPE = "FieldType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_name": "FieldName",
        "field_type": "FieldType",
    }

    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

