"""PropertyTypes for AWS::Greengrass::ResourceDefinition."""

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
class GroupOwnerSetting(PropertyType):
    AUTO_ADD_GROUP_OWNER = "AutoAddGroupOwner"
    GROUP_OWNER = "GroupOwner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_add_group_owner": "AutoAddGroupOwner",
        "group_owner": "GroupOwner",
    }

    auto_add_group_owner: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    group_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LocalDeviceResourceData(PropertyType):
    SOURCE_PATH = "SourcePath"
    GROUP_OWNER_SETTING = "GroupOwnerSetting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
        "group_owner_setting": "GroupOwnerSetting",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_owner_setting: Optional[GroupOwnerSetting] = None


@dataclass
class LocalVolumeResourceData(PropertyType):
    SOURCE_PATH = "SourcePath"
    DESTINATION_PATH = "DestinationPath"
    GROUP_OWNER_SETTING = "GroupOwnerSetting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
        "destination_path": "DestinationPath",
        "group_owner_setting": "GroupOwnerSetting",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_owner_setting: Optional[GroupOwnerSetting] = None


@dataclass
class ResourceDataContainer(PropertyType):
    SECRETS_MANAGER_SECRET_RESOURCE_DATA = "SecretsManagerSecretResourceData"
    SAGE_MAKER_MACHINE_LEARNING_MODEL_RESOURCE_DATA = "SageMakerMachineLearningModelResourceData"
    LOCAL_VOLUME_RESOURCE_DATA = "LocalVolumeResourceData"
    LOCAL_DEVICE_RESOURCE_DATA = "LocalDeviceResourceData"
    S3_MACHINE_LEARNING_MODEL_RESOURCE_DATA = "S3MachineLearningModelResourceData"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager_secret_resource_data": "SecretsManagerSecretResourceData",
        "sage_maker_machine_learning_model_resource_data": "SageMakerMachineLearningModelResourceData",
        "local_volume_resource_data": "LocalVolumeResourceData",
        "local_device_resource_data": "LocalDeviceResourceData",
        "s3_machine_learning_model_resource_data": "S3MachineLearningModelResourceData",
    }

    secrets_manager_secret_resource_data: Optional[SecretsManagerSecretResourceData] = None
    sage_maker_machine_learning_model_resource_data: Optional[SageMakerMachineLearningModelResourceData] = None
    local_volume_resource_data: Optional[LocalVolumeResourceData] = None
    local_device_resource_data: Optional[LocalDeviceResourceData] = None
    s3_machine_learning_model_resource_data: Optional[S3MachineLearningModelResourceData] = None


@dataclass
class ResourceDefinitionVersion(PropertyType):
    RESOURCES = "Resources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resources": "Resources",
    }

    resources: Optional[list[ResourceInstance]] = None


@dataclass
class ResourceDownloadOwnerSetting(PropertyType):
    GROUP_OWNER = "GroupOwner"
    GROUP_PERMISSION = "GroupPermission"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_owner": "GroupOwner",
        "group_permission": "GroupPermission",
    }

    group_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_permission: Optional[Union[str, Permission, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceInstance(PropertyType):
    RESOURCE_DATA_CONTAINER = "ResourceDataContainer"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_data_container": "ResourceDataContainer",
        "id": "Id",
        "name": "Name",
    }

    resource_data_container: Optional[ResourceDataContainer] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3MachineLearningModelResourceData(PropertyType):
    OWNER_SETTING = "OwnerSetting"
    DESTINATION_PATH = "DestinationPath"
    S3_URI = "S3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner_setting": "OwnerSetting",
        "destination_path": "DestinationPath",
        "s3_uri": "S3Uri",
    }

    owner_setting: Optional[ResourceDownloadOwnerSetting] = None
    destination_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SageMakerMachineLearningModelResourceData(PropertyType):
    OWNER_SETTING = "OwnerSetting"
    DESTINATION_PATH = "DestinationPath"
    SAGE_MAKER_JOB_ARN = "SageMakerJobArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner_setting": "OwnerSetting",
        "destination_path": "DestinationPath",
        "sage_maker_job_arn": "SageMakerJobArn",
    }

    owner_setting: Optional[ResourceDownloadOwnerSetting] = None
    destination_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sage_maker_job_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecretsManagerSecretResourceData(PropertyType):
    ARN = "ARN"
    ADDITIONAL_STAGING_LABELS_TO_DOWNLOAD = "AdditionalStagingLabelsToDownload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "ARN",
        "additional_staging_labels_to_download": "AdditionalStagingLabelsToDownload",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_staging_labels_to_download: Optional[Union[list[str], Ref]] = None

