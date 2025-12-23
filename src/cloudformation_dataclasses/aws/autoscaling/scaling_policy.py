"""PropertyTypes for AWS::AutoScaling::ScalingPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomizedMetricSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "metrics": "Metrics",
        "statistic": "Statistic",
        "dimensions": "Dimensions",
        "period": "Period",
        "unit": "Unit",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metrics: Optional[list[TargetTrackingMetricDataQuery]] = None
    statistic: Optional[Union[str, MetricStatistic, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[MetricDimension]] = None
    period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Metric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "dimensions": "Dimensions",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[MetricDimension]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDataQuery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "return_data": "ReturnData",
        "expression": "Expression",
        "label": "Label",
        "metric_stat": "MetricStat",
        "id": "Id",
    }

    return_data: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_stat: Optional[MetricStat] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricStat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stat": "Stat",
        "metric": "Metric",
        "unit": "Unit",
    }

    stat: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric: Optional[Metric] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredefinedMetricSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, MetricType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_capacity_breach_behavior": "MaxCapacityBreachBehavior",
        "max_capacity_buffer": "MaxCapacityBuffer",
        "mode": "Mode",
        "metric_specifications": "MetricSpecifications",
        "scheduling_buffer_time": "SchedulingBufferTime",
    }

    max_capacity_breach_behavior: Optional[Union[str, PredictiveScalingMaxCapacityBreachBehavior, Ref, GetAtt, Sub]] = None
    max_capacity_buffer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, PredictiveScalingMode, Ref, GetAtt, Sub]] = None
    metric_specifications: Optional[list[PredictiveScalingMetricSpecification]] = None
    scheduling_buffer_time: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingCustomizedCapacityMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class PredictiveScalingCustomizedLoadMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class PredictiveScalingCustomizedScalingMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class PredictiveScalingMetricSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "customized_load_metric_specification": "CustomizedLoadMetricSpecification",
        "predefined_load_metric_specification": "PredefinedLoadMetricSpecification",
        "target_value": "TargetValue",
        "predefined_scaling_metric_specification": "PredefinedScalingMetricSpecification",
        "customized_capacity_metric_specification": "CustomizedCapacityMetricSpecification",
        "customized_scaling_metric_specification": "CustomizedScalingMetricSpecification",
        "predefined_metric_pair_specification": "PredefinedMetricPairSpecification",
    }

    customized_load_metric_specification: Optional[PredictiveScalingCustomizedLoadMetric] = None
    predefined_load_metric_specification: Optional[PredictiveScalingPredefinedLoadMetric] = None
    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    predefined_scaling_metric_specification: Optional[PredictiveScalingPredefinedScalingMetric] = None
    customized_capacity_metric_specification: Optional[PredictiveScalingCustomizedCapacityMetric] = None
    customized_scaling_metric_specification: Optional[PredictiveScalingCustomizedScalingMetric] = None
    predefined_metric_pair_specification: Optional[PredictiveScalingPredefinedMetricPair] = None


@dataclass
class PredictiveScalingPredefinedLoadMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, PredefinedLoadMetricType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedMetricPair(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, PredefinedMetricPairType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedScalingMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, PredefinedScalingMetricType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StepAdjustment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_interval_upper_bound": "MetricIntervalUpperBound",
        "metric_interval_lower_bound": "MetricIntervalLowerBound",
        "scaling_adjustment": "ScalingAdjustment",
    }

    metric_interval_upper_bound: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metric_interval_lower_bound: Optional[Union[float, Ref, GetAtt, Sub]] = None
    scaling_adjustment: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
        "customized_metric_specification": "CustomizedMetricSpecification",
        "disable_scale_in": "DisableScaleIn",
        "predefined_metric_specification": "PredefinedMetricSpecification",
    }

    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    customized_metric_specification: Optional[CustomizedMetricSpecification] = None
    disable_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    predefined_metric_specification: Optional[PredefinedMetricSpecification] = None


@dataclass
class TargetTrackingMetricDataQuery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "return_data": "ReturnData",
        "expression": "Expression",
        "label": "Label",
        "metric_stat": "MetricStat",
        "period": "Period",
        "id": "Id",
    }

    return_data: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_stat: Optional[TargetTrackingMetricStat] = None
    period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingMetricStat(PropertyType):
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

