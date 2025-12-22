"""PropertyTypes for AWS::ECS::Service."""

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
class AdvancedConfiguration(PropertyType):
    TEST_LISTENER_RULE = "TestListenerRule"
    ALTERNATE_TARGET_GROUP_ARN = "AlternateTargetGroupArn"
    PRODUCTION_LISTENER_RULE = "ProductionListenerRule"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "test_listener_rule": "TestListenerRule",
        "alternate_target_group_arn": "AlternateTargetGroupArn",
        "production_listener_rule": "ProductionListenerRule",
        "role_arn": "RoleArn",
    }

    test_listener_rule: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alternate_target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    production_listener_rule: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsVpcConfiguration(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"
    ASSIGN_PUBLIC_IP = "AssignPublicIp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
        "assign_public_ip": "AssignPublicIp",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None
    assign_public_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CanaryConfiguration(PropertyType):
    CANARY_PERCENT = "CanaryPercent"
    CANARY_BAKE_TIME_IN_MINUTES = "CanaryBakeTimeInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canary_percent": "CanaryPercent",
        "canary_bake_time_in_minutes": "CanaryBakeTimeInMinutes",
    }

    canary_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None
    canary_bake_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    CAPACITY_PROVIDER = "CapacityProvider"
    BASE = "Base"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "base": "Base",
        "weight": "Weight",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentAlarms(PropertyType):
    ALARM_NAMES = "AlarmNames"
    ENABLE = "Enable"
    ROLLBACK = "Rollback"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_names": "AlarmNames",
        "enable": "Enable",
        "rollback": "Rollback",
    }

    alarm_names: Optional[Union[list[str], Ref]] = None
    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rollback: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentCircuitBreaker(PropertyType):
    ENABLE = "Enable"
    ROLLBACK = "Rollback"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable": "Enable",
        "rollback": "Rollback",
    }

    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rollback: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfiguration(PropertyType):
    CANARY_CONFIGURATION = "CanaryConfiguration"
    BAKE_TIME_IN_MINUTES = "BakeTimeInMinutes"
    LIFECYCLE_HOOKS = "LifecycleHooks"
    ALARMS = "Alarms"
    STRATEGY = "Strategy"
    DEPLOYMENT_CIRCUIT_BREAKER = "DeploymentCircuitBreaker"
    MAXIMUM_PERCENT = "MaximumPercent"
    MINIMUM_HEALTHY_PERCENT = "MinimumHealthyPercent"
    LINEAR_CONFIGURATION = "LinearConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canary_configuration": "CanaryConfiguration",
        "bake_time_in_minutes": "BakeTimeInMinutes",
        "lifecycle_hooks": "LifecycleHooks",
        "alarms": "Alarms",
        "strategy": "Strategy",
        "deployment_circuit_breaker": "DeploymentCircuitBreaker",
        "maximum_percent": "MaximumPercent",
        "minimum_healthy_percent": "MinimumHealthyPercent",
        "linear_configuration": "LinearConfiguration",
    }

    canary_configuration: Optional[CanaryConfiguration] = None
    bake_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lifecycle_hooks: Optional[list[DeploymentLifecycleHook]] = None
    alarms: Optional[DeploymentAlarms] = None
    strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deployment_circuit_breaker: Optional[DeploymentCircuitBreaker] = None
    maximum_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_healthy_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    linear_configuration: Optional[LinearConfiguration] = None


