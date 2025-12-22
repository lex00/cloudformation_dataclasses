"""PropertyTypes for AWS::ECS::CapacityProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratorManufacturer:
    """AcceleratorManufacturer enum values."""

    AMAZON_WEB_SERVICES = "amazon-web-services"
    AMD = "amd"
    NVIDIA = "nvidia"
    XILINX = "xilinx"
    HABANA = "habana"


class AcceleratorName:
    """AcceleratorName enum values."""

    A100 = "a100"
    INFERENTIA = "inferentia"
    K520 = "k520"
    K80 = "k80"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    T4 = "t4"
    VU9P = "vu9p"
    V100 = "v100"
    A10G = "a10g"
    H100 = "h100"
    T4G = "t4g"


class AcceleratorType:
    """AcceleratorType enum values."""

    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class AccessType:
    """AccessType enum values."""

    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class AgentUpdateStatus:
    """AgentUpdateStatus enum values."""

    PENDING = "PENDING"
    STAGING = "STAGING"
    STAGED = "STAGED"
    UPDATING = "UPDATING"
    UPDATED = "UPDATED"
    FAILED = "FAILED"


class ApplicationProtocol:
    """ApplicationProtocol enum values."""

    HTTP = "http"
    HTTP2 = "http2"
    GRPC = "grpc"


class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AvailabilityZoneRebalancing:
    """AvailabilityZoneRebalancing enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BareMetal:
    """BareMetal enum values."""

    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class BurstablePerformance:
    """BurstablePerformance enum values."""

    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class CPUArchitecture:
    """CPUArchitecture enum values."""

    X86_64 = "X86_64"
    ARM64 = "ARM64"


class CapacityProviderField:
    """CapacityProviderField enum values."""

    TAGS = "TAGS"


class CapacityProviderStatus:
    """CapacityProviderStatus enum values."""

    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    DEPROVISIONING = "DEPROVISIONING"
    INACTIVE = "INACTIVE"


class CapacityProviderType:
    """CapacityProviderType enum values."""

    EC2_AUTOSCALING = "EC2_AUTOSCALING"
    MANAGED_INSTANCES = "MANAGED_INSTANCES"
    FARGATE = "FARGATE"
    FARGATE_SPOT = "FARGATE_SPOT"


class CapacityProviderUpdateStatus:
    """CapacityProviderUpdateStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"


class ClusterField:
    """ClusterField enum values."""

    ATTACHMENTS = "ATTACHMENTS"
    CONFIGURATIONS = "CONFIGURATIONS"
    SETTINGS = "SETTINGS"
    STATISTICS = "STATISTICS"
    TAGS = "TAGS"


class ClusterSettingName:
    """ClusterSettingName enum values."""

    CONTAINERINSIGHTS = "containerInsights"


class Compatibility:
    """Compatibility enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"
    MANAGED_INSTANCES = "MANAGED_INSTANCES"


class Connectivity:
    """Connectivity enum values."""

    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"


class ContainerCondition:
    """ContainerCondition enum values."""

    START = "START"
    COMPLETE = "COMPLETE"
    SUCCESS = "SUCCESS"
    HEALTHY = "HEALTHY"


class ContainerInstanceField:
    """ContainerInstanceField enum values."""

    TAGS = "TAGS"
    CONTAINER_INSTANCE_HEALTH = "CONTAINER_INSTANCE_HEALTH"


class ContainerInstanceStatus:
    """ContainerInstanceStatus enum values."""

    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"
    REGISTERING = "REGISTERING"
    DEREGISTERING = "DEREGISTERING"
    REGISTRATION_FAILED = "REGISTRATION_FAILED"


class CpuManufacturer:
    """CpuManufacturer enum values."""

    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"


class DeploymentControllerType:
    """DeploymentControllerType enum values."""

    ECS = "ECS"
    CODE_DEPLOY = "CODE_DEPLOY"
    EXTERNAL = "EXTERNAL"


