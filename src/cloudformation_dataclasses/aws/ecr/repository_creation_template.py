"""PropertyTypes for AWS::ECR::RepositoryCreationTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

