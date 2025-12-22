"""PropertyTypes for AWS::Backup::BackupPlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AggregationPeriod:
    """AggregationPeriod enum values."""

    ONE_DAY = "ONE_DAY"
    SEVEN_DAYS = "SEVEN_DAYS"
    FOURTEEN_DAYS = "FOURTEEN_DAYS"


class BackupJobState:
    """BackupJobState enum values."""

    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ABORTING = "ABORTING"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    PARTIAL = "PARTIAL"


class BackupJobStatus:
    """BackupJobStatus enum values."""

    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ABORTING = "ABORTING"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    PARTIAL = "PARTIAL"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class BackupVaultEvent:
    """BackupVaultEvent enum values."""

    BACKUP_JOB_STARTED = "BACKUP_JOB_STARTED"
    BACKUP_JOB_COMPLETED = "BACKUP_JOB_COMPLETED"
    BACKUP_JOB_SUCCESSFUL = "BACKUP_JOB_SUCCESSFUL"
    BACKUP_JOB_FAILED = "BACKUP_JOB_FAILED"
    BACKUP_JOB_EXPIRED = "BACKUP_JOB_EXPIRED"
    RESTORE_JOB_STARTED = "RESTORE_JOB_STARTED"
    RESTORE_JOB_COMPLETED = "RESTORE_JOB_COMPLETED"
    RESTORE_JOB_SUCCESSFUL = "RESTORE_JOB_SUCCESSFUL"
    RESTORE_JOB_FAILED = "RESTORE_JOB_FAILED"
    COPY_JOB_STARTED = "COPY_JOB_STARTED"
    COPY_JOB_SUCCESSFUL = "COPY_JOB_SUCCESSFUL"
    COPY_JOB_FAILED = "COPY_JOB_FAILED"
    RECOVERY_POINT_MODIFIED = "RECOVERY_POINT_MODIFIED"
    BACKUP_PLAN_CREATED = "BACKUP_PLAN_CREATED"
    BACKUP_PLAN_MODIFIED = "BACKUP_PLAN_MODIFIED"
    S3_BACKUP_OBJECT_FAILED = "S3_BACKUP_OBJECT_FAILED"
    S3_RESTORE_OBJECT_FAILED = "S3_RESTORE_OBJECT_FAILED"
    CONTINUOUS_BACKUP_INTERRUPTED = "CONTINUOUS_BACKUP_INTERRUPTED"
    RECOVERY_POINT_INDEX_COMPLETED = "RECOVERY_POINT_INDEX_COMPLETED"
    RECOVERY_POINT_INDEX_DELETED = "RECOVERY_POINT_INDEX_DELETED"
    RECOVERY_POINT_INDEXING_FAILED = "RECOVERY_POINT_INDEXING_FAILED"


class ConditionType:
    """ConditionType enum values."""

    STRINGEQUALS = "STRINGEQUALS"


class CopyJobState:
    """CopyJobState enum values."""

    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIAL = "PARTIAL"


class CopyJobStatus:
    """CopyJobStatus enum values."""

    CREATED = "CREATED"
    RUNNING = "RUNNING"
    ABORTING = "ABORTING"
    ABORTED = "ABORTED"
    COMPLETING = "COMPLETING"
    COMPLETED = "COMPLETED"
    FAILING = "FAILING"
    FAILED = "FAILED"
    PARTIAL = "PARTIAL"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class EncryptionKeyType:
    """EncryptionKeyType enum values."""

    AWS_OWNED_KMS_KEY = "AWS_OWNED_KMS_KEY"
    CUSTOMER_MANAGED_KMS_KEY = "CUSTOMER_MANAGED_KMS_KEY"


class Index:
    """Index enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class IndexStatus:
    """IndexStatus enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    DELETING = "DELETING"


class LegalHoldStatus:
    """LegalHoldStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    CANCELING = "CANCELING"
    CANCELED = "CANCELED"


class LifecycleDeleteAfterEvent:
    """LifecycleDeleteAfterEvent enum values."""

    DELETE_AFTER_COPY = "DELETE_AFTER_COPY"


