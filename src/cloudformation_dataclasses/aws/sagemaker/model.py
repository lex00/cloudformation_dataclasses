"""PropertyTypes for AWS::SageMaker::Model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalModelDataSource(PropertyType):
    CHANNEL_NAME = "ChannelName"
    S3_DATA_SOURCE = "S3DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_name": "ChannelName",
        "s3_data_source": "S3DataSource",
    }

    channel_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_data_source: Optional[S3DataSource] = None


@dataclass
class ContainerDefinition(PropertyType):
    IMAGE_CONFIG = "ImageConfig"
    INFERENCE_SPECIFICATION_NAME = "InferenceSpecificationName"
    CONTAINER_HOSTNAME = "ContainerHostname"
    MODEL_PACKAGE_NAME = "ModelPackageName"
    MODE = "Mode"
    ENVIRONMENT = "Environment"
    MODEL_DATA_URL = "ModelDataUrl"
    IMAGE = "Image"
    MODEL_DATA_SOURCE = "ModelDataSource"
    MULTI_MODEL_CONFIG = "MultiModelConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_config": "ImageConfig",
        "inference_specification_name": "InferenceSpecificationName",
        "container_hostname": "ContainerHostname",
        "model_package_name": "ModelPackageName",
        "mode": "Mode",
        "environment": "Environment",
        "model_data_url": "ModelDataUrl",
        "image": "Image",
        "model_data_source": "ModelDataSource",
        "multi_model_config": "MultiModelConfig",
    }

    image_config: Optional[ImageConfig] = None
    inference_specification_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_package_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, ContainerMode, Ref, GetAtt, Sub]] = None
    environment: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    model_data_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_data_source: Optional[ModelDataSource] = None
    multi_model_config: Optional[MultiModelConfig] = None


@dataclass
class HubAccessConfig(PropertyType):
    HUB_CONTENT_ARN = "HubContentArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hub_content_arn": "HubContentArn",
    }

    hub_content_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageConfig(PropertyType):
    REPOSITORY_AUTH_CONFIG = "RepositoryAuthConfig"
    REPOSITORY_ACCESS_MODE = "RepositoryAccessMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_auth_config": "RepositoryAuthConfig",
        "repository_access_mode": "RepositoryAccessMode",
    }

    repository_auth_config: Optional[RepositoryAuthConfig] = None
    repository_access_mode: Optional[Union[str, RepositoryAccessMode, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceExecutionConfig(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, InferenceExecutionMode, Ref, GetAtt, Sub]] = None


@dataclass
class ModelAccessConfig(PropertyType):
    ACCEPT_EULA = "AcceptEula"

    _property_mappings: ClassVar[dict[str, str]] = {
        "accept_eula": "AcceptEula",
    }

    accept_eula: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ModelDataSource(PropertyType):
    S3_DATA_SOURCE = "S3DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_source": "S3DataSource",
    }

    s3_data_source: Optional[S3DataSource] = None


@dataclass
class MultiModelConfig(PropertyType):
    MODEL_CACHE_SETTING = "ModelCacheSetting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_cache_setting": "ModelCacheSetting",
    }

    model_cache_setting: Optional[Union[str, ModelCacheSetting, Ref, GetAtt, Sub]] = None


@dataclass
class RepositoryAuthConfig(PropertyType):
    REPOSITORY_CREDENTIALS_PROVIDER_ARN = "RepositoryCredentialsProviderArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_credentials_provider_arn": "RepositoryCredentialsProviderArn",
    }

    repository_credentials_provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3DataSource(PropertyType):
    MODEL_ACCESS_CONFIG = "ModelAccessConfig"
    S3_URI = "S3Uri"
    S3_DATA_TYPE = "S3DataType"
    COMPRESSION_TYPE = "CompressionType"
    HUB_ACCESS_CONFIG = "HubAccessConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_access_config": "ModelAccessConfig",
        "s3_uri": "S3Uri",
        "s3_data_type": "S3DataType",
        "compression_type": "CompressionType",
        "hub_access_config": "HubAccessConfig",
    }

    model_access_config: Optional[ModelAccessConfig] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_data_type: Optional[Union[str, S3DataType, Ref, GetAtt, Sub]] = None
    compression_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hub_access_config: Optional[HubAccessConfig] = None


@dataclass
class VpcConfig(PropertyType):
    SUBNETS = "Subnets"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

