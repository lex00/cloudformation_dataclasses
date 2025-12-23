"""PropertyTypes for AWS::MediaLive::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ClusterNetworkSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interface_mappings": "InterfaceMappings",
        "default_route": "DefaultRoute",
    }

    interface_mappings: Optional[list[InterfaceMapping]] = None
    default_route: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InterfaceMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "network_id": "NetworkId",
        "logical_interface_name": "LogicalInterfaceName",
    }

    network_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logical_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

