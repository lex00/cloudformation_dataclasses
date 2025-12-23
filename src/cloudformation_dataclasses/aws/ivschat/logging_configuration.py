"""PropertyTypes for AWS::IVSChat::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

