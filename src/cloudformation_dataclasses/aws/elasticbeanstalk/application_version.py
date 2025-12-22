"""PropertyTypes for AWS::ElasticBeanstalk::ApplicationVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionHistoryStatus:
    """ActionHistoryStatus enum values."""

    COMPLETED = "Completed"
    FAILED = "Failed"
    UNKNOWN = "Unknown"


class ActionStatus:
    """ActionStatus enum values."""

    SCHEDULED = "Scheduled"
    PENDING = "Pending"
    RUNNING = "Running"
    UNKNOWN = "Unknown"


class ActionType:
    """ActionType enum values."""

    INSTANCEREFRESH = "InstanceRefresh"
    PLATFORMUPDATE = "PlatformUpdate"
    UNKNOWN = "Unknown"


class ApplicationVersionStatus:
    """ApplicationVersionStatus enum values."""

    PROCESSED = "Processed"
    UNPROCESSED = "Unprocessed"
    FAILED = "Failed"
    PROCESSING = "Processing"
    BUILDING = "Building"


class ComputeType:
    """ComputeType enum values."""

    BUILD_GENERAL1_SMALL = "BUILD_GENERAL1_SMALL"
    BUILD_GENERAL1_MEDIUM = "BUILD_GENERAL1_MEDIUM"
    BUILD_GENERAL1_LARGE = "BUILD_GENERAL1_LARGE"


class ConfigurationDeploymentStatus:
    """ConfigurationDeploymentStatus enum values."""

    DEPLOYED = "deployed"
    PENDING = "pending"
    FAILED = "failed"


class ConfigurationOptionValueType:
    """ConfigurationOptionValueType enum values."""

    SCALAR = "Scalar"
    LIST = "List"


class EnvironmentHealth:
    """EnvironmentHealth enum values."""

    GREEN = "Green"
    YELLOW = "Yellow"
    RED = "Red"
    GREY = "Grey"


class EnvironmentHealthAttribute:
    """EnvironmentHealthAttribute enum values."""

    STATUS = "Status"
    COLOR = "Color"
    CAUSES = "Causes"
    APPLICATIONMETRICS = "ApplicationMetrics"
    INSTANCESHEALTH = "InstancesHealth"
    ALL = "All"
    HEALTHSTATUS = "HealthStatus"
    REFRESHEDAT = "RefreshedAt"


class EnvironmentHealthStatus:
    """EnvironmentHealthStatus enum values."""

    NODATA = "NoData"
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    OK = "Ok"
    INFO = "Info"
    WARNING = "Warning"
    DEGRADED = "Degraded"
    SEVERE = "Severe"
    SUSPENDED = "Suspended"


class EnvironmentInfoType:
    """EnvironmentInfoType enum values."""

    TAIL = "tail"
    BUNDLE = "bundle"


class EnvironmentStatus:
    """EnvironmentStatus enum values."""

    ABORTING = "Aborting"
    LAUNCHING = "Launching"
    UPDATING = "Updating"
    LINKINGFROM = "LinkingFrom"
    LINKINGTO = "LinkingTo"
    READY = "Ready"
    TERMINATING = "Terminating"
    TERMINATED = "Terminated"


class EventSeverity:
    """EventSeverity enum values."""

    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class FailureType:
    """FailureType enum values."""

    UPDATECANCELLED = "UpdateCancelled"
    CANCELLATIONFAILED = "CancellationFailed"
    ROLLBACKFAILED = "RollbackFailed"
    ROLLBACKSUCCESSFUL = "RollbackSuccessful"
    INTERNALFAILURE = "InternalFailure"
    INVALIDENVIRONMENTSTATE = "InvalidEnvironmentState"
    PERMISSIONSERROR = "PermissionsError"


class InstancesHealthAttribute:
    """InstancesHealthAttribute enum values."""

    HEALTHSTATUS = "HealthStatus"
    COLOR = "Color"
    CAUSES = "Causes"
    APPLICATIONMETRICS = "ApplicationMetrics"
    REFRESHEDAT = "RefreshedAt"
    LAUNCHEDAT = "LaunchedAt"
    SYSTEM = "System"
    DEPLOYMENT = "Deployment"
    AVAILABILITYZONE = "AvailabilityZone"
    INSTANCETYPE = "InstanceType"
    ALL = "All"


class PlatformStatus:
    """PlatformStatus enum values."""

    CREATING = "Creating"
    FAILED = "Failed"
    READY = "Ready"
    DELETING = "Deleting"
    DELETED = "Deleted"


class SourceRepository:
    """SourceRepository enum values."""

    CODECOMMIT = "CodeCommit"
    S3 = "S3"


class SourceType:
    """SourceType enum values."""

    GIT = "Git"
    ZIP = "Zip"


class ValidationSeverity:
    """ValidationSeverity enum values."""

    ERROR = "error"
    WARNING = "warning"


@dataclass
class SourceBundle(PropertyType):
    S3_BUCKET = "S3Bucket"
    S3_KEY = "S3Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "s3_key": "S3Key",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

