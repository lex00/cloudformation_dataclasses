"""PropertyTypes for AWS::DataBrew::Project."""

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
class Sample(PropertyType):
    TYPE = "Type"
    SIZE = "Size"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "size": "Size",
    }

    type_: Optional[Union[str, SampleType, Ref, GetAtt, Sub]] = None
    size: Optional[Union[int, Ref, GetAtt, Sub]] = None

