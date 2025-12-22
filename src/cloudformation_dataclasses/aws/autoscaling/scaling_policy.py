"""PropertyTypes for AWS::AutoScaling::ScalingPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratorManufacturer:
    """AcceleratorManufacturer enum values."""

    NVIDIA = "nvidia"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    XILINX = "xilinx"


class AcceleratorName:
    """AcceleratorName enum values."""

    A100 = "a100"
    V100 = "v100"
    K80 = "k80"
    T4 = "t4"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    VU9P = "vu9p"


class AcceleratorType:
    """AcceleratorType enum values."""

    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class BareMetal:
    """BareMetal enum values."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    REQUIRED = "required"


class BurstablePerformance:
    """BurstablePerformance enum values."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    REQUIRED = "required"


class CapacityDistributionStrategy:
    """CapacityDistributionStrategy enum values."""

    BALANCED_ONLY = "balanced-only"
    BALANCED_BEST_EFFORT = "balanced-best-effort"


class CapacityReservationPreference:
    """CapacityReservationPreference enum values."""

    CAPACITY_RESERVATIONS_ONLY = "capacity-reservations-only"
    CAPACITY_RESERVATIONS_FIRST = "capacity-reservations-first"
    NONE = "none"
    DEFAULT = "default"


class CpuManufacturer:
    """CpuManufacturer enum values."""

    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    APPLE = "apple"


class ImpairedZoneHealthCheckBehavior:
    """ImpairedZoneHealthCheckBehavior enum values."""

    REPLACEUNHEALTHY = "ReplaceUnhealthy"
    IGNOREUNHEALTHY = "IgnoreUnhealthy"


class InstanceGeneration:
    """InstanceGeneration enum values."""

    CURRENT = "current"
    PREVIOUS = "previous"


class InstanceMetadataEndpointState:
    """InstanceMetadataEndpointState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class InstanceMetadataHttpTokensState:
    """InstanceMetadataHttpTokensState enum values."""

    OPTIONAL = "optional"
    REQUIRED = "required"


class InstanceRefreshStatus:
    """InstanceRefreshStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
    ROLLBACKINPROGRESS = "RollbackInProgress"
    ROLLBACKFAILED = "RollbackFailed"
    ROLLBACKSUCCESSFUL = "RollbackSuccessful"
    BAKING = "Baking"


class LifecycleState:
    """LifecycleState enum values."""

    PENDING = "Pending"
    PENDING_WAIT = "Pending:Wait"
    PENDING_PROCEED = "Pending:Proceed"
    QUARANTINED = "Quarantined"
    INSERVICE = "InService"
    TERMINATING = "Terminating"
    TERMINATING_WAIT = "Terminating:Wait"
    TERMINATING_PROCEED = "Terminating:Proceed"
    TERMINATED = "Terminated"
    DETACHING = "Detaching"
    DETACHED = "Detached"
    ENTERINGSTANDBY = "EnteringStandby"
    STANDBY = "Standby"
    WARMED_PENDING = "Warmed:Pending"
    WARMED_PENDING_WAIT = "Warmed:Pending:Wait"
    WARMED_PENDING_PROCEED = "Warmed:Pending:Proceed"
    WARMED_TERMINATING = "Warmed:Terminating"
    WARMED_TERMINATING_WAIT = "Warmed:Terminating:Wait"
    WARMED_TERMINATING_PROCEED = "Warmed:Terminating:Proceed"
    WARMED_TERMINATED = "Warmed:Terminated"
    WARMED_STOPPED = "Warmed:Stopped"
    WARMED_RUNNING = "Warmed:Running"
    WARMED_HIBERNATED = "Warmed:Hibernated"


class LocalStorage:
    """LocalStorage enum values."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    REQUIRED = "required"


class LocalStorageType:
    """LocalStorageType enum values."""

    HDD = "hdd"
    SSD = "ssd"


class MetricStatistic:
    """MetricStatistic enum values."""

    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    SAMPLECOUNT = "SampleCount"
    SUM = "Sum"


class MetricType:
    """MetricType enum values."""

    ASGAVERAGECPUUTILIZATION = "ASGAverageCPUUtilization"
    ASGAVERAGENETWORKIN = "ASGAverageNetworkIn"
    ASGAVERAGENETWORKOUT = "ASGAverageNetworkOut"
    ALBREQUESTCOUNTPERTARGET = "ALBRequestCountPerTarget"


class PredefinedLoadMetricType:
    """PredefinedLoadMetricType enum values."""

    ASGTOTALCPUUTILIZATION = "ASGTotalCPUUtilization"
    ASGTOTALNETWORKIN = "ASGTotalNetworkIn"
    ASGTOTALNETWORKOUT = "ASGTotalNetworkOut"
    ALBTARGETGROUPREQUESTCOUNT = "ALBTargetGroupRequestCount"


class PredefinedMetricPairType:
    """PredefinedMetricPairType enum values."""

    ASGCPUUTILIZATION = "ASGCPUUtilization"
    ASGNETWORKIN = "ASGNetworkIn"
    ASGNETWORKOUT = "ASGNetworkOut"
    ALBREQUESTCOUNT = "ALBRequestCount"


class PredefinedScalingMetricType:
    """PredefinedScalingMetricType enum values."""

    ASGAVERAGECPUUTILIZATION = "ASGAverageCPUUtilization"
    ASGAVERAGENETWORKIN = "ASGAverageNetworkIn"
    ASGAVERAGENETWORKOUT = "ASGAverageNetworkOut"
    ALBREQUESTCOUNTPERTARGET = "ALBRequestCountPerTarget"


