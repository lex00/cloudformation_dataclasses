"""PropertyTypes for AWS::Elasticsearch::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AutoTuneDesiredState:
    """AutoTuneDesiredState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AutoTuneState:
    """AutoTuneState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLE_IN_PROGRESS = "ENABLE_IN_PROGRESS"
    DISABLE_IN_PROGRESS = "DISABLE_IN_PROGRESS"
    DISABLED_AND_ROLLBACK_SCHEDULED = "DISABLED_AND_ROLLBACK_SCHEDULED"
    DISABLED_AND_ROLLBACK_IN_PROGRESS = "DISABLED_AND_ROLLBACK_IN_PROGRESS"
    DISABLED_AND_ROLLBACK_COMPLETE = "DISABLED_AND_ROLLBACK_COMPLETE"
    DISABLED_AND_ROLLBACK_ERROR = "DISABLED_AND_ROLLBACK_ERROR"
    ERROR = "ERROR"


class AutoTuneType:
    """AutoTuneType enum values."""

    SCHEDULED_ACTION = "SCHEDULED_ACTION"


class ConfigChangeStatus:
    """ConfigChangeStatus enum values."""

    PENDING = "Pending"
    INITIALIZING = "Initializing"
    VALIDATING = "Validating"
    VALIDATIONFAILED = "ValidationFailed"
    APPLYINGCHANGES = "ApplyingChanges"
    COMPLETED = "Completed"
    PENDINGUSERINPUT = "PendingUserInput"
    CANCELLED = "Cancelled"


class DeploymentStatus:
    """DeploymentStatus enum values."""

    PENDING_UPDATE = "PENDING_UPDATE"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    NOT_ELIGIBLE = "NOT_ELIGIBLE"
    ELIGIBLE = "ELIGIBLE"


class DescribePackagesFilterName:
    """DescribePackagesFilterName enum values."""

    PACKAGEID = "PackageID"
    PACKAGENAME = "PackageName"
    PACKAGESTATUS = "PackageStatus"


class DomainPackageStatus:
    """DomainPackageStatus enum values."""

    ASSOCIATING = "ASSOCIATING"
    ASSOCIATION_FAILED = "ASSOCIATION_FAILED"
    ACTIVE = "ACTIVE"
    DISSOCIATING = "DISSOCIATING"
    DISSOCIATION_FAILED = "DISSOCIATION_FAILED"


class DomainProcessingStatusType:
    """DomainProcessingStatusType enum values."""

    CREATING = "Creating"
    ACTIVE = "Active"
    MODIFYING = "Modifying"
    UPGRADINGENGINEVERSION = "UpgradingEngineVersion"
    UPDATINGSERVICESOFTWARE = "UpdatingServiceSoftware"
    ISOLATED = "Isolated"
    DELETING = "Deleting"


class ESPartitionInstanceType:
    """ESPartitionInstanceType enum values."""

    M3_MEDIUM_ELASTICSEARCH = "m3.medium.elasticsearch"
    M3_LARGE_ELASTICSEARCH = "m3.large.elasticsearch"
    M3_XLARGE_ELASTICSEARCH = "m3.xlarge.elasticsearch"
    M3_2XLARGE_ELASTICSEARCH = "m3.2xlarge.elasticsearch"
    M4_LARGE_ELASTICSEARCH = "m4.large.elasticsearch"
    M4_XLARGE_ELASTICSEARCH = "m4.xlarge.elasticsearch"
    M4_2XLARGE_ELASTICSEARCH = "m4.2xlarge.elasticsearch"
    M4_4XLARGE_ELASTICSEARCH = "m4.4xlarge.elasticsearch"
    M4_10XLARGE_ELASTICSEARCH = "m4.10xlarge.elasticsearch"
    M5_LARGE_ELASTICSEARCH = "m5.large.elasticsearch"
    M5_XLARGE_ELASTICSEARCH = "m5.xlarge.elasticsearch"
    M5_2XLARGE_ELASTICSEARCH = "m5.2xlarge.elasticsearch"
    M5_4XLARGE_ELASTICSEARCH = "m5.4xlarge.elasticsearch"
    M5_12XLARGE_ELASTICSEARCH = "m5.12xlarge.elasticsearch"
    R5_LARGE_ELASTICSEARCH = "r5.large.elasticsearch"
    R5_XLARGE_ELASTICSEARCH = "r5.xlarge.elasticsearch"
    R5_2XLARGE_ELASTICSEARCH = "r5.2xlarge.elasticsearch"
    R5_4XLARGE_ELASTICSEARCH = "r5.4xlarge.elasticsearch"
    R5_12XLARGE_ELASTICSEARCH = "r5.12xlarge.elasticsearch"
    C5_LARGE_ELASTICSEARCH = "c5.large.elasticsearch"
    C5_XLARGE_ELASTICSEARCH = "c5.xlarge.elasticsearch"
    C5_2XLARGE_ELASTICSEARCH = "c5.2xlarge.elasticsearch"
    C5_4XLARGE_ELASTICSEARCH = "c5.4xlarge.elasticsearch"
    C5_9XLARGE_ELASTICSEARCH = "c5.9xlarge.elasticsearch"
    C5_18XLARGE_ELASTICSEARCH = "c5.18xlarge.elasticsearch"
    ULTRAWARM1_MEDIUM_ELASTICSEARCH = "ultrawarm1.medium.elasticsearch"
    ULTRAWARM1_LARGE_ELASTICSEARCH = "ultrawarm1.large.elasticsearch"
    T2_MICRO_ELASTICSEARCH = "t2.micro.elasticsearch"
    T2_SMALL_ELASTICSEARCH = "t2.small.elasticsearch"
    T2_MEDIUM_ELASTICSEARCH = "t2.medium.elasticsearch"
    R3_LARGE_ELASTICSEARCH = "r3.large.elasticsearch"
    R3_XLARGE_ELASTICSEARCH = "r3.xlarge.elasticsearch"
    R3_2XLARGE_ELASTICSEARCH = "r3.2xlarge.elasticsearch"
    R3_4XLARGE_ELASTICSEARCH = "r3.4xlarge.elasticsearch"
    R3_8XLARGE_ELASTICSEARCH = "r3.8xlarge.elasticsearch"
    I2_XLARGE_ELASTICSEARCH = "i2.xlarge.elasticsearch"
    I2_2XLARGE_ELASTICSEARCH = "i2.2xlarge.elasticsearch"
    D2_XLARGE_ELASTICSEARCH = "d2.xlarge.elasticsearch"
    D2_2XLARGE_ELASTICSEARCH = "d2.2xlarge.elasticsearch"
    D2_4XLARGE_ELASTICSEARCH = "d2.4xlarge.elasticsearch"
    D2_8XLARGE_ELASTICSEARCH = "d2.8xlarge.elasticsearch"
    C4_LARGE_ELASTICSEARCH = "c4.large.elasticsearch"
    C4_XLARGE_ELASTICSEARCH = "c4.xlarge.elasticsearch"
    C4_2XLARGE_ELASTICSEARCH = "c4.2xlarge.elasticsearch"
    C4_4XLARGE_ELASTICSEARCH = "c4.4xlarge.elasticsearch"
    C4_8XLARGE_ELASTICSEARCH = "c4.8xlarge.elasticsearch"
    R4_LARGE_ELASTICSEARCH = "r4.large.elasticsearch"
    R4_XLARGE_ELASTICSEARCH = "r4.xlarge.elasticsearch"
    R4_2XLARGE_ELASTICSEARCH = "r4.2xlarge.elasticsearch"
    R4_4XLARGE_ELASTICSEARCH = "r4.4xlarge.elasticsearch"
    R4_8XLARGE_ELASTICSEARCH = "r4.8xlarge.elasticsearch"
    R4_16XLARGE_ELASTICSEARCH = "r4.16xlarge.elasticsearch"
    I3_LARGE_ELASTICSEARCH = "i3.large.elasticsearch"
    I3_XLARGE_ELASTICSEARCH = "i3.xlarge.elasticsearch"
    I3_2XLARGE_ELASTICSEARCH = "i3.2xlarge.elasticsearch"
    I3_4XLARGE_ELASTICSEARCH = "i3.4xlarge.elasticsearch"
    I3_8XLARGE_ELASTICSEARCH = "i3.8xlarge.elasticsearch"
    I3_16XLARGE_ELASTICSEARCH = "i3.16xlarge.elasticsearch"


class ESWarmPartitionInstanceType:
    """ESWarmPartitionInstanceType enum values."""

    ULTRAWARM1_MEDIUM_ELASTICSEARCH = "ultrawarm1.medium.elasticsearch"
    ULTRAWARM1_LARGE_ELASTICSEARCH = "ultrawarm1.large.elasticsearch"


class EngineType:
    """EngineType enum values."""

    OPENSEARCH = "OpenSearch"
    ELASTICSEARCH = "Elasticsearch"


class InboundCrossClusterSearchConnectionStatusCode:
    """InboundCrossClusterSearchConnectionStatusCode enum values."""

    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    APPROVED = "APPROVED"
    REJECTING = "REJECTING"
    REJECTED = "REJECTED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class InitiatedBy:
    """InitiatedBy enum values."""

    CUSTOMER = "CUSTOMER"
    SERVICE = "SERVICE"


class LogType:
    """LogType enum values."""

    INDEX_SLOW_LOGS = "INDEX_SLOW_LOGS"
    SEARCH_SLOW_LOGS = "SEARCH_SLOW_LOGS"
    ES_APPLICATION_LOGS = "ES_APPLICATION_LOGS"
    AUDIT_LOGS = "AUDIT_LOGS"


class OptionState:
    """OptionState enum values."""

    REQUIRESINDEXDOCUMENTS = "RequiresIndexDocuments"
    PROCESSING = "Processing"
    ACTIVE = "Active"


class OutboundCrossClusterSearchConnectionStatusCode:
    """OutboundCrossClusterSearchConnectionStatusCode enum values."""

    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    VALIDATING = "VALIDATING"
    VALIDATION_FAILED = "VALIDATION_FAILED"
    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class OverallChangeStatus:
    """OverallChangeStatus enum values."""

    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PackageStatus:
    """PackageStatus enum values."""

    COPYING = "COPYING"
    COPY_FAILED = "COPY_FAILED"
    VALIDATING = "VALIDATING"
    VALIDATION_FAILED = "VALIDATION_FAILED"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETE_FAILED = "DELETE_FAILED"


class PackageType:
    """PackageType enum values."""

    TXT_DICTIONARY = "TXT-DICTIONARY"


class PrincipalType:
    """PrincipalType enum values."""

    AWS_ACCOUNT = "AWS_ACCOUNT"
    AWS_SERVICE = "AWS_SERVICE"


class PropertyValueType:
    """PropertyValueType enum values."""

    PLAIN_TEXT = "PLAIN_TEXT"
    STRINGIFIED_JSON = "STRINGIFIED_JSON"


class ReservedElasticsearchInstancePaymentOption:
    """ReservedElasticsearchInstancePaymentOption enum values."""

    ALL_UPFRONT = "ALL_UPFRONT"
    PARTIAL_UPFRONT = "PARTIAL_UPFRONT"
    NO_UPFRONT = "NO_UPFRONT"


class RollbackOnDisable:
    """RollbackOnDisable enum values."""

    NO_ROLLBACK = "NO_ROLLBACK"
    DEFAULT_ROLLBACK = "DEFAULT_ROLLBACK"


class ScheduledAutoTuneActionType:
    """ScheduledAutoTuneActionType enum values."""

    JVM_HEAP_SIZE_TUNING = "JVM_HEAP_SIZE_TUNING"
    JVM_YOUNG_GEN_TUNING = "JVM_YOUNG_GEN_TUNING"


class ScheduledAutoTuneSeverityType:
    """ScheduledAutoTuneSeverityType enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TLSSecurityPolicy:
    """TLSSecurityPolicy enum values."""

    POLICY_MIN_TLS_1_0_2019_07 = "Policy-Min-TLS-1-0-2019-07"
    POLICY_MIN_TLS_1_2_2019_07 = "Policy-Min-TLS-1-2-2019-07"
    POLICY_MIN_TLS_1_2_PFS_2023_10 = "Policy-Min-TLS-1-2-PFS-2023-10"


class TimeUnit:
    """TimeUnit enum values."""

    HOURS = "HOURS"


class UpgradeStatus:
    """UpgradeStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    SUCCEEDED_WITH_ISSUES = "SUCCEEDED_WITH_ISSUES"
    FAILED = "FAILED"


class UpgradeStep:
    """UpgradeStep enum values."""

    PRE_UPGRADE_CHECK = "PRE_UPGRADE_CHECK"
    SNAPSHOT = "SNAPSHOT"
    UPGRADE = "UPGRADE"


class VolumeType:
    """VolumeType enum values."""

    STANDARD = "standard"
    GP2 = "gp2"
    IO1 = "io1"
    GP3 = "gp3"


class VpcEndpointErrorCode:
    """VpcEndpointErrorCode enum values."""

    ENDPOINT_NOT_FOUND = "ENDPOINT_NOT_FOUND"
    SERVER_ERROR = "SERVER_ERROR"


class VpcEndpointStatus:
    """VpcEndpointStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


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

