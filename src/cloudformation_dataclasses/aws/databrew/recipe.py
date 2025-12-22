"""PropertyTypes for AWS::DataBrew::Recipe."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AnalyticsMode:
    """AnalyticsMode enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class CompressionFormat:
    """CompressionFormat enum values."""

    GZIP = "GZIP"
    LZ4 = "LZ4"
    SNAPPY = "SNAPPY"
    BZIP2 = "BZIP2"
    DEFLATE = "DEFLATE"
    LZO = "LZO"
    BROTLI = "BROTLI"
    ZSTD = "ZSTD"
    ZLIB = "ZLIB"


class DatabaseOutputMode:
    """DatabaseOutputMode enum values."""

    NEW_TABLE = "NEW_TABLE"


class EncryptionMode:
    """EncryptionMode enum values."""

    SSE_KMS = "SSE-KMS"
    SSE_S3 = "SSE-S3"


class InputFormat:
    """InputFormat enum values."""

    CSV = "CSV"
    JSON = "JSON"
    PARQUET = "PARQUET"
    EXCEL = "EXCEL"
    ORC = "ORC"


class JobRunState:
    """JobRunState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"


class JobType:
    """JobType enum values."""

    PROFILE = "PROFILE"
    RECIPE = "RECIPE"


class LogSubscription:
    """LogSubscription enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class Order:
    """Order enum values."""

    DESCENDING = "DESCENDING"
    ASCENDING = "ASCENDING"


class OrderedBy:
    """OrderedBy enum values."""

    LAST_MODIFIED_DATE = "LAST_MODIFIED_DATE"


class OutputFormat:
    """OutputFormat enum values."""

    CSV = "CSV"
    JSON = "JSON"
    PARQUET = "PARQUET"
    GLUEPARQUET = "GLUEPARQUET"
    AVRO = "AVRO"
    ORC = "ORC"
    XML = "XML"
    TABLEAUHYPER = "TABLEAUHYPER"


class ParameterType:
    """ParameterType enum values."""

    DATETIME = "Datetime"
    NUMBER = "Number"
    STRING = "String"


class SampleMode:
    """SampleMode enum values."""

    FULL_DATASET = "FULL_DATASET"
    CUSTOM_ROWS = "CUSTOM_ROWS"


class SampleType:
    """SampleType enum values."""

    FIRST_N = "FIRST_N"
    LAST_N = "LAST_N"
    RANDOM = "RANDOM"


class SessionStatus:
    """SessionStatus enum values."""

    ASSIGNED = "ASSIGNED"
    FAILED = "FAILED"
    INITIALIZING = "INITIALIZING"
    PROVISIONING = "PROVISIONING"
    READY = "READY"
    RECYCLING = "RECYCLING"
    ROTATING = "ROTATING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"


class Source:
    """Source enum values."""

    S3 = "S3"
    DATA_CATALOG = "DATA-CATALOG"
    DATABASE = "DATABASE"


class ThresholdType:
    """ThresholdType enum values."""

    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"


class ThresholdUnit:
    """ThresholdUnit enum values."""

    COUNT = "COUNT"
    PERCENTAGE = "PERCENTAGE"


class ValidationMode:
    """ValidationMode enum values."""

    CHECK_ALL = "CHECK_ALL"


@dataclass
class Action(PropertyType):
    PARAMETERS = "Parameters"
    OPERATION = "Operation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "operation": "Operation",
    }

    parameters: Optional[RecipeParameters] = None
    operation: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionExpression(PropertyType):
    CONDITION = "Condition"
    VALUE = "Value"
    TARGET_COLUMN = "TargetColumn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "value": "Value",
        "target_column": "TargetColumn",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_column: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class Input(PropertyType):
    S3_INPUT_DEFINITION = "S3InputDefinition"
    DATA_CATALOG_INPUT_DEFINITION = "DataCatalogInputDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_input_definition": "S3InputDefinition",
        "data_catalog_input_definition": "DataCatalogInputDefinition",
    }

    s3_input_definition: Optional[S3Location] = None
    data_catalog_input_definition: Optional[DataCatalogInputDefinition] = None


