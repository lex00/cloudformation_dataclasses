"""PropertyTypes for AWS::WAFRegional::XssMatchSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FieldToMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "data": "Data",
    }

    type_: Optional[Union[str, MatchFieldType, Ref, GetAtt, Sub]] = None
    data: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class XssMatchTuple(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformation": "TextTransformation",
        "field_to_match": "FieldToMatch",
    }

    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None

