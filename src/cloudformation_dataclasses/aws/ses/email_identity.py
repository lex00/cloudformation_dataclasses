"""PropertyTypes for AWS::SES::EmailIdentity."""

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
class ConfigurationSetAttributes(PropertyType):
    CONFIGURATION_SET_NAME = "ConfigurationSetName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_set_name": "ConfigurationSetName",
    }

    configuration_set_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DkimAttributes(PropertyType):
    SIGNING_ENABLED = "SigningEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "signing_enabled": "SigningEnabled",
    }

    signing_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DkimSigningAttributes(PropertyType):
    DOMAIN_SIGNING_PRIVATE_KEY = "DomainSigningPrivateKey"
    DOMAIN_SIGNING_SELECTOR = "DomainSigningSelector"
    NEXT_SIGNING_KEY_LENGTH = "NextSigningKeyLength"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_signing_private_key": "DomainSigningPrivateKey",
        "domain_signing_selector": "DomainSigningSelector",
        "next_signing_key_length": "NextSigningKeyLength",
    }

    domain_signing_private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_signing_selector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next_signing_key_length: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FeedbackAttributes(PropertyType):
    EMAIL_FORWARDING_ENABLED = "EmailForwardingEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email_forwarding_enabled": "EmailForwardingEnabled",
    }

    email_forwarding_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MailFromAttributes(PropertyType):
    MAIL_FROM_DOMAIN = "MailFromDomain"
    BEHAVIOR_ON_MX_FAILURE = "BehaviorOnMxFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mail_from_domain": "MailFromDomain",
        "behavior_on_mx_failure": "BehaviorOnMxFailure",
    }

    mail_from_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    behavior_on_mx_failure: Optional[Union[str, Ref, GetAtt, Sub]] = None