class DeploymentLifecycleHookStage:
    """DeploymentLifecycleHookStage enum values."""

    RECONCILE_SERVICE = "RECONCILE_SERVICE"
    PRE_SCALE_UP = "PRE_SCALE_UP"
    POST_SCALE_UP = "POST_SCALE_UP"
    TEST_TRAFFIC_SHIFT = "TEST_TRAFFIC_SHIFT"
    POST_TEST_TRAFFIC_SHIFT = "POST_TEST_TRAFFIC_SHIFT"
    PRODUCTION_TRAFFIC_SHIFT = "PRODUCTION_TRAFFIC_SHIFT"
    POST_PRODUCTION_TRAFFIC_SHIFT = "POST_PRODUCTION_TRAFFIC_SHIFT"


class DeploymentRolloutState:
    """DeploymentRolloutState enum values."""

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class DeploymentStrategy:
    """DeploymentStrategy enum values."""

    ROLLING = "ROLLING"
    BLUE_GREEN = "BLUE_GREEN"
    LINEAR = "LINEAR"
    CANARY = "CANARY"


class DesiredStatus:
    """DesiredStatus enum values."""

    RUNNING = "RUNNING"
    PENDING = "PENDING"
    STOPPED = "STOPPED"


class DeviceCgroupPermission:
    """DeviceCgroupPermission enum values."""

    READ = "read"
    WRITE = "write"
    MKNOD = "mknod"


class EBSResourceType:
    """EBSResourceType enum values."""

    VOLUME = "volume"


class EFSAuthorizationConfigIAM:
    """EFSAuthorizationConfigIAM enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EFSTransitEncryption:
    """EFSTransitEncryption enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EnvironmentFileType:
    """EnvironmentFileType enum values."""

    S3 = "s3"


class ExecuteCommandLogging:
    """ExecuteCommandLogging enum values."""

    NONE = "NONE"
    DEFAULT = "DEFAULT"
    OVERRIDE = "OVERRIDE"


class ExpressGatewayServiceInclude:
    """ExpressGatewayServiceInclude enum values."""

    TAGS = "TAGS"


class ExpressGatewayServiceScalingMetric:
    """ExpressGatewayServiceScalingMetric enum values."""

    AVERAGE_CPU = "AVERAGE_CPU"
    AVERAGE_MEMORY = "AVERAGE_MEMORY"
    REQUEST_COUNT_PER_TARGET = "REQUEST_COUNT_PER_TARGET"


class ExpressGatewayServiceStatusCode:
    """ExpressGatewayServiceStatusCode enum values."""

    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"
    INACTIVE = "INACTIVE"


class FirelensConfigurationType:
    """FirelensConfigurationType enum values."""

    FLUENTD = "fluentd"
    FLUENTBIT = "fluentbit"


class HealthStatus:
    """HealthStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"


class InstanceGeneration:
    """InstanceGeneration enum values."""

    CURRENT = "current"
    PREVIOUS = "previous"


class InstanceHealthCheckState:
    """InstanceHealthCheckState enum values."""

    OK = "OK"
    IMPAIRED = "IMPAIRED"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    INITIALIZING = "INITIALIZING"


class InstanceHealthCheckType:
    """InstanceHealthCheckType enum values."""

    CONTAINER_RUNTIME = "CONTAINER_RUNTIME"


class IpcMode:
    """IpcMode enum values."""

    HOST = "host"
    TASK = "task"
    NONE = "none"


class LaunchType:
    """LaunchType enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"
    MANAGED_INSTANCES = "MANAGED_INSTANCES"


class LocalStorage:
    """LocalStorage enum values."""

    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class LocalStorageType:
    """LocalStorageType enum values."""

    HDD = "hdd"
    SSD = "ssd"


class LogDriver:
    """LogDriver enum values."""

    JSON_FILE = "json-file"
    SYSLOG = "syslog"
    JOURNALD = "journald"
    GELF = "gelf"
    FLUENTD = "fluentd"
    AWSLOGS = "awslogs"
    SPLUNK = "splunk"
    AWSFIRELENS = "awsfirelens"


class ManagedAgentName:
    """ManagedAgentName enum values."""

    EXECUTECOMMANDAGENT = "ExecuteCommandAgent"