class MalwareScanner:
    """MalwareScanner enum values."""

    GUARDDUTY = "GUARDDUTY"


class MpaRevokeSessionStatus:
    """MpaRevokeSessionStatus enum values."""

    PENDING = "PENDING"
    FAILED = "FAILED"


class MpaSessionStatus:
    """MpaSessionStatus enum values."""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    FAILED = "FAILED"


class RecoveryPointStatus:
    """RecoveryPointStatus enum values."""

    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    DELETING = "DELETING"
    EXPIRED = "EXPIRED"
    AVAILABLE = "AVAILABLE"
    STOPPED = "STOPPED"
    CREATING = "CREATING"


class RestoreDeletionStatus:
    """RestoreDeletionStatus enum values."""

    DELETING = "DELETING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"


class RestoreJobState:
    """RestoreJobState enum values."""

    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class RestoreJobStatus:
    """RestoreJobStatus enum values."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ABORTED = "ABORTED"
    FAILED = "FAILED"


class RestoreTestingRecoveryPointSelectionAlgorithm:
    """RestoreTestingRecoveryPointSelectionAlgorithm enum values."""

    LATEST_WITHIN_WINDOW = "LATEST_WITHIN_WINDOW"
    RANDOM_WITHIN_WINDOW = "RANDOM_WITHIN_WINDOW"


class RestoreTestingRecoveryPointType:
    """RestoreTestingRecoveryPointType enum values."""

    CONTINUOUS = "CONTINUOUS"
    SNAPSHOT = "SNAPSHOT"


class RestoreValidationStatus:
    """RestoreValidationStatus enum values."""

    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"
    TIMED_OUT = "TIMED_OUT"
    VALIDATING = "VALIDATING"


class RuleExecutionType:
    """RuleExecutionType enum values."""

    CONTINUOUS = "CONTINUOUS"
    SNAPSHOTS = "SNAPSHOTS"
    CONTINUOUS_AND_SNAPSHOTS = "CONTINUOUS_AND_SNAPSHOTS"


class ScanFinding:
    """ScanFinding enum values."""

    MALWARE = "MALWARE"


class ScanJobState:
    """ScanJobState enum values."""

    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ISSUES = "COMPLETED_WITH_ISSUES"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class ScanJobStatus:
    """ScanJobStatus enum values."""

    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ISSUES = "COMPLETED_WITH_ISSUES"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class ScanMode:
    """ScanMode enum values."""

    FULL_SCAN = "FULL_SCAN"
    INCREMENTAL_SCAN = "INCREMENTAL_SCAN"


class ScanResourceType:
    """ScanResourceType enum values."""

    EBS = "EBS"
    EC2 = "EC2"
    S3 = "S3"


class ScanResultStatus:
    """ScanResultStatus enum values."""

    NO_THREATS_FOUND = "NO_THREATS_FOUND"
    THREATS_FOUND = "THREATS_FOUND"


class ScanState:
    """ScanState enum values."""

    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ISSUES = "COMPLETED_WITH_ISSUES"
    CREATED = "CREATED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"


class StorageClass:
    """StorageClass enum values."""

    WARM = "WARM"
    COLD = "COLD"
    DELETED = "DELETED"


class VaultState:
    """VaultState enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"


class VaultType:
    """VaultType enum values."""

    BACKUP_VAULT = "BACKUP_VAULT"
    LOGICALLY_AIR_GAPPED_BACKUP_VAULT = "LOGICALLY_AIR_GAPPED_BACKUP_VAULT"
    RESTORE_ACCESS_BACKUP_VAULT = "RESTORE_ACCESS_BACKUP_VAULT"


