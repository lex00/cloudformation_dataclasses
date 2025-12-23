"""PropertyTypes for AWS::AppMesh::VirtualRouter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PortMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "protocol": "Protocol",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualRouterListener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port_mapping": "PortMapping",
    }

    port_mapping: Optional[PortMapping] = None


@dataclass
class VirtualRouterSpec(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "listeners": "Listeners",
    }

    listeners: Optional[list[VirtualRouterListener]] = None

