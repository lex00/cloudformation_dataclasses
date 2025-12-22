"""PropertyTypes for AWS::ElasticBeanstalk::Application."""

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
class ApplicationResourceLifecycleConfig(PropertyType):
    SERVICE_ROLE = "ServiceRole"
    VERSION_LIFECYCLE_CONFIG = "VersionLifecycleConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_role": "ServiceRole",
        "version_lifecycle_config": "VersionLifecycleConfig",
    }

    service_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version_lifecycle_config: Optional[ApplicationVersionLifecycleConfig] = None


@dataclass
class ApplicationVersionLifecycleConfig(PropertyType):
    MAX_COUNT_RULE = "MaxCountRule"
    MAX_AGE_RULE = "MaxAgeRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_count_rule": "MaxCountRule",
        "max_age_rule": "MaxAgeRule",
    }

    max_count_rule: Optional[MaxCountRule] = None
    max_age_rule: Optional[MaxAgeRule] = None


@dataclass
class MaxAgeRule(PropertyType):
    DELETE_SOURCE_FROM_S3 = "DeleteSourceFromS3"
    MAX_AGE_IN_DAYS = "MaxAgeInDays"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delete_source_from_s3": "DeleteSourceFromS3",
        "max_age_in_days": "MaxAgeInDays",
        "enabled": "Enabled",
    }

    delete_source_from_s3: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_age_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MaxCountRule(PropertyType):
    DELETE_SOURCE_FROM_S3 = "DeleteSourceFromS3"
    ENABLED = "Enabled"
    MAX_COUNT = "MaxCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delete_source_from_s3": "DeleteSourceFromS3",
        "enabled": "Enabled",
        "max_count": "MaxCount",
    }

    delete_source_from_s3: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

