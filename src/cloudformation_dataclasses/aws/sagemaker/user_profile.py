"""PropertyTypes for AWS::SageMaker::UserProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppLifecycleManagement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_settings": "IdleSettings",
    }

    idle_settings: Optional[IdleSettings] = None


@dataclass
class CodeEditorAppSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_url": "RepositoryUrl",
    }

    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomFileSystemConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "gid": "Gid",
    }

    uid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultEbsStorageSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_ebs_volume_size_in_gb": "MaximumEbsVolumeSizeInGb",
        "default_ebs_volume_size_in_gb": "DefaultEbsVolumeSizeInGb",
    }

    maximum_ebs_volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_ebs_volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultSpaceStorageSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ebs_storage_settings": "DefaultEbsStorageSettings",
    }

    default_ebs_storage_settings: Optional[DefaultEbsStorageSettings] = None


@dataclass
class EFSFileSystemConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_path": "FileSystemPath",
        "file_system_id": "FileSystemId",
    }

    file_system_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FSxLustreFileSystemConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_path": "FileSystemPath",
        "file_system_id": "FileSystemId",
    }

    file_system_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HiddenSageMakerImage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sage_maker_image_name": "SageMakerImageName",
        "version_aliases": "VersionAliases",
    }

    sage_maker_image_name: Optional[Union[str, SageMakerImageName, Ref, GetAtt, Sub]] = None
    version_aliases: Optional[Union[list[str], Ref]] = None


@dataclass
class IdleSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_resource_spec": "DefaultResourceSpec",
        "lifecycle_config_arns": "LifecycleConfigArns",
    }

    default_resource_spec: Optional[ResourceSpec] = None
    lifecycle_config_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class KernelGatewayAppSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_status": "AccessStatus",
        "user_group": "UserGroup",
    }

    access_status: Optional[Union[str, RStudioServerProAccessStatus, Ref, GetAtt, Sub]] = None
    user_group: Optional[Union[str, RStudioServerProUserGroup, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceSpec(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_path": "MountPath",
        "s3_uri": "S3Uri",
    }

    mount_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SharingSettings(PropertyType):
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

