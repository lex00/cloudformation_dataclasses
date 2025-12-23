"""PropertyTypes for AWS::WAF::ByteMatchSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ByteMatchTuple(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_to_match": "FieldToMatch",
        "positional_constraint": "PositionalConstraint",
        "target_string": "TargetString",
        "target_string_base64": "TargetStringBase64",
        "text_transformation": "TextTransformation",
    }

    field_to_match: Optional[FieldToMatch] = None
    positional_constraint: Optional[Union[str, PositionalConstraint, Ref, GetAtt, Sub]] = None
    target_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_string_base64: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None


@dataclass
class FieldToMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data": "Data",
        "type_": "Type",
    }

    data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, MatchFieldType, Ref, GetAtt, Sub]] = None

