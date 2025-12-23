"""PropertyTypes for AWS::NetworkManager::CoreNetwork."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CoreNetworkEdge(PropertyType):
    INSIDE_CIDR_BLOCKS = "InsideCidrBlocks"
    ASN = "Asn"
    EDGE_LOCATION = "EdgeLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inside_cidr_blocks": "InsideCidrBlocks",
        "asn": "Asn",
        "edge_location": "EdgeLocation",
    }

    inside_cidr_blocks: Optional[Union[list[str], Ref]] = None
    asn: Optional[Union[float, Ref, GetAtt, Sub]] = None
    edge_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CoreNetworkNetworkFunctionGroup(PropertyType):
    EDGE_LOCATIONS = "EdgeLocations"
    SEGMENTS = "Segments"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "edge_locations": "EdgeLocations",
        "segments": "Segments",
        "name": "Name",
    }

    edge_locations: Optional[Union[list[str], Ref]] = None
    segments: Optional[Segments] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CoreNetworkSegment(PropertyType):
    EDGE_LOCATIONS = "EdgeLocations"
    SHARED_SEGMENTS = "SharedSegments"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "edge_locations": "EdgeLocations",
        "shared_segments": "SharedSegments",
        "name": "Name",
    }

    edge_locations: Optional[Union[list[str], Ref]] = None
    shared_segments: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Segments(PropertyType):
    SEND_TO = "SendTo"
    SEND_VIA = "SendVia"

    _property_mappings: ClassVar[dict[str, str]] = {
        "send_to": "SendTo",
        "send_via": "SendVia",
    }

    send_to: Optional[Union[list[str], Ref]] = None
    send_via: Optional[Union[list[str], Ref]] = None

