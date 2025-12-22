"""PropertyTypes for AWS::GreengrassV2::Deployment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CloudComponentState:
    """CloudComponentState enum values."""

    REQUESTED = "REQUESTED"
    INITIATED = "INITIATED"
    DEPLOYABLE = "DEPLOYABLE"
    FAILED = "FAILED"
    DEPRECATED = "DEPRECATED"


class ComponentDependencyType:
    """ComponentDependencyType enum values."""

    HARD = "HARD"
    SOFT = "SOFT"


class ComponentVisibilityScope:
    """ComponentVisibilityScope enum values."""

    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"


class CoreDeviceStatus:
    """CoreDeviceStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class DeploymentComponentUpdatePolicyAction:
    """DeploymentComponentUpdatePolicyAction enum values."""

    NOTIFY_COMPONENTS = "NOTIFY_COMPONENTS"
    SKIP_NOTIFY_COMPONENTS = "SKIP_NOTIFY_COMPONENTS"


class DeploymentFailureHandlingPolicy:
    """DeploymentFailureHandlingPolicy enum values."""

    ROLLBACK = "ROLLBACK"
    DO_NOTHING = "DO_NOTHING"


class DeploymentHistoryFilter:
    """DeploymentHistoryFilter enum values."""

    ALL = "ALL"
    LATEST_ONLY = "LATEST_ONLY"


class DeploymentStatus:
    """DeploymentStatus enum values."""

    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    INACTIVE = "INACTIVE"


