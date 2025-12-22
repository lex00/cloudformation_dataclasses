"""PropertyTypes for AWS::Amplify::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BuildComputeType:
    """BuildComputeType enum values."""

    STANDARD_8GB = "STANDARD_8GB"
    LARGE_16GB = "LARGE_16GB"
    XLARGE_72GB = "XLARGE_72GB"


class CacheConfigType:
    """CacheConfigType enum values."""

    AMPLIFY_MANAGED = "AMPLIFY_MANAGED"
    AMPLIFY_MANAGED_NO_COOKIES = "AMPLIFY_MANAGED_NO_COOKIES"


class CertificateType:
    """CertificateType enum values."""

    AMPLIFY_MANAGED = "AMPLIFY_MANAGED"
    CUSTOM = "CUSTOM"


class DomainStatus:
    """DomainStatus enum values."""

    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    IN_PROGRESS = "IN_PROGRESS"
    AVAILABLE = "AVAILABLE"
    IMPORTING_CUSTOM_CERTIFICATE = "IMPORTING_CUSTOM_CERTIFICATE"
    PENDING_DEPLOYMENT = "PENDING_DEPLOYMENT"
    AWAITING_APP_CNAME = "AWAITING_APP_CNAME"
    FAILED = "FAILED"
    CREATING = "CREATING"
    REQUESTING_CERTIFICATE = "REQUESTING_CERTIFICATE"
    UPDATING = "UPDATING"


class JobStatus:
    """JobStatus enum values."""

    CREATED = "CREATED"
    PENDING = "PENDING"
    PROVISIONING = "PROVISIONING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    SUCCEED = "SUCCEED"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"


class JobType:
    """JobType enum values."""

    RELEASE = "RELEASE"
    RETRY = "RETRY"
    MANUAL = "MANUAL"
    WEB_HOOK = "WEB_HOOK"


class Platform:
    """Platform enum values."""

    WEB = "WEB"
    WEB_DYNAMIC = "WEB_DYNAMIC"
    WEB_COMPUTE = "WEB_COMPUTE"


class RepositoryCloneMethod:
    """RepositoryCloneMethod enum values."""

    SSH = "SSH"
    TOKEN = "TOKEN"
    SIGV4 = "SIGV4"


class SourceUrlType:
    """SourceUrlType enum values."""

    ZIP = "ZIP"
    BUCKET_PREFIX = "BUCKET_PREFIX"


class Stage:
    """Stage enum values."""

    PRODUCTION = "PRODUCTION"
    BETA = "BETA"
    DEVELOPMENT = "DEVELOPMENT"
    EXPERIMENTAL = "EXPERIMENTAL"
    PULL_REQUEST = "PULL_REQUEST"


class UpdateStatus:
    """UpdateStatus enum values."""

    REQUESTING_CERTIFICATE = "REQUESTING_CERTIFICATE"
    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    IMPORTING_CUSTOM_CERTIFICATE = "IMPORTING_CUSTOM_CERTIFICATE"
    PENDING_DEPLOYMENT = "PENDING_DEPLOYMENT"
    AWAITING_APP_CNAME = "AWAITING_APP_CNAME"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"


class WafStatus:
    """WafStatus enum values."""

    ASSOCIATING = "ASSOCIATING"
    ASSOCIATION_FAILED = "ASSOCIATION_FAILED"
    ASSOCIATION_SUCCESS = "ASSOCIATION_SUCCESS"
    DISASSOCIATING = "DISASSOCIATING"
    DISASSOCIATION_FAILED = "DISASSOCIATION_FAILED"


@dataclass
class Certificate(PropertyType):
    CERTIFICATE_TYPE = "CertificateType"
    CERTIFICATE_VERIFICATION_DNS_RECORD = "CertificateVerificationDNSRecord"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_type": "CertificateType",
        "certificate_verification_dns_record": "CertificateVerificationDNSRecord",
        "certificate_arn": "CertificateArn",
    }

    certificate_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_verification_dns_record: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CertificateSettings(PropertyType):
    CERTIFICATE_TYPE = "CertificateType"
    CUSTOM_CERTIFICATE_ARN = "CustomCertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_type": "CertificateType",
        "custom_certificate_arn": "CustomCertificateArn",
    }

    certificate_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubDomainSetting(PropertyType):
    PREFIX = "Prefix"
    BRANCH_NAME = "BranchName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix": "Prefix",
        "branch_name": "BranchName",
    }

    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    branch_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

