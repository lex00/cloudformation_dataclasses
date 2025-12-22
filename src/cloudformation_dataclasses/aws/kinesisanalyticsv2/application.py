"""PropertyTypes for AWS::KinesisAnalyticsV2::Application."""

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
class ApplicationCodeConfiguration(PropertyType):
    CODE_CONTENT_TYPE = "CodeContentType"
    CODE_CONTENT = "CodeContent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "code_content_type": "CodeContentType",
        "code_content": "CodeContent",
    }

    code_content_type: Optional[Union[str, CodeContentType, Ref, GetAtt, Sub]] = None
    code_content: Optional[CodeContent] = None


@dataclass
class ApplicationConfiguration(PropertyType):
    APPLICATION_CODE_CONFIGURATION = "ApplicationCodeConfiguration"
    APPLICATION_ENCRYPTION_CONFIGURATION = "ApplicationEncryptionConfiguration"
    ENVIRONMENT_PROPERTIES = "EnvironmentProperties"
    FLINK_APPLICATION_CONFIGURATION = "FlinkApplicationConfiguration"
    SQL_APPLICATION_CONFIGURATION = "SqlApplicationConfiguration"
    ZEPPELIN_APPLICATION_CONFIGURATION = "ZeppelinApplicationConfiguration"
    VPC_CONFIGURATIONS = "VpcConfigurations"
    APPLICATION_SNAPSHOT_CONFIGURATION = "ApplicationSnapshotConfiguration"
    APPLICATION_SYSTEM_ROLLBACK_CONFIGURATION = "ApplicationSystemRollbackConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_code_configuration": "ApplicationCodeConfiguration",
        "application_encryption_configuration": "ApplicationEncryptionConfiguration",
        "environment_properties": "EnvironmentProperties",
        "flink_application_configuration": "FlinkApplicationConfiguration",
        "sql_application_configuration": "SqlApplicationConfiguration",
        "zeppelin_application_configuration": "ZeppelinApplicationConfiguration",
        "vpc_configurations": "VpcConfigurations",
        "application_snapshot_configuration": "ApplicationSnapshotConfiguration",
        "application_system_rollback_configuration": "ApplicationSystemRollbackConfiguration",
    }

    application_code_configuration: Optional[ApplicationCodeConfiguration] = None
    application_encryption_configuration: Optional[ApplicationEncryptionConfiguration] = None
    environment_properties: Optional[EnvironmentProperties] = None
    flink_application_configuration: Optional[FlinkApplicationConfiguration] = None
    sql_application_configuration: Optional[SqlApplicationConfiguration] = None
    zeppelin_application_configuration: Optional[ZeppelinApplicationConfiguration] = None
    vpc_configurations: Optional[list[VpcConfiguration]] = None
    application_snapshot_configuration: Optional[ApplicationSnapshotConfiguration] = None
    application_system_rollback_configuration: Optional[ApplicationSystemRollbackConfiguration] = None


@dataclass
class ApplicationEncryptionConfiguration(PropertyType):
    KEY_TYPE = "KeyType"
    KEY_ID = "KeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_type": "KeyType",
        "key_id": "KeyId",
    }

    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationMaintenanceConfiguration(PropertyType):
    APPLICATION_MAINTENANCE_WINDOW_START_TIME = "ApplicationMaintenanceWindowStartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_maintenance_window_start_time": "ApplicationMaintenanceWindowStartTime",
    }

    application_maintenance_window_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationRestoreConfiguration(PropertyType):
    SNAPSHOT_NAME = "SnapshotName"
    APPLICATION_RESTORE_TYPE = "ApplicationRestoreType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_name": "SnapshotName",
        "application_restore_type": "ApplicationRestoreType",
    }

    snapshot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_restore_type: Optional[Union[str, ApplicationRestoreType, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationSnapshotConfiguration(PropertyType):
    SNAPSHOTS_ENABLED = "SnapshotsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshots_enabled": "SnapshotsEnabled",
    }

    snapshots_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationSystemRollbackConfiguration(PropertyType):
    ROLLBACK_ENABLED = "RollbackEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rollback_enabled": "RollbackEnabled",
    }

    rollback_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


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
class CatalogConfiguration(PropertyType):
    GLUE_DATA_CATALOG_CONFIGURATION = "GlueDataCatalogConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_data_catalog_configuration": "GlueDataCatalogConfiguration",
    }

    glue_data_catalog_configuration: Optional[GlueDataCatalogConfiguration] = None


