"""PropertyTypes for AWS::CodePipeline::Webhook."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionCategory:
    """ActionCategory enum values."""

    SOURCE = "Source"
    BUILD = "Build"
    DEPLOY = "Deploy"
    TEST = "Test"
    INVOKE = "Invoke"
    APPROVAL = "Approval"
    COMPUTE = "Compute"


class ActionConfigurationPropertyType:
    """ActionConfigurationPropertyType enum values."""

    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"


class ActionExecutionStatus:
    """ActionExecutionStatus enum values."""

    INPROGRESS = "InProgress"
    ABANDONED = "Abandoned"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class ActionOwner:
    """ActionOwner enum values."""

    AWS = "AWS"
    THIRDPARTY = "ThirdParty"
    CUSTOM = "Custom"


class ApprovalStatus:
    """ApprovalStatus enum values."""

    APPROVED = "Approved"
    REJECTED = "Rejected"


class ArtifactLocationType:
    """ArtifactLocationType enum values."""

    S3 = "S3"


class ArtifactStoreType:
    """ArtifactStoreType enum values."""

    S3 = "S3"


class BlockerType:
    """BlockerType enum values."""

    SCHEDULE = "Schedule"


class ConditionExecutionStatus:
    """ConditionExecutionStatus enum values."""

    INPROGRESS = "InProgress"
    FAILED = "Failed"
    ERRORED = "Errored"
    SUCCEEDED = "Succeeded"
    CANCELLED = "Cancelled"
    ABANDONED = "Abandoned"
    OVERRIDDEN = "Overridden"


class ConditionType:
    """ConditionType enum values."""

    BEFORE_ENTRY = "BEFORE_ENTRY"
    ON_SUCCESS = "ON_SUCCESS"


class EncryptionKeyType:
    """EncryptionKeyType enum values."""

    KMS = "KMS"


class EnvironmentVariableType:
    """EnvironmentVariableType enum values."""

    PLAINTEXT = "PLAINTEXT"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class ExecutionMode:
    """ExecutionMode enum values."""

    QUEUED = "QUEUED"
    SUPERSEDED = "SUPERSEDED"
    PARALLEL = "PARALLEL"


class ExecutionType:
    """ExecutionType enum values."""

    STANDARD = "STANDARD"
    ROLLBACK = "ROLLBACK"


class ExecutorType:
    """ExecutorType enum values."""

    JOBWORKER = "JobWorker"
    LAMBDA = "Lambda"


class FailureType:
    """FailureType enum values."""

    JOBFAILED = "JobFailed"
    CONFIGURATIONERROR = "ConfigurationError"
    PERMISSIONERROR = "PermissionError"
    REVISIONOUTOFSYNC = "RevisionOutOfSync"
    REVISIONUNAVAILABLE = "RevisionUnavailable"
    SYSTEMUNAVAILABLE = "SystemUnavailable"


class GitPullRequestEventType:
    """GitPullRequestEventType enum values."""

    OPEN = "OPEN"
    UPDATED = "UPDATED"
    CLOSED = "CLOSED"


class JobStatus:
    """JobStatus enum values."""

    CREATED = "Created"
    QUEUED = "Queued"
    DISPATCHED = "Dispatched"
    INPROGRESS = "InProgress"
    TIMEDOUT = "TimedOut"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class PipelineExecutionStatus:
    """PipelineExecutionStatus enum values."""

    CANCELLED = "Cancelled"
    INPROGRESS = "InProgress"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    SUCCEEDED = "Succeeded"
    SUPERSEDED = "Superseded"
    FAILED = "Failed"


class PipelineTriggerProviderType:
    """PipelineTriggerProviderType enum values."""

    CODESTARSOURCECONNECTION = "CodeStarSourceConnection"


class PipelineType:
    """PipelineType enum values."""

    V1 = "V1"
    V2 = "V2"


class Result:
    """Result enum values."""

    ROLLBACK = "ROLLBACK"
    FAIL = "FAIL"
    RETRY = "RETRY"
    SKIP = "SKIP"


class RetryTrigger:
    """RetryTrigger enum values."""

    AUTOMATEDSTAGERETRY = "AutomatedStageRetry"
    MANUALSTAGERETRY = "ManualStageRetry"


class RuleCategory:
    """RuleCategory enum values."""

    RULE = "Rule"


class RuleConfigurationPropertyType:
    """RuleConfigurationPropertyType enum values."""

    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"


class RuleExecutionStatus:
    """RuleExecutionStatus enum values."""

    INPROGRESS = "InProgress"
    ABANDONED = "Abandoned"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class RuleOwner:
    """RuleOwner enum values."""

    AWS = "AWS"


class SourceRevisionType:
    """SourceRevisionType enum values."""

    COMMIT_ID = "COMMIT_ID"
    IMAGE_DIGEST = "IMAGE_DIGEST"
    S3_OBJECT_VERSION_ID = "S3_OBJECT_VERSION_ID"
    S3_OBJECT_KEY = "S3_OBJECT_KEY"


class StageExecutionStatus:
    """StageExecutionStatus enum values."""

    CANCELLED = "Cancelled"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    SUCCEEDED = "Succeeded"
    SKIPPED = "Skipped"


class StageRetryMode:
    """StageRetryMode enum values."""

    FAILED_ACTIONS = "FAILED_ACTIONS"
    ALL_ACTIONS = "ALL_ACTIONS"


class StageTransitionType:
    """StageTransitionType enum values."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class StartTimeRange:
    """StartTimeRange enum values."""

    LATEST = "Latest"
    ALL = "All"


class TargetFilterName:
    """TargetFilterName enum values."""

    TARGET_STATUS = "TARGET_STATUS"


class TriggerType:
    """TriggerType enum values."""

    CREATEPIPELINE = "CreatePipeline"
    STARTPIPELINEEXECUTION = "StartPipelineExecution"
    POLLFORSOURCECHANGES = "PollForSourceChanges"
    WEBHOOK = "Webhook"
    CLOUDWATCHEVENT = "CloudWatchEvent"
    PUTACTIONREVISION = "PutActionRevision"
    WEBHOOKV2 = "WebhookV2"
    MANUALROLLBACK = "ManualRollback"
    AUTOMATEDROLLBACK = "AutomatedRollback"


class WebhookAuthenticationType:
    """WebhookAuthenticationType enum values."""

    GITHUB_HMAC = "GITHUB_HMAC"
    IP = "IP"
    UNAUTHENTICATED = "UNAUTHENTICATED"


@dataclass
class WebhookAuthConfiguration(PropertyType):
    ALLOWED_IP_RANGE = "AllowedIPRange"
    SECRET_TOKEN = "SecretToken"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_ip_range": "AllowedIPRange",
        "secret_token": "SecretToken",
    }

    allowed_ip_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebhookFilterRule(PropertyType):
    JSON_PATH = "JsonPath"
    MATCH_EQUALS = "MatchEquals"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json_path": "JsonPath",
        "match_equals": "MatchEquals",
    }

    json_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_equals: Optional[Union[str, Ref, GetAtt, Sub]] = None

