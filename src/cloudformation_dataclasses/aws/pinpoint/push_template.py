"""PropertyTypes for AWS::Pinpoint::PushTemplate."""

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
class APNSPushNotificationTemplate(PropertyType):
    ACTION = "Action"
    MEDIA_URL = "MediaUrl"
    TITLE = "Title"
    SOUND = "Sound"
    BODY = "Body"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "media_url": "MediaUrl",
        "title": "Title",
        "sound": "Sound",
        "body": "Body",
        "url": "Url",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    media_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AndroidPushNotificationTemplate(PropertyType):
    ACTION = "Action"
    IMAGE_URL = "ImageUrl"
    SMALL_IMAGE_ICON_URL = "SmallImageIconUrl"
    TITLE = "Title"
    IMAGE_ICON_URL = "ImageIconUrl"
    SOUND = "Sound"
    BODY = "Body"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "image_url": "ImageUrl",
        "small_image_icon_url": "SmallImageIconUrl",
        "title": "Title",
        "image_icon_url": "ImageIconUrl",
        "sound": "Sound",
        "body": "Body",
        "url": "Url",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    image_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    small_image_icon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_icon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultPushNotificationTemplate(PropertyType):
    ACTION = "Action"
    TITLE = "Title"
    SOUND = "Sound"
    BODY = "Body"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "title": "Title",
        "sound": "Sound",
        "body": "Body",
        "url": "Url",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None

