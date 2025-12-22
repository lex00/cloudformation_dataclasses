"""PropertyTypes for AWS::GuardDuty::Filter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AdminStatus:
    """AdminStatus enum values."""

    ENABLED = "ENABLED"
    DISABLE_IN_PROGRESS = "DISABLE_IN_PROGRESS"


class AutoEnableMembers:
    """AutoEnableMembers enum values."""

    NEW = "NEW"
    ALL = "ALL"
    NONE = "NONE"


class ClusterStatus:
    """ClusterStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    PENDING = "PENDING"


class CoverageFilterCriterionKey:
    """CoverageFilterCriterionKey enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    CLUSTER_NAME = "CLUSTER_NAME"
    RESOURCE_TYPE = "RESOURCE_TYPE"
    COVERAGE_STATUS = "COVERAGE_STATUS"
    ADDON_VERSION = "ADDON_VERSION"
    MANAGEMENT_TYPE = "MANAGEMENT_TYPE"
    EKS_CLUSTER_NAME = "EKS_CLUSTER_NAME"
    ECS_CLUSTER_NAME = "ECS_CLUSTER_NAME"
    AGENT_VERSION = "AGENT_VERSION"
    INSTANCE_ID = "INSTANCE_ID"
    CLUSTER_ARN = "CLUSTER_ARN"


class CoverageSortKey:
    """CoverageSortKey enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    CLUSTER_NAME = "CLUSTER_NAME"
    COVERAGE_STATUS = "COVERAGE_STATUS"
    ISSUE = "ISSUE"
    ADDON_VERSION = "ADDON_VERSION"
    UPDATED_AT = "UPDATED_AT"
    EKS_CLUSTER_NAME = "EKS_CLUSTER_NAME"
    ECS_CLUSTER_NAME = "ECS_CLUSTER_NAME"
    INSTANCE_ID = "INSTANCE_ID"


class CoverageStatisticsType:
    """CoverageStatisticsType enum values."""

    COUNT_BY_RESOURCE_TYPE = "COUNT_BY_RESOURCE_TYPE"
    COUNT_BY_COVERAGE_STATUS = "COUNT_BY_COVERAGE_STATUS"


class CoverageStatus:
    """CoverageStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class CriterionKey:
    """CriterionKey enum values."""

    EC2_INSTANCE_ARN = "EC2_INSTANCE_ARN"
    SCAN_ID = "SCAN_ID"
    ACCOUNT_ID = "ACCOUNT_ID"
    GUARDDUTY_FINDING_ID = "GUARDDUTY_FINDING_ID"
    SCAN_START_TIME = "SCAN_START_TIME"
    SCAN_STATUS = "SCAN_STATUS"
    SCAN_TYPE = "SCAN_TYPE"


class DataSource:
    """DataSource enum values."""

    FLOW_LOGS = "FLOW_LOGS"
    CLOUD_TRAIL = "CLOUD_TRAIL"
    DNS_LOGS = "DNS_LOGS"
    S3_LOGS = "S3_LOGS"
    KUBERNETES_AUDIT_LOGS = "KUBERNETES_AUDIT_LOGS"
    EC2_MALWARE_SCAN = "EC2_MALWARE_SCAN"


class DataSourceStatus:
    """DataSourceStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DestinationType:
    """DestinationType enum values."""

    S3 = "S3"


class DetectionSource:
    """DetectionSource enum values."""

    AMAZON = "AMAZON"
    BITDEFENDER = "BITDEFENDER"


class DetectorFeature:
    """DetectorFeature enum values."""

    S3_DATA_EVENTS = "S3_DATA_EVENTS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    EBS_MALWARE_PROTECTION = "EBS_MALWARE_PROTECTION"
    RDS_LOGIN_EVENTS = "RDS_LOGIN_EVENTS"
    EKS_RUNTIME_MONITORING = "EKS_RUNTIME_MONITORING"
    LAMBDA_NETWORK_LOGS = "LAMBDA_NETWORK_LOGS"
    RUNTIME_MONITORING = "RUNTIME_MONITORING"


