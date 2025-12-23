"""PropertyTypes for AWS::EC2::NetworkInterface."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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
class InstanceIpv6Address(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_address": "Ipv6Address",
    }

    ipv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ipv4PrefixSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv4_prefix": "Ipv4Prefix",
    }

    ipv4_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ipv6PrefixSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_prefix": "Ipv6Prefix",
    }

    ipv6_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_ip_address": "PrivateIpAddress",
        "primary": "Primary",
    }

    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PublicIpDnsNameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_hostname_type": "DnsHostnameType",
        "public_ipv4_dns_name": "PublicIpv4DnsName",
        "public_dual_stack_dns_name": "PublicDualStackDnsName",
        "public_ipv6_dns_name": "PublicIpv6DnsName",
    }

    dns_hostname_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    public_ipv4_dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    public_dual_stack_dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    public_ipv6_dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

