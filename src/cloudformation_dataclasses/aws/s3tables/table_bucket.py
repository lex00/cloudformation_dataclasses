"""PropertyTypes for AWS::S3Tables::TableBucket."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
        "sse_algorithm": "SSEAlgorithm",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageClassConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
    }

    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UnreferencedFileRemoval(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "noncurrent_days": "NoncurrentDays",
        "unreferenced_days": "UnreferencedDays",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    noncurrent_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unreferenced_days: Optional[Union[int, Ref, GetAtt, Sub]] = None

