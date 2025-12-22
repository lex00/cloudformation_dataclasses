"""PropertyTypes for AWS::Timestream::Table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BatchLoadDataFormat:
    """BatchLoadDataFormat enum values."""

    CSV = "CSV"


class BatchLoadStatus:
    """BatchLoadStatus enum values."""

    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    PROGRESS_STOPPED = "PROGRESS_STOPPED"
    PENDING_RESUME = "PENDING_RESUME"


class DimensionValueType:
    """DimensionValueType enum values."""

    VARCHAR = "VARCHAR"


class MeasureValueType:
    """MeasureValueType enum values."""

    DOUBLE = "DOUBLE"
    BIGINT = "BIGINT"
    VARCHAR = "VARCHAR"
    BOOLEAN = "BOOLEAN"
    TIMESTAMP = "TIMESTAMP"
    MULTI = "MULTI"


class PartitionKeyEnforcementLevel:
    """PartitionKeyEnforcementLevel enum values."""

    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"


class PartitionKeyType:
    """PartitionKeyType enum values."""

    DIMENSION = "DIMENSION"
    MEASURE = "MEASURE"


class S3EncryptionOption:
    """S3EncryptionOption enum values."""

    SSE_S3 = "SSE_S3"
    SSE_KMS = "SSE_KMS"


class ScalarMeasureValueType:
    """ScalarMeasureValueType enum values."""

    DOUBLE = "DOUBLE"
    BIGINT = "BIGINT"
    BOOLEAN = "BOOLEAN"
    VARCHAR = "VARCHAR"
    TIMESTAMP = "TIMESTAMP"


class TableStatus:
    """TableStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    RESTORING = "RESTORING"


class TimeUnit:
    """TimeUnit enum values."""

    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MICROSECONDS = "MICROSECONDS"
    NANOSECONDS = "NANOSECONDS"


@dataclass
class MagneticStoreRejectedDataLocation(PropertyType):
    S3_CONFIGURATION = "S3Configuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_configuration": "S3Configuration",
    }

    s3_configuration: Optional[S3Configuration] = None


@dataclass
class MagneticStoreWriteProperties(PropertyType):
    ENABLE_MAGNETIC_STORE_WRITES = "EnableMagneticStoreWrites"
    MAGNETIC_STORE_REJECTED_DATA_LOCATION = "MagneticStoreRejectedDataLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_magnetic_store_writes": "EnableMagneticStoreWrites",
        "magnetic_store_rejected_data_location": "MagneticStoreRejectedDataLocation",
    }

    enable_magnetic_store_writes: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    magnetic_store_rejected_data_location: Optional[MagneticStoreRejectedDataLocation] = None


@dataclass
class PartitionKey(PropertyType):
    TYPE = "Type"
    ENFORCEMENT_IN_RECORD = "EnforcementInRecord"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "enforcement_in_record": "EnforcementInRecord",
        "name": "Name",
    }

    type_: Optional[Union[str, PartitionKeyType, Ref, GetAtt, Sub]] = None
    enforcement_in_record: Optional[Union[str, PartitionKeyEnforcementLevel, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionProperties(PropertyType):
    MAGNETIC_STORE_RETENTION_PERIOD_IN_DAYS = "MagneticStoreRetentionPeriodInDays"
    MEMORY_STORE_RETENTION_PERIOD_IN_HOURS = "MemoryStoreRetentionPeriodInHours"

    _property_mappings: ClassVar[dict[str, str]] = {
        "magnetic_store_retention_period_in_days": "MagneticStoreRetentionPeriodInDays",
        "memory_store_retention_period_in_hours": "MemoryStoreRetentionPeriodInHours",
    }

    magnetic_store_retention_period_in_days: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_store_retention_period_in_hours: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"
    KMS_KEY_ID = "KmsKeyId"
    OBJECT_KEY_PREFIX = "ObjectKeyPrefix"
    ENCRYPTION_OPTION = "EncryptionOption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "kms_key_id": "KmsKeyId",
        "object_key_prefix": "ObjectKeyPrefix",
        "encryption_option": "EncryptionOption",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_option: Optional[Union[str, S3EncryptionOption, Ref, GetAtt, Sub]] = None


@dataclass
class Schema(PropertyType):
    COMPOSITE_PARTITION_KEY = "CompositePartitionKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "composite_partition_key": "CompositePartitionKey",
    }

    composite_partition_key: Optional[list[PartitionKey]] = None

