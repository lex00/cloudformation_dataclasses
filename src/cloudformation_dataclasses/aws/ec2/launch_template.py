"""PropertyTypes for AWS::EC2::LaunchTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AcceleratorCount(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AcceleratorTotalMemoryMiB(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BaselineEbsBandwidthMbps(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BaselinePerformanceFactors(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu": "Cpu",
    }

    cpu: Optional[Cpu] = None


@dataclass
class BlockDeviceMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs": "Ebs",
        "no_device": "NoDevice",
        "virtual_name": "VirtualName",
        "device_name": "DeviceName",
    }

    ebs: Optional[Ebs] = None
    no_device: Optional[Union[str, Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
        "capacity_reservation_resource_group_arn": "CapacityReservationResourceGroupArn",
        "capacity_reservation_id": "CapacityReservationId",
    }

    capacity_reservation_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capacity_reservation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionTrackingSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "udp_timeout": "UdpTimeout",
        "tcp_established_timeout": "TcpEstablishedTimeout",
        "udp_stream_timeout": "UdpStreamTimeout",
    }

    udp_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    tcp_established_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    udp_stream_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Cpu(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "references": "References",
    }

    references: Optional[list[Reference]] = None


@dataclass
class CpuOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "threads_per_core": "ThreadsPerCore",
        "amd_sev_snp": "AmdSevSnp",
        "core_count": "CoreCount",
    }

    threads_per_core: Optional[Union[int, Ref, GetAtt, Sub]] = None
    amd_sev_snp: Optional[Union[str, AmdSevSnpSpecification, Ref, GetAtt, Sub]] = None
    core_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CreditSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_credits": "CpuCredits",
    }

    cpu_credits: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ebs(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "iops": "Iops",
        "volume_initialization_rate": "VolumeInitializationRate",
        "volume_size": "VolumeSize",
        "delete_on_termination": "DeleteOnTermination",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_initialization_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnaSrdSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ena_srd_enabled": "EnaSrdEnabled",
        "ena_srd_udp_specification": "EnaSrdUdpSpecification",
    }

    ena_srd_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ena_srd_udp_specification: Optional[EnaSrdUdpSpecification] = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ena_srd_udp_enabled": "EnaSrdUdpEnabled",
    }

    ena_srd_udp_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnclaveOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HibernationOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configured": "Configured",
    }

    configured: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IamInstanceProfile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
        "name": "Name",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceMarketOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "spot_options": "SpotOptions",
        "market_type": "MarketType",
    }

    spot_options: Optional[SpotOptions] = None
    market_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_generations": "InstanceGenerations",
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
        "accelerator_count": "AcceleratorCount",
        "network_bandwidth_gbps": "NetworkBandwidthGbps",
        "baseline_performance_factors": "BaselinePerformanceFactors",
        "spot_max_price_percentage_over_lowest_price": "SpotMaxPricePercentageOverLowestPrice",
        "baseline_ebs_bandwidth_mbps": "BaselineEbsBandwidthMbps",
        "accelerator_names": "AcceleratorNames",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "burstable_performance": "BurstablePerformance",
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    instance_generations: Optional[Union[list[str], Ref]] = None
    memory_gi_b_per_v_cpu: Optional[MemoryGiBPerVCpu] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    v_cpu_count: Optional[VCpuCount] = None
    accelerator_manufacturers: Optional[Union[list[str], Ref]] = None
    local_storage: Optional[Union[str, LocalStorage, Ref, GetAtt, Sub]] = None
    cpu_manufacturers: Optional[Union[list[str], Ref]] = None
    bare_metal: Optional[Union[str, BareMetal, Ref, GetAtt, Sub]] = None
    require_hibernate_support: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    memory_mi_b: Optional[MemoryMiB] = None
    local_storage_types: Optional[Union[list[str], Ref]] = None
    network_interface_count: Optional[NetworkInterfaceCount] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    accelerator_count: Optional[AcceleratorCount] = None
    network_bandwidth_gbps: Optional[NetworkBandwidthGbps] = None
    baseline_performance_factors: Optional[BaselinePerformanceFactors] = None
    spot_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbps] = None
    accelerator_names: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiB] = None
    burstable_performance: Optional[Union[str, BurstablePerformance, Ref, GetAtt, Sub]] = None
    total_local_storage_gb: Optional[TotalLocalStorageGB] = None


@dataclass
class Ipv4PrefixSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv4_prefix": "Ipv4Prefix",
    }

    ipv4_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ipv6Add(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_address": "Ipv6Address",
    }

    ipv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ipv6PrefixSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_prefix": "Ipv6Prefix",
    }

    ipv6_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplateData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "tag_specifications": "TagSpecifications",
        "network_performance_options": "NetworkPerformanceOptions",
        "user_data": "UserData",
        "block_device_mappings": "BlockDeviceMappings",
        "maintenance_options": "MaintenanceOptions",
        "iam_instance_profile": "IamInstanceProfile",
        "kernel_id": "KernelId",
        "ebs_optimized": "EbsOptimized",
        "placement": "Placement",
        "network_interfaces": "NetworkInterfaces",
        "enclave_options": "EnclaveOptions",
        "image_id": "ImageId",
        "instance_type": "InstanceType",
        "monitoring": "Monitoring",
        "hibernation_options": "HibernationOptions",
        "metadata_options": "MetadataOptions",
        "license_specifications": "LicenseSpecifications",
        "instance_initiated_shutdown_behavior": "InstanceInitiatedShutdownBehavior",
        "disable_api_stop": "DisableApiStop",
        "cpu_options": "CpuOptions",
        "private_dns_name_options": "PrivateDnsNameOptions",
        "security_group_ids": "SecurityGroupIds",
        "key_name": "KeyName",
        "disable_api_termination": "DisableApiTermination",
        "instance_market_options": "InstanceMarketOptions",
        "instance_requirements": "InstanceRequirements",
        "ram_disk_id": "RamDiskId",
        "capacity_reservation_specification": "CapacityReservationSpecification",
        "credit_specification": "CreditSpecification",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    tag_specifications: Optional[list[TagSpecification]] = None
    network_performance_options: Optional[NetworkPerformanceOptions] = None
    user_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    block_device_mappings: Optional[list[BlockDeviceMapping]] = None
    maintenance_options: Optional[MaintenanceOptions] = None
    iam_instance_profile: Optional[IamInstanceProfile] = None
    kernel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    placement: Optional[Placement] = None
    network_interfaces: Optional[list[NetworkInterface]] = None
    enclave_options: Optional[EnclaveOptions] = None
    image_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring: Optional[Monitoring] = None
    hibernation_options: Optional[HibernationOptions] = None
    metadata_options: Optional[MetadataOptions] = None
    license_specifications: Optional[list[LicenseSpecification]] = None
    instance_initiated_shutdown_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disable_api_stop: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cpu_options: Optional[CpuOptions] = None
    private_dns_name_options: Optional[PrivateDnsNameOptions] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disable_api_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    instance_market_options: Optional[InstanceMarketOptions] = None
    instance_requirements: Optional[InstanceRequirements] = None
    ram_disk_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capacity_reservation_specification: Optional[CapacityReservationSpecification] = None
    credit_specification: Optional[CreditSpecification] = None


@dataclass
class LaunchTemplateTagSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class LicenseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "license_configuration_arn": "LicenseConfigurationArn",
    }

    license_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_recovery": "AutoRecovery",
    }

    auto_recovery: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryGiBPerVCpu(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryMiB(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_put_response_hop_limit": "HttpPutResponseHopLimit",
        "http_tokens": "HttpTokens",
        "http_protocol_ipv6": "HttpProtocolIpv6",
        "instance_metadata_tags": "InstanceMetadataTags",
        "http_endpoint": "HttpEndpoint",
    }

    http_put_response_hop_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_tokens: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_protocol_ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_metadata_tags: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Monitoring(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkBandwidthGbps(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterface(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "private_ip_address": "PrivateIpAddress",
        "private_ip_addresses": "PrivateIpAddresses",
        "secondary_private_ip_address_count": "SecondaryPrivateIpAddressCount",
        "ipv6_prefix_count": "Ipv6PrefixCount",
        "ipv4_prefixes": "Ipv4Prefixes",
        "device_index": "DeviceIndex",
        "primary_ipv6": "PrimaryIpv6",
        "ipv4_prefix_count": "Ipv4PrefixCount",
        "ena_queue_count": "EnaQueueCount",
        "ipv6_prefixes": "Ipv6Prefixes",
        "subnet_id": "SubnetId",
        "ipv6_addresses": "Ipv6Addresses",
        "associate_public_ip_address": "AssociatePublicIpAddress",
        "network_interface_id": "NetworkInterfaceId",
        "network_card_index": "NetworkCardIndex",
        "interface_type": "InterfaceType",
        "associate_carrier_ip_address": "AssociateCarrierIpAddress",
        "ena_srd_specification": "EnaSrdSpecification",
        "ipv6_address_count": "Ipv6AddressCount",
        "groups": "Groups",
        "delete_on_termination": "DeleteOnTermination",
        "connection_tracking_specification": "ConnectionTrackingSpecification",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_ip_addresses: Optional[list[PrivateIpAdd]] = None
    secondary_private_ip_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ipv6_prefix_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ipv4_prefixes: Optional[list[Ipv4PrefixSpecification]] = None
    device_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    primary_ipv6: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ipv4_prefix_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ena_queue_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ipv6_prefixes: Optional[list[Ipv6PrefixSpecification]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipv6_addresses: Optional[list[Ipv6Add]] = None
    associate_public_ip_address: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_card_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interface_type: Optional[Union[str, NetworkInterfaceType, Ref, GetAtt, Sub]] = None
    associate_carrier_ip_address: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ena_srd_specification: Optional[EnaSrdSpecification] = None
    ipv6_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[list[str], Ref]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    connection_tracking_specification: Optional[ConnectionTrackingSpecification] = None


@dataclass
class NetworkInterfaceCount(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkPerformanceOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bandwidth_weighting": "BandwidthWeighting",
    }

    bandwidth_weighting: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Placement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "tenancy": "Tenancy",
        "spread_domain": "SpreadDomain",
        "partition_number": "PartitionNumber",
        "availability_zone": "AvailabilityZone",
        "affinity": "Affinity",
        "host_id": "HostId",
        "host_resource_group_arn": "HostResourceGroupArn",
        "group_id": "GroupId",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tenancy: Optional[Union[str, Tenancy, Ref, GetAtt, Sub]] = None
    spread_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    partition_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    affinity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateDnsNameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_a_record": "EnableResourceNameDnsARecord",
        "hostname_type": "HostnameType",
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hostname_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_resource_name_dns_aaaa_record: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateIpAdd(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_ip_address": "PrivateIpAddress",
        "primary": "Primary",
    }

    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Reference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_family": "InstanceFamily",
    }

    instance_family: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpotOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "spot_instance_type": "SpotInstanceType",
        "instance_interruption_behavior": "InstanceInterruptionBehavior",
        "max_price": "MaxPrice",
        "block_duration_minutes": "BlockDurationMinutes",
        "valid_until": "ValidUntil",
    }

    spot_instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_interruption_behavior: Optional[Union[str, SpotInstanceInterruptionBehavior, Ref, GetAtt, Sub]] = None
    max_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    block_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    valid_until: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class TotalLocalStorageGB(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class VCpuCount(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None

