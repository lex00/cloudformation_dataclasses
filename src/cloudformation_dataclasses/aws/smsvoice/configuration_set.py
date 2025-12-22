"""PropertyTypes for AWS::SMSVOICE::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLogsDestination(PropertyType):
    IAM_ROLE_ARN = "IamRoleArn"
    LOG_GROUP_ARN = "LogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_role_arn": "IamRoleArn",
        "log_group_arn": "LogGroupArn",
    }

    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventDestination(PropertyType):
    EVENT_DESTINATION_NAME = "EventDestinationName"
    SNS_DESTINATION = "SnsDestination"
    ENABLED = "Enabled"
    MATCHING_EVENT_TYPES = "MatchingEventTypes"
    CLOUD_WATCH_LOGS_DESTINATION = "CloudWatchLogsDestination"
    KINESIS_FIREHOSE_DESTINATION = "KinesisFirehoseDestination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_destination_name": "EventDestinationName",
        "sns_destination": "SnsDestination",
        "enabled": "Enabled",
        "matching_event_types": "MatchingEventTypes",
        "cloud_watch_logs_destination": "CloudWatchLogsDestination",
        "kinesis_firehose_destination": "KinesisFirehoseDestination",
    }

    event_destination_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sns_destination: Optional[SnsDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    matching_event_types: Optional[Union[list[str], Ref]] = None
    cloud_watch_logs_destination: Optional[CloudWatchLogsDestination] = None
    kinesis_firehose_destination: Optional[KinesisFirehoseDestination] = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    DELIVERY_STREAM_ARN = "DeliveryStreamArn"
    IAM_ROLE_ARN = "IamRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_arn": "DeliveryStreamArn",
        "iam_role_arn": "IamRoleArn",
    }

    delivery_stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnsDestination(PropertyType):
    TOPIC_ARN = "TopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

