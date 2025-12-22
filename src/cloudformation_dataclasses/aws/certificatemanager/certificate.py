"""PropertyTypes for AWS::CertificateManager::Certificate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CertificateExport:
    """CertificateExport enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CertificateManagedBy:
    """CertificateManagedBy enum values."""

    CLOUDFRONT = "CLOUDFRONT"


class CertificateStatus:
    """CertificateStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"


class CertificateTransparencyLoggingPreference:
    """CertificateTransparencyLoggingPreference enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CertificateType:
    """CertificateType enum values."""

    IMPORTED = "IMPORTED"
    AMAZON_ISSUED = "AMAZON_ISSUED"
    PRIVATE = "PRIVATE"


class DomainStatus:
    """DomainStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class ExtendedKeyUsageName:
    """ExtendedKeyUsageName enum values."""

    TLS_WEB_SERVER_AUTHENTICATION = "TLS_WEB_SERVER_AUTHENTICATION"
    TLS_WEB_CLIENT_AUTHENTICATION = "TLS_WEB_CLIENT_AUTHENTICATION"
    CODE_SIGNING = "CODE_SIGNING"
    EMAIL_PROTECTION = "EMAIL_PROTECTION"
    TIME_STAMPING = "TIME_STAMPING"
    OCSP_SIGNING = "OCSP_SIGNING"
    IPSEC_END_SYSTEM = "IPSEC_END_SYSTEM"
    IPSEC_TUNNEL = "IPSEC_TUNNEL"
    IPSEC_USER = "IPSEC_USER"
    ANY = "ANY"
    NONE = "NONE"
    CUSTOM = "CUSTOM"


class FailureReason:
    """FailureReason enum values."""

    NO_AVAILABLE_CONTACTS = "NO_AVAILABLE_CONTACTS"
    ADDITIONAL_VERIFICATION_REQUIRED = "ADDITIONAL_VERIFICATION_REQUIRED"
    DOMAIN_NOT_ALLOWED = "DOMAIN_NOT_ALLOWED"
    INVALID_PUBLIC_DOMAIN = "INVALID_PUBLIC_DOMAIN"
    DOMAIN_VALIDATION_DENIED = "DOMAIN_VALIDATION_DENIED"
    CAA_ERROR = "CAA_ERROR"
    PCA_LIMIT_EXCEEDED = "PCA_LIMIT_EXCEEDED"
    PCA_INVALID_ARN = "PCA_INVALID_ARN"
    PCA_INVALID_STATE = "PCA_INVALID_STATE"
    PCA_REQUEST_FAILED = "PCA_REQUEST_FAILED"
    PCA_NAME_CONSTRAINTS_VALIDATION = "PCA_NAME_CONSTRAINTS_VALIDATION"
    PCA_RESOURCE_NOT_FOUND = "PCA_RESOURCE_NOT_FOUND"
    PCA_INVALID_ARGS = "PCA_INVALID_ARGS"
    PCA_INVALID_DURATION = "PCA_INVALID_DURATION"
    PCA_ACCESS_DENIED = "PCA_ACCESS_DENIED"
    SLR_NOT_FOUND = "SLR_NOT_FOUND"
    OTHER = "OTHER"


class KeyAlgorithm:
    """KeyAlgorithm enum values."""

    RSA_1024 = "RSA_1024"
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"
    EC_PRIME256V1 = "EC_prime256v1"
    EC_SECP384R1 = "EC_secp384r1"
    EC_SECP521R1 = "EC_secp521r1"


class KeyUsageName:
    """KeyUsageName enum values."""

    DIGITAL_SIGNATURE = "DIGITAL_SIGNATURE"
    NON_REPUDIATION = "NON_REPUDIATION"
    KEY_ENCIPHERMENT = "KEY_ENCIPHERMENT"
    DATA_ENCIPHERMENT = "DATA_ENCIPHERMENT"
    KEY_AGREEMENT = "KEY_AGREEMENT"
    CERTIFICATE_SIGNING = "CERTIFICATE_SIGNING"
    CRL_SIGNING = "CRL_SIGNING"
    ENCIPHER_ONLY = "ENCIPHER_ONLY"
    DECIPHER_ONLY = "DECIPHER_ONLY"
    ANY = "ANY"
    CUSTOM = "CUSTOM"


class RecordType:
    """RecordType enum values."""

    CNAME = "CNAME"


class RenewalEligibility:
    """RenewalEligibility enum values."""

    ELIGIBLE = "ELIGIBLE"
    INELIGIBLE = "INELIGIBLE"


class RenewalStatus:
    """RenewalStatus enum values."""

    PENDING_AUTO_RENEWAL = "PENDING_AUTO_RENEWAL"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class RevocationReason:
    """RevocationReason enum values."""

    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CA_COMPROMISE = "CA_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERCEDED = "SUPERCEDED"
    SUPERSEDED = "SUPERSEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    CERTIFICATE_HOLD = "CERTIFICATE_HOLD"
    REMOVE_FROM_CRL = "REMOVE_FROM_CRL"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


class SortBy:
    """SortBy enum values."""

    CREATED_AT = "CREATED_AT"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ValidationMethod:
    """ValidationMethod enum values."""

    EMAIL = "EMAIL"
    DNS = "DNS"
    HTTP = "HTTP"


@dataclass
class DomainValidationOption(PropertyType):
    DOMAIN_NAME = "DomainName"
    HOSTED_ZONE_ID = "HostedZoneId"
    VALIDATION_DOMAIN = "ValidationDomain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_name": "DomainName",
        "hosted_zone_id": "HostedZoneId",
        "validation_domain": "ValidationDomain",
    }

    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    validation_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None

