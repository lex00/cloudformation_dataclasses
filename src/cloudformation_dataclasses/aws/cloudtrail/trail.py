"""PropertyTypes for AWS::CloudTrail::Trail."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BillingMode:
    """BillingMode enum values."""

    EXTENDABLE_RETENTION_PRICING = "EXTENDABLE_RETENTION_PRICING"
    FIXED_RETENTION_PRICING = "FIXED_RETENTION_PRICING"


class DashboardStatus:
    """DashboardStatus enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    UPDATING = "UPDATING"
    UPDATED = "UPDATED"
    DELETING = "DELETING"


class DashboardType:
    """DashboardType enum values."""

    MANAGED = "MANAGED"
    CUSTOM = "CUSTOM"


class DeliveryStatus:
    """DeliveryStatus enum values."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    FAILED_SIGNING_FILE = "FAILED_SIGNING_FILE"
    PENDING = "PENDING"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    ACCESS_DENIED = "ACCESS_DENIED"
    ACCESS_DENIED_SIGNING_FILE = "ACCESS_DENIED_SIGNING_FILE"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"


class DestinationType:
    """DestinationType enum values."""

    EVENT_DATA_STORE = "EVENT_DATA_STORE"
    AWS_SERVICE = "AWS_SERVICE"


class EventCategory:
    """EventCategory enum values."""

    INSIGHT = "insight"


class EventCategoryAggregation:
    """EventCategoryAggregation enum values."""

    DATA = "Data"


class EventDataStoreStatus:
    """EventDataStoreStatus enum values."""

    CREATED = "CREATED"
    ENABLED = "ENABLED"
    PENDING_DELETION = "PENDING_DELETION"
    STARTING_INGESTION = "STARTING_INGESTION"
    STOPPING_INGESTION = "STOPPING_INGESTION"
    STOPPED_INGESTION = "STOPPED_INGESTION"


class FederationStatus:
    """FederationStatus enum values."""

    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


class ImportFailureStatus:
    """ImportFailureStatus enum values."""

    FAILED = "FAILED"
    RETRY = "RETRY"
    SUCCEEDED = "SUCCEEDED"


class ImportStatus:
    """ImportStatus enum values."""

    INITIALIZING = "INITIALIZING"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    STOPPED = "STOPPED"
    COMPLETED = "COMPLETED"


class InsightType:
    """InsightType enum values."""

    APICALLRATEINSIGHT = "ApiCallRateInsight"
    APIERRORRATEINSIGHT = "ApiErrorRateInsight"


class InsightsMetricDataType:
    """InsightsMetricDataType enum values."""

    FILLWITHZEROS = "FillWithZeros"
    NONZERODATA = "NonZeroData"


class ListInsightsDataDimensionKey:
    """ListInsightsDataDimensionKey enum values."""

    EVENTID = "EventId"
    EVENTNAME = "EventName"
    EVENTSOURCE = "EventSource"


class ListInsightsDataType:
    """ListInsightsDataType enum values."""

    INSIGHTSEVENTS = "InsightsEvents"


class LookupAttributeKey:
    """LookupAttributeKey enum values."""

    EVENTID = "EventId"
    EVENTNAME = "EventName"
    READONLY = "ReadOnly"
    USERNAME = "Username"
    RESOURCETYPE = "ResourceType"
    RESOURCENAME = "ResourceName"
    EVENTSOURCE = "EventSource"
    ACCESSKEYID = "AccessKeyId"


class MaxEventSize:
    """MaxEventSize enum values."""

    STANDARD = "Standard"
    LARGE = "Large"


class QueryStatus:
    """QueryStatus enum values."""

    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    TIMED_OUT = "TIMED_OUT"


class ReadWriteType:
    """ReadWriteType enum values."""

    READONLY = "ReadOnly"
    WRITEONLY = "WriteOnly"
    ALL = "All"


class RefreshScheduleFrequencyUnit:
    """RefreshScheduleFrequencyUnit enum values."""

    HOURS = "HOURS"
    DAYS = "DAYS"


class RefreshScheduleStatus:
    """RefreshScheduleStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SourceEventCategory:
    """SourceEventCategory enum values."""

    MANAGEMENT = "Management"
    DATA = "Data"


class Template:
    """Template enum values."""

    API_ACTIVITY = "API_ACTIVITY"
    RESOURCE_ACCESS = "RESOURCE_ACCESS"
    USER_ACTIONS = "USER_ACTIONS"


class Type:
    """Type enum values."""

    TAGCONTEXT = "TagContext"
    REQUESTCONTEXT = "RequestContext"


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

