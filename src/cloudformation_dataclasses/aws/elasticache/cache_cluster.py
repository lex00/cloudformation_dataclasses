"""PropertyTypes for AWS::ElastiCache::CacheCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLogsDestinationDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DestinationDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_details": "CloudWatchLogsDetails",
        "kinesis_firehose_details": "KinesisFirehoseDetails",
    }

    cloud_watch_logs_details: Optional[CloudWatchLogsDestinationDetails] = None
    kinesis_firehose_details: Optional[KinesisFirehoseDestinationDetails] = None


@dataclass
class KinesisFirehoseDestinationDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogDeliveryConfigurationRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_details": "DestinationDetails",
        "destination_type": "DestinationType",
        "log_format": "LogFormat",
        "log_type": "LogType",
    }

    destination_details: Optional[DestinationDetails] = None
    destination_type: Optional[Union[str, DestinationType, Ref, GetAtt, Sub]] = None
    log_format: Optional[Union[str, LogFormat, Ref, GetAtt, Sub]] = None
    log_type: Optional[Union[str, LogType, Ref, GetAtt, Sub]] = None

