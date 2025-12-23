"""PropertyTypes for AWS::ECS::TaskDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthorizationConfig(PropertyType):
    IAM = "IAM"
    ACCESS_POINT_ID = "AccessPointId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "IAM",
        "access_point_id": "AccessPointId",
    }

    iam: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_point_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerDefinition(PropertyType):
    USER = "User"
    SECRETS = "Secrets"
    MEMORY = "Memory"
    PRIVILEGED = "Privileged"
    HEALTH_CHECK = "HealthCheck"
    START_TIMEOUT = "StartTimeout"
    VOLUMES_FROM = "VolumesFrom"
    CPU = "Cpu"
    ENTRY_POINT = "EntryPoint"
    DNS_SERVERS = "DnsServers"
    READONLY_ROOT_FILESYSTEM = "ReadonlyRootFilesystem"
    IMAGE = "Image"
    ESSENTIAL = "Essential"
    LOG_CONFIGURATION = "LogConfiguration"
    RESOURCE_REQUIREMENTS = "ResourceRequirements"
    ENVIRONMENT_FILES = "EnvironmentFiles"
    NAME = "Name"
    FIRELENS_CONFIGURATION = "FirelensConfiguration"
    DOCKER_SECURITY_OPTIONS = "DockerSecurityOptions"
    SYSTEM_CONTROLS = "SystemControls"
    INTERACTIVE = "Interactive"
    DNS_SEARCH_DOMAINS = "DnsSearchDomains"
    CREDENTIAL_SPECS = "CredentialSpecs"
    ULIMITS = "Ulimits"
    STOP_TIMEOUT = "StopTimeout"
    WORKING_DIRECTORY = "WorkingDirectory"
    MEMORY_RESERVATION = "MemoryReservation"
    REPOSITORY_CREDENTIALS = "RepositoryCredentials"
    EXTRA_HOSTS = "ExtraHosts"
    HOSTNAME = "Hostname"
    LINUX_PARAMETERS = "LinuxParameters"
    VERSION_CONSISTENCY = "VersionConsistency"
    RESTART_POLICY = "RestartPolicy"
    DISABLE_NETWORKING = "DisableNetworking"
    PSEUDO_TERMINAL = "PseudoTerminal"
    MOUNT_POINTS = "MountPoints"
    DEPENDS_ON = "DependsOn"
    DOCKER_LABELS = "DockerLabels"
    PORT_MAPPINGS = "PortMappings"
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    LINKS = "Links"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user": "User",
        "secrets": "Secrets",
        "memory": "Memory",
        "privileged": "Privileged",
        "health_check": "HealthCheck",
        "start_timeout": "StartTimeout",
        "volumes_from": "VolumesFrom",
        "cpu": "Cpu",
        "entry_point": "EntryPoint",
        "dns_servers": "DnsServers",
        "readonly_root_filesystem": "ReadonlyRootFilesystem",
        "image": "Image",
        "essential": "Essential",
        "log_configuration": "LogConfiguration",
        "resource_requirements": "ResourceRequirements",
        "environment_files": "EnvironmentFiles",
        "name": "Name",
        "firelens_configuration": "FirelensConfiguration",
        "docker_security_options": "DockerSecurityOptions",
        "system_controls": "SystemControls",
        "interactive": "Interactive",
        "dns_search_domains": "DnsSearchDomains",
        "credential_specs": "CredentialSpecs",
        "ulimits": "Ulimits",
        "stop_timeout": "StopTimeout",
        "working_directory": "WorkingDirectory",
        "memory_reservation": "MemoryReservation",
        "repository_credentials": "RepositoryCredentials",
        "extra_hosts": "ExtraHosts",
        "hostname": "Hostname",
        "linux_parameters": "LinuxParameters",
        "version_consistency": "VersionConsistency",
        "restart_policy": "RestartPolicy",
        "disable_networking": "DisableNetworking",
        "pseudo_terminal": "PseudoTerminal",
        "mount_points": "MountPoints",
        "depends_on": "DependsOn",
        "docker_labels": "DockerLabels",
        "port_mappings": "PortMappings",
        "command": "Command",
        "environment": "Environment",
        "links": "Links",
    }

    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets: Optional[list[Secret]] = None
    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    privileged: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    health_check: Optional[HealthCheck] = None
    start_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volumes_from: Optional[list[VolumeFrom]] = None
    cpu: Optional[Union[int, Ref, GetAtt, Sub]] = None
    entry_point: Optional[Union[list[str], Ref]] = None
    dns_servers: Optional[Union[list[str], Ref]] = None
    readonly_root_filesystem: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    essential: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_configuration: Optional[LogConfiguration] = None
    resource_requirements: Optional[list[ResourceRequirement]] = None
    environment_files: Optional[list[EnvironmentFile]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    firelens_configuration: Optional[FirelensConfiguration] = None
    docker_security_options: Optional[Union[list[str], Ref]] = None
    system_controls: Optional[list[SystemControl]] = None
    interactive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dns_search_domains: Optional[Union[list[str], Ref]] = None
    credential_specs: Optional[Union[list[str], Ref]] = None
    ulimits: Optional[list[Ulimit]] = None
    stop_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    working_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_reservation: Optional[Union[int, Ref, GetAtt, Sub]] = None
    repository_credentials: Optional[RepositoryCredentials] = None
    extra_hosts: Optional[list[HostEntry]] = None
    hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    linux_parameters: Optional[LinuxParameters] = None
    version_consistency: Optional[Union[str, Ref, GetAtt, Sub]] = None
    restart_policy: Optional[RestartPolicy] = None
    disable_networking: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    pseudo_terminal: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    mount_points: Optional[list[MountPoint]] = None
    depends_on: Optional[list[ContainerDependency]] = None
    docker_labels: Optional[dict[str, str]] = None
    port_mappings: Optional[list[PortMapping]] = None
    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[KeyValuePair]] = None
    links: Optional[Union[list[str], Ref]] = None


@dataclass
class ContainerDependency(PropertyType):
    CONDITION = "Condition"
    CONTAINER_NAME = "ContainerName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "container_name": "ContainerName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class DockerVolumeConfiguration(PropertyType):
    DRIVER_OPTS = "DriverOpts"
    SCOPE = "Scope"
    AUTOPROVISION = "Autoprovision"
    DRIVER = "Driver"
    LABELS = "Labels"

    _property_mappings: ClassVar[dict[str, str]] = {
        "driver_opts": "DriverOpts",
        "scope": "Scope",
        "autoprovision": "Autoprovision",
        "driver": "Driver",
        "labels": "Labels",
    }

    driver_opts: Optional[dict[str, str]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    autoprovision: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    driver: Optional[Union[str, Ref, GetAtt, Sub]] = None
    labels: Optional[dict[str, str]] = None


@dataclass
class EFSVolumeConfiguration(PropertyType):
    FILESYSTEM_ID = "FilesystemId"
    TRANSIT_ENCRYPTION = "TransitEncryption"
    AUTHORIZATION_CONFIG = "AuthorizationConfig"
    ROOT_DIRECTORY = "RootDirectory"
    TRANSIT_ENCRYPTION_PORT = "TransitEncryptionPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filesystem_id": "FilesystemId",
        "transit_encryption": "TransitEncryption",
        "authorization_config": "AuthorizationConfig",
        "root_directory": "RootDirectory",
        "transit_encryption_port": "TransitEncryptionPort",
    }

    filesystem_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transit_encryption: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_config: Optional[AuthorizationConfig] = None
    root_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transit_encryption_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentFile(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EphemeralStorage(PropertyType):
    SIZE_IN_GI_B = "SizeInGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gi_b": "SizeInGiB",
    }

    size_in_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FSxAuthorizationConfig(PropertyType):
    CREDENTIALS_PARAMETER = "CredentialsParameter"
    DOMAIN = "Domain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credentials_parameter": "CredentialsParameter",
        "domain": "Domain",
    }

    credentials_parameter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FSxWindowsFileServerVolumeConfiguration(PropertyType):
    AUTHORIZATION_CONFIG = "AuthorizationConfig"
    FILE_SYSTEM_ID = "FileSystemId"
    ROOT_DIRECTORY = "RootDirectory"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_config": "AuthorizationConfig",
        "file_system_id": "FileSystemId",
        "root_directory": "RootDirectory",
    }

    authorization_config: Optional[FSxAuthorizationConfig] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    root_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class HealthCheck(PropertyType):
    COMMAND = "Command"
    TIMEOUT = "Timeout"
    RETRIES = "Retries"
    INTERVAL = "Interval"
    START_PERIOD = "StartPeriod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "command": "Command",
        "timeout": "Timeout",
        "retries": "Retries",
        "interval": "Interval",
        "start_period": "StartPeriod",
    }

    command: Optional[Union[list[str], Ref]] = None
    timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    start_period: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HostEntry(PropertyType):
    HOSTNAME = "Hostname"
    IP_ADDRESS = "IpAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hostname": "Hostname",
        "ip_address": "IpAddress",
    }

    hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HostVolumeProperties(PropertyType):
    SOURCE_PATH = "SourcePath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KernelCapabilities(PropertyType):
    ADD = "Add"
    DROP = "Drop"

    _property_mappings: ClassVar[dict[str, str]] = {
        "add": "Add",
        "drop": "Drop",
    }

    add: Optional[Union[list[str], Ref]] = None
    drop: Optional[Union[list[str], Ref]] = None


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
class LinuxParameters(PropertyType):
    CAPABILITIES = "Capabilities"
    SWAPPINESS = "Swappiness"
    TMPFS = "Tmpfs"
    SHARED_MEMORY_SIZE = "SharedMemorySize"
    DEVICES = "Devices"
    INIT_PROCESS_ENABLED = "InitProcessEnabled"
    MAX_SWAP = "MaxSwap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capabilities": "Capabilities",
        "swappiness": "Swappiness",
        "tmpfs": "Tmpfs",
        "shared_memory_size": "SharedMemorySize",
        "devices": "Devices",
        "init_process_enabled": "InitProcessEnabled",
        "max_swap": "MaxSwap",
    }

    capabilities: Optional[KernelCapabilities] = None
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
class PortMapping(PropertyType):
    APP_PROTOCOL = "AppProtocol"
    CONTAINER_PORT_RANGE = "ContainerPortRange"
    HOST_PORT = "HostPort"
    CONTAINER_PORT = "ContainerPort"
    PROTOCOL = "Protocol"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_protocol": "AppProtocol",
        "container_port_range": "ContainerPortRange",
        "host_port": "HostPort",
        "container_port": "ContainerPort",
        "protocol": "Protocol",
        "name": "Name",
    }

    app_protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_port_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProxyConfiguration(PropertyType):
    PROXY_CONFIGURATION_PROPERTIES = "ProxyConfigurationProperties"
    TYPE = "Type"
    CONTAINER_NAME = "ContainerName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "proxy_configuration_properties": "ProxyConfigurationProperties",
        "type_": "Type",
        "container_name": "ContainerName",
    }

    proxy_configuration_properties: Optional[list[KeyValuePair]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class RestartPolicy(PropertyType):
    IGNORED_EXIT_CODES = "IgnoredExitCodes"
    RESTART_ATTEMPT_PERIOD = "RestartAttemptPeriod"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ignored_exit_codes": "IgnoredExitCodes",
        "restart_attempt_period": "RestartAttemptPeriod",
        "enabled": "Enabled",
    }

    ignored_exit_codes: Optional[Union[list[int], Ref]] = None
    restart_attempt_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


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
class SystemControl(PropertyType):
    VALUE = "Value"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "namespace": "Namespace",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskDefinitionPlacementConstraint(PropertyType):
    TYPE = "Type"
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "expression": "Expression",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
    EFS_VOLUME_CONFIGURATION = "EFSVolumeConfiguration"
    HOST = "Host"
    CONFIGURED_AT_LAUNCH = "ConfiguredAtLaunch"
    DOCKER_VOLUME_CONFIGURATION = "DockerVolumeConfiguration"
    F_SX_WINDOWS_FILE_SERVER_VOLUME_CONFIGURATION = "FSxWindowsFileServerVolumeConfiguration"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_volume_configuration": "EFSVolumeConfiguration",
        "host": "Host",
        "configured_at_launch": "ConfiguredAtLaunch",
        "docker_volume_configuration": "DockerVolumeConfiguration",
        "f_sx_windows_file_server_volume_configuration": "FSxWindowsFileServerVolumeConfiguration",
        "name": "Name",
    }

    efs_volume_configuration: Optional[EFSVolumeConfiguration] = None
    host: Optional[HostVolumeProperties] = None
    configured_at_launch: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    docker_volume_configuration: Optional[DockerVolumeConfiguration] = None
    f_sx_windows_file_server_volume_configuration: Optional[FSxWindowsFileServerVolumeConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeFrom(PropertyType):
    READ_ONLY = "ReadOnly"
    SOURCE_CONTAINER = "SourceContainer"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only": "ReadOnly",
        "source_container": "SourceContainer",
    }

    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source_container: Optional[Union[str, Ref, GetAtt, Sub]] = None

