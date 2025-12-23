"""PropertyTypes for AWS::GreengrassV2::ComponentVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComponentDependencyRequirement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version_requirement": "VersionRequirement",
        "dependency_type": "DependencyType",
    }

    version_requirement: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dependency_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentPlatform(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes": "Attributes",
        "name": "Name",
    }

    attributes: Optional[dict[str, str]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaContainerParams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volumes": "Volumes",
        "mount_ro_sysfs": "MountROSysfs",
        "memory_size_in_kb": "MemorySizeInKB",
        "devices": "Devices",
    }

    volumes: Optional[list[LambdaVolumeMount]] = None
    mount_ro_sysfs: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    memory_size_in_kb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    devices: Optional[list[LambdaDeviceMount]] = None


@dataclass
class LambdaDeviceMount(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "add_group_owner": "AddGroupOwner",
        "permission": "Permission",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    add_group_owner: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    permission: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaEventSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "topic": "Topic",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaExecutionParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_instances_count": "MaxInstancesCount",
        "timeout_in_seconds": "TimeoutInSeconds",
        "environment_variables": "EnvironmentVariables",
        "event_sources": "EventSources",
        "pinned": "Pinned",
        "exec_args": "ExecArgs",
        "linux_process_params": "LinuxProcessParams",
        "input_payload_encoding_type": "InputPayloadEncodingType",
        "max_queue_size": "MaxQueueSize",
        "status_timeout_in_seconds": "StatusTimeoutInSeconds",
        "max_idle_time_in_seconds": "MaxIdleTimeInSeconds",
    }

    max_instances_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    environment_variables: Optional[dict[str, str]] = None
    event_sources: Optional[list[LambdaEventSource]] = None
    pinned: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exec_args: Optional[Union[list[str], Ref]] = None
    linux_process_params: Optional[LambdaLinuxProcessParams] = None
    input_payload_encoding_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_queue_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    status_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_idle_time_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaFunctionRecipeSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "component_dependencies": "ComponentDependencies",
        "component_lambda_parameters": "ComponentLambdaParameters",
        "lambda_arn": "LambdaArn",
        "component_platforms": "ComponentPlatforms",
        "component_name": "ComponentName",
        "component_version": "ComponentVersion",
    }

    component_dependencies: Optional[dict[str, Any]] = None
    component_lambda_parameters: Optional[LambdaExecutionParameters] = None
    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_platforms: Optional[list[ComponentPlatform]] = None
    component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaLinuxProcessParams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "isolation_mode": "IsolationMode",
        "container_params": "ContainerParams",
    }

    isolation_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_params: Optional[LambdaContainerParams] = None


@dataclass
class LambdaVolumeMount(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
        "destination_path": "DestinationPath",
        "add_group_owner": "AddGroupOwner",
        "permission": "Permission",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    add_group_owner: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    permission: Optional[Union[str, Ref, GetAtt, Sub]] = None