class ManagedDraining:
    """ManagedDraining enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ManagedInstancesMonitoringOptions:
    """ManagedInstancesMonitoringOptions enum values."""

    BASIC = "BASIC"
    DETAILED = "DETAILED"


class ManagedResourceStatus:
    """ManagedResourceStatus enum values."""

    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    DEPROVISIONING = "DEPROVISIONING"
    DELETED = "DELETED"
    FAILED = "FAILED"


class ManagedScalingStatus:
    """ManagedScalingStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ManagedTerminationProtection:
    """ManagedTerminationProtection enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class NetworkMode:
    """NetworkMode enum values."""

    BRIDGE = "bridge"
    HOST = "host"
    AWSVPC = "awsvpc"
    NONE = "none"


class OSFamily:
    """OSFamily enum values."""

    WINDOWS_SERVER_2019_FULL = "WINDOWS_SERVER_2019_FULL"
    WINDOWS_SERVER_2019_CORE = "WINDOWS_SERVER_2019_CORE"
    WINDOWS_SERVER_2016_FULL = "WINDOWS_SERVER_2016_FULL"
    WINDOWS_SERVER_2004_CORE = "WINDOWS_SERVER_2004_CORE"
    WINDOWS_SERVER_2022_CORE = "WINDOWS_SERVER_2022_CORE"
    WINDOWS_SERVER_2022_FULL = "WINDOWS_SERVER_2022_FULL"
    WINDOWS_SERVER_2025_CORE = "WINDOWS_SERVER_2025_CORE"
    WINDOWS_SERVER_2025_FULL = "WINDOWS_SERVER_2025_FULL"
    WINDOWS_SERVER_20H2_CORE = "WINDOWS_SERVER_20H2_CORE"
    LINUX = "LINUX"


class PidMode:
    """PidMode enum values."""

    HOST = "host"
    TASK = "task"


class PlacementConstraintType:
    """PlacementConstraintType enum values."""

    DISTINCTINSTANCE = "distinctInstance"
    MEMBEROF = "memberOf"


class PlacementStrategyType:
    """PlacementStrategyType enum values."""

    RANDOM = "random"
    SPREAD = "spread"
    BINPACK = "binpack"


class PlatformDeviceType:
    """PlatformDeviceType enum values."""

    GPU = "GPU"


class PropagateMITags:
    """PropagateMITags enum values."""

    CAPACITY_PROVIDER = "CAPACITY_PROVIDER"
    NONE = "NONE"


class PropagateTags:
    """PropagateTags enum values."""

    TASK_DEFINITION = "TASK_DEFINITION"
    SERVICE = "SERVICE"
    NONE = "NONE"


class ProxyConfigurationType:
    """ProxyConfigurationType enum values."""

    APPMESH = "APPMESH"


class ResourceManagementType:
    """ResourceManagementType enum values."""

    CUSTOMER = "CUSTOMER"
    ECS = "ECS"


class ResourceType:
    """ResourceType enum values."""

    GPU = "GPU"
    INFERENCEACCELERATOR = "InferenceAccelerator"


class ScaleUnit:
    """ScaleUnit enum values."""

    PERCENT = "PERCENT"


class SchedulingStrategy:
    """SchedulingStrategy enum values."""

    REPLICA = "REPLICA"
    DAEMON = "DAEMON"


class Scope:
    """Scope enum values."""

    TASK = "task"
    SHARED = "shared"


class ServiceConnectAccessLoggingFormat:
    """ServiceConnectAccessLoggingFormat enum values."""

    TEXT = "TEXT"
    JSON = "JSON"


class ServiceConnectIncludeQueryParameters:
    """ServiceConnectIncludeQueryParameters enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ServiceDeploymentLifecycleStage:
    """ServiceDeploymentLifecycleStage enum values."""

    RECONCILE_SERVICE = "RECONCILE_SERVICE"
    PRE_SCALE_UP = "PRE_SCALE_UP"
    SCALE_UP = "SCALE_UP"
    POST_SCALE_UP = "POST_SCALE_UP"
    TEST_TRAFFIC_SHIFT = "TEST_TRAFFIC_SHIFT"
    POST_TEST_TRAFFIC_SHIFT = "POST_TEST_TRAFFIC_SHIFT"
    PRODUCTION_TRAFFIC_SHIFT = "PRODUCTION_TRAFFIC_SHIFT"
    POST_PRODUCTION_TRAFFIC_SHIFT = "POST_PRODUCTION_TRAFFIC_SHIFT"
    BAKE_TIME = "BAKE_TIME"
    CLEAN_UP = "CLEAN_UP"


