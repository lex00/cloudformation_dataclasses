"""PropertyTypes for AWS::ECR::RepositoryCreationTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ArtifactStatus:
    """ArtifactStatus enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"


class ArtifactStatusFilter:
    """ArtifactStatusFilter enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"
    ANY = "ANY"


class EncryptionType:
    """EncryptionType enum values."""

    AES256 = "AES256"
    KMS = "KMS"
    KMS_DSSE = "KMS_DSSE"


class FindingSeverity:
    """FindingSeverity enum values."""

    INFORMATIONAL = "INFORMATIONAL"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"
    UNDEFINED = "UNDEFINED"


class ImageActionType:
    """ImageActionType enum values."""

    EXPIRE = "EXPIRE"
    TRANSITION = "TRANSITION"


class ImageFailureCode:
    """ImageFailureCode enum values."""

    INVALIDIMAGEDIGEST = "InvalidImageDigest"
    INVALIDIMAGETAG = "InvalidImageTag"
    IMAGETAGDOESNOTMATCHDIGEST = "ImageTagDoesNotMatchDigest"
    IMAGENOTFOUND = "ImageNotFound"
    MISSINGDIGESTANDTAG = "MissingDigestAndTag"
    IMAGEREFERENCEDBYMANIFESTLIST = "ImageReferencedByManifestList"
    KMSERROR = "KmsError"
    UPSTREAMACCESSDENIED = "UpstreamAccessDenied"
    UPSTREAMTOOMANYREQUESTS = "UpstreamTooManyRequests"
    UPSTREAMUNAVAILABLE = "UpstreamUnavailable"
    IMAGEINACCESSIBLE = "ImageInaccessible"


class ImageStatus:
    """ImageStatus enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"


class ImageStatusFilter:
    """ImageStatusFilter enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"
    ANY = "ANY"


class ImageTagMutability:
    """ImageTagMutability enum values."""

    MUTABLE = "MUTABLE"
    IMMUTABLE = "IMMUTABLE"
    IMMUTABLE_WITH_EXCLUSION = "IMMUTABLE_WITH_EXCLUSION"
    MUTABLE_WITH_EXCLUSION = "MUTABLE_WITH_EXCLUSION"


class ImageTagMutabilityExclusionFilterType:
    """ImageTagMutabilityExclusionFilterType enum values."""

    WILDCARD = "WILDCARD"


class LayerAvailability:
    """LayerAvailability enum values."""

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    ARCHIVED = "ARCHIVED"


class LayerFailureCode:
    """LayerFailureCode enum values."""

    INVALIDLAYERDIGEST = "InvalidLayerDigest"
    MISSINGLAYERDIGEST = "MissingLayerDigest"


class LifecyclePolicyPreviewStatus:
    """LifecyclePolicyPreviewStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"


class LifecyclePolicyStorageClass:
    """LifecyclePolicyStorageClass enum values."""

    ARCHIVE = "ARCHIVE"
    STANDARD = "STANDARD"


class LifecyclePolicyTargetStorageClass:
    """LifecyclePolicyTargetStorageClass enum values."""

    ARCHIVE = "ARCHIVE"


class RCTAppliedFor:
    """RCTAppliedFor enum values."""

    REPLICATION = "REPLICATION"
    PULL_THROUGH_CACHE = "PULL_THROUGH_CACHE"


class ReplicationStatus:
    """ReplicationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class RepositoryFilterType:
    """RepositoryFilterType enum values."""

    PREFIX_MATCH = "PREFIX_MATCH"


class ScanFrequency:
    """ScanFrequency enum values."""

    SCAN_ON_PUSH = "SCAN_ON_PUSH"
    CONTINUOUS_SCAN = "CONTINUOUS_SCAN"
    MANUAL = "MANUAL"


class ScanStatus:
    """ScanStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    UNSUPPORTED_IMAGE = "UNSUPPORTED_IMAGE"
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    SCAN_ELIGIBILITY_EXPIRED = "SCAN_ELIGIBILITY_EXPIRED"
    FINDINGS_UNAVAILABLE = "FINDINGS_UNAVAILABLE"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    IMAGE_ARCHIVED = "IMAGE_ARCHIVED"


class ScanType:
    """ScanType enum values."""

    BASIC = "BASIC"
    ENHANCED = "ENHANCED"


class ScanningConfigurationFailureCode:
    """ScanningConfigurationFailureCode enum values."""

    REPOSITORY_NOT_FOUND = "REPOSITORY_NOT_FOUND"


class ScanningRepositoryFilterType:
    """ScanningRepositoryFilterType enum values."""

    WILDCARD = "WILDCARD"


class SigningRepositoryFilterType:
    """SigningRepositoryFilterType enum values."""

    WILDCARD_MATCH = "WILDCARD_MATCH"


class SigningStatus:
    """SigningStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class TagStatus:
    """TagStatus enum values."""

    TAGGED = "TAGGED"
    UNTAGGED = "UNTAGGED"
    ANY = "ANY"


class TargetStorageClass:
    """TargetStorageClass enum values."""

    STANDARD = "STANDARD"
    ARCHIVE = "ARCHIVE"


class UpstreamRegistry:
    """UpstreamRegistry enum values."""

    ECR = "ecr"
    ECR_PUBLIC = "ecr-public"
    QUAY = "quay"
    K8S = "k8s"
    DOCKER_HUB = "docker-hub"
    GITHUB_CONTAINER_REGISTRY = "github-container-registry"
    AZURE_CONTAINER_REGISTRY = "azure-container-registry"
    GITLAB_CONTAINER_REGISTRY = "gitlab-container-registry"


@dataclass
class EncryptionConfiguration(PropertyType):
    ENCRYPTION_TYPE = "EncryptionType"
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "kms_key": "KmsKey",
    }

    encryption_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageTagMutabilityExclusionFilter(PropertyType):
    IMAGE_TAG_MUTABILITY_EXCLUSION_FILTER_TYPE = "ImageTagMutabilityExclusionFilterType"
    IMAGE_TAG_MUTABILITY_EXCLUSION_FILTER_VALUE = "ImageTagMutabilityExclusionFilterValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_tag_mutability_exclusion_filter_type": "ImageTagMutabilityExclusionFilterType",
        "image_tag_mutability_exclusion_filter_value": "ImageTagMutabilityExclusionFilterValue",
    }

    image_tag_mutability_exclusion_filter_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_tag_mutability_exclusion_filter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None

