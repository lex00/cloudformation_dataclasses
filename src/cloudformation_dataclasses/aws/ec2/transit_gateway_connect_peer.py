"""PropertyTypes for AWS::EC2::TransitGatewayConnectPeer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TransitGatewayAttachmentBgpConfiguration(PropertyType):
    TRANSIT_GATEWAY_ADDRESS = "TransitGatewayAddress"
    PEER_ADDRESS = "PeerAddress"
    BGP_STATUS = "BgpStatus"
    PEER_ASN = "PeerAsn"
    TRANSIT_GATEWAY_ASN = "TransitGatewayAsn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transit_gateway_address": "TransitGatewayAddress",
        "peer_address": "PeerAddress",
        "bgp_status": "BgpStatus",
        "peer_asn": "PeerAsn",
        "transit_gateway_asn": "TransitGatewayAsn",
    }

    transit_gateway_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    peer_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bgp_status: Optional[Union[str, BgpStatus, Ref, GetAtt, Sub]] = None
    peer_asn: Optional[Union[float, Ref, GetAtt, Sub]] = None
    transit_gateway_asn: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TransitGatewayConnectPeerConfiguration(PropertyType):
    TRANSIT_GATEWAY_ADDRESS = "TransitGatewayAddress"
    BGP_CONFIGURATIONS = "BgpConfigurations"
    PEER_ADDRESS = "PeerAddress"
    INSIDE_CIDR_BLOCKS = "InsideCidrBlocks"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transit_gateway_address": "TransitGatewayAddress",
        "bgp_configurations": "BgpConfigurations",
        "peer_address": "PeerAddress",
        "inside_cidr_blocks": "InsideCidrBlocks",
        "protocol": "Protocol",
    }

    transit_gateway_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bgp_configurations: Optional[list[TransitGatewayAttachmentBgpConfiguration]] = None
    peer_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inside_cidr_blocks: Optional[Union[list[str], Ref]] = None
    protocol: Optional[Union[str, ProtocolValue, Ref, GetAtt, Sub]] = None

