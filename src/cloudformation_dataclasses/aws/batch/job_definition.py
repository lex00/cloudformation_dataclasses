"""PropertyTypes for AWS::Batch::JobDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ArrayJobDependency:
    """ArrayJobDependency enum values."""

    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEState:
    """CEState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEStatus:
    """CEStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class CEType:
    """CEType enum values."""

    MANAGED = "MANAGED"
    UNMANAGED = "UNMANAGED"


class CRAllocationStrategy:
    """CRAllocationStrategy enum values."""

    BEST_FIT = "BEST_FIT"
    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"


class CRType:
    """CRType enum values."""

    EC2 = "EC2"
    SPOT = "SPOT"
    FARGATE = "FARGATE"
    FARGATE_SPOT = "FARGATE_SPOT"


class CRUpdateAllocationStrategy:
    """CRUpdateAllocationStrategy enum values."""

    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"


class DeviceCgroupPermission:
    """DeviceCgroupPermission enum values."""

    READ = "READ"
    WRITE = "WRITE"
    MKNOD = "MKNOD"


class EFSAuthorizationConfigIAM:
    """EFSAuthorizationConfigIAM enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EFSTransitEncryption:
    """EFSTransitEncryption enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FirelensConfigurationType:
    """FirelensConfigurationType enum values."""

    FLUENTD = "fluentd"
    FLUENTBIT = "fluentbit"


class JQState:
    """JQState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class JQStatus:
    """JQStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class JobDefinitionType:
    """JobDefinitionType enum values."""

    CONTAINER = "container"
    MULTINODE = "multinode"


class JobQueueType:
    """JobQueueType enum values."""

    EKS = "EKS"
    ECS = "ECS"
    ECS_FARGATE = "ECS_FARGATE"
    SAGEMAKER_TRAINING = "SAGEMAKER_TRAINING"


class JobStateTimeLimitActionsAction:
    """JobStateTimeLimitActionsAction enum values."""

    CANCEL = "CANCEL"
    TERMINATE = "TERMINATE"


class JobStateTimeLimitActionsState:
    """JobStateTimeLimitActionsState enum values."""

    RUNNABLE = "RUNNABLE"


class JobStatus:
    """JobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    RUNNABLE = "RUNNABLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


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


class OrchestrationType:
    """OrchestrationType enum values."""

    ECS = "ECS"
    EKS = "EKS"


class PlatformCapability:
    """PlatformCapability enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"


class ResourceType:
    """ResourceType enum values."""

    GPU = "GPU"
    VCPU = "VCPU"
    MEMORY = "MEMORY"


class RetryAction:
    """RetryAction enum values."""

    RETRY = "RETRY"
    EXIT = "EXIT"


class ServiceEnvironmentState:
    """ServiceEnvironmentState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ServiceEnvironmentStatus:
    """ServiceEnvironmentStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class ServiceEnvironmentType:
    """ServiceEnvironmentType enum values."""

    SAGEMAKER_TRAINING = "SAGEMAKER_TRAINING"


class ServiceJobRetryAction:
    """ServiceJobRetryAction enum values."""

    RETRY = "RETRY"
    EXIT = "EXIT"


class ServiceJobStatus:
    """ServiceJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    RUNNABLE = "RUNNABLE"
    SCHEDULED = "SCHEDULED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class ServiceJobType:
    """ServiceJobType enum values."""

    SAGEMAKER_TRAINING = "SAGEMAKER_TRAINING"


class ServiceResourceIdName:
    """ServiceResourceIdName enum values."""

    TRAININGJOBARN = "TrainingJobArn"


class UserdataType:
    """UserdataType enum values."""

    EKS_BOOTSTRAP_SH = "EKS_BOOTSTRAP_SH"
    EKS_NODEADM = "EKS_NODEADM"


@dataclass
class ConsumableResourceProperties(PropertyType):
    CONSUMABLE_RESOURCE_LIST = "ConsumableResourceList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumable_resource_list": "ConsumableResourceList",
    }

    consumable_resource_list: Optional[list[ConsumableResourceRequirement]] = None


