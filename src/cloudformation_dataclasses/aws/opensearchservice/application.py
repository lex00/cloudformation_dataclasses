"""PropertyTypes for AWS::OpenSearchService::Application."""

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
class AppConfig(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSource(PropertyType):
    DATA_SOURCE_ARN = "DataSourceArn"
    DATA_SOURCE_DESCRIPTION = "DataSourceDescription"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "data_source_description": "DataSourceDescription",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source_description: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamIdentityCenterOptions(PropertyType):
    IAM_IDENTITY_CENTER_INSTANCE_ARN = "IamIdentityCenterInstanceArn"
    IAM_ROLE_FOR_IDENTITY_CENTER_APPLICATION_ARN = "IamRoleForIdentityCenterApplicationArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_identity_center_instance_arn": "IamIdentityCenterInstanceArn",
        "iam_role_for_identity_center_application_arn": "IamRoleForIdentityCenterApplicationArn",
        "enabled": "Enabled",
    }

    iam_identity_center_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_for_identity_center_application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