class DetectorFeatureResult:
    """DetectorFeatureResult enum values."""

    FLOW_LOGS = "FLOW_LOGS"
    CLOUD_TRAIL = "CLOUD_TRAIL"
    DNS_LOGS = "DNS_LOGS"
    S3_DATA_EVENTS = "S3_DATA_EVENTS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    EBS_MALWARE_PROTECTION = "EBS_MALWARE_PROTECTION"
    RDS_LOGIN_EVENTS = "RDS_LOGIN_EVENTS"
    EKS_RUNTIME_MONITORING = "EKS_RUNTIME_MONITORING"
    LAMBDA_NETWORK_LOGS = "LAMBDA_NETWORK_LOGS"
    RUNTIME_MONITORING = "RUNTIME_MONITORING"


class DetectorStatus:
    """DetectorStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EbsSnapshotPreservation:
    """EbsSnapshotPreservation enum values."""

    NO_RETENTION = "NO_RETENTION"
    RETENTION_WITH_FINDING = "RETENTION_WITH_FINDING"


class EcsClusterStatus:
    """EcsClusterStatus enum values."""

    ACTIVE = "ACTIVE"
    PROVISIONING = "PROVISIONING"
    DEPROVISIONING = "DEPROVISIONING"
    FAILED = "FAILED"
    INACTIVE = "INACTIVE"


class EcsLaunchType:
    """EcsLaunchType enum values."""

    FARGATE = "FARGATE"
    EC2 = "EC2"


class FeatureAdditionalConfiguration:
    """FeatureAdditionalConfiguration enum values."""

    EKS_ADDON_MANAGEMENT = "EKS_ADDON_MANAGEMENT"
    ECS_FARGATE_AGENT_MANAGEMENT = "ECS_FARGATE_AGENT_MANAGEMENT"
    EC2_AGENT_MANAGEMENT = "EC2_AGENT_MANAGEMENT"


class FeatureStatus:
    """FeatureStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Feedback:
    """Feedback enum values."""

    USEFUL = "USEFUL"
    NOT_USEFUL = "NOT_USEFUL"


class FilterAction:
    """FilterAction enum values."""

    NOOP = "NOOP"
    ARCHIVE = "ARCHIVE"


class FindingPublishingFrequency:
    """FindingPublishingFrequency enum values."""

    FIFTEEN_MINUTES = "FIFTEEN_MINUTES"
    ONE_HOUR = "ONE_HOUR"
    SIX_HOURS = "SIX_HOURS"


class FindingResourceType:
    """FindingResourceType enum values."""

    EC2_INSTANCE = "EC2_INSTANCE"
    EC2_NETWORK_INTERFACE = "EC2_NETWORK_INTERFACE"
    S3_BUCKET = "S3_BUCKET"
    S3_OBJECT = "S3_OBJECT"
    ACCESS_KEY = "ACCESS_KEY"
    EKS_CLUSTER = "EKS_CLUSTER"
    KUBERNETES_WORKLOAD = "KUBERNETES_WORKLOAD"
    CONTAINER = "CONTAINER"
    ECS_CLUSTER = "ECS_CLUSTER"
    ECS_TASK = "ECS_TASK"
    AUTOSCALING_AUTO_SCALING_GROUP = "AUTOSCALING_AUTO_SCALING_GROUP"
    IAM_INSTANCE_PROFILE = "IAM_INSTANCE_PROFILE"
    CLOUDFORMATION_STACK = "CLOUDFORMATION_STACK"
    EC2_LAUNCH_TEMPLATE = "EC2_LAUNCH_TEMPLATE"
    EC2_VPC = "EC2_VPC"
    EC2_IMAGE = "EC2_IMAGE"


