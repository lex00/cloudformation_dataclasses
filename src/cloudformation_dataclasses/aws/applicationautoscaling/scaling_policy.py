"""PropertyTypes for AWS::ApplicationAutoScaling::ScalingPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomizedMetricSpecification(PropertyType):
    METRIC_NAME = "MetricName"
    METRICS = "Metrics"
    STATISTIC = "Statistic"
    DIMENSIONS = "Dimensions"
    UNIT = "Unit"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "metrics": "Metrics",
        "statistic": "Statistic",
        "dimensions": "Dimensions",
        "unit": "Unit",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metrics: Optional[list[TargetTrackingMetricDataQuery]] = None
    statistic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[MetricDimension]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDimension(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredefinedMetricSpecification(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingCustomizedCapacityMetric(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[PredictiveScalingMetricDataQuery]] = None


@dataclass
class PredictiveScalingCustomizedLoadMetric(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[PredictiveScalingMetricDataQuery]] = None


@dataclass
class PredictiveScalingCustomizedScalingMetric(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[PredictiveScalingMetricDataQuery]] = None


@dataclass
class PredictiveScalingMetric(PropertyType):
    METRIC_NAME = "MetricName"
    DIMENSIONS = "Dimensions"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "dimensions": "Dimensions",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[PredictiveScalingMetricDimension]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingMetricDataQuery(PropertyType):
    RETURN_DATA = "ReturnData"
    EXPRESSION = "Expression"
    LABEL = "Label"
    METRIC_STAT = "MetricStat"
    ID = "Id"

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
    metric_stat: Optional[PredictiveScalingMetricStat] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingMetricDimension(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingMetricSpecification(PropertyType):
    CUSTOMIZED_LOAD_METRIC_SPECIFICATION = "CustomizedLoadMetricSpecification"
    PREDEFINED_LOAD_METRIC_SPECIFICATION = "PredefinedLoadMetricSpecification"
    TARGET_VALUE = "TargetValue"
    PREDEFINED_SCALING_METRIC_SPECIFICATION = "PredefinedScalingMetricSpecification"
    CUSTOMIZED_CAPACITY_METRIC_SPECIFICATION = "CustomizedCapacityMetricSpecification"
    CUSTOMIZED_SCALING_METRIC_SPECIFICATION = "CustomizedScalingMetricSpecification"
    PREDEFINED_METRIC_PAIR_SPECIFICATION = "PredefinedMetricPairSpecification"

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
class PredictiveScalingMetricStat(PropertyType):
    STAT = "Stat"
    METRIC = "Metric"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stat": "Stat",
        "metric": "Metric",
        "unit": "Unit",
    }

    stat: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric: Optional[PredictiveScalingMetric] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPolicyConfiguration(PropertyType):
    MAX_CAPACITY_BREACH_BEHAVIOR = "MaxCapacityBreachBehavior"
    MAX_CAPACITY_BUFFER = "MaxCapacityBuffer"
    MODE = "Mode"
    METRIC_SPECIFICATIONS = "MetricSpecifications"
    SCHEDULING_BUFFER_TIME = "SchedulingBufferTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_capacity_breach_behavior": "MaxCapacityBreachBehavior",
        "max_capacity_buffer": "MaxCapacityBuffer",
        "mode": "Mode",
        "metric_specifications": "MetricSpecifications",
        "scheduling_buffer_time": "SchedulingBufferTime",
    }

    max_capacity_breach_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_capacity_buffer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_specifications: Optional[list[PredictiveScalingMetricSpecification]] = None
    scheduling_buffer_time: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedLoadMetric(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedMetricPair(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedScalingMetric(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StepAdjustment(PropertyType):
    METRIC_INTERVAL_UPPER_BOUND = "MetricIntervalUpperBound"
    METRIC_INTERVAL_LOWER_BOUND = "MetricIntervalLowerBound"
    SCALING_ADJUSTMENT = "ScalingAdjustment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_interval_upper_bound": "MetricIntervalUpperBound",
        "metric_interval_lower_bound": "MetricIntervalLowerBound",
        "scaling_adjustment": "ScalingAdjustment",
    }

    metric_interval_upper_bound: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metric_interval_lower_bound: Optional[Union[float, Ref, GetAtt, Sub]] = None
    scaling_adjustment: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StepScalingPolicyConfiguration(PropertyType):
    METRIC_AGGREGATION_TYPE = "MetricAggregationType"
    COOLDOWN = "Cooldown"
    STEP_ADJUSTMENTS = "StepAdjustments"
    MIN_ADJUSTMENT_MAGNITUDE = "MinAdjustmentMagnitude"
    ADJUSTMENT_TYPE = "AdjustmentType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_aggregation_type": "MetricAggregationType",
        "cooldown": "Cooldown",
        "step_adjustments": "StepAdjustments",
        "min_adjustment_magnitude": "MinAdjustmentMagnitude",
        "adjustment_type": "AdjustmentType",
    }

    metric_aggregation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    step_adjustments: Optional[list[StepAdjustment]] = None
    min_adjustment_magnitude: Optional[Union[int, Ref, GetAtt, Sub]] = None
    adjustment_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingMetric(PropertyType):
    METRIC_NAME = "MetricName"
    DIMENSIONS = "Dimensions"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "dimensions": "Dimensions",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[TargetTrackingMetricDimension]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingMetricDataQuery(PropertyType):
    RETURN_DATA = "ReturnData"
    EXPRESSION = "Expression"
    LABEL = "Label"
    METRIC_STAT = "MetricStat"
    ID = "Id"

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
    metric_stat: Optional[TargetTrackingMetricStat] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingMetricDimension(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingMetricStat(PropertyType):
    STAT = "Stat"
    METRIC = "Metric"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stat": "Stat",
        "metric": "Metric",
        "unit": "Unit",
    }

    stat: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric: Optional[TargetTrackingMetric] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    SCALE_OUT_COOLDOWN = "ScaleOutCooldown"
    TARGET_VALUE = "TargetValue"
    CUSTOMIZED_METRIC_SPECIFICATION = "CustomizedMetricSpecification"
    DISABLE_SCALE_IN = "DisableScaleIn"
    SCALE_IN_COOLDOWN = "ScaleInCooldown"
    PREDEFINED_METRIC_SPECIFICATION = "PredefinedMetricSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_out_cooldown": "ScaleOutCooldown",
        "target_value": "TargetValue",
        "customized_metric_specification": "CustomizedMetricSpecification",
        "disable_scale_in": "DisableScaleIn",
        "scale_in_cooldown": "ScaleInCooldown",
        "predefined_metric_specification": "PredefinedMetricSpecification",
    }

    scale_out_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    customized_metric_specification: Optional[CustomizedMetricSpecification] = None
    disable_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scale_in_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    predefined_metric_specification: Optional[PredefinedMetricSpecification] = None

