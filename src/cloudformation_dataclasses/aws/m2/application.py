"""PropertyTypes for AWS::M2::Application."""

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
class Definition(PropertyType):
    CONTENT = "Content"
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
        "s3_location": "S3Location",
    }

    content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_location: Optional[Union[str, Ref, GetAtt, Sub]] = None

