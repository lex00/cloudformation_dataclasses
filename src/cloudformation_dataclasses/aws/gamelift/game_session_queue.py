"""PropertyTypes for AWS::GameLift::GameSessionQueue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FilterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_locations": "AllowedLocations",
    }

    allowed_locations: Optional[Union[list[str], Ref]] = None


@dataclass
class GameSessionQueueDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_arn": "DestinationArn",
    }

    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PlayerLatencyPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_duration_seconds": "PolicyDurationSeconds",
        "maximum_individual_player_latency_milliseconds": "MaximumIndividualPlayerLatencyMilliseconds",
    }

    policy_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_individual_player_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PriorityConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "priority_order": "PriorityOrder",
        "location_order": "LocationOrder",
    }

    priority_order: Optional[Union[list[str], Ref]] = None
    location_order: Optional[Union[list[str], Ref]] = None

