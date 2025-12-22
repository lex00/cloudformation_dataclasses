"""PropertyTypes for AWS::ECS::ExpressGatewayService."""

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
class AutoScalingArns(PropertyType):
    SCALABLE_TARGET = "ScalableTarget"
    APPLICATION_AUTO_SCALING_POLICIES = "ApplicationAutoScalingPolicies"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scalable_target": "ScalableTarget",
        "application_auto_scaling_policies": "ApplicationAutoScalingPolicies",
    }

    scalable_target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_auto_scaling_policies: Optional[Union[list[str], Ref]] = None


@dataclass
class ECSManagedResourceArns(PropertyType):
    LOG_GROUPS = "LogGroups"
    SERVICE_SECURITY_GROUPS = "ServiceSecurityGroups"
    METRIC_ALARMS = "MetricAlarms"
    INGRESS_PATH = "IngressPath"
    AUTO_SCALING = "AutoScaling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_groups": "LogGroups",
        "service_security_groups": "ServiceSecurityGroups",
        "metric_alarms": "MetricAlarms",
        "ingress_path": "IngressPath",
        "auto_scaling": "AutoScaling",
    }

    log_groups: Optional[Union[list[str], Ref]] = None
    service_security_groups: Optional[Union[list[str], Ref]] = None
    metric_alarms: Optional[Union[list[str], Ref]] = None
    ingress_path: Optional[IngressPathArns] = None
    auto_scaling: Optional[AutoScalingArns] = None


@dataclass
class ExpressGatewayContainer(PropertyType):
    REPOSITORY_CREDENTIALS = "RepositoryCredentials"
    SECRETS = "Secrets"
    COMMAND = "Command"
    AWS_LOGS_CONFIGURATION = "AwsLogsConfiguration"
    CONTAINER_PORT = "ContainerPort"
    ENVIRONMENT = "Environment"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_credentials": "RepositoryCredentials",
        "secrets": "Secrets",
        "command": "Command",
        "aws_logs_configuration": "AwsLogsConfiguration",
        "container_port": "ContainerPort",
        "environment": "Environment",
        "image": "Image",
    }

    repository_credentials: Optional[ExpressGatewayRepositoryCredentials] = None
    secrets: Optional[list[Secret]] = None
    command: Optional[Union[list[str], Ref]] = None
    aws_logs_configuration: Optional[ExpressGatewayServiceAwsLogsConfiguration] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    environment: Optional[list[KeyValuePair]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayRepositoryCredentials(PropertyType):
    CREDENTIALS_PARAMETER = "CredentialsParameter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credentials_parameter": "CredentialsParameter",
    }

    credentials_parameter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayScalingTarget(PropertyType):
    MIN_TASK_COUNT = "MinTaskCount"
    AUTO_SCALING_METRIC = "AutoScalingMetric"
    AUTO_SCALING_TARGET_VALUE = "AutoScalingTargetValue"
    MAX_TASK_COUNT = "MaxTaskCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_task_count": "MinTaskCount",
        "auto_scaling_metric": "AutoScalingMetric",
        "auto_scaling_target_value": "AutoScalingTargetValue",
        "max_task_count": "MaxTaskCount",
    }

    min_task_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_scaling_metric: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_scaling_target_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_task_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayServiceAwsLogsConfiguration(PropertyType):
    LOG_STREAM_PREFIX = "LogStreamPrefix"
    LOG_GROUP = "LogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_prefix": "LogStreamPrefix",
        "log_group": "LogGroup",
    }

    log_stream_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayServiceConfiguration(PropertyType):
    SERVICE_REVISION_ARN = "ServiceRevisionArn"
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    TASK_ROLE_ARN = "TaskRoleArn"
    SCALING_TARGET = "ScalingTarget"
    INGRESS_PATHS = "IngressPaths"
    PRIMARY_CONTAINER = "PrimaryContainer"
    MEMORY = "Memory"
    HEALTH_CHECK_PATH = "HealthCheckPath"
    CREATED_AT = "CreatedAt"
    CPU = "Cpu"
    NETWORK_CONFIGURATION = "NetworkConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_revision_arn": "ServiceRevisionArn",
        "execution_role_arn": "ExecutionRoleArn",
        "task_role_arn": "TaskRoleArn",
        "scaling_target": "ScalingTarget",
        "ingress_paths": "IngressPaths",
        "primary_container": "PrimaryContainer",
        "memory": "Memory",
        "health_check_path": "HealthCheckPath",
        "created_at": "CreatedAt",
        "cpu": "Cpu",
        "network_configuration": "NetworkConfiguration",
    }

    service_revision_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scaling_target: Optional[ExpressGatewayScalingTarget] = None
    ingress_paths: Optional[list[IngressPathSummary]] = None
    primary_container: Optional[ExpressGatewayContainer] = None
    memory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    health_check_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_configuration: Optional[ExpressGatewayServiceNetworkConfiguration] = None


@dataclass
class ExpressGatewayServiceNetworkConfiguration(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None


@dataclass
class ExpressGatewayServiceStatus(PropertyType):
    STATUS_CODE = "StatusCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status_code": "StatusCode",
    }

    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressPathArns(PropertyType):
    LISTENER_ARN = "ListenerArn"
    LOAD_BALANCER_ARN = "LoadBalancerArn"
    TARGET_GROUP_ARNS = "TargetGroupArns"
    LISTENER_RULE_ARN = "ListenerRuleArn"
    LOAD_BALANCER_SECURITY_GROUPS = "LoadBalancerSecurityGroups"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "listener_arn": "ListenerArn",
        "load_balancer_arn": "LoadBalancerArn",
        "target_group_arns": "TargetGroupArns",
        "listener_rule_arn": "ListenerRuleArn",
        "load_balancer_security_groups": "LoadBalancerSecurityGroups",
        "certificate_arn": "CertificateArn",
    }

    listener_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_group_arns: Optional[Union[list[str], Ref]] = None
    listener_rule_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_security_groups: Optional[Union[list[str], Ref]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressPathSummary(PropertyType):
    ENDPOINT = "Endpoint"
    ACCESS_TYPE = "AccessType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "access_type": "AccessType",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValuePair(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

