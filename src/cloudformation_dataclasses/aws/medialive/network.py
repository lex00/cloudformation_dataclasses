"""PropertyTypes for AWS::MediaLive::Network."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IpPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Route(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
        "gateway": "Gateway",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    gateway: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

