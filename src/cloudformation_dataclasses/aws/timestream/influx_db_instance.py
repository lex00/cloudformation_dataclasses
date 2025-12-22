"""PropertyTypes for AWS::Timestream::InfluxDBInstance."""

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
class LogDeliveryConfiguration(PropertyType):
    S3_CONFIGURATION = "S3Configuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_configuration": "S3Configuration",
    }

    s3_configuration: Optional[S3Configuration] = None


@dataclass
class S3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "enabled": "Enabled",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

