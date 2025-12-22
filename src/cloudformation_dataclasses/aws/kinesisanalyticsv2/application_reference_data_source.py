"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource."""

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
class CSVMappingParameters(PropertyType):
    RECORD_ROW_DELIMITER = "RecordRowDelimiter"
    RECORD_COLUMN_DELIMITER = "RecordColumnDelimiter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "record_row_delimiter": "RecordRowDelimiter",
        "record_column_delimiter": "RecordColumnDelimiter",
    }

    record_row_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_column_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JSONMappingParameters(PropertyType):
    RECORD_ROW_PATH = "RecordRowPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "record_row_path": "RecordRowPath",
    }

    record_row_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MappingParameters(PropertyType):
    JSON_MAPPING_PARAMETERS = "JSONMappingParameters"
    CSV_MAPPING_PARAMETERS = "CSVMappingParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json_mapping_parameters": "JSONMappingParameters",
        "csv_mapping_parameters": "CSVMappingParameters",
    }

    json_mapping_parameters: Optional[JSONMappingParameters] = None
    csv_mapping_parameters: Optional[CSVMappingParameters] = None


@dataclass
class RecordColumn(PropertyType):
    MAPPING = "Mapping"
    SQL_TYPE = "SqlType"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mapping": "Mapping",
        "sql_type": "SqlType",
        "name": "Name",
    }

    mapping: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecordFormat(PropertyType):
    MAPPING_PARAMETERS = "MappingParameters"
    RECORD_FORMAT_TYPE = "RecordFormatType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mapping_parameters": "MappingParameters",
        "record_format_type": "RecordFormatType",
    }

    mapping_parameters: Optional[MappingParameters] = None
    record_format_type: Optional[Union[str, RecordFormatType, Ref, GetAtt, Sub]] = None


@dataclass
class ReferenceDataSource(PropertyType):
    REFERENCE_SCHEMA = "ReferenceSchema"
    TABLE_NAME = "TableName"
    S3_REFERENCE_DATA_SOURCE = "S3ReferenceDataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "reference_schema": "ReferenceSchema",
        "table_name": "TableName",
        "s3_reference_data_source": "S3ReferenceDataSource",
    }

    reference_schema: Optional[ReferenceSchema] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_reference_data_source: Optional[S3ReferenceDataSource] = None


@dataclass
class ReferenceSchema(PropertyType):
    RECORD_ENCODING = "RecordEncoding"
    RECORD_COLUMNS = "RecordColumns"
    RECORD_FORMAT = "RecordFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "record_encoding": "RecordEncoding",
        "record_columns": "RecordColumns",
        "record_format": "RecordFormat",
    }

    record_encoding: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_columns: Optional[list[RecordColumn]] = None
    record_format: Optional[RecordFormat] = None


@dataclass
class S3ReferenceDataSource(PropertyType):
    BUCKET_ARN = "BucketARN"
    FILE_KEY = "FileKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "file_key": "FileKey",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

