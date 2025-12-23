"""PropertyTypes for AWS::SageMaker::AppImageConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CodeEditorAppImageConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_config": "ContainerConfig",
    }

    container_config: Optional[ContainerConfig] = None


@dataclass
class ContainerConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FileSystemConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_config": "ContainerConfig",
    }

    container_config: Optional[ContainerConfig] = None


@dataclass
class KernelGatewayImageConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kernel_specs": "KernelSpecs",
        "file_system_config": "FileSystemConfig",
    }

    kernel_specs: Optional[list[KernelSpec]] = None
    file_system_config: Optional[FileSystemConfig] = None


@dataclass
class KernelSpec(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_name": "DisplayName",
        "name": "Name",
    }

    display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

