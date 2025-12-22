"""PropertyTypes for AWS::Pinpoint::Segment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Action:
    """Action enum values."""

    OPEN_APP = "OPEN_APP"
    DEEP_LINK = "DEEP_LINK"
    URL = "URL"


class Alignment:
    """Alignment enum values."""

    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"


class AttributeType:
    """AttributeType enum values."""

    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"
    CONTAINS = "CONTAINS"
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    ON = "ON"
    BETWEEN = "BETWEEN"


class ButtonAction:
    """ButtonAction enum values."""

    LINK = "LINK"
    DEEP_LINK = "DEEP_LINK"
    CLOSE = "CLOSE"


class CampaignStatus:
    """CampaignStatus enum values."""

    SCHEDULED = "SCHEDULED"
    EXECUTING = "EXECUTING"
    PENDING_NEXT_RUN = "PENDING_NEXT_RUN"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    DELETED = "DELETED"
    INVALID = "INVALID"


class ChannelType:
    """ChannelType enum values."""

    PUSH = "PUSH"
    GCM = "GCM"
    APNS = "APNS"
    APNS_SANDBOX = "APNS_SANDBOX"
    APNS_VOIP = "APNS_VOIP"
    APNS_VOIP_SANDBOX = "APNS_VOIP_SANDBOX"
    ADM = "ADM"
    SMS = "SMS"
    VOICE = "VOICE"
    EMAIL = "EMAIL"
    BAIDU = "BAIDU"
    CUSTOM = "CUSTOM"
    IN_APP = "IN_APP"


class DayOfWeek:
    """DayOfWeek enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DeliveryStatus:
    """DeliveryStatus enum values."""

    SUCCESSFUL = "SUCCESSFUL"
    THROTTLED = "THROTTLED"
    TEMPORARY_FAILURE = "TEMPORARY_FAILURE"
    PERMANENT_FAILURE = "PERMANENT_FAILURE"
    UNKNOWN_FAILURE = "UNKNOWN_FAILURE"
    OPT_OUT = "OPT_OUT"
    DUPLICATE = "DUPLICATE"


class DimensionType:
    """DimensionType enum values."""

    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"


class Duration:
    """Duration enum values."""

    HR_24 = "HR_24"
    DAY_7 = "DAY_7"
    DAY_14 = "DAY_14"
    DAY_30 = "DAY_30"


class FilterType:
    """FilterType enum values."""

    SYSTEM = "SYSTEM"
    ENDPOINT = "ENDPOINT"


class Format:
    """Format enum values."""

    CSV = "CSV"
    JSON = "JSON"


class Frequency:
    """Frequency enum values."""

    ONCE = "ONCE"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    EVENT = "EVENT"
    IN_APP_EVENT = "IN_APP_EVENT"


class Include:
    """Include enum values."""

    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


class JobStatus:
    """JobStatus enum values."""

    CREATED = "CREATED"
    PREPARING_FOR_INITIALIZATION = "PREPARING_FOR_INITIALIZATION"
    INITIALIZING = "INITIALIZING"
    PROCESSING = "PROCESSING"
    PENDING_JOB = "PENDING_JOB"
    COMPLETING = "COMPLETING"
    COMPLETED = "COMPLETED"
    FAILING = "FAILING"
    FAILED = "FAILED"


class JourneyRunStatus:
    """JourneyRunStatus enum values."""

    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Layout:
    """Layout enum values."""

    BOTTOM_BANNER = "BOTTOM_BANNER"
    TOP_BANNER = "TOP_BANNER"
    OVERLAYS = "OVERLAYS"
    MOBILE_FEED = "MOBILE_FEED"
    MIDDLE_BANNER = "MIDDLE_BANNER"
    CAROUSEL = "CAROUSEL"


class MessageType:
    """MessageType enum values."""

    TRANSACTIONAL = "TRANSACTIONAL"
    PROMOTIONAL = "PROMOTIONAL"


class Mode:
    """Mode enum values."""

    DELIVERY = "DELIVERY"
    FILTER = "FILTER"


class Operator:
    """Operator enum values."""

    ALL = "ALL"
    ANY = "ANY"


