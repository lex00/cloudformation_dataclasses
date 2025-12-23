"""PropertyTypes for AWS::Notifications::NotificationHub."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NotificationHubStatusSummary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_hub_status": "NotificationHubStatus",
        "notification_hub_status_reason": "NotificationHubStatusReason",
    }

    notification_hub_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_hub_status_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None

