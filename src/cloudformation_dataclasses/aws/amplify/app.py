"""PropertyTypes for AWS::Amplify::App."""

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
class AutoBranchCreationConfig(PropertyType):
    ENVIRONMENT_VARIABLES = "EnvironmentVariables"
    AUTO_BRANCH_CREATION_PATTERNS = "AutoBranchCreationPatterns"
    ENABLE_AUTO_BRANCH_CREATION = "EnableAutoBranchCreation"
    PULL_REQUEST_ENVIRONMENT_NAME = "PullRequestEnvironmentName"
    ENABLE_PULL_REQUEST_PREVIEW = "EnablePullRequestPreview"
    ENABLE_AUTO_BUILD = "EnableAutoBuild"
    ENABLE_PERFORMANCE_MODE = "EnablePerformanceMode"
    BUILD_SPEC = "BuildSpec"
    STAGE = "Stage"
    BASIC_AUTH_CONFIG = "BasicAuthConfig"
    FRAMEWORK = "Framework"

    _property_mappings: ClassVar[dict[str, str]] = {
        "environment_variables": "EnvironmentVariables",
        "auto_branch_creation_patterns": "AutoBranchCreationPatterns",
        "enable_auto_branch_creation": "EnableAutoBranchCreation",
        "pull_request_environment_name": "PullRequestEnvironmentName",
        "enable_pull_request_preview": "EnablePullRequestPreview",
        "enable_auto_build": "EnableAutoBuild",
        "enable_performance_mode": "EnablePerformanceMode",
        "build_spec": "BuildSpec",
        "stage": "Stage",
        "basic_auth_config": "BasicAuthConfig",
        "framework": "Framework",
    }

    environment_variables: Optional[list[EnvironmentVariable]] = None
    auto_branch_creation_patterns: Optional[Union[list[str], Ref]] = None
    enable_auto_branch_creation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    pull_request_environment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_pull_request_preview: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_auto_build: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_performance_mode: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    build_spec: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    basic_auth_config: Optional[BasicAuthConfig] = None
    framework: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class CacheConfig(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomRule(PropertyType):
    CONDITION = "Condition"
    STATUS = "Status"
    TARGET = "Target"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "status": "Status",
        "target": "Target",
        "source": "Source",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


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


@dataclass
class JobConfig(PropertyType):
    BUILD_COMPUTE_TYPE = "BuildComputeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "build_compute_type": "BuildComputeType",
    }

    build_compute_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

