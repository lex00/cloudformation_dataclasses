"""PropertyTypes for AWS::EC2::NetworkInterfaceAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EnaSrdSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ena_srd_enabled": "EnaSrdEnabled",
        "ena_srd_udp_specification": "EnaSrdUdpSpecification",
    }

    ena_srd_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ena_srd_udp_specification: Optional[EnaSrdUdpSpecification] = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ena_srd_udp_enabled": "EnaSrdUdpEnabled",
    }

    ena_srd_udp_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

