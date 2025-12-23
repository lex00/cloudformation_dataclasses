"""PropertyTypes for AWS::Route53Resolver::ResolverEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IpAddressRequest(PropertyType):
    IPV6 = "Ipv6"
    IP = "Ip"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6": "Ipv6",
        "ip": "Ip",
        "subnet_id": "SubnetId",
    }

    ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