class FindingStatisticType:
    """FindingStatisticType enum values."""

    COUNT_BY_SEVERITY = "COUNT_BY_SEVERITY"


class FreeTrialFeatureResult:
    """FreeTrialFeatureResult enum values."""

    FLOW_LOGS = "FLOW_LOGS"
    CLOUD_TRAIL = "CLOUD_TRAIL"
    DNS_LOGS = "DNS_LOGS"
    S3_DATA_EVENTS = "S3_DATA_EVENTS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    EBS_MALWARE_PROTECTION = "EBS_MALWARE_PROTECTION"
    RDS_LOGIN_EVENTS = "RDS_LOGIN_EVENTS"
    EKS_RUNTIME_MONITORING = "EKS_RUNTIME_MONITORING"
    LAMBDA_NETWORK_LOGS = "LAMBDA_NETWORK_LOGS"
    FARGATE_RUNTIME_MONITORING = "FARGATE_RUNTIME_MONITORING"
    EC2_RUNTIME_MONITORING = "EC2_RUNTIME_MONITORING"


class GroupByType:
    """GroupByType enum values."""

    ACCOUNT = "ACCOUNT"
    DATE = "DATE"
    FINDING_TYPE = "FINDING_TYPE"
    RESOURCE = "RESOURCE"
    SEVERITY = "SEVERITY"


class IndicatorType:
    """IndicatorType enum values."""

    SUSPICIOUS_USER_AGENT = "SUSPICIOUS_USER_AGENT"
    SUSPICIOUS_NETWORK = "SUSPICIOUS_NETWORK"
    MALICIOUS_IP = "MALICIOUS_IP"
    TOR_IP = "TOR_IP"
    ATTACK_TACTIC = "ATTACK_TACTIC"
    HIGH_RISK_API = "HIGH_RISK_API"
    ATTACK_TECHNIQUE = "ATTACK_TECHNIQUE"
    UNUSUAL_API_FOR_ACCOUNT = "UNUSUAL_API_FOR_ACCOUNT"
    UNUSUAL_ASN_FOR_ACCOUNT = "UNUSUAL_ASN_FOR_ACCOUNT"
    UNUSUAL_ASN_FOR_USER = "UNUSUAL_ASN_FOR_USER"
    SUSPICIOUS_PROCESS = "SUSPICIOUS_PROCESS"
    MALICIOUS_DOMAIN = "MALICIOUS_DOMAIN"
    MALICIOUS_PROCESS = "MALICIOUS_PROCESS"
    CRYPTOMINING_IP = "CRYPTOMINING_IP"
    CRYPTOMINING_DOMAIN = "CRYPTOMINING_DOMAIN"
    CRYPTOMINING_PROCESS = "CRYPTOMINING_PROCESS"


class IpSetFormat:
    """IpSetFormat enum values."""

    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class IpSetStatus:
    """IpSetStatus enum values."""

    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


class KubernetesResourcesTypes:
    """KubernetesResourcesTypes enum values."""

    PODS = "PODS"
    JOBS = "JOBS"
    CRONJOBS = "CRONJOBS"
    DEPLOYMENTS = "DEPLOYMENTS"
    DAEMONSETS = "DAEMONSETS"
    STATEFULSETS = "STATEFULSETS"
    REPLICASETS = "REPLICASETS"
    REPLICATIONCONTROLLERS = "REPLICATIONCONTROLLERS"


class ListMalwareScansCriterionKey:
    """ListMalwareScansCriterionKey enum values."""

    RESOURCE_ARN = "RESOURCE_ARN"
    SCAN_ID = "SCAN_ID"
    ACCOUNT_ID = "ACCOUNT_ID"
    GUARDDUTY_FINDING_ID = "GUARDDUTY_FINDING_ID"
    RESOURCE_TYPE = "RESOURCE_TYPE"
    SCAN_START_TIME = "SCAN_START_TIME"
    SCAN_STATUS = "SCAN_STATUS"
    SCAN_TYPE = "SCAN_TYPE"