@dataclass
class CheckpointConfiguration(PropertyType):
    CONFIGURATION_TYPE = "ConfigurationType"
    CHECKPOINT_INTERVAL = "CheckpointInterval"
    MIN_PAUSE_BETWEEN_CHECKPOINTS = "MinPauseBetweenCheckpoints"
    CHECKPOINTING_ENABLED = "CheckpointingEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_type": "ConfigurationType",
        "checkpoint_interval": "CheckpointInterval",
        "min_pause_between_checkpoints": "MinPauseBetweenCheckpoints",
        "checkpointing_enabled": "CheckpointingEnabled",
    }

    configuration_type: Optional[Union[str, ConfigurationType, Ref, GetAtt, Sub]] = None
    checkpoint_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_pause_between_checkpoints: Optional[Union[int, Ref, GetAtt, Sub]] = None
    checkpointing_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CodeContent(PropertyType):
    ZIP_FILE_CONTENT = "ZipFileContent"
    S3_CONTENT_LOCATION = "S3ContentLocation"
    TEXT_CONTENT = "TextContent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "zip_file_content": "ZipFileContent",
        "s3_content_location": "S3ContentLocation",
        "text_content": "TextContent",
    }

    zip_file_content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_content_location: Optional[S3ContentLocation] = None
    text_content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomArtifactConfiguration(PropertyType):
    MAVEN_REFERENCE = "MavenReference"
    S3_CONTENT_LOCATION = "S3ContentLocation"
    ARTIFACT_TYPE = "ArtifactType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maven_reference": "MavenReference",
        "s3_content_location": "S3ContentLocation",
        "artifact_type": "ArtifactType",
    }

    maven_reference: Optional[MavenReference] = None
    s3_content_location: Optional[S3ContentLocation] = None
    artifact_type: Optional[Union[str, ArtifactType, Ref, GetAtt, Sub]] = None


@dataclass
class DeployAsApplicationConfiguration(PropertyType):
    S3_CONTENT_LOCATION = "S3ContentLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_content_location": "S3ContentLocation",
    }

    s3_content_location: Optional[S3ContentBaseLocation] = None


@dataclass
class EnvironmentProperties(PropertyType):
    PROPERTY_GROUPS = "PropertyGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "property_groups": "PropertyGroups",
    }

    property_groups: Optional[list[PropertyGroup]] = None


@dataclass
class FlinkApplicationConfiguration(PropertyType):
    CHECKPOINT_CONFIGURATION = "CheckpointConfiguration"
    PARALLELISM_CONFIGURATION = "ParallelismConfiguration"
    MONITORING_CONFIGURATION = "MonitoringConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "checkpoint_configuration": "CheckpointConfiguration",
        "parallelism_configuration": "ParallelismConfiguration",
        "monitoring_configuration": "MonitoringConfiguration",
    }

    checkpoint_configuration: Optional[CheckpointConfiguration] = None
    parallelism_configuration: Optional[ParallelismConfiguration] = None
    monitoring_configuration: Optional[MonitoringConfiguration] = None


@dataclass
class FlinkRunConfiguration(PropertyType):
    ALLOW_NON_RESTORED_STATE = "AllowNonRestoredState"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_non_restored_state": "AllowNonRestoredState",
    }

    allow_non_restored_state: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GlueDataCatalogConfiguration(PropertyType):
    DATABASE_ARN = "DatabaseARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_arn": "DatabaseARN",
    }

    database_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Input(PropertyType):
    NAME_PREFIX = "NamePrefix"
    INPUT_SCHEMA = "InputSchema"
    KINESIS_STREAMS_INPUT = "KinesisStreamsInput"
    KINESIS_FIREHOSE_INPUT = "KinesisFirehoseInput"
    INPUT_PROCESSING_CONFIGURATION = "InputProcessingConfiguration"
    INPUT_PARALLELISM = "InputParallelism"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name_prefix": "NamePrefix",
        "input_schema": "InputSchema",
        "kinesis_streams_input": "KinesisStreamsInput",
        "kinesis_firehose_input": "KinesisFirehoseInput",
        "input_processing_configuration": "InputProcessingConfiguration",
        "input_parallelism": "InputParallelism",
    }

    name_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_schema: Optional[InputSchema] = None
    kinesis_streams_input: Optional[KinesisStreamsInput] = None
    kinesis_firehose_input: Optional[KinesisFirehoseInput] = None
    input_processing_configuration: Optional[InputProcessingConfiguration] = None
    input_parallelism: Optional[InputParallelism] = None


@dataclass
class InputLambdaProcessor(PropertyType):
    RESOURCE_ARN = "ResourceARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputParallelism(PropertyType):
    COUNT = "Count"

    _property_mappings: ClassVar[dict[str, str]] = {
        "count": "Count",
    }

    count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InputProcessingConfiguration(PropertyType):
    INPUT_LAMBDA_PROCESSOR = "InputLambdaProcessor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_lambda_processor": "InputLambdaProcessor",
    }

    input_lambda_processor: Optional[InputLambdaProcessor] = None


