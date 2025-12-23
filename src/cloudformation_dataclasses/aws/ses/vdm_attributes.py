"""PropertyTypes for AWS::SES::VdmAttributes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DashboardAttributes(PropertyType):
    ENGAGEMENT_METRICS = "EngagementMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "engagement_metrics": "EngagementMetrics",
    }

    engagement_metrics: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardianAttributes(PropertyType):
    OPTIMIZED_SHARED_DELIVERY = "OptimizedSharedDelivery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "optimized_shared_delivery": "OptimizedSharedDelivery",
    }

    optimized_shared_delivery: Optional[Union[str, Ref, GetAtt, Sub]] = None

