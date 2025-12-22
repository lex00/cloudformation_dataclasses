"""PropertyTypes for AWS::IVSChat::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChatTokenCapability:
    """ChatTokenCapability enum values."""

    SEND_MESSAGE = "SEND_MESSAGE"
    DISCONNECT_USER = "DISCONNECT_USER"
    DELETE_MESSAGE = "DELETE_MESSAGE"


class CreateLoggingConfigurationState:
    """CreateLoggingConfigurationState enum values."""

    ACTIVE = "ACTIVE"


class FallbackResult:
    """FallbackResult enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class LoggingConfigurationState:
    """LoggingConfigurationState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    ACTIVE = "ACTIVE"


class ResourceType:
    """ResourceType enum values."""

    ROOM = "ROOM"


class UpdateLoggingConfigurationState:
    """UpdateLoggingConfigurationState enum values."""

    ACTIVE = "ACTIVE"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


@dataclass
class CloudWatchLogsDestinationConfiguration(PropertyType):
    LOG_GROUP_NAME = "LogGroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_name": "LogGroupName",
    }

    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DestinationConfiguration(PropertyType):
    S3 = "S3"
    FIREHOSE = "Firehose"
    CLOUD_WATCH_LOGS = "CloudWatchLogs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "firehose": "Firehose",
        "cloud_watch_logs": "CloudWatchLogs",
    }

    s3: Optional[S3DestinationConfiguration] = None
    firehose: Optional[FirehoseDestinationConfiguration] = None
    cloud_watch_logs: Optional[CloudWatchLogsDestinationConfiguration] = None


@dataclass
class FirehoseDestinationConfiguration(PropertyType):
    DELIVERY_STREAM_NAME = "DeliveryStreamName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_name": "DeliveryStreamName",
    }

    delivery_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    BUCKET_NAME = "BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

