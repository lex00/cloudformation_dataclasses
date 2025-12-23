"""PropertyTypes for AWS::ApplicationAutoScaling::ScalableTarget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ScalableTargetAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_capacity": "MinCapacity",
        "max_capacity": "MaxCapacity",
    }

    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduledAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timezone": "Timezone",
        "scheduled_action_name": "ScheduledActionName",
        "end_time": "EndTime",
        "schedule": "Schedule",
        "start_time": "StartTime",
        "scalable_target_action": "ScalableTargetAction",
    }

    timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scheduled_action_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scalable_target_action: Optional[ScalableTargetAction] = None


@dataclass
class SuspendedState(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic_scaling_out_suspended": "DynamicScalingOutSuspended",
        "scheduled_scaling_suspended": "ScheduledScalingSuspended",
        "dynamic_scaling_in_suspended": "DynamicScalingInSuspended",
    }

    dynamic_scaling_out_suspended: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scheduled_scaling_suspended: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dynamic_scaling_in_suspended: Optional[Union[bool, Ref, GetAtt, Sub]] = None

