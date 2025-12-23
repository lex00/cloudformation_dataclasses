"""PropertyTypes for AWS::Elasticsearch::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainEndpointOptions(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "kms_key_id": "KmsKeyId",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogPublishingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_log_group_arn": "CloudWatchLogsLogGroupArn",
        "enabled": "Enabled",
    }

    cloud_watch_logs_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MasterUserOptions(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SnapshotOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "automated_snapshot_start_hour": "AutomatedSnapshotStartHour",
    }

    automated_snapshot_start_hour: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VPCOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ZoneAwarenessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_count": "AvailabilityZoneCount",
    }

    availability_zone_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

