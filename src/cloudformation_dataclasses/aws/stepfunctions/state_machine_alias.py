"""PropertyTypes for AWS::StepFunctions::StateMachineAlias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeploymentPreference(PropertyType):
    TYPE = "Type"
    STATE_MACHINE_VERSION_ARN = "StateMachineVersionArn"
    PERCENTAGE = "Percentage"
    ALARMS = "Alarms"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "state_machine_version_arn": "StateMachineVersionArn",
        "percentage": "Percentage",
        "alarms": "Alarms",
        "interval": "Interval",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state_machine_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    alarms: Optional[Union[list[str], Ref]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingConfigurationVersion(PropertyType):
    STATE_MACHINE_VERSION_ARN = "StateMachineVersionArn"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state_machine_version_arn": "StateMachineVersionArn",
        "weight": "Weight",
    }

    state_machine_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

