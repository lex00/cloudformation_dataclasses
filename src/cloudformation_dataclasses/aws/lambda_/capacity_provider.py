"""PropertyTypes for AWS::Lambda::CapacityProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityProviderPermissionsConfig(PropertyType):
    CAPACITY_PROVIDER_OPERATOR_ROLE_ARN = "CapacityProviderOperatorRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider_operator_role_arn": "CapacityProviderOperatorRoleArn",
    }

    capacity_provider_operator_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityProviderScalingConfig(PropertyType):
    SCALING_POLICIES = "ScalingPolicies"
    SCALING_MODE = "ScalingMode"
    MAX_V_CPU_COUNT = "MaxVCpuCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scaling_policies": "ScalingPolicies",
        "scaling_mode": "ScalingMode",
        "max_v_cpu_count": "MaxVCpuCount",
    }

    scaling_policies: Optional[list[TargetTrackingScalingPolicy]] = None
    scaling_mode: Optional[Union[str, CapacityProviderScalingMode, Ref, GetAtt, Sub]] = None
    max_v_cpu_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityProviderVpcConfig(PropertyType):
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class InstanceRequirements(PropertyType):
    ALLOWED_INSTANCE_TYPES = "AllowedInstanceTypes"
    EXCLUDED_INSTANCE_TYPES = "ExcludedInstanceTypes"
    ARCHITECTURES = "Architectures"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_instance_types": "AllowedInstanceTypes",
        "excluded_instance_types": "ExcludedInstanceTypes",
        "architectures": "Architectures",
    }

    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    architectures: Optional[Union[list[str], Ref]] = None


@dataclass
class TargetTrackingScalingPolicy(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    TARGET_VALUE = "TargetValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "target_value": "TargetValue",
    }

    predefined_metric_type: Optional[Union[str, CapacityProviderPredefinedMetricType, Ref, GetAtt, Sub]] = None
    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None