@dataclass
class DeploymentController(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentLifecycleHook(PropertyType):
    LIFECYCLE_STAGES = "LifecycleStages"
    HOOK_TARGET_ARN = "HookTargetArn"
    HOOK_DETAILS = "HookDetails"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle_stages": "LifecycleStages",
        "hook_target_arn": "HookTargetArn",
        "hook_details": "HookDetails",
        "role_arn": "RoleArn",
    }

    lifecycle_stages: Optional[Union[list[str], Ref]] = None
    hook_target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hook_details: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EBSTagSpecification(PropertyType):
    PROPAGATE_TAGS = "PropagateTags"
    RESOURCE_TYPE = "ResourceType"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "propagate_tags": "PropagateTags",
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    propagate_tags: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class ForceNewDeployment(PropertyType):
    ENABLE_FORCE_NEW_DEPLOYMENT = "EnableForceNewDeployment"
    FORCE_NEW_DEPLOYMENT_NONCE = "ForceNewDeploymentNonce"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_force_new_deployment": "EnableForceNewDeployment",
        "force_new_deployment_nonce": "ForceNewDeploymentNonce",
    }

    enable_force_new_deployment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    force_new_deployment_nonce: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LinearConfiguration(PropertyType):
    STEP_BAKE_TIME_IN_MINUTES = "StepBakeTimeInMinutes"
    STEP_PERCENT = "StepPercent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "step_bake_time_in_minutes": "StepBakeTimeInMinutes",
        "step_percent": "StepPercent",
    }

    step_bake_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    step_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LoadBalancer(PropertyType):
    TARGET_GROUP_ARN = "TargetGroupArn"
    LOAD_BALANCER_NAME = "LoadBalancerName"
    CONTAINER_NAME = "ContainerName"
    CONTAINER_PORT = "ContainerPort"
    ADVANCED_CONFIGURATION = "AdvancedConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_arn": "TargetGroupArn",
        "load_balancer_name": "LoadBalancerName",
        "container_name": "ContainerName",
        "container_port": "ContainerPort",
        "advanced_configuration": "AdvancedConfiguration",
    }

    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    advanced_configuration: Optional[AdvancedConfiguration] = None


@dataclass
class LogConfiguration(PropertyType):
    SECRET_OPTIONS = "SecretOptions"
    OPTIONS = "Options"
    LOG_DRIVER = "LogDriver"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_options": "SecretOptions",
        "options": "Options",
        "log_driver": "LogDriver",
    }

    secret_options: Optional[list[Secret]] = None
    options: Optional[dict[str, str]] = None
    log_driver: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    AWSVPC_CONFIGURATION = "AwsvpcConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "awsvpc_configuration": "AwsvpcConfiguration",
    }

    awsvpc_configuration: Optional[AwsVpcConfiguration] = None


@dataclass
class PlacementConstraint(PropertyType):
    TYPE = "Type"
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "expression": "Expression",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PlacementStrategy(PropertyType):
    FIELD = "Field"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "type_": "Type",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Secret(PropertyType):
    VALUE_FROM = "ValueFrom"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_from": "ValueFrom",
        "name": "Name",
    }

    value_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectAccessLogConfiguration(PropertyType):
    FORMAT = "Format"
    INCLUDE_QUERY_PARAMETERS = "IncludeQueryParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "include_query_parameters": "IncludeQueryParameters",
    }

    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_query_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectClientAlias(PropertyType):
    DNS_NAME = "DnsName"
    TEST_TRAFFIC_RULES = "TestTrafficRules"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DnsName",
        "test_traffic_rules": "TestTrafficRules",
        "port": "Port",
    }

    dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    test_traffic_rules: Optional[ServiceConnectTestTrafficRules] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectConfiguration(PropertyType):
    SERVICES = "Services"
    ACCESS_LOG_CONFIGURATION = "AccessLogConfiguration"
    ENABLED = "Enabled"
    LOG_CONFIGURATION = "LogConfiguration"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "services": "Services",
        "access_log_configuration": "AccessLogConfiguration",
        "enabled": "Enabled",
        "log_configuration": "LogConfiguration",
        "namespace": "Namespace",
    }

    services: Optional[list[ServiceConnectService]] = None
    access_log_configuration: Optional[ServiceConnectAccessLogConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_configuration: Optional[LogConfiguration] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectService(PropertyType):
    TIMEOUT = "Timeout"
    INGRESS_PORT_OVERRIDE = "IngressPortOverride"
    CLIENT_ALIASES = "ClientAliases"
    TLS = "Tls"
    DISCOVERY_NAME = "DiscoveryName"
    PORT_NAME = "PortName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout": "Timeout",
        "ingress_port_override": "IngressPortOverride",
        "client_aliases": "ClientAliases",
        "tls": "Tls",
        "discovery_name": "DiscoveryName",
        "port_name": "PortName",
    }

    timeout: Optional[TimeoutConfiguration] = None
    ingress_port_override: Optional[Union[int, Ref, GetAtt, Sub]] = None
    client_aliases: Optional[list[ServiceConnectClientAlias]] = None
    tls: Optional[ServiceConnectTlsConfiguration] = None
    discovery_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTestTrafficRules(PropertyType):
    HEADER = "Header"

    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
    }

    header: Optional[ServiceConnectTestTrafficRulesHeader] = None


