"""PropertyTypes for AWS::Backup::LogicallyAirGappedBackupVault."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

