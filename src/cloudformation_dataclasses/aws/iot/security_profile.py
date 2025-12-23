"""PropertyTypes for AWS::IoT::SecurityProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AlertTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alert_target_arn": "AlertTargetArn",
        "role_arn": "RoleArn",
    }

    alert_target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Behavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "export_metric": "ExportMetric",
        "suppress_alerts": "SuppressAlerts",
        "metric": "Metric",
        "criteria": "Criteria",
        "metric_dimension": "MetricDimension",
        "name": "Name",
    }

    export_metric: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    suppress_alerts: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    metric: Optional[Union[str, Ref, GetAtt, Sub]] = None
    criteria: Optional[BehaviorCriteria] = None
    metric_dimension: Optional[MetricDimension] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BehaviorCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "ml_detection_config": "MlDetectionConfig",
        "value": "Value",
        "statistical_threshold": "StatisticalThreshold",
        "duration_seconds": "DurationSeconds",
        "consecutive_datapoints_to_alarm": "ConsecutiveDatapointsToAlarm",
        "consecutive_datapoints_to_clear": "ConsecutiveDatapointsToClear",
    }

    comparison_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ml_detection_config: Optional[MachineLearningDetectionConfig] = None
    value: Optional[MetricValue] = None
    statistical_threshold: Optional[StatisticalThreshold] = None
    duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    consecutive_datapoints_to_alarm: Optional[Union[int, Ref, GetAtt, Sub]] = None
    consecutive_datapoints_to_clear: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MachineLearningDetectionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "confidence_level": "ConfidenceLevel",
    }

    confidence_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "dimension_name": "DimensionName",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricToRetain(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "export_metric": "ExportMetric",
        "metric": "Metric",
        "metric_dimension": "MetricDimension",
    }

    export_metric: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    metric: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_dimension: Optional[MetricDimension] = None


@dataclass
class MetricValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "numbers": "Numbers",
        "number": "Number",
        "ports": "Ports",
        "count": "Count",
        "strings": "Strings",
        "cidrs": "Cidrs",
    }

    numbers: Optional[Union[list[float], Ref]] = None
    number: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ports: Optional[Union[list[int], Ref]] = None
    count: Optional[Union[str, Ref, GetAtt, Sub]] = None
    strings: Optional[Union[list[str], Ref]] = None
    cidrs: Optional[Union[list[str], Ref]] = None


@dataclass
class MetricsExportConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mqtt_topic": "MqttTopic",
        "role_arn": "RoleArn",
    }

    mqtt_topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StatisticalThreshold(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "statistic": "Statistic",
    }

    statistic: Optional[Union[str, Ref, GetAtt, Sub]] = None

