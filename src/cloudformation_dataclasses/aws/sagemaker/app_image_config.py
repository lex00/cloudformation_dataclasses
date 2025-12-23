"""PropertyTypes for AWS::SageMaker::AppImageConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CodeEditorAppImageConfig(PropertyType):
    CONTAINER_CONFIG = "ContainerConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_config": "ContainerConfig",
    }

    container_config: Optional[ContainerConfig] = None


@dataclass
class ContainerConfig(PropertyType):
    CONTAINER_ENTRYPOINT = "ContainerEntrypoint"
    CONTAINER_ENVIRONMENT_VARIABLES = "ContainerEnvironmentVariables"
    CONTAINER_ARGUMENTS = "ContainerArguments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_entrypoint": "ContainerEntrypoint",
        "container_environment_variables": "ContainerEnvironmentVariables",
        "container_arguments": "ContainerArguments",
    }

    container_entrypoint: Optional[Union[list[str], Ref]] = None
    container_environment_variables: Optional[list[CustomImageContainerEnvironmentVariable]] = None
    container_arguments: Optional[Union[list[str], Ref]] = None


@dataclass
class CustomImageContainerEnvironmentVariable(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FileSystemConfig(PropertyType):
    MOUNT_PATH = "MountPath"
    DEFAULT_GID = "DefaultGid"
    DEFAULT_UID = "DefaultUid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_path": "MountPath",
        "default_gid": "DefaultGid",
        "default_uid": "DefaultUid",
    }

    mount_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_gid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_uid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JupyterLabAppImageConfig(PropertyType):
    CONTAINER_CONFIG = "ContainerConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_config": "ContainerConfig",
    }

    container_config: Optional[ContainerConfig] = None


@dataclass
class KernelGatewayImageConfig(PropertyType):
    KERNEL_SPECS = "KernelSpecs"
    FILE_SYSTEM_CONFIG = "FileSystemConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kernel_specs": "KernelSpecs",
        "file_system_config": "FileSystemConfig",
    }

    kernel_specs: Optional[list[KernelSpec]] = None
    file_system_config: Optional[FileSystemConfig] = None


@dataclass
class KernelSpec(PropertyType):
    DISPLAY_NAME = "DisplayName"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "display_name": "DisplayName",
        "name": "Name",
    }

    display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

