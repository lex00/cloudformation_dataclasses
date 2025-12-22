"""PropertyTypes for AWS::EFS::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class DeletionMode:
    """DeletionMode enum values."""

    ALL_CONFIGURATIONS = "ALL_CONFIGURATIONS"
    LOCAL_CONFIGURATION_ONLY = "LOCAL_CONFIGURATION_ONLY"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4_ONLY = "IPV4_ONLY"
    IPV6_ONLY = "IPV6_ONLY"
    DUAL_STACK = "DUAL_STACK"


class LifeCycleState:
    """LifeCycleState enum values."""

    CREATING = "creating"
    AVAILABLE = "available"
    UPDATING = "updating"
    DELETING = "deleting"
    DELETED = "deleted"
    ERROR = "error"


class PerformanceMode:
    """PerformanceMode enum values."""

    GENERALPURPOSE = "generalPurpose"
    MAXIO = "maxIO"


class ReplicationOverwriteProtection:
    """ReplicationOverwriteProtection enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    REPLICATING = "REPLICATING"


class ReplicationStatus:
    """ReplicationStatus enum values."""

    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DELETING = "DELETING"
    ERROR = "ERROR"
    PAUSED = "PAUSED"
    PAUSING = "PAUSING"


class Resource:
    """Resource enum values."""

    FILE_SYSTEM = "FILE_SYSTEM"
    MOUNT_TARGET = "MOUNT_TARGET"


class ResourceIdType:
    """ResourceIdType enum values."""

    LONG_ID = "LONG_ID"
    SHORT_ID = "SHORT_ID"


class Status:
    """Status enum values."""

    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DISABLED = "DISABLED"
    DISABLING = "DISABLING"


class ThroughputMode:
    """ThroughputMode enum values."""

    BURSTING = "bursting"
    PROVISIONED = "provisioned"
    ELASTIC = "elastic"


class TransitionToArchiveRules:
    """TransitionToArchiveRules enum values."""

    AFTER_1_DAY = "AFTER_1_DAY"
    AFTER_7_DAYS = "AFTER_7_DAYS"
    AFTER_14_DAYS = "AFTER_14_DAYS"
    AFTER_30_DAYS = "AFTER_30_DAYS"
    AFTER_60_DAYS = "AFTER_60_DAYS"
    AFTER_90_DAYS = "AFTER_90_DAYS"
    AFTER_180_DAYS = "AFTER_180_DAYS"
    AFTER_270_DAYS = "AFTER_270_DAYS"
    AFTER_365_DAYS = "AFTER_365_DAYS"


class TransitionToIARules:
    """TransitionToIARules enum values."""

    AFTER_7_DAYS = "AFTER_7_DAYS"
    AFTER_14_DAYS = "AFTER_14_DAYS"
    AFTER_30_DAYS = "AFTER_30_DAYS"
    AFTER_60_DAYS = "AFTER_60_DAYS"
    AFTER_90_DAYS = "AFTER_90_DAYS"
    AFTER_1_DAY = "AFTER_1_DAY"
    AFTER_180_DAYS = "AFTER_180_DAYS"
    AFTER_270_DAYS = "AFTER_270_DAYS"
    AFTER_365_DAYS = "AFTER_365_DAYS"


class TransitionToPrimaryStorageClassRules:
    """TransitionToPrimaryStorageClassRules enum values."""

    AFTER_1_ACCESS = "AFTER_1_ACCESS"


@dataclass
class AccessPointTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CreationInfo(PropertyType):
    OWNER_GID = "OwnerGid"
    OWNER_UID = "OwnerUid"
    PERMISSIONS = "Permissions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner_gid": "OwnerGid",
        "owner_uid": "OwnerUid",
        "permissions": "Permissions",
    }

    owner_gid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    owner_uid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    permissions: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PosixUser(PropertyType):
    UID = "Uid"
    SECONDARY_GIDS = "SecondaryGids"
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "secondary_gids": "SecondaryGids",
        "gid": "Gid",
    }

    uid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_gids: Optional[Union[list[str], Ref]] = None
    gid: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RootDirectory(PropertyType):
    PATH = "Path"
    CREATION_INFO = "CreationInfo"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "creation_info": "CreationInfo",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_info: Optional[CreationInfo] = None

