"""PropertyTypes for AWS::AutoScaling::AutoScalingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AcceleratorCountRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AcceleratorTotalMemoryMiBRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AvailabilityZoneDistribution(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_distribution_strategy": "CapacityDistributionStrategy",
    }

    capacity_distribution_strategy: Optional[Union[str, CapacityDistributionStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class AvailabilityZoneImpairmentPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "zonal_shift_enabled": "ZonalShiftEnabled",
        "impaired_zone_health_check_behavior": "ImpairedZoneHealthCheckBehavior",
    }

    zonal_shift_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    impaired_zone_health_check_behavior: Optional[Union[str, ImpairedZoneHealthCheckBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu": "Cpu",
    }

    cpu: Optional[CpuPerformanceFactorRequest] = None


@dataclass
class CapacityReservationSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_preference": "CapacityReservationPreference",
        "capacity_reservation_target": "CapacityReservationTarget",
    }

    capacity_reservation_preference: Optional[Union[str, CapacityReservationPreference, Ref, GetAtt, Sub]] = None
    capacity_reservation_target: Optional[CapacityReservationTarget] = None


@dataclass
class CapacityReservationTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_ids": "CapacityReservationIds",
        "capacity_reservation_resource_group_arns": "CapacityReservationResourceGroupArns",
    }

    capacity_reservation_ids: Optional[Union[list[str], Ref]] = None
    capacity_reservation_resource_group_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "references": "References",
    }

    references: Optional[list[PerformanceFactorReferenceRequest]] = None


@dataclass
class InstanceMaintenancePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_healthy_percentage": "MaxHealthyPercentage",
        "min_healthy_percentage": "MinHealthyPercentage",
    }

    max_healthy_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_healthy_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_generations": "InstanceGenerations",
        "accelerator_types": "AcceleratorTypes",
        "memory_gi_b_per_v_cpu": "MemoryGiBPerVCpu",
        "accelerator_manufacturers": "AcceleratorManufacturers",
        "v_cpu_count": "VCpuCount",
        "local_storage": "LocalStorage",
        "cpu_manufacturers": "CpuManufacturers",
        "bare_metal": "BareMetal",
        "require_hibernate_support": "RequireHibernateSupport",
        "max_spot_price_as_percentage_of_optimal_on_demand_price": "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice",
        "on_demand_max_price_percentage_over_lowest_price": "OnDemandMaxPricePercentageOverLowestPrice",
        "memory_mi_b": "MemoryMiB",
        "local_storage_types": "LocalStorageTypes",
        "network_interface_count": "NetworkInterfaceCount",
        "excluded_instance_types": "ExcludedInstanceTypes",
        "allowed_instance_types": "AllowedInstanceTypes",
        "accelerator_count": "AcceleratorCount",
        "network_bandwidth_gbps": "NetworkBandwidthGbps",
        "baseline_performance_factors": "BaselinePerformanceFactors",
        "baseline_ebs_bandwidth_mbps": "BaselineEbsBandwidthMbps",
        "spot_max_price_percentage_over_lowest_price": "SpotMaxPricePercentageOverLowestPrice",
        "accelerator_names": "AcceleratorNames",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "burstable_performance": "BurstablePerformance",
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    instance_generations: Optional[Union[list[str], Ref]] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    memory_gi_b_per_v_cpu: Optional[MemoryGiBPerVCpuRequest] = None
    accelerator_manufacturers: Optional[Union[list[str], Ref]] = None
    v_cpu_count: Optional[VCpuCountRequest] = None
    local_storage: Optional[Union[str, LocalStorage, Ref, GetAtt, Sub]] = None
    cpu_manufacturers: Optional[Union[list[str], Ref]] = None
    bare_metal: Optional[Union[str, BareMetal, Ref, GetAtt, Sub]] = None
    require_hibernate_support: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    memory_mi_b: Optional[MemoryMiBRequest] = None
    local_storage_types: Optional[Union[list[str], Ref]] = None
    network_interface_count: Optional[NetworkInterfaceCountRequest] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    accelerator_count: Optional[AcceleratorCountRequest] = None
    network_bandwidth_gbps: Optional[NetworkBandwidthGbpsRequest] = None
    baseline_performance_factors: Optional[BaselinePerformanceFactorsRequest] = None
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    spot_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    accelerator_names: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiBRequest] = None
    burstable_performance: Optional[Union[str, BurstablePerformance, Ref, GetAtt, Sub]] = None
    total_local_storage_gb: Optional[TotalLocalStorageGBRequest] = None


@dataclass
class InstancesDistribution(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_allocation_strategy": "OnDemandAllocationStrategy",
        "on_demand_base_capacity": "OnDemandBaseCapacity",
        "on_demand_percentage_above_base_capacity": "OnDemandPercentageAboveBaseCapacity",
        "spot_instance_pools": "SpotInstancePools",
        "spot_allocation_strategy": "SpotAllocationStrategy",
        "spot_max_price": "SpotMaxPrice",
    }

    on_demand_allocation_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_demand_base_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_demand_percentage_above_base_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_instance_pools: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_allocation_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    spot_max_price: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_specification": "LaunchTemplateSpecification",
        "overrides": "Overrides",
    }

    launch_template_specification: Optional[LaunchTemplateSpecification] = None
    overrides: Optional[list[LaunchTemplateOverrides]] = None


@dataclass
class LaunchTemplateOverrides(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_specification": "LaunchTemplateSpecification",
        "weighted_capacity": "WeightedCapacity",
        "instance_requirements": "InstanceRequirements",
        "instance_type": "InstanceType",
    }

    launch_template_specification: Optional[LaunchTemplateSpecification] = None
    weighted_capacity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_requirements: Optional[InstanceRequirements] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "launch_template_id": "LaunchTemplateId",
    }

    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleHookSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle_hook_name": "LifecycleHookName",
        "lifecycle_transition": "LifecycleTransition",
        "heartbeat_timeout": "HeartbeatTimeout",
        "notification_metadata": "NotificationMetadata",
        "default_result": "DefaultResult",
        "notification_target_arn": "NotificationTargetARN",
        "role_arn": "RoleARN",
    }

    lifecycle_hook_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lifecycle_transition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    heartbeat_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    notification_metadata: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_result: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryMiBRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsCollection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metrics": "Metrics",
        "granularity": "Granularity",
    }

    metrics: Optional[Union[list[str], Ref]] = None
    granularity: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MixedInstancesPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instances_distribution": "InstancesDistribution",
        "launch_template": "LaunchTemplate",
    }

    instances_distribution: Optional[InstancesDistribution] = None
    launch_template: Optional[LaunchTemplate] = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicARN",
        "notification_types": "NotificationTypes",
    }

    topic_arn: Optional[Union[list[str], Ref]] = None
    notification_types: Optional[Union[list[str], Ref]] = None


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_family": "InstanceFamily",
    }

    instance_family: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
        "propagate_at_launch": "PropagateAtLaunch",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    propagate_at_launch: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TrafficSourceIdentifier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "identifier": "Identifier",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VCpuCountRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None

