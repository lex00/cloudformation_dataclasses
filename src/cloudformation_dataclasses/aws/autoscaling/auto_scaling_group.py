"""PropertyTypes for AWS::AutoScaling::AutoScalingGroup."""

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
class AcceleratorCountRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AcceleratorTotalMemoryMiBRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AvailabilityZoneDistribution(PropertyType):
    CAPACITY_DISTRIBUTION_STRATEGY = "CapacityDistributionStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_distribution_strategy": "CapacityDistributionStrategy",
    }

    capacity_distribution_strategy: Optional[Union[str, CapacityDistributionStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class AvailabilityZoneImpairmentPolicy(PropertyType):
    ZONAL_SHIFT_ENABLED = "ZonalShiftEnabled"
    IMPAIRED_ZONE_HEALTH_CHECK_BEHAVIOR = "ImpairedZoneHealthCheckBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "zonal_shift_enabled": "ZonalShiftEnabled",
        "impaired_zone_health_check_behavior": "ImpairedZoneHealthCheckBehavior",
    }

    zonal_shift_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    impaired_zone_health_check_behavior: Optional[Union[str, ImpairedZoneHealthCheckBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    CPU = "Cpu"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu": "Cpu",
    }

    cpu: Optional[CpuPerformanceFactorRequest] = None


@dataclass
class CapacityReservationSpecification(PropertyType):
    CAPACITY_RESERVATION_PREFERENCE = "CapacityReservationPreference"
    CAPACITY_RESERVATION_TARGET = "CapacityReservationTarget"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_preference": "CapacityReservationPreference",
        "capacity_reservation_target": "CapacityReservationTarget",
    }

    capacity_reservation_preference: Optional[Union[str, CapacityReservationPreference, Ref, GetAtt, Sub]] = None
    capacity_reservation_target: Optional[CapacityReservationTarget] = None


@dataclass
class CapacityReservationTarget(PropertyType):
    CAPACITY_RESERVATION_IDS = "CapacityReservationIds"
    CAPACITY_RESERVATION_RESOURCE_GROUP_ARNS = "CapacityReservationResourceGroupArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_ids": "CapacityReservationIds",
        "capacity_reservation_resource_group_arns": "CapacityReservationResourceGroupArns",
    }

    capacity_reservation_ids: Optional[Union[list[str], Ref]] = None
    capacity_reservation_resource_group_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    REFERENCES = "References"

    _property_mappings: ClassVar[dict[str, str]] = {
        "references": "References",
    }

    references: Optional[list[PerformanceFactorReferenceRequest]] = None


