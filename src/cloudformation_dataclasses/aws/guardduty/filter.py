"""PropertyTypes for AWS::GuardDuty::Filter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Condition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "equals": "Equals",
        "less_than": "LessThan",
        "less_than_or_equal": "LessThanOrEqual",
        "greater_than": "GreaterThan",
        "lt": "Lt",
        "gte": "Gte",
        "neq": "Neq",
        "greater_than_or_equal": "GreaterThanOrEqual",
        "eq": "Eq",
        "lte": "Lte",
        "gt": "Gt",
        "not_equals": "NotEquals",
    }

    equals: Optional[Union[list[str], Ref]] = None
    less_than: Optional[Union[int, Ref, GetAtt, Sub]] = None
    less_than_or_equal: Optional[Union[int, Ref, GetAtt, Sub]] = None
    greater_than: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lt: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    neq: Optional[Union[list[str], Ref]] = None
    greater_than_or_equal: Optional[Union[int, Ref, GetAtt, Sub]] = None
    eq: Optional[Union[list[str], Ref]] = None
    lte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gt: Optional[Union[int, Ref, GetAtt, Sub]] = None
    not_equals: Optional[Union[list[str], Ref]] = None


@dataclass
class FindingCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "criterion": "Criterion",
    }

    criterion: Optional[dict[str, Any]] = None


@dataclass
class TagItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

