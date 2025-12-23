"""PropertyTypes for AWS::MediaConnect::BridgeOutput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BridgeNetworkOutput(PropertyType):
    NETWORK_NAME = "NetworkName"
    PORT = "Port"
    IP_ADDRESS = "IpAddress"
    PROTOCOL = "Protocol"
    TTL = "Ttl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_name": "NetworkName",
        "port": "Port",
        "ip_address": "IpAddress",
        "protocol": "Protocol",
        "ttl": "Ttl",
    }

    network_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None
    ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None

