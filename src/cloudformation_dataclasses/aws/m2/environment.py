"""PropertyTypes for AWS::M2::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationDeploymentLifecycle:
    """ApplicationDeploymentLifecycle enum values."""

    DEPLOYING = "Deploying"
    DEPLOYED = "Deployed"


class ApplicationLifecycle:
    """ApplicationLifecycle enum values."""

    CREATING = "Creating"
    CREATED = "Created"
    AVAILABLE = "Available"
    READY = "Ready"
    STARTING = "Starting"
    RUNNING = "Running"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"
    DELETING = "Deleting"
    DELETING_FROM_ENVIRONMENT = "Deleting From Environment"


class ApplicationVersionLifecycle:
    """ApplicationVersionLifecycle enum values."""

    CREATING = "Creating"
    AVAILABLE = "Available"
    FAILED = "Failed"


class BatchJobExecutionStatus:
    """BatchJobExecutionStatus enum values."""

    SUBMITTING = "Submitting"
    HOLDING = "Holding"
    DISPATCHING = "Dispatching"
    RUNNING = "Running"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    PURGED = "Purged"
    SUCCEEDED_WITH_WARNING = "Succeeded With Warning"


class BatchJobType:
    """BatchJobType enum values."""

    VSE = "VSE"
    JES2 = "JES2"
    JES3 = "JES3"


class DataSetTaskLifecycle:
    """DataSetTaskLifecycle enum values."""

    CREATING = "Creating"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"


class DeploymentLifecycle:
    """DeploymentLifecycle enum values."""

    DEPLOYING = "Deploying"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    UPDATING_DEPLOYMENT = "Updating Deployment"


class EngineType:
    """EngineType enum values."""

    MICROFOCUS = "microfocus"
    BLUAGE = "bluage"


class EnvironmentLifecycle:
    """EnvironmentLifecycle enum values."""

    CREATING = "Creating"
    AVAILABLE = "Available"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"
    UNHEALTHY = "UnHealthy"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "ipv4"
    DUAL = "dual"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FEATURENOTAVAILABLE = "featureNotAvailable"
    UNSUPPORTEDENGINEVERSION = "unsupportedEngineVersion"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


@dataclass
class EfsStorageConfiguration(PropertyType):
    MOUNT_POINT = "MountPoint"
    FILE_SYSTEM_ID = "FileSystemId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_point": "MountPoint",
        "file_system_id": "FileSystemId",
    }

    mount_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FsxStorageConfiguration(PropertyType):
    MOUNT_POINT = "MountPoint"
    FILE_SYSTEM_ID = "FileSystemId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_point": "MountPoint",
        "file_system_id": "FileSystemId",
    }

    mount_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HighAvailabilityConfig(PropertyType):
    DESIRED_CAPACITY = "DesiredCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "desired_capacity": "DesiredCapacity",
    }

    desired_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StorageConfiguration(PropertyType):
    EFS = "Efs"
    FSX = "Fsx"

    _property_mappings: ClassVar[dict[str, str]] = {
        "efs": "Efs",
        "fsx": "Fsx",
    }

    efs: Optional[EfsStorageConfiguration] = None
    fsx: Optional[FsxStorageConfiguration] = None

