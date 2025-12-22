"""PropertyTypes for AWS::SES::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BehaviorOnMXFailure:
    """BehaviorOnMXFailure enum values."""

    USEDEFAULTVALUE = "UseDefaultValue"
    REJECTMESSAGE = "RejectMessage"


class BounceType:
    """BounceType enum values."""

    DOESNOTEXIST = "DoesNotExist"
    MESSAGETOOLARGE = "MessageTooLarge"
    EXCEEDEDQUOTA = "ExceededQuota"
    CONTENTREJECTED = "ContentRejected"
    UNDEFINED = "Undefined"
    TEMPORARYFAILURE = "TemporaryFailure"


class BulkEmailStatus:
    """BulkEmailStatus enum values."""

    SUCCESS = "Success"
    MESSAGEREJECTED = "MessageRejected"
    MAILFROMDOMAINNOTVERIFIED = "MailFromDomainNotVerified"
    CONFIGURATIONSETDOESNOTEXIST = "ConfigurationSetDoesNotExist"
    TEMPLATEDOESNOTEXIST = "TemplateDoesNotExist"
    ACCOUNTSUSPENDED = "AccountSuspended"
    ACCOUNTTHROTTLED = "AccountThrottled"
    ACCOUNTDAILYQUOTAEXCEEDED = "AccountDailyQuotaExceeded"
    INVALIDSENDINGPOOLNAME = "InvalidSendingPoolName"
    ACCOUNTSENDINGPAUSED = "AccountSendingPaused"
    CONFIGURATIONSETSENDINGPAUSED = "ConfigurationSetSendingPaused"
    INVALIDPARAMETERVALUE = "InvalidParameterValue"
    TRANSIENTFAILURE = "TransientFailure"
    FAILED = "Failed"


class ConfigurationSetAttribute:
    """ConfigurationSetAttribute enum values."""

    EVENTDESTINATIONS = "eventDestinations"
    TRACKINGOPTIONS = "trackingOptions"
    DELIVERYOPTIONS = "deliveryOptions"
    REPUTATIONOPTIONS = "reputationOptions"


class CustomMailFromStatus:
    """CustomMailFromStatus enum values."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"
    TEMPORARYFAILURE = "TemporaryFailure"


class DimensionValueSource:
    """DimensionValueSource enum values."""

    MESSAGETAG = "messageTag"
    EMAILHEADER = "emailHeader"
    LINKTAG = "linkTag"


class DsnAction:
    """DsnAction enum values."""

    FAILED = "failed"
    DELAYED = "delayed"
    DELIVERED = "delivered"
    RELAYED = "relayed"
    EXPANDED = "expanded"


class EventType:
    """EventType enum values."""

    SEND = "send"
    REJECT = "reject"
    BOUNCE = "bounce"
    COMPLAINT = "complaint"
    DELIVERY = "delivery"
    OPEN = "open"
    CLICK = "click"
    RENDERINGFAILURE = "renderingFailure"


class IdentityType:
    """IdentityType enum values."""

    EMAILADDRESS = "EmailAddress"
    DOMAIN = "Domain"


class InvocationType:
    """InvocationType enum values."""

    EVENT = "Event"
    REQUESTRESPONSE = "RequestResponse"


class NotificationType:
    """NotificationType enum values."""

    BOUNCE = "Bounce"
    COMPLAINT = "Complaint"
    DELIVERY = "Delivery"


class ReceiptFilterPolicy:
    """ReceiptFilterPolicy enum values."""

    BLOCK = "Block"
    ALLOW = "Allow"


class SNSActionEncoding:
    """SNSActionEncoding enum values."""

    UTF_8 = "UTF-8"
    BASE64 = "Base64"


class StopScope:
    """StopScope enum values."""

    RULESET = "RuleSet"


class TlsPolicy:
    """TlsPolicy enum values."""

    REQUIRE = "Require"
    OPTIONAL = "Optional"


class VerificationStatus:
    """VerificationStatus enum values."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"
    TEMPORARYFAILURE = "TemporaryFailure"
    NOTSTARTED = "NotStarted"


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

