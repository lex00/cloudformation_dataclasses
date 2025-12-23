"""PropertyTypes for AWS::IoT::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AbortConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "criteria_list": "CriteriaList",
    }

    criteria_list: Optional[list[AbortCriteria]] = None


@dataclass
class AbortCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "failure_type": "FailureType",
        "threshold_percentage": "ThresholdPercentage",
        "min_number_of_executed_things": "MinNumberOfExecutedThings",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    failure_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    min_number_of_executed_things: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ExponentialRolloutRate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rate_increase_criteria": "RateIncreaseCriteria",
        "base_rate_per_minute": "BaseRatePerMinute",
        "increment_factor": "IncrementFactor",
    }

    rate_increase_criteria: Optional[RateIncreaseCriteria] = None
    base_rate_per_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    increment_factor: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class JobExecutionsRetryConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_criteria_list": "RetryCriteriaList",
    }

    retry_criteria_list: Optional[list[RetryCriteria]] = None


@dataclass
class JobExecutionsRolloutConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_per_minute": "MaximumPerMinute",
        "exponential_rollout_rate": "ExponentialRolloutRate",
    }

    maximum_per_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    exponential_rollout_rate: Optional[ExponentialRolloutRate] = None


@dataclass
class MaintenanceWindow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_minutes": "DurationInMinutes",
        "start_time": "StartTime",
    }

    duration_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PresignedUrlConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expires_in_sec": "ExpiresInSec",
        "role_arn": "RoleArn",
    }

    expires_in_sec: Optional[Union[int, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RateIncreaseCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_succeeded_things": "NumberOfSucceededThings",
        "number_of_notified_things": "NumberOfNotifiedThings",
    }

    number_of_succeeded_things: Optional[Union[int, Ref, GetAtt, Sub]] = None
    number_of_notified_things: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RetryCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "failure_type": "FailureType",
        "number_of_retries": "NumberOfRetries",
    }

    failure_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    number_of_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeoutConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "in_progress_timeout_in_minutes": "InProgressTimeoutInMinutes",
    }

    in_progress_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None

