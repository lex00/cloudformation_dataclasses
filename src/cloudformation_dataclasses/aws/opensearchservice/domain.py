"""PropertyTypes for AWS::OpenSearchService::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AWSServicePrincipal:
    """AWSServicePrincipal enum values."""

    APPLICATION_OPENSEARCHSERVICE_AMAZONAWS_COM = "application.opensearchservice.amazonaws.com"


class ActionSeverity:
    """ActionSeverity enum values."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class ActionStatus:
    """ActionStatus enum values."""

    PENDING_UPDATE = "PENDING_UPDATE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    NOT_ELIGIBLE = "NOT_ELIGIBLE"
    ELIGIBLE = "ELIGIBLE"


class ActionType:
    """ActionType enum values."""

    SERVICE_SOFTWARE_UPDATE = "SERVICE_SOFTWARE_UPDATE"
    JVM_HEAP_SIZE_TUNING = "JVM_HEAP_SIZE_TUNING"
    JVM_YOUNG_GEN_TUNING = "JVM_YOUNG_GEN_TUNING"


class AppConfigType:
    """AppConfigType enum values."""

    OPENSEARCHDASHBOARDS_DASHBOARDADMIN_USERS = "opensearchDashboards.dashboardAdmin.users"
    OPENSEARCHDASHBOARDS_DASHBOARDADMIN_GROUPS = "opensearchDashboards.dashboardAdmin.groups"


class ApplicationStatus:
    """ApplicationStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


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


class ConnectionMode:
    """ConnectionMode enum values."""

    DIRECT = "DIRECT"
    VPC_ENDPOINT = "VPC_ENDPOINT"


class DataSourceStatus:
    """DataSourceStatus enum values."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"


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
    PACKAGETYPE = "PackageType"
    ENGINEVERSION = "EngineVersion"
    PACKAGEOWNER = "PackageOwner"


class DomainHealth:
    """DomainHealth enum values."""

    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
    NOTAVAILABLE = "NotAvailable"


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


class DomainState:
    """DomainState enum values."""

    ACTIVE = "Active"
    PROCESSING = "Processing"
    NOTAVAILABLE = "NotAvailable"


class DryRunMode:
    """DryRunMode enum values."""

    BASIC = "Basic"
    VERBOSE = "Verbose"


class EngineType:
    """EngineType enum values."""

    OPENSEARCH = "OpenSearch"
    ELASTICSEARCH = "Elasticsearch"


class IPAddressType:
    """IPAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"


class InboundConnectionStatusCode:
    """InboundConnectionStatusCode enum values."""

    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    APPROVED = "APPROVED"
    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    REJECTING = "REJECTING"
    REJECTED = "REJECTED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class IndexStatus:
    """IndexStatus enum values."""

    CREATED = "CREATED"
    UPDATED = "UPDATED"
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


class MaintenanceStatus:
    """MaintenanceStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"


class MaintenanceType:
    """MaintenanceType enum values."""

    REBOOT_NODE = "REBOOT_NODE"
    RESTART_SEARCH_PROCESS = "RESTART_SEARCH_PROCESS"
    RESTART_DASHBOARD = "RESTART_DASHBOARD"


class MasterNodeStatus:
    """MasterNodeStatus enum values."""

    AVAILABLE = "Available"
    UNAVAILABLE = "UnAvailable"


class NaturalLanguageQueryGenerationCurrentState:
    """NaturalLanguageQueryGenerationCurrentState enum values."""

    NOT_ENABLED = "NOT_ENABLED"
    ENABLE_COMPLETE = "ENABLE_COMPLETE"
    ENABLE_IN_PROGRESS = "ENABLE_IN_PROGRESS"
    ENABLE_FAILED = "ENABLE_FAILED"
    DISABLE_COMPLETE = "DISABLE_COMPLETE"
    DISABLE_IN_PROGRESS = "DISABLE_IN_PROGRESS"
    DISABLE_FAILED = "DISABLE_FAILED"


