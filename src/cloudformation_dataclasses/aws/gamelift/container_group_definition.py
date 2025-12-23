"""PropertyTypes for AWS::GameLift::ContainerGroupDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ContainerDependency(PropertyType):
    CONDITION = "Condition"
    CONTAINER_NAME = "ContainerName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "container_name": "ContainerName",
    }

    condition: Optional[Union[str, ContainerDependencyCondition, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerEnvironment(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerHealthCheck(PropertyType):
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
class ContainerMountPoint(PropertyType):
    INSTANCE_PATH = "InstancePath"
    CONTAINER_PATH = "ContainerPath"
    ACCESS_LEVEL = "AccessLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_path": "InstancePath",
        "container_path": "ContainerPath",
        "access_level": "AccessLevel",
    }

    instance_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_level: Optional[Union[str, ContainerMountPointAccessLevel, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerPortRange(PropertyType):
    FROM_PORT = "FromPort"
    TO_PORT = "ToPort"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
        "protocol": "Protocol",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, IpProtocol, Ref, GetAtt, Sub]] = None


@dataclass
class GameServerContainerDefinition(PropertyType):
    MOUNT_POINTS = "MountPoints"
    DEPENDS_ON = "DependsOn"
    CONTAINER_NAME = "ContainerName"
    ENVIRONMENT_OVERRIDE = "EnvironmentOverride"
    SERVER_SDK_VERSION = "ServerSdkVersion"
    IMAGE_URI = "ImageUri"
    RESOLVED_IMAGE_DIGEST = "ResolvedImageDigest"
    PORT_CONFIGURATION = "PortConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_points": "MountPoints",
        "depends_on": "DependsOn",
        "container_name": "ContainerName",
        "environment_override": "EnvironmentOverride",
        "server_sdk_version": "ServerSdkVersion",
        "image_uri": "ImageUri",
        "resolved_image_digest": "ResolvedImageDigest",
        "port_configuration": "PortConfiguration",
    }

    mount_points: Optional[list[ContainerMountPoint]] = None
    depends_on: Optional[list[ContainerDependency]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment_override: Optional[list[ContainerEnvironment]] = None
    server_sdk_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resolved_image_digest: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_configuration: Optional[PortConfiguration] = None


@dataclass
class PortConfiguration(PropertyType):
    CONTAINER_PORT_RANGES = "ContainerPortRanges"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_port_ranges": "ContainerPortRanges",
    }

    container_port_ranges: Optional[list[ContainerPortRange]] = None


@dataclass
class SupportContainerDefinition(PropertyType):
    MOUNT_POINTS = "MountPoints"
    DEPENDS_ON = "DependsOn"
    CONTAINER_NAME = "ContainerName"
    MEMORY_HARD_LIMIT_MEBIBYTES = "MemoryHardLimitMebibytes"
    ENVIRONMENT_OVERRIDE = "EnvironmentOverride"
    HEALTH_CHECK = "HealthCheck"
    VCPU = "Vcpu"
    IMAGE_URI = "ImageUri"
    RESOLVED_IMAGE_DIGEST = "ResolvedImageDigest"
    ESSENTIAL = "Essential"
    PORT_CONFIGURATION = "PortConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_points": "MountPoints",
        "depends_on": "DependsOn",
        "container_name": "ContainerName",
        "memory_hard_limit_mebibytes": "MemoryHardLimitMebibytes",
        "environment_override": "EnvironmentOverride",
        "health_check": "HealthCheck",
        "vcpu": "Vcpu",
        "image_uri": "ImageUri",
        "resolved_image_digest": "ResolvedImageDigest",
        "essential": "Essential",
        "port_configuration": "PortConfiguration",
    }

    mount_points: Optional[list[ContainerMountPoint]] = None
    depends_on: Optional[list[ContainerDependency]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_hard_limit_mebibytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    environment_override: Optional[list[ContainerEnvironment]] = None
    health_check: Optional[ContainerHealthCheck] = None
    vcpu: Optional[Union[float, Ref, GetAtt, Sub]] = None
    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resolved_image_digest: Optional[Union[str, Ref, GetAtt, Sub]] = None
    essential: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    port_configuration: Optional[PortConfiguration] = None

