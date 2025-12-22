"""PropertyTypes for AWS::DataBrew::Ruleset."""

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
class Rule(PropertyType):
    COLUMN_SELECTORS = "ColumnSelectors"
    DISABLED = "Disabled"
    SUBSTITUTION_MAP = "SubstitutionMap"
    NAME = "Name"
    CHECK_EXPRESSION = "CheckExpression"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_selectors": "ColumnSelectors",
        "disabled": "Disabled",
        "substitution_map": "SubstitutionMap",
        "name": "Name",
        "check_expression": "CheckExpression",
        "threshold": "Threshold",
    }

    column_selectors: Optional[list[ColumnSelector]] = None
    disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    substitution_map: Optional[list[SubstitutionValue]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    check_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold: Optional[Threshold] = None


@dataclass
class SubstitutionValue(PropertyType):
    VALUE = "Value"
    VALUE_REFERENCE = "ValueReference"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "value_reference": "ValueReference",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Threshold(PropertyType):
    TYPE = "Type"
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "unit": "Unit",
    }

    type_: Optional[Union[str, ThresholdType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, ThresholdUnit, Ref, GetAtt, Sub]] = None

