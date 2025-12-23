"""PropertyTypes for AWS::WAFRegional::ByteMatchSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ByteMatchTuple(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_string": "TargetString",
        "target_string_base64": "TargetStringBase64",
        "positional_constraint": "PositionalConstraint",
        "text_transformation": "TextTransformation",
        "field_to_match": "FieldToMatch",
    }

    target_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_string_base64: Optional[Union[str, Ref, GetAtt, Sub]] = None
    positional_constraint: Optional[Union[str, PositionalConstraint, Ref, GetAtt, Sub]] = None
    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None


@dataclass
class FieldToMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "data": "Data",
    }

    type_: Optional[Union[str, MatchFieldType, Ref, GetAtt, Sub]] = None
    data: Optional[Union[str, Ref, GetAtt, Sub]] = None