class MalwareProtectionPlanStatus:
    """MalwareProtectionPlanStatus enum values."""

    ACTIVE = "ACTIVE"
    WARNING = "WARNING"
    ERROR = "ERROR"


class MalwareProtectionPlanTaggingActionStatus:
    """MalwareProtectionPlanTaggingActionStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MalwareProtectionResourceType:
    """MalwareProtectionResourceType enum values."""

    EBS_RECOVERY_POINT = "EBS_RECOVERY_POINT"
    EBS_SNAPSHOT = "EBS_SNAPSHOT"
    EBS_VOLUME = "EBS_VOLUME"
    EC2_AMI = "EC2_AMI"
    EC2_INSTANCE = "EC2_INSTANCE"
    EC2_RECOVERY_POINT = "EC2_RECOVERY_POINT"
    S3_RECOVERY_POINT = "S3_RECOVERY_POINT"
    S3_BUCKET = "S3_BUCKET"


class MalwareProtectionScanStatus:
    """MalwareProtectionScanStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ISSUES = "COMPLETED_WITH_ISSUES"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class MalwareProtectionScanType:
    """MalwareProtectionScanType enum values."""

    BACKUP_INITIATED = "BACKUP_INITIATED"
    ON_DEMAND = "ON_DEMAND"
    GUARDDUTY_INITIATED = "GUARDDUTY_INITIATED"


class ManagementType:
    """ManagementType enum values."""

    AUTO_MANAGED = "AUTO_MANAGED"
    MANUAL = "MANUAL"
    DISABLED = "DISABLED"


