"""PropertyTypes for AWS::CloudTrail::EventDataStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedEventSelector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_selectors": "FieldSelectors",
        "name": "Name",
    }

    field_selectors: Optional[list[AdvancedFieldSelector]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "equals": "Equals",
        "not_starts_with": "NotStartsWith",
        "not_ends_with": "NotEndsWith",
        "starts_with": "StartsWith",
        "ends_with": "EndsWith",
        "not_equals": "NotEquals",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    equals: Optional[Union[list[str], Ref]] = None
    not_starts_with: Optional[Union[list[str], Ref]] = None
    not_ends_with: Optional[Union[list[str], Ref]] = None
    starts_with: Optional[Union[list[str], Ref]] = None
    ends_with: Optional[Union[list[str], Ref]] = None
    not_equals: Optional[Union[list[str], Ref]] = None


@dataclass
class ContextKeySelector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "equals": "Equals",
    }

    type_: Optional[Union[str, Type, Ref, GetAtt, Sub]] = None
    equals: Optional[Union[list[str], Ref]] = None


@dataclass
class InsightSelector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "insight_type": "InsightType",
    }

    insight_type: Optional[Union[str, InsightType, Ref, GetAtt, Sub]] = None

