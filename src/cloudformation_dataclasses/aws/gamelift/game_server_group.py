"""PropertyTypes for AWS::GameLift::GameServerGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoScalingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_tracking_configuration": "TargetTrackingConfiguration",
        "estimated_instance_warmup": "EstimatedInstanceWarmup",
    }

    target_tracking_configuration: Optional[TargetTrackingConfiguration] = None
    estimated_instance_warmup: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_capacity": "WeightedCapacity",
        "instance_type": "InstanceType",
    }

    weighted_capacity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, GameServerGroupInstanceType, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "launch_template_id": "LaunchTemplateId",
    }

    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
    }

    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None

