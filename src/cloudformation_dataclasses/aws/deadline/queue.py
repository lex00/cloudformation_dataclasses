"""PropertyTypes for AWS::Deadline::Queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratorName:
    """AcceleratorName enum values."""

    T4 = "t4"
    A10G = "a10g"
    L4 = "l4"
    L40S = "l40s"


class AcceleratorType:
    """AcceleratorType enum values."""

    GPU = "gpu"


class AutoScalingMode:
    """AutoScalingMode enum values."""

    NO_SCALING = "NO_SCALING"
    EVENT_BASED_AUTO_SCALING = "EVENT_BASED_AUTO_SCALING"


class AutoScalingStatus:
    """AutoScalingStatus enum values."""

    GROWING = "GROWING"
    STEADY = "STEADY"
    SHRINKING = "SHRINKING"


class BudgetActionType:
    """BudgetActionType enum values."""

    STOP_SCHEDULING_AND_COMPLETE_TASKS = "STOP_SCHEDULING_AND_COMPLETE_TASKS"
    STOP_SCHEDULING_AND_CANCEL_TASKS = "STOP_SCHEDULING_AND_CANCEL_TASKS"


class BudgetStatus:
    """BudgetStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    GREATER_THAN_EQUAL_TO = "GREATER_THAN_EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN_EQUAL_TO = "LESS_THAN_EQUAL_TO"
    LESS_THAN = "LESS_THAN"


class CompletedStatus:
    """CompletedStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    INTERRUPTED = "INTERRUPTED"
    CANCELED = "CANCELED"
    NEVER_ATTEMPTED = "NEVER_ATTEMPTED"


class ConflictExceptionReason:
    """ConflictExceptionReason enum values."""

    CONFLICT_EXCEPTION = "CONFLICT_EXCEPTION"
    CONCURRENT_MODIFICATION = "CONCURRENT_MODIFICATION"
    RESOURCE_ALREADY_EXISTS = "RESOURCE_ALREADY_EXISTS"
    RESOURCE_IN_USE = "RESOURCE_IN_USE"
    STATUS_CONFLICT = "STATUS_CONFLICT"


class CpuArchitectureType:
    """CpuArchitectureType enum values."""

    X86_64 = "x86_64"
    ARM64 = "arm64"


class CreateJobTargetTaskRunStatus:
    """CreateJobTargetTaskRunStatus enum values."""

    READY = "READY"
    SUSPENDED = "SUSPENDED"


class CustomerManagedFleetOperatingSystemFamily:
    """CustomerManagedFleetOperatingSystemFamily enum values."""

    WINDOWS = "WINDOWS"
    LINUX = "LINUX"
    MACOS = "MACOS"


class DefaultQueueBudgetAction:
    """DefaultQueueBudgetAction enum values."""

    NONE = "NONE"
    STOP_SCHEDULING_AND_COMPLETE_TASKS = "STOP_SCHEDULING_AND_COMPLETE_TASKS"
    STOP_SCHEDULING_AND_CANCEL_TASKS = "STOP_SCHEDULING_AND_CANCEL_TASKS"


class DependencyConsumerResolutionStatus:
    """DependencyConsumerResolutionStatus enum values."""

    RESOLVED = "RESOLVED"
    UNRESOLVED = "UNRESOLVED"


class DesiredWorkerStatus:
    """DesiredWorkerStatus enum values."""

    STOPPED = "STOPPED"


class Ec2MarketType:
    """Ec2MarketType enum values."""

    ON_DEMAND = "on-demand"
    SPOT = "spot"
    WAIT_AND_SAVE = "wait-and-save"


class EnvironmentTemplateType:
    """EnvironmentTemplateType enum values."""

    JSON = "JSON"
    YAML = "YAML"


class FileSystemLocationType:
    """FileSystemLocationType enum values."""

    SHARED = "SHARED"
    LOCAL = "LOCAL"


class FleetStatus:
    """FleetStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    SUSPENDED = "SUSPENDED"


class JobAttachmentsFileSystem:
    """JobAttachmentsFileSystem enum values."""

    COPIED = "COPIED"
    VIRTUAL = "VIRTUAL"


class JobEntityErrorCode:
    """JobEntityErrorCode enum values."""

    ACCESSDENIEDEXCEPTION = "AccessDeniedException"
    INTERNALSERVEREXCEPTION = "InternalServerException"
    VALIDATIONEXCEPTION = "ValidationException"
    RESOURCENOTFOUNDEXCEPTION = "ResourceNotFoundException"
    MAXPAYLOADSIZEEXCEEDED = "MaxPayloadSizeExceeded"
    CONFLICTEXCEPTION = "ConflictException"


