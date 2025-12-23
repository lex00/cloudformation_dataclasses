"""PropertyTypes for AWS::CodeDeploy::DeploymentConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MinimumHealthyHosts(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MinimumHealthyHostsPerZone(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedCanary(PropertyType):
    CANARY_PERCENTAGE = "CanaryPercentage"
    CANARY_INTERVAL = "CanaryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canary_percentage": "CanaryPercentage",
        "canary_interval": "CanaryInterval",
    }

    canary_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    canary_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedLinear(PropertyType):
    LINEAR_INTERVAL = "LinearInterval"
    LINEAR_PERCENTAGE = "LinearPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "linear_interval": "LinearInterval",
        "linear_percentage": "LinearPercentage",
    }

    linear_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    linear_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    TYPE = "Type"
    TIME_BASED_LINEAR = "TimeBasedLinear"
    TIME_BASED_CANARY = "TimeBasedCanary"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "time_based_linear": "TimeBasedLinear",
        "time_based_canary": "TimeBasedCanary",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_based_linear: Optional[TimeBasedLinear] = None
    time_based_canary: Optional[TimeBasedCanary] = None


@dataclass
class ZonalConfig(PropertyType):
    MONITOR_DURATION_IN_SECONDS = "MonitorDurationInSeconds"
    MINIMUM_HEALTHY_HOSTS_PER_ZONE = "MinimumHealthyHostsPerZone"
    FIRST_ZONE_MONITOR_DURATION_IN_SECONDS = "FirstZoneMonitorDurationInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "monitor_duration_in_seconds": "MonitorDurationInSeconds",
        "minimum_healthy_hosts_per_zone": "MinimumHealthyHostsPerZone",
        "first_zone_monitor_duration_in_seconds": "FirstZoneMonitorDurationInSeconds",
    }

    monitor_duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_healthy_hosts_per_zone: Optional[MinimumHealthyHostsPerZone] = None
    first_zone_monitor_duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None