@dataclass
class InstanceMaintenancePolicy(PropertyType):
    MAX_HEALTHY_PERCENTAGE = "MaxHealthyPercentage"
    MIN_HEALTHY_PERCENTAGE = "MinHealthyPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_healthy_percentage": "MaxHealthyPercentage",
        "min_healthy_percentage": "MinHealthyPercentage",
    }

    max_healthy_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_healthy_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirements(PropertyType):
    INSTANCE_GENERATIONS = "InstanceGenerations"
    ACCELERATOR_TYPES = "AcceleratorTypes"
    MEMORY_GI_B_PER_V_CPU = "MemoryGiBPerVCpu"
    ACCELERATOR_MANUFACTURERS = "AcceleratorManufacturers"
    V_CPU_COUNT = "VCpuCount"
    LOCAL_STORAGE = "LocalStorage"
    CPU_MANUFACTURERS = "CpuManufacturers"
    BARE_METAL = "BareMetal"
    REQUIRE_HIBERNATE_SUPPORT = "RequireHibernateSupport"
    MAX_SPOT_PRICE_AS_PERCENTAGE_OF_OPTIMAL_ON_DEMAND_PRICE = "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    ON_DEMAND_MAX_PRICE_PERCENTAGE_OVER_LOWEST_PRICE = "OnDemandMaxPricePercentageOverLowestPrice"
    MEMORY_MI_B = "MemoryMiB"
    LOCAL_STORAGE_TYPES = "LocalStorageTypes"
    NETWORK_INTERFACE_COUNT = "NetworkInterfaceCount"
    EXCLUDED_INSTANCE_TYPES = "ExcludedInstanceTypes"
    ALLOWED_INSTANCE_TYPES = "AllowedInstanceTypes"
    ACCELERATOR_COUNT = "AcceleratorCount"
    NETWORK_BANDWIDTH_GBPS = "NetworkBandwidthGbps"
    BASELINE_PERFORMANCE_FACTORS = "BaselinePerformanceFactors"
    BASELINE_EBS_BANDWIDTH_MBPS = "BaselineEbsBandwidthMbps"
    SPOT_MAX_PRICE_PERCENTAGE_OVER_LOWEST_PRICE = "SpotMaxPricePercentageOverLowestPrice"
    ACCELERATOR_NAMES = "AcceleratorNames"
    ACCELERATOR_TOTAL_MEMORY_MI_B = "AcceleratorTotalMemoryMiB"
    BURSTABLE_PERFORMANCE = "BurstablePerformance"
    TOTAL_LOCAL_STORAGE_GB = "TotalLocalStorageGB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_generations": "InstanceGenerations",
        "accelerator_types": "AcceleratorTypes",
        "memory_gi_b_per_v_cpu": "MemoryGiBPerVCpu",
        "accelerator_manufacturers": "AcceleratorManufacturers",
        "v_cpu_count": "VCpuCount",
        "local_storage": "LocalStorage",
        "cpu_manufacturers": "CpuManufacturers",
        "bare_metal": "BareMetal",
        "require_hibernate_support": "RequireHibernateSupport",
        "max_spot_price_as_percentage_of_optimal_on_demand_price": "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice",
        "on_demand_max_price_percentage_over_lowest_price": "OnDemandMaxPricePercentageOverLowestPrice",
        "memory_mi_b": "MemoryMiB",
        "local_storage_types": "LocalStorageTypes",
        "network_interface_count": "NetworkInterfaceCount",
        "excluded_instance_types": "ExcludedInstanceTypes",
        "allowed_instance_types": "AllowedInstanceTypes",
        "accelerator_count": "AcceleratorCount",
        "network_bandwidth_gbps": "NetworkBandwidthGbps",
        "baseline_performance_factors": "BaselinePerformanceFactors",
        "baseline_ebs_bandwidth_mbps": "BaselineEbsBandwidthMbps",
        "spot_max_price_percentage_over_lowest_price": "SpotMaxPricePercentageOverLowestPrice",
        "accelerator_names": "AcceleratorNames",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "burstable_performance": "BurstablePerformance",
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    instance_generations: Optional[Union[list[str], Ref]] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    memory_gi_b_per_v_cpu: Optional[MemoryGiBPerVCpuRequest] = None
    accelerator_manufacturers: Optional[Union[list[str], Ref]] = None
    v_cpu_count: Optional[VCpuCountRequest] = None
    local_storage: Optional[Union[str, LocalStorage, Ref, GetAtt, Sub]] = None
    cpu_manufacturers: Optional[Union[list[str], Ref]] = None
    bare_metal: Optional[Union[str, BareMetal, Ref, GetAtt, Sub]] = None
    require_hibernate_support: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    memory_mi_b: Optional[MemoryMiBRequest] = None
    local_storage_types: Optional[Union[list[str], Ref]] = None
    network_interface_count: Optional[NetworkInterfaceCountRequest] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    accelerator_count: Optional[AcceleratorCountRequest] = None
    network_bandwidth_gbps: Optional[NetworkBandwidthGbpsRequest] = None
    baseline_performance_factors: Optional[BaselinePerformanceFactorsRequest] = None
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    spot_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    accelerator_names: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiBRequest] = None
    burstable_performance: Optional[Union[str, BurstablePerformance, Ref, GetAtt, Sub]] = None
    total_local_storage_gb: Optional[TotalLocalStorageGBRequest] = None


