"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationMode:
    """ApplicationMode enum values."""

    STREAMING = "STREAMING"
    INTERACTIVE = "INTERACTIVE"


class ApplicationRestoreType:
    """ApplicationRestoreType enum values."""

    SKIP_RESTORE_FROM_SNAPSHOT = "SKIP_RESTORE_FROM_SNAPSHOT"
    RESTORE_FROM_LATEST_SNAPSHOT = "RESTORE_FROM_LATEST_SNAPSHOT"
    RESTORE_FROM_CUSTOM_SNAPSHOT = "RESTORE_FROM_CUSTOM_SNAPSHOT"


class ApplicationStatus:
    """ApplicationStatus enum values."""

    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    READY = "READY"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"
    AUTOSCALING = "AUTOSCALING"
    FORCE_STOPPING = "FORCE_STOPPING"
    ROLLING_BACK = "ROLLING_BACK"
    MAINTENANCE = "MAINTENANCE"
    ROLLED_BACK = "ROLLED_BACK"


class ArtifactType:
    """ArtifactType enum values."""

    UDF = "UDF"
    DEPENDENCY_JAR = "DEPENDENCY_JAR"


class CodeContentType:
    """CodeContentType enum values."""

    PLAINTEXT = "PLAINTEXT"
    ZIPFILE = "ZIPFILE"


class ConfigurationType:
    """ConfigurationType enum values."""

    DEFAULT = "DEFAULT"
    CUSTOM = "CUSTOM"


class InputStartingPosition:
    """InputStartingPosition enum values."""

    NOW = "NOW"
    TRIM_HORIZON = "TRIM_HORIZON"
    LAST_STOPPED_POINT = "LAST_STOPPED_POINT"


class KeyType:
    """KeyType enum values."""

    AWS_OWNED_KEY = "AWS_OWNED_KEY"
    CUSTOMER_MANAGED_KEY = "CUSTOMER_MANAGED_KEY"


class LogLevel:
    """LogLevel enum values."""

    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"


class MetricsLevel:
    """MetricsLevel enum values."""

    APPLICATION = "APPLICATION"
    TASK = "TASK"
    OPERATOR = "OPERATOR"
    PARALLELISM = "PARALLELISM"


class OperationStatus:
    """OperationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"


class RecordFormatType:
    """RecordFormatType enum values."""

    JSON = "JSON"
    CSV = "CSV"


class RuntimeEnvironment:
    """RuntimeEnvironment enum values."""

    SQL_1_0 = "SQL-1_0"
    FLINK_1_6 = "FLINK-1_6"
    FLINK_1_8 = "FLINK-1_8"
    ZEPPELIN_FLINK_1_0 = "ZEPPELIN-FLINK-1_0"
    FLINK_1_11 = "FLINK-1_11"
    FLINK_1_13 = "FLINK-1_13"
    ZEPPELIN_FLINK_2_0 = "ZEPPELIN-FLINK-2_0"
    FLINK_1_15 = "FLINK-1_15"
    ZEPPELIN_FLINK_3_0 = "ZEPPELIN-FLINK-3_0"
    FLINK_1_18 = "FLINK-1_18"
    FLINK_1_19 = "FLINK-1_19"
    FLINK_1_20 = "FLINK-1_20"


class SnapshotStatus:
    """SnapshotStatus enum values."""

    CREATING = "CREATING"
    READY = "READY"
    DELETING = "DELETING"
    FAILED = "FAILED"


class UrlType:
    """UrlType enum values."""

    FLINK_DASHBOARD_URL = "FLINK_DASHBOARD_URL"
    ZEPPELIN_UI_URL = "ZEPPELIN_UI_URL"


@dataclass
class CloudWatchLoggingOption(PropertyType):
    LOG_STREAM_ARN = "LogStreamARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_arn": "LogStreamARN",
    }

    log_stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