@dataclass
class ConsumableResourceRequirement(PropertyType):
    CONSUMABLE_RESOURCE = "ConsumableResource"
    QUANTITY = "Quantity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumable_resource": "ConsumableResource",
        "quantity": "Quantity",
    }

    consumable_resource: Optional[Union[str, Ref, GetAtt, Sub]] = None
    quantity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerProperties(PropertyType):
    REPOSITORY_CREDENTIALS = "RepositoryCredentials"
    USER = "User"
    SECRETS = "Secrets"
    MEMORY = "Memory"
    PRIVILEGED = "Privileged"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    LINUX_PARAMETERS = "LinuxParameters"
    FARGATE_PLATFORM_CONFIGURATION = "FargatePlatformConfiguration"
    JOB_ROLE_ARN = "JobRoleArn"
    READONLY_ROOT_FILESYSTEM = "ReadonlyRootFilesystem"
    VCPUS = "Vcpus"
    IMAGE = "Image"
    RESOURCE_REQUIREMENTS = "ResourceRequirements"
    LOG_CONFIGURATION = "LogConfiguration"
    MOUNT_POINTS = "MountPoints"
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    RUNTIME_PLATFORM = "RuntimePlatform"
    VOLUMES = "Volumes"
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    ULIMITS = "Ulimits"
    NETWORK_CONFIGURATION = "NetworkConfiguration"
    EPHEMERAL_STORAGE = "EphemeralStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_credentials": "RepositoryCredentials",
        "user": "User",
        "secrets": "Secrets",
        "memory": "Memory",
        "privileged": "Privileged",
        "enable_execute_command": "EnableExecuteCommand",
        "linux_parameters": "LinuxParameters",
        "fargate_platform_configuration": "FargatePlatformConfiguration",
        "job_role_arn": "JobRoleArn",
        "readonly_root_filesystem": "ReadonlyRootFilesystem",
        "vcpus": "Vcpus",
        "image": "Image",
        "resource_requirements": "ResourceRequirements",
        "log_configuration": "LogConfiguration",
        "mount_points": "MountPoints",
        "execution_role_arn": "ExecutionRoleArn",
        "runtime_platform": "RuntimePlatform",
        "volumes": "Volumes",
        "command": "Command",
        "environment": "Environment",
        "ulimits": "Ulimits",
        "network_configuration": "NetworkConfiguration",
        "ephemeral_storage": "EphemeralStorage",
    }

    repository_credentials: Optional[RepositoryCredentials] = None
    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets: Optional[list[Secret]] = None
    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    privileged: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    linux_parameters: Optional[LinuxParameters] = None
    fargate_platform_configuration: Optional[FargatePlatformConfiguration] = None
    job_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    readonly_root_filesystem: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    vcpus: Optional[Union[int, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_requirements: Optional[list[ResourceRequirement]] = None
    log_configuration: Optional[LogConfiguration] = None
    mount_points: Optional[list[MountPoint]] = None
    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_platform: Optional[RuntimePlatform] = None
    volumes: Optional[list[Volume]] = None
    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[Environment]] = None
    ulimits: Optional[list[Ulimit]] = None
    network_configuration: Optional[NetworkConfiguration] = None
    ephemeral_storage: Optional[EphemeralStorage] = None


@dataclass
class Device(PropertyType):
    HOST_PATH = "HostPath"
    PERMISSIONS = "Permissions"
    CONTAINER_PATH = "ContainerPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "host_path": "HostPath",
        "permissions": "Permissions",
        "container_path": "ContainerPath",
    }

    host_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    permissions: Optional[Union[list[str], Ref]] = None
    container_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EFSAuthorizationConfig(PropertyType):
    IAM = "Iam"
    ACCESS_POINT_ID = "AccessPointId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
        "access_point_id": "AccessPointId",
    }

    iam: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_point_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EFSVolumeConfiguration(PropertyType):
    TRANSIT_ENCRYPTION = "TransitEncryption"
    AUTHORIZATION_CONFIG = "AuthorizationConfig"
    FILE_SYSTEM_ID = "FileSystemId"
    ROOT_DIRECTORY = "RootDirectory"
    TRANSIT_ENCRYPTION_PORT = "TransitEncryptionPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transit_encryption": "TransitEncryption",
        "authorization_config": "AuthorizationConfig",
        "file_system_id": "FileSystemId",
        "root_directory": "RootDirectory",
        "transit_encryption_port": "TransitEncryptionPort",
    }

    transit_encryption: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_config: Optional[EFSAuthorizationConfig] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    root_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transit_encryption_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EcsProperties(PropertyType):
    TASK_PROPERTIES = "TaskProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "task_properties": "TaskProperties",
    }

    task_properties: Optional[list[EcsTaskProperties]] = None