@dataclass
class InstancesDistribution(PropertyType):
    ON_DEMAND_ALLOCATION_STRATEGY = "OnDemandAllocationStrategy"
    ON_DEMAND_BASE_CAPACITY = "OnDemandBaseCapacity"
    ON_DEMAND_PERCENTAGE_ABOVE_BASE_CAPACITY = "OnDemandPercentageAboveBaseCapacity"
    SPOT_INSTANCE_POOLS = "SpotInstancePools"
    SPOT_ALLOCATION_STRATEGY = "SpotAllocationStrategy"
    SPOT_MAX_PRICE = "SpotMaxPrice"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_allocation_strategy": "OnDemandAllocationStrategy",
        "on_demand_base_capacity": "OnDemandBaseCapacity",
        "on_demand_percentage_above_base_capacity": "OnDemandPercentageAboveBaseCapacity",
        "spot_instance_pools": "SpotInstancePools",
        "spot_allocation_strategy": "SpotAllocationStrategy",
        "spot_max_price": "SpotMaxPrice",
    }

    on_demand_allocation_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_demand_base_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_demand_percentage_above_base_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_instance_pools: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_allocation_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    spot_max_price: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplate(PropertyType):
    LAUNCH_TEMPLATE_SPECIFICATION = "LaunchTemplateSpecification"
    OVERRIDES = "Overrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_specification": "LaunchTemplateSpecification",
        "overrides": "Overrides",
    }

    launch_template_specification: Optional[LaunchTemplateSpecification] = None
    overrides: Optional[list[LaunchTemplateOverrides]] = None


@dataclass
class LaunchTemplateOverrides(PropertyType):
    LAUNCH_TEMPLATE_SPECIFICATION = "LaunchTemplateSpecification"
    WEIGHTED_CAPACITY = "WeightedCapacity"
    INSTANCE_REQUIREMENTS = "InstanceRequirements"
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_specification": "LaunchTemplateSpecification",
        "weighted_capacity": "WeightedCapacity",
        "instance_requirements": "InstanceRequirements",
        "instance_type": "InstanceType",
    }

    launch_template_specification: Optional[LaunchTemplateSpecification] = None
    weighted_capacity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_requirements: Optional[InstanceRequirements] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    LAUNCH_TEMPLATE_NAME = "LaunchTemplateName"
    VERSION = "Version"
    LAUNCH_TEMPLATE_ID = "LaunchTemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "launch_template_id": "LaunchTemplateId",
    }

    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleHookSpecification(PropertyType):
    LIFECYCLE_HOOK_NAME = "LifecycleHookName"
    LIFECYCLE_TRANSITION = "LifecycleTransition"
    HEARTBEAT_TIMEOUT = "HeartbeatTimeout"
    NOTIFICATION_METADATA = "NotificationMetadata"
    DEFAULT_RESULT = "DefaultResult"
    NOTIFICATION_TARGET_ARN = "NotificationTargetARN"
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle_hook_name": "LifecycleHookName",
        "lifecycle_transition": "LifecycleTransition",
        "heartbeat_timeout": "HeartbeatTimeout",
        "notification_metadata": "NotificationMetadata",
        "default_result": "DefaultResult",
        "notification_target_arn": "NotificationTargetARN",
        "role_arn": "RoleARN",
    }

    lifecycle_hook_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lifecycle_transition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    heartbeat_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    notification_metadata: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_result: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryMiBRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsCollection(PropertyType):
    METRICS = "Metrics"
    GRANULARITY = "Granularity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metrics": "Metrics",
        "granularity": "Granularity",
    }

    metrics: Optional[Union[list[str], Ref]] = None
    granularity: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MixedInstancesPolicy(PropertyType):
    INSTANCES_DISTRIBUTION = "InstancesDistribution"
    LAUNCH_TEMPLATE = "LaunchTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instances_distribution": "InstancesDistribution",
        "launch_template": "LaunchTemplate",
    }

    instances_distribution: Optional[InstancesDistribution] = None
    launch_template: Optional[LaunchTemplate] = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfiguration(PropertyType):
    TOPIC_ARN = "TopicARN"
    NOTIFICATION_TYPES = "NotificationTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicARN",
        "notification_types": "NotificationTypes",
    }

    topic_arn: Optional[Union[list[str], Ref]] = None
    notification_types: Optional[Union[list[str], Ref]] = None


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    INSTANCE_FAMILY = "InstanceFamily"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_family": "InstanceFamily",
    }

    instance_family: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagProperty(PropertyType):
    VALUE = "Value"
    KEY = "Key"
    PROPAGATE_AT_LAUNCH = "PropagateAtLaunch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
        "propagate_at_launch": "PropagateAtLaunch",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    propagate_at_launch: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TrafficSourceIdentifier(PropertyType):
    TYPE = "Type"
    IDENTIFIER = "Identifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "identifier": "Identifier",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VCpuCountRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None