class ServiceDeploymentRollbackMonitorsStatus:
    """ServiceDeploymentRollbackMonitorsStatus enum values."""

    TRIGGERED = "TRIGGERED"
    MONITORING = "MONITORING"
    MONITORING_COMPLETE = "MONITORING_COMPLETE"
    DISABLED = "DISABLED"


class ServiceDeploymentStatus:
    """ServiceDeploymentStatus enum values."""

    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"
    STOPPED = "STOPPED"
    STOP_REQUESTED = "STOP_REQUESTED"
    IN_PROGRESS = "IN_PROGRESS"
    ROLLBACK_REQUESTED = "ROLLBACK_REQUESTED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_SUCCESSFUL = "ROLLBACK_SUCCESSFUL"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"


class ServiceField:
    """ServiceField enum values."""

    TAGS = "TAGS"


class SettingName:
    """SettingName enum values."""

    SERVICELONGARNFORMAT = "serviceLongArnFormat"
    TASKLONGARNFORMAT = "taskLongArnFormat"
    CONTAINERINSTANCELONGARNFORMAT = "containerInstanceLongArnFormat"
    AWSVPCTRUNKING = "awsvpcTrunking"
    CONTAINERINSIGHTS = "containerInsights"
    FARGATEFIPSMODE = "fargateFIPSMode"
    TAGRESOURCEAUTHORIZATION = "tagResourceAuthorization"
    FARGATETASKRETIREMENTWAITPERIOD = "fargateTaskRetirementWaitPeriod"
    GUARDDUTYACTIVATE = "guardDutyActivate"
    DEFAULTLOGDRIVERMODE = "defaultLogDriverMode"


class SettingType:
    """SettingType enum values."""

    USER = "user"
    AWS_MANAGED = "aws_managed"


class SortOrder:
    """SortOrder enum values."""

    ASC = "ASC"
    DESC = "DESC"


class StabilityStatus:
    """StabilityStatus enum values."""

    STEADY_STATE = "STEADY_STATE"
    STABILIZING = "STABILIZING"


class StopServiceDeploymentStopType:
    """StopServiceDeploymentStopType enum values."""

    ABORT = "ABORT"
    ROLLBACK = "ROLLBACK"


class TargetType:
    """TargetType enum values."""

    CONTAINER_INSTANCE = "container-instance"


class TaskDefinitionFamilyStatus:
    """TaskDefinitionFamilyStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ALL = "ALL"


class TaskDefinitionField:
    """TaskDefinitionField enum values."""

    TAGS = "TAGS"


class TaskDefinitionPlacementConstraintType:
    """TaskDefinitionPlacementConstraintType enum values."""

    MEMBEROF = "memberOf"


class TaskDefinitionStatus:
    """TaskDefinitionStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"


class TaskField:
    """TaskField enum values."""

    TAGS = "TAGS"


class TaskFilesystemType:
    """TaskFilesystemType enum values."""

    EXT3 = "ext3"
    EXT4 = "ext4"
    XFS = "xfs"
    NTFS = "ntfs"


class TaskSetField:
    """TaskSetField enum values."""

    TAGS = "TAGS"


class TaskStopCode:
    """TaskStopCode enum values."""

    TASKFAILEDTOSTART = "TaskFailedToStart"
    ESSENTIALCONTAINEREXITED = "EssentialContainerExited"
    USERINITIATED = "UserInitiated"
    SERVICESCHEDULERINITIATED = "ServiceSchedulerInitiated"
    SPOTINTERRUPTION = "SpotInterruption"
    TERMINATIONNOTICE = "TerminationNotice"


class TransportProtocol:
    """TransportProtocol enum values."""

    TCP = "tcp"
    UDP = "udp"


class UlimitName:
    """UlimitName enum values."""

    CORE = "core"
    CPU = "cpu"
    DATA = "data"
    FSIZE = "fsize"
    LOCKS = "locks"
    MEMLOCK = "memlock"
    MSGQUEUE = "msgqueue"
    NICE = "nice"
    NOFILE = "nofile"
    NPROC = "nproc"
    RSS = "rss"
    RTPRIO = "rtprio"
    RTTIME = "rttime"
    SIGPENDING = "sigpending"
    STACK = "stack"


