"""PropertyTypes for AWS::KinesisAnalyticsV2::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationCodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code_content_type": "CodeContentType",
        "code_content": "CodeContent",
    }

    code_content_type: Optional[Union[str, CodeContentType, Ref, GetAtt, Sub]] = None
    code_content: Optional[CodeContent] = None


@dataclass
class ApplicationConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_type": "KeyType",
        "key_id": "KeyId",
    }

    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationMaintenanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_maintenance_window_start_time": "ApplicationMaintenanceWindowStartTime",
    }

    application_maintenance_window_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationRestoreConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_name": "SnapshotName",
        "application_restore_type": "ApplicationRestoreType",
    }

    snapshot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_restore_type: Optional[Union[str, ApplicationRestoreType, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationSnapshotConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshots_enabled": "SnapshotsEnabled",
    }

    snapshots_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationSystemRollbackConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rollback_enabled": "RollbackEnabled",
    }

    rollback_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CSVMappingParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "record_row_delimiter": "RecordRowDelimiter",
        "record_column_delimiter": "RecordColumnDelimiter",
    }

    record_row_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_column_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CatalogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_data_catalog_configuration": "GlueDataCatalogConfiguration",
    }

    glue_data_catalog_configuration: Optional[GlueDataCatalogConfiguration] = None


@dataclass
class CheckpointConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_content_location": "S3ContentLocation",
    }

    s3_content_location: Optional[S3ContentBaseLocation] = None


@dataclass
class EnvironmentProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "property_groups": "PropertyGroups",
    }

    property_groups: Optional[list[PropertyGroup]] = None


@dataclass
class FlinkApplicationConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_non_restored_state": "AllowNonRestoredState",
    }

    allow_non_restored_state: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GlueDataCatalogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_arn": "DatabaseARN",
    }

    database_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Input(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputParallelism(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "count": "Count",
    }

    count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InputProcessingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_lambda_processor": "InputLambdaProcessor",
    }

    input_lambda_processor: Optional[InputLambdaProcessor] = None


@dataclass
class InputSchema(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "record_row_path": "RecordRowPath",
    }

    record_row_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisFirehoseInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MappingParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "json_mapping_parameters": "JSONMappingParameters",
        "csv_mapping_parameters": "CSVMappingParameters",
    }

    json_mapping_parameters: Optional[JSONMappingParameters] = None
    csv_mapping_parameters: Optional[CSVMappingParameters] = None


@dataclass
class MavenReference(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "property_map": "PropertyMap",
        "property_group_id": "PropertyGroupId",
    }

    property_map: Optional[dict[str, str]] = None
    property_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecordColumn(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "mapping_parameters": "MappingParameters",
        "record_format_type": "RecordFormatType",
    }

    mapping_parameters: Optional[MappingParameters] = None
    record_format_type: Optional[Union[str, RecordFormatType, Ref, GetAtt, Sub]] = None


@dataclass
class RunConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "flink_run_configuration": "FlinkRunConfiguration",
        "application_restore_configuration": "ApplicationRestoreConfiguration",
    }

    flink_run_configuration: Optional[FlinkRunConfiguration] = None
    application_restore_configuration: Optional[ApplicationRestoreConfiguration] = None


@dataclass
class S3ContentBaseLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "base_path": "BasePath",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3ContentLocation(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: Optional[list[Input]] = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ZeppelinApplicationConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_level": "LogLevel",
    }

    log_level: Optional[Union[str, LogLevel, Ref, GetAtt, Sub]] = None

