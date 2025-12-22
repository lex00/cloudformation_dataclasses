"""PropertyTypes for AWS::Backup::BackupVault."""

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
class LockConfigurationType(PropertyType):
    CHANGEABLE_FOR_DAYS = "ChangeableForDays"
    MAX_RETENTION_DAYS = "MaxRetentionDays"
    MIN_RETENTION_DAYS = "MinRetentionDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "changeable_for_days": "ChangeableForDays",
        "max_retention_days": "MaxRetentionDays",
        "min_retention_days": "MinRetentionDays",
    }

    changeable_for_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationObjectType(PropertyType):
    SNS_TOPIC_ARN = "SNSTopicArn"
    BACKUP_VAULT_EVENTS = "BackupVaultEvents"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_topic_arn": "SNSTopicArn",
        "backup_vault_events": "BackupVaultEvents",
    }

    sns_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    backup_vault_events: Optional[Union[list[str], Ref]] = None

