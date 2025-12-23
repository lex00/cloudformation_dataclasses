"""PropertyTypes for AWS::VpcLattice::ResourceConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DnsResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "domain_name": "DomainName",
    }

    ip_address_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceConfigurationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_resource": "IpResource",
        "dns_resource": "DnsResource",
        "arn_resource": "ArnResource",
    }

    ip_resource: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_resource: Optional[DnsResource] = None
    arn_resource: Optional[Union[str, Ref, GetAtt, Sub]] = None