class PredictiveScalingMaxCapacityBreachBehavior:
    """PredictiveScalingMaxCapacityBreachBehavior enum values."""

    HONORMAXCAPACITY = "HonorMaxCapacity"
    INCREASEMAXCAPACITY = "IncreaseMaxCapacity"


class PredictiveScalingMode:
    """PredictiveScalingMode enum values."""

    FORECASTANDSCALE = "ForecastAndScale"
    FORECASTONLY = "ForecastOnly"


class RefreshStrategy:
    """RefreshStrategy enum values."""

    ROLLING = "Rolling"
    REPLACEROOTVOLUME = "ReplaceRootVolume"


class RetentionAction:
    """RetentionAction enum values."""

    RETAIN = "retain"
    TERMINATE = "terminate"


class RetryStrategy:
    """RetryStrategy enum values."""

    RETRY_WITH_GROUP_CONFIGURATION = "retry-with-group-configuration"
    NONE = "none"


class ScaleInProtectedInstances:
    """ScaleInProtectedInstances enum values."""

    REFRESH = "Refresh"
    IGNORE = "Ignore"
    WAIT = "Wait"


class ScalingActivityStatusCode:
    """ScalingActivityStatusCode enum values."""

    PENDINGSPOTBIDPLACEMENT = "PendingSpotBidPlacement"
    WAITINGFORSPOTINSTANCEREQUESTID = "WaitingForSpotInstanceRequestId"
    WAITINGFORSPOTINSTANCEID = "WaitingForSpotInstanceId"
    WAITINGFORINSTANCEID = "WaitingForInstanceId"
    PREINSERVICE = "PreInService"
    INPROGRESS = "InProgress"
    WAITINGFORELBCONNECTIONDRAINING = "WaitingForELBConnectionDraining"
    MIDLIFECYCLEACTION = "MidLifecycleAction"
    WAITINGFORINSTANCEWARMUP = "WaitingForInstanceWarmup"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    WAITINGFORCONNECTIONDRAINING = "WaitingForConnectionDraining"
    WAITINGFORINPLACEUPDATETOSTART = "WaitingForInPlaceUpdateToStart"
    WAITINGFORINPLACEUPDATETOFINALIZE = "WaitingForInPlaceUpdateToFinalize"
    INPLACEUPDATEINPROGRESS = "InPlaceUpdateInProgress"


class StandbyInstances:
    """StandbyInstances enum values."""

    TERMINATE = "Terminate"
    IGNORE = "Ignore"
    WAIT = "Wait"


class WarmPoolState:
    """WarmPoolState enum values."""

    STOPPED = "Stopped"
    RUNNING = "Running"
    HIBERNATED = "Hibernated"


class WarmPoolStatus:
    """WarmPoolStatus enum values."""

    PENDINGDELETE = "PendingDelete"


@dataclass
class CustomizedMetricSpecification(PropertyType):
    METRIC_NAME = "MetricName"
    METRICS = "Metrics"
    STATISTIC = "Statistic"
    DIMENSIONS = "Dimensions"
    PERIOD = "Period"
    UNIT = "Unit"
    NAMESPACE = "Namespace"

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
    METRIC_NAME = "MetricName"
    DIMENSIONS = "Dimensions"
    NAMESPACE = "Namespace"

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
    metric_stat: Optional[MetricStat] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class MetricStat(PropertyType):
    STAT = "Stat"
    METRIC = "Metric"
    UNIT = "Unit"

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
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, MetricType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingConfiguration(PropertyType):
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

    max_capacity_breach_behavior: Optional[Union[str, PredictiveScalingMaxCapacityBreachBehavior, Ref, GetAtt, Sub]] = None
    max_capacity_buffer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, PredictiveScalingMode, Ref, GetAtt, Sub]] = None
    metric_specifications: Optional[list[PredictiveScalingMetricSpecification]] = None
    scheduling_buffer_time: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingCustomizedCapacityMetric(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class PredictiveScalingCustomizedLoadMetric(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


@dataclass
class PredictiveScalingCustomizedScalingMetric(PropertyType):
    METRIC_DATA_QUERIES = "MetricDataQueries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_data_queries": "MetricDataQueries",
    }

    metric_data_queries: Optional[list[MetricDataQuery]] = None


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
class PredictiveScalingPredefinedLoadMetric(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, PredefinedLoadMetricType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedMetricPair(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, PredefinedMetricPairType, Ref, GetAtt, Sub]] = None
    resource_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveScalingPredefinedScalingMetric(PropertyType):
    PREDEFINED_METRIC_TYPE = "PredefinedMetricType"
    RESOURCE_LABEL = "ResourceLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "predefined_metric_type": "PredefinedMetricType",
        "resource_label": "ResourceLabel",
    }

    predefined_metric_type: Optional[Union[str, PredefinedScalingMetricType, Ref, GetAtt, Sub]] = None
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
class TargetTrackingConfiguration(PropertyType):
    TARGET_VALUE = "TargetValue"
    CUSTOMIZED_METRIC_SPECIFICATION = "CustomizedMetricSpecification"
    DISABLE_SCALE_IN = "DisableScaleIn"
    PREDEFINED_METRIC_SPECIFICATION = "PredefinedMetricSpecification"

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
    RETURN_DATA = "ReturnData"
    EXPRESSION = "Expression"
    LABEL = "Label"
    METRIC_STAT = "MetricStat"
    PERIOD = "Period"
    ID = "Id"

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

