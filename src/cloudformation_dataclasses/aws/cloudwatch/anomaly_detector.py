"""PropertyTypes for AWS::CloudWatch::AnomalyDetector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionsSuppressedBy:
    """ActionsSuppressedBy enum values."""

    WAITPERIOD = "WaitPeriod"
    EXTENSIONPERIOD = "ExtensionPeriod"
    ALARM = "Alarm"


class AlarmType:
    """AlarmType enum values."""

    COMPOSITEALARM = "CompositeAlarm"
    METRICALARM = "MetricAlarm"


class AnomalyDetectorStateValue:
    """AnomalyDetectorStateValue enum values."""

    PENDING_TRAINING = "PENDING_TRAINING"
    TRAINED_INSUFFICIENT_DATA = "TRAINED_INSUFFICIENT_DATA"
    TRAINED = "TRAINED"


class AnomalyDetectorType:
    """AnomalyDetectorType enum values."""

    SINGLE_METRIC = "SINGLE_METRIC"
    METRIC_MATH = "METRIC_MATH"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"
    LESSTHANLOWERORGREATERTHANUPPERTHRESHOLD = "LessThanLowerOrGreaterThanUpperThreshold"
    LESSTHANLOWERTHRESHOLD = "LessThanLowerThreshold"
    GREATERTHANUPPERTHRESHOLD = "GreaterThanUpperThreshold"


class EvaluationState:
    """EvaluationState enum values."""

    PARTIAL_DATA = "PARTIAL_DATA"


class HistoryItemType:
    """HistoryItemType enum values."""

    CONFIGURATIONUPDATE = "ConfigurationUpdate"
    STATEUPDATE = "StateUpdate"
    ACTION = "Action"
    ALARMCONTRIBUTORSTATEUPDATE = "AlarmContributorStateUpdate"
    ALARMCONTRIBUTORACTION = "AlarmContributorAction"


class MetricStreamOutputFormat:
    """MetricStreamOutputFormat enum values."""

    JSON = "json"
    OPENTELEMETRY0_7 = "opentelemetry0.7"
    OPENTELEMETRY1_0 = "opentelemetry1.0"


class RecentlyActive:
    """RecentlyActive enum values."""

    PT3H = "PT3H"


class ScanBy:
    """ScanBy enum values."""

    TIMESTAMPDESCENDING = "TimestampDescending"
    TIMESTAMPASCENDING = "TimestampAscending"


class StandardUnit:
    """StandardUnit enum values."""

    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


class StateValue:
    """StateValue enum values."""

    OK = "OK"
    ALARM = "ALARM"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class Statistic:
    """Statistic enum values."""

    SAMPLECOUNT = "SampleCount"
    AVERAGE = "Average"
    SUM = "Sum"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"


class StatusCode:
    """StatusCode enum values."""

    COMPLETE = "Complete"
    INTERNALERROR = "InternalError"
    PARTIALDATA = "PartialData"
    FORBIDDEN = "Forbidden"


@dataclass
class Configuration(PropertyType):
    METRIC_TIME_ZONE = "MetricTimeZone"
    EXCLUDED_TIME_RANGES = "ExcludedTimeRanges"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_time_zone": "MetricTimeZone",
        "excluded_time_ranges": "ExcludedTimeRanges",
    }

    metric_time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    excluded_time_ranges: Optional[list[Range]] = None


@dataclass
class Dimension(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Metric(PropertyType):
    METRIC_NAME = "MetricName"
    DIMENSIONS = "Dimensions"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "dimensions": "Dimensions",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[Dimension]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricCharacteristics(PropertyType):
    PERIODIC_SPIKES = "PeriodicSpikes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "periodic_spikes": "PeriodicSpikes",
    }

    periodic_spikes: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDataQueries(PropertyType):
    pass


@dataclass
class MetricDataQuery(PropertyType):
    ACCOUNT_ID = "AccountId"
    RETURN_DATA = "ReturnData"
    EXPRESSION = "Expression"
    METRIC_STAT = "MetricStat"
    LABEL = "Label"
    PERIOD = "Period"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_id": "AccountId",
        "return_data": "ReturnData",
        "expression": "Expression",
        "metric_stat": "MetricStat",
        "label": "Label",
        "period": "Period",
        "id": "Id",
    }

    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    return_data: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_stat: Optional[MetricStat] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricMathAnomalyDetector(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class MetricStat(PropertyType):
    STAT = "Stat"
    PERIOD = "Period"
    METRIC = "Metric"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stat": "Stat",
        "period": "Period",
        "metric": "Metric",
        "unit": "Unit",
    }

    stat: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    metric: Optional[Metric] = None
    unit: Optional[Union[str, StandardUnit, Ref, GetAtt, Sub]] = None


@dataclass
class Range(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleMetricAnomalyDetector(PropertyType):
    METRIC_NAME = "MetricName"
    ACCOUNT_ID = "AccountId"
    STAT = "Stat"
    DIMENSIONS = "Dimensions"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "account_id": "AccountId",
        "stat": "Stat",
        "dimensions": "Dimensions",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stat: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[Dimension]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None

