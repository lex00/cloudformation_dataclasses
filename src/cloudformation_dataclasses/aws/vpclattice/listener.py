"""PropertyTypes for AWS::VpcLattice::Listener."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DefaultAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forward": "Forward",
        "fixed_response": "FixedResponse",
    }

    forward: Optional[Forward] = None
    fixed_response: Optional[FixedResponse] = None


@dataclass
class FixedResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status_code": "StatusCode",
    }

    status_code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Forward(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_groups": "TargetGroups",
    }

    target_groups: Optional[list[WeightedTargetGroup]] = None


@dataclass
class WeightedTargetGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "weight": "Weight",
        "target_group_identifier": "TargetGroupIdentifier",
    }

    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_group_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