class MfaStatus:
    """MfaStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class NetworkDirection:
    """NetworkDirection enum values."""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"


class OrderBy:
    """OrderBy enum values."""

    ASC = "ASC"
    DESC = "DESC"


class OrgFeature:
    """OrgFeature enum values."""

    S3_DATA_EVENTS = "S3_DATA_EVENTS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    EBS_MALWARE_PROTECTION = "EBS_MALWARE_PROTECTION"
    RDS_LOGIN_EVENTS = "RDS_LOGIN_EVENTS"
    EKS_RUNTIME_MONITORING = "EKS_RUNTIME_MONITORING"
    LAMBDA_NETWORK_LOGS = "LAMBDA_NETWORK_LOGS"
    RUNTIME_MONITORING = "RUNTIME_MONITORING"


class OrgFeatureAdditionalConfiguration:
    """OrgFeatureAdditionalConfiguration enum values."""

    EKS_ADDON_MANAGEMENT = "EKS_ADDON_MANAGEMENT"
    ECS_FARGATE_AGENT_MANAGEMENT = "ECS_FARGATE_AGENT_MANAGEMENT"
    EC2_AGENT_MANAGEMENT = "EC2_AGENT_MANAGEMENT"


class OrgFeatureStatus:
    """OrgFeatureStatus enum values."""

    NEW = "NEW"
    NONE = "NONE"
    ALL = "ALL"


class ProfileSubtype:
    """ProfileSubtype enum values."""

    FREQUENT = "FREQUENT"
    INFREQUENT = "INFREQUENT"
    UNSEEN = "UNSEEN"
    RARE = "RARE"


class ProfileType:
    """ProfileType enum values."""

    FREQUENCY = "FREQUENCY"


class PublicAccessStatus:
    """PublicAccessStatus enum values."""

    BLOCKED = "BLOCKED"
    ALLOWED = "ALLOWED"


class PublicAclIgnoreBehavior:
    """PublicAclIgnoreBehavior enum values."""

    IGNORED = "IGNORED"
    NOT_IGNORED = "NOT_IGNORED"


class PublicBucketRestrictBehavior:
    """PublicBucketRestrictBehavior enum values."""

    RESTRICTED = "RESTRICTED"
    NOT_RESTRICTED = "NOT_RESTRICTED"


class PublishingStatus:
    """PublishingStatus enum values."""

    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    PUBLISHING = "PUBLISHING"
    UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY = "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY"
    STOPPED = "STOPPED"


class ResourceType:
    """ResourceType enum values."""

    EKS = "EKS"
    ECS = "ECS"
    EC2 = "EC2"


class ScanCategory:
    """ScanCategory enum values."""

    FULL_SCAN = "FULL_SCAN"
    INCREMENTAL_SCAN = "INCREMENTAL_SCAN"


class ScanCriterionKey:
    """ScanCriterionKey enum values."""

    EC2_INSTANCE_TAG = "EC2_INSTANCE_TAG"


class ScanResult:
    """ScanResult enum values."""

    CLEAN = "CLEAN"
    INFECTED = "INFECTED"


class ScanResultStatus:
    """ScanResultStatus enum values."""

    NO_THREATS_FOUND = "NO_THREATS_FOUND"
    THREATS_FOUND = "THREATS_FOUND"


class ScanStatus:
    """ScanStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class ScanStatusReason:
    """ScanStatusReason enum values."""

    ACCESS_DENIED = "ACCESS_DENIED"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    SNAPSHOT_SIZE_LIMIT_EXCEEDED = "SNAPSHOT_SIZE_LIMIT_EXCEEDED"
    RESOURCE_UNAVAILABLE = "RESOURCE_UNAVAILABLE"
    INCONSISTENT_SOURCE = "INCONSISTENT_SOURCE"
    INCREMENTAL_NO_DIFFERENCE = "INCREMENTAL_NO_DIFFERENCE"
    NO_EBS_VOLUMES_FOUND = "NO_EBS_VOLUMES_FOUND"
    UNSUPPORTED_PRODUCT_CODE_TYPE = "UNSUPPORTED_PRODUCT_CODE_TYPE"
    AMI_SNAPSHOT_LIMIT_EXCEEDED = "AMI_SNAPSHOT_LIMIT_EXCEEDED"
    UNRELATED_RESOURCES = "UNRELATED_RESOURCES"
    BASE_RESOURCE_NOT_SCANNED = "BASE_RESOURCE_NOT_SCANNED"
    BASE_CREATED_AFTER_TARGET = "BASE_CREATED_AFTER_TARGET"
    UNSUPPORTED_FOR_INCREMENTAL = "UNSUPPORTED_FOR_INCREMENTAL"
    UNSUPPORTED_AMI = "UNSUPPORTED_AMI"
    UNSUPPORTED_SNAPSHOT = "UNSUPPORTED_SNAPSHOT"
    UNSUPPORTED_COMPOSITE_RECOVERY_POINT = "UNSUPPORTED_COMPOSITE_RECOVERY_POINT"


class ScanType:
    """ScanType enum values."""

    GUARDDUTY_INITIATED = "GUARDDUTY_INITIATED"
    ON_DEMAND = "ON_DEMAND"


class SignalType:
    """SignalType enum values."""

    FINDING = "FINDING"
    CLOUD_TRAIL = "CLOUD_TRAIL"
    S3_DATA_EVENTS = "S3_DATA_EVENTS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    FLOW_LOGS = "FLOW_LOGS"
    DNS_LOGS = "DNS_LOGS"
    RUNTIME_MONITORING = "RUNTIME_MONITORING"


class ThreatEntitySetFormat:
    """ThreatEntitySetFormat enum values."""

    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class ThreatEntitySetStatus:
    """ThreatEntitySetStatus enum values."""

    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


class ThreatIntelSetFormat:
    """ThreatIntelSetFormat enum values."""

    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class ThreatIntelSetStatus:
    """ThreatIntelSetStatus enum values."""

    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


class TriggerType:
    """TriggerType enum values."""

    BACKUP = "BACKUP"
    GUARDDUTY = "GUARDDUTY"


