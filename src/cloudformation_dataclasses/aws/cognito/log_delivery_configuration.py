"""PropertyTypes for AWS::Cognito::LogDeliveryConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    LOG_GROUP_ARN = "LogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FirehoseConfiguration(PropertyType):
    STREAM_ARN = "StreamArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_arn": "StreamArn",
    }

    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfiguration(PropertyType):
    FIREHOSE_CONFIGURATION = "FirehoseConfiguration"
    EVENT_SOURCE = "EventSource"
    S3_CONFIGURATION = "S3Configuration"
    CLOUD_WATCH_LOGS_CONFIGURATION = "CloudWatchLogsConfiguration"
    LOG_LEVEL = "LogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "firehose_configuration": "FirehoseConfiguration",
        "event_source": "EventSource",
        "s3_configuration": "S3Configuration",
        "cloud_watch_logs_configuration": "CloudWatchLogsConfiguration",
        "log_level": "LogLevel",
    }

    firehose_configuration: Optional[FirehoseConfiguration] = None
    event_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_configuration: Optional[S3Configuration] = None
    cloud_watch_logs_configuration: Optional[CloudWatchLogsConfiguration] = None
    log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Configuration(PropertyType):
    BUCKET_ARN = "BucketArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

