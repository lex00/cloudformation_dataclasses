"""PropertyTypes for AWS::AppMesh::Mesh."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EgressFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MeshServiceDiscovery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_preference": "IpPreference",
    }

    ip_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MeshSpec(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "egress_filter": "EgressFilter",
        "service_discovery": "ServiceDiscovery",
    }

    egress_filter: Optional[EgressFilter] = None
    service_discovery: Optional[MeshServiceDiscovery] = None

