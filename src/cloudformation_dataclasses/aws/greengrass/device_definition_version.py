"""PropertyTypes for AWS::Greengrass::DeviceDefinitionVersion."""

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
class Device(PropertyType):
    SYNC_SHADOW = "SyncShadow"
    THING_ARN = "ThingArn"
    ID = "Id"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sync_shadow": "SyncShadow",
        "thing_arn": "ThingArn",
        "id": "Id",
        "certificate_arn": "CertificateArn",
    }

    sync_shadow: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    thing_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

