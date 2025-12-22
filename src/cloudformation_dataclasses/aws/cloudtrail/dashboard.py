"""PropertyTypes for AWS::CloudTrail::Dashboard."""

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
class Frequency(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RefreshSchedule(PropertyType):
    STATUS = "Status"
    TIME_OF_DAY = "TimeOfDay"
    FREQUENCY = "Frequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "time_of_day": "TimeOfDay",
        "frequency": "Frequency",
    }

    status: Optional[Union[str, RefreshScheduleStatus, Ref, GetAtt, Sub]] = None
    time_of_day: Optional[Union[str, Ref, GetAtt, Sub]] = None
    frequency: Optional[Frequency] = None


@dataclass
class Widget(PropertyType):
    QUERY_STATEMENT = "QueryStatement"
    QUERY_PARAMETERS = "QueryParameters"
    VIEW_PROPERTIES = "ViewProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_statement": "QueryStatement",
        "query_parameters": "QueryParameters",
        "view_properties": "ViewProperties",
    }

    query_statement: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_parameters: Optional[Union[list[str], Ref]] = None
    view_properties: Optional[dict[str, str]] = None

