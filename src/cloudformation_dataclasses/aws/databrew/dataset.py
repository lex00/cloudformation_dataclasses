"""PropertyTypes for AWS::DataBrew::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CsvOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "header_row": "HeaderRow",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_row: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataCatalogInputDefinition(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "values_map": "ValuesMap",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values_map: Optional[list[FilterValue]] = None


@dataclass
class FilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "value_reference": "ValueReference",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormatOptions(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_line": "MultiLine",
    }

    multi_line: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Metadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_arn": "SourceArn",
    }

    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PathOptions(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "path_parameter_name": "PathParameterName",
        "dataset_parameter": "DatasetParameter",
    }

    path_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataset_parameter: Optional[DatasetParameter] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "bucket_owner": "BucketOwner",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