@dataclass
class EcsTaskProperties(PropertyType):
    PLATFORM_VERSION = "PlatformVersion"
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    RUNTIME_PLATFORM = "RuntimePlatform"
    TASK_ROLE_ARN = "TaskRoleArn"
    IPC_MODE = "IpcMode"
    VOLUMES = "Volumes"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    CONTAINERS = "Containers"
    NETWORK_CONFIGURATION = "NetworkConfiguration"
    PID_MODE = "PidMode"
    EPHEMERAL_STORAGE = "EphemeralStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "platform_version": "PlatformVersion",
        "execution_role_arn": "ExecutionRoleArn",
        "runtime_platform": "RuntimePlatform",
        "task_role_arn": "TaskRoleArn",
        "ipc_mode": "IpcMode",
        "volumes": "Volumes",
        "enable_execute_command": "EnableExecuteCommand",
        "containers": "Containers",
        "network_configuration": "NetworkConfiguration",
        "pid_mode": "PidMode",
        "ephemeral_storage": "EphemeralStorage",
    }

    platform_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_platform: Optional[RuntimePlatform] = None
    task_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipc_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volumes: Optional[list[Volume]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    containers: Optional[list[TaskContainerProperties]] = None
    network_configuration: Optional[NetworkConfiguration] = None
    pid_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ephemeral_storage: Optional[EphemeralStorage] = None


@dataclass
class EksContainer(PropertyType):
    ARGS = "Args"
    VOLUME_MOUNTS = "VolumeMounts"
    IMAGE_PULL_POLICY = "ImagePullPolicy"
    COMMAND = "Command"
    SECURITY_CONTEXT = "SecurityContext"
    RESOURCES = "Resources"
    IMAGE = "Image"
    ENV = "Env"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "args": "Args",
        "volume_mounts": "VolumeMounts",
        "image_pull_policy": "ImagePullPolicy",
        "command": "Command",
        "security_context": "SecurityContext",
        "resources": "Resources",
        "image": "Image",
        "env": "Env",
        "name": "Name",
    }

    args: Optional[Union[list[str], Ref]] = None
    volume_mounts: Optional[list[EksContainerVolumeMount]] = None
    image_pull_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    command: Optional[Union[list[str], Ref]] = None
    security_context: Optional[EksContainerSecurityContext] = None
    resources: Optional[EksContainerResourceRequirements] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    env: Optional[list[EksContainerEnvironmentVariable]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksContainerEnvironmentVariable(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksContainerResourceRequirements(PropertyType):
    LIMITS = "Limits"
    REQUESTS = "Requests"

    _property_mappings: ClassVar[dict[str, str]] = {
        "limits": "Limits",
        "requests": "Requests",
    }

    limits: Optional[dict[str, str]] = None
    requests: Optional[dict[str, str]] = None


@dataclass
class EksContainerSecurityContext(PropertyType):
    RUN_AS_USER = "RunAsUser"
    ALLOW_PRIVILEGE_ESCALATION = "AllowPrivilegeEscalation"
    RUN_AS_NON_ROOT = "RunAsNonRoot"
    PRIVILEGED = "Privileged"
    READ_ONLY_ROOT_FILESYSTEM = "ReadOnlyRootFilesystem"
    RUN_AS_GROUP = "RunAsGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "run_as_user": "RunAsUser",
        "allow_privilege_escalation": "AllowPrivilegeEscalation",
        "run_as_non_root": "RunAsNonRoot",
        "privileged": "Privileged",
        "read_only_root_filesystem": "ReadOnlyRootFilesystem",
        "run_as_group": "RunAsGroup",
    }

    run_as_user: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allow_privilege_escalation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    run_as_non_root: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    privileged: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    read_only_root_filesystem: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    run_as_group: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EksContainerVolumeMount(PropertyType):
    MOUNT_PATH = "MountPath"
    READ_ONLY = "ReadOnly"
    SUB_PATH = "SubPath"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_path": "MountPath",
        "read_only": "ReadOnly",
        "sub_path": "SubPath",
        "name": "Name",
    }

    mount_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sub_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksEmptyDir(PropertyType):
    MEDIUM = "Medium"
    SIZE_LIMIT = "SizeLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "medium": "Medium",
        "size_limit": "SizeLimit",
    }

    medium: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_limit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksHostPath(PropertyType):
    PATH = "Path"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksMetadata(PropertyType):
    ANNOTATIONS = "Annotations"
    LABELS = "Labels"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "annotations": "Annotations",
        "labels": "Labels",
        "namespace": "Namespace",
    }

    annotations: Optional[dict[str, str]] = None
    labels: Optional[dict[str, str]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksPersistentVolumeClaim(PropertyType):
    READ_ONLY = "ReadOnly"
    CLAIM_NAME = "ClaimName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only": "ReadOnly",
        "claim_name": "ClaimName",
    }

    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    claim_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksPodProperties(PropertyType):
    INIT_CONTAINERS = "InitContainers"
    VOLUMES = "Volumes"
    DNS_POLICY = "DnsPolicy"
    CONTAINERS = "Containers"
    METADATA = "Metadata"
    SERVICE_ACCOUNT_NAME = "ServiceAccountName"
    IMAGE_PULL_SECRETS = "ImagePullSecrets"
    HOST_NETWORK = "HostNetwork"
    SHARE_PROCESS_NAMESPACE = "ShareProcessNamespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "init_containers": "InitContainers",
        "volumes": "Volumes",
        "dns_policy": "DnsPolicy",
        "containers": "Containers",
        "metadata": "Metadata",
        "service_account_name": "ServiceAccountName",
        "image_pull_secrets": "ImagePullSecrets",
        "host_network": "HostNetwork",
        "share_process_namespace": "ShareProcessNamespace",
    }

    init_containers: Optional[list[EksContainer]] = None
    volumes: Optional[list[EksVolume]] = None
    dns_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    containers: Optional[list[EksContainer]] = None
    metadata: Optional[EksMetadata] = None
    service_account_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_pull_secrets: Optional[list[ImagePullSecret]] = None
    host_network: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    share_process_namespace: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EksProperties(PropertyType):
    POD_PROPERTIES = "PodProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pod_properties": "PodProperties",
    }

    pod_properties: Optional[EksPodProperties] = None


