"""PropertyTypes for AWS::GreengrassV2::Deployment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComponentConfigurationUpdate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "merge": "Merge",
        "reset": "Reset",
    }

    merge: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reset: Optional[Union[list[str], Ref]] = None


@dataclass
class ComponentDeploymentSpecification(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "timeout_in_seconds": "TimeoutInSeconds",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfigurationValidationPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_in_seconds": "TimeoutInSeconds",
    }

    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentIoTJobConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "criteria_list": "CriteriaList",
    }

    criteria_list: Optional[list[IoTJobAbortCriteria]] = None


@dataclass
class IoTJobAbortCriteria(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_per_minute": "MaximumPerMinute",
        "exponential_rate": "ExponentialRate",
    }

    maximum_per_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    exponential_rate: Optional[IoTJobExponentialRolloutRate] = None


@dataclass
class IoTJobExponentialRolloutRate(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_succeeded_things": "NumberOfSucceededThings",
        "number_of_notified_things": "NumberOfNotifiedThings",
    }

    number_of_succeeded_things: Optional[Union[int, Ref, GetAtt, Sub]] = None
    number_of_notified_things: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IoTJobTimeoutConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "in_progress_timeout_in_minutes": "InProgressTimeoutInMinutes",
    }

    in_progress_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SystemResourceLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory": "Memory",
        "cpus": "Cpus",
    }

    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cpus: Optional[Union[float, Ref, GetAtt, Sub]] = None

