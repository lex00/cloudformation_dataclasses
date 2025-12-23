"""PropertyTypes for AWS::OpenSearchService::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AIMLOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_vectors_engine": "S3VectorsEngine",
    }

    s3_vectors_engine: Optional[S3VectorsEngine] = None


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_federation_options": "IAMFederationOptions",
        "anonymous_auth_enabled": "AnonymousAuthEnabled",
        "internal_user_database_enabled": "InternalUserDatabaseEnabled",
        "saml_options": "SAMLOptions",
        "enabled": "Enabled",
        "jwt_options": "JWTOptions",
        "anonymous_auth_disable_date": "AnonymousAuthDisableDate",
        "master_user_options": "MasterUserOptions",
    }

    iam_federation_options: Optional[IAMFederationOptions] = None
    anonymous_auth_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    internal_user_database_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    saml_options: Optional[SAMLOptions] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    jwt_options: Optional[JWTOptions] = None
    anonymous_auth_disable_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_user_options: Optional[MasterUserOptions] = None


@dataclass
class ClusterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_az_with_standby_enabled": "MultiAZWithStandbyEnabled",
        "dedicated_master_enabled": "DedicatedMasterEnabled",
        "zone_awareness_config": "ZoneAwarenessConfig",
        "cold_storage_options": "ColdStorageOptions",
        "node_options": "NodeOptions",
        "warm_type": "WarmType",
        "instance_count": "InstanceCount",
        "warm_enabled": "WarmEnabled",
        "warm_count": "WarmCount",
        "dedicated_master_count": "DedicatedMasterCount",
        "instance_type": "InstanceType",
        "zone_awareness_enabled": "ZoneAwarenessEnabled",
        "dedicated_master_type": "DedicatedMasterType",
    }

    multi_az_with_standby_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dedicated_master_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    zone_awareness_config: Optional[ZoneAwarenessConfig] = None
    cold_storage_options: Optional[ColdStorageOptions] = None
    node_options: Optional[list[NodeOption]] = None
    warm_type: Optional[Union[str, OpenSearchWarmPartitionInstanceType, Ref, GetAtt, Sub]] = None
    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    warm_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    warm_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dedicated_master_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, OpenSearchPartitionInstanceType, Ref, GetAtt, Sub]] = None
    zone_awareness_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dedicated_master_type: Optional[Union[str, OpenSearchPartitionInstanceType, Ref, GetAtt, Sub]] = None


@dataclass
class CognitoOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "user_pool_id": "UserPoolId",
        "enabled": "Enabled",
        "identity_pool_id": "IdentityPoolId",
        "role_arn": "RoleArn",
    }

    user_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    identity_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColdStorageOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainEndpointOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_endpoint_enabled": "CustomEndpointEnabled",
        "enforce_https": "EnforceHTTPS",
        "custom_endpoint_certificate_arn": "CustomEndpointCertificateArn",
        "custom_endpoint": "CustomEndpoint",
        "tls_security_policy": "TLSSecurityPolicy",
    }

    custom_endpoint_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enforce_https: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    custom_endpoint_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tls_security_policy: Optional[Union[str, TLSSecurityPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class EBSOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_enabled": "EBSEnabled",
        "volume_type": "VolumeType",
        "throughput": "Throughput",
        "iops": "Iops",
        "volume_size": "VolumeSize",
    }

    ebs_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, VolumeType, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "enabled": "Enabled",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IAMFederationOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_key": "SubjectKey",
        "roles_key": "RolesKey",
        "enabled": "Enabled",
    }

    subject_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    roles_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IdentityCenterOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "identity_center_application_arn": "IdentityCenterApplicationARN",
        "identity_center_instance_arn": "IdentityCenterInstanceARN",
        "subject_key": "SubjectKey",
        "enabled_api_access": "EnabledAPIAccess",
        "roles_key": "RolesKey",
        "identity_store_id": "IdentityStoreId",
    }

    identity_center_application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identity_center_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject_key: Optional[Union[str, SubjectKeyIdCOption, Ref, GetAtt, Sub]] = None
    enabled_api_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    roles_key: Optional[Union[str, RolesKeyIdCOption, Ref, GetAtt, Sub]] = None
    identity_store_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Idp(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id": "EntityId",
        "metadata_content": "MetadataContent",
    }

    entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JWTOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_key": "SubjectKey",
        "public_key": "PublicKey",
        "roles_key": "RolesKey",
        "enabled": "Enabled",
    }

    subject_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    public_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    roles_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


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
        "master_user_password": "MasterUserPassword",
        "master_user_arn": "MasterUserARN",
        "master_user_name": "MasterUserName",
    }

    master_user_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_user_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NodeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "enabled": "Enabled",
        "count": "Count",
    }

    type_: Optional[Union[str, OpenSearchPartitionInstanceType, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NodeOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "node_type": "NodeType",
        "node_config": "NodeConfig",
    }

    node_type: Optional[Union[str, NodeOptionsNodeType, Ref, GetAtt, Sub]] = None
    node_config: Optional[NodeConfig] = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OffPeakWindow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "window_start_time": "WindowStartTime",
    }

    window_start_time: Optional[WindowStartTime] = None


@dataclass
class OffPeakWindowOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "off_peak_window": "OffPeakWindow",
        "enabled": "Enabled",
    }

    off_peak_window: Optional[OffPeakWindow] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3VectorsEngine(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SAMLOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "master_backend_role": "MasterBackendRole",
        "subject_key": "SubjectKey",
        "idp": "Idp",
        "session_timeout_minutes": "SessionTimeoutMinutes",
        "roles_key": "RolesKey",
        "enabled": "Enabled",
        "master_user_name": "MasterUserName",
    }

    master_backend_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    idp: Optional[Idp] = None
    session_timeout_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    roles_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    master_user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceSoftwareOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "new_version": "NewVersion",
        "update_status": "UpdateStatus",
        "description": "Description",
        "cancellable": "Cancellable",
        "current_version": "CurrentVersion",
        "automated_update_date": "AutomatedUpdateDate",
        "update_available": "UpdateAvailable",
        "optional_deployment": "OptionalDeployment",
    }

    new_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    update_status: Optional[Union[str, DeploymentStatus, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cancellable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    current_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    automated_update_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    update_available: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    optional_deployment: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SnapshotOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "automated_snapshot_start_hour": "AutomatedSnapshotStartHour",
    }

    automated_snapshot_start_hour: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SoftwareUpdateOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_software_update_enabled": "AutoSoftwareUpdateEnabled",
    }

    auto_software_update_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VPCOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class WindowStartTime(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hours": "Hours",
        "minutes": "Minutes",
    }

    hours: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ZoneAwarenessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_count": "AvailabilityZoneCount",
    }

    availability_zone_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

