"""PropertyTypes for AWS::EC2::VPCEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DnsOptionsSpecification(PropertyType):
    PRIVATE_DNS_ONLY_FOR_INBOUND_RESOLVER_ENDPOINT = "PrivateDnsOnlyForInboundResolverEndpoint"
    PRIVATE_DNS_SPECIFIED_DOMAINS = "PrivateDnsSpecifiedDomains"
    DNS_RECORD_IP_TYPE = "DnsRecordIpType"
    PRIVATE_DNS_PREFERENCE = "PrivateDnsPreference"

    _property_mappings: ClassVar[dict[str, str]] = {
        "private_dns_only_for_inbound_resolver_endpoint": "PrivateDnsOnlyForInboundResolverEndpoint",
        "private_dns_specified_domains": "PrivateDnsSpecifiedDomains",
        "dns_record_ip_type": "DnsRecordIpType",
        "private_dns_preference": "PrivateDnsPreference",
    }

    private_dns_only_for_inbound_resolver_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_dns_specified_domains: Optional[Union[list[str], Ref]] = None
    dns_record_ip_type: Optional[Union[str, DnsRecordIpType, Ref, GetAtt, Sub]] = None
    private_dns_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None

