"""PropertyTypes for AWS::KinesisAnalytics::ApplicationReferenceDataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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
    REFERENCE_ROLE_ARN = "ReferenceRoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "file_key": "FileKey",
        "reference_role_arn": "ReferenceRoleARN",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reference_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

