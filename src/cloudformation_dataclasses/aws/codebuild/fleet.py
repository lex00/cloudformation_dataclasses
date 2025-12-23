"""PropertyTypes for AWS::CodeBuild::Fleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComputeConfiguration(PropertyType):
    DISK = "disk"
    MEMORY = "memory"
    V_CPU = "vCpu"
    INSTANCE_TYPE = "instanceType"
    MACHINE_TYPE = "machineType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disk": "disk",
        "memory": "memory",
        "v_cpu": "vCpu",
        "instance_type": "instanceType",
        "machine_type": "machineType",
    }

    disk: Optional[Union[int, Ref, GetAtt, Sub]] = None
    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    v_cpu: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[str, MachineType, Ref, GetAtt, Sub]] = None


@dataclass
class FleetProxyRule(PropertyType):
    TYPE = "Type"
    EFFECT = "Effect"
    ENTITIES = "Entities"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "effect": "Effect",
        "entities": "Entities",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effect: Optional[Union[str, Ref, GetAtt, Sub]] = None
    entities: Optional[Union[list[str], Ref]] = None


@dataclass
class ProxyConfiguration(PropertyType):
    DEFAULT_BEHAVIOR = "DefaultBehavior"
    ORDERED_PROXY_RULES = "OrderedProxyRules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_behavior": "DefaultBehavior",
        "ordered_proxy_rules": "OrderedProxyRules",
    }

    default_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ordered_proxy_rules: Optional[list[FleetProxyRule]] = None


@dataclass
class ScalingConfigurationInput(PropertyType):
    TARGET_TRACKING_SCALING_CONFIGS = "TargetTrackingScalingConfigs"
    SCALING_TYPE = "ScalingType"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_tracking_scaling_configs": "TargetTrackingScalingConfigs",
        "scaling_type": "ScalingType",
        "max_capacity": "MaxCapacity",
    }

    target_tracking_scaling_configs: Optional[list[TargetTrackingScalingConfiguration]] = None
    scaling_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingScalingConfiguration(PropertyType):
    TARGET_VALUE = "TargetValue"
    METRIC_TYPE = "MetricType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
        "metric_type": "MetricType",
    }

    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    SUBNETS = "Subnets"
    VPC_ID = "VpcId"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "vpc_id": "VpcId",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

