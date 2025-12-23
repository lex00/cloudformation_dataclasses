"""PropertyTypes for AWS::Backup::BackupVault."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