class NaturalLanguageQueryGenerationDesiredState:
    """NaturalLanguageQueryGenerationDesiredState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class NodeOptionsNodeType:
    """NodeOptionsNodeType enum values."""

    COORDINATOR = "coordinator"


class NodeStatus:
    """NodeStatus enum values."""

    ACTIVE = "Active"
    STANDBY = "StandBy"
    NOTAVAILABLE = "NotAvailable"


class NodeType:
    """NodeType enum values."""

    DATA = "Data"
    ULTRAWARM = "Ultrawarm"
    MASTER = "Master"


class OpenSearchPartitionInstanceType:
    """OpenSearchPartitionInstanceType enum values."""

    M3_MEDIUM_SEARCH = "m3.medium.search"
    M3_LARGE_SEARCH = "m3.large.search"
    M3_XLARGE_SEARCH = "m3.xlarge.search"
    M3_2XLARGE_SEARCH = "m3.2xlarge.search"
    M4_LARGE_SEARCH = "m4.large.search"
    M4_XLARGE_SEARCH = "m4.xlarge.search"
    M4_2XLARGE_SEARCH = "m4.2xlarge.search"
    M4_4XLARGE_SEARCH = "m4.4xlarge.search"
    M4_10XLARGE_SEARCH = "m4.10xlarge.search"
    M5_LARGE_SEARCH = "m5.large.search"
    M5_XLARGE_SEARCH = "m5.xlarge.search"
    M5_2XLARGE_SEARCH = "m5.2xlarge.search"
    M5_4XLARGE_SEARCH = "m5.4xlarge.search"
    M5_12XLARGE_SEARCH = "m5.12xlarge.search"
    M5_24XLARGE_SEARCH = "m5.24xlarge.search"
    R5_LARGE_SEARCH = "r5.large.search"
    R5_XLARGE_SEARCH = "r5.xlarge.search"
    R5_2XLARGE_SEARCH = "r5.2xlarge.search"
    R5_4XLARGE_SEARCH = "r5.4xlarge.search"
    R5_12XLARGE_SEARCH = "r5.12xlarge.search"
    R5_24XLARGE_SEARCH = "r5.24xlarge.search"
    C5_LARGE_SEARCH = "c5.large.search"
    C5_XLARGE_SEARCH = "c5.xlarge.search"
    C5_2XLARGE_SEARCH = "c5.2xlarge.search"
    C5_4XLARGE_SEARCH = "c5.4xlarge.search"
    C5_9XLARGE_SEARCH = "c5.9xlarge.search"
    C5_18XLARGE_SEARCH = "c5.18xlarge.search"
    T3_NANO_SEARCH = "t3.nano.search"
    T3_MICRO_SEARCH = "t3.micro.search"
    T3_SMALL_SEARCH = "t3.small.search"
    T3_MEDIUM_SEARCH = "t3.medium.search"
    T3_LARGE_SEARCH = "t3.large.search"
    T3_XLARGE_SEARCH = "t3.xlarge.search"
    T3_2XLARGE_SEARCH = "t3.2xlarge.search"
    OR1_MEDIUM_SEARCH = "or1.medium.search"
    OR1_LARGE_SEARCH = "or1.large.search"
    OR1_XLARGE_SEARCH = "or1.xlarge.search"
    OR1_2XLARGE_SEARCH = "or1.2xlarge.search"
    OR1_4XLARGE_SEARCH = "or1.4xlarge.search"
    OR1_8XLARGE_SEARCH = "or1.8xlarge.search"
    OR1_12XLARGE_SEARCH = "or1.12xlarge.search"
    OR1_16XLARGE_SEARCH = "or1.16xlarge.search"
    ULTRAWARM1_MEDIUM_SEARCH = "ultrawarm1.medium.search"
    ULTRAWARM1_LARGE_SEARCH = "ultrawarm1.large.search"
    ULTRAWARM1_XLARGE_SEARCH = "ultrawarm1.xlarge.search"
    T2_MICRO_SEARCH = "t2.micro.search"
    T2_SMALL_SEARCH = "t2.small.search"
    T2_MEDIUM_SEARCH = "t2.medium.search"
    R3_LARGE_SEARCH = "r3.large.search"
    R3_XLARGE_SEARCH = "r3.xlarge.search"
    R3_2XLARGE_SEARCH = "r3.2xlarge.search"
    R3_4XLARGE_SEARCH = "r3.4xlarge.search"
    R3_8XLARGE_SEARCH = "r3.8xlarge.search"
    I2_XLARGE_SEARCH = "i2.xlarge.search"
    I2_2XLARGE_SEARCH = "i2.2xlarge.search"
    D2_XLARGE_SEARCH = "d2.xlarge.search"
    D2_2XLARGE_SEARCH = "d2.2xlarge.search"
    D2_4XLARGE_SEARCH = "d2.4xlarge.search"
    D2_8XLARGE_SEARCH = "d2.8xlarge.search"
    C4_LARGE_SEARCH = "c4.large.search"
    C4_XLARGE_SEARCH = "c4.xlarge.search"
    C4_2XLARGE_SEARCH = "c4.2xlarge.search"
    C4_4XLARGE_SEARCH = "c4.4xlarge.search"
    C4_8XLARGE_SEARCH = "c4.8xlarge.search"
    R4_LARGE_SEARCH = "r4.large.search"
    R4_XLARGE_SEARCH = "r4.xlarge.search"
    R4_2XLARGE_SEARCH = "r4.2xlarge.search"
    R4_4XLARGE_SEARCH = "r4.4xlarge.search"
    R4_8XLARGE_SEARCH = "r4.8xlarge.search"
    R4_16XLARGE_SEARCH = "r4.16xlarge.search"
    I3_LARGE_SEARCH = "i3.large.search"
    I3_XLARGE_SEARCH = "i3.xlarge.search"
    I3_2XLARGE_SEARCH = "i3.2xlarge.search"
    I3_4XLARGE_SEARCH = "i3.4xlarge.search"
    I3_8XLARGE_SEARCH = "i3.8xlarge.search"
    I3_16XLARGE_SEARCH = "i3.16xlarge.search"
    R6G_LARGE_SEARCH = "r6g.large.search"
    R6G_XLARGE_SEARCH = "r6g.xlarge.search"
    R6G_2XLARGE_SEARCH = "r6g.2xlarge.search"
    R6G_4XLARGE_SEARCH = "r6g.4xlarge.search"
    R6G_8XLARGE_SEARCH = "r6g.8xlarge.search"
    R6G_12XLARGE_SEARCH = "r6g.12xlarge.search"
    M6G_LARGE_SEARCH = "m6g.large.search"
    M6G_XLARGE_SEARCH = "m6g.xlarge.search"
    M6G_2XLARGE_SEARCH = "m6g.2xlarge.search"
    M6G_4XLARGE_SEARCH = "m6g.4xlarge.search"
    M6G_8XLARGE_SEARCH = "m6g.8xlarge.search"
    M6G_12XLARGE_SEARCH = "m6g.12xlarge.search"
    C6G_LARGE_SEARCH = "c6g.large.search"
    C6G_XLARGE_SEARCH = "c6g.xlarge.search"
    C6G_2XLARGE_SEARCH = "c6g.2xlarge.search"
    C6G_4XLARGE_SEARCH = "c6g.4xlarge.search"
    C6G_8XLARGE_SEARCH = "c6g.8xlarge.search"
    C6G_12XLARGE_SEARCH = "c6g.12xlarge.search"
    R6GD_LARGE_SEARCH = "r6gd.large.search"
    R6GD_XLARGE_SEARCH = "r6gd.xlarge.search"
    R6GD_2XLARGE_SEARCH = "r6gd.2xlarge.search"
    R6GD_4XLARGE_SEARCH = "r6gd.4xlarge.search"
    R6GD_8XLARGE_SEARCH = "r6gd.8xlarge.search"
    R6GD_12XLARGE_SEARCH = "r6gd.12xlarge.search"
    R6GD_16XLARGE_SEARCH = "r6gd.16xlarge.search"
    T4G_SMALL_SEARCH = "t4g.small.search"
    T4G_MEDIUM_SEARCH = "t4g.medium.search"


class OpenSearchWarmPartitionInstanceType:
    """OpenSearchWarmPartitionInstanceType enum values."""

    ULTRAWARM1_MEDIUM_SEARCH = "ultrawarm1.medium.search"
    ULTRAWARM1_LARGE_SEARCH = "ultrawarm1.large.search"
    ULTRAWARM1_XLARGE_SEARCH = "ultrawarm1.xlarge.search"


class OptionState:
    """OptionState enum values."""

    REQUIRESINDEXDOCUMENTS = "RequiresIndexDocuments"
    PROCESSING = "Processing"
    ACTIVE = "Active"


class OutboundConnectionStatusCode:
    """OutboundConnectionStatusCode enum values."""

    VALIDATING = "VALIDATING"
    VALIDATION_FAILED = "VALIDATION_FAILED"
    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    APPROVED = "APPROVED"
    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    REJECTING = "REJECTING"
    REJECTED = "REJECTED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class OverallChangeStatus:
    """OverallChangeStatus enum values."""

    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PackageScopeOperationEnum:
    """PackageScopeOperationEnum enum values."""

    ADD = "ADD"
    OVERRIDE = "OVERRIDE"
    REMOVE = "REMOVE"


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
    ZIP_PLUGIN = "ZIP-PLUGIN"
    PACKAGE_LICENSE = "PACKAGE-LICENSE"
    PACKAGE_CONFIG = "PACKAGE-CONFIG"


class PrincipalType:
    """PrincipalType enum values."""

    AWS_ACCOUNT = "AWS_ACCOUNT"
    AWS_SERVICE = "AWS_SERVICE"


class PropertyValueType:
    """PropertyValueType enum values."""

    PLAIN_TEXT = "PLAIN_TEXT"
    STRINGIFIED_JSON = "STRINGIFIED_JSON"


class RequirementLevel:
    """RequirementLevel enum values."""

    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    NONE = "NONE"


class ReservedInstancePaymentOption:
    """ReservedInstancePaymentOption enum values."""

    ALL_UPFRONT = "ALL_UPFRONT"
    PARTIAL_UPFRONT = "PARTIAL_UPFRONT"
    NO_UPFRONT = "NO_UPFRONT"


class RolesKeyIdCOption:
    """RolesKeyIdCOption enum values."""

    GROUPNAME = "GroupName"
    GROUPID = "GroupId"


class RollbackOnDisable:
    """RollbackOnDisable enum values."""

    NO_ROLLBACK = "NO_ROLLBACK"
    DEFAULT_ROLLBACK = "DEFAULT_ROLLBACK"


class ScheduleAt:
    """ScheduleAt enum values."""

    NOW = "NOW"
    TIMESTAMP = "TIMESTAMP"
    OFF_PEAK_WINDOW = "OFF_PEAK_WINDOW"


class ScheduledAutoTuneActionType:
    """ScheduledAutoTuneActionType enum values."""

    JVM_HEAP_SIZE_TUNING = "JVM_HEAP_SIZE_TUNING"
    JVM_YOUNG_GEN_TUNING = "JVM_YOUNG_GEN_TUNING"


class ScheduledAutoTuneSeverityType:
    """ScheduledAutoTuneSeverityType enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class ScheduledBy:
    """ScheduledBy enum values."""

    CUSTOMER = "CUSTOMER"
    SYSTEM = "SYSTEM"