@dataclass
class InputSchema(PropertyType):
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
class JSONMappingParameters(PropertyType):
    RECORD_ROW_PATH = "RecordRowPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "record_row_path": "RecordRowPath",
    }

    record_row_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisFirehoseInput(PropertyType):
    RESOURCE_ARN = "ResourceARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamsInput(PropertyType):
    RESOURCE_ARN = "ResourceARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class MavenReference(PropertyType):
    ARTIFACT_ID = "ArtifactId"
    VERSION = "Version"
    GROUP_ID = "GroupId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "artifact_id": "ArtifactId",
        "version": "Version",
        "group_id": "GroupId",
    }

    artifact_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringConfiguration(PropertyType):
    CONFIGURATION_TYPE = "ConfigurationType"
    METRICS_LEVEL = "MetricsLevel"
    LOG_LEVEL = "LogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_type": "ConfigurationType",
        "metrics_level": "MetricsLevel",
        "log_level": "LogLevel",
    }

    configuration_type: Optional[Union[str, ConfigurationType, Ref, GetAtt, Sub]] = None
    metrics_level: Optional[Union[str, MetricsLevel, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, LogLevel, Ref, GetAtt, Sub]] = None


@dataclass
class ParallelismConfiguration(PropertyType):
    CONFIGURATION_TYPE = "ConfigurationType"
    PARALLELISM_PER_KPU = "ParallelismPerKPU"
    AUTO_SCALING_ENABLED = "AutoScalingEnabled"
    PARALLELISM = "Parallelism"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_type": "ConfigurationType",
        "parallelism_per_kpu": "ParallelismPerKPU",
        "auto_scaling_enabled": "AutoScalingEnabled",
        "parallelism": "Parallelism",
    }

    configuration_type: Optional[Union[str, ConfigurationType, Ref, GetAtt, Sub]] = None
    parallelism_per_kpu: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_scaling_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    parallelism: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PropertyGroup(PropertyType):
    PROPERTY_MAP = "PropertyMap"
    PROPERTY_GROUP_ID = "PropertyGroupId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "property_map": "PropertyMap",
        "property_group_id": "PropertyGroupId",
    }

    property_map: Optional[dict[str, str]] = None
    property_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class RunConfiguration(PropertyType):
    FLINK_RUN_CONFIGURATION = "FlinkRunConfiguration"
    APPLICATION_RESTORE_CONFIGURATION = "ApplicationRestoreConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flink_run_configuration": "FlinkRunConfiguration",
        "application_restore_configuration": "ApplicationRestoreConfiguration",
    }

    flink_run_configuration: Optional[FlinkRunConfiguration] = None
    application_restore_configuration: Optional[ApplicationRestoreConfiguration] = None


@dataclass
class S3ContentBaseLocation(PropertyType):
    BUCKET_ARN = "BucketARN"
    BASE_PATH = "BasePath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "base_path": "BasePath",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3ContentLocation(PropertyType):
    BUCKET_ARN = "BucketARN"
    FILE_KEY = "FileKey"
    OBJECT_VERSION = "ObjectVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "file_key": "FileKey",
        "object_version": "ObjectVersion",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SqlApplicationConfiguration(PropertyType):
    INPUTS = "Inputs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: Optional[list[Input]] = None


@dataclass
class VpcConfiguration(PropertyType):
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ZeppelinApplicationConfiguration(PropertyType):
    CATALOG_CONFIGURATION = "CatalogConfiguration"
    MONITORING_CONFIGURATION = "MonitoringConfiguration"
    DEPLOY_AS_APPLICATION_CONFIGURATION = "DeployAsApplicationConfiguration"
    CUSTOM_ARTIFACTS_CONFIGURATION = "CustomArtifactsConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_configuration": "CatalogConfiguration",
        "monitoring_configuration": "MonitoringConfiguration",
        "deploy_as_application_configuration": "DeployAsApplicationConfiguration",
        "custom_artifacts_configuration": "CustomArtifactsConfiguration",
    }

    catalog_configuration: Optional[CatalogConfiguration] = None
    monitoring_configuration: Optional[ZeppelinMonitoringConfiguration] = None
    deploy_as_application_configuration: Optional[DeployAsApplicationConfiguration] = None
    custom_artifacts_configuration: Optional[list[CustomArtifactConfiguration]] = None


@dataclass
class ZeppelinMonitoringConfiguration(PropertyType):
    LOG_LEVEL = "LogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_level": "LogLevel",
    }

    log_level: Optional[Union[str, LogLevel, Ref, GetAtt, Sub]] = None

