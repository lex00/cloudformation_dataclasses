"""PropertyTypes for AWS::Batch::JobQueue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ArrayJobDependency:
    """ArrayJobDependency enum values."""

    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEState:
    """CEState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEStatus:
    """CEStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class CEType:
    """CEType enum values."""

    MANAGED = "MANAGED"
    UNMANAGED = "UNMANAGED"


class CRAllocationStrategy:
    """CRAllocationStrategy enum values."""

    BEST_FIT = "BEST_FIT"
    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"


class CRType:
    """CRType enum values."""

    EC2 = "EC2"
    SPOT = "SPOT"
    FARGATE = "FARGATE"
    FARGATE_SPOT = "FARGATE_SPOT"


class CRUpdateAllocationStrategy:
    """CRUpdateAllocationStrategy enum values."""

    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"


class DeviceCgroupPermission:
    """DeviceCgroupPermission enum values."""

    READ = "READ"
    WRITE = "WRITE"
    MKNOD = "MKNOD"


class EFSAuthorizationConfigIAM:
    """EFSAuthorizationConfigIAM enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EFSTransitEncryption:
    """EFSTransitEncryption enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FirelensConfigurationType:
    """FirelensConfigurationType enum values."""

    FLUENTD = "fluentd"
    FLUENTBIT = "fluentbit"


class JQState:
    """JQState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class JQStatus:
    """JQStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class JobDefinitionType:
    """JobDefinitionType enum values."""

    CONTAINER = "container"
    MULTINODE = "multinode"


class JobQueueType:
    """JobQueueType enum values."""

    EKS = "EKS"
    ECS = "ECS"
    ECS_FARGATE = "ECS_FARGATE"
    SAGEMAKER_TRAINING = "SAGEMAKER_TRAINING"


class JobStateTimeLimitActionsAction:
    """JobStateTimeLimitActionsAction enum values."""

    CANCEL = "CANCEL"
    TERMINATE = "TERMINATE"


class JobStateTimeLimitActionsState:
    """JobStateTimeLimitActionsState enum values."""

    RUNNABLE = "RUNNABLE"


class JobStatus:
    """JobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    RUNNABLE = "RUNNABLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class LogDriver:
    """LogDriver enum values."""

    JSON_FILE = "json-file"
    SYSLOG = "syslog"
    JOURNALD = "journald"
    GELF = "gelf"
    FLUENTD = "fluentd"
    AWSLOGS = "awslogs"
    SPLUNK = "splunk"
    AWSFIRELENS = "awsfirelens"


class OrchestrationType:
    """OrchestrationType enum values."""

    ECS = "ECS"
    EKS = "EKS"


class PlatformCapability:
    """PlatformCapability enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"


class ResourceType:
    """ResourceType enum values."""

    GPU = "GPU"
    VCPU = "VCPU"
    MEMORY = "MEMORY"


class RetryAction:
    """RetryAction enum values."""

    RETRY = "RETRY"
    EXIT = "EXIT"


class ServiceEnvironmentState:
    """ServiceEnvironmentState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ServiceEnvironmentStatus:
    """ServiceEnvironmentStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class ServiceEnvironmentType:
    """ServiceEnvironmentType enum values."""

    SAGEMAKER_TRAINING = "SAGEMAKER_TRAINING"


class ServiceJobRetryAction:
    """ServiceJobRetryAction enum values."""

    RETRY = "RETRY"
    EXIT = "EXIT"


class ServiceJobStatus:
    """ServiceJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    RUNNABLE = "RUNNABLE"
    SCHEDULED = "SCHEDULED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class ServiceJobType:
    """ServiceJobType enum values."""

    SAGEMAKER_TRAINING = "SAGEMAKER_TRAINING"


class ServiceResourceIdName:
    """ServiceResourceIdName enum values."""

    TRAININGJOBARN = "TrainingJobArn"


class UserdataType:
    """UserdataType enum values."""

    EKS_BOOTSTRAP_SH = "EKS_BOOTSTRAP_SH"
    EKS_NODEADM = "EKS_NODEADM"


@dataclass
class ComputeEnvironmentOrder(PropertyType):
    COMPUTE_ENVIRONMENT = "ComputeEnvironment"
    ORDER = "Order"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_environment": "ComputeEnvironment",
        "order": "Order",
    }

    compute_environment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    order: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JobStateTimeLimitAction(PropertyType):
    ACTION = "Action"
    MAX_TIME_SECONDS = "MaxTimeSeconds"
    STATE = "State"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "max_time_seconds": "MaxTimeSeconds",
        "state": "State",
        "reason": "Reason",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_time_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceEnvironmentOrder(PropertyType):
    ORDER = "Order"
    SERVICE_ENVIRONMENT = "ServiceEnvironment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "order": "Order",
        "service_environment": "ServiceEnvironment",
    }

    order: Optional[Union[int, Ref, GetAtt, Sub]] = None
    service_environment: Optional[Union[str, Ref, GetAtt, Sub]] = None

