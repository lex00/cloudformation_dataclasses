"""PropertyTypes for AWS::PinpointEmail::ConfigurationSetEventDestination."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchDestination(PropertyType):
    DIMENSION_CONFIGURATIONS = "DimensionConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_configurations": "DimensionConfigurations",
    }

    dimension_configurations: Optional[list[DimensionConfiguration]] = None


@dataclass
class DimensionConfiguration(PropertyType):
    DIMENSION_VALUE_SOURCE = "DimensionValueSource"
    DEFAULT_DIMENSION_VALUE = "DefaultDimensionValue"
    DIMENSION_NAME = "DimensionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_value_source": "DimensionValueSource",
        "default_dimension_value": "DefaultDimensionValue",
        "dimension_name": "DimensionName",
    }

    dimension_value_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_dimension_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventDestination(PropertyType):
    SNS_DESTINATION = "SnsDestination"
    CLOUD_WATCH_DESTINATION = "CloudWatchDestination"
    ENABLED = "Enabled"
    MATCHING_EVENT_TYPES = "MatchingEventTypes"
    PINPOINT_DESTINATION = "PinpointDestination"
    KINESIS_FIREHOSE_DESTINATION = "KinesisFirehoseDestination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_destination": "SnsDestination",
        "cloud_watch_destination": "CloudWatchDestination",
        "enabled": "Enabled",
        "matching_event_types": "MatchingEventTypes",
        "pinpoint_destination": "PinpointDestination",
        "kinesis_firehose_destination": "KinesisFirehoseDestination",
    }

    sns_destination: Optional[SnsDestination] = None
    cloud_watch_destination: Optional[CloudWatchDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    matching_event_types: Optional[Union[list[str], Ref]] = None
    pinpoint_destination: Optional[PinpointDestination] = None
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
class PinpointDestination(PropertyType):
    APPLICATION_ARN = "ApplicationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_arn": "ApplicationArn",
    }

    application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnsDestination(PropertyType):
    TOPIC_ARN = "TopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

