"""PropertyTypes for AWS::SageMaker::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Alarm(PropertyType):
    ALARM_NAME = "AlarmName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_name": "AlarmName",
    }

    alarm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AutoRollbackConfig(PropertyType):
    ALARMS = "Alarms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarms": "Alarms",
    }

    alarms: Optional[list[Alarm]] = None


@dataclass
class BlueGreenUpdatePolicy(PropertyType):
    MAXIMUM_EXECUTION_TIMEOUT_IN_SECONDS = "MaximumExecutionTimeoutInSeconds"
    TERMINATION_WAIT_IN_SECONDS = "TerminationWaitInSeconds"
    TRAFFIC_ROUTING_CONFIGURATION = "TrafficRoutingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_execution_timeout_in_seconds": "MaximumExecutionTimeoutInSeconds",
        "termination_wait_in_seconds": "TerminationWaitInSeconds",
        "traffic_routing_configuration": "TrafficRoutingConfiguration",
    }

    maximum_execution_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    termination_wait_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    traffic_routing_configuration: Optional[TrafficRoutingConfig] = None


@dataclass
class CapacitySize(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, CapacitySizeType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfig(PropertyType):
    AUTO_ROLLBACK_CONFIGURATION = "AutoRollbackConfiguration"
    ROLLING_UPDATE_POLICY = "RollingUpdatePolicy"
    BLUE_GREEN_UPDATE_POLICY = "BlueGreenUpdatePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_rollback_configuration": "AutoRollbackConfiguration",
        "rolling_update_policy": "RollingUpdatePolicy",
        "blue_green_update_policy": "BlueGreenUpdatePolicy",
    }

    auto_rollback_configuration: Optional[AutoRollbackConfig] = None
    rolling_update_policy: Optional[RollingUpdatePolicy] = None
    blue_green_update_policy: Optional[BlueGreenUpdatePolicy] = None


@dataclass
class RollingUpdatePolicy(PropertyType):
    MAXIMUM_EXECUTION_TIMEOUT_IN_SECONDS = "MaximumExecutionTimeoutInSeconds"
    MAXIMUM_BATCH_SIZE = "MaximumBatchSize"
    WAIT_INTERVAL_IN_SECONDS = "WaitIntervalInSeconds"
    ROLLBACK_MAXIMUM_BATCH_SIZE = "RollbackMaximumBatchSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_execution_timeout_in_seconds": "MaximumExecutionTimeoutInSeconds",
        "maximum_batch_size": "MaximumBatchSize",
        "wait_interval_in_seconds": "WaitIntervalInSeconds",
        "rollback_maximum_batch_size": "RollbackMaximumBatchSize",
    }

    maximum_execution_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_batch_size: Optional[CapacitySize] = None
    wait_interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rollback_maximum_batch_size: Optional[CapacitySize] = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    TYPE = "Type"
    LINEAR_STEP_SIZE = "LinearStepSize"
    CANARY_SIZE = "CanarySize"
    WAIT_INTERVAL_IN_SECONDS = "WaitIntervalInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "linear_step_size": "LinearStepSize",
        "canary_size": "CanarySize",
        "wait_interval_in_seconds": "WaitIntervalInSeconds",
    }

    type_: Optional[Union[str, TrafficRoutingConfigType, Ref, GetAtt, Sub]] = None
    linear_step_size: Optional[CapacitySize] = None
    canary_size: Optional[CapacitySize] = None
    wait_interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VariantProperty(PropertyType):
    VARIANT_PROPERTY_TYPE = "VariantPropertyType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variant_property_type": "VariantPropertyType",
    }

    variant_property_type: Optional[Union[str, VariantPropertyType, Ref, GetAtt, Sub]] = None

