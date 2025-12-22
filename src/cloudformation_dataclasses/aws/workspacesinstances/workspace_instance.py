"""PropertyTypes for AWS::WorkspacesInstances::WorkspaceInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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
class CapacityReservationSpecification(PropertyType):
    CAPACITY_RESERVATION_PREFERENCE = "CapacityReservationPreference"
    CAPACITY_RESERVATION_TARGET = "CapacityReservationTarget"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_preference": "CapacityReservationPreference",
        "capacity_reservation_target": "CapacityReservationTarget",
    }

    capacity_reservation_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capacity_reservation_target: Optional[CapacityReservationTarget] = None


@dataclass
class CapacityReservationTarget(PropertyType):
    CAPACITY_RESERVATION_RESOURCE_GROUP_ARN = "CapacityReservationResourceGroupArn"
    CAPACITY_RESERVATION_ID = "CapacityReservationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_resource_group_arn": "CapacityReservationResourceGroupArn",
        "capacity_reservation_id": "CapacityReservationId",
    }

    capacity_reservation_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capacity_reservation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CpuOptionsRequest(PropertyType):
    THREADS_PER_CORE = "ThreadsPerCore"
    CORE_COUNT = "CoreCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "threads_per_core": "ThreadsPerCore",
        "core_count": "CoreCount",
    }

    threads_per_core: Optional[Union[int, Ref, GetAtt, Sub]] = None
    core_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CreditSpecificationRequest(PropertyType):
    CPU_CREDITS = "CpuCredits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_credits": "CpuCredits",
    }

    cpu_credits: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EC2ManagedInstance(PropertyType):
    INSTANCE_ID = "InstanceId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_id": "InstanceId",
    }

    instance_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EbsBlockDevice(PropertyType):
    VOLUME_TYPE = "VolumeType"
    KMS_KEY_ID = "KmsKeyId"
    ENCRYPTED = "Encrypted"
    THROUGHPUT = "Throughput"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "iops": "Iops",
        "volume_size": "VolumeSize",
    }

    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EnclaveOptionsRequest(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HibernationOptionsRequest(PropertyType):
    CONFIGURED = "Configured"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configured": "Configured",
    }

    configured: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IamInstanceProfileSpecification(PropertyType):
    ARN = "Arn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
        "name": "Name",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceMaintenanceOptionsRequest(PropertyType):
    AUTO_RECOVERY = "AutoRecovery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_recovery": "AutoRecovery",
    }

    auto_recovery: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceMarketOptionsRequest(PropertyType):
    SPOT_OPTIONS = "SpotOptions"
    MARKET_TYPE = "MarketType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "spot_options": "SpotOptions",
        "market_type": "MarketType",
    }

    spot_options: Optional[SpotMarketOptions] = None
    market_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceMetadataOptionsRequest(PropertyType):
    HTTP_PUT_RESPONSE_HOP_LIMIT = "HttpPutResponseHopLimit"
    HTTP_PROTOCOL_IPV6 = "HttpProtocolIpv6"
    HTTP_TOKENS = "HttpTokens"
    INSTANCE_METADATA_TAGS = "InstanceMetadataTags"
    HTTP_ENDPOINT = "HttpEndpoint"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_put_response_hop_limit": "HttpPutResponseHopLimit",
        "http_protocol_ipv6": "HttpProtocolIpv6",
        "http_tokens": "HttpTokens",
        "instance_metadata_tags": "InstanceMetadataTags",
        "http_endpoint": "HttpEndpoint",
    }

    http_put_response_hop_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_protocol_ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_tokens: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_metadata_tags: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceNetworkInterfaceSpecification(PropertyType):
    DESCRIPTION = "Description"
    DEVICE_INDEX = "DeviceIndex"
    GROUPS = "Groups"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "device_index": "DeviceIndex",
        "groups": "Groups",
        "subnet_id": "SubnetId",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[list[str], Ref]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceNetworkPerformanceOptionsRequest(PropertyType):
    BANDWIDTH_WEIGHTING = "BandwidthWeighting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bandwidth_weighting": "BandwidthWeighting",
    }

    bandwidth_weighting: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LicenseConfigurationRequest(PropertyType):
    LICENSE_CONFIGURATION_ARN = "LicenseConfigurationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "license_configuration_arn": "LicenseConfigurationArn",
    }

    license_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedInstance(PropertyType):
    NETWORK_PERFORMANCE_OPTIONS = "NetworkPerformanceOptions"
    TAG_SPECIFICATIONS = "TagSpecifications"
    USER_DATA = "UserData"
    BLOCK_DEVICE_MAPPINGS = "BlockDeviceMappings"
    MAINTENANCE_OPTIONS = "MaintenanceOptions"
    IAM_INSTANCE_PROFILE = "IamInstanceProfile"
    SUBNET_ID = "SubnetId"
    EBS_OPTIMIZED = "EbsOptimized"
    PLACEMENT = "Placement"
    IPV6_ADDRESS_COUNT = "Ipv6AddressCount"
    ENCLAVE_OPTIONS = "EnclaveOptions"
    NETWORK_INTERFACES = "NetworkInterfaces"
    IMAGE_ID = "ImageId"
    INSTANCE_TYPE = "InstanceType"
    MONITORING = "Monitoring"
    HIBERNATION_OPTIONS = "HibernationOptions"
    LICENSE_SPECIFICATIONS = "LicenseSpecifications"
    METADATA_OPTIONS = "MetadataOptions"
    DISABLE_API_STOP = "DisableApiStop"
    CPU_OPTIONS = "CpuOptions"
    PRIVATE_DNS_NAME_OPTIONS = "PrivateDnsNameOptions"
    ENABLE_PRIMARY_IPV6 = "EnablePrimaryIpv6"
    KEY_NAME = "KeyName"
    INSTANCE_MARKET_OPTIONS = "InstanceMarketOptions"
    CAPACITY_RESERVATION_SPECIFICATION = "CapacityReservationSpecification"
    CREDIT_SPECIFICATION = "CreditSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_performance_options": "NetworkPerformanceOptions",
        "tag_specifications": "TagSpecifications",
        "user_data": "UserData",
        "block_device_mappings": "BlockDeviceMappings",
        "maintenance_options": "MaintenanceOptions",
        "iam_instance_profile": "IamInstanceProfile",
        "subnet_id": "SubnetId",
        "ebs_optimized": "EbsOptimized",
        "placement": "Placement",
        "ipv6_address_count": "Ipv6AddressCount",
        "enclave_options": "EnclaveOptions",
        "network_interfaces": "NetworkInterfaces",
        "image_id": "ImageId",
        "instance_type": "InstanceType",
        "monitoring": "Monitoring",
        "hibernation_options": "HibernationOptions",
        "license_specifications": "LicenseSpecifications",
        "metadata_options": "MetadataOptions",
        "disable_api_stop": "DisableApiStop",
        "cpu_options": "CpuOptions",
        "private_dns_name_options": "PrivateDnsNameOptions",
        "enable_primary_ipv6": "EnablePrimaryIpv6",
        "key_name": "KeyName",
        "instance_market_options": "InstanceMarketOptions",
        "capacity_reservation_specification": "CapacityReservationSpecification",
        "credit_specification": "CreditSpecification",
    }

    network_performance_options: Optional[InstanceNetworkPerformanceOptionsRequest] = None
    tag_specifications: Optional[list[TagSpecification]] = None
    user_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    block_device_mappings: Optional[list[BlockDeviceMapping]] = None
    maintenance_options: Optional[InstanceMaintenanceOptionsRequest] = None
    iam_instance_profile: Optional[IamInstanceProfileSpecification] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    placement: Optional[Placement] = None
    ipv6_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enclave_options: Optional[EnclaveOptionsRequest] = None
    network_interfaces: Optional[list[InstanceNetworkInterfaceSpecification]] = None
    image_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring: Optional[RunInstancesMonitoringEnabled] = None
    hibernation_options: Optional[HibernationOptionsRequest] = None
    license_specifications: Optional[list[LicenseConfigurationRequest]] = None
    metadata_options: Optional[InstanceMetadataOptionsRequest] = None
    disable_api_stop: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cpu_options: Optional[CpuOptionsRequest] = None
    private_dns_name_options: Optional[PrivateDnsNameOptionsRequest] = None
    enable_primary_ipv6: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_market_options: Optional[InstanceMarketOptionsRequest] = None
    capacity_reservation_specification: Optional[CapacityReservationSpecification] = None
    credit_specification: Optional[CreditSpecificationRequest] = None


@dataclass
class Placement(PropertyType):
    GROUP_NAME = "GroupName"
    TENANCY = "Tenancy"
    PARTITION_NUMBER = "PartitionNumber"
    AVAILABILITY_ZONE = "AvailabilityZone"
    GROUP_ID = "GroupId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "tenancy": "Tenancy",
        "partition_number": "PartitionNumber",
        "availability_zone": "AvailabilityZone",
        "group_id": "GroupId",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tenancy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    partition_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateDnsNameOptionsRequest(PropertyType):
    ENABLE_RESOURCE_NAME_DNS_A_RECORD = "EnableResourceNameDnsARecord"
    HOSTNAME_TYPE = "HostnameType"
    ENABLE_RESOURCE_NAME_DNS_AAAA_RECORD = "EnableResourceNameDnsAAAARecord"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_a_record": "EnableResourceNameDnsARecord",
        "hostname_type": "HostnameType",
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hostname_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_resource_name_dns_aaaa_record: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RunInstancesMonitoringEnabled(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SpotMarketOptions(PropertyType):
    VALID_UNTIL_UTC = "ValidUntilUtc"
    SPOT_INSTANCE_TYPE = "SpotInstanceType"
    INSTANCE_INTERRUPTION_BEHAVIOR = "InstanceInterruptionBehavior"
    MAX_PRICE = "MaxPrice"

    _property_mappings: ClassVar[dict[str, str]] = {
        "valid_until_utc": "ValidUntilUtc",
        "spot_instance_type": "SpotInstanceType",
        "instance_interruption_behavior": "InstanceInterruptionBehavior",
        "max_price": "MaxPrice",
    }

    valid_until_utc: Optional[Union[str, Ref, GetAtt, Sub]] = None
    spot_instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_interruption_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_price: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagSpecification(PropertyType):
    RESOURCE_TYPE = "ResourceType"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None

