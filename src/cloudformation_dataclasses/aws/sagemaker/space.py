"""PropertyTypes for AWS::SageMaker::Space."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CodeRepository(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_url": "RepositoryUrl",
    }

    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomFileSystem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "f_sx_lustre_file_system": "FSxLustreFileSystem",
        "efs_file_system": "EFSFileSystem",
        "s3_file_system": "S3FileSystem",
    }

    f_sx_lustre_file_system: Optional[FSxLustreFileSystem] = None
    efs_file_system: Optional[EFSFileSystem] = None
    s3_file_system: Optional[S3FileSystem] = None


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
class EFSFileSystem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_id": "FileSystemId",
    }

    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EbsStorageSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_volume_size_in_gb": "EbsVolumeSizeInGb",
    }

    ebs_volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FSxLustreFileSystem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_id": "FileSystemId",
    }

    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class OwnershipSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "owner_user_profile_name": "OwnerUserProfileName",
    }

    owner_user_profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class S3FileSystem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpaceAppLifecycleManagement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_settings": "IdleSettings",
    }

    idle_settings: Optional[SpaceIdleSettings] = None


@dataclass
class SpaceCodeEditorAppSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_resource_spec": "DefaultResourceSpec",
        "app_lifecycle_management": "AppLifecycleManagement",
    }

    default_resource_spec: Optional[ResourceSpec] = None
    app_lifecycle_management: Optional[SpaceAppLifecycleManagement] = None


@dataclass
class SpaceIdleSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_timeout_in_minutes": "IdleTimeoutInMinutes",
    }

    idle_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpaceJupyterLabAppSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_resource_spec": "DefaultResourceSpec",
        "code_repositories": "CodeRepositories",
        "app_lifecycle_management": "AppLifecycleManagement",
    }

    default_resource_spec: Optional[ResourceSpec] = None
    code_repositories: Optional[list[CodeRepository]] = None
    app_lifecycle_management: Optional[SpaceAppLifecycleManagement] = None


@dataclass
class SpaceSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jupyter_lab_app_settings": "JupyterLabAppSettings",
        "kernel_gateway_app_settings": "KernelGatewayAppSettings",
        "code_editor_app_settings": "CodeEditorAppSettings",
        "space_managed_resources": "SpaceManagedResources",
        "remote_access": "RemoteAccess",
        "jupyter_server_app_settings": "JupyterServerAppSettings",
        "custom_file_systems": "CustomFileSystems",
        "app_type": "AppType",
        "space_storage_settings": "SpaceStorageSettings",
    }

    jupyter_lab_app_settings: Optional[SpaceJupyterLabAppSettings] = None
    kernel_gateway_app_settings: Optional[KernelGatewayAppSettings] = None
    code_editor_app_settings: Optional[SpaceCodeEditorAppSettings] = None
    space_managed_resources: Optional[Union[str, FeatureStatus, Ref, GetAtt, Sub]] = None
    remote_access: Optional[Union[str, FeatureStatus, Ref, GetAtt, Sub]] = None
    jupyter_server_app_settings: Optional[JupyterServerAppSettings] = None
    custom_file_systems: Optional[list[CustomFileSystem]] = None
    app_type: Optional[Union[str, AppType, Ref, GetAtt, Sub]] = None
    space_storage_settings: Optional[SpaceStorageSettings] = None


@dataclass
class SpaceSharingSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sharing_type": "SharingType",
    }

    sharing_type: Optional[Union[str, SharingType, Ref, GetAtt, Sub]] = None


@dataclass
class SpaceStorageSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_storage_settings": "EbsStorageSettings",
    }

    ebs_storage_settings: Optional[EbsStorageSettings] = None

