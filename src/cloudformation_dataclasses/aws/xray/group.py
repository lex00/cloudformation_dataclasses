"""PropertyTypes for AWS::XRay::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InsightsConfiguration(PropertyType):
    NOTIFICATIONS_ENABLED = "NotificationsEnabled"
    INSIGHTS_ENABLED = "InsightsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notifications_enabled": "NotificationsEnabled",
        "insights_enabled": "InsightsEnabled",
    }

    notifications_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    insights_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

