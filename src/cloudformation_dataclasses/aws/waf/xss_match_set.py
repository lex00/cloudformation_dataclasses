"""PropertyTypes for AWS::WAF::XssMatchSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FieldToMatch(PropertyType):
    DATA = "Data"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data": "Data",
        "type_": "Type",
    }

    data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, MatchFieldType, Ref, GetAtt, Sub]] = None


@dataclass
class XssMatchTuple(PropertyType):
    FIELD_TO_MATCH = "FieldToMatch"
    TEXT_TRANSFORMATION = "TextTransformation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_to_match": "FieldToMatch",
        "text_transformation": "TextTransformation",
    }

    field_to_match: Optional[FieldToMatch] = None
    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None

