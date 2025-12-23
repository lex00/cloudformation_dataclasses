"""PropertyTypes for AWS::Route53RecoveryControl::SafetyRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssertionRule(PropertyType):
    ASSERTED_CONTROLS = "AssertedControls"
    WAIT_PERIOD_MS = "WaitPeriodMs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "asserted_controls": "AssertedControls",
        "wait_period_ms": "WaitPeriodMs",
    }

    asserted_controls: Optional[Union[list[str], Ref]] = None
    wait_period_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class GatingRule(PropertyType):
    TARGET_CONTROLS = "TargetControls"
    GATING_CONTROLS = "GatingControls"
    WAIT_PERIOD_MS = "WaitPeriodMs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_controls": "TargetControls",
        "gating_controls": "GatingControls",
        "wait_period_ms": "WaitPeriodMs",
    }

    target_controls: Optional[Union[list[str], Ref]] = None
    gating_controls: Optional[Union[list[str], Ref]] = None
    wait_period_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RuleConfig(PropertyType):
    TYPE = "Type"
    INVERTED = "Inverted"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "inverted": "Inverted",
        "threshold": "Threshold",
    }

    type_: Optional[Union[str, RuleType, Ref, GetAtt, Sub]] = None
    inverted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None

