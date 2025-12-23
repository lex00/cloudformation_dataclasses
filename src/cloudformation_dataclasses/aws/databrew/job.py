"""PropertyTypes for AWS::DataBrew::Job."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AllowedStatistics(PropertyType):
    STATISTICS = "Statistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statistics": "Statistics",
    }

    statistics: Optional[Union[list[str], Ref]] = None


@dataclass
class ColumnSelector(PropertyType):
    REGEX = "Regex"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regex": "Regex",
        "name": "Name",
    }

    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColumnStatisticsConfiguration(PropertyType):
    STATISTICS = "Statistics"
    SELECTORS = "Selectors"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statistics": "Statistics",
        "selectors": "Selectors",
    }

    statistics: Optional[StatisticsConfiguration] = None
    selectors: Optional[list[ColumnSelector]] = None


@dataclass
class CsvOutputOptions(PropertyType):
    DELIMITER = "Delimiter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataCatalogOutput(PropertyType):
    TABLE_NAME = "TableName"
    OVERWRITE = "Overwrite"
    S3_OPTIONS = "S3Options"
    DATABASE_OPTIONS = "DatabaseOptions"
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "overwrite": "Overwrite",
        "s3_options": "S3Options",
        "database_options": "DatabaseOptions",
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    s3_options: Optional[S3TableOutputOptions] = None
    database_options: Optional[DatabaseTableOutputOptions] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseOutput(PropertyType):
    DATABASE_OUTPUT_MODE = "DatabaseOutputMode"
    DATABASE_OPTIONS = "DatabaseOptions"
    GLUE_CONNECTION_NAME = "GlueConnectionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_output_mode": "DatabaseOutputMode",
        "database_options": "DatabaseOptions",
        "glue_connection_name": "GlueConnectionName",
    }

    database_output_mode: Optional[Union[str, DatabaseOutputMode, Ref, GetAtt, Sub]] = None
    database_options: Optional[DatabaseTableOutputOptions] = None
    glue_connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseTableOutputOptions(PropertyType):
    TEMP_DIRECTORY = "TempDirectory"
    TABLE_NAME = "TableName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "temp_directory": "TempDirectory",
        "table_name": "TableName",
    }

    temp_directory: Optional[S3Location] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EntityDetectorConfiguration(PropertyType):
    ENTITY_TYPES = "EntityTypes"
    ALLOWED_STATISTICS = "AllowedStatistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_types": "EntityTypes",
        "allowed_statistics": "AllowedStatistics",
    }

    entity_types: Optional[Union[list[str], Ref]] = None
    allowed_statistics: Optional[AllowedStatistics] = None


@dataclass
class JobSample(PropertyType):
    SIZE = "Size"
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size": "Size",
        "mode": "Mode",
    }

    size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, SampleMode, Ref, GetAtt, Sub]] = None


@dataclass
class Output(PropertyType):
    OVERWRITE = "Overwrite"
    FORMAT = "Format"
    MAX_OUTPUT_FILES = "MaxOutputFiles"
    COMPRESSION_FORMAT = "CompressionFormat"
    PARTITION_COLUMNS = "PartitionColumns"
    FORMAT_OPTIONS = "FormatOptions"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overwrite": "Overwrite",
        "format": "Format",
        "max_output_files": "MaxOutputFiles",
        "compression_format": "CompressionFormat",
        "partition_columns": "PartitionColumns",
        "format_options": "FormatOptions",
        "location": "Location",
    }

    overwrite: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, OutputFormat, Ref, GetAtt, Sub]] = None
    max_output_files: Optional[Union[int, Ref, GetAtt, Sub]] = None
    compression_format: Optional[Union[str, CompressionFormat, Ref, GetAtt, Sub]] = None
    partition_columns: Optional[Union[list[str], Ref]] = None
    format_options: Optional[OutputFormatOptions] = None
    location: Optional[S3Location] = None


@dataclass
class OutputFormatOptions(PropertyType):
    CSV = "Csv"

    _property_mappings: ClassVar[dict[str, str]] = {
        "csv": "Csv",
    }

    csv: Optional[CsvOutputOptions] = None


@dataclass
class OutputLocation(PropertyType):
    BUCKET = "Bucket"
    BUCKET_OWNER = "BucketOwner"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "bucket_owner": "BucketOwner",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProfileConfiguration(PropertyType):
    PROFILE_COLUMNS = "ProfileColumns"
    DATASET_STATISTICS_CONFIGURATION = "DatasetStatisticsConfiguration"
    COLUMN_STATISTICS_CONFIGURATIONS = "ColumnStatisticsConfigurations"
    ENTITY_DETECTOR_CONFIGURATION = "EntityDetectorConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "profile_columns": "ProfileColumns",
        "dataset_statistics_configuration": "DatasetStatisticsConfiguration",
        "column_statistics_configurations": "ColumnStatisticsConfigurations",
        "entity_detector_configuration": "EntityDetectorConfiguration",
    }

    profile_columns: Optional[list[ColumnSelector]] = None
    dataset_statistics_configuration: Optional[StatisticsConfiguration] = None
    column_statistics_configurations: Optional[list[ColumnStatisticsConfiguration]] = None
    entity_detector_configuration: Optional[EntityDetectorConfiguration] = None


@dataclass
class Recipe(PropertyType):
    VERSION = "Version"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "name": "Name",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    BUCKET_OWNER = "BucketOwner"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "bucket_owner": "BucketOwner",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3TableOutputOptions(PropertyType):
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "location": "Location",
    }

    location: Optional[S3Location] = None


@dataclass
class StatisticOverride(PropertyType):
    PARAMETERS = "Parameters"
    STATISTIC = "Statistic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "statistic": "Statistic",
    }

    parameters: Optional[dict[str, str]] = None
    statistic: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StatisticsConfiguration(PropertyType):
    INCLUDED_STATISTICS = "IncludedStatistics"
    OVERRIDES = "Overrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "included_statistics": "IncludedStatistics",
        "overrides": "Overrides",
    }

    included_statistics: Optional[Union[list[str], Ref]] = None
    overrides: Optional[list[StatisticOverride]] = None


@dataclass
class ValidationConfiguration(PropertyType):
    RULESET_ARN = "RulesetArn"
    VALIDATION_MODE = "ValidationMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ruleset_arn": "RulesetArn",
        "validation_mode": "ValidationMode",
    }

    ruleset_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    validation_mode: Optional[Union[str, ValidationMode, Ref, GetAtt, Sub]] = None

