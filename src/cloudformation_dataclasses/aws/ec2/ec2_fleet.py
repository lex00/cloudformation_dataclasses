"""PropertyTypes for AWS::EC2::EC2Fleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AcceleratorCountRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AcceleratorTotalMemoryMiBRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    CPU = "Cpu"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu": "Cpu",
    }

    cpu: Optional[CpuPerformanceFactorRequest] = None


@dataclass
class BlockDeviceMapping(PropertyType):
    EBS = "Ebs"
    NO_DEVICE = "NoDevice"
    VIRTUAL_NAME = "VirtualName"
    DEVICE_NAME = "DeviceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs": "Ebs",
        "no_device": "NoDevice",
        "virtual_name": "VirtualName",
        "device_name": "DeviceName",
    }

    ebs: Optional[EbsBlockDevice] = None
    no_device: Optional[Union[str, Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityRebalance(PropertyType):
    TERMINATION_DELAY = "TerminationDelay"
    REPLACEMENT_STRATEGY = "ReplacementStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "termination_delay": "TerminationDelay",
        "replacement_strategy": "ReplacementStrategy",
    }

    termination_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    replacement_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityReservationOptionsRequest(PropertyType):
    USAGE_STRATEGY = "UsageStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "usage_strategy": "UsageStrategy",
    }

    usage_strategy: Optional[Union[str, FleetCapacityReservationUsageStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    REFERENCES = "References"

    _property_mappings: ClassVar[dict[str, str]] = {
        "references": "References",
    }

    references: Optional[list[PerformanceFactorReferenceRequest]] = None


@dataclass
class EbsBlockDevice(PropertyType):
    SNAPSHOT_ID = "SnapshotId"
    VOLUME_TYPE = "VolumeType"
    KMS_KEY_ID = "KmsKeyId"
    ENCRYPTED = "Encrypted"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"
    DELETE_ON_TERMINATION = "DeleteOnTermination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "encrypted": "Encrypted",
        "iops": "Iops",
        "volume_size": "VolumeSize",
        "delete_on_termination": "DeleteOnTermination",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, VolumeType, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FleetLaunchTemplateConfigRequest(PropertyType):
    LAUNCH_TEMPLATE_SPECIFICATION = "LaunchTemplateSpecification"
    OVERRIDES = "Overrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_specification": "LaunchTemplateSpecification",
        "overrides": "Overrides",
    }

    launch_template_specification: Optional[FleetLaunchTemplateSpecificationRequest] = None
    overrides: Optional[list[FleetLaunchTemplateOverridesRequest]] = None


@dataclass
class FleetLaunchTemplateOverridesRequest(PropertyType):
    WEIGHTED_CAPACITY = "WeightedCapacity"
    PLACEMENT = "Placement"
    PRIORITY = "Priority"
    BLOCK_DEVICE_MAPPINGS = "BlockDeviceMappings"
    AVAILABILITY_ZONE = "AvailabilityZone"
    SUBNET_ID = "SubnetId"
    INSTANCE_REQUIREMENTS = "InstanceRequirements"
    INSTANCE_TYPE = "InstanceType"
    MAX_PRICE = "MaxPrice"

    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_capacity": "WeightedCapacity",
        "placement": "Placement",
        "priority": "Priority",
        "block_device_mappings": "BlockDeviceMappings",
        "availability_zone": "AvailabilityZone",
        "subnet_id": "SubnetId",
        "instance_requirements": "InstanceRequirements",
        "instance_type": "InstanceType",
        "max_price": "MaxPrice",
    }

    weighted_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    placement: Optional[Placement] = None
    priority: Optional[Union[float, Ref, GetAtt, Sub]] = None
    block_device_mappings: Optional[list[BlockDeviceMapping]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_requirements: Optional[InstanceRequirementsRequest] = None
    instance_type: Optional[Union[str, InstanceType, Ref, GetAtt, Sub]] = None
    max_price: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FleetLaunchTemplateSpecificationRequest(PropertyType):
    LAUNCH_TEMPLATE_NAME = "LaunchTemplateName"
    VERSION = "Version"
    LAUNCH_TEMPLATE_ID = "LaunchTemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "launch_template_id": "LaunchTemplateId",
    }

    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    INSTANCE_GENERATIONS = "InstanceGenerations"
    REQUIRE_ENCRYPTION_IN_TRANSIT = "RequireEncryptionInTransit"
    MEMORY_GI_B_PER_V_CPU = "MemoryGiBPerVCpu"
    ACCELERATOR_TYPES = "AcceleratorTypes"
    V_CPU_COUNT = "VCpuCount"
    ACCELERATOR_MANUFACTURERS = "AcceleratorManufacturers"
    LOCAL_STORAGE = "LocalStorage"
    CPU_MANUFACTURERS = "CpuManufacturers"
    BARE_METAL = "BareMetal"
    REQUIRE_HIBERNATE_SUPPORT = "RequireHibernateSupport"
    MAX_SPOT_PRICE_AS_PERCENTAGE_OF_OPTIMAL_ON_DEMAND_PRICE = "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    ON_DEMAND_MAX_PRICE_PERCENTAGE_OVER_LOWEST_PRICE = "OnDemandMaxPricePercentageOverLowestPrice"
    MEMORY_MI_B = "MemoryMiB"
    LOCAL_STORAGE_TYPES = "LocalStorageTypes"
    NETWORK_INTERFACE_COUNT = "NetworkInterfaceCount"
    EXCLUDED_INSTANCE_TYPES = "ExcludedInstanceTypes"
    ALLOWED_INSTANCE_TYPES = "AllowedInstanceTypes"
    NETWORK_BANDWIDTH_GBPS = "NetworkBandwidthGbps"
    ACCELERATOR_COUNT = "AcceleratorCount"
    BASELINE_PERFORMANCE_FACTORS = "BaselinePerformanceFactors"
    SPOT_MAX_PRICE_PERCENTAGE_OVER_LOWEST_PRICE = "SpotMaxPricePercentageOverLowestPrice"
    BASELINE_EBS_BANDWIDTH_MBPS = "BaselineEbsBandwidthMbps"
    ACCELERATOR_NAMES = "AcceleratorNames"
    ACCELERATOR_TOTAL_MEMORY_MI_B = "AcceleratorTotalMemoryMiB"
    BURSTABLE_PERFORMANCE = "BurstablePerformance"
    TOTAL_LOCAL_STORAGE_GB = "TotalLocalStorageGB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_generations": "InstanceGenerations",
        "require_encryption_in_transit": "RequireEncryptionInTransit",
        "memory_gi_b_per_v_cpu": "MemoryGiBPerVCpu",
        "accelerator_types": "AcceleratorTypes",
        "v_cpu_count": "VCpuCount",
        "accelerator_manufacturers": "AcceleratorManufacturers",
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
        "network_bandwidth_gbps": "NetworkBandwidthGbps",
        "accelerator_count": "AcceleratorCount",
        "baseline_performance_factors": "BaselinePerformanceFactors",
        "spot_max_price_percentage_over_lowest_price": "SpotMaxPricePercentageOverLowestPrice",
        "baseline_ebs_bandwidth_mbps": "BaselineEbsBandwidthMbps",
        "accelerator_names": "AcceleratorNames",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "burstable_performance": "BurstablePerformance",
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    instance_generations: Optional[Union[list[str], Ref]] = None
    require_encryption_in_transit: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    memory_gi_b_per_v_cpu: Optional[MemoryGiBPerVCpuRequest] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    v_cpu_count: Optional[VCpuCountRangeRequest] = None
    accelerator_manufacturers: Optional[Union[list[str], Ref]] = None
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
    network_bandwidth_gbps: Optional[NetworkBandwidthGbpsRequest] = None
    accelerator_count: Optional[AcceleratorCountRequest] = None
    baseline_performance_factors: Optional[BaselinePerformanceFactorsRequest] = None
    spot_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    accelerator_names: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiBRequest] = None
    burstable_performance: Optional[Union[str, BurstablePerformance, Ref, GetAtt, Sub]] = None
    total_local_storage_gb: Optional[TotalLocalStorageGBRequest] = None


@dataclass
class MaintenanceStrategies(PropertyType):
    CAPACITY_REBALANCE = "CapacityRebalance"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_rebalance": "CapacityRebalance",
    }

    capacity_rebalance: Optional[CapacityRebalance] = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryMiBRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandOptionsRequest(PropertyType):
    SINGLE_AVAILABILITY_ZONE = "SingleAvailabilityZone"
    ALLOCATION_STRATEGY = "AllocationStrategy"
    SINGLE_INSTANCE_TYPE = "SingleInstanceType"
    MIN_TARGET_CAPACITY = "MinTargetCapacity"
    MAX_TOTAL_PRICE = "MaxTotalPrice"
    CAPACITY_RESERVATION_OPTIONS = "CapacityReservationOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "single_availability_zone": "SingleAvailabilityZone",
        "allocation_strategy": "AllocationStrategy",
        "single_instance_type": "SingleInstanceType",
        "min_target_capacity": "MinTargetCapacity",
        "max_total_price": "MaxTotalPrice",
        "capacity_reservation_options": "CapacityReservationOptions",
    }

    single_availability_zone: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    allocation_strategy: Optional[Union[str, FleetOnDemandAllocationStrategy, Ref, GetAtt, Sub]] = None
    single_instance_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    min_target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_total_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[CapacityReservationOptionsRequest] = None


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    INSTANCE_FAMILY = "InstanceFamily"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_family": "InstanceFamily",
    }

    instance_family: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Placement(PropertyType):
    GROUP_NAME = "GroupName"
    TENANCY = "Tenancy"
    SPREAD_DOMAIN = "SpreadDomain"
    PARTITION_NUMBER = "PartitionNumber"
    AVAILABILITY_ZONE = "AvailabilityZone"
    AFFINITY = "Affinity"
    HOST_ID = "HostId"
    HOST_RESOURCE_GROUP_ARN = "HostResourceGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "tenancy": "Tenancy",
        "spread_domain": "SpreadDomain",
        "partition_number": "PartitionNumber",
        "availability_zone": "AvailabilityZone",
        "affinity": "Affinity",
        "host_id": "HostId",
        "host_resource_group_arn": "HostResourceGroupArn",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tenancy: Optional[Union[str, Tenancy, Ref, GetAtt, Sub]] = None
    spread_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    partition_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    affinity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpotOptionsRequest(PropertyType):
    SINGLE_AVAILABILITY_ZONE = "SingleAvailabilityZone"
    ALLOCATION_STRATEGY = "AllocationStrategy"
    SINGLE_INSTANCE_TYPE = "SingleInstanceType"
    MIN_TARGET_CAPACITY = "MinTargetCapacity"
    MAX_TOTAL_PRICE = "MaxTotalPrice"
    MAINTENANCE_STRATEGIES = "MaintenanceStrategies"
    INSTANCE_INTERRUPTION_BEHAVIOR = "InstanceInterruptionBehavior"
    INSTANCE_POOLS_TO_USE_COUNT = "InstancePoolsToUseCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "single_availability_zone": "SingleAvailabilityZone",
        "allocation_strategy": "AllocationStrategy",
        "single_instance_type": "SingleInstanceType",
        "min_target_capacity": "MinTargetCapacity",
        "max_total_price": "MaxTotalPrice",
        "maintenance_strategies": "MaintenanceStrategies",
        "instance_interruption_behavior": "InstanceInterruptionBehavior",
        "instance_pools_to_use_count": "InstancePoolsToUseCount",
    }

    single_availability_zone: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    allocation_strategy: Optional[Union[str, SpotAllocationStrategy, Ref, GetAtt, Sub]] = None
    single_instance_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    min_target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_total_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maintenance_strategies: Optional[MaintenanceStrategies] = None
    instance_interruption_behavior: Optional[Union[str, SpotInstanceInterruptionBehavior, Ref, GetAtt, Sub]] = None
    instance_pools_to_use_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TagSpecification(PropertyType):
    RESOURCE_TYPE = "ResourceType"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class TargetCapacitySpecificationRequest(PropertyType):
    DEFAULT_TARGET_CAPACITY_TYPE = "DefaultTargetCapacityType"
    TOTAL_TARGET_CAPACITY = "TotalTargetCapacity"
    ON_DEMAND_TARGET_CAPACITY = "OnDemandTargetCapacity"
    SPOT_TARGET_CAPACITY = "SpotTargetCapacity"
    TARGET_CAPACITY_UNIT_TYPE = "TargetCapacityUnitType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_target_capacity_type": "DefaultTargetCapacityType",
        "total_target_capacity": "TotalTargetCapacity",
        "on_demand_target_capacity": "OnDemandTargetCapacity",
        "spot_target_capacity": "SpotTargetCapacity",
        "target_capacity_unit_type": "TargetCapacityUnitType",
    }

    default_target_capacity_type: Optional[Union[str, DefaultTargetCapacityType, Ref, GetAtt, Sub]] = None
    total_target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_demand_target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_capacity_unit_type: Optional[Union[str, TargetCapacityUnitType, Ref, GetAtt, Sub]] = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None