@dataclass
class EksSecret(PropertyType):
    SECRET_NAME = "SecretName"
    OPTIONAL = "Optional"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
        "optional": "Optional",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    optional: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EksVolume(PropertyType):
    SECRET = "Secret"
    EMPTY_DIR = "EmptyDir"
    HOST_PATH = "HostPath"
    PERSISTENT_VOLUME_CLAIM = "PersistentVolumeClaim"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret": "Secret",
        "empty_dir": "EmptyDir",
        "host_path": "HostPath",
        "persistent_volume_claim": "PersistentVolumeClaim",
        "name": "Name",
    }

    secret: Optional[EksSecret] = None
    empty_dir: Optional[EksEmptyDir] = None
    host_path: Optional[EksHostPath] = None
    persistent_volume_claim: Optional[EksPersistentVolumeClaim] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Environment(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EphemeralStorage(PropertyType):
    SIZE_IN_GI_B = "SizeInGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gi_b": "SizeInGiB",
    }

    size_in_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluateOnExit(PropertyType):
    ACTION = "Action"
    ON_EXIT_CODE = "OnExitCode"
    ON_REASON = "OnReason"
    ON_STATUS_REASON = "OnStatusReason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "on_exit_code": "OnExitCode",
        "on_reason": "OnReason",
        "on_status_reason": "OnStatusReason",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_exit_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_status_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FargatePlatformConfiguration(PropertyType):
    PLATFORM_VERSION = "PlatformVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "platform_version": "PlatformVersion",
    }

    platform_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FirelensConfiguration(PropertyType):
    OPTIONS = "Options"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "type_": "Type",
    }

    options: Optional[dict[str, str]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Host(PropertyType):
    SOURCE_PATH = "SourcePath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImagePullSecret(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JobTimeout(PropertyType):
    ATTEMPT_DURATION_SECONDS = "AttemptDurationSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attempt_duration_seconds": "AttemptDurationSeconds",
    }

    attempt_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LinuxParameters(PropertyType):
    SWAPPINESS = "Swappiness"
    TMPFS = "Tmpfs"
    SHARED_MEMORY_SIZE = "SharedMemorySize"
    DEVICES = "Devices"
    INIT_PROCESS_ENABLED = "InitProcessEnabled"
    MAX_SWAP = "MaxSwap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "swappiness": "Swappiness",
        "tmpfs": "Tmpfs",
        "shared_memory_size": "SharedMemorySize",
        "devices": "Devices",
        "init_process_enabled": "InitProcessEnabled",
        "max_swap": "MaxSwap",
    }

    swappiness: Optional[Union[int, Ref, GetAtt, Sub]] = None
    tmpfs: Optional[list[Tmpfs]] = None
    shared_memory_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    devices: Optional[list[Device]] = None
    init_process_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_swap: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
