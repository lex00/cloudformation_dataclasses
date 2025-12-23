"""PropertyTypes for AWS::EC2::Instance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssociationParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

    ebs: Optional[Ebs] = None
    no_device: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CpuOptions(PropertyType):
    THREADS_PER_CORE = "ThreadsPerCore"
    CORE_COUNT = "CoreCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "threads_per_core": "ThreadsPerCore",
        "core_count": "CoreCount",
    }

    threads_per_core: Optional[Union[int, Ref, GetAtt, Sub]] = None
    core_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CreditSpecification(PropertyType):
    CPU_CREDITS = "CPUCredits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_credits": "CPUCredits",
    }

    cpu_credits: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ebs(PropertyType):
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
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticGpuSpecification(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticInferenceAccelerator(PropertyType):
    TYPE = "Type"
    COUNT = "Count"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "count": "Count",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EnaSrdSpecification(PropertyType):
    ENA_SRD_ENABLED = "EnaSrdEnabled"
    ENA_SRD_UDP_SPECIFICATION = "EnaSrdUdpSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ena_srd_enabled": "EnaSrdEnabled",
        "ena_srd_udp_specification": "EnaSrdUdpSpecification",
    }

    ena_srd_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ena_srd_udp_specification: Optional[EnaSrdUdpSpecification] = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    ENA_SRD_UDP_ENABLED = "EnaSrdUdpEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ena_srd_udp_enabled": "EnaSrdUdpEnabled",
    }

    ena_srd_udp_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnclaveOptions(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HibernationOptions(PropertyType):
    CONFIGURED = "Configured"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configured": "Configured",
    }

    configured: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceIpv6Address(PropertyType):
    IPV6_ADDRESS = "Ipv6Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_address": "Ipv6Address",
    }

    ipv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
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
class LicenseSpecification(PropertyType):
    LICENSE_CONFIGURATION_ARN = "LicenseConfigurationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "license_configuration_arn": "LicenseConfigurationArn",
    }

    license_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataOptions(PropertyType):
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
class NetworkInterface(PropertyType):
    DESCRIPTION = "Description"
    PRIVATE_IP_ADDRESS = "PrivateIpAddress"
    PRIVATE_IP_ADDRESSES = "PrivateIpAddresses"
    SECONDARY_PRIVATE_IP_ADDRESS_COUNT = "SecondaryPrivateIpAddressCount"
    DEVICE_INDEX = "DeviceIndex"
    GROUP_SET = "GroupSet"
    IPV6_ADDRESSES = "Ipv6Addresses"
    SUBNET_ID = "SubnetId"
    ASSOCIATE_PUBLIC_IP_ADDRESS = "AssociatePublicIpAddress"
    NETWORK_INTERFACE_ID = "NetworkInterfaceId"
    ASSOCIATE_CARRIER_IP_ADDRESS = "AssociateCarrierIpAddress"
    ENA_SRD_SPECIFICATION = "EnaSrdSpecification"
    IPV6_ADDRESS_COUNT = "Ipv6AddressCount"
    DELETE_ON_TERMINATION = "DeleteOnTermination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "private_ip_address": "PrivateIpAddress",
        "private_ip_addresses": "PrivateIpAddresses",
        "secondary_private_ip_address_count": "SecondaryPrivateIpAddressCount",
        "device_index": "DeviceIndex",
        "group_set": "GroupSet",
        "ipv6_addresses": "Ipv6Addresses",
        "subnet_id": "SubnetId",
        "associate_public_ip_address": "AssociatePublicIpAddress",
        "network_interface_id": "NetworkInterfaceId",
        "associate_carrier_ip_address": "AssociateCarrierIpAddress",
        "ena_srd_specification": "EnaSrdSpecification",
        "ipv6_address_count": "Ipv6AddressCount",
        "delete_on_termination": "DeleteOnTermination",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_ip_addresses: Optional[list[PrivateIpAddressSpecification]] = None
    secondary_private_ip_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    device_index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_set: Optional[Union[list[str], Ref]] = None
    ipv6_addresses: Optional[list[InstanceIpv6Address]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    associate_public_ip_address: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    associate_carrier_ip_address: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ena_srd_specification: Optional[EnaSrdSpecification] = None
    ipv6_address_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateDnsNameOptions(PropertyType):
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
class PrivateIpAddressSpecification(PropertyType):
    PRIVATE_IP_ADDRESS = "PrivateIpAddress"
    PRIMARY = "Primary"

    _property_mappings: ClassVar[dict[str, str]] = {
        "private_ip_address": "PrivateIpAddress",
        "primary": "Primary",
    }

    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SsmAssociation(PropertyType):
    ASSOCIATION_PARAMETERS = "AssociationParameters"
    DOCUMENT_NAME = "DocumentName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "association_parameters": "AssociationParameters",
        "document_name": "DocumentName",
    }

    association_parameters: Optional[list[AssociationParameter]] = None
    document_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class State(PropertyType):
    CODE = "Code"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "code": "Code",
        "name": "Name",
    }

    code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Volume(PropertyType):
    VOLUME_ID = "VolumeId"
    DEVICE = "Device"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_id": "VolumeId",
        "device": "Device",
    }

    volume_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device: Optional[Union[str, Ref, GetAtt, Sub]] = None