class TrustedEntitySetFormat:
    """TrustedEntitySetFormat enum values."""

    TXT = "TXT"
    STIX = "STIX"
    OTX_CSV = "OTX_CSV"
    ALIEN_VAULT = "ALIEN_VAULT"
    PROOF_POINT = "PROOF_POINT"
    FIRE_EYE = "FIRE_EYE"


class TrustedEntitySetStatus:
    """TrustedEntitySetStatus enum values."""

    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATING = "DEACTIVATING"
    ERROR = "ERROR"
    DELETE_PENDING = "DELETE_PENDING"
    DELETED = "DELETED"


class UsageFeature:
    """UsageFeature enum values."""

    FLOW_LOGS = "FLOW_LOGS"
    CLOUD_TRAIL = "CLOUD_TRAIL"
    DNS_LOGS = "DNS_LOGS"
    S3_DATA_EVENTS = "S3_DATA_EVENTS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    EBS_MALWARE_PROTECTION = "EBS_MALWARE_PROTECTION"
    RDS_LOGIN_EVENTS = "RDS_LOGIN_EVENTS"
    LAMBDA_NETWORK_LOGS = "LAMBDA_NETWORK_LOGS"
    EKS_RUNTIME_MONITORING = "EKS_RUNTIME_MONITORING"
    FARGATE_RUNTIME_MONITORING = "FARGATE_RUNTIME_MONITORING"
    EC2_RUNTIME_MONITORING = "EC2_RUNTIME_MONITORING"
    RDS_DBI_PROTECTION_PROVISIONED = "RDS_DBI_PROTECTION_PROVISIONED"
    RDS_DBI_PROTECTION_SERVERLESS = "RDS_DBI_PROTECTION_SERVERLESS"


class UsageStatisticType:
    """UsageStatisticType enum values."""

    SUM_BY_ACCOUNT = "SUM_BY_ACCOUNT"
    SUM_BY_DATA_SOURCE = "SUM_BY_DATA_SOURCE"
    SUM_BY_RESOURCE = "SUM_BY_RESOURCE"
    TOP_RESOURCES = "TOP_RESOURCES"
    SUM_BY_FEATURES = "SUM_BY_FEATURES"
    TOP_ACCOUNTS_BY_FEATURE = "TOP_ACCOUNTS_BY_FEATURE"


@dataclass
class Condition(PropertyType):
    EQUALS = "Equals"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    LT = "Lt"
    GTE = "Gte"
    NEQ = "Neq"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    EQ = "Eq"
    LTE = "Lte"
    GT = "Gt"
    NOT_EQUALS = "NotEquals"

    _property_mappings: ClassVar[dict[str, str]] = {
        "equals": "Equals",
        "less_than": "LessThan",
        "less_than_or_equal": "LessThanOrEqual",
        "greater_than": "GreaterThan",
        "lt": "Lt",
        "gte": "Gte",
        "neq": "Neq",
        "greater_than_or_equal": "GreaterThanOrEqual",
        "eq": "Eq",
        "lte": "Lte",
        "gt": "Gt",
        "not_equals": "NotEquals",
    }

    equals: Optional[Union[list[str], Ref]] = None
    less_than: Optional[Union[int, Ref, GetAtt, Sub]] = None
    less_than_or_equal: Optional[Union[int, Ref, GetAtt, Sub]] = None
    greater_than: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lt: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    neq: Optional[Union[list[str], Ref]] = None
    greater_than_or_equal: Optional[Union[int, Ref, GetAtt, Sub]] = None
    eq: Optional[Union[list[str], Ref]] = None
    lte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gt: Optional[Union[int, Ref, GetAtt, Sub]] = None
    not_equals: Optional[Union[list[str], Ref]] = None


@dataclass
class FindingCriteria(PropertyType):
    CRITERION = "Criterion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "criterion": "Criterion",
    }

    criterion: Optional[dict[str, Any]] = None


@dataclass
class TagItem(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

