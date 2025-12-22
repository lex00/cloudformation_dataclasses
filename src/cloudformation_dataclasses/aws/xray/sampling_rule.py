"""PropertyTypes for AWS::XRay::SamplingRule."""

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
class SamplingRule(PropertyType):
    PRIORITY = "Priority"
    RESERVOIR_SIZE = "ReservoirSize"
    RULE_ARN = "RuleARN"
    URL_PATH = "URLPath"
    ATTRIBUTES = "Attributes"
    FIXED_RATE = "FixedRate"
    HOST = "Host"
    RESOURCE_ARN = "ResourceARN"
    HTTP_METHOD = "HTTPMethod"
    SERVICE_NAME = "ServiceName"
    VERSION = "Version"
    SERVICE_TYPE = "ServiceType"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "reservoir_size": "ReservoirSize",
        "rule_arn": "RuleARN",
        "url_path": "URLPath",
        "attributes": "Attributes",
        "fixed_rate": "FixedRate",
        "host": "Host",
        "resource_arn": "ResourceARN",
        "http_method": "HTTPMethod",
        "service_name": "ServiceName",
        "version": "Version",
        "service_type": "ServiceType",
        "rule_name": "RuleName",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    reservoir_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rule_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[dict[str, str]] = None
    fixed_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[int, Ref, GetAtt, Sub]] = None
    service_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

