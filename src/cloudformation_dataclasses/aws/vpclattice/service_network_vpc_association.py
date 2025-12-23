"""PropertyTypes for AWS::VpcLattice::ServiceNetworkVpcAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DnsOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_dns_specified_domains": "PrivateDnsSpecifiedDomains",
        "private_dns_preference": "PrivateDnsPreference",
    }

    private_dns_specified_domains: Optional[Union[list[str], Ref]] = None
    private_dns_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None

