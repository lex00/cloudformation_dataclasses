"""PropertyTypes for AWS::EMR::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Application(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_info": "AdditionalInfo",
        "args": "Args",
        "name": "Name",
        "version": "Version",
    }

    additional_info: Optional[dict[str, str]] = None
    args: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AutoScalingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "rules": "Rules",
    }

    constraints: Optional[ScalingConstraints] = None
    rules: Optional[list[ScalingRule]] = None


@dataclass
class AutoTerminationPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_timeout": "IdleTimeout",
    }

    idle_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BootstrapActionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "script_bootstrap_action": "ScriptBootstrapAction",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    script_bootstrap_action: Optional[ScriptBootstrapActionConfig] = None


@dataclass
class CloudWatchAlarmDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "dimensions": "Dimensions",
        "evaluation_periods": "EvaluationPeriods",
        "metric_name": "MetricName",
        "namespace": "Namespace",
        "period": "Period",
        "statistic": "Statistic",
        "threshold": "Threshold",
        "unit": "Unit",
    }

    comparison_operator: Optional[Union[str, ComparisonOperator, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[MetricDimension]] = None
    evaluation_periods: Optional[Union[int, Ref, GetAtt, Sub]] = None
    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    statistic: Optional[Union[str, Statistic, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Unit, Ref, GetAtt, Sub]] = None


@dataclass
class ComputeLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_capacity_units": "MaximumCapacityUnits",
        "maximum_core_capacity_units": "MaximumCoreCapacityUnits",
        "maximum_on_demand_capacity_units": "MaximumOnDemandCapacityUnits",
        "minimum_capacity_units": "MinimumCapacityUnits",
        "unit_type": "UnitType",
    }

    maximum_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_core_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_on_demand_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit_type: Optional[Union[str, ComputeLimitsUnitType, Ref, GetAtt, Sub]] = None


@dataclass
class Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "classification": "Classification",
        "configuration_properties": "ConfigurationProperties",
        "configurations": "Configurations",
    }

    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_properties: Optional[dict[str, str]] = None
    configurations: Optional[list[Configuration]] = None


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_specification": "VolumeSpecification",
        "volumes_per_instance": "VolumesPerInstance",
    }

    volume_specification: Optional[VolumeSpecification] = None
    volumes_per_instance: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EbsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_block_device_configs": "EbsBlockDeviceConfigs",
        "ebs_optimized": "EbsOptimized",
    }

    ebs_block_device_configs: Optional[list[EbsBlockDeviceConfig]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HadoopJarStepConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "args": "Args",
        "jar": "Jar",
        "main_class": "MainClass",
        "step_properties": "StepProperties",
    }

    args: Optional[Union[list[str], Ref]] = None
    jar: Optional[Union[str, Ref, GetAtt, Sub]] = None
    main_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    step_properties: Optional[list[KeyValue]] = None


@dataclass
class InstanceFleetConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_type_configs": "InstanceTypeConfigs",
        "launch_specifications": "LaunchSpecifications",
        "name": "Name",
        "resize_specifications": "ResizeSpecifications",
        "target_on_demand_capacity": "TargetOnDemandCapacity",
        "target_spot_capacity": "TargetSpotCapacity",
    }

    instance_type_configs: Optional[list[InstanceTypeConfig]] = None
    launch_specifications: Optional[InstanceFleetProvisioningSpecifications] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resize_specifications: Optional[InstanceFleetResizingSpecifications] = None
    target_on_demand_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_spot_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_specification": "OnDemandSpecification",
        "spot_specification": "SpotSpecification",
    }

    on_demand_specification: Optional[OnDemandProvisioningSpecification] = None
    spot_specification: Optional[SpotProvisioningSpecification] = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_resize_specification": "OnDemandResizeSpecification",
        "spot_resize_specification": "SpotResizeSpecification",
    }

    on_demand_resize_specification: Optional[OnDemandResizingSpecification] = None
    spot_resize_specification: Optional[SpotResizingSpecification] = None


@dataclass
class InstanceGroupConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_scaling_policy": "AutoScalingPolicy",
        "bid_price": "BidPrice",
        "configurations": "Configurations",
        "custom_ami_id": "CustomAmiId",
        "ebs_configuration": "EbsConfiguration",
        "instance_count": "InstanceCount",
        "instance_type": "InstanceType",
        "market": "Market",
        "name": "Name",
    }

    auto_scaling_policy: Optional[AutoScalingPolicy] = None
    bid_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configurations: Optional[list[Configuration]] = None
    custom_ami_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_configuration: Optional[EbsConfiguration] = None
    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    market: Optional[Union[str, MarketType, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceTypeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bid_price": "BidPrice",
        "bid_price_as_percentage_of_on_demand_price": "BidPriceAsPercentageOfOnDemandPrice",
        "configurations": "Configurations",
        "custom_ami_id": "CustomAmiId",
        "ebs_configuration": "EbsConfiguration",
        "instance_type": "InstanceType",
        "priority": "Priority",
        "weighted_capacity": "WeightedCapacity",
    }

    bid_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bid_price_as_percentage_of_on_demand_price: Optional[Union[float, Ref, GetAtt, Sub]] = None
    configurations: Optional[list[Configuration]] = None
    custom_ami_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_configuration: Optional[EbsConfiguration] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[float, Ref, GetAtt, Sub]] = None
    weighted_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JobFlowInstancesConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_master_security_groups": "AdditionalMasterSecurityGroups",
        "additional_slave_security_groups": "AdditionalSlaveSecurityGroups",
        "core_instance_fleet": "CoreInstanceFleet",
        "core_instance_group": "CoreInstanceGroup",
        "ec2_key_name": "Ec2KeyName",
        "ec2_subnet_id": "Ec2SubnetId",
        "ec2_subnet_ids": "Ec2SubnetIds",
        "emr_managed_master_security_group": "EmrManagedMasterSecurityGroup",
        "emr_managed_slave_security_group": "EmrManagedSlaveSecurityGroup",
        "hadoop_version": "HadoopVersion",
        "keep_job_flow_alive_when_no_steps": "KeepJobFlowAliveWhenNoSteps",
        "master_instance_fleet": "MasterInstanceFleet",
        "master_instance_group": "MasterInstanceGroup",
        "placement": "Placement",
        "service_access_security_group": "ServiceAccessSecurityGroup",
        "task_instance_fleets": "TaskInstanceFleets",
        "task_instance_groups": "TaskInstanceGroups",
        "termination_protected": "TerminationProtected",
        "unhealthy_node_replacement": "UnhealthyNodeReplacement",
    }

    additional_master_security_groups: Optional[Union[list[str], Ref]] = None
    additional_slave_security_groups: Optional[Union[list[str], Ref]] = None
    core_instance_fleet: Optional[InstanceFleetConfig] = None
    core_instance_group: Optional[InstanceGroupConfig] = None
    ec2_key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ec2_subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ec2_subnet_ids: Optional[Union[list[str], Ref]] = None
    emr_managed_master_security_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    emr_managed_slave_security_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hadoop_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    keep_job_flow_alive_when_no_steps: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    master_instance_fleet: Optional[InstanceFleetConfig] = None
    master_instance_group: Optional[InstanceGroupConfig] = None
    placement: Optional[PlacementType] = None
    service_access_security_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task_instance_fleets: Optional[list[InstanceFleetConfig]] = None
    task_instance_groups: Optional[list[InstanceGroupConfig]] = None
    termination_protected: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    unhealthy_node_replacement: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KerberosAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_domain_join_password": "ADDomainJoinPassword",
        "ad_domain_join_user": "ADDomainJoinUser",
        "cross_realm_trust_principal_password": "CrossRealmTrustPrincipalPassword",
        "kdc_admin_password": "KdcAdminPassword",
        "realm": "Realm",
    }

    ad_domain_join_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ad_domain_join_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_realm_trust_principal_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kdc_admin_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    realm: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key": "Key",
        "value": "Value",
    }

    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedScalingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_limits": "ComputeLimits",
        "scaling_strategy": "ScalingStrategy",
        "utilization_performance_index": "UtilizationPerformanceIndex",
    }

    compute_limits: Optional[ComputeLimits] = None
    scaling_strategy: Optional[Union[str, ScalingStrategy, Ref, GetAtt, Sub]] = None
    utilization_performance_index: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key": "Key",
        "value": "Value",
    }

    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_preference": "CapacityReservationPreference",
        "capacity_reservation_resource_group_arn": "CapacityReservationResourceGroupArn",
        "usage_strategy": "UsageStrategy",
    }

    capacity_reservation_preference: Optional[Union[str, OnDemandCapacityReservationPreference, Ref, GetAtt, Sub]] = None
    capacity_reservation_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    usage_strategy: Optional[Union[str, OnDemandCapacityReservationUsageStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "capacity_reservation_options": "CapacityReservationOptions",
    }

    allocation_strategy: Optional[Union[str, OnDemandProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[OnDemandCapacityReservationOptions] = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "capacity_reservation_options": "CapacityReservationOptions",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, OnDemandProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[OnDemandCapacityReservationOptions] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PlacementGroupConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_role": "InstanceRole",
        "placement_strategy": "PlacementStrategy",
    }

    instance_role: Optional[Union[str, InstanceRoleType, Ref, GetAtt, Sub]] = None
    placement_strategy: Optional[Union[str, PlacementGroupStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class PlacementType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone": "AvailabilityZone",
    }

    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "market": "Market",
        "simple_scaling_policy_configuration": "SimpleScalingPolicyConfiguration",
    }

    market: Optional[Union[str, MarketType, Ref, GetAtt, Sub]] = None
    simple_scaling_policy_configuration: Optional[SimpleScalingPolicyConfiguration] = None


@dataclass
class ScalingConstraints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_capacity": "MaxCapacity",
        "min_capacity": "MinCapacity",
    }

    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "description": "Description",
        "name": "Name",
        "trigger": "Trigger",
    }

    action: Optional[ScalingAction] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger: Optional[ScalingTrigger] = None


@dataclass
class ScalingTrigger(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_alarm_definition": "CloudWatchAlarmDefinition",
    }

    cloud_watch_alarm_definition: Optional[CloudWatchAlarmDefinition] = None


@dataclass
class ScriptBootstrapActionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "args": "Args",
        "path": "Path",
    }

    args: Optional[Union[list[str], Ref]] = None
    path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SimpleScalingPolicyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "adjustment_type": "AdjustmentType",
        "cool_down": "CoolDown",
        "scaling_adjustment": "ScalingAdjustment",
    }

    adjustment_type: Optional[Union[str, AdjustmentType, Ref, GetAtt, Sub]] = None
    cool_down: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scaling_adjustment: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "block_duration_minutes": "BlockDurationMinutes",
        "timeout_action": "TimeoutAction",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, SpotProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    block_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout_action: Optional[Union[str, SpotProvisioningTimeoutAction, Ref, GetAtt, Sub]] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotResizingSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, SpotProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StepConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_on_failure": "ActionOnFailure",
        "hadoop_jar_step": "HadoopJarStep",
        "name": "Name",
    }

    action_on_failure: Optional[Union[str, ActionOnFailure, Ref, GetAtt, Sub]] = None
    hadoop_jar_step: Optional[HadoopJarStepConfig] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iops": "Iops",
        "size_in_gb": "SizeInGB",
        "throughput": "Throughput",
        "volume_type": "VolumeType",
    }

    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

