"""PropertyTypes for AWS::SES::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DashboardOptions(PropertyType):
    ENGAGEMENT_METRICS = "EngagementMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "engagement_metrics": "EngagementMetrics",
    }

    engagement_metrics: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeliveryOptions(PropertyType):
    MAX_DELIVERY_SECONDS = "MaxDeliverySeconds"
    SENDING_POOL_NAME = "SendingPoolName"
    TLS_POLICY = "TlsPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_delivery_seconds": "MaxDeliverySeconds",
        "sending_pool_name": "SendingPoolName",
        "tls_policy": "TlsPolicy",
    }

    max_delivery_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    sending_pool_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tls_policy: Optional[Union[str, TlsPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class GuardianOptions(PropertyType):
    OPTIMIZED_SHARED_DELIVERY = "OptimizedSharedDelivery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "optimized_shared_delivery": "OptimizedSharedDelivery",
    }

    optimized_shared_delivery: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReputationOptions(PropertyType):
    REPUTATION_METRICS_ENABLED = "ReputationMetricsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "reputation_metrics_enabled": "ReputationMetricsEnabled",
    }

    reputation_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SendingOptions(PropertyType):
    SENDING_ENABLED = "SendingEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sending_enabled": "SendingEnabled",
    }

    sending_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SuppressionOptions(PropertyType):
    SUPPRESSED_REASONS = "SuppressedReasons"

    _property_mappings: ClassVar[dict[str, str]] = {
        "suppressed_reasons": "SuppressedReasons",
    }

    suppressed_reasons: Optional[Union[list[str], Ref]] = None


@dataclass
class TrackingOptions(PropertyType):
    HTTPS_POLICY = "HttpsPolicy"
    CUSTOM_REDIRECT_DOMAIN = "CustomRedirectDomain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "https_policy": "HttpsPolicy",
        "custom_redirect_domain": "CustomRedirectDomain",
    }

    https_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_redirect_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VdmOptions(PropertyType):
    DASHBOARD_OPTIONS = "DashboardOptions"
    GUARDIAN_OPTIONS = "GuardianOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dashboard_options": "DashboardOptions",
        "guardian_options": "GuardianOptions",
    }

    dashboard_options: Optional[DashboardOptions] = None
    guardian_options: Optional[GuardianOptions] = None

