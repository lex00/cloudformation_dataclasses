"""PropertyTypes for AWS::ObservabilityAdmin::OrganizationCentralizationRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Action:
    """Action enum values."""

    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    COUNT = "COUNT"
    CAPTCHA = "CAPTCHA"
    CHALLENGE = "CHALLENGE"
    EXCLUDED_AS_COUNT = "EXCLUDED_AS_COUNT"


class CentralizationFailureReason:
    """CentralizationFailureReason enum values."""

    TRUSTED_ACCESS_NOT_ENABLED = "TRUSTED_ACCESS_NOT_ENABLED"
    DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION = "DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"


class DestinationType:
    """DestinationType enum values."""

    CLOUD_WATCH_LOGS = "cloud-watch-logs"


class EncryptedLogGroupStrategy:
    """EncryptedLogGroupStrategy enum values."""

    ALLOW = "ALLOW"
    SKIP = "SKIP"


class EncryptionConflictResolutionStrategy:
    """EncryptionConflictResolutionStrategy enum values."""

    ALLOW = "ALLOW"
    SKIP = "SKIP"


class EncryptionStrategy:
    """EncryptionStrategy enum values."""

    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    AWS_OWNED = "AWS_OWNED"


class FilterBehavior:
    """FilterBehavior enum values."""

    KEEP = "KEEP"
    DROP = "DROP"


class FilterRequirement:
    """FilterRequirement enum values."""

    MEETS_ALL = "MEETS_ALL"
    MEETS_ANY = "MEETS_ANY"


class IntegrationStatus:
    """IntegrationStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class LogType:
    """LogType enum values."""

    APPLICATION_LOGS = "APPLICATION_LOGS"
    USAGE_LOGS = "USAGE_LOGS"


class OutputFormat:
    """OutputFormat enum values."""

    PLAIN = "plain"
    JSON = "json"


class RecordFormat:
    """RecordFormat enum values."""

    STRING = "STRING"
    JSON = "JSON"


class ResourceType:
    """ResourceType enum values."""

    AWS_EC2_INSTANCE = "AWS::EC2::Instance"
    AWS_EC2_VPC = "AWS::EC2::VPC"
    AWS_LAMBDA_FUNCTION = "AWS::Lambda::Function"
    AWS_CLOUDTRAIL = "AWS::CloudTrail"
    AWS_EKS_CLUSTER = "AWS::EKS::Cluster"
    AWS_WAFV2_WEBACL = "AWS::WAFv2::WebACL"
    AWS_ELASTICLOADBALANCINGV2_LOADBALANCER = "AWS::ElasticLoadBalancingV2::LoadBalancer"
    AWS_ROUTE53RESOLVER_RESOLVERENDPOINT = "AWS::Route53Resolver::ResolverEndpoint"
    AWS_BEDROCKAGENTCORE_RUNTIME = "AWS::BedrockAgentCore::Runtime"
    AWS_BEDROCKAGENTCORE_BROWSER = "AWS::BedrockAgentCore::Browser"
    AWS_BEDROCKAGENTCORE_CODEINTERPRETER = "AWS::BedrockAgentCore::CodeInterpreter"


class RuleHealth:
    """RuleHealth enum values."""

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    PROVISIONING = "Provisioning"


class SSEAlgorithm:
    """SSEAlgorithm enum values."""

    AWS_KMS = "aws:kms"
    AES256 = "AES256"


class Status:
    """Status enum values."""

    NOT_STARTED = "NOT_STARTED"
    STARTING = "STARTING"
    FAILED_START = "FAILED_START"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    FAILED_STOP = "FAILED_STOP"
    STOPPED = "STOPPED"


class TelemetryEnrichmentStatus:
    """TelemetryEnrichmentStatus enum values."""

    RUNNING = "Running"
    STOPPED = "Stopped"
    IMPAIRED = "Impaired"


class TelemetryPipelineStatus:
    """TelemetryPipelineStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"


class TelemetrySourceType:
    """TelemetrySourceType enum values."""

    VPC_FLOW_LOGS = "VPC_FLOW_LOGS"
    ROUTE53_RESOLVER_QUERY_LOGS = "ROUTE53_RESOLVER_QUERY_LOGS"
    EKS_AUDIT_LOGS = "EKS_AUDIT_LOGS"
    EKS_AUTHENTICATOR_LOGS = "EKS_AUTHENTICATOR_LOGS"
    EKS_CONTROLLER_MANAGER_LOGS = "EKS_CONTROLLER_MANAGER_LOGS"
    EKS_SCHEDULER_LOGS = "EKS_SCHEDULER_LOGS"
    EKS_API_LOGS = "EKS_API_LOGS"


class TelemetryState:
    """TelemetryState enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    NOTAPPLICABLE = "NotApplicable"


class TelemetryType:
    """TelemetryType enum values."""

    LOGS = "Logs"
    METRICS = "Metrics"
    TRACES = "Traces"


class WAFLogType:
    """WAFLogType enum values."""

    WAF_LOGS = "WAF_LOGS"


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

