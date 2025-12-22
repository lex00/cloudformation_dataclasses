"""PropertyTypes for AWS::AppConfig::Extension."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionPoint:
    """ActionPoint enum values."""

    PRE_CREATE_HOSTED_CONFIGURATION_VERSION = "PRE_CREATE_HOSTED_CONFIGURATION_VERSION"
    PRE_START_DEPLOYMENT = "PRE_START_DEPLOYMENT"
    AT_DEPLOYMENT_TICK = "AT_DEPLOYMENT_TICK"
    ON_DEPLOYMENT_START = "ON_DEPLOYMENT_START"
    ON_DEPLOYMENT_STEP = "ON_DEPLOYMENT_STEP"
    ON_DEPLOYMENT_BAKING = "ON_DEPLOYMENT_BAKING"
    ON_DEPLOYMENT_COMPLETE = "ON_DEPLOYMENT_COMPLETE"
    ON_DEPLOYMENT_ROLLED_BACK = "ON_DEPLOYMENT_ROLLED_BACK"


class BadRequestReason:
    """BadRequestReason enum values."""

    INVALIDCONFIGURATION = "InvalidConfiguration"


class BytesMeasure:
    """BytesMeasure enum values."""

    KILOBYTES = "KILOBYTES"


class DeletionProtectionCheck:
    """DeletionProtectionCheck enum values."""

    ACCOUNT_DEFAULT = "ACCOUNT_DEFAULT"
    APPLY = "APPLY"
    BYPASS = "BYPASS"


class DeploymentEventType:
    """DeploymentEventType enum values."""

    PERCENTAGE_UPDATED = "PERCENTAGE_UPDATED"
    ROLLBACK_STARTED = "ROLLBACK_STARTED"
    ROLLBACK_COMPLETED = "ROLLBACK_COMPLETED"
    BAKE_TIME_STARTED = "BAKE_TIME_STARTED"
    DEPLOYMENT_STARTED = "DEPLOYMENT_STARTED"
    DEPLOYMENT_COMPLETED = "DEPLOYMENT_COMPLETED"
    REVERT_COMPLETED = "REVERT_COMPLETED"


class DeploymentState:
    """DeploymentState enum values."""

    BAKING = "BAKING"
    VALIDATING = "VALIDATING"
    DEPLOYING = "DEPLOYING"
    COMPLETE = "COMPLETE"
    ROLLING_BACK = "ROLLING_BACK"
    ROLLED_BACK = "ROLLED_BACK"
    REVERTED = "REVERTED"


class EnvironmentState:
    """EnvironmentState enum values."""

    READY_FOR_DEPLOYMENT = "READY_FOR_DEPLOYMENT"
    DEPLOYING = "DEPLOYING"
    ROLLING_BACK = "ROLLING_BACK"
    ROLLED_BACK = "ROLLED_BACK"
    REVERTED = "REVERTED"


class GrowthType:
    """GrowthType enum values."""

    LINEAR = "LINEAR"
    EXPONENTIAL = "EXPONENTIAL"


class ReplicateTo:
    """ReplicateTo enum values."""

    NONE = "NONE"
    SSM_DOCUMENT = "SSM_DOCUMENT"


class TriggeredBy:
    """TriggeredBy enum values."""

    USER = "USER"
    APPCONFIG = "APPCONFIG"
    CLOUDWATCH_ALARM = "CLOUDWATCH_ALARM"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class ValidatorType:
    """ValidatorType enum values."""

    JSON_SCHEMA = "JSON_SCHEMA"
    LAMBDA = "LAMBDA"


@dataclass
class Parameter(PropertyType):
    DYNAMIC = "Dynamic"
    DESCRIPTION = "Description"
    REQUIRED = "Required"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic": "Dynamic",
        "description": "Description",
        "required": "Required",
    }

    dynamic: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None