class RecencyType:
    """RecencyType enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class SegmentType:
    """SegmentType enum values."""

    DIMENSIONAL = "DIMENSIONAL"
    IMPORT = "IMPORT"


class SourceType:
    """SourceType enum values."""

    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


class State:
    """State enum values."""

    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    CLOSED = "CLOSED"
    PAUSED = "PAUSED"


class TemplateType:
    """TemplateType enum values."""

    EMAIL = "EMAIL"
    SMS = "SMS"
    VOICE = "VOICE"
    PUSH = "PUSH"
    INAPP = "INAPP"


class Type:
    """Type enum values."""

    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


class __EndpointTypesElement:
    """__EndpointTypesElement enum values."""

    PUSH = "PUSH"
    GCM = "GCM"
    APNS = "APNS"
    APNS_SANDBOX = "APNS_SANDBOX"
    APNS_VOIP = "APNS_VOIP"
    APNS_VOIP_SANDBOX = "APNS_VOIP_SANDBOX"
    ADM = "ADM"
    SMS = "SMS"
    VOICE = "VOICE"
    EMAIL = "EMAIL"
    BAIDU = "BAIDU"
    CUSTOM = "CUSTOM"
    IN_APP = "IN_APP"


class __TimezoneEstimationMethodsElement:
    """__TimezoneEstimationMethodsElement enum values."""

    PHONE_NUMBER = "PHONE_NUMBER"
    POSTAL_CODE = "POSTAL_CODE"


@dataclass
class AttributeDimension(PropertyType):
    ATTRIBUTE_TYPE = "AttributeType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_type": "AttributeType",
        "values": "Values",
    }

    attribute_type: Optional[Union[str, AttributeType, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Behavior(PropertyType):
    RECENCY = "Recency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recency": "Recency",
    }

    recency: Optional[Recency] = None


@dataclass
class Coordinates(PropertyType):
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"

    _property_mappings: ClassVar[dict[str, str]] = {
        "latitude": "Latitude",
        "longitude": "Longitude",
    }

    latitude: Optional[Union[float, Ref, GetAtt, Sub]] = None
    longitude: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Demographic(PropertyType):
    APP_VERSION = "AppVersion"
    DEVICE_TYPE = "DeviceType"
    PLATFORM = "Platform"
    CHANNEL = "Channel"
    MODEL = "Model"
    MAKE = "Make"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_version": "AppVersion",
        "device_type": "DeviceType",
        "platform": "Platform",
        "channel": "Channel",
        "model": "Model",
        "make": "Make",
    }

    app_version: Optional[SetDimension] = None
    device_type: Optional[SetDimension] = None
    platform: Optional[SetDimension] = None
    channel: Optional[SetDimension] = None
    model: Optional[SetDimension] = None
    make: Optional[SetDimension] = None


@dataclass
class GPSPoint(PropertyType):
    RANGE_IN_KILOMETERS = "RangeInKilometers"
    COORDINATES = "Coordinates"

    _property_mappings: ClassVar[dict[str, str]] = {
        "range_in_kilometers": "RangeInKilometers",
        "coordinates": "Coordinates",
    }

    range_in_kilometers: Optional[Union[float, Ref, GetAtt, Sub]] = None
    coordinates: Optional[Coordinates] = None


@dataclass
class Groups(PropertyType):
    TYPE = "Type"
    SOURCE_TYPE = "SourceType"
    DIMENSIONS = "Dimensions"
    SOURCE_SEGMENTS = "SourceSegments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "source_type": "SourceType",
        "dimensions": "Dimensions",
        "source_segments": "SourceSegments",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[SegmentDimensions]] = None
    source_segments: Optional[list[SourceSegments]] = None


@dataclass
class Location(PropertyType):
    GPS_POINT = "GPSPoint"
    COUNTRY = "Country"

    _property_mappings: ClassVar[dict[str, str]] = {
        "gps_point": "GPSPoint",
        "country": "Country",
    }

    gps_point: Optional[GPSPoint] = None
    country: Optional[SetDimension] = None


@dataclass
class Recency(PropertyType):
    DURATION = "Duration"
    RECENCY_TYPE = "RecencyType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "recency_type": "RecencyType",
    }

    duration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recency_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SegmentDimensions(PropertyType):
    DEMOGRAPHIC = "Demographic"
    METRICS = "Metrics"
    ATTRIBUTES = "Attributes"
    BEHAVIOR = "Behavior"
    USER_ATTRIBUTES = "UserAttributes"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "demographic": "Demographic",
        "metrics": "Metrics",
        "attributes": "Attributes",
        "behavior": "Behavior",
        "user_attributes": "UserAttributes",
        "location": "Location",
    }

    demographic: Optional[Demographic] = None
    metrics: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    attributes: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    behavior: Optional[Behavior] = None
    user_attributes: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    location: Optional[Location] = None


@dataclass
class SegmentGroups(PropertyType):
    GROUPS = "Groups"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "groups": "Groups",
        "include": "Include",
    }

    groups: Optional[list[Groups]] = None
    include: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SetDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, DimensionType, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class SourceSegments(PropertyType):
    VERSION = "Version"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "id": "Id",
    }

    version: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

