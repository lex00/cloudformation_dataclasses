"""PropertyTypes for AWS::EC2::SpotFleet."""

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
class BlockDeviceMapping(PropertyType):
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
class ClassicLoadBalancer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClassicLoadBalancersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "classic_load_balancers": "ClassicLoadBalancers",
    }

    classic_load_balancers: Optional[list[ClassicLoadBalancer]] = None


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "references": "References",
    }

    references: Optional[list[PerformanceFactorReferenceRequest]] = None


@dataclass
class EbsBlockDevice(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "encrypted": "Encrypted",
        "iops": "Iops",
        "volume_size": "VolumeSize",
        "delete_on_termination": "DeleteOnTermination",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, VolumeType, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FleetLaunchTemplateSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "launch_template_id": "LaunchTemplateId",
    }

    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GroupIdentifier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_id": "GroupId",
    }

    group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamInstanceProfileSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceIpv6Address(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_address": "Ipv6Address",
    }

    ipv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceNetworkInterfaceSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "private_ip_addresses": "PrivateIpAddresses",
        "secondary_private_ip_address_count": "SecondaryPrivateIpAddressCount",
        "device_index": "DeviceIndex",
        "groups": "Groups",
        "ipv6_address_count": "Ipv6AddressCount",
        "ipv6_addresses": "Ipv6Addresses",
        "subnet_id": "SubnetId",
        "associate_public_ip_address": "AssociatePublicIpAddress",
        "network_interface_id": "NetworkInterfaceId",
        "delete_on_termination": "DeleteOnTermination",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_ip_addresses: Optional[list[PrivateIpAddressSpecification]] = None
    secondary_private_ip_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    device_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[list[str], Ref]] = None
    ipv6_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ipv6_addresses: Optional[list[InstanceIpv6Address]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    associate_public_ip_address: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
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
class LaunchTemplateConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_specification": "LaunchTemplateSpecification",
        "overrides": "Overrides",
    }

    launch_template_specification: Optional[FleetLaunchTemplateSpecification] = None
    overrides: Optional[list[LaunchTemplateOverrides]] = None


