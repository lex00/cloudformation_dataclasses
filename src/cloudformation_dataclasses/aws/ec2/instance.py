"""PropertyTypes for AWS::EC2::Instance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssociationParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BlockDeviceMapping(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "threads_per_core": "ThreadsPerCore",
        "core_count": "CoreCount",
    }

    threads_per_core: Optional[Union[int, Ref, GetAtt, Sub]] = None
    core_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CreditSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_credits": "CPUCredits",
    }

    cpu_credits: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ebs(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticInferenceAccelerator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "count": "Count",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
class InstanceIpv6Address(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_address": "Ipv6Address",
    }

    ipv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class LicenseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "license_configuration_arn": "LicenseConfigurationArn",
    }

    license_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataOptions(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_ip_address": "PrivateIpAddress",
        "primary": "Primary",
    }

    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SsmAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "association_parameters": "AssociationParameters",
        "document_name": "DocumentName",
    }

    association_parameters: Optional[list[AssociationParameter]] = None
    document_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class State(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code": "Code",
        "name": "Name",
    }

    code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Volume(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_id": "VolumeId",
        "device": "Device",
    }

    volume_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device: Optional[Union[str, Ref, GetAtt, Sub]] = None

