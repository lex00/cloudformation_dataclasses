"""PropertyTypes for AWS::EMR::InstanceGroupConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoScalingPolicy(PropertyType):
    CONSTRAINTS = "Constraints"
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "rules": "Rules",
    }

    constraints: Optional[ScalingConstraints] = None
    rules: Optional[list[ScalingRule]] = None


@dataclass
class CloudWatchAlarmDefinition(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    DIMENSIONS = "Dimensions"
    EVALUATION_PERIODS = "EvaluationPeriods"
    METRIC_NAME = "MetricName"
    NAMESPACE = "Namespace"
    PERIOD = "Period"
    STATISTIC = "Statistic"
    THRESHOLD = "Threshold"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "dimensions": "Dimensions",
        "evaluation_periods": "EvaluationPeriods",
        "metric_name": "MetricName",
        "namespace": "Namespace",
        "period": "Period",
        "statistic": "Statistic",
        "threshold": "Threshold",
        "unit": "Unit",
    }

    comparison_operator: Optional[Union[str, ComparisonOperator, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[MetricDimension]] = None
    evaluation_periods: Optional[Union[int, Ref, GetAtt, Sub]] = None
    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    statistic: Optional[Union[str, Statistic, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Unit, Ref, GetAtt, Sub]] = None


@dataclass
class Configuration(PropertyType):
    CLASSIFICATION = "Classification"
    CONFIGURATION_PROPERTIES = "ConfigurationProperties"
    CONFIGURATIONS = "Configurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "classification": "Classification",
        "configuration_properties": "ConfigurationProperties",
        "configurations": "Configurations",
    }

    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_properties: Optional[dict[str, str]] = None
    configurations: Optional[list[Configuration]] = None


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    VOLUME_SPECIFICATION = "VolumeSpecification"
    VOLUMES_PER_INSTANCE = "VolumesPerInstance"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_specification": "VolumeSpecification",
        "volumes_per_instance": "VolumesPerInstance",
    }

    volume_specification: Optional[VolumeSpecification] = None
    volumes_per_instance: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EbsConfiguration(PropertyType):
    EBS_BLOCK_DEVICE_CONFIGS = "EbsBlockDeviceConfigs"
    EBS_OPTIMIZED = "EbsOptimized"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_block_device_configs": "EbsBlockDeviceConfigs",
        "ebs_optimized": "EbsOptimized",
    }

    ebs_block_device_configs: Optional[list[EbsBlockDeviceConfig]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDimension(PropertyType):
    KEY = "Key"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key": "Key",
        "value": "Value",
    }

    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingAction(PropertyType):
    MARKET = "Market"
    SIMPLE_SCALING_POLICY_CONFIGURATION = "SimpleScalingPolicyConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "market": "Market",
        "simple_scaling_policy_configuration": "SimpleScalingPolicyConfiguration",
    }

    market: Optional[Union[str, MarketType, Ref, GetAtt, Sub]] = None
    simple_scaling_policy_configuration: Optional[SimpleScalingPolicyConfiguration] = None


@dataclass
class ScalingConstraints(PropertyType):
    MAX_CAPACITY = "MaxCapacity"
    MIN_CAPACITY = "MinCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_capacity": "MaxCapacity",
        "min_capacity": "MinCapacity",
    }

    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingRule(PropertyType):
    ACTION = "Action"
    DESCRIPTION = "Description"
    NAME = "Name"
    TRIGGER = "Trigger"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "description": "Description",
        "name": "Name",
        "trigger": "Trigger",
    }

    action: Optional[ScalingAction] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger: Optional[ScalingTrigger] = None


@dataclass
class ScalingTrigger(PropertyType):
    CLOUD_WATCH_ALARM_DEFINITION = "CloudWatchAlarmDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_alarm_definition": "CloudWatchAlarmDefinition",
    }

    cloud_watch_alarm_definition: Optional[CloudWatchAlarmDefinition] = None


@dataclass
class SimpleScalingPolicyConfiguration(PropertyType):
    ADJUSTMENT_TYPE = "AdjustmentType"
    COOL_DOWN = "CoolDown"
    SCALING_ADJUSTMENT = "ScalingAdjustment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "adjustment_type": "AdjustmentType",
        "cool_down": "CoolDown",
        "scaling_adjustment": "ScalingAdjustment",
    }

    adjustment_type: Optional[Union[str, AdjustmentType, Ref, GetAtt, Sub]] = None
    cool_down: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scaling_adjustment: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeSpecification(PropertyType):
    IOPS = "Iops"
    SIZE_IN_GB = "SizeInGB"
    THROUGHPUT = "Throughput"
    VOLUME_TYPE = "VolumeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iops": "Iops",
        "size_in_gb": "SizeInGB",
        "throughput": "Throughput",
        "volume_type": "VolumeType",
    }

    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