@dataclass
class LaunchTemplateOverrides(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "spot_price": "SpotPrice",
        "weighted_capacity": "WeightedCapacity",
        "priority": "Priority",
        "availability_zone": "AvailabilityZone",
        "subnet_id": "SubnetId",
        "instance_requirements": "InstanceRequirements",
        "instance_type": "InstanceType",
    }

    spot_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weighted_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[float, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_requirements: Optional[InstanceRequirementsRequest] = None
    instance_type: Optional[Union[str, InstanceType, Ref, GetAtt, Sub]] = None


@dataclass
class LoadBalancersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "classic_load_balancers_config": "ClassicLoadBalancersConfig",
        "target_groups_config": "TargetGroupsConfig",
    }

    classic_load_balancers_config: Optional[ClassicLoadBalancersConfig] = None
    target_groups_config: Optional[TargetGroupsConfig] = None


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
class PerformanceFactorReferenceRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_family": "InstanceFamily",
    }

    instance_family: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_ip_address": "PrivateIpAddress",
        "primary": "Primary",
    }

    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SpotCapacityRebalance(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "termination_delay": "TerminationDelay",
        "replacement_strategy": "ReplacementStrategy",
    }

    termination_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    replacement_strategy: Optional[Union[str, ReplacementStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class SpotFleetLaunchSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "tag_specifications": "TagSpecifications",
        "user_data": "UserData",
        "block_device_mappings": "BlockDeviceMappings",
        "iam_instance_profile": "IamInstanceProfile",
        "kernel_id": "KernelId",
        "subnet_id": "SubnetId",
        "ebs_optimized": "EbsOptimized",
        "key_name": "KeyName",
        "ramdisk_id": "RamdiskId",
        "spot_price": "SpotPrice",
        "weighted_capacity": "WeightedCapacity",
        "placement": "Placement",
        "network_interfaces": "NetworkInterfaces",
        "image_id": "ImageId",
        "instance_requirements": "InstanceRequirements",
        "instance_type": "InstanceType",
        "monitoring": "Monitoring",
    }

    security_groups: Optional[list[GroupIdentifier]] = None
    tag_specifications: Optional[list[SpotFleetTagSpecification]] = None
    user_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    block_device_mappings: Optional[list[BlockDeviceMapping]] = None
    iam_instance_profile: Optional[IamInstanceProfileSpecification] = None
    kernel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ramdisk_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    spot_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weighted_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    placement: Optional[SpotPlacement] = None
    network_interfaces: Optional[list[InstanceNetworkInterfaceSpecification]] = None
    image_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_requirements: Optional[InstanceRequirementsRequest] = None
    instance_type: Optional[Union[str, InstanceType, Ref, GetAtt, Sub]] = None
    monitoring: Optional[SpotFleetMonitoring] = None


@dataclass
class SpotFleetMonitoring(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SpotFleetRequestConfigData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "context": "Context",
        "spot_max_total_price": "SpotMaxTotalPrice",
        "excess_capacity_termination_policy": "ExcessCapacityTerminationPolicy",
        "tag_specifications": "TagSpecifications",
        "instance_pools_to_use_count": "InstancePoolsToUseCount",
        "launch_template_configs": "LaunchTemplateConfigs",
        "target_capacity_unit_type": "TargetCapacityUnitType",
        "iam_fleet_role": "IamFleetRole",
        "spot_maintenance_strategies": "SpotMaintenanceStrategies",
        "terminate_instances_with_expiration": "TerminateInstancesWithExpiration",
        "valid_until": "ValidUntil",
        "on_demand_max_total_price": "OnDemandMaxTotalPrice",
        "on_demand_allocation_strategy": "OnDemandAllocationStrategy",
        "spot_price": "SpotPrice",
        "allocation_strategy": "AllocationStrategy",
        "on_demand_target_capacity": "OnDemandTargetCapacity",
        "type_": "Type",
        "launch_specifications": "LaunchSpecifications",
        "instance_interruption_behavior": "InstanceInterruptionBehavior",
        "load_balancers_config": "LoadBalancersConfig",
        "valid_from": "ValidFrom",
        "replace_unhealthy_instances": "ReplaceUnhealthyInstances",
        "target_capacity": "TargetCapacity",
    }

    context: Optional[Union[str, Ref, GetAtt, Sub]] = None
    spot_max_total_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    excess_capacity_termination_policy: Optional[Union[str, ExcessCapacityTerminationPolicy, Ref, GetAtt, Sub]] = None
    tag_specifications: Optional[list[SpotFleetTagSpecification]] = None
    instance_pools_to_use_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    launch_template_configs: Optional[list[LaunchTemplateConfig]] = None
    target_capacity_unit_type: Optional[Union[str, TargetCapacityUnitType, Ref, GetAtt, Sub]] = None
    iam_fleet_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    spot_maintenance_strategies: Optional[SpotMaintenanceStrategies] = None
    terminate_instances_with_expiration: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    valid_until: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_demand_max_total_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_demand_allocation_strategy: Optional[Union[str, OnDemandAllocationStrategy, Ref, GetAtt, Sub]] = None
    spot_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allocation_strategy: Optional[Union[str, AllocationStrategy, Ref, GetAtt, Sub]] = None
    on_demand_target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, FleetType, Ref, GetAtt, Sub]] = None
    launch_specifications: Optional[list[SpotFleetLaunchSpecification]] = None
    instance_interruption_behavior: Optional[Union[str, InstanceInterruptionBehavior, Ref, GetAtt, Sub]] = None
    load_balancers_config: Optional[LoadBalancersConfig] = None
    valid_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replace_unhealthy_instances: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotFleetTagSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class SpotMaintenanceStrategies(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_rebalance": "CapacityRebalance",
    }

    capacity_rebalance: Optional[SpotCapacityRebalance] = None


@dataclass
class SpotPlacement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "tenancy": "Tenancy",
        "availability_zone": "AvailabilityZone",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tenancy: Optional[Union[str, Tenancy, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_groups": "TargetGroups",
    }

    target_groups: Optional[list[TargetGroup]] = None


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

