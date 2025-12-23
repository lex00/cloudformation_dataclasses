"""PropertyTypes for AWS::Lightsail::Disk."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AddOn(PropertyType):
    STATUS = "Status"
    ADD_ON_TYPE = "AddOnType"
    AUTO_SNAPSHOT_ADD_ON_REQUEST = "AutoSnapshotAddOnRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "add_on_type": "AddOnType",
        "auto_snapshot_add_on_request": "AutoSnapshotAddOnRequest",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    add_on_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_snapshot_add_on_request: Optional[AutoSnapshotAddOn] = None


@dataclass
class AutoSnapshotAddOn(PropertyType):
    SNAPSHOT_TIME_OF_DAY = "SnapshotTimeOfDay"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_time_of_day": "SnapshotTimeOfDay",
    }

    snapshot_time_of_day: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Location(PropertyType):
    REGION_NAME = "RegionName"
    AVAILABILITY_ZONE = "AvailabilityZone"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
        "availability_zone": "AvailabilityZone",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None

