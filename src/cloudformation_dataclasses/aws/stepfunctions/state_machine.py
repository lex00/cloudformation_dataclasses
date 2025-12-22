"""PropertyTypes for AWS::StepFunctions::StateMachine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class EncryptionType:
    """EncryptionType enum values."""

    AWS_OWNED_KEY = "AWS_OWNED_KEY"
    CUSTOMER_MANAGED_KMS_KEY = "CUSTOMER_MANAGED_KMS_KEY"


class ExecutionRedriveFilter:
    """ExecutionRedriveFilter enum values."""

    REDRIVEN = "REDRIVEN"
    NOT_REDRIVEN = "NOT_REDRIVEN"


class ExecutionRedriveStatus:
    """ExecutionRedriveStatus enum values."""

    REDRIVABLE = "REDRIVABLE"
    NOT_REDRIVABLE = "NOT_REDRIVABLE"
    REDRIVABLE_BY_MAP_RUN = "REDRIVABLE_BY_MAP_RUN"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    ABORTED = "ABORTED"
    PENDING_REDRIVE = "PENDING_REDRIVE"


class HistoryEventType:
    """HistoryEventType enum values."""

    ACTIVITYFAILED = "ActivityFailed"
    ACTIVITYSCHEDULED = "ActivityScheduled"
    ACTIVITYSCHEDULEFAILED = "ActivityScheduleFailed"
    ACTIVITYSTARTED = "ActivityStarted"
    ACTIVITYSUCCEEDED = "ActivitySucceeded"
    ACTIVITYTIMEDOUT = "ActivityTimedOut"
    CHOICESTATEENTERED = "ChoiceStateEntered"
    CHOICESTATEEXITED = "ChoiceStateExited"
    EXECUTIONABORTED = "ExecutionAborted"
    EXECUTIONFAILED = "ExecutionFailed"
    EXECUTIONSTARTED = "ExecutionStarted"
    EXECUTIONSUCCEEDED = "ExecutionSucceeded"
    EXECUTIONTIMEDOUT = "ExecutionTimedOut"
    FAILSTATEENTERED = "FailStateEntered"
    LAMBDAFUNCTIONFAILED = "LambdaFunctionFailed"
    LAMBDAFUNCTIONSCHEDULED = "LambdaFunctionScheduled"
    LAMBDAFUNCTIONSCHEDULEFAILED = "LambdaFunctionScheduleFailed"
    LAMBDAFUNCTIONSTARTED = "LambdaFunctionStarted"
    LAMBDAFUNCTIONSTARTFAILED = "LambdaFunctionStartFailed"
    LAMBDAFUNCTIONSUCCEEDED = "LambdaFunctionSucceeded"
    LAMBDAFUNCTIONTIMEDOUT = "LambdaFunctionTimedOut"
    MAPITERATIONABORTED = "MapIterationAborted"
    MAPITERATIONFAILED = "MapIterationFailed"
    MAPITERATIONSTARTED = "MapIterationStarted"
    MAPITERATIONSUCCEEDED = "MapIterationSucceeded"
    MAPSTATEABORTED = "MapStateAborted"
    MAPSTATEENTERED = "MapStateEntered"
    MAPSTATEEXITED = "MapStateExited"
    MAPSTATEFAILED = "MapStateFailed"
    MAPSTATESTARTED = "MapStateStarted"
    MAPSTATESUCCEEDED = "MapStateSucceeded"
    PARALLELSTATEABORTED = "ParallelStateAborted"
    PARALLELSTATEENTERED = "ParallelStateEntered"
    PARALLELSTATEEXITED = "ParallelStateExited"
    PARALLELSTATEFAILED = "ParallelStateFailed"
    PARALLELSTATESTARTED = "ParallelStateStarted"
    PARALLELSTATESUCCEEDED = "ParallelStateSucceeded"
    PASSSTATEENTERED = "PassStateEntered"
    PASSSTATEEXITED = "PassStateExited"
    SUCCEEDSTATEENTERED = "SucceedStateEntered"
    SUCCEEDSTATEEXITED = "SucceedStateExited"
    TASKFAILED = "TaskFailed"
    TASKSCHEDULED = "TaskScheduled"
    TASKSTARTED = "TaskStarted"
    TASKSTARTFAILED = "TaskStartFailed"
    TASKSTATEABORTED = "TaskStateAborted"
    TASKSTATEENTERED = "TaskStateEntered"
    TASKSTATEEXITED = "TaskStateExited"
    TASKSUBMITFAILED = "TaskSubmitFailed"
    TASKSUBMITTED = "TaskSubmitted"
    TASKSUCCEEDED = "TaskSucceeded"
    TASKTIMEDOUT = "TaskTimedOut"
    WAITSTATEABORTED = "WaitStateAborted"
    WAITSTATEENTERED = "WaitStateEntered"
    WAITSTATEEXITED = "WaitStateExited"
    MAPRUNABORTED = "MapRunAborted"
    MAPRUNFAILED = "MapRunFailed"
    MAPRUNSTARTED = "MapRunStarted"
    MAPRUNSUCCEEDED = "MapRunSucceeded"
    EXECUTIONREDRIVEN = "ExecutionRedriven"
    MAPRUNREDRIVEN = "MapRunRedriven"
    EVALUATIONFAILED = "EvaluationFailed"


class IncludedData:
    """IncludedData enum values."""

    ALL_DATA = "ALL_DATA"
    METADATA_ONLY = "METADATA_ONLY"


class InspectionLevel:
    """InspectionLevel enum values."""

    INFO = "INFO"
    DEBUG = "DEBUG"
    TRACE = "TRACE"


class KmsKeyState:
    """KmsKeyState enum values."""

    DISABLED = "DISABLED"
    PENDING_DELETION = "PENDING_DELETION"
    PENDING_IMPORT = "PENDING_IMPORT"
    UNAVAILABLE = "UNAVAILABLE"
    CREATING = "CREATING"


class LogLevel:
    """LogLevel enum values."""

    ALL = "ALL"
    ERROR = "ERROR"
    FATAL = "FATAL"
    OFF = "OFF"


class MapRunStatus:
    """MapRunStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    ABORTED = "ABORTED"


