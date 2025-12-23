"""PropertyTypes for AWS::SageMaker::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AlarmDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_name": "AlarmName",
    }

    alarm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacitySizeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, NodeUnavailabilityType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterAutoScalingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "auto_scaler_type": "AutoScalerType",
    }

    mode: Optional[Union[str, ClusterAutoScalingMode, Ref, GetAtt, Sub]] = None
    auto_scaler_type: Optional[Union[str, ClusterAutoScalerType, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterCapacityRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "spot": "Spot",
        "on_demand": "OnDemand",
    }

    spot: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    on_demand: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class ClusterEbsVolumeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
        "volume_kms_key_id": "VolumeKmsKeyId",
        "root_volume": "RootVolume",
    }

    volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    root_volume: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterInstanceGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_requirements": "CapacityRequirements",
        "instance_group_name": "InstanceGroupName",
        "instance_storage_configs": "InstanceStorageConfigs",
        "kubernetes_config": "KubernetesConfig",
        "life_cycle_config": "LifeCycleConfig",
        "training_plan_arn": "TrainingPlanArn",
        "threads_per_core": "ThreadsPerCore",
        "override_vpc_config": "OverrideVpcConfig",
        "instance_count": "InstanceCount",
        "on_start_deep_health_checks": "OnStartDeepHealthChecks",
        "image_id": "ImageId",
        "current_count": "CurrentCount",
        "scheduled_update_config": "ScheduledUpdateConfig",
        "instance_type": "InstanceType",
        "execution_role": "ExecutionRole",
    }

    capacity_requirements: Optional[ClusterCapacityRequirements] = None
    instance_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_storage_configs: Optional[list[ClusterInstanceStorageConfig]] = None
    kubernetes_config: Optional[ClusterKubernetesConfig] = None
    life_cycle_config: Optional[ClusterLifeCycleConfig] = None
    training_plan_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threads_per_core: Optional[Union[int, Ref, GetAtt, Sub]] = None
    override_vpc_config: Optional[VpcConfig] = None
    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_start_deep_health_checks: Optional[Union[list[str], Ref]] = None
    image_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    current_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scheduled_update_config: Optional[ScheduledUpdateConfig] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterInstanceStorageConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_volume_config": "EbsVolumeConfig",
    }

    ebs_volume_config: Optional[ClusterEbsVolumeConfig] = None


@dataclass
class ClusterKubernetesConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "labels": "Labels",
        "taints": "Taints",
    }

    labels: Optional[dict[str, str]] = None
    taints: Optional[list[ClusterKubernetesTaint]] = None


@dataclass
class ClusterKubernetesTaint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "effect": "Effect",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effect: Optional[Union[str, ClusterKubernetesTaintEffect, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterLifeCycleConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_s3_uri": "SourceS3Uri",
        "on_create": "OnCreate",
    }

    source_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_create: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterOrchestratorEksConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_arn": "ClusterArn",
    }

    cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterRestrictedInstanceGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "override_vpc_config": "OverrideVpcConfig",
        "instance_count": "InstanceCount",
        "on_start_deep_health_checks": "OnStartDeepHealthChecks",
        "environment_config": "EnvironmentConfig",
        "instance_group_name": "InstanceGroupName",
        "instance_storage_configs": "InstanceStorageConfigs",
        "current_count": "CurrentCount",
        "training_plan_arn": "TrainingPlanArn",
        "instance_type": "InstanceType",
        "threads_per_core": "ThreadsPerCore",
        "execution_role": "ExecutionRole",
    }

    override_vpc_config: Optional[VpcConfig] = None
    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_start_deep_health_checks: Optional[Union[list[str], Ref]] = None
    environment_config: Optional[EnvironmentConfig] = None
    instance_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_storage_configs: Optional[list[ClusterInstanceStorageConfig]] = None
    current_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    training_plan_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threads_per_core: Optional[Union[int, Ref, GetAtt, Sub]] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_rollback_configuration": "AutoRollbackConfiguration",
        "rolling_update_policy": "RollingUpdatePolicy",
        "wait_interval_in_seconds": "WaitIntervalInSeconds",
    }

    auto_rollback_configuration: Optional[list[AlarmDetails]] = None
    rolling_update_policy: Optional[RollingUpdatePolicy] = None
    wait_interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "f_sx_lustre_config": "FSxLustreConfig",
    }

    f_sx_lustre_config: Optional[FSxLustreConfig] = None


@dataclass
class FSxLustreConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gi_b": "SizeInGiB",
        "per_unit_storage_throughput": "PerUnitStorageThroughput",
    }

    size_in_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    per_unit_storage_throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Orchestrator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "eks": "Eks",
    }

    eks: Optional[ClusterOrchestratorEksConfig] = None


@dataclass
class RollingUpdatePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_batch_size": "MaximumBatchSize",
        "rollback_maximum_batch_size": "RollbackMaximumBatchSize",
    }

    maximum_batch_size: Optional[CapacitySizeConfig] = None
    rollback_maximum_batch_size: Optional[CapacitySizeConfig] = None


@dataclass
class ScheduledUpdateConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
        "deployment_config": "DeploymentConfig",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deployment_config: Optional[DeploymentConfig] = None


@dataclass
class TieredStorageConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "instance_memory_allocation_percentage": "InstanceMemoryAllocationPercentage",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_memory_allocation_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnets": "Subnets",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None

