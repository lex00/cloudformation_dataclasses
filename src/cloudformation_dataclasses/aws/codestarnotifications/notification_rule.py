"""PropertyTypes for AWS::CodeStarNotifications::NotificationRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Target(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_type": "TargetType",
        "target_address": "TargetAddress",
    }

    target_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

