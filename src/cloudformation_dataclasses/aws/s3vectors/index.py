"""PropertyTypes for AWS::S3Vectors::Index."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class DataType:
    """DataType enum values."""

    FLOAT32 = "float32"


class DistanceMetric:
    """DistanceMetric enum values."""

    EUCLIDEAN = "euclidean"
    COSINE = "cosine"


class SseType:
    """SseType enum values."""

    AES256 = "AES256"
    AWS_KMS = "aws:kms"


@dataclass
class EncryptionConfiguration(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    SSE_TYPE = "SseType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "sse_type": "SseType",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataConfiguration(PropertyType):
    NON_FILTERABLE_METADATA_KEYS = "NonFilterableMetadataKeys"

    _property_mappings: ClassVar[dict[str, str]] = {
        "non_filterable_metadata_keys": "NonFilterableMetadataKeys",
    }

    non_filterable_metadata_keys: Optional[Union[list[str], Ref]] = None

