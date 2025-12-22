"""PropertyTypes for AWS::AutoScalingPlans::ScalingPlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationSource(PropertyType):
    CLOUD_FORMATION_STACK_ARN = "CloudFormationStackARN"
    TAG_FILTERS = "TagFilters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_formation_stack_arn": "CloudFormationStackARN",
        "tag_filters": "TagFilters",
    }

    cloud_formation_stack_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_filters: Optional[list[TagFilter]] = None


@dataclass
class CustomizedLoadMetricSpecification(PropertyType):
    METRIC_NAME = "MetricName"
    STATISTIC = "Statistic"
    DIMENSIONS = "Dimensions"
    UNIT = "Unit"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "statistic": "Statistic",
        "dimensions": "Dimensions",
        "unit": "Unit",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    statistic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[MetricDimension]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomizedScalingMetricSpecification(PropertyType):
    METRIC_NAME = "MetricName"
    STATISTIC = "Statistic"
    DIMENSIONS = "Dimensions"
    UNIT = "Unit"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "statistic": "Statistic",
        "dimensions": "Dimensions",
        "unit": "Unit",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
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
class PredefinedLoadMetricSpecification(PropertyType):
    PREDEFINED_LOAD_METRIC_TYPE = "PredefinedLoadMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_load_metric_type": "PredefinedLoadMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_load_metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredefinedScalingMetricSpecification(PropertyType):
    RESOURCE_LABEL = "ResourceLabel"
    PREDEFINED_SCALING_METRIC_TYPE = "PredefinedScalingMetricType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_label": "ResourceLabel",
        "predefined_scaling_metric_type": "PredefinedScalingMetricType",
    }

    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    predefined_scaling_metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingInstruction(PropertyType):
    DISABLE_DYNAMIC_SCALING = "DisableDynamicScaling"
    SERVICE_NAMESPACE = "ServiceNamespace"
    PREDICTIVE_SCALING_MAX_CAPACITY_BEHAVIOR = "PredictiveScalingMaxCapacityBehavior"
    SCALABLE_DIMENSION = "ScalableDimension"
    SCALING_POLICY_UPDATE_BEHAVIOR = "ScalingPolicyUpdateBehavior"
    MIN_CAPACITY = "MinCapacity"
    TARGET_TRACKING_CONFIGURATIONS = "TargetTrackingConfigurations"
    PREDICTIVE_SCALING_MAX_CAPACITY_BUFFER = "PredictiveScalingMaxCapacityBuffer"
    CUSTOMIZED_LOAD_METRIC_SPECIFICATION = "CustomizedLoadMetricSpecification"
    PREDEFINED_LOAD_METRIC_SPECIFICATION = "PredefinedLoadMetricSpecification"
    RESOURCE_ID = "ResourceId"
    SCHEDULED_ACTION_BUFFER_TIME = "ScheduledActionBufferTime"
    MAX_CAPACITY = "MaxCapacity"
    PREDICTIVE_SCALING_MODE = "PredictiveScalingMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disable_dynamic_scaling": "DisableDynamicScaling",
        "service_namespace": "ServiceNamespace",
        "predictive_scaling_max_capacity_behavior": "PredictiveScalingMaxCapacityBehavior",
        "scalable_dimension": "ScalableDimension",
        "scaling_policy_update_behavior": "ScalingPolicyUpdateBehavior",
        "min_capacity": "MinCapacity",
        "target_tracking_configurations": "TargetTrackingConfigurations",
        "predictive_scaling_max_capacity_buffer": "PredictiveScalingMaxCapacityBuffer",
        "customized_load_metric_specification": "CustomizedLoadMetricSpecification",
        "predefined_load_metric_specification": "PredefinedLoadMetricSpecification",
        "resource_id": "ResourceId",
        "scheduled_action_buffer_time": "ScheduledActionBufferTime",
        "max_capacity": "MaxCapacity",
        "predictive_scaling_mode": "PredictiveScalingMode",
    }

    disable_dynamic_scaling: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    service_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    predictive_scaling_max_capacity_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scalable_dimension: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scaling_policy_update_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_tracking_configurations: Optional[list[TargetTrackingConfiguration]] = None
    predictive_scaling_max_capacity_buffer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    customized_load_metric_specification: Optional[CustomizedLoadMetricSpecification] = None
    predefined_load_metric_specification: Optional[PredefinedLoadMetricSpecification] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scheduled_action_buffer_time: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    predictive_scaling_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagFilter(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    SCALE_OUT_COOLDOWN = "ScaleOutCooldown"
    TARGET_VALUE = "TargetValue"
    PREDEFINED_SCALING_METRIC_SPECIFICATION = "PredefinedScalingMetricSpecification"
    DISABLE_SCALE_IN = "DisableScaleIn"
    SCALE_IN_COOLDOWN = "ScaleInCooldown"
    ESTIMATED_INSTANCE_WARMUP = "EstimatedInstanceWarmup"
    CUSTOMIZED_SCALING_METRIC_SPECIFICATION = "CustomizedScalingMetricSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_out_cooldown": "ScaleOutCooldown",
        "target_value": "TargetValue",
        "predefined_scaling_metric_specification": "PredefinedScalingMetricSpecification",
        "disable_scale_in": "DisableScaleIn",
        "scale_in_cooldown": "ScaleInCooldown",
        "estimated_instance_warmup": "EstimatedInstanceWarmup",
        "customized_scaling_metric_specification": "CustomizedScalingMetricSpecification",
    }

    scale_out_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    predefined_scaling_metric_specification: Optional[PredefinedScalingMetricSpecification] = None
    disable_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scale_in_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    estimated_instance_warmup: Optional[Union[int, Ref, GetAtt, Sub]] = None
    customized_scaling_metric_specification: Optional[CustomizedScalingMetricSpecification] = None

