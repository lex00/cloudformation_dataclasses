"""PropertyTypes for AWS::KinesisAnalytics::Application."""

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
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamsInput(PropertyType):
    RESOURCE_ARN = "ResourceARN"
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

