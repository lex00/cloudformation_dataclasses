"""PropertyTypes for AWS::Greengrass::ResourceDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GroupOwnerSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_add_group_owner": "AutoAddGroupOwner",
        "group_owner": "GroupOwner",
    }

    auto_add_group_owner: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    group_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LocalDeviceResourceData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
        "group_owner_setting": "GroupOwnerSetting",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_owner_setting: Optional[GroupOwnerSetting] = None


@dataclass
class LocalVolumeResourceData(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "resources": "Resources",
    }

    resources: Optional[list[ResourceInstance]] = None


@dataclass
class ResourceDownloadOwnerSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_owner": "GroupOwner",
        "group_permission": "GroupPermission",
    }

    group_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_permission: Optional[Union[str, Permission, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceInstance(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "ARN",
        "additional_staging_labels_to_download": "AdditionalStagingLabelsToDownload",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_staging_labels_to_download: Optional[Union[list[str], Ref]] = None

