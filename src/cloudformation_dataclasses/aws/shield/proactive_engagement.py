"""PropertyTypes for AWS::Shield::ProactiveEngagement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationLayerAutomaticResponseStatus:
    """ApplicationLayerAutomaticResponseStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AttackLayer:
    """AttackLayer enum values."""

    NETWORK = "NETWORK"
    APPLICATION = "APPLICATION"


class AttackPropertyIdentifier:
    """AttackPropertyIdentifier enum values."""

    DESTINATION_URL = "DESTINATION_URL"
    REFERRER = "REFERRER"
    SOURCE_ASN = "SOURCE_ASN"
    SOURCE_COUNTRY = "SOURCE_COUNTRY"
    SOURCE_IP_ADDRESS = "SOURCE_IP_ADDRESS"
    SOURCE_USER_AGENT = "SOURCE_USER_AGENT"
    WORDPRESS_PINGBACK_REFLECTOR = "WORDPRESS_PINGBACK_REFLECTOR"
    WORDPRESS_PINGBACK_SOURCE = "WORDPRESS_PINGBACK_SOURCE"


class AutoRenew:
    """AutoRenew enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ProactiveEngagementStatus:
    """ProactiveEngagementStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    PENDING = "PENDING"


class ProtectedResourceType:
    """ProtectedResourceType enum values."""

    CLOUDFRONT_DISTRIBUTION = "CLOUDFRONT_DISTRIBUTION"
    ROUTE_53_HOSTED_ZONE = "ROUTE_53_HOSTED_ZONE"
    ELASTIC_IP_ALLOCATION = "ELASTIC_IP_ALLOCATION"
    CLASSIC_LOAD_BALANCER = "CLASSIC_LOAD_BALANCER"
    APPLICATION_LOAD_BALANCER = "APPLICATION_LOAD_BALANCER"
    GLOBAL_ACCELERATOR = "GLOBAL_ACCELERATOR"


class ProtectionGroupAggregation:
    """ProtectionGroupAggregation enum values."""

    SUM = "SUM"
    MEAN = "MEAN"
    MAX = "MAX"


class ProtectionGroupPattern:
    """ProtectionGroupPattern enum values."""

    ALL = "ALL"
    ARBITRARY = "ARBITRARY"
    BY_RESOURCE_TYPE = "BY_RESOURCE_TYPE"


class SubResourceType:
    """SubResourceType enum values."""

    IP = "IP"
    URL = "URL"


class SubscriptionState:
    """SubscriptionState enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Unit:
    """Unit enum values."""

    BITS = "BITS"
    BYTES = "BYTES"
    PACKETS = "PACKETS"
    REQUESTS = "REQUESTS"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


@dataclass
class EmergencyContact(PropertyType):
    CONTACT_NOTES = "ContactNotes"
    PHONE_NUMBER = "PhoneNumber"
    EMAIL_ADDRESS = "EmailAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_notes": "ContactNotes",
        "phone_number": "PhoneNumber",
        "email_address": "EmailAddress",
    }

    contact_notes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