@dataclass
class RecipeParameters(PropertyType):
    IGNORE_CASE = "IgnoreCase"
    PATTERN_OPTIONS = "PatternOptions"
    COUNT = "Count"
    ORDER_BY_COLUMN = "OrderByColumn"
    UPPER_BOUND = "UpperBound"
    JOIN_KEYS = "JoinKeys"
    REMOVE_LEADING_AND_TRAILING_PUNCTUATION = "RemoveLeadingAndTrailingPunctuation"
    STEP_INDEX = "StepIndex"
    GROUP_BY_AGG_FUNCTION_OPTIONS = "GroupByAggFunctionOptions"
    POSITION = "Position"
    STOP_WORDS_MODE = "StopWordsMode"
    SOURCE_COLUMN = "SourceColumn"
    CUSTOM_CHARACTERS = "CustomCharacters"
    TIME_ZONE = "TimeZone"
    REMOVE_LEADING_AND_TRAILING_QUOTES = "RemoveLeadingAndTrailingQuotes"
    SOURCE_COLUMN2 = "SourceColumn2"
    COLLAPSE_CONSECUTIVE_WHITESPACE = "CollapseConsecutiveWhitespace"
    NUM_ROWS_AFTER = "NumRowsAfter"
    REMOVE_LETTERS = "RemoveLetters"
    SOURCE_COLUMN1 = "SourceColumn1"
    USE_NEW_DATA_FRAME = "UseNewDataFrame"
    INTERVAL = "Interval"
    LOWER_BOUND = "LowerBound"
    TOKENIZER_PATTERN = "TokenizerPattern"
    LEFT_COLUMNS = "LeftColumns"
    CHARS_TO_REMOVE = "CharsToRemove"
    VALUE1 = "Value1"
    DELETE_OTHER_ROWS = "DeleteOtherRows"
    VALUE2 = "Value2"
    CATEGORY_MAP = "CategoryMap"
    START_PATTERN = "StartPattern"
    START_POSITION = "StartPosition"
    SHEET_INDEXES = "SheetIndexes"
    TARGET_INDEX = "TargetIndex"
    REMOVE_SOURCE_COLUMN = "RemoveSourceColumn"
    DATE_TIME_PARAMETERS = "DateTimeParameters"
    END_VALUE = "EndValue"
    REMOVE_CUSTOM_CHARACTERS = "RemoveCustomCharacters"
    END_POSITION = "EndPosition"
    PATTERN = "Pattern"
    DELIMITER = "Delimiter"
    REMOVE_SPECIAL_CHARACTERS = "RemoveSpecialCharacters"
    REMOVE_ALL_QUOTES = "RemoveAllQuotes"
    END_PATTERN = "EndPattern"
    START_COLUMN_INDEX = "StartColumnIndex"
    MODE_TYPE = "ModeType"
    SECONDARY_INPUTS = "SecondaryInputs"
    SAMPLE_TYPE = "SampleType"
    DATE_TIME_FORMAT = "DateTimeFormat"
    OTHER = "Other"
    CASE_STATEMENT = "CaseStatement"
    FALSE_STRING = "FalseString"
    REMOVE_ALL_PUNCTUATION = "RemoveAllPunctuation"
    CUSTOM_STOP_WORDS = "CustomStopWords"
    MAP_TYPE = "MapType"
    COLUMN_RANGE = "ColumnRange"
    CUSTOM_VALUE = "CustomValue"
    INPUT = "Input"
    STEP_COUNT = "StepCount"
    TARGET_DATE_FORMAT = "TargetDateFormat"
    SECOND_INPUT = "SecondInput"
    GROUP_BY_COLUMNS = "GroupByColumns"
    NUM_ROWS_BEFORE = "NumRowsBefore"
    IS_TEXT = "IsText"
    TARGET_COLUMN = "TargetColumn"
    REMOVE_NUMBERS = "RemoveNumbers"
    PERIOD = "Period"
    NUM_ROWS = "NumRows"
    RIGHT_COLUMNS = "RightColumns"
    STEMMING_MODE = "StemmingMode"
    UNITS = "Units"
    SAMPLE_SIZE = "SampleSize"
    INCLUDE_IN_SPLIT = "IncludeInSplit"
    AGGREGATE_FUNCTION = "AggregateFunction"
    VALUE = "Value"
    EXPONENT = "Exponent"
    START_VALUE = "StartValue"
    PATTERN_OPTION2 = "PatternOption2"
    REMOVE_CUSTOM_VALUE = "RemoveCustomValue"
    PATTERN_OPTION1 = "PatternOption1"
    MULTI_LINE = "MultiLine"
    TRUE_STRING = "TrueString"
    REMOVE_LEADING_AND_TRAILING_WHITESPACE = "RemoveLeadingAndTrailingWhitespace"
    HIDDEN_COLUMNS = "HiddenColumns"
    REMOVE_ALL_WHITESPACE = "RemoveAllWhitespace"
    VIEW_FRAME = "ViewFrame"
    COLUMN_DATA_TYPE = "ColumnDataType"
    JOIN_TYPE = "JoinType"
    BASE = "Base"
    VALUE_COLUMN = "ValueColumn"
    DATASETS_COLUMNS = "DatasetsColumns"
    UDF_LANG = "UdfLang"
    TARGET_COLUMN_NAMES = "TargetColumnNames"
    DATE_ADD_VALUE = "DateAddValue"
    EXPAND_CONTRACTIONS = "ExpandContractions"
    UNPIVOT_COLUMN = "UnpivotColumn"
    STRATEGY = "Strategy"
    SHEET_NAMES = "SheetNames"
    LIMIT = "Limit"
    ORDER_BY_COLUMNS = "OrderByColumns"
    SOURCE_COLUMNS = "SourceColumns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ignore_case": "IgnoreCase",
        "pattern_options": "PatternOptions",
        "count": "Count",
        "order_by_column": "OrderByColumn",
        "upper_bound": "UpperBound",
        "join_keys": "JoinKeys",
        "remove_leading_and_trailing_punctuation": "RemoveLeadingAndTrailingPunctuation",
        "step_index": "StepIndex",
        "group_by_agg_function_options": "GroupByAggFunctionOptions",
        "position": "Position",
        "stop_words_mode": "StopWordsMode",
        "source_column": "SourceColumn",
        "custom_characters": "CustomCharacters",
        "time_zone": "TimeZone",
        "remove_leading_and_trailing_quotes": "RemoveLeadingAndTrailingQuotes",
        "source_column2": "SourceColumn2",
        "collapse_consecutive_whitespace": "CollapseConsecutiveWhitespace",
        "num_rows_after": "NumRowsAfter",
        "remove_letters": "RemoveLetters",
        "source_column1": "SourceColumn1",
        "use_new_data_frame": "UseNewDataFrame",
        "interval": "Interval",
        "lower_bound": "LowerBound",
        "tokenizer_pattern": "TokenizerPattern",
        "left_columns": "LeftColumns",
        "chars_to_remove": "CharsToRemove",
        "value1": "Value1",
        "delete_other_rows": "DeleteOtherRows",
        "value2": "Value2",
        "category_map": "CategoryMap",
        "start_pattern": "StartPattern",
        "start_position": "StartPosition",
        "sheet_indexes": "SheetIndexes",
        "target_index": "TargetIndex",
        "remove_source_column": "RemoveSourceColumn",
        "date_time_parameters": "DateTimeParameters",
        "end_value": "EndValue",
        "remove_custom_characters": "RemoveCustomCharacters",
        "end_position": "EndPosition",
        "pattern": "Pattern",
        "delimiter": "Delimiter",
        "remove_special_characters": "RemoveSpecialCharacters",
        "remove_all_quotes": "RemoveAllQuotes",
        "end_pattern": "EndPattern",
        "start_column_index": "StartColumnIndex",
        "mode_type": "ModeType",
        "secondary_inputs": "SecondaryInputs",
        "sample_type": "SampleType",
        "date_time_format": "DateTimeFormat",
        "other": "Other",
        "case_statement": "CaseStatement",
        "false_string": "FalseString",
        "remove_all_punctuation": "RemoveAllPunctuation",
        "custom_stop_words": "CustomStopWords",
        "map_type": "MapType",
        "column_range": "ColumnRange",
        "custom_value": "CustomValue",
        "input": "Input",
        "step_count": "StepCount",
        "target_date_format": "TargetDateFormat",
        "second_input": "SecondInput",
        "group_by_columns": "GroupByColumns",
        "num_rows_before": "NumRowsBefore",
        "is_text": "IsText",
        "target_column": "TargetColumn",
        "remove_numbers": "RemoveNumbers",
        "period": "Period",
        "num_rows": "NumRows",
        "right_columns": "RightColumns",
        "stemming_mode": "StemmingMode",
        "units": "Units",
        "sample_size": "SampleSize",
        "include_in_split": "IncludeInSplit",
        "aggregate_function": "AggregateFunction",
        "value": "Value",
        "exponent": "Exponent",
        "start_value": "StartValue",
        "pattern_option2": "PatternOption2",
        "remove_custom_value": "RemoveCustomValue",
        "pattern_option1": "PatternOption1",
        "multi_line": "MultiLine",
        "true_string": "TrueString",
        "remove_leading_and_trailing_whitespace": "RemoveLeadingAndTrailingWhitespace",
        "hidden_columns": "HiddenColumns",
        "remove_all_whitespace": "RemoveAllWhitespace",
        "view_frame": "ViewFrame",
        "column_data_type": "ColumnDataType",
        "join_type": "JoinType",
        "base": "Base",
        "value_column": "ValueColumn",
        "datasets_columns": "DatasetsColumns",
        "udf_lang": "UdfLang",
        "target_column_names": "TargetColumnNames",
        "date_add_value": "DateAddValue",
        "expand_contractions": "ExpandContractions",
        "unpivot_column": "UnpivotColumn",
        "strategy": "Strategy",
        "sheet_names": "SheetNames",
        "limit": "Limit",
        "order_by_columns": "OrderByColumns",
        "source_columns": "SourceColumns",
    }

    ignore_case: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_options: Optional[Union[str, Ref, GetAtt, Sub]] = None
    count: Optional[Union[str, Ref, GetAtt, Sub]] = None
    order_by_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    upper_bound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    join_keys: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_leading_and_trailing_punctuation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    step_index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_by_agg_function_options: Optional[Union[str, Ref, GetAtt, Sub]] = None
    position: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stop_words_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_characters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_leading_and_trailing_quotes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    collapse_consecutive_whitespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    num_rows_after: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_letters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_new_data_frame: Optional[Union[str, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lower_bound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tokenizer_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    left_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chars_to_remove: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delete_other_rows: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category_map: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_position: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sheet_indexes: Optional[Union[list[int], Ref]] = None
    target_index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_source_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    date_time_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_custom_characters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_position: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_special_characters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_all_quotes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_column_index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mode_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_inputs: Optional[list[SecondaryInput]] = None
    sample_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    date_time_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    other: Optional[Union[str, Ref, GetAtt, Sub]] = None
    case_statement: Optional[Union[str, Ref, GetAtt, Sub]] = None
    false_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_all_punctuation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_stop_words: Optional[Union[str, Ref, GetAtt, Sub]] = None
    map_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input: Optional[Input] = None
    step_count: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_date_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    second_input: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_by_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    num_rows_before: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_numbers: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[str, Ref, GetAtt, Sub]] = None
    num_rows: Optional[Union[str, Ref, GetAtt, Sub]] = None
    right_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stemming_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sample_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_in_split: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aggregate_function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exponent: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_option2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_custom_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_option1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multi_line: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    true_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_leading_and_trailing_whitespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hidden_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_all_whitespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    view_frame: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    join_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    datasets_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    udf_lang: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_column_names: Optional[Union[str, Ref, GetAtt, Sub]] = None
    date_add_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expand_contractions: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unpivot_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sheet_names: Optional[Union[list[str], Ref]] = None
    limit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    order_by_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_columns: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecipeStep(PropertyType):
    ACTION = "Action"
    CONDITION_EXPRESSIONS = "ConditionExpressions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "condition_expressions": "ConditionExpressions",
    }

    action: Optional[Action] = None
    condition_expressions: Optional[list[ConditionExpression]] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecondaryInput(PropertyType):
    S3_INPUT_DEFINITION = "S3InputDefinition"
    DATA_CATALOG_INPUT_DEFINITION = "DataCatalogInputDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_input_definition": "S3InputDefinition",
        "data_catalog_input_definition": "DataCatalogInputDefinition",
    }

    s3_input_definition: Optional[S3Location] = None
    data_catalog_input_definition: Optional[DataCatalogInputDefinition] = None