class JobLifecycleStatus:
    """JobLifecycleStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    UPLOAD_IN_PROGRESS = "UPLOAD_IN_PROGRESS"
    UPLOAD_FAILED = "UPLOAD_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_SUCCEEDED = "UPDATE_SUCCEEDED"
    ARCHIVED = "ARCHIVED"


class JobTargetTaskRunStatus:
    """JobTargetTaskRunStatus enum values."""

    READY = "READY"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    CANCELED = "CANCELED"
    SUSPENDED = "SUSPENDED"
    PENDING = "PENDING"


class JobTemplateType:
    """JobTemplateType enum values."""

    JSON = "JSON"
    YAML = "YAML"


class LicenseEndpointStatus:
    """LicenseEndpointStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    READY = "READY"
    NOT_READY = "NOT_READY"


class LogicalOperator:
    """LogicalOperator enum values."""

    AND = "AND"
    OR = "OR"


class MembershipLevel:
    """MembershipLevel enum values."""

    VIEWER = "VIEWER"
    CONTRIBUTOR = "CONTRIBUTOR"
    OWNER = "OWNER"
    MANAGER = "MANAGER"


class PathFormat:
    """PathFormat enum values."""

    WINDOWS = "windows"
    POSIX = "posix"


class Period:
    """Period enum values."""

    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class PrincipalType:
    """PrincipalType enum values."""

    USER = "USER"
    GROUP = "GROUP"


class QueueBlockedReason:
    """QueueBlockedReason enum values."""

    NO_BUDGET_CONFIGURED = "NO_BUDGET_CONFIGURED"
    BUDGET_THRESHOLD_REACHED = "BUDGET_THRESHOLD_REACHED"


class QueueFleetAssociationStatus:
    """QueueFleetAssociationStatus enum values."""

    ACTIVE = "ACTIVE"
    STOP_SCHEDULING_AND_COMPLETE_TASKS = "STOP_SCHEDULING_AND_COMPLETE_TASKS"
    STOP_SCHEDULING_AND_CANCEL_TASKS = "STOP_SCHEDULING_AND_CANCEL_TASKS"
    STOPPED = "STOPPED"


class QueueLimitAssociationStatus:
    """QueueLimitAssociationStatus enum values."""

    ACTIVE = "ACTIVE"
    STOP_LIMIT_USAGE_AND_COMPLETE_TASKS = "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS"
    STOP_LIMIT_USAGE_AND_CANCEL_TASKS = "STOP_LIMIT_USAGE_AND_CANCEL_TASKS"
    STOPPED = "STOPPED"


class QueueStatus:
    """QueueStatus enum values."""

    IDLE = "IDLE"
    SCHEDULING = "SCHEDULING"
    SCHEDULING_BLOCKED = "SCHEDULING_BLOCKED"


class RunAs:
    """RunAs enum values."""

    QUEUE_CONFIGURED_USER = "QUEUE_CONFIGURED_USER"
    WORKER_AGENT_USER = "WORKER_AGENT_USER"


class SearchTermMatchingType:
    """SearchTermMatchingType enum values."""

    FUZZY_MATCH = "FUZZY_MATCH"
    CONTAINS = "CONTAINS"


class ServiceManagedFleetOperatingSystemFamily:
    """ServiceManagedFleetOperatingSystemFamily enum values."""

    WINDOWS = "WINDOWS"
    LINUX = "LINUX"


class ServiceQuotaExceededExceptionReason:
    """ServiceQuotaExceededExceptionReason enum values."""

    SERVICE_QUOTA_EXCEEDED_EXCEPTION = "SERVICE_QUOTA_EXCEEDED_EXCEPTION"
    KMS_KEY_LIMIT_EXCEEDED = "KMS_KEY_LIMIT_EXCEEDED"
    DEPENDENCY_LIMIT_EXCEEDED = "DEPENDENCY_LIMIT_EXCEEDED"


class SessionActionStatus:
    """SessionActionStatus enum values."""

    ASSIGNED = "ASSIGNED"
    RUNNING = "RUNNING"
    CANCELING = "CANCELING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    INTERRUPTED = "INTERRUPTED"
    CANCELED = "CANCELED"
    NEVER_ATTEMPTED = "NEVER_ATTEMPTED"
    SCHEDULED = "SCHEDULED"
    RECLAIMING = "RECLAIMING"
    RECLAIMED = "RECLAIMED"


class SessionLifecycleStatus:
    """SessionLifecycleStatus enum values."""

    STARTED = "STARTED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCEEDED = "UPDATE_SUCCEEDED"
    UPDATE_FAILED = "UPDATE_FAILED"
    ENDED = "ENDED"


class SessionLifecycleTargetStatus:
    """SessionLifecycleTargetStatus enum values."""

    ENDED = "ENDED"


