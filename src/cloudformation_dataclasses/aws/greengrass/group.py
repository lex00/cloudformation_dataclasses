"""PropertyTypes for AWS::Greengrass::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BulkDeploymentStatus:
    """BulkDeploymentStatus enum values."""

    INITIALIZING = "Initializing"
    RUNNING = "Running"
    COMPLETED = "Completed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"


class ConfigurationSyncStatus:
    """ConfigurationSyncStatus enum values."""

    INSYNC = "InSync"
    OUTOFSYNC = "OutOfSync"


class DeploymentType:
    """DeploymentType enum values."""

    NEWDEPLOYMENT = "NewDeployment"
    REDEPLOYMENT = "Redeployment"
    RESETDEPLOYMENT = "ResetDeployment"
    FORCERESETDEPLOYMENT = "ForceResetDeployment"


class EncodingType:
    """EncodingType enum values."""

    BINARY = "binary"
    JSON = "json"


class FunctionIsolationMode:
    """FunctionIsolationMode enum values."""

    GREENGRASSCONTAINER = "GreengrassContainer"
    NOCONTAINER = "NoContainer"


class LoggerComponent:
    """LoggerComponent enum values."""

    GREENGRASSSYSTEM = "GreengrassSystem"
    LAMBDA = "Lambda"


class LoggerLevel:
    """LoggerLevel enum values."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class LoggerType:
    """LoggerType enum values."""

    FILESYSTEM = "FileSystem"
    AWSCLOUDWATCH = "AWSCloudWatch"


class Permission:
    """Permission enum values."""

    RO = "ro"
    RW = "rw"


class SoftwareToUpdate:
    """SoftwareToUpdate enum values."""

    CORE = "core"
    OTA_AGENT = "ota_agent"


class Telemetry:
    """Telemetry enum values."""

    ON = "On"
    OFF = "Off"


class UpdateAgentLogLevel:
    """UpdateAgentLogLevel enum values."""

    NONE = "NONE"
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    VERBOSE = "VERBOSE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class UpdateTargetsArchitecture:
    """UpdateTargetsArchitecture enum values."""

    ARMV6L = "armv6l"
    ARMV7L = "armv7l"
    X86_64 = "x86_64"
    AARCH64 = "aarch64"


class UpdateTargetsOperatingSystem:
    """UpdateTargetsOperatingSystem enum values."""

    UBUNTU = "ubuntu"
    RASPBIAN = "raspbian"
    AMAZON_LINUX = "amazon_linux"
    OPENWRT = "openwrt"


@dataclass
class GroupVersion(PropertyType):
    LOGGER_DEFINITION_VERSION_ARN = "LoggerDefinitionVersionArn"
    DEVICE_DEFINITION_VERSION_ARN = "DeviceDefinitionVersionArn"
    FUNCTION_DEFINITION_VERSION_ARN = "FunctionDefinitionVersionArn"
    CORE_DEFINITION_VERSION_ARN = "CoreDefinitionVersionArn"
    RESOURCE_DEFINITION_VERSION_ARN = "ResourceDefinitionVersionArn"
    CONNECTOR_DEFINITION_VERSION_ARN = "ConnectorDefinitionVersionArn"
    SUBSCRIPTION_DEFINITION_VERSION_ARN = "SubscriptionDefinitionVersionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logger_definition_version_arn": "LoggerDefinitionVersionArn",
        "device_definition_version_arn": "DeviceDefinitionVersionArn",
        "function_definition_version_arn": "FunctionDefinitionVersionArn",
        "core_definition_version_arn": "CoreDefinitionVersionArn",
        "resource_definition_version_arn": "ResourceDefinitionVersionArn",
        "connector_definition_version_arn": "ConnectorDefinitionVersionArn",
        "subscription_definition_version_arn": "SubscriptionDefinitionVersionArn",
    }

    logger_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    function_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    core_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subscription_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

