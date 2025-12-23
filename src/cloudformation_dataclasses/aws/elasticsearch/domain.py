"""PropertyTypes for AWS::Elasticsearch::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    ANONYMOUS_AUTH_ENABLED = "AnonymousAuthEnabled"
    ENABLED = "Enabled"
    INTERNAL_USER_DATABASE_ENABLED = "InternalUserDatabaseEnabled"
    MASTER_USER_OPTIONS = "MasterUserOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "anonymous_auth_enabled": "AnonymousAuthEnabled",
        "enabled": "Enabled",
        "internal_user_database_enabled": "InternalUserDatabaseEnabled",
        "master_user_options": "MasterUserOptions",
    }

    anonymous_auth_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    internal_user_database_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    master_user_options: Optional[MasterUserOptions] = None


@dataclass
class CognitoOptions(PropertyType):
    ENABLED = "Enabled"
    IDENTITY_POOL_ID = "IdentityPoolId"
    ROLE_ARN = "RoleArn"
    USER_POOL_ID = "UserPoolId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "identity_pool_id": "IdentityPoolId",
        "role_arn": "RoleArn",
        "user_pool_id": "UserPoolId",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    identity_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColdStorageOptions(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainEndpointOptions(PropertyType):
    CUSTOM_ENDPOINT = "CustomEndpoint"
    CUSTOM_ENDPOINT_CERTIFICATE_ARN = "CustomEndpointCertificateArn"
    CUSTOM_ENDPOINT_ENABLED = "CustomEndpointEnabled"
    ENFORCE_HTTPS = "EnforceHTTPS"
    TLS_SECURITY_POLICY = "TLSSecurityPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_endpoint": "CustomEndpoint",
        "custom_endpoint_certificate_arn": "CustomEndpointCertificateArn",
        "custom_endpoint_enabled": "CustomEndpointEnabled",
        "enforce_https": "EnforceHTTPS",
        "tls_security_policy": "TLSSecurityPolicy",
    }

    custom_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_endpoint_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_endpoint_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enforce_https: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tls_security_policy: Optional[Union[str, TLSSecurityPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class EBSOptions(PropertyType):
    EBS_ENABLED = "EBSEnabled"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"
    VOLUME_TYPE = "VolumeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_enabled": "EBSEnabled",
        "iops": "Iops",
        "volume_size": "VolumeSize",
        "volume_type": "VolumeType",
    }

    ebs_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, VolumeType, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticsearchClusterConfig(PropertyType):
    COLD_STORAGE_OPTIONS = "ColdStorageOptions"
    DEDICATED_MASTER_COUNT = "DedicatedMasterCount"
    DEDICATED_MASTER_ENABLED = "DedicatedMasterEnabled"
    DEDICATED_MASTER_TYPE = "DedicatedMasterType"
    INSTANCE_COUNT = "InstanceCount"
    INSTANCE_TYPE = "InstanceType"
    WARM_COUNT = "WarmCount"
    WARM_ENABLED = "WarmEnabled"
    WARM_TYPE = "WarmType"
    ZONE_AWARENESS_CONFIG = "ZoneAwarenessConfig"
    ZONE_AWARENESS_ENABLED = "ZoneAwarenessEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cold_storage_options": "ColdStorageOptions",
        "dedicated_master_count": "DedicatedMasterCount",
        "dedicated_master_enabled": "DedicatedMasterEnabled",
        "dedicated_master_type": "DedicatedMasterType",
        "instance_count": "InstanceCount",
        "instance_type": "InstanceType",
        "warm_count": "WarmCount",
        "warm_enabled": "WarmEnabled",
        "warm_type": "WarmType",
        "zone_awareness_config": "ZoneAwarenessConfig",
        "zone_awareness_enabled": "ZoneAwarenessEnabled",
    }

    cold_storage_options: Optional[ColdStorageOptions] = None
    dedicated_master_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dedicated_master_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dedicated_master_type: Optional[Union[str, ESPartitionInstanceType, Ref, GetAtt, Sub]] = None
    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, ESPartitionInstanceType, Ref, GetAtt, Sub]] = None
    warm_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    warm_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    warm_type: Optional[Union[str, ESWarmPartitionInstanceType, Ref, GetAtt, Sub]] = None
    zone_awareness_config: Optional[ZoneAwarenessConfig] = None
    zone_awareness_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    ENABLED = "Enabled"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "kms_key_id": "KmsKeyId",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogPublishingOption(PropertyType):
    CLOUD_WATCH_LOGS_LOG_GROUP_ARN = "CloudWatchLogsLogGroupArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_log_group_arn": "CloudWatchLogsLogGroupArn",
        "enabled": "Enabled",
    }

    cloud_watch_logs_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MasterUserOptions(PropertyType):
    MASTER_USER_ARN = "MasterUserARN"
    MASTER_USER_NAME = "MasterUserName"
    MASTER_USER_PASSWORD = "MasterUserPassword"

    _property_mappings: ClassVar[dict[str, str]] = {
        "master_user_arn": "MasterUserARN",
        "master_user_name": "MasterUserName",
        "master_user_password": "MasterUserPassword",
    }

    master_user_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_user_password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SnapshotOptions(PropertyType):
    AUTOMATED_SNAPSHOT_START_HOUR = "AutomatedSnapshotStartHour"

    _property_mappings: ClassVar[dict[str, str]] = {
        "automated_snapshot_start_hour": "AutomatedSnapshotStartHour",
    }

    automated_snapshot_start_hour: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VPCOptions(PropertyType):
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ZoneAwarenessConfig(PropertyType):
    AVAILABILITY_ZONE_COUNT = "AvailabilityZoneCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_count": "AvailabilityZoneCount",
    }

    availability_zone_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