@dataclass
class AdvancedBackupSettingResourceType(PropertyType):
    BACKUP_OPTIONS = "BackupOptions"
    RESOURCE_TYPE = "ResourceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "backup_options": "BackupOptions",
        "resource_type": "ResourceType",
    }

    backup_options: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BackupPlanResourceType(PropertyType):
    BACKUP_PLAN_NAME = "BackupPlanName"
    ADVANCED_BACKUP_SETTINGS = "AdvancedBackupSettings"
    BACKUP_PLAN_RULE = "BackupPlanRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "backup_plan_name": "BackupPlanName",
        "advanced_backup_settings": "AdvancedBackupSettings",
        "backup_plan_rule": "BackupPlanRule",
    }

    backup_plan_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    advanced_backup_settings: Optional[list[AdvancedBackupSettingResourceType]] = None
    backup_plan_rule: Optional[list[BackupRuleResourceType]] = None


@dataclass
class BackupRuleResourceType(PropertyType):
    COMPLETION_WINDOW_MINUTES = "CompletionWindowMinutes"
    SCHEDULE_EXPRESSION = "ScheduleExpression"
    RECOVERY_POINT_TAGS = "RecoveryPointTags"
    COPY_ACTIONS = "CopyActions"
    ENABLE_CONTINUOUS_BACKUP = "EnableContinuousBackup"
    LIFECYCLE = "Lifecycle"
    INDEX_ACTIONS = "IndexActions"
    TARGET_BACKUP_VAULT = "TargetBackupVault"
    START_WINDOW_MINUTES = "StartWindowMinutes"
    SCHEDULE_EXPRESSION_TIMEZONE = "ScheduleExpressionTimezone"
    TARGET_LOGICALLY_AIR_GAPPED_BACKUP_VAULT_ARN = "TargetLogicallyAirGappedBackupVaultArn"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "completion_window_minutes": "CompletionWindowMinutes",
        "schedule_expression": "ScheduleExpression",
        "recovery_point_tags": "RecoveryPointTags",
        "copy_actions": "CopyActions",
        "enable_continuous_backup": "EnableContinuousBackup",
        "lifecycle": "Lifecycle",
        "index_actions": "IndexActions",
        "target_backup_vault": "TargetBackupVault",
        "start_window_minutes": "StartWindowMinutes",
        "schedule_expression_timezone": "ScheduleExpressionTimezone",
        "target_logically_air_gapped_backup_vault_arn": "TargetLogicallyAirGappedBackupVaultArn",
        "rule_name": "RuleName",
    }

    completion_window_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recovery_point_tags: Optional[dict[str, str]] = None
    copy_actions: Optional[list[CopyActionResourceType]] = None
    enable_continuous_backup: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    lifecycle: Optional[LifecycleResourceType] = None
    index_actions: Optional[list[IndexActionsResourceType]] = None
    target_backup_vault: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_window_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    schedule_expression_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_logically_air_gapped_backup_vault_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CopyActionResourceType(PropertyType):
    LIFECYCLE = "Lifecycle"
    DESTINATION_BACKUP_VAULT_ARN = "DestinationBackupVaultArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle": "Lifecycle",
        "destination_backup_vault_arn": "DestinationBackupVaultArn",
    }

    lifecycle: Optional[LifecycleResourceType] = None
    destination_backup_vault_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IndexActionsResourceType(PropertyType):
    RESOURCE_TYPES = "ResourceTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_types": "ResourceTypes",
    }

    resource_types: Optional[Union[list[str], Ref]] = None


@dataclass
class LifecycleResourceType(PropertyType):
    OPT_IN_TO_ARCHIVE_FOR_SUPPORTED_RESOURCES = "OptInToArchiveForSupportedResources"
    DELETE_AFTER_DAYS = "DeleteAfterDays"
    MOVE_TO_COLD_STORAGE_AFTER_DAYS = "MoveToColdStorageAfterDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "opt_in_to_archive_for_supported_resources": "OptInToArchiveForSupportedResources",
        "delete_after_days": "DeleteAfterDays",
        "move_to_cold_storage_after_days": "MoveToColdStorageAfterDays",
    }

    opt_in_to_archive_for_supported_resources: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    delete_after_days: Optional[Union[float, Ref, GetAtt, Sub]] = None
    move_to_cold_storage_after_days: Optional[Union[float, Ref, GetAtt, Sub]] = None

