"""PropertyTypes for AWS::S3Tables::Table."""

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
class Compaction(PropertyType):
    STATUS = "Status"
    TARGET_FILE_SIZE_MB = "TargetFileSizeMB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "target_file_size_mb": "TargetFileSizeMB",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_file_size_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IcebergMetadata(PropertyType):
    ICEBERG_SCHEMA = "IcebergSchema"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iceberg_schema": "IcebergSchema",
    }

    iceberg_schema: Optional[IcebergSchema] = None


@dataclass
class IcebergSchema(PropertyType):
    SCHEMA_FIELD_LIST = "SchemaFieldList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_field_list": "SchemaFieldList",
    }

    schema_field_list: Optional[list[SchemaField]] = None


@dataclass
class SchemaField(PropertyType):
    TYPE = "Type"
    REQUIRED = "Required"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "required": "Required",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnapshotManagement(PropertyType):
    STATUS = "Status"
    MIN_SNAPSHOTS_TO_KEEP = "MinSnapshotsToKeep"
    MAX_SNAPSHOT_AGE_HOURS = "MaxSnapshotAgeHours"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "min_snapshots_to_keep": "MinSnapshotsToKeep",
        "max_snapshot_age_hours": "MaxSnapshotAgeHours",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_snapshots_to_keep: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_snapshot_age_hours: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StorageClassConfiguration(PropertyType):
    STORAGE_CLASS = "StorageClass"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
    }

    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None

