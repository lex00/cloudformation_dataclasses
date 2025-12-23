"""PropertyTypes for AWS::OpsWorks::Instance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BlockDeviceMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "device_name": "DeviceName",
        "ebs": "Ebs",
        "no_device": "NoDevice",
        "virtual_name": "VirtualName",
    }

    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs: Optional[EbsBlockDevice] = None
    no_device: Optional[Union[str, Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EbsBlockDevice(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delete_on_termination": "DeleteOnTermination",
        "iops": "Iops",
        "snapshot_id": "SnapshotId",
        "volume_size": "VolumeSize",
        "volume_type": "VolumeType",
    }

    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedAutoScaling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "friday": "Friday",
        "monday": "Monday",
        "saturday": "Saturday",
        "sunday": "Sunday",
        "thursday": "Thursday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
    }

    friday: Optional[dict[str, str]] = None
    monday: Optional[dict[str, str]] = None
    saturday: Optional[dict[str, str]] = None
    sunday: Optional[dict[str, str]] = None
    thursday: Optional[dict[str, str]] = None
    tuesday: Optional[dict[str, str]] = None
    wednesday: Optional[dict[str, str]] = None