class VersionConsistency:
    """VersionConsistency enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


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
class AutoScalingGroupProvider(PropertyType):
    MANAGED_SCALING = "ManagedScaling"
    AUTO_SCALING_GROUP_ARN = "AutoScalingGroupArn"
    MANAGED_TERMINATION_PROTECTION = "ManagedTerminationProtection"
    MANAGED_DRAINING = "ManagedDraining"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_scaling": "ManagedScaling",
        "auto_scaling_group_arn": "AutoScalingGroupArn",
        "managed_termination_protection": "ManagedTerminationProtection",
        "managed_draining": "ManagedDraining",
    }

    managed_scaling: Optional[ManagedScaling] = None
    auto_scaling_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_termination_protection: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_draining: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class InfrastructureOptimization(PropertyType):
    SCALE_IN_AFTER = "ScaleInAfter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_in_after": "ScaleInAfter",
    }

    scale_in_after: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceLaunchTemplate(PropertyType):
    EC2_INSTANCE_PROFILE_ARN = "Ec2InstanceProfileArn"
    STORAGE_CONFIGURATION = "StorageConfiguration"
    NETWORK_CONFIGURATION = "NetworkConfiguration"
    INSTANCE_REQUIREMENTS = "InstanceRequirements"
    MONITORING = "Monitoring"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ec2_instance_profile_arn": "Ec2InstanceProfileArn",
        "storage_configuration": "StorageConfiguration",
        "network_configuration": "NetworkConfiguration",
        "instance_requirements": "InstanceRequirements",
        "monitoring": "Monitoring",
    }

    ec2_instance_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_configuration: Optional[ManagedInstancesStorageConfiguration] = None
    network_configuration: Optional[ManagedInstancesNetworkConfiguration] = None
    instance_requirements: Optional[InstanceRequirementsRequest] = None
    monitoring: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    LOCAL_STORAGE_TYPES = "LocalStorageTypes"
    INSTANCE_GENERATIONS = "InstanceGenerations"
    NETWORK_INTERFACE_COUNT = "NetworkInterfaceCount"
    MEMORY_GI_B_PER_V_CPU = "MemoryGiBPerVCpu"
    ACCELERATOR_TYPES = "AcceleratorTypes"
    V_CPU_COUNT = "VCpuCount"
    EXCLUDED_INSTANCE_TYPES = "ExcludedInstanceTypes"
    ACCELERATOR_MANUFACTURERS = "AcceleratorManufacturers"
    ALLOWED_INSTANCE_TYPES = "AllowedInstanceTypes"
    LOCAL_STORAGE = "LocalStorage"
    CPU_MANUFACTURERS = "CpuManufacturers"
    NETWORK_BANDWIDTH_GBPS = "NetworkBandwidthGbps"
    ACCELERATOR_COUNT = "AcceleratorCount"
    BARE_METAL = "BareMetal"
    REQUIRE_HIBERNATE_SUPPORT = "RequireHibernateSupport"
    MAX_SPOT_PRICE_AS_PERCENTAGE_OF_OPTIMAL_ON_DEMAND_PRICE = "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    SPOT_MAX_PRICE_PERCENTAGE_OVER_LOWEST_PRICE = "SpotMaxPricePercentageOverLowestPrice"
    BASELINE_EBS_BANDWIDTH_MBPS = "BaselineEbsBandwidthMbps"
    ON_DEMAND_MAX_PRICE_PERCENTAGE_OVER_LOWEST_PRICE = "OnDemandMaxPricePercentageOverLowestPrice"
    ACCELERATOR_NAMES = "AcceleratorNames"
    ACCELERATOR_TOTAL_MEMORY_MI_B = "AcceleratorTotalMemoryMiB"
    BURSTABLE_PERFORMANCE = "BurstablePerformance"
    MEMORY_MI_B = "MemoryMiB"
    TOTAL_LOCAL_STORAGE_GB = "TotalLocalStorageGB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "local_storage_types": "LocalStorageTypes",
        "instance_generations": "InstanceGenerations",
        "network_interface_count": "NetworkInterfaceCount",
        "memory_gi_b_per_v_cpu": "MemoryGiBPerVCpu",
        "accelerator_types": "AcceleratorTypes",
        "v_cpu_count": "VCpuCount",
        "excluded_instance_types": "ExcludedInstanceTypes",
        "accelerator_manufacturers": "AcceleratorManufacturers",
        "allowed_instance_types": "AllowedInstanceTypes",
        "local_storage": "LocalStorage",
        "cpu_manufacturers": "CpuManufacturers",
        "network_bandwidth_gbps": "NetworkBandwidthGbps",
        "accelerator_count": "AcceleratorCount",
        "bare_metal": "BareMetal",
        "require_hibernate_support": "RequireHibernateSupport",
        "max_spot_price_as_percentage_of_optimal_on_demand_price": "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice",
        "spot_max_price_percentage_over_lowest_price": "SpotMaxPricePercentageOverLowestPrice",
        "baseline_ebs_bandwidth_mbps": "BaselineEbsBandwidthMbps",
        "on_demand_max_price_percentage_over_lowest_price": "OnDemandMaxPricePercentageOverLowestPrice",
        "accelerator_names": "AcceleratorNames",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "burstable_performance": "BurstablePerformance",
        "memory_mi_b": "MemoryMiB",
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    local_storage_types: Optional[Union[list[str], Ref]] = None
    instance_generations: Optional[Union[list[str], Ref]] = None
    network_interface_count: Optional[NetworkInterfaceCountRequest] = None
    memory_gi_b_per_v_cpu: Optional[MemoryGiBPerVCpuRequest] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    v_cpu_count: Optional[VCpuCountRangeRequest] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    accelerator_manufacturers: Optional[Union[list[str], Ref]] = None
    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    local_storage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu_manufacturers: Optional[Union[list[str], Ref]] = None
    network_bandwidth_gbps: Optional[NetworkBandwidthGbpsRequest] = None
    accelerator_count: Optional[AcceleratorCountRequest] = None
    bare_metal: Optional[Union[str, Ref, GetAtt, Sub]] = None
    require_hibernate_support: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spot_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, Ref, GetAtt, Sub]] = None
    accelerator_names: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiBRequest] = None
    burstable_performance: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_mi_b: Optional[MemoryMiBRequest] = None
    total_local_storage_gb: Optional[TotalLocalStorageGBRequest] = None


@dataclass
class ManagedInstancesNetworkConfiguration(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None


@dataclass
class ManagedInstancesProvider(PropertyType):
    INFRASTRUCTURE_ROLE_ARN = "InfrastructureRoleArn"
    PROPAGATE_TAGS = "PropagateTags"
    INFRASTRUCTURE_OPTIMIZATION = "InfrastructureOptimization"
    INSTANCE_LAUNCH_TEMPLATE = "InstanceLaunchTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "infrastructure_role_arn": "InfrastructureRoleArn",
        "propagate_tags": "PropagateTags",
        "infrastructure_optimization": "InfrastructureOptimization",
        "instance_launch_template": "InstanceLaunchTemplate",
    }

    infrastructure_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    propagate_tags: Optional[Union[str, Ref, GetAtt, Sub]] = None
    infrastructure_optimization: Optional[InfrastructureOptimization] = None
    instance_launch_template: Optional[InstanceLaunchTemplate] = None


@dataclass
class ManagedInstancesStorageConfiguration(PropertyType):
    STORAGE_SIZE_GI_B = "StorageSizeGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_size_gi_b": "StorageSizeGiB",
    }

    storage_size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedScaling(PropertyType):
    STATUS = "Status"
    MINIMUM_SCALING_STEP_SIZE = "MinimumScalingStepSize"
    INSTANCE_WARMUP_PERIOD = "InstanceWarmupPeriod"
    TARGET_CAPACITY = "TargetCapacity"
    MAXIMUM_SCALING_STEP_SIZE = "MaximumScalingStepSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "minimum_scaling_step_size": "MinimumScalingStepSize",
        "instance_warmup_period": "InstanceWarmupPeriod",
        "target_capacity": "TargetCapacity",
        "maximum_scaling_step_size": "MaximumScalingStepSize",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_scaling_step_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_warmup_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_scaling_step_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
class VCpuCountRangeRequest(PropertyType):
    MIN = "Min"
    MAX = "Max"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None