class SessionsStatisticsAggregationStatus:
    """SessionsStatisticsAggregationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    TIMEOUT = "TIMEOUT"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class StepLifecycleStatus:
    """StepLifecycleStatus enum values."""

    CREATE_COMPLETE = "CREATE_COMPLETE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_SUCCEEDED = "UPDATE_SUCCEEDED"


class StepParameterType:
    """StepParameterType enum values."""

    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"
    PATH = "PATH"
    CHUNK_INT = "CHUNK_INT"


class StepTargetTaskRunStatus:
    """StepTargetTaskRunStatus enum values."""

    READY = "READY"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    CANCELED = "CANCELED"
    SUSPENDED = "SUSPENDED"
    PENDING = "PENDING"


class StorageProfileOperatingSystemFamily:
    """StorageProfileOperatingSystemFamily enum values."""

    WINDOWS = "WINDOWS"
    LINUX = "LINUX"
    MACOS = "MACOS"


class TagPropagationMode:
    """TagPropagationMode enum values."""

    NO_PROPAGATION = "NO_PROPAGATION"
    PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH = "PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH"


class TaskRunStatus:
    """TaskRunStatus enum values."""

    PENDING = "PENDING"
    READY = "READY"
    ASSIGNED = "ASSIGNED"
    STARTING = "STARTING"
    SCHEDULED = "SCHEDULED"
    INTERRUPTING = "INTERRUPTING"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    NOT_COMPATIBLE = "NOT_COMPATIBLE"


class TaskTargetRunStatus:
    """TaskTargetRunStatus enum values."""

    READY = "READY"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    CANCELED = "CANCELED"
    SUSPENDED = "SUSPENDED"
    PENDING = "PENDING"


class UpdateJobLifecycleStatus:
    """UpdateJobLifecycleStatus enum values."""

    ARCHIVED = "ARCHIVED"


class UpdateQueueFleetAssociationStatus:
    """UpdateQueueFleetAssociationStatus enum values."""

    ACTIVE = "ACTIVE"
    STOP_SCHEDULING_AND_COMPLETE_TASKS = "STOP_SCHEDULING_AND_COMPLETE_TASKS"
    STOP_SCHEDULING_AND_CANCEL_TASKS = "STOP_SCHEDULING_AND_CANCEL_TASKS"


class UpdateQueueLimitAssociationStatus:
    """UpdateQueueLimitAssociationStatus enum values."""

    ACTIVE = "ACTIVE"
    STOP_LIMIT_USAGE_AND_COMPLETE_TASKS = "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS"
    STOP_LIMIT_USAGE_AND_CANCEL_TASKS = "STOP_LIMIT_USAGE_AND_CANCEL_TASKS"


class UpdatedWorkerStatus:
    """UpdatedWorkerStatus enum values."""

    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class UsageGroupByField:
    """UsageGroupByField enum values."""

    QUEUE_ID = "QUEUE_ID"
    FLEET_ID = "FLEET_ID"
    JOB_ID = "JOB_ID"
    USER_ID = "USER_ID"
    USAGE_TYPE = "USAGE_TYPE"
    INSTANCE_TYPE = "INSTANCE_TYPE"
    LICENSE_PRODUCT = "LICENSE_PRODUCT"


class UsageStatistic:
    """UsageStatistic enum values."""

    SUM = "SUM"
    MIN = "MIN"
    MAX = "MAX"
    AVG = "AVG"


class UsageType:
    """UsageType enum values."""

    COMPUTE = "COMPUTE"
    LICENSE = "LICENSE"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


class WorkerStatus:
    """WorkerStatus enum values."""

    CREATED = "CREATED"
    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    NOT_RESPONDING = "NOT_RESPONDING"
    NOT_COMPATIBLE = "NOT_COMPATIBLE"
    RUNNING = "RUNNING"
    IDLE = "IDLE"


@dataclass
class JobAttachmentSettings(PropertyType):
    ROOT_PREFIX = "RootPrefix"
    S3_BUCKET_NAME = "S3BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "root_prefix": "RootPrefix",
        "s3_bucket_name": "S3BucketName",
    }

    root_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JobRunAsUser(PropertyType):
    RUN_AS = "RunAs"
    POSIX = "Posix"
    WINDOWS = "Windows"

    _property_mappings: ClassVar[dict[str, str]] = {
        "run_as": "RunAs",
        "posix": "Posix",
        "windows": "Windows",
    }

    run_as: Optional[Union[str, Ref, GetAtt, Sub]] = None
    posix: Optional[PosixUser] = None
    windows: Optional[WindowsUser] = None


@dataclass
class PosixUser(PropertyType):
    GROUP = "Group"
    USER = "User"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group": "Group",
        "user": "User",
    }

    group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WindowsUser(PropertyType):
    USER = "User"
    PASSWORD_ARN = "PasswordArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user": "User",
        "password_arn": "PasswordArn",
    }

    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

