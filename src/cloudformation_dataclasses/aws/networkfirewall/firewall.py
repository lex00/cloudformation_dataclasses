"""PropertyTypes for AWS::NetworkFirewall::Firewall."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AvailabilityZoneMapping(PropertyType):
    AVAILABILITY_ZONE = "AvailabilityZone"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone": "AvailabilityZone",
    }

    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubnetMapping(PropertyType):
    IP_ADDRESS_TYPE = "IPAddressType"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IPAddressType",
        "subnet_id": "SubnetId",
    }

    ip_address_type: Optional[Union[str, IPAddressType, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

