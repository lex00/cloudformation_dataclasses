"""PropertyTypes for AWS::SES::EmailIdentity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

