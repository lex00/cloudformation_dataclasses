"""PropertyTypes for AWS::ECS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    CAPACITY_PROVIDER = "CapacityProvider"
    WEIGHT = "Weight"
    BASE = "Base"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "weight": "Weight",
        "base": "Base",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterConfiguration(PropertyType):
    MANAGED_STORAGE_CONFIGURATION = "ManagedStorageConfiguration"
    EXECUTE_COMMAND_CONFIGURATION = "ExecuteCommandConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_storage_configuration": "ManagedStorageConfiguration",
        "execute_command_configuration": "ExecuteCommandConfiguration",
    }

    managed_storage_configuration: Optional[ManagedStorageConfiguration] = None
    execute_command_configuration: Optional[ExecuteCommandConfiguration] = None


@dataclass
class ClusterSettings(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExecuteCommandConfiguration(PropertyType):
    LOGGING = "Logging"
    KMS_KEY_ID = "KmsKeyId"
    LOG_CONFIGURATION = "LogConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logging": "Logging",
        "kms_key_id": "KmsKeyId",
        "log_configuration": "LogConfiguration",
    }

    logging: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_configuration: Optional[ExecuteCommandLogConfiguration] = None


@dataclass
class ExecuteCommandLogConfiguration(PropertyType):
    S3_ENCRYPTION_ENABLED = "S3EncryptionEnabled"
    CLOUD_WATCH_ENCRYPTION_ENABLED = "CloudWatchEncryptionEnabled"
    CLOUD_WATCH_LOG_GROUP_NAME = "CloudWatchLogGroupName"
    S3_KEY_PREFIX = "S3KeyPrefix"
    S3_BUCKET_NAME = "S3BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_encryption_enabled": "S3EncryptionEnabled",
        "cloud_watch_encryption_enabled": "CloudWatchEncryptionEnabled",
        "cloud_watch_log_group_name": "CloudWatchLogGroupName",
        "s3_key_prefix": "S3KeyPrefix",
        "s3_bucket_name": "S3BucketName",
    }

    s3_encryption_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloud_watch_encryption_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloud_watch_log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedStorageConfiguration(PropertyType):
    FARGATE_EPHEMERAL_STORAGE_KMS_KEY_ID = "FargateEphemeralStorageKmsKeyId"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fargate_ephemeral_storage_kms_key_id": "FargateEphemeralStorageKmsKeyId",
        "kms_key_id": "KmsKeyId",
    }

    fargate_ephemeral_storage_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectDefaults(PropertyType):
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "namespace": "Namespace",
    }

    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None

