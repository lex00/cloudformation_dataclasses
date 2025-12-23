"""PropertyTypes for AWS::WAFRegional::SizeConstraintSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FieldToMatch(PropertyType):
    TYPE = "Type"
    DATA = "Data"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "data": "Data",
    }

    type_: Optional[Union[str, MatchFieldType, Ref, GetAtt, Sub]] = None
    data: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SizeConstraint(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    SIZE = "Size"
    TEXT_TRANSFORMATION = "TextTransformation"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "size": "Size",
        "text_transformation": "TextTransformation",
        "field_to_match": "FieldToMatch",
    }

    comparison_operator: Optional[Union[str, ComparisonOperator, Ref, GetAtt, Sub]] = None
    size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None

