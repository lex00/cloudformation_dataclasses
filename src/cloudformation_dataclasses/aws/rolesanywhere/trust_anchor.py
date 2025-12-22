"""PropertyTypes for AWS::RolesAnywhere::TrustAnchor."""

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
class NotificationSetting(PropertyType):
    CHANNEL = "Channel"
    ENABLED = "Enabled"
    EVENT = "Event"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel": "Channel",
        "enabled": "Enabled",
        "event": "Event",
        "threshold": "Threshold",
    }

    channel: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    SOURCE_TYPE = "SourceType"
    SOURCE_DATA = "SourceData"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_type": "SourceType",
        "source_data": "SourceData",
    }

    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_data: Optional[SourceData] = None


@dataclass
class SourceData(PropertyType):
    ACM_PCA_ARN = "AcmPcaArn"
    X509_CERTIFICATE_DATA = "X509CertificateData"

    _property_mappings: ClassVar[dict[str, str]] = {
        "acm_pca_arn": "AcmPcaArn",
        "x509_certificate_data": "X509CertificateData",
    }

    acm_pca_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    x509_certificate_data: Optional[Union[str, Ref, GetAtt, Sub]] = None

