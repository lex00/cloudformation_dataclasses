"""PropertyTypes for AWS::Backup::BackupPlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedBackupSettingResourceType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "backup_options": "BackupOptions",
        "resource_type": "ResourceType",
    }

    backup_options: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BackupPlanResourceType(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle": "Lifecycle",
        "destination_backup_vault_arn": "DestinationBackupVaultArn",
    }

    lifecycle: Optional[LifecycleResourceType] = None
    destination_backup_vault_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IndexActionsResourceType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_types": "ResourceTypes",
    }

    resource_types: Optional[Union[list[str], Ref]] = None


@dataclass
class LifecycleResourceType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "opt_in_to_archive_for_supported_resources": "OptInToArchiveForSupportedResources",
        "delete_after_days": "DeleteAfterDays",
        "move_to_cold_storage_after_days": "MoveToColdStorageAfterDays",
    }

    opt_in_to_archive_for_supported_resources: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    delete_after_days: Optional[Union[float, Ref, GetAtt, Sub]] = None
    move_to_cold_storage_after_days: Optional[Union[float, Ref, GetAtt, Sub]] = None

