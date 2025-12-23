"""PropertyTypes for AWS::WAF::SizeConstraintSet."""

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
class SizeConstraint(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    FIELD_TO_MATCH = "FieldToMatch"
    SIZE = "Size"
    TEXT_TRANSFORMATION = "TextTransformation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "field_to_match": "FieldToMatch",
        "size": "Size",
        "text_transformation": "TextTransformation",
    }

    comparison_operator: Optional[Union[str, ComparisonOperator, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None
    size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None

