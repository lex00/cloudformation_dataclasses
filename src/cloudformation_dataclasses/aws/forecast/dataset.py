"""PropertyTypes for AWS::Forecast::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AttributeType:
    """AttributeType enum values."""

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    TIMESTAMP = "timestamp"
    GEOLOCATION = "geolocation"


class AutoMLOverrideStrategy:
    """AutoMLOverrideStrategy enum values."""

    LATENCYOPTIMIZED = "LatencyOptimized"
    ACCURACYOPTIMIZED = "AccuracyOptimized"


class Condition:
    """Condition enum values."""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


class DatasetType:
    """DatasetType enum values."""

    TARGET_TIME_SERIES = "TARGET_TIME_SERIES"
    RELATED_TIME_SERIES = "RELATED_TIME_SERIES"
    ITEM_METADATA = "ITEM_METADATA"


class DayOfWeek:
    """DayOfWeek enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class Domain:
    """Domain enum values."""

    RETAIL = "RETAIL"
    CUSTOM = "CUSTOM"
    INVENTORY_PLANNING = "INVENTORY_PLANNING"
    EC2_CAPACITY = "EC2_CAPACITY"
    WORK_FORCE = "WORK_FORCE"
    WEB_TRAFFIC = "WEB_TRAFFIC"
    METRICS = "METRICS"


class EvaluationType:
    """EvaluationType enum values."""

    SUMMARY = "SUMMARY"
    COMPUTED = "COMPUTED"


class FeaturizationMethodName:
    """FeaturizationMethodName enum values."""

    FILLING = "filling"


class FilterConditionString:
    """FilterConditionString enum values."""

    IS = "IS"
    IS_NOT = "IS_NOT"


class ImportMode:
    """ImportMode enum values."""

    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"


class Month:
    """Month enum values."""

    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"


class Operation:
    """Operation enum values."""

    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"


class OptimizationMetric:
    """OptimizationMetric enum values."""

    WAPE = "WAPE"
    RMSE = "RMSE"
    AVERAGEWEIGHTEDQUANTILELOSS = "AverageWeightedQuantileLoss"
    MASE = "MASE"
    MAPE = "MAPE"


class ScalingType:
    """ScalingType enum values."""

    AUTO = "Auto"
    LINEAR = "Linear"
    LOGARITHMIC = "Logarithmic"
    REVERSELOGARITHMIC = "ReverseLogarithmic"


class State:
    """State enum values."""

    ACTIVE = "Active"
    DELETED = "Deleted"


class TimePointGranularity:
    """TimePointGranularity enum values."""

    ALL = "ALL"
    SPECIFIC = "SPECIFIC"


class TimeSeriesGranularity:
    """TimeSeriesGranularity enum values."""

    ALL = "ALL"
    SPECIFIC = "SPECIFIC"


@dataclass
class AttributesItems(PropertyType):
    ATTRIBUTE_TYPE = "AttributeType"
    ATTRIBUTE_NAME = "AttributeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_type": "AttributeType",
        "attribute_name": "AttributeName",
    }

    attribute_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfig(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "role_arn": "RoleArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schema(PropertyType):
    ATTRIBUTES = "Attributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes": "Attributes",
    }

    attributes: Optional[list[AttributesItems]] = None


@dataclass
class TagsItems(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

