"""PropertyTypes for AWS::CloudWatch::AnomalyDetector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_time_zone": "MetricTimeZone",
        "excluded_time_ranges": "ExcludedTimeRanges",
    }

    metric_time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    excluded_time_ranges: Optional[list[Range]] = None


@dataclass
class Dimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Metric(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "periodic_spikes": "PeriodicSpikes",
    }

    periodic_spikes: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDataQueries(PropertyType):
    pass


@dataclass
class MetricDataQuery(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class MetricStat(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleMetricAnomalyDetector(PropertyType):
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