class SkipUnavailableStatus:
    """SkipUnavailableStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SubjectKeyIdCOption:
    """SubjectKeyIdCOption enum values."""

    USERNAME = "UserName"
    USERID = "UserId"
    EMAIL = "Email"


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


class ZoneStatus:
    """ZoneStatus enum values."""

    ACTIVE = "Active"
    STANDBY = "StandBy"
    NOTAVAILABLE = "NotAvailable"


@dataclass
class AIMLOptions(PropertyType):
    S3_VECTORS_ENGINE = "S3VectorsEngine"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_vectors_engine": "S3VectorsEngine",
    }

    s3_vectors_engine: Optional[S3VectorsEngine] = None


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    IAM_FEDERATION_OPTIONS = "IAMFederationOptions"
    ANONYMOUS_AUTH_ENABLED = "AnonymousAuthEnabled"
    INTERNAL_USER_DATABASE_ENABLED = "InternalUserDatabaseEnabled"
    SAML_OPTIONS = "SAMLOptions"
    ENABLED = "Enabled"
    JWT_OPTIONS = "JWTOptions"
    ANONYMOUS_AUTH_DISABLE_DATE = "AnonymousAuthDisableDate"
    MASTER_USER_OPTIONS = "MasterUserOptions"

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
    MULTI_AZ_WITH_STANDBY_ENABLED = "MultiAZWithStandbyEnabled"
    DEDICATED_MASTER_ENABLED = "DedicatedMasterEnabled"
    ZONE_AWARENESS_CONFIG = "ZoneAwarenessConfig"
    COLD_STORAGE_OPTIONS = "ColdStorageOptions"
    NODE_OPTIONS = "NodeOptions"
    WARM_TYPE = "WarmType"
    INSTANCE_COUNT = "InstanceCount"
    WARM_ENABLED = "WarmEnabled"
    WARM_COUNT = "WarmCount"
    DEDICATED_MASTER_COUNT = "DedicatedMasterCount"
    INSTANCE_TYPE = "InstanceType"
    ZONE_AWARENESS_ENABLED = "ZoneAwarenessEnabled"
    DEDICATED_MASTER_TYPE = "DedicatedMasterType"

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
    USER_POOL_ID = "UserPoolId"
    ENABLED = "Enabled"
    IDENTITY_POOL_ID = "IdentityPoolId"
    ROLE_ARN = "RoleArn"

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
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainEndpointOptions(PropertyType):
    CUSTOM_ENDPOINT_ENABLED = "CustomEndpointEnabled"
    ENFORCE_HTTPS = "EnforceHTTPS"
    CUSTOM_ENDPOINT_CERTIFICATE_ARN = "CustomEndpointCertificateArn"
    CUSTOM_ENDPOINT = "CustomEndpoint"
    TLS_SECURITY_POLICY = "TLSSecurityPolicy"

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
    EBS_ENABLED = "EBSEnabled"
    VOLUME_TYPE = "VolumeType"
    THROUGHPUT = "Throughput"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"

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
    KMS_KEY_ID = "KmsKeyId"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "enabled": "Enabled",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IAMFederationOptions(PropertyType):
    SUBJECT_KEY = "SubjectKey"
    ROLES_KEY = "RolesKey"
    ENABLED = "Enabled"

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
    IDENTITY_CENTER_APPLICATION_ARN = "IdentityCenterApplicationARN"
    IDENTITY_CENTER_INSTANCE_ARN = "IdentityCenterInstanceARN"
    SUBJECT_KEY = "SubjectKey"
    ENABLED_API_ACCESS = "EnabledAPIAccess"
    ROLES_KEY = "RolesKey"
    IDENTITY_STORE_ID = "IdentityStoreId"

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
    ENTITY_ID = "EntityId"
    METADATA_CONTENT = "MetadataContent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id": "EntityId",
        "metadata_content": "MetadataContent",
    }

    entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JWTOptions(PropertyType):
    SUBJECT_KEY = "SubjectKey"
    PUBLIC_KEY = "PublicKey"
    ROLES_KEY = "RolesKey"
    ENABLED = "Enabled"

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
    MASTER_USER_PASSWORD = "MasterUserPassword"
    MASTER_USER_ARN = "MasterUserARN"
    MASTER_USER_NAME = "MasterUserName"

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
    TYPE = "Type"
    ENABLED = "Enabled"
    COUNT = "Count"

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
    NODE_TYPE = "NodeType"
    NODE_CONFIG = "NodeConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_type": "NodeType",
        "node_config": "NodeConfig",
    }

    node_type: Optional[Union[str, NodeOptionsNodeType, Ref, GetAtt, Sub]] = None
    node_config: Optional[NodeConfig] = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OffPeakWindow(PropertyType):
    WINDOW_START_TIME = "WindowStartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "window_start_time": "WindowStartTime",
    }

    window_start_time: Optional[WindowStartTime] = None


@dataclass
class OffPeakWindowOptions(PropertyType):
    OFF_PEAK_WINDOW = "OffPeakWindow"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "off_peak_window": "OffPeakWindow",
        "enabled": "Enabled",
    }

    off_peak_window: Optional[OffPeakWindow] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3VectorsEngine(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SAMLOptions(PropertyType):
    MASTER_BACKEND_ROLE = "MasterBackendRole"
    SUBJECT_KEY = "SubjectKey"
    IDP = "Idp"
    SESSION_TIMEOUT_MINUTES = "SessionTimeoutMinutes"
    ROLES_KEY = "RolesKey"
    ENABLED = "Enabled"
    MASTER_USER_NAME = "MasterUserName"

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
    NEW_VERSION = "NewVersion"
    UPDATE_STATUS = "UpdateStatus"
    DESCRIPTION = "Description"
    CANCELLABLE = "Cancellable"
    CURRENT_VERSION = "CurrentVersion"
    AUTOMATED_UPDATE_DATE = "AutomatedUpdateDate"
    UPDATE_AVAILABLE = "UpdateAvailable"
    OPTIONAL_DEPLOYMENT = "OptionalDeployment"

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
    AUTOMATED_SNAPSHOT_START_HOUR = "AutomatedSnapshotStartHour"

    _property_mappings: ClassVar[dict[str, str]] = {
        "automated_snapshot_start_hour": "AutomatedSnapshotStartHour",
    }

    automated_snapshot_start_hour: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SoftwareUpdateOptions(PropertyType):
    AUTO_SOFTWARE_UPDATE_ENABLED = "AutoSoftwareUpdateEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_software_update_enabled": "AutoSoftwareUpdateEnabled",
    }

    auto_software_update_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


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
class WindowStartTime(PropertyType):
    HOURS = "Hours"
    MINUTES = "Minutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hours": "Hours",
        "minutes": "Minutes",
    }

    hours: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ZoneAwarenessConfig(PropertyType):
    AVAILABILITY_ZONE_COUNT = "AvailabilityZoneCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_count": "AvailabilityZoneCount",
    }

    availability_zone_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

