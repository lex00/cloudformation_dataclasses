"""PropertyTypes for AWS::VpcLattice::Listener."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DefaultAction(PropertyType):
    FORWARD = "Forward"
    FIXED_RESPONSE = "FixedResponse"

    _property_mappings: ClassVar[dict[str, str]] = {
        "forward": "Forward",
        "fixed_response": "FixedResponse",
    }

    forward: Optional[Forward] = None
    fixed_response: Optional[FixedResponse] = None


@dataclass
class FixedResponse(PropertyType):
    STATUS_CODE = "StatusCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status_code": "StatusCode",
    }

    status_code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Forward(PropertyType):
    TARGET_GROUPS = "TargetGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_groups": "TargetGroups",
    }

    target_groups: Optional[list[WeightedTargetGroup]] = None


@dataclass
class WeightedTargetGroup(PropertyType):
    WEIGHT = "Weight"
    TARGET_GROUP_IDENTIFIER = "TargetGroupIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "weight": "Weight",
        "target_group_identifier": "TargetGroupIdentifier",
    }

    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_group_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

