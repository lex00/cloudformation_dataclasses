"""PropertyTypes for AWS::RolesAnywhere::Profile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CertificateField:
    """CertificateField enum values."""

    X509SUBJECT = "x509Subject"
    X509ISSUER = "x509Issuer"
    X509SAN = "x509SAN"


class NotificationChannel:
    """NotificationChannel enum values."""

    ALL = "ALL"


class NotificationEvent:
    """NotificationEvent enum values."""

    CA_CERTIFICATE_EXPIRY = "CA_CERTIFICATE_EXPIRY"
    END_ENTITY_CERTIFICATE_EXPIRY = "END_ENTITY_CERTIFICATE_EXPIRY"


class TrustAnchorType:
    """TrustAnchorType enum values."""

    AWS_ACM_PCA = "AWS_ACM_PCA"
    CERTIFICATE_BUNDLE = "CERTIFICATE_BUNDLE"
    SELF_SIGNED_REPOSITORY = "SELF_SIGNED_REPOSITORY"


@dataclass
class AttributeMapping(PropertyType):
    MAPPING_RULES = "MappingRules"
    CERTIFICATE_FIELD = "CertificateField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mapping_rules": "MappingRules",
        "certificate_field": "CertificateField",
    }

    mapping_rules: Optional[list[MappingRule]] = None
    certificate_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MappingRule(PropertyType):
    SPECIFIER = "Specifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "specifier": "Specifier",
    }

    specifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

