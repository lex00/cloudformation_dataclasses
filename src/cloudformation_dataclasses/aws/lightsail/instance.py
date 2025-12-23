"""PropertyTypes for AWS::Lightsail::Instance."""

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
class Disk(PropertyType):
    SIZE_IN_GB = "SizeInGb"
    PATH = "Path"
    ATTACHMENT_STATE = "AttachmentState"
    IS_SYSTEM_DISK = "IsSystemDisk"
    ATTACHED_TO = "AttachedTo"
    IOPS = "IOPS"
    DISK_NAME = "DiskName"

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
    CPU_COUNT = "CpuCount"
    RAM_SIZE_IN_GB = "RamSizeInGb"
    DISKS = "Disks"

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
    REGION_NAME = "RegionName"
    AVAILABILITY_ZONE = "AvailabilityZone"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
        "availability_zone": "AvailabilityZone",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonthlyTransfer(PropertyType):
    GB_PER_MONTH_ALLOCATED = "GbPerMonthAllocated"

    _property_mappings: ClassVar[dict[str, str]] = {
        "gb_per_month_allocated": "GbPerMonthAllocated",
    }

    gb_per_month_allocated: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Networking(PropertyType):
    PORTS = "Ports"
    MONTHLY_TRANSFER = "MonthlyTransfer"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ports": "Ports",
        "monthly_transfer": "MonthlyTransfer",
    }

    ports: Optional[list[Port]] = None
    monthly_transfer: Optional[MonthlyTransfer] = None


@dataclass
class Port(PropertyType):
    FROM_PORT = "FromPort"
    ACCESS_DIRECTION = "AccessDirection"
    CIDR_LIST_ALIASES = "CidrListAliases"
    TO_PORT = "ToPort"
    IPV6_CIDRS = "Ipv6Cidrs"
    ACCESS_FROM = "AccessFrom"
    PROTOCOL = "Protocol"
    ACCESS_TYPE = "AccessType"
    CIDRS = "Cidrs"
    COMMON_NAME = "CommonName"

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
    CODE = "Code"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "code": "Code",
        "name": "Name",
    }

    code: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

