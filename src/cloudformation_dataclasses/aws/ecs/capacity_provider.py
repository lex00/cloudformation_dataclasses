"""PropertyTypes for AWS::ECS::CapacityProvider."""

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
class AutoScalingGroupProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_scaling": "ManagedScaling",
        "auto_scaling_group_arn": "AutoScalingGroupArn",
        "managed_termination_protection": "ManagedTerminationProtection",
        "managed_draining": "ManagedDraining",
    }

    managed_scaling: Optional[ManagedScaling] = None
    auto_scaling_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_termination_protection: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_draining: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InfrastructureOptimization(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_in_after": "ScaleInAfter",
    }

    scale_in_after: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceLaunchTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ec2_instance_profile_arn": "Ec2InstanceProfileArn",
        "storage_configuration": "StorageConfiguration",
        "network_configuration": "NetworkConfiguration",
        "instance_requirements": "InstanceRequirements",
        "monitoring": "Monitoring",
    }

    ec2_instance_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_configuration: Optional[ManagedInstancesStorageConfiguration] = None
    network_configuration: Optional[ManagedInstancesNetworkConfiguration] = None
    instance_requirements: Optional[InstanceRequirementsRequest] = None
    monitoring: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "local_storage_types": "LocalStorageTypes",
        "instance_generations": "InstanceGenerations",
        "network_interface_count": "NetworkInterfaceCount",
        "memory_gi_b_per_v_cpu": "MemoryGiBPerVCpu",
        "accelerator_types": "AcceleratorTypes",
        "v_cpu_count": "VCpuCount",
        "excluded_instance_types": "ExcludedInstanceTypes",
        "accelerator_manufacturers": "AcceleratorManufacturers",
        "allowed_instance_types": "AllowedInstanceTypes",
        "local_storage": "LocalStorage",
        "cpu_manufacturers": "CpuManufacturers",
        "network_bandwidth_gbps": "NetworkBandwidthGbps",
        "accelerator_count": "AcceleratorCount",
        "bare_metal": "BareMetal",
        "require_hibernate_support": "RequireHibernateSupport",
        "max_spot_price_as_percentage_of_optimal_on_demand_price": "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice",
        "spot_max_price_percentage_over_lowest_price": "SpotMaxPricePercentageOverLowestPrice",
        "baseline_ebs_bandwidth_mbps": "BaselineEbsBandwidthMbps",
        "on_demand_max_price_percentage_over_lowest_price": "OnDemandMaxPricePercentageOverLowestPrice",
        "accelerator_names": "AcceleratorNames",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "burstable_performance": "BurstablePerformance",
        "memory_mi_b": "MemoryMiB",
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    local_storage_types: Optional[Union[list[str], Ref]] = None
    instance_generations: Optional[Union[list[str], Ref]] = None
    network_interface_count: Optional[NetworkInterfaceCountRequest] = None
    memory_gi_b_per_v_cpu: Optional[MemoryGiBPerVCpuRequest] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    v_cpu_count: Optional[VCpuCountRangeRequest] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    accelerator_manufacturers: Optional[Union[list[str], Ref]] = None
    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    local_storage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu_manufacturers: Optional[Union[list[str], Ref]] = None
    network_bandwidth_gbps: Optional[NetworkBandwidthGbpsRequest] = None
    accelerator_count: Optional[AcceleratorCountRequest] = None
    bare_metal: Optional[Union[str, Ref, GetAtt, Sub]] = None
    require_hibernate_support: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    accelerator_names: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiBRequest] = None
    burstable_performance: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_mi_b: Optional[MemoryMiBRequest] = None
    total_local_storage_gb: Optional[TotalLocalStorageGBRequest] = None


@dataclass
class ManagedInstancesNetworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None


@dataclass
class ManagedInstancesProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "infrastructure_role_arn": "InfrastructureRoleArn",
        "propagate_tags": "PropagateTags",
        "infrastructure_optimization": "InfrastructureOptimization",
        "instance_launch_template": "InstanceLaunchTemplate",
    }

    infrastructure_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    propagate_tags: Optional[Union[str, Ref, GetAtt, Sub]] = None
    infrastructure_optimization: Optional[InfrastructureOptimization] = None
    instance_launch_template: Optional[InstanceLaunchTemplate] = None


@dataclass
class ManagedInstancesStorageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_size_gi_b": "StorageSizeGiB",
    }

    storage_size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedScaling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "minimum_scaling_step_size": "MinimumScalingStepSize",
        "instance_warmup_period": "InstanceWarmupPeriod",
        "target_capacity": "TargetCapacity",
        "maximum_scaling_step_size": "MaximumScalingStepSize",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_scaling_step_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_warmup_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_scaling_step_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
class TotalLocalStorageGBRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None

