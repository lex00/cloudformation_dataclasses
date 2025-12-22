"""PropertyTypes for AWS::CodeArtifact::PackageGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AllowPublish:
    """AllowPublish enum values."""

    ALLOW = "ALLOW"
    BLOCK = "BLOCK"


class AllowUpstream:
    """AllowUpstream enum values."""

    ALLOW = "ALLOW"
    BLOCK = "BLOCK"


class DomainStatus:
    """DomainStatus enum values."""

    ACTIVE = "Active"
    DELETED = "Deleted"


class EndpointType:
    """EndpointType enum values."""

    DUALSTACK = "dualstack"
    IPV4 = "ipv4"


class ExternalConnectionStatus:
    """ExternalConnectionStatus enum values."""

    AVAILABLE = "Available"


class HashAlgorithm:
    """HashAlgorithm enum values."""

    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"


class PackageFormat:
    """PackageFormat enum values."""

    NPM = "npm"
    PYPI = "pypi"
    MAVEN = "maven"
    NUGET = "nuget"
    GENERIC = "generic"
    RUBY = "ruby"
    SWIFT = "swift"
    CARGO = "cargo"


class PackageGroupAllowedRepositoryUpdateType:
    """PackageGroupAllowedRepositoryUpdateType enum values."""

    ADDED = "ADDED"
    REMOVED = "REMOVED"


class PackageGroupAssociationType:
    """PackageGroupAssociationType enum values."""

    STRONG = "STRONG"
    WEAK = "WEAK"


class PackageGroupOriginRestrictionMode:
    """PackageGroupOriginRestrictionMode enum values."""

    ALLOW = "ALLOW"
    ALLOW_SPECIFIC_REPOSITORIES = "ALLOW_SPECIFIC_REPOSITORIES"
    BLOCK = "BLOCK"
    INHERIT = "INHERIT"


class PackageGroupOriginRestrictionType:
    """PackageGroupOriginRestrictionType enum values."""

    EXTERNAL_UPSTREAM = "EXTERNAL_UPSTREAM"
    INTERNAL_UPSTREAM = "INTERNAL_UPSTREAM"
    PUBLISH = "PUBLISH"


class PackageVersionErrorCode:
    """PackageVersionErrorCode enum values."""

    ALREADY_EXISTS = "ALREADY_EXISTS"
    MISMATCHED_REVISION = "MISMATCHED_REVISION"
    MISMATCHED_STATUS = "MISMATCHED_STATUS"
    NOT_ALLOWED = "NOT_ALLOWED"
    NOT_FOUND = "NOT_FOUND"
    SKIPPED = "SKIPPED"


class PackageVersionOriginType:
    """PackageVersionOriginType enum values."""

    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    UNKNOWN = "UNKNOWN"


class PackageVersionSortType:
    """PackageVersionSortType enum values."""

    PUBLISHED_TIME = "PUBLISHED_TIME"


class PackageVersionStatus:
    """PackageVersionStatus enum values."""

    PUBLISHED = "Published"
    UNFINISHED = "Unfinished"
    UNLISTED = "Unlisted"
    ARCHIVED = "Archived"
    DISPOSED = "Disposed"
    DELETED = "Deleted"


class ResourceType:
    """ResourceType enum values."""

    DOMAIN = "domain"
    REPOSITORY = "repository"
    PACKAGE = "package"
    PACKAGE_VERSION = "package-version"
    ASSET = "asset"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    CANNOT_PARSE = "CANNOT_PARSE"
    ENCRYPTION_KEY_ERROR = "ENCRYPTION_KEY_ERROR"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    OTHER = "OTHER"


@dataclass
class OriginConfiguration(PropertyType):
    RESTRICTIONS = "Restrictions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "restrictions": "Restrictions",
    }

    restrictions: Optional[Restrictions] = None


@dataclass
class RestrictionType(PropertyType):
    REPOSITORIES = "Repositories"
    RESTRICTION_MODE = "RestrictionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repositories": "Repositories",
        "restriction_mode": "RestrictionMode",
    }

    repositories: Optional[Union[list[str], Ref]] = None
    restriction_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Restrictions(PropertyType):
    EXTERNAL_UPSTREAM = "ExternalUpstream"
    PUBLISH = "Publish"
    INTERNAL_UPSTREAM = "InternalUpstream"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_upstream": "ExternalUpstream",
        "publish": "Publish",
        "internal_upstream": "InternalUpstream",
    }

    external_upstream: Optional[RestrictionType] = None
    publish: Optional[RestrictionType] = None
    internal_upstream: Optional[RestrictionType] = None

