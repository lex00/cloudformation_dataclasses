"""PropertyTypes for AWS::CloudTrail::Trail."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedEventSelector(PropertyType):
    FIELD_SELECTORS = "FieldSelectors"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_selectors": "FieldSelectors",
        "name": "Name",
    }

    field_selectors: Optional[list[AdvancedFieldSelector]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    FIELD = "Field"
    EQUALS = "Equals"
    NOT_STARTS_WITH = "NotStartsWith"
    NOT_ENDS_WITH = "NotEndsWith"
    STARTS_WITH = "StartsWith"
    ENDS_WITH = "EndsWith"
    NOT_EQUALS = "NotEquals"

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
class AggregationConfiguration(PropertyType):
    EVENT_CATEGORY = "EventCategory"
    TEMPLATES = "Templates"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_category": "EventCategory",
        "templates": "Templates",
    }

    event_category: Optional[Union[str, EventCategoryAggregation, Ref, GetAtt, Sub]] = None
    templates: Optional[Union[list[str], Ref]] = None


@dataclass
class DataResource(PropertyType):
    TYPE = "Type"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "values": "Values",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class EventSelector(PropertyType):
    INCLUDE_MANAGEMENT_EVENTS = "IncludeManagementEvents"
    READ_WRITE_TYPE = "ReadWriteType"
    EXCLUDE_MANAGEMENT_EVENT_SOURCES = "ExcludeManagementEventSources"
    DATA_RESOURCES = "DataResources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_management_events": "IncludeManagementEvents",
        "read_write_type": "ReadWriteType",
        "exclude_management_event_sources": "ExcludeManagementEventSources",
        "data_resources": "DataResources",
    }

    include_management_events: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    read_write_type: Optional[Union[str, ReadWriteType, Ref, GetAtt, Sub]] = None
    exclude_management_event_sources: Optional[Union[list[str], Ref]] = None
    data_resources: Optional[list[DataResource]] = None


@dataclass
class InsightSelector(PropertyType):
    INSIGHT_TYPE = "InsightType"
    EVENT_CATEGORIES = "EventCategories"

    _property_mappings: ClassVar[dict[str, str]] = {
        "insight_type": "InsightType",
        "event_categories": "EventCategories",
    }

    insight_type: Optional[Union[str, InsightType, Ref, GetAtt, Sub]] = None
    event_categories: Optional[Union[list[str], Ref]] = None

