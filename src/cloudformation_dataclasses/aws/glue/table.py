"""PropertyTypes for AWS::Glue::Table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Column(PropertyType):
    COMMENT = "Comment"
    TYPE = "Type"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "type_": "Type",
        "name": "Name",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IcebergInput(PropertyType):
    METADATA_OPERATION = "MetadataOperation"
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metadata_operation": "MetadataOperation",
        "version": "Version",
    }

    metadata_operation: Optional[MetadataOperation] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataOperation(PropertyType):
    pass


@dataclass
class OpenTableFormatInput(PropertyType):
    ICEBERG_INPUT = "IcebergInput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iceberg_input": "IcebergInput",
    }

    iceberg_input: Optional[IcebergInput] = None


@dataclass
class Order(PropertyType):
    COLUMN = "Column"
    SORT_ORDER = "SortOrder"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "sort_order": "SortOrder",
    }

    column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sort_order: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaId(PropertyType):
    REGISTRY_NAME = "RegistryName"
    SCHEMA_NAME = "SchemaName"
    SCHEMA_ARN = "SchemaArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "registry_name": "RegistryName",
        "schema_name": "SchemaName",
        "schema_arn": "SchemaArn",
    }

    registry_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaReference(PropertyType):
    SCHEMA_VERSION_ID = "SchemaVersionId"
    SCHEMA_ID = "SchemaId"
    SCHEMA_VERSION_NUMBER = "SchemaVersionNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_version_id": "SchemaVersionId",
        "schema_id": "SchemaId",
        "schema_version_number": "SchemaVersionNumber",
    }

    schema_version_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_id: Optional[SchemaId] = None
    schema_version_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SerdeInfo(PropertyType):
    PARAMETERS = "Parameters"
    SERIALIZATION_LIBRARY = "SerializationLibrary"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "serialization_library": "SerializationLibrary",
        "name": "Name",
    }

    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    serialization_library: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SkewedInfo(PropertyType):
    SKEWED_COLUMN_NAMES = "SkewedColumnNames"
    SKEWED_COLUMN_VALUES = "SkewedColumnValues"
    SKEWED_COLUMN_VALUE_LOCATION_MAPS = "SkewedColumnValueLocationMaps"

    _property_mappings: ClassVar[dict[str, str]] = {
        "skewed_column_names": "SkewedColumnNames",
        "skewed_column_values": "SkewedColumnValues",
        "skewed_column_value_location_maps": "SkewedColumnValueLocationMaps",
    }

    skewed_column_names: Optional[Union[list[str], Ref]] = None
    skewed_column_values: Optional[Union[list[str], Ref]] = None
    skewed_column_value_location_maps: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class StorageDescriptor(PropertyType):
    STORED_AS_SUB_DIRECTORIES = "StoredAsSubDirectories"
    PARAMETERS = "Parameters"
    BUCKET_COLUMNS = "BucketColumns"
    NUMBER_OF_BUCKETS = "NumberOfBuckets"
    OUTPUT_FORMAT = "OutputFormat"
    COLUMNS = "Columns"
    SERDE_INFO = "SerdeInfo"
    SORT_COLUMNS = "SortColumns"
    COMPRESSED = "Compressed"
    SCHEMA_REFERENCE = "SchemaReference"
    SKEWED_INFO = "SkewedInfo"
    INPUT_FORMAT = "InputFormat"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stored_as_sub_directories": "StoredAsSubDirectories",
        "parameters": "Parameters",
        "bucket_columns": "BucketColumns",
        "number_of_buckets": "NumberOfBuckets",
        "output_format": "OutputFormat",
        "columns": "Columns",
        "serde_info": "SerdeInfo",
        "sort_columns": "SortColumns",
        "compressed": "Compressed",
        "schema_reference": "SchemaReference",
        "skewed_info": "SkewedInfo",
        "input_format": "InputFormat",
        "location": "Location",
    }

    stored_as_sub_directories: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    bucket_columns: Optional[Union[list[str], Ref]] = None
    number_of_buckets: Optional[Union[int, Ref, GetAtt, Sub]] = None
    output_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[Column]] = None
    serde_info: Optional[SerdeInfo] = None
    sort_columns: Optional[list[Order]] = None
    compressed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    schema_reference: Optional[SchemaReference] = None
    skewed_info: Optional[SkewedInfo] = None
    input_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableIdentifier(PropertyType):
    DATABASE_NAME = "DatabaseName"
    REGION = "Region"
    CATALOG_ID = "CatalogId"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
        "region": "Region",
        "catalog_id": "CatalogId",
        "name": "Name",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableInput(PropertyType):
    OWNER = "Owner"
    VIEW_ORIGINAL_TEXT = "ViewOriginalText"
    DESCRIPTION = "Description"
    TABLE_TYPE = "TableType"
    PARAMETERS = "Parameters"
    VIEW_EXPANDED_TEXT = "ViewExpandedText"
    STORAGE_DESCRIPTOR = "StorageDescriptor"
    TARGET_TABLE = "TargetTable"
    PARTITION_KEYS = "PartitionKeys"
    RETENTION = "Retention"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
        "view_original_text": "ViewOriginalText",
        "description": "Description",
        "table_type": "TableType",
        "parameters": "Parameters",
        "view_expanded_text": "ViewExpandedText",
        "storage_descriptor": "StorageDescriptor",
        "target_table": "TargetTable",
        "partition_keys": "PartitionKeys",
        "retention": "Retention",
        "name": "Name",
    }

    owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    view_original_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    view_expanded_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_descriptor: Optional[StorageDescriptor] = None
    target_table: Optional[TableIdentifier] = None
    partition_keys: Optional[list[Column]] = None
    retention: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

