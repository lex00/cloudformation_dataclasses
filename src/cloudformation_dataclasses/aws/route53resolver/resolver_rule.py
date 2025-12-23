"""PropertyTypes for AWS::Route53Resolver::ResolverRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TargetAddress(PropertyType):
    IPV6 = "Ipv6"
    IP = "Ip"
    PORT = "Port"
    PROTOCOL = "Protocol"
    SERVER_NAME_INDICATION = "ServerNameIndication"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6": "Ipv6",
        "ip": "Ip",
        "port": "Port",
        "protocol": "Protocol",
        "server_name_indication": "ServerNameIndication",
    }

    ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None
    server_name_indication: Optional[Union[str, Ref, GetAtt, Sub]] = None

