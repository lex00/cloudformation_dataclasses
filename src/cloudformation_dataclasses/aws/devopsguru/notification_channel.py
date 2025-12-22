"""PropertyTypes for AWS::DevOpsGuru::NotificationChannel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NotificationChannelConfig(PropertyType):
    FILTERS = "Filters"
    SNS = "Sns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "sns": "Sns",
    }

    filters: Optional[NotificationFilterConfig] = None
    sns: Optional[SnsChannelConfig] = None


@dataclass
class NotificationFilterConfig(PropertyType):
    MESSAGE_TYPES = "MessageTypes"
    SEVERITIES = "Severities"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_types": "MessageTypes",
        "severities": "Severities",
    }

    message_types: Optional[Union[list[str], Ref]] = None
    severities: Optional[Union[list[str], Ref]] = None


@dataclass
class SnsChannelConfig(PropertyType):
    TOPIC_ARN = "TopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

