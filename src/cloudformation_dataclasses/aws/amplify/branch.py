"""PropertyTypes for AWS::Amplify::Branch."""

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
class Backend(PropertyType):
    STACK_ARN = "StackArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stack_arn": "StackArn",
    }

    stack_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthConfig(PropertyType):
    USERNAME = "Username"
    ENABLE_BASIC_AUTH = "EnableBasicAuth"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "enable_basic_auth": "EnableBasicAuth",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_basic_auth: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentVariable(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

