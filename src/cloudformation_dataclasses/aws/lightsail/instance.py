"""PropertyTypes for AWS::Lightsail::Instance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AddOn(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_time_of_day": "SnapshotTimeOfDay",
    }

    snapshot_time_of_day: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Disk(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGb",
        "path": "Path",
        "attachment_state": "AttachmentState",
        "is_system_disk": "IsSystemDisk",
        "attached_to": "AttachedTo",
        "iops": "IOPS",
        "disk_name": "DiskName",
    }

    size_in_gb: Optional[Union[str, Ref, GetAtt, Sub]] = None
    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attachment_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_system_disk: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    attached_to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    disk_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Hardware(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_count": "CpuCount",
        "ram_size_in_gb": "RamSizeInGb",
        "disks": "Disks",
    }

    cpu_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ram_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    disks: Optional[list[Disk]] = None


@dataclass
class Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
        "availability_zone": "AvailabilityZone",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonthlyTransfer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gb_per_month_allocated": "GbPerMonthAllocated",
    }

    gb_per_month_allocated: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Networking(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ports": "Ports",
        "monthly_transfer": "MonthlyTransfer",
    }

    ports: Optional[list[Port]] = None
    monthly_transfer: Optional[MonthlyTransfer] = None


@dataclass
class Port(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "access_direction": "AccessDirection",
        "cidr_list_aliases": "CidrListAliases",
        "to_port": "ToPort",
        "ipv6_cidrs": "Ipv6Cidrs",
        "access_from": "AccessFrom",
        "protocol": "Protocol",
        "access_type": "AccessType",
        "cidrs": "Cidrs",
        "common_name": "CommonName",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    access_direction: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr_list_aliases: Optional[Union[list[str], Ref]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ipv6_cidrs: Optional[Union[list[str], Ref]] = None
    access_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidrs: Optional[Union[list[str], Ref]] = None
    common_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class State(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code": "Code",
        "name": "Name",
    }

    code: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

