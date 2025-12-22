"""PropertyTypes for AWS::S3Tables::TableBucket."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class IcebergCompactionStrategy:
    """IcebergCompactionStrategy enum values."""

    AUTO = "auto"
    BINPACK = "binpack"
    SORT = "sort"
    Z_ORDER = "z-order"


class JobStatus:
    """JobStatus enum values."""

    NOT_YET_RUN = "Not_Yet_Run"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    DISABLED = "Disabled"


class MaintenanceStatus:
    """MaintenanceStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class OpenTableFormat:
    """OpenTableFormat enum values."""

    ICEBERG = "ICEBERG"


class ReplicationStatus:
    """ReplicationStatus enum values."""

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class SSEAlgorithm:
    """SSEAlgorithm enum values."""

    AES256 = "AES256"
    AWS_KMS = "aws:kms"


class StorageClass:
    """StorageClass enum values."""

    STANDARD = "STANDARD"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"


class TableBucketMaintenanceType:
    """TableBucketMaintenanceType enum values."""

    ICEBERGUNREFERENCEDFILEREMOVAL = "icebergUnreferencedFileRemoval"


class TableBucketType:
    """TableBucketType enum values."""

    CUSTOMER = "customer"
    AWS = "aws"


class TableMaintenanceJobType:
    """TableMaintenanceJobType enum values."""

    ICEBERGCOMPACTION = "icebergCompaction"
    ICEBERGSNAPSHOTMANAGEMENT = "icebergSnapshotManagement"
    ICEBERGUNREFERENCEDFILEREMOVAL = "icebergUnreferencedFileRemoval"


class TableMaintenanceType:
    """TableMaintenanceType enum values."""

    ICEBERGCOMPACTION = "icebergCompaction"
    ICEBERGSNAPSHOTMANAGEMENT = "icebergSnapshotManagement"


class TableRecordExpirationJobStatus:
    """TableRecordExpirationJobStatus enum values."""

    NOTYETRUN = "NotYetRun"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    DISABLED = "Disabled"


class TableRecordExpirationStatus:
    """TableRecordExpirationStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class TableType:
    """TableType enum values."""

    CUSTOMER = "customer"
    AWS = "aws"


@dataclass
class EncryptionConfiguration(PropertyType):
    KMS_KEY_ARN = "KMSKeyArn"
    SSE_ALGORITHM = "SSEAlgorithm"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
        "sse_algorithm": "SSEAlgorithm",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsConfiguration(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageClassConfiguration(PropertyType):
    STORAGE_CLASS = "StorageClass"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
    }

    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UnreferencedFileRemoval(PropertyType):
    STATUS = "Status"
    NONCURRENT_DAYS = "NoncurrentDays"
    UNREFERENCED_DAYS = "UnreferencedDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "noncurrent_days": "NoncurrentDays",
        "unreferenced_days": "UnreferencedDays",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    noncurrent_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unreferenced_days: Optional[Union[int, Ref, GetAtt, Sub]] = None

