"""PropertyTypes for AWS::EFS::FileSystem."""

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
class BackupPolicy(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, Status, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticFileSystemTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FileSystemProtection(PropertyType):
    REPLICATION_OVERWRITE_PROTECTION = "ReplicationOverwriteProtection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replication_overwrite_protection": "ReplicationOverwriteProtection",
    }

    replication_overwrite_protection: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LifecyclePolicy(PropertyType):
    TRANSITION_TO_IA = "TransitionToIA"
    TRANSITION_TO_PRIMARY_STORAGE_CLASS = "TransitionToPrimaryStorageClass"
    TRANSITION_TO_ARCHIVE = "TransitionToArchive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_to_ia": "TransitionToIA",
        "transition_to_primary_storage_class": "TransitionToPrimaryStorageClass",
        "transition_to_archive": "TransitionToArchive",
    }

    transition_to_ia: Optional[Union[str, TransitionToIARules, Ref, GetAtt, Sub]] = None
    transition_to_primary_storage_class: Optional[Union[str, TransitionToPrimaryStorageClassRules, Ref, GetAtt, Sub]] = None
    transition_to_archive: Optional[Union[str, TransitionToArchiveRules, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationConfiguration(PropertyType):
    DESTINATIONS = "Destinations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destinations": "Destinations",
    }

    destinations: Optional[list[ReplicationDestination]] = None


@dataclass
class ReplicationDestination(PropertyType):
    STATUS = "Status"
    KMS_KEY_ID = "KmsKeyId"
    AVAILABILITY_ZONE_NAME = "AvailabilityZoneName"
    FILE_SYSTEM_ID = "FileSystemId"
    REGION = "Region"
    ROLE_ARN = "RoleArn"
    STATUS_MESSAGE = "StatusMessage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "kms_key_id": "KmsKeyId",
        "availability_zone_name": "AvailabilityZoneName",
        "file_system_id": "FileSystemId",
        "region": "Region",
        "role_arn": "RoleArn",
        "status_message": "StatusMessage",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_message: Optional[Union[str, Ref, GetAtt, Sub]] = None

