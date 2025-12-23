"""PropertyTypes for AWS::SageMaker::UserProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppLifecycleManagement(PropertyType):
    IDLE_SETTINGS = "IdleSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_settings": "IdleSettings",
    }

    idle_settings: Optional[IdleSettings] = None


@dataclass
class CodeEditorAppSettings(PropertyType):
    CUSTOM_IMAGES = "CustomImages"
    DEFAULT_RESOURCE_SPEC = "DefaultResourceSpec"
    LIFECYCLE_CONFIG_ARNS = "LifecycleConfigArns"
    BUILT_IN_LIFECYCLE_CONFIG_ARN = "BuiltInLifecycleConfigArn"
    APP_LIFECYCLE_MANAGEMENT = "AppLifecycleManagement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_images": "CustomImages",
        "default_resource_spec": "DefaultResourceSpec",
        "lifecycle_config_arns": "LifecycleConfigArns",
        "built_in_lifecycle_config_arn": "BuiltInLifecycleConfigArn",
        "app_lifecycle_management": "AppLifecycleManagement",
    }

    custom_images: Optional[list[CustomImage]] = None
    default_resource_spec: Optional[ResourceSpec] = None
    lifecycle_config_arns: Optional[Union[list[str], Ref]] = None
    built_in_lifecycle_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_lifecycle_management: Optional[AppLifecycleManagement] = None


@dataclass
class CodeRepository(PropertyType):
    REPOSITORY_URL = "RepositoryUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_url": "RepositoryUrl",
    }

    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomFileSystemConfig(PropertyType):
    EFS_FILE_SYSTEM_CONFIG = "EFSFileSystemConfig"
    S3_FILE_SYSTEM_CONFIG = "S3FileSystemConfig"
    F_SX_LUSTRE_FILE_SYSTEM_CONFIG = "FSxLustreFileSystemConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_system_config": "EFSFileSystemConfig",
        "s3_file_system_config": "S3FileSystemConfig",
        "f_sx_lustre_file_system_config": "FSxLustreFileSystemConfig",
    }

    efs_file_system_config: Optional[EFSFileSystemConfig] = None
    s3_file_system_config: Optional[S3FileSystemConfig] = None
    f_sx_lustre_file_system_config: Optional[FSxLustreFileSystemConfig] = None


@dataclass
class CustomImage(PropertyType):
    IMAGE_NAME = "ImageName"
    APP_IMAGE_CONFIG_NAME = "AppImageConfigName"
    IMAGE_VERSION_NUMBER = "ImageVersionNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_name": "ImageName",
        "app_image_config_name": "AppImageConfigName",
        "image_version_number": "ImageVersionNumber",
    }

    image_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_image_config_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_version_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPosixUserConfig(PropertyType):
    UID = "Uid"
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "gid": "Gid",
    }

    uid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultEbsStorageSettings(PropertyType):
    MAXIMUM_EBS_VOLUME_SIZE_IN_GB = "MaximumEbsVolumeSizeInGb"
    DEFAULT_EBS_VOLUME_SIZE_IN_GB = "DefaultEbsVolumeSizeInGb"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_ebs_volume_size_in_gb": "MaximumEbsVolumeSizeInGb",
        "default_ebs_volume_size_in_gb": "DefaultEbsVolumeSizeInGb",
    }

    maximum_ebs_volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_ebs_volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultSpaceStorageSettings(PropertyType):
    DEFAULT_EBS_STORAGE_SETTINGS = "DefaultEbsStorageSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ebs_storage_settings": "DefaultEbsStorageSettings",
    }

    default_ebs_storage_settings: Optional[DefaultEbsStorageSettings] = None


@dataclass
class EFSFileSystemConfig(PropertyType):
    FILE_SYSTEM_PATH = "FileSystemPath"
    FILE_SYSTEM_ID = "FileSystemId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_path": "FileSystemPath",
        "file_system_id": "FileSystemId",
    }

    file_system_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FSxLustreFileSystemConfig(PropertyType):
    FILE_SYSTEM_PATH = "FileSystemPath"
    FILE_SYSTEM_ID = "FileSystemId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_path": "FileSystemPath",
        "file_system_id": "FileSystemId",
    }

    file_system_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HiddenSageMakerImage(PropertyType):
    SAGE_MAKER_IMAGE_NAME = "SageMakerImageName"
    VERSION_ALIASES = "VersionAliases"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sage_maker_image_name": "SageMakerImageName",
        "version_aliases": "VersionAliases",
    }

    sage_maker_image_name: Optional[Union[str, SageMakerImageName, Ref, GetAtt, Sub]] = None
    version_aliases: Optional[Union[list[str], Ref]] = None


@dataclass
class IdleSettings(PropertyType):
    MAX_IDLE_TIMEOUT_IN_MINUTES = "MaxIdleTimeoutInMinutes"
    IDLE_TIMEOUT_IN_MINUTES = "IdleTimeoutInMinutes"
    MIN_IDLE_TIMEOUT_IN_MINUTES = "MinIdleTimeoutInMinutes"
    LIFECYCLE_MANAGEMENT = "LifecycleManagement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_idle_timeout_in_minutes": "MaxIdleTimeoutInMinutes",
        "idle_timeout_in_minutes": "IdleTimeoutInMinutes",
        "min_idle_timeout_in_minutes": "MinIdleTimeoutInMinutes",
        "lifecycle_management": "LifecycleManagement",
    }

    max_idle_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    idle_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_idle_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lifecycle_management: Optional[Union[str, LifecycleManagement, Ref, GetAtt, Sub]] = None


@dataclass
class JupyterLabAppSettings(PropertyType):
    CUSTOM_IMAGES = "CustomImages"
    DEFAULT_RESOURCE_SPEC = "DefaultResourceSpec"
    LIFECYCLE_CONFIG_ARNS = "LifecycleConfigArns"
    BUILT_IN_LIFECYCLE_CONFIG_ARN = "BuiltInLifecycleConfigArn"
    CODE_REPOSITORIES = "CodeRepositories"
    APP_LIFECYCLE_MANAGEMENT = "AppLifecycleManagement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_images": "CustomImages",
        "default_resource_spec": "DefaultResourceSpec",
        "lifecycle_config_arns": "LifecycleConfigArns",
        "built_in_lifecycle_config_arn": "BuiltInLifecycleConfigArn",
        "code_repositories": "CodeRepositories",
        "app_lifecycle_management": "AppLifecycleManagement",
    }

    custom_images: Optional[list[CustomImage]] = None
    default_resource_spec: Optional[ResourceSpec] = None
    lifecycle_config_arns: Optional[Union[list[str], Ref]] = None
    built_in_lifecycle_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code_repositories: Optional[list[CodeRepository]] = None
    app_lifecycle_management: Optional[AppLifecycleManagement] = None


@dataclass
class JupyterServerAppSettings(PropertyType):
    DEFAULT_RESOURCE_SPEC = "DefaultResourceSpec"
    LIFECYCLE_CONFIG_ARNS = "LifecycleConfigArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_resource_spec": "DefaultResourceSpec",
        "lifecycle_config_arns": "LifecycleConfigArns",
    }

    default_resource_spec: Optional[ResourceSpec] = None
    lifecycle_config_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class KernelGatewayAppSettings(PropertyType):
    CUSTOM_IMAGES = "CustomImages"
    DEFAULT_RESOURCE_SPEC = "DefaultResourceSpec"
    LIFECYCLE_CONFIG_ARNS = "LifecycleConfigArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_images": "CustomImages",
        "default_resource_spec": "DefaultResourceSpec",
        "lifecycle_config_arns": "LifecycleConfigArns",
    }

    custom_images: Optional[list[CustomImage]] = None
    default_resource_spec: Optional[ResourceSpec] = None
    lifecycle_config_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class RStudioServerProAppSettings(PropertyType):
    ACCESS_STATUS = "AccessStatus"
    USER_GROUP = "UserGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_status": "AccessStatus",
        "user_group": "UserGroup",
    }

    access_status: Optional[Union[str, RStudioServerProAccessStatus, Ref, GetAtt, Sub]] = None
    user_group: Optional[Union[str, RStudioServerProUserGroup, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceSpec(PropertyType):
    LIFECYCLE_CONFIG_ARN = "LifecycleConfigArn"
    SAGE_MAKER_IMAGE_ARN = "SageMakerImageArn"
    INSTANCE_TYPE = "InstanceType"
    SAGE_MAKER_IMAGE_VERSION_ARN = "SageMakerImageVersionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle_config_arn": "LifecycleConfigArn",
        "sage_maker_image_arn": "SageMakerImageArn",
        "instance_type": "InstanceType",
        "sage_maker_image_version_arn": "SageMakerImageVersionArn",
    }

    lifecycle_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sage_maker_image_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, AppInstanceType, Ref, GetAtt, Sub]] = None
    sage_maker_image_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3FileSystemConfig(PropertyType):
    MOUNT_PATH = "MountPath"
    S3_URI = "S3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_path": "MountPath",
        "s3_uri": "S3Uri",
    }

    mount_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SharingSettings(PropertyType):
    NOTEBOOK_OUTPUT_OPTION = "NotebookOutputOption"
    S3_KMS_KEY_ID = "S3KmsKeyId"
    S3_OUTPUT_PATH = "S3OutputPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notebook_output_option": "NotebookOutputOption",
        "s3_kms_key_id": "S3KmsKeyId",
        "s3_output_path": "S3OutputPath",
    }

    notebook_output_option: Optional[Union[str, NotebookOutputOption, Ref, GetAtt, Sub]] = None
    s3_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StudioWebPortalSettings(PropertyType):
    HIDDEN_SAGE_MAKER_IMAGE_VERSION_ALIASES = "HiddenSageMakerImageVersionAliases"
    HIDDEN_APP_TYPES = "HiddenAppTypes"
    HIDDEN_INSTANCE_TYPES = "HiddenInstanceTypes"
    HIDDEN_ML_TOOLS = "HiddenMlTools"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hidden_sage_maker_image_version_aliases": "HiddenSageMakerImageVersionAliases",
        "hidden_app_types": "HiddenAppTypes",
        "hidden_instance_types": "HiddenInstanceTypes",
        "hidden_ml_tools": "HiddenMlTools",
    }

    hidden_sage_maker_image_version_aliases: Optional[list[HiddenSageMakerImage]] = None
    hidden_app_types: Optional[Union[list[str], Ref]] = None
    hidden_instance_types: Optional[Union[list[str], Ref]] = None
    hidden_ml_tools: Optional[Union[list[str], Ref]] = None


@dataclass
class UserSettings(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    JUPYTER_LAB_APP_SETTINGS = "JupyterLabAppSettings"
    KERNEL_GATEWAY_APP_SETTINGS = "KernelGatewayAppSettings"
    STUDIO_WEB_PORTAL_SETTINGS = "StudioWebPortalSettings"
    CUSTOM_FILE_SYSTEM_CONFIGS = "CustomFileSystemConfigs"
    CUSTOM_POSIX_USER_CONFIG = "CustomPosixUserConfig"
    CODE_EDITOR_APP_SETTINGS = "CodeEditorAppSettings"
    R_STUDIO_SERVER_PRO_APP_SETTINGS = "RStudioServerProAppSettings"
    STUDIO_WEB_PORTAL = "StudioWebPortal"
    JUPYTER_SERVER_APP_SETTINGS = "JupyterServerAppSettings"
    AUTO_MOUNT_HOME_EFS = "AutoMountHomeEFS"
    DEFAULT_LANDING_URI = "DefaultLandingUri"
    EXECUTION_ROLE = "ExecutionRole"
    SPACE_STORAGE_SETTINGS = "SpaceStorageSettings"
    SHARING_SETTINGS = "SharingSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "jupyter_lab_app_settings": "JupyterLabAppSettings",
        "kernel_gateway_app_settings": "KernelGatewayAppSettings",
        "studio_web_portal_settings": "StudioWebPortalSettings",
        "custom_file_system_configs": "CustomFileSystemConfigs",
        "custom_posix_user_config": "CustomPosixUserConfig",
        "code_editor_app_settings": "CodeEditorAppSettings",
        "r_studio_server_pro_app_settings": "RStudioServerProAppSettings",
        "studio_web_portal": "StudioWebPortal",
        "jupyter_server_app_settings": "JupyterServerAppSettings",
        "auto_mount_home_efs": "AutoMountHomeEFS",
        "default_landing_uri": "DefaultLandingUri",
        "execution_role": "ExecutionRole",
        "space_storage_settings": "SpaceStorageSettings",
        "sharing_settings": "SharingSettings",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    jupyter_lab_app_settings: Optional[JupyterLabAppSettings] = None
    kernel_gateway_app_settings: Optional[KernelGatewayAppSettings] = None
    studio_web_portal_settings: Optional[StudioWebPortalSettings] = None
    custom_file_system_configs: Optional[list[CustomFileSystemConfig]] = None
    custom_posix_user_config: Optional[CustomPosixUserConfig] = None
    code_editor_app_settings: Optional[CodeEditorAppSettings] = None
    r_studio_server_pro_app_settings: Optional[RStudioServerProAppSettings] = None
    studio_web_portal: Optional[Union[str, StudioWebPortal, Ref, GetAtt, Sub]] = None
    jupyter_server_app_settings: Optional[JupyterServerAppSettings] = None
    auto_mount_home_efs: Optional[Union[str, AutoMountHomeEFS, Ref, GetAtt, Sub]] = None
    default_landing_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    space_storage_settings: Optional[DefaultSpaceStorageSettings] = None
    sharing_settings: Optional[SharingSettings] = None

