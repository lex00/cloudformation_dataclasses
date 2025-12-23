"""PropertyTypes for AWS::NetworkManager::ConnectPeer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BgpOptions(PropertyType):
    PEER_ASN = "PeerAsn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "peer_asn": "PeerAsn",
    }

    peer_asn: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectPeerBgpConfiguration(PropertyType):
    PEER_ADDRESS = "PeerAddress"
    CORE_NETWORK_ADDRESS = "CoreNetworkAddress"
    PEER_ASN = "PeerAsn"
    CORE_NETWORK_ASN = "CoreNetworkAsn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "peer_address": "PeerAddress",
        "core_network_address": "CoreNetworkAddress",
        "peer_asn": "PeerAsn",
        "core_network_asn": "CoreNetworkAsn",
    }

    peer_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    core_network_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    peer_asn: Optional[Union[float, Ref, GetAtt, Sub]] = None
    core_network_asn: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectPeerConfiguration(PropertyType):
    BGP_CONFIGURATIONS = "BgpConfigurations"
    PEER_ADDRESS = "PeerAddress"
    CORE_NETWORK_ADDRESS = "CoreNetworkAddress"
    INSIDE_CIDR_BLOCKS = "InsideCidrBlocks"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bgp_configurations": "BgpConfigurations",
        "peer_address": "PeerAddress",
        "core_network_address": "CoreNetworkAddress",
        "inside_cidr_blocks": "InsideCidrBlocks",
        "protocol": "Protocol",
    }

    bgp_configurations: Optional[list[ConnectPeerBgpConfiguration]] = None
    peer_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    core_network_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inside_cidr_blocks: Optional[Union[list[str], Ref]] = None
    protocol: Optional[Union[str, TunnelProtocol, Ref, GetAtt, Sub]] = None