class MountPoint(PropertyType):
    READ_ONLY = "ReadOnly"
    SOURCE_VOLUME = "SourceVolume"
    CONTAINER_PATH = "ContainerPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only": "ReadOnly",
        "source_volume": "SourceVolume",
        "container_path": "ContainerPath",
    }

    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source_volume: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiNodeContainerProperties(PropertyType):
    REPOSITORY_CREDENTIALS = "RepositoryCredentials"
    USER = "User"
    SECRETS = "Secrets"
    MEMORY = "Memory"
    PRIVILEGED = "Privileged"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    LINUX_PARAMETERS = "LinuxParameters"
    JOB_ROLE_ARN = "JobRoleArn"
    READONLY_ROOT_FILESYSTEM = "ReadonlyRootFilesystem"
    VCPUS = "Vcpus"
    IMAGE = "Image"
    RESOURCE_REQUIREMENTS = "ResourceRequirements"
    LOG_CONFIGURATION = "LogConfiguration"
    MOUNT_POINTS = "MountPoints"
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    RUNTIME_PLATFORM = "RuntimePlatform"
    VOLUMES = "Volumes"
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    ULIMITS = "Ulimits"
    INSTANCE_TYPE = "InstanceType"
    EPHEMERAL_STORAGE = "EphemeralStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_credentials": "RepositoryCredentials",
        "user": "User",
        "secrets": "Secrets",
        "memory": "Memory",
        "privileged": "Privileged",
        "enable_execute_command": "EnableExecuteCommand",
        "linux_parameters": "LinuxParameters",
        "job_role_arn": "JobRoleArn",
        "readonly_root_filesystem": "ReadonlyRootFilesystem",
        "vcpus": "Vcpus",
        "image": "Image",
        "resource_requirements": "ResourceRequirements",
        "log_configuration": "LogConfiguration",
        "mount_points": "MountPoints",
        "execution_role_arn": "ExecutionRoleArn",
        "runtime_platform": "RuntimePlatform",
        "volumes": "Volumes",
        "command": "Command",
        "environment": "Environment",
        "ulimits": "Ulimits",
        "instance_type": "InstanceType",
        "ephemeral_storage": "EphemeralStorage",
    }

    repository_credentials: Optional[RepositoryCredentials] = None
    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets: Optional[list[Secret]] = None
    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    privileged: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    linux_parameters: Optional[LinuxParameters] = None
    job_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    readonly_root_filesystem: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    vcpus: Optional[Union[int, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_requirements: Optional[list[ResourceRequirement]] = None
    log_configuration: Optional[LogConfiguration] = None
    mount_points: Optional[list[MountPoint]] = None
    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_platform: Optional[RuntimePlatform] = None
    volumes: Optional[list[Volume]] = None
    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[Environment]] = None
    ulimits: Optional[list[Ulimit]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ephemeral_storage: Optional[EphemeralStorage] = None


@dataclass
class MultiNodeEcsProperties(PropertyType):
    TASK_PROPERTIES = "TaskProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "task_properties": "TaskProperties",
    }

    task_properties: Optional[list[MultiNodeEcsTaskProperties]] = None


@dataclass
class MultiNodeEcsTaskProperties(PropertyType):
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    TASK_ROLE_ARN = "TaskRoleArn"
    IPC_MODE = "IpcMode"
    VOLUMES = "Volumes"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    CONTAINERS = "Containers"
    PID_MODE = "PidMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role_arn": "ExecutionRoleArn",
        "task_role_arn": "TaskRoleArn",
        "ipc_mode": "IpcMode",
        "volumes": "Volumes",
        "enable_execute_command": "EnableExecuteCommand",
        "containers": "Containers",
        "pid_mode": "PidMode",
    }

    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipc_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volumes: Optional[list[Volume]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    containers: Optional[list[TaskContainerProperties]] = None
    pid_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    ASSIGN_PUBLIC_IP = "AssignPublicIp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "assign_public_ip": "AssignPublicIp",
    }

    assign_public_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NodeProperties(PropertyType):
    MAIN_NODE = "MainNode"
    NODE_RANGE_PROPERTIES = "NodeRangeProperties"
    NUM_NODES = "NumNodes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "main_node": "MainNode",
        "node_range_properties": "NodeRangeProperties",
        "num_nodes": "NumNodes",
    }

    main_node: Optional[Union[int, Ref, GetAtt, Sub]] = None
    node_range_properties: Optional[list[NodeRangeProperty]] = None
    num_nodes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NodeRangeProperty(PropertyType):
    CONTAINER = "Container"
    TARGET_NODES = "TargetNodes"
    ECS_PROPERTIES = "EcsProperties"
    INSTANCE_TYPES = "InstanceTypes"
    EKS_PROPERTIES = "EksProperties"
    CONSUMABLE_RESOURCE_PROPERTIES = "ConsumableResourceProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container": "Container",
        "target_nodes": "TargetNodes",
        "ecs_properties": "EcsProperties",
        "instance_types": "InstanceTypes",
        "eks_properties": "EksProperties",
        "consumable_resource_properties": "ConsumableResourceProperties",
    }

    container: Optional[MultiNodeContainerProperties] = None
    target_nodes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ecs_properties: Optional[MultiNodeEcsProperties] = None
    instance_types: Optional[Union[list[str], Ref]] = None
    eks_properties: Optional[EksProperties] = None
    consumable_resource_properties: Optional[ConsumableResourceProperties] = None


