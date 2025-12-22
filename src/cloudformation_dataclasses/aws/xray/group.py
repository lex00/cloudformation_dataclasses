"""PropertyTypes for AWS::XRay::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class EncryptionStatus:
    """EncryptionStatus enum values."""

    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"


class EncryptionType:
    """EncryptionType enum values."""

    NONE = "NONE"
    KMS = "KMS"


class InsightCategory:
    """InsightCategory enum values."""

    FAULT = "FAULT"


class InsightState:
    """InsightState enum values."""

    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


class RetrievalStatus:
    """RetrievalStatus enum values."""

    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    TIMEOUT = "TIMEOUT"


class SamplingStrategyName:
    """SamplingStrategyName enum values."""

    PARTIALSCAN = "PartialScan"
    FIXEDRATE = "FixedRate"


class TimeRangeType:
    """TimeRangeType enum values."""

    TRACEID = "TraceId"
    EVENT = "Event"
    SERVICE = "Service"


class TraceFormatType:
    """TraceFormatType enum values."""

    XRAY = "XRAY"
    OTEL = "OTEL"


class TraceSegmentDestination:
    """TraceSegmentDestination enum values."""

    XRAY = "XRay"
    CLOUDWATCHLOGS = "CloudWatchLogs"


class TraceSegmentDestinationStatus:
    """TraceSegmentDestinationStatus enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"


@dataclass
class InsightsConfiguration(PropertyType):
    NOTIFICATIONS_ENABLED = "NotificationsEnabled"
    INSIGHTS_ENABLED = "InsightsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notifications_enabled": "NotificationsEnabled",
        "insights_enabled": "InsightsEnabled",
    }

    notifications_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    insights_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