class MockResponseValidationMode:
    """MockResponseValidationMode enum values."""

    STRICT = "STRICT"
    PRESENT = "PRESENT"
    NONE = "NONE"


class StateMachineStatus:
    """StateMachineStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class StateMachineType:
    """StateMachineType enum values."""

    STANDARD = "STANDARD"
    EXPRESS = "EXPRESS"


class SyncExecutionStatus:
    """SyncExecutionStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"


class TestExecutionStatus:
    """TestExecutionStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    RETRIABLE = "RETRIABLE"
    CAUGHT_ERROR = "CAUGHT_ERROR"


class ValidateStateMachineDefinitionResultCode:
    """ValidateStateMachineDefinitionResultCode enum values."""

    OK = "OK"
    FAIL = "FAIL"


class ValidateStateMachineDefinitionSeverity:
    """ValidateStateMachineDefinitionSeverity enum values."""

    ERROR = "ERROR"
    WARNING = "WARNING"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    API_DOES_NOT_SUPPORT_LABELED_ARNS = "API_DOES_NOT_SUPPORT_LABELED_ARNS"
    MISSING_REQUIRED_PARAMETER = "MISSING_REQUIRED_PARAMETER"
    CANNOT_UPDATE_COMPLETED_MAP_RUN = "CANNOT_UPDATE_COMPLETED_MAP_RUN"
    INVALID_ROUTING_CONFIGURATION = "INVALID_ROUTING_CONFIGURATION"


@dataclass
class CloudWatchLogsLogGroup(PropertyType):
    LOG_GROUP_ARN = "LogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    TYPE = "Type"
    KMS_KEY_ID = "KmsKeyId"
    KMS_DATA_KEY_REUSE_PERIOD_SECONDS = "KmsDataKeyReusePeriodSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "kms_key_id": "KmsKeyId",
        "kms_data_key_reuse_period_seconds": "KmsDataKeyReusePeriodSeconds",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_data_key_reuse_period_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LogDestination(PropertyType):
    CLOUD_WATCH_LOGS_LOG_GROUP = "CloudWatchLogsLogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_log_group": "CloudWatchLogsLogGroup",
    }

    cloud_watch_logs_log_group: Optional[CloudWatchLogsLogGroup] = None


@dataclass
class LoggingConfiguration(PropertyType):
    INCLUDE_EXECUTION_DATA = "IncludeExecutionData"
    DESTINATIONS = "Destinations"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_execution_data": "IncludeExecutionData",
        "destinations": "Destinations",
        "level": "Level",
    }

    include_execution_data: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    destinations: Optional[list[LogDestination]] = None
    level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    VERSION = "Version"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagsEntry(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TracingConfiguration(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

