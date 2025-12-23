"""PropertyTypes for AWS::EC2::NatGateway."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AvailabilityZoneAddress(PropertyType):
    AVAILABILITY_ZONE_ID = "AvailabilityZoneId"
    AVAILABILITY_ZONE = "AvailabilityZone"
    ALLOCATION_IDS = "AllocationIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_id": "AvailabilityZoneId",
        "availability_zone": "AvailabilityZone",
        "allocation_ids": "AllocationIds",
    }

    availability_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allocation_ids: Optional[Union[list[str], Ref]] = None

