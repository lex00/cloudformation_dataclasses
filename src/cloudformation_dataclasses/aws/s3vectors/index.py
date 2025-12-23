"""PropertyTypes for AWS::S3Vectors::Index."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "sse_type": "SseType",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "non_filterable_metadata_keys": "NonFilterableMetadataKeys",
    }

    non_filterable_metadata_keys: Optional[Union[list[str], Ref]] = None

