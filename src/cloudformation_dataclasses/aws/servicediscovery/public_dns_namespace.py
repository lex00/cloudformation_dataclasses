"""PropertyTypes for AWS::ServiceDiscovery::PublicDnsNamespace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Properties(PropertyType):
    DNS_PROPERTIES = "DnsProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_properties": "DnsProperties",
    }

    dns_properties: Optional[PublicDnsPropertiesMutable] = None


@dataclass
class PublicDnsPropertiesMutable(PropertyType):
    SOA = "SOA"

    _property_mappings: ClassVar[dict[str, str]] = {
        "soa": "SOA",
    }

    soa: Optional[SOA] = None


@dataclass
class SOA(PropertyType):
    TTL = "TTL"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ttl": "TTL",
    }

    ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None

