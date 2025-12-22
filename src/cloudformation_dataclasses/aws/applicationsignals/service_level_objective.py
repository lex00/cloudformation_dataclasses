"""PropertyTypes for AWS::ApplicationSignals::ServiceLevelObjective."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BurnRateConfiguration(PropertyType):
    LOOK_BACK_WINDOW_MINUTES = "LookBackWindowMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "look_back_window_minutes": "LookBackWindowMinutes",
    }

    look_back_window_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CalendarInterval(PropertyType):
    DURATION_UNIT = "DurationUnit"
    START_TIME = "StartTime"
    DURATION = "Duration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_unit": "DurationUnit",
        "start_time": "StartTime",
        "duration": "Duration",
    }

    duration_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[int, Ref, GetAtt, Sub]] = None
    duration: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DependencyConfig(PropertyType):
    DEPENDENCY_KEY_ATTRIBUTES = "DependencyKeyAttributes"
    DEPENDENCY_OPERATION_NAME = "DependencyOperationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dependency_key_attributes": "DependencyKeyAttributes",
        "dependency_operation_name": "DependencyOperationName",
    }

    dependency_key_attributes: Optional[dict[str, str]] = None
    dependency_operation_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class ExclusionWindow(PropertyType):
    WINDOW = "Window"
    RECURRENCE_RULE = "RecurrenceRule"
    START_TIME = "StartTime"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "window": "Window",
        "recurrence_rule": "RecurrenceRule",
        "start_time": "StartTime",
        "reason": "Reason",
    }

    window: Optional[Window] = None
    recurrence_rule: Optional[RecurrenceRule] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Goal(PropertyType):
    WARNING_THRESHOLD = "WarningThreshold"
    ATTAINMENT_GOAL = "AttainmentGoal"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "warning_threshold": "WarningThreshold",
        "attainment_goal": "AttainmentGoal",
        "interval": "Interval",
    }

    warning_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    attainment_goal: Optional[Union[float, Ref, GetAtt, Sub]] = None
    interval: Optional[Interval] = None


@dataclass
class Interval(PropertyType):
    ROLLING_INTERVAL = "RollingInterval"
    CALENDAR_INTERVAL = "CalendarInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rolling_interval": "RollingInterval",
        "calendar_interval": "CalendarInterval",
    }

    rolling_interval: Optional[RollingInterval] = None
    calendar_interval: Optional[CalendarInterval] = None


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
class MetricDataQuery(PropertyType):
    ACCOUNT_ID = "AccountId"
    RETURN_DATA = "ReturnData"
    EXPRESSION = "Expression"
    METRIC_STAT = "MetricStat"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_id": "AccountId",
        "return_data": "ReturnData",
        "expression": "Expression",
        "metric_stat": "MetricStat",
        "id": "Id",
    }

    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    return_data: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_stat: Optional[MetricStat] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoredRequestCountMetric(PropertyType):
    GOOD_COUNT_METRIC = "GoodCountMetric"
    BAD_COUNT_METRIC = "BadCountMetric"

    _property_mappings: ClassVar[dict[str, str]] = {
        "good_count_metric": "GoodCountMetric",
        "bad_count_metric": "BadCountMetric",
    }

    good_count_metric: Optional[list[MetricDataQuery]] = None
    bad_count_metric: Optional[list[MetricDataQuery]] = None


@dataclass
class RecurrenceRule(PropertyType):
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RequestBasedSli(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    REQUEST_BASED_SLI_METRIC = "RequestBasedSliMetric"
    METRIC_THRESHOLD = "MetricThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "request_based_sli_metric": "RequestBasedSliMetric",
        "metric_threshold": "MetricThreshold",
    }

    comparison_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    request_based_sli_metric: Optional[RequestBasedSliMetric] = None
    metric_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class RequestBasedSliMetric(PropertyType):
    MONITORED_REQUEST_COUNT_METRIC = "MonitoredRequestCountMetric"
    OPERATION_NAME = "OperationName"
    TOTAL_REQUEST_COUNT_METRIC = "TotalRequestCountMetric"
    KEY_ATTRIBUTES = "KeyAttributes"
    METRIC_TYPE = "MetricType"
    DEPENDENCY_CONFIG = "DependencyConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "monitored_request_count_metric": "MonitoredRequestCountMetric",
        "operation_name": "OperationName",
        "total_request_count_metric": "TotalRequestCountMetric",
        "key_attributes": "KeyAttributes",
        "metric_type": "MetricType",
        "dependency_config": "DependencyConfig",
    }

    monitored_request_count_metric: Optional[MonitoredRequestCountMetric] = None
    operation_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    total_request_count_metric: Optional[list[MetricDataQuery]] = None
    key_attributes: Optional[dict[str, str]] = None
    metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dependency_config: Optional[DependencyConfig] = None


@dataclass
class RollingInterval(PropertyType):
    DURATION_UNIT = "DurationUnit"
    DURATION = "Duration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_unit": "DurationUnit",
        "duration": "Duration",
    }

    duration_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    duration: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Sli(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    SLI_METRIC = "SliMetric"
    METRIC_THRESHOLD = "MetricThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "sli_metric": "SliMetric",
        "metric_threshold": "MetricThreshold",
    }

    comparison_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sli_metric: Optional[SliMetric] = None
    metric_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class SliMetric(PropertyType):
    STATISTIC = "Statistic"
    OPERATION_NAME = "OperationName"
    KEY_ATTRIBUTES = "KeyAttributes"
    METRIC_TYPE = "MetricType"
    PERIOD_SECONDS = "PeriodSeconds"
    METRIC_DATA_QUERIES = "MetricDataQueries"
    DEPENDENCY_CONFIG = "DependencyConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statistic": "Statistic",
        "operation_name": "OperationName",
        "key_attributes": "KeyAttributes",
        "metric_type": "MetricType",
        "period_seconds": "PeriodSeconds",
        "metric_data_queries": "MetricDataQueries",
        "dependency_config": "DependencyConfig",
    }

    statistic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    operation_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_attributes: Optional[dict[str, str]] = None
    metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    metric_data_queries: Optional[list[MetricDataQuery]] = None
    dependency_config: Optional[DependencyConfig] = None


@dataclass
class Window(PropertyType):
    DURATION_UNIT = "DurationUnit"
    DURATION = "Duration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_unit": "DurationUnit",
        "duration": "Duration",
    }

    duration_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    duration: Optional[Union[int, Ref, GetAtt, Sub]] = None