@dataclass
class RepositoryCredentials(PropertyType):
    CREDENTIALS_PARAMETER = "CredentialsParameter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credentials_parameter": "CredentialsParameter",
    }

    credentials_parameter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceRequirement(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceRetentionPolicy(PropertyType):
    SKIP_DEREGISTER_ON_UPDATE = "SkipDeregisterOnUpdate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "skip_deregister_on_update": "SkipDeregisterOnUpdate",
    }

    skip_deregister_on_update: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RetryStrategy(PropertyType):
    EVALUATE_ON_EXIT = "EvaluateOnExit"
    ATTEMPTS = "Attempts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "evaluate_on_exit": "EvaluateOnExit",
        "attempts": "Attempts",
    }

    evaluate_on_exit: Optional[list[EvaluateOnExit]] = None
    attempts: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RuntimePlatform(PropertyType):
    OPERATING_SYSTEM_FAMILY = "OperatingSystemFamily"
    CPU_ARCHITECTURE = "CpuArchitecture"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operating_system_family": "OperatingSystemFamily",
        "cpu_architecture": "CpuArchitecture",
    }

    operating_system_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu_architecture: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class TaskContainerDependency(PropertyType):
    CONDITION = "Condition"
    CONTAINER_NAME = "ContainerName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "container_name": "ContainerName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskContainerProperties(PropertyType):
    REPOSITORY_CREDENTIALS = "RepositoryCredentials"
    USER = "User"
    SECRETS = "Secrets"
    PRIVILEGED = "Privileged"
    LINUX_PARAMETERS = "LinuxParameters"
    READONLY_ROOT_FILESYSTEM = "ReadonlyRootFilesystem"
    IMAGE = "Image"
    LOG_CONFIGURATION = "LogConfiguration"
    ESSENTIAL = "Essential"
    RESOURCE_REQUIREMENTS = "ResourceRequirements"
    NAME = "Name"
    MOUNT_POINTS = "MountPoints"
    FIRELENS_CONFIGURATION = "FirelensConfiguration"
    DEPENDS_ON = "DependsOn"
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    ULIMITS = "Ulimits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_credentials": "RepositoryCredentials",
        "user": "User",
        "secrets": "Secrets",
        "privileged": "Privileged",
        "linux_parameters": "LinuxParameters",
        "readonly_root_filesystem": "ReadonlyRootFilesystem",
        "image": "Image",
        "log_configuration": "LogConfiguration",
        "essential": "Essential",
        "resource_requirements": "ResourceRequirements",
        "name": "Name",
        "mount_points": "MountPoints",
        "firelens_configuration": "FirelensConfiguration",
        "depends_on": "DependsOn",
        "command": "Command",
        "environment": "Environment",
        "ulimits": "Ulimits",
    }

    repository_credentials: Optional[RepositoryCredentials] = None
    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets: Optional[list[Secret]] = None
    privileged: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    linux_parameters: Optional[LinuxParameters] = None
    readonly_root_filesystem: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_configuration: Optional[LogConfiguration] = None
    essential: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    resource_requirements: Optional[list[ResourceRequirement]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mount_points: Optional[list[MountPoint]] = None
    firelens_configuration: Optional[FirelensConfiguration] = None
    depends_on: Optional[list[TaskContainerDependency]] = None
    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[Environment]] = None
    ulimits: Optional[list[Ulimit]] = None


@dataclass
class Tmpfs(PropertyType):
    SIZE = "Size"
    CONTAINER_PATH = "ContainerPath"
    MOUNT_OPTIONS = "MountOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size": "Size",
        "container_path": "ContainerPath",
        "mount_options": "MountOptions",
    }

    size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    container_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mount_options: Optional[Union[list[str], Ref]] = None


@dataclass
class Ulimit(PropertyType):
    SOFT_LIMIT = "SoftLimit"
    HARD_LIMIT = "HardLimit"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "soft_limit": "SoftLimit",
        "hard_limit": "HardLimit",
        "name": "Name",
    }

    soft_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    hard_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Volume(PropertyType):
    HOST = "Host"
    EFS_VOLUME_CONFIGURATION = "EfsVolumeConfiguration"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "host": "Host",
        "efs_volume_configuration": "EfsVolumeConfiguration",
        "name": "Name",
    }

    host: Optional[Host] = None
    efs_volume_configuration: Optional[EFSVolumeConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

