"""PropertyTypes for AWS::KinesisFirehose::DeliveryStream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmazonOpenSearchServerlessBufferingHints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_in_seconds": "IntervalInSeconds",
        "size_in_m_bs": "SizeInMBs",
    }

    interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AmazonOpenSearchServerlessDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "s3_configuration": "S3Configuration",
        "buffering_hints": "BufferingHints",
        "retry_options": "RetryOptions",
        "collection_endpoint": "CollectionEndpoint",
        "vpc_configuration": "VpcConfiguration",
        "processing_configuration": "ProcessingConfiguration",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
        "role_arn": "RoleARN",
        "s3_backup_mode": "S3BackupMode",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    buffering_hints: Optional[AmazonOpenSearchServerlessBufferingHints] = None
    retry_options: Optional[AmazonOpenSearchServerlessRetryOptions] = None
    collection_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_configuration: Optional[VpcConfiguration] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_mode: Optional[Union[str, AmazonOpenSearchServerlessS3BackupMode, Ref, GetAtt, Sub]] = None


@dataclass
class AmazonOpenSearchServerlessRetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AmazonopensearchserviceBufferingHints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_in_seconds": "IntervalInSeconds",
        "size_in_m_bs": "SizeInMBs",
    }

    interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AmazonopensearchserviceDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_name": "TypeName",
        "index_rotation_period": "IndexRotationPeriod",
        "processing_configuration": "ProcessingConfiguration",
        "cluster_endpoint": "ClusterEndpoint",
        "domain_arn": "DomainARN",
        "role_arn": "RoleARN",
        "s3_backup_mode": "S3BackupMode",
        "index_name": "IndexName",
        "document_id_options": "DocumentIdOptions",
        "s3_configuration": "S3Configuration",
        "buffering_hints": "BufferingHints",
        "retry_options": "RetryOptions",
        "vpc_configuration": "VpcConfiguration",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
    }

    type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index_rotation_period: Optional[Union[str, AmazonopensearchserviceIndexRotationPeriod, Ref, GetAtt, Sub]] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    cluster_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_mode: Optional[Union[str, AmazonopensearchserviceS3BackupMode, Ref, GetAtt, Sub]] = None
    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    document_id_options: Optional[DocumentIdOptions] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    buffering_hints: Optional[AmazonopensearchserviceBufferingHints] = None
    retry_options: Optional[AmazonopensearchserviceRetryOptions] = None
    vpc_configuration: Optional[VpcConfiguration] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None


@dataclass
class AmazonopensearchserviceRetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AuthenticationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connectivity": "Connectivity",
        "role_arn": "RoleARN",
    }

    connectivity: Optional[Union[str, Connectivity, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BufferingHints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_in_seconds": "IntervalInSeconds",
        "size_in_m_bs": "SizeInMBs",
    }

    interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CatalogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_arn": "CatalogArn",
        "warehouse_location": "WarehouseLocation",
    }

    catalog_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    warehouse_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLoggingOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_name": "LogStreamName",
        "enabled": "Enabled",
        "log_group_name": "LogGroupName",
    }

    log_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CopyCommand(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_table_name": "DataTableName",
        "copy_options": "CopyOptions",
        "data_table_columns": "DataTableColumns",
    }

    data_table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_options: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_table_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataFormatConversionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_format_configuration": "InputFormatConfiguration",
        "enabled": "Enabled",
        "schema_configuration": "SchemaConfiguration",
        "output_format_configuration": "OutputFormatConfiguration",
    }

    input_format_configuration: Optional[InputFormatConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    schema_configuration: Optional[SchemaConfiguration] = None
    output_format_configuration: Optional[OutputFormatConfiguration] = None


@dataclass
class DatabaseColumns(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class DatabaseSourceAuthenticationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager_configuration": "SecretsManagerConfiguration",
    }

    secrets_manager_configuration: Optional[SecretsManagerConfiguration] = None


@dataclass
class DatabaseSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "digest": "Digest",
        "port": "Port",
        "public_certificate": "PublicCertificate",
        "columns": "Columns",
        "type_": "Type",
        "surrogate_keys": "SurrogateKeys",
        "databases": "Databases",
        "endpoint": "Endpoint",
        "ssl_mode": "SSLMode",
        "snapshot_watermark_table": "SnapshotWatermarkTable",
        "database_source_authentication_configuration": "DatabaseSourceAuthenticationConfiguration",
        "tables": "Tables",
        "database_source_vpc_configuration": "DatabaseSourceVPCConfiguration",
    }

    digest: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    public_certificate: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[DatabaseColumns] = None
    type_: Optional[Union[str, DatabaseType, Ref, GetAtt, Sub]] = None
    surrogate_keys: Optional[Union[list[str], Ref]] = None
    databases: Optional[Databases] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssl_mode: Optional[Union[str, SSLMode, Ref, GetAtt, Sub]] = None
    snapshot_watermark_table: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_source_authentication_configuration: Optional[DatabaseSourceAuthenticationConfiguration] = None
    tables: Optional[DatabaseTables] = None
    database_source_vpc_configuration: Optional[DatabaseSourceVPCConfiguration] = None


@dataclass
class DatabaseSourceVPCConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_endpoint_service_name": "VpcEndpointServiceName",
    }

    vpc_endpoint_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseTables(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class Databases(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class DeliveryStreamEncryptionConfigurationInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_type": "KeyType",
        "key_arn": "KeyARN",
    }

    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Deserializer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hive_json_ser_de": "HiveJsonSerDe",
        "open_x_json_ser_de": "OpenXJsonSerDe",
    }

    hive_json_ser_de: Optional[HiveJsonSerDe] = None
    open_x_json_ser_de: Optional[OpenXJsonSerDe] = None


@dataclass
class DestinationTableConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_database_name": "DestinationDatabaseName",
        "s3_error_output_prefix": "S3ErrorOutputPrefix",
        "destination_table_name": "DestinationTableName",
        "unique_keys": "UniqueKeys",
        "partition_spec": "PartitionSpec",
    }

    destination_database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_error_output_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unique_keys: Optional[Union[list[str], Ref]] = None
    partition_spec: Optional[PartitionSpec] = None


@dataclass
class DirectPutSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "throughput_hint_in_m_bs": "ThroughputHintInMBs",
    }

    throughput_hint_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentIdOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_document_id_format": "DefaultDocumentIdFormat",
    }

    default_document_id_format: Optional[Union[str, DefaultDocumentIdFormat, Ref, GetAtt, Sub]] = None


@dataclass
class DynamicPartitioningConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "retry_options": "RetryOptions",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    retry_options: Optional[RetryOptions] = None


@dataclass
class ElasticsearchBufferingHints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_in_seconds": "IntervalInSeconds",
        "size_in_m_bs": "SizeInMBs",
    }

    interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticsearchDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_name": "TypeName",
        "index_rotation_period": "IndexRotationPeriod",
        "processing_configuration": "ProcessingConfiguration",
        "cluster_endpoint": "ClusterEndpoint",
        "domain_arn": "DomainARN",
        "role_arn": "RoleARN",
        "s3_backup_mode": "S3BackupMode",
        "index_name": "IndexName",
        "document_id_options": "DocumentIdOptions",
        "s3_configuration": "S3Configuration",
        "buffering_hints": "BufferingHints",
        "retry_options": "RetryOptions",
        "vpc_configuration": "VpcConfiguration",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
    }

    type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index_rotation_period: Optional[Union[str, ElasticsearchIndexRotationPeriod, Ref, GetAtt, Sub]] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    cluster_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_mode: Optional[Union[str, ElasticsearchS3BackupMode, Ref, GetAtt, Sub]] = None
    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    document_id_options: Optional[DocumentIdOptions] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    buffering_hints: Optional[ElasticsearchBufferingHints] = None
    retry_options: Optional[ElasticsearchRetryOptions] = None
    vpc_configuration: Optional[VpcConfiguration] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None


@dataclass
class ElasticsearchRetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_encryption_config": "KMSEncryptionConfig",
        "no_encryption_config": "NoEncryptionConfig",
    }

    kms_encryption_config: Optional[KMSEncryptionConfig] = None
    no_encryption_config: Optional[Union[str, NoEncryptionConfig, Ref, GetAtt, Sub]] = None


@dataclass
class ExtendedS3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "error_output_prefix": "ErrorOutputPrefix",
        "s3_backup_configuration": "S3BackupConfiguration",
        "bucket_arn": "BucketARN",
        "compression_format": "CompressionFormat",
        "data_format_conversion_configuration": "DataFormatConversionConfiguration",
        "encryption_configuration": "EncryptionConfiguration",
        "custom_time_zone": "CustomTimeZone",
        "dynamic_partitioning_configuration": "DynamicPartitioningConfiguration",
        "prefix": "Prefix",
        "processing_configuration": "ProcessingConfiguration",
        "role_arn": "RoleARN",
        "s3_backup_mode": "S3BackupMode",
        "buffering_hints": "BufferingHints",
        "file_extension": "FileExtension",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
    }

    error_output_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_configuration: Optional[S3DestinationConfiguration] = None
    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    compression_format: Optional[Union[str, CompressionFormat, Ref, GetAtt, Sub]] = None
    data_format_conversion_configuration: Optional[DataFormatConversionConfiguration] = None
    encryption_configuration: Optional[EncryptionConfiguration] = None
    custom_time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dynamic_partitioning_configuration: Optional[DynamicPartitioningConfiguration] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_mode: Optional[Union[str, S3BackupMode, Ref, GetAtt, Sub]] = None
    buffering_hints: Optional[BufferingHints] = None
    file_extension: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None


@dataclass
class HiveJsonSerDe(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timestamp_formats": "TimestampFormats",
    }

    timestamp_formats: Optional[Union[list[str], Ref]] = None


@dataclass
class HttpEndpointCommonAttribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_value": "AttributeValue",
        "attribute_name": "AttributeName",
    }

    attribute_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpEndpointConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_key": "AccessKey",
        "url": "Url",
        "name": "Name",
    }

    access_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpEndpointDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "request_configuration": "RequestConfiguration",
        "s3_configuration": "S3Configuration",
        "buffering_hints": "BufferingHints",
        "retry_options": "RetryOptions",
        "secrets_manager_configuration": "SecretsManagerConfiguration",
        "endpoint_configuration": "EndpointConfiguration",
        "processing_configuration": "ProcessingConfiguration",
        "role_arn": "RoleARN",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
        "s3_backup_mode": "S3BackupMode",
    }

    request_configuration: Optional[HttpEndpointRequestConfiguration] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    buffering_hints: Optional[BufferingHints] = None
    retry_options: Optional[RetryOptions] = None
    secrets_manager_configuration: Optional[SecretsManagerConfiguration] = None
    endpoint_configuration: Optional[HttpEndpointConfiguration] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None
    s3_backup_mode: Optional[Union[str, HttpEndpointS3BackupMode, Ref, GetAtt, Sub]] = None


@dataclass
class HttpEndpointRequestConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "common_attributes": "CommonAttributes",
        "content_encoding": "ContentEncoding",
    }

    common_attributes: Optional[list[HttpEndpointCommonAttribute]] = None
    content_encoding: Optional[Union[str, ContentEncoding, Ref, GetAtt, Sub]] = None


@dataclass
class IcebergDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_configuration": "CatalogConfiguration",
        "s3_configuration": "S3Configuration",
        "destination_table_configuration_list": "DestinationTableConfigurationList",
        "buffering_hints": "BufferingHints",
        "table_creation_configuration": "TableCreationConfiguration",
        "retry_options": "RetryOptions",
        "s3_backup_mode": "s3BackupMode",
        "processing_configuration": "ProcessingConfiguration",
        "schema_evolution_configuration": "SchemaEvolutionConfiguration",
        "append_only": "AppendOnly",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
        "role_arn": "RoleARN",
    }

    catalog_configuration: Optional[CatalogConfiguration] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    destination_table_configuration_list: Optional[list[DestinationTableConfiguration]] = None
    buffering_hints: Optional[BufferingHints] = None
    table_creation_configuration: Optional[TableCreationConfiguration] = None
    retry_options: Optional[RetryOptions] = None
    s3_backup_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    schema_evolution_configuration: Optional[SchemaEvolutionConfiguration] = None
    append_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "deserializer": "Deserializer",
    }

    deserializer: Optional[Deserializer] = None


@dataclass
class KMSEncryptionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "awskms_key_arn": "AWSKMSKeyARN",
    }

    awskms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kinesis_stream_arn": "KinesisStreamARN",
        "role_arn": "RoleARN",
    }

    kinesis_stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MSKSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_configuration": "AuthenticationConfiguration",
        "read_from_timestamp": "ReadFromTimestamp",
        "msk_cluster_arn": "MSKClusterARN",
        "topic_name": "TopicName",
    }

    authentication_configuration: Optional[AuthenticationConfiguration] = None
    read_from_timestamp: Optional[Union[str, Ref, GetAtt, Sub]] = None
    msk_cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenXJsonSerDe(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "convert_dots_in_json_keys_to_underscores": "ConvertDotsInJsonKeysToUnderscores",
        "column_to_json_key_mappings": "ColumnToJsonKeyMappings",
        "case_insensitive": "CaseInsensitive",
    }

    convert_dots_in_json_keys_to_underscores: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    column_to_json_key_mappings: Optional[dict[str, str]] = None
    case_insensitive: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OrcSerDe(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "padding_tolerance": "PaddingTolerance",
        "compression": "Compression",
        "stripe_size_bytes": "StripeSizeBytes",
        "bloom_filter_columns": "BloomFilterColumns",
        "bloom_filter_false_positive_probability": "BloomFilterFalsePositiveProbability",
        "enable_padding": "EnablePadding",
        "format_version": "FormatVersion",
        "row_index_stride": "RowIndexStride",
        "block_size_bytes": "BlockSizeBytes",
        "dictionary_key_threshold": "DictionaryKeyThreshold",
    }

    padding_tolerance: Optional[Union[float, Ref, GetAtt, Sub]] = None
    compression: Optional[Union[str, OrcCompression, Ref, GetAtt, Sub]] = None
    stripe_size_bytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    bloom_filter_columns: Optional[Union[list[str], Ref]] = None
    bloom_filter_false_positive_probability: Optional[Union[float, Ref, GetAtt, Sub]] = None
    enable_padding: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    format_version: Optional[Union[str, OrcFormatVersion, Ref, GetAtt, Sub]] = None
    row_index_stride: Optional[Union[int, Ref, GetAtt, Sub]] = None
    block_size_bytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dictionary_key_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OutputFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "serializer": "Serializer",
    }

    serializer: Optional[Serializer] = None


@dataclass
class ParquetSerDe(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compression": "Compression",
        "block_size_bytes": "BlockSizeBytes",
        "enable_dictionary_compression": "EnableDictionaryCompression",
        "page_size_bytes": "PageSizeBytes",
        "max_padding_bytes": "MaxPaddingBytes",
        "writer_version": "WriterVersion",
    }

    compression: Optional[Union[str, ParquetCompression, Ref, GetAtt, Sub]] = None
    block_size_bytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enable_dictionary_compression: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    page_size_bytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_padding_bytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    writer_version: Optional[Union[str, ParquetWriterVersion, Ref, GetAtt, Sub]] = None


@dataclass
class PartitionField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_name": "SourceName",
    }

    source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PartitionSpec(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "identity": "Identity",
    }

    identity: Optional[list[PartitionField]] = None


@dataclass
class ProcessingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "processors": "Processors",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    processors: Optional[list[Processor]] = None


@dataclass
class Processor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "parameters": "Parameters",
    }

    type_: Optional[Union[str, ProcessorType, Ref, GetAtt, Sub]] = None
    parameters: Optional[list[ProcessorParameter]] = None


@dataclass
class ProcessorParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, ProcessorParameterName, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_backup_configuration": "S3BackupConfiguration",
        "s3_configuration": "S3Configuration",
        "username": "Username",
        "copy_command": "CopyCommand",
        "retry_options": "RetryOptions",
        "secrets_manager_configuration": "SecretsManagerConfiguration",
        "processing_configuration": "ProcessingConfiguration",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
        "cluster_jdbcurl": "ClusterJDBCURL",
        "role_arn": "RoleARN",
        "password": "Password",
        "s3_backup_mode": "S3BackupMode",
    }

    s3_backup_configuration: Optional[S3DestinationConfiguration] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_command: Optional[CopyCommand] = None
    retry_options: Optional[RedshiftRetryOptions] = None
    secrets_manager_configuration: Optional[SecretsManagerConfiguration] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None
    cluster_jdbcurl: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_mode: Optional[Union[str, RedshiftS3BackupMode, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftRetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "error_output_prefix": "ErrorOutputPrefix",
        "bucket_arn": "BucketARN",
        "buffering_hints": "BufferingHints",
        "compression_format": "CompressionFormat",
        "encryption_configuration": "EncryptionConfiguration",
        "prefix": "Prefix",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
        "role_arn": "RoleARN",
    }

    error_output_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    buffering_hints: Optional[BufferingHints] = None
    compression_format: Optional[Union[str, CompressionFormat, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[EncryptionConfiguration] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version_id": "VersionId",
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "region": "Region",
        "catalog_id": "CatalogId",
        "role_arn": "RoleARN",
    }

    version_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaEvolutionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SecretsManagerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretARN",
        "enabled": "Enabled",
        "role_arn": "RoleARN",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Serializer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "orc_ser_de": "OrcSerDe",
        "parquet_ser_de": "ParquetSerDe",
    }

    orc_ser_de: Optional[OrcSerDe] = None
    parquet_ser_de: Optional[ParquetSerDe] = None


@dataclass
class SnowflakeBufferingHints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_in_seconds": "IntervalInSeconds",
        "size_in_m_bs": "SizeInMBs",
    }

    interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_key": "PrivateKey",
        "user": "User",
        "table": "Table",
        "snowflake_vpc_configuration": "SnowflakeVpcConfiguration",
        "data_loading_option": "DataLoadingOption",
        "schema": "Schema",
        "content_column_name": "ContentColumnName",
        "secrets_manager_configuration": "SecretsManagerConfiguration",
        "snowflake_role_configuration": "SnowflakeRoleConfiguration",
        "processing_configuration": "ProcessingConfiguration",
        "account_url": "AccountUrl",
        "role_arn": "RoleARN",
        "s3_backup_mode": "S3BackupMode",
        "s3_configuration": "S3Configuration",
        "buffering_hints": "BufferingHints",
        "meta_data_column_name": "MetaDataColumnName",
        "database": "Database",
        "retry_options": "RetryOptions",
        "key_passphrase": "KeyPassphrase",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
    }

    private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table: Optional[Union[str, Ref, GetAtt, Sub]] = None
    snowflake_vpc_configuration: Optional[SnowflakeVpcConfiguration] = None
    data_loading_option: Optional[Union[str, SnowflakeDataLoadingOption, Ref, GetAtt, Sub]] = None
    schema: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_configuration: Optional[SecretsManagerConfiguration] = None
    snowflake_role_configuration: Optional[SnowflakeRoleConfiguration] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    account_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_backup_mode: Optional[Union[str, SnowflakeS3BackupMode, Ref, GetAtt, Sub]] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    buffering_hints: Optional[SnowflakeBufferingHints] = None
    meta_data_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retry_options: Optional[SnowflakeRetryOptions] = None
    key_passphrase: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None


@dataclass
class SnowflakeRetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeRoleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snowflake_role": "SnowflakeRole",
        "enabled": "Enabled",
    }

    snowflake_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeVpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_link_vpce_id": "PrivateLinkVpceId",
    }

    private_link_vpce_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SplunkBufferingHints(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_in_seconds": "IntervalInSeconds",
        "size_in_m_bs": "SizeInMBs",
    }

    interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_m_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SplunkDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hec_endpoint": "HECEndpoint",
        "s3_configuration": "S3Configuration",
        "buffering_hints": "BufferingHints",
        "hec_token": "HECToken",
        "retry_options": "RetryOptions",
        "hec_endpoint_type": "HECEndpointType",
        "secrets_manager_configuration": "SecretsManagerConfiguration",
        "hec_acknowledgment_timeout_in_seconds": "HECAcknowledgmentTimeoutInSeconds",
        "processing_configuration": "ProcessingConfiguration",
        "cloud_watch_logging_options": "CloudWatchLoggingOptions",
        "s3_backup_mode": "S3BackupMode",
    }

    hec_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_configuration: Optional[S3DestinationConfiguration] = None
    buffering_hints: Optional[SplunkBufferingHints] = None
    hec_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retry_options: Optional[SplunkRetryOptions] = None
    hec_endpoint_type: Optional[Union[str, HECEndpointType, Ref, GetAtt, Sub]] = None
    secrets_manager_configuration: Optional[SecretsManagerConfiguration] = None
    hec_acknowledgment_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    processing_configuration: Optional[ProcessingConfiguration] = None
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptions] = None
    s3_backup_mode: Optional[Union[str, SplunkS3BackupMode, Ref, GetAtt, Sub]] = None


@dataclass
class SplunkRetryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TableCreationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
        "role_arn": "RoleARN",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

