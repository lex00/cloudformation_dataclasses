"""PropertyTypes for AWS::DataBrew::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CsvOptions(PropertyType):
    DELIMITER = "Delimiter"
    HEADER_ROW = "HeaderRow"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "header_row": "HeaderRow",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_row: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataCatalogInputDefinition(PropertyType):
    TABLE_NAME = "TableName"
    TEMP_DIRECTORY = "TempDirectory"
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "temp_directory": "TempDirectory",
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    temp_directory: Optional[S3Location] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseInputDefinition(PropertyType):
    TEMP_DIRECTORY = "TempDirectory"
    QUERY_STRING = "QueryString"
    GLUE_CONNECTION_NAME = "GlueConnectionName"
    DATABASE_TABLE_NAME = "DatabaseTableName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "temp_directory": "TempDirectory",
        "query_string": "QueryString",
        "glue_connection_name": "GlueConnectionName",
        "database_table_name": "DatabaseTableName",
    }

    temp_directory: Optional[S3Location] = None
    query_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    glue_connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetParameter(PropertyType):
    TYPE = "Type"
    DATETIME_OPTIONS = "DatetimeOptions"
    FILTER = "Filter"
    CREATE_COLUMN = "CreateColumn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "datetime_options": "DatetimeOptions",
        "filter": "Filter",
        "create_column": "CreateColumn",
        "name": "Name",
    }

    type_: Optional[Union[str, ParameterType, Ref, GetAtt, Sub]] = None
    datetime_options: Optional[DatetimeOptions] = None
    filter: Optional[FilterExpression] = None
    create_column: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatetimeOptions(PropertyType):
    LOCALE_CODE = "LocaleCode"
    FORMAT = "Format"
    TIMEZONE_OFFSET = "TimezoneOffset"

    _property_mappings: ClassVar[dict[str, str]] = {
        "locale_code": "LocaleCode",
        "format": "Format",
        "timezone_offset": "TimezoneOffset",
    }

    locale_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timezone_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExcelOptions(PropertyType):
    HEADER_ROW = "HeaderRow"
    SHEET_NAMES = "SheetNames"
    SHEET_INDEXES = "SheetIndexes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "header_row": "HeaderRow",
        "sheet_names": "SheetNames",
        "sheet_indexes": "SheetIndexes",
    }

    header_row: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sheet_names: Optional[Union[list[str], Ref]] = None
    sheet_indexes: Optional[Union[list[int], Ref]] = None


@dataclass
class FilesLimit(PropertyType):
    ORDER = "Order"
    ORDERED_BY = "OrderedBy"
    MAX_FILES = "MaxFiles"

    _property_mappings: ClassVar[dict[str, str]] = {
        "order": "Order",
        "ordered_by": "OrderedBy",
        "max_files": "MaxFiles",
    }

    order: Optional[Union[str, Order, Ref, GetAtt, Sub]] = None
    ordered_by: Optional[Union[str, OrderedBy, Ref, GetAtt, Sub]] = None
    max_files: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FilterExpression(PropertyType):
    EXPRESSION = "Expression"
    VALUES_MAP = "ValuesMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "values_map": "ValuesMap",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values_map: Optional[list[FilterValue]] = None


@dataclass
class FilterValue(PropertyType):
    VALUE = "Value"
    VALUE_REFERENCE = "ValueReference"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "value_reference": "ValueReference",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormatOptions(PropertyType):
    EXCEL = "Excel"
    CSV = "Csv"
    JSON = "Json"

    _property_mappings: ClassVar[dict[str, str]] = {
        "excel": "Excel",
        "csv": "Csv",
        "json": "Json",
    }

    excel: Optional[ExcelOptions] = None
    csv: Optional[CsvOptions] = None
    json: Optional[JsonOptions] = None


@dataclass
class Input(PropertyType):
    DATABASE_INPUT_DEFINITION = "DatabaseInputDefinition"
    S3_INPUT_DEFINITION = "S3InputDefinition"
    METADATA = "Metadata"
    DATA_CATALOG_INPUT_DEFINITION = "DataCatalogInputDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_input_definition": "DatabaseInputDefinition",
        "s3_input_definition": "S3InputDefinition",
        "metadata": "Metadata",
        "data_catalog_input_definition": "DataCatalogInputDefinition",
    }

    database_input_definition: Optional[DatabaseInputDefinition] = None
    s3_input_definition: Optional[S3Location] = None
    metadata: Optional[Metadata] = None
    data_catalog_input_definition: Optional[DataCatalogInputDefinition] = None


@dataclass
class JsonOptions(PropertyType):
    MULTI_LINE = "MultiLine"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_line": "MultiLine",
    }

    multi_line: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Metadata(PropertyType):
    SOURCE_ARN = "SourceArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_arn": "SourceArn",
    }

    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PathOptions(PropertyType):
    PARAMETERS = "Parameters"
    LAST_MODIFIED_DATE_CONDITION = "LastModifiedDateCondition"
    FILES_LIMIT = "FilesLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "last_modified_date_condition": "LastModifiedDateCondition",
        "files_limit": "FilesLimit",
    }

    parameters: Optional[list[PathParameter]] = None
    last_modified_date_condition: Optional[FilterExpression] = None
    files_limit: Optional[FilesLimit] = None


@dataclass
class PathParameter(PropertyType):
    PATH_PARAMETER_NAME = "PathParameterName"
    DATASET_PARAMETER = "DatasetParameter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path_parameter_name": "PathParameterName",
        "dataset_parameter": "DatasetParameter",
    }

    path_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataset_parameter: Optional[DatasetParameter] = None


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

