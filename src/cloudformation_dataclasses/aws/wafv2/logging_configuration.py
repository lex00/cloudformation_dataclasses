"""PropertyTypes for AWS::WAFv2::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, ActionValue, Ref, GetAtt, Sub]] = None


@dataclass
class Condition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "label_name_condition": "LabelNameCondition",
        "action_condition": "ActionCondition",
    }

    label_name_condition: Optional[LabelNameCondition] = None
    action_condition: Optional[ActionCondition] = None


@dataclass
class FieldToMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "query_string": "QueryString",
        "uri_path": "UriPath",
        "method": "Method",
        "single_header": "SingleHeader",
    }

    query_string: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    uri_path: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    method: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    single_header: Optional[SingleHeader] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "requirement": "Requirement",
        "behavior": "Behavior",
        "conditions": "Conditions",
    }

    requirement: Optional[Union[str, FilterRequirement, Ref, GetAtt, Sub]] = None
    behavior: Optional[Union[str, FilterBehavior, Ref, GetAtt, Sub]] = None
    conditions: Optional[list[Condition]] = None


@dataclass
class LabelNameCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "label_name": "LabelName",
    }

    label_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "default_behavior": "DefaultBehavior",
    }

    filters: Optional[list[Filter]] = None
    default_behavior: Optional[Union[str, FilterBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class SingleHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

