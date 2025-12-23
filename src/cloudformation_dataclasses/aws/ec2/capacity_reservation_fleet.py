"""PropertyTypes for AWS::EC2::CapacityReservationFleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InstanceTypeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "availability_zone_id": "AvailabilityZoneId",
        "availability_zone": "AvailabilityZone",
        "instance_platform": "InstancePlatform",
        "instance_type": "InstanceType",
        "weight": "Weight",
        "ebs_optimized": "EbsOptimized",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    availability_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_platform: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TagSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None

