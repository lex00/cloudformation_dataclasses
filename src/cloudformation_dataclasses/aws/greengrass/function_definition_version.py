"""PropertyTypes for AWS::Greengrass::FunctionDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DefaultConfig(PropertyType):
    EXECUTION = "Execution"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution": "Execution",
    }

    execution: Optional[Execution] = None


@dataclass
class Environment(PropertyType):
    VARIABLES = "Variables"
    EXECUTION = "Execution"
    RESOURCE_ACCESS_POLICIES = "ResourceAccessPolicies"
    ACCESS_SYSFS = "AccessSysfs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "execution": "Execution",
        "resource_access_policies": "ResourceAccessPolicies",
        "access_sysfs": "AccessSysfs",
    }

    variables: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    execution: Optional[Execution] = None
    resource_access_policies: Optional[list[ResourceAccessPolicy]] = None
    access_sysfs: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Execution(PropertyType):
    ISOLATION_MODE = "IsolationMode"
    RUN_AS = "RunAs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "isolation_mode": "IsolationMode",
        "run_as": "RunAs",
    }

    isolation_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    run_as: Optional[RunAs] = None


@dataclass
class Function(PropertyType):
    FUNCTION_ARN = "FunctionArn"
    FUNCTION_CONFIGURATION = "FunctionConfiguration"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionArn",
        "function_configuration": "FunctionConfiguration",
        "id": "Id",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    function_configuration: Optional[FunctionConfiguration] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FunctionConfiguration(PropertyType):
    MEMORY_SIZE = "MemorySize"
    PINNED = "Pinned"
    EXEC_ARGS = "ExecArgs"
    TIMEOUT = "Timeout"
    ENCODING_TYPE = "EncodingType"
    ENVIRONMENT = "Environment"
    EXECUTABLE = "Executable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_size": "MemorySize",
        "pinned": "Pinned",
        "exec_args": "ExecArgs",
        "timeout": "Timeout",
        "encoding_type": "EncodingType",
        "environment": "Environment",
        "executable": "Executable",
    }

    memory_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    pinned: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exec_args: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encoding_type: Optional[Union[str, EncodingType, Ref, GetAtt, Sub]] = None
    environment: Optional[Environment] = None
    executable: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceAccessPolicy(PropertyType):
    RESOURCE_ID = "ResourceId"
    PERMISSION = "Permission"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_id": "ResourceId",
        "permission": "Permission",
    }

    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    permission: Optional[Union[str, Permission, Ref, GetAtt, Sub]] = None


@dataclass
class RunAs(PropertyType):
    UID = "Uid"
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "gid": "Gid",
    }

    uid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gid: Optional[Union[int, Ref, GetAtt, Sub]] = None

