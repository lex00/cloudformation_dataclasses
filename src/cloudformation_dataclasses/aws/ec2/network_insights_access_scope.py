"""PropertyTypes for AWS::EC2::NetworkInsightsAccessScope."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessScopePathRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "through_resources": "ThroughResources",
        "source": "Source",
    }

    destination: Optional[PathStatementRequest] = None
    through_resources: Optional[list[ThroughResourcesStatementRequest]] = None
    source: Optional[PathStatementRequest] = None


@dataclass
class PacketHeaderStatementRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protocols": "Protocols",
        "destination_ports": "DestinationPorts",
        "destination_addresses": "DestinationAddresses",
        "destination_prefix_lists": "DestinationPrefixLists",
        "source_addresses": "SourceAddresses",
        "source_ports": "SourcePorts",
        "source_prefix_lists": "SourcePrefixLists",
    }

    protocols: Optional[Union[list[str], Ref]] = None
    destination_ports: Optional[Union[list[str], Ref]] = None
    destination_addresses: Optional[Union[list[str], Ref]] = None
    destination_prefix_lists: Optional[Union[list[str], Ref]] = None
    source_addresses: Optional[Union[list[str], Ref]] = None
    source_ports: Optional[Union[list[str], Ref]] = None
    source_prefix_lists: Optional[Union[list[str], Ref]] = None


@dataclass
class PathStatementRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_statement": "ResourceStatement",
        "packet_header_statement": "PacketHeaderStatement",
    }

    resource_statement: Optional[ResourceStatementRequest] = None
    packet_header_statement: Optional[PacketHeaderStatementRequest] = None


@dataclass
class ResourceStatementRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_types": "ResourceTypes",
        "resources": "Resources",
    }

    resource_types: Optional[Union[list[str], Ref]] = None
    resources: Optional[Union[list[str], Ref]] = None


@dataclass
class ThroughResourcesStatementRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_statement": "ResourceStatement",
    }

    resource_statement: Optional[ResourceStatementRequest] = None

