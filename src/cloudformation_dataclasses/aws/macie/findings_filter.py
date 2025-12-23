"""PropertyTypes for AWS::Macie::FindingsFilter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CriterionAdditionalProperties(PropertyType):
    LT = "lt"
    GTE = "gte"
    NEQ = "neq"
    LTE = "lte"
    EQ = "eq"
    GT = "gt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lt": "lt",
        "gte": "gte",
        "neq": "neq",
        "lte": "lte",
        "eq": "eq",
        "gt": "gt",
    }

    lt: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    neq: Optional[Union[list[str], Ref]] = None
    lte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    eq: Optional[Union[list[str], Ref]] = None
    gt: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FindingCriteria(PropertyType):
    CRITERION = "Criterion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "criterion": "Criterion",
    }

    criterion: Optional[dict[str, Any]] = None

