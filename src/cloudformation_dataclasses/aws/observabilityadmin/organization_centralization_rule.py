"""PropertyTypes for AWS::ObservabilityAdmin::OrganizationCentralizationRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CentralizationRule(PropertyType):
    DESTINATION = "Destination"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
    }

    destination: Optional[CentralizationRuleDestination] = None
    source: Optional[CentralizationRuleSource] = None


@dataclass
class CentralizationRuleDestination(PropertyType):
    ACCOUNT = "Account"
    DESTINATION_LOGS_CONFIGURATION = "DestinationLogsConfiguration"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account": "Account",
        "destination_logs_configuration": "DestinationLogsConfiguration",
        "region": "Region",
    }

    account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_logs_configuration: Optional[DestinationLogsConfiguration] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CentralizationRuleSource(PropertyType):
    SCOPE = "Scope"
    SOURCE_LOGS_CONFIGURATION = "SourceLogsConfiguration"
    REGIONS = "Regions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "source_logs_configuration": "SourceLogsConfiguration",
        "regions": "Regions",
    }

    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_logs_configuration: Optional[SourceLogsConfiguration] = None
    regions: Optional[Union[list[str], Ref]] = None


@dataclass
class DestinationLogsConfiguration(PropertyType):
    LOGS_ENCRYPTION_CONFIGURATION = "LogsEncryptionConfiguration"
    BACKUP_CONFIGURATION = "BackupConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logs_encryption_configuration": "LogsEncryptionConfiguration",
        "backup_configuration": "BackupConfiguration",
    }

    logs_encryption_configuration: Optional[LogsEncryptionConfiguration] = None
    backup_configuration: Optional[LogsBackupConfiguration] = None


@dataclass
class LogsBackupConfiguration(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "region": "Region",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogsEncryptionConfiguration(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    ENCRYPTION_STRATEGY = "EncryptionStrategy"
    ENCRYPTION_CONFLICT_RESOLUTION_STRATEGY = "EncryptionConflictResolutionStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "encryption_strategy": "EncryptionStrategy",
        "encryption_conflict_resolution_strategy": "EncryptionConflictResolutionStrategy",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_strategy: Optional[Union[str, EncryptionStrategy, Ref, GetAtt, Sub]] = None
    encryption_conflict_resolution_strategy: Optional[Union[str, EncryptionConflictResolutionStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class SourceLogsConfiguration(PropertyType):
    ENCRYPTED_LOG_GROUP_STRATEGY = "EncryptedLogGroupStrategy"
    LOG_GROUP_SELECTION_CRITERIA = "LogGroupSelectionCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encrypted_log_group_strategy": "EncryptedLogGroupStrategy",
        "log_group_selection_criteria": "LogGroupSelectionCriteria",
    }

    encrypted_log_group_strategy: Optional[Union[str, EncryptedLogGroupStrategy, Ref, GetAtt, Sub]] = None
    log_group_selection_criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None