@dataclass
class ServiceConnectTestTrafficRulesHeader(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[ServiceConnectTestTrafficRulesHeaderValue] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTestTrafficRulesHeaderValue(PropertyType):
    EXACT = "Exact"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTlsCertificateAuthority(PropertyType):
    AWS_PCA_AUTHORITY_ARN = "AwsPcaAuthorityArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_pca_authority_arn": "AwsPcaAuthorityArn",
    }

    aws_pca_authority_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTlsConfiguration(PropertyType):
    ISSUER_CERTIFICATE_AUTHORITY = "IssuerCertificateAuthority"
    KMS_KEY = "KmsKey"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "issuer_certificate_authority": "IssuerCertificateAuthority",
        "kms_key": "KmsKey",
        "role_arn": "RoleArn",
    }

    issuer_certificate_authority: Optional[ServiceConnectTlsCertificateAuthority] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceManagedEBSVolumeConfiguration(PropertyType):
    SNAPSHOT_ID = "SnapshotId"
    VOLUME_TYPE = "VolumeType"
    KMS_KEY_ID = "KmsKeyId"
    TAG_SPECIFICATIONS = "TagSpecifications"
    FILESYSTEM_TYPE = "FilesystemType"
    ENCRYPTED = "Encrypted"
    THROUGHPUT = "Throughput"
    VOLUME_INITIALIZATION_RATE = "VolumeInitializationRate"
    IOPS = "Iops"
    SIZE_IN_GI_B = "SizeInGiB"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "tag_specifications": "TagSpecifications",
        "filesystem_type": "FilesystemType",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "volume_initialization_rate": "VolumeInitializationRate",
        "iops": "Iops",
        "size_in_gi_b": "SizeInGiB",
        "role_arn": "RoleArn",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_specifications: Optional[list[EBSTagSpecification]] = None
    filesystem_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_initialization_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceRegistry(PropertyType):
    CONTAINER_NAME = "ContainerName"
    PORT = "Port"
    CONTAINER_PORT = "ContainerPort"
    REGISTRY_ARN = "RegistryArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "port": "Port",
        "container_port": "ContainerPort",
        "registry_arn": "RegistryArn",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    registry_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceVolumeConfiguration(PropertyType):
    MANAGED_EBS_VOLUME = "ManagedEBSVolume"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_ebs_volume": "ManagedEBSVolume",
        "name": "Name",
    }

    managed_ebs_volume: Optional[ServiceManagedEBSVolumeConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeoutConfiguration(PropertyType):
    PER_REQUEST_TIMEOUT_SECONDS = "PerRequestTimeoutSeconds"
    IDLE_TIMEOUT_SECONDS = "IdleTimeoutSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request_timeout_seconds": "PerRequestTimeoutSeconds",
        "idle_timeout_seconds": "IdleTimeoutSeconds",
    }

    per_request_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    idle_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcLatticeConfiguration(PropertyType):
    TARGET_GROUP_ARN = "TargetGroupArn"
    PORT_NAME = "PortName"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_arn": "TargetGroupArn",
        "port_name": "PortName",
        "role_arn": "RoleArn",
    }

    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

