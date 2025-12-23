"""PropertyTypes for AWS::Connect::RoutingProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CrossChannelBehavior(PropertyType):
    BEHAVIOR_TYPE = "BehaviorType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "behavior_type": "BehaviorType",
    }

    behavior_type: Optional[Union[str, BehaviorType, Ref, GetAtt, Sub]] = None


@dataclass
class MediaConcurrency(PropertyType):
    CONCURRENCY = "Concurrency"
    CHANNEL = "Channel"
    CROSS_CHANNEL_BEHAVIOR = "CrossChannelBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "concurrency": "Concurrency",
        "channel": "Channel",
        "cross_channel_behavior": "CrossChannelBehavior",
    }

    concurrency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    channel: Optional[Union[str, Channel, Ref, GetAtt, Sub]] = None
    cross_channel_behavior: Optional[CrossChannelBehavior] = None


@dataclass
class RoutingProfileManualAssignmentQueueConfig(PropertyType):
    QUEUE_REFERENCE = "QueueReference"

    _property_mappings: ClassVar[dict[str, str]] = {
        "queue_reference": "QueueReference",
    }

    queue_reference: Optional[RoutingProfileQueueReference] = None


@dataclass
class RoutingProfileQueueConfig(PropertyType):
    PRIORITY = "Priority"
    QUEUE_REFERENCE = "QueueReference"
    DELAY = "Delay"

    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "queue_reference": "QueueReference",
        "delay": "Delay",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    queue_reference: Optional[RoutingProfileQueueReference] = None
    delay: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingProfileQueueReference(PropertyType):
    CHANNEL = "Channel"
    QUEUE_ARN = "QueueArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel": "Channel",
        "queue_arn": "QueueArn",
    }

    channel: Optional[Union[str, Channel, Ref, GetAtt, Sub]] = None
    queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

