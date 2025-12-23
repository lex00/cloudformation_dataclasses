"""PropertyTypes for AWS::CloudFront::MonitoringSubscription."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MonitoringSubscription(PropertyType):
    REALTIME_METRICS_SUBSCRIPTION_CONFIG = "RealtimeMetricsSubscriptionConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "realtime_metrics_subscription_config": "RealtimeMetricsSubscriptionConfig",
    }

    realtime_metrics_subscription_config: Optional[RealtimeMetricsSubscriptionConfig] = None


@dataclass
class RealtimeMetricsSubscriptionConfig(PropertyType):
    REALTIME_METRICS_SUBSCRIPTION_STATUS = "RealtimeMetricsSubscriptionStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "realtime_metrics_subscription_status": "RealtimeMetricsSubscriptionStatus",
    }

    realtime_metrics_subscription_status: Optional[Union[str, RealtimeMetricsSubscriptionStatus, Ref, GetAtt, Sub]] = None