class EffectiveDeploymentExecutionStatus:
    """EffectiveDeploymentExecutionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    QUEUED = "QUEUED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    TIMED_OUT = "TIMED_OUT"
    CANCELED = "CANCELED"
    REJECTED = "REJECTED"
    SUCCEEDED = "SUCCEEDED"


class InstalledComponentLifecycleState:
    """InstalledComponentLifecycleState enum values."""

    NEW = "NEW"
    INSTALLED = "INSTALLED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    ERRORED = "ERRORED"
    BROKEN = "BROKEN"
    FINISHED = "FINISHED"


class InstalledComponentTopologyFilter:
    """InstalledComponentTopologyFilter enum values."""

    ALL = "ALL"
    ROOT = "ROOT"


class IoTJobAbortAction:
    """IoTJobAbortAction enum values."""

    CANCEL = "CANCEL"


class IoTJobExecutionFailureType:
    """IoTJobExecutionFailureType enum values."""

    FAILED = "FAILED"
    REJECTED = "REJECTED"
    TIMED_OUT = "TIMED_OUT"
    ALL = "ALL"


class IotEndpointType:
    """IotEndpointType enum values."""

    FIPS = "fips"
    STANDARD = "standard"


class LambdaEventSourceType:
    """LambdaEventSourceType enum values."""

    PUB_SUB = "PUB_SUB"
    IOT_CORE = "IOT_CORE"


class LambdaFilesystemPermission:
    """LambdaFilesystemPermission enum values."""

    RO = "ro"
    RW = "rw"


class LambdaInputPayloadEncodingType:
    """LambdaInputPayloadEncodingType enum values."""

    JSON = "json"
    BINARY = "binary"


class LambdaIsolationMode:
    """LambdaIsolationMode enum values."""

    GREENGRASSCONTAINER = "GreengrassContainer"
    NOCONTAINER = "NoContainer"


class RecipeOutputFormat:
    """RecipeOutputFormat enum values."""

    JSON = "JSON"
    YAML = "YAML"


class S3EndpointType:
    """S3EndpointType enum values."""

    REGIONAL = "REGIONAL"
    GLOBAL = "GLOBAL"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


class VendorGuidance:
    """VendorGuidance enum values."""

    ACTIVE = "ACTIVE"
    DISCONTINUED = "DISCONTINUED"
    DELETED = "DELETED"


@dataclass
class ComponentConfigurationUpdate(PropertyType):
    MERGE = "Merge"
    RESET = "Reset"

    _property_mappings: ClassVar[dict[str, str]] = {
        "merge": "Merge",
        "reset": "Reset",
    }

    merge: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reset: Optional[Union[list[str], Ref]] = None


@dataclass
class ComponentDeploymentSpecification(PropertyType):
    RUN_WITH = "RunWith"
    CONFIGURATION_UPDATE = "ConfigurationUpdate"
    COMPONENT_VERSION = "ComponentVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "run_with": "RunWith",
        "configuration_update": "ConfigurationUpdate",
        "component_version": "ComponentVersion",
    }

    run_with: Optional[ComponentRunWith] = None
    configuration_update: Optional[ComponentConfigurationUpdate] = None
    component_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentRunWith(PropertyType):
    WINDOWS_USER = "WindowsUser"
    SYSTEM_RESOURCE_LIMITS = "SystemResourceLimits"
    POSIX_USER = "PosixUser"

    _property_mappings: ClassVar[dict[str, str]] = {
        "windows_user": "WindowsUser",
        "system_resource_limits": "SystemResourceLimits",
        "posix_user": "PosixUser",
    }

    windows_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    system_resource_limits: Optional[SystemResourceLimits] = None
    posix_user: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentComponentUpdatePolicy(PropertyType):
    ACTION = "Action"
    TIMEOUT_IN_SECONDS = "TimeoutInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "timeout_in_seconds": "TimeoutInSeconds",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfigurationValidationPolicy(PropertyType):
    TIMEOUT_IN_SECONDS = "TimeoutInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_in_seconds": "TimeoutInSeconds",
    }

    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentIoTJobConfiguration(PropertyType):
    JOB_EXECUTIONS_ROLLOUT_CONFIG = "JobExecutionsRolloutConfig"
    TIMEOUT_CONFIG = "TimeoutConfig"
    ABORT_CONFIG = "AbortConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "job_executions_rollout_config": "JobExecutionsRolloutConfig",
        "timeout_config": "TimeoutConfig",
        "abort_config": "AbortConfig",
    }

    job_executions_rollout_config: Optional[IoTJobExecutionsRolloutConfig] = None
    timeout_config: Optional[IoTJobTimeoutConfig] = None
    abort_config: Optional[IoTJobAbortConfig] = None


@dataclass
class DeploymentPolicies(PropertyType):
    COMPONENT_UPDATE_POLICY = "ComponentUpdatePolicy"
    CONFIGURATION_VALIDATION_POLICY = "ConfigurationValidationPolicy"
    FAILURE_HANDLING_POLICY = "FailureHandlingPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "component_update_policy": "ComponentUpdatePolicy",
        "configuration_validation_policy": "ConfigurationValidationPolicy",
        "failure_handling_policy": "FailureHandlingPolicy",
    }

    component_update_policy: Optional[DeploymentComponentUpdatePolicy] = None
    configuration_validation_policy: Optional[DeploymentConfigurationValidationPolicy] = None
    failure_handling_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IoTJobAbortConfig(PropertyType):
    CRITERIA_LIST = "CriteriaList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "criteria_list": "CriteriaList",
    }

    criteria_list: Optional[list[IoTJobAbortCriteria]] = None


@dataclass
class IoTJobAbortCriteria(PropertyType):
    FAILURE_TYPE = "FailureType"
    ACTION = "Action"
    THRESHOLD_PERCENTAGE = "ThresholdPercentage"
    MIN_NUMBER_OF_EXECUTED_THINGS = "MinNumberOfExecutedThings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "failure_type": "FailureType",
        "action": "Action",
        "threshold_percentage": "ThresholdPercentage",
        "min_number_of_executed_things": "MinNumberOfExecutedThings",
    }

    failure_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    min_number_of_executed_things: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IoTJobExecutionsRolloutConfig(PropertyType):
    MAXIMUM_PER_MINUTE = "MaximumPerMinute"
    EXPONENTIAL_RATE = "ExponentialRate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_per_minute": "MaximumPerMinute",
        "exponential_rate": "ExponentialRate",
    }

    maximum_per_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    exponential_rate: Optional[IoTJobExponentialRolloutRate] = None


@dataclass
class IoTJobExponentialRolloutRate(PropertyType):
    RATE_INCREASE_CRITERIA = "RateIncreaseCriteria"
    BASE_RATE_PER_MINUTE = "BaseRatePerMinute"
    INCREMENT_FACTOR = "IncrementFactor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rate_increase_criteria": "RateIncreaseCriteria",
        "base_rate_per_minute": "BaseRatePerMinute",
        "increment_factor": "IncrementFactor",
    }

    rate_increase_criteria: Optional[IoTJobRateIncreaseCriteria] = None
    base_rate_per_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    increment_factor: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class IoTJobRateIncreaseCriteria(PropertyType):
    NUMBER_OF_SUCCEEDED_THINGS = "NumberOfSucceededThings"
    NUMBER_OF_NOTIFIED_THINGS = "NumberOfNotifiedThings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_succeeded_things": "NumberOfSucceededThings",
        "number_of_notified_things": "NumberOfNotifiedThings",
    }

    number_of_succeeded_things: Optional[Union[int, Ref, GetAtt, Sub]] = None
    number_of_notified_things: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IoTJobTimeoutConfig(PropertyType):
    IN_PROGRESS_TIMEOUT_IN_MINUTES = "InProgressTimeoutInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "in_progress_timeout_in_minutes": "InProgressTimeoutInMinutes",
    }

    in_progress_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SystemResourceLimits(PropertyType):
    MEMORY = "Memory"
    CPUS = "Cpus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "memory": "Memory",
        "cpus": "Cpus",
    }

    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cpus: Optional[Union[float, Ref, GetAtt, Sub]] = None

