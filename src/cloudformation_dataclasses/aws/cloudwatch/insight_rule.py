"""PropertyTypes for AWS::CloudWatch::InsightRule."""

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
class Tags(PropertyType):
    pass

