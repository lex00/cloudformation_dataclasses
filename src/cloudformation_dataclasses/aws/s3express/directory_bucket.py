"""PropertyTypes for AWS::S3Express::DirectoryBucket."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days_after_initiation": "DaysAfterInitiation",
    }

    days_after_initiation: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BucketEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "server_side_encryption_configuration": "ServerSideEncryptionConfiguration",
    }

    server_side_encryption_configuration: Optional[list[ServerSideEncryptionRule]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[Rule]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "expiration_in_days": "ExpirationInDays",
        "object_size_greater_than": "ObjectSizeGreaterThan",
        "id": "Id",
        "prefix": "Prefix",
        "abort_incomplete_multipart_upload": "AbortIncompleteMultipartUpload",
        "object_size_less_than": "ObjectSizeLessThan",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    object_size_greater_than: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = None
    object_size_less_than: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_algorithm": "SSEAlgorithm",
        "kms_master_key_id": "KMSMasterKeyID",
    }

    sse_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_master_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_key_enabled": "BucketKeyEnabled",
        "server_side_encryption_by_default": "ServerSideEncryptionByDefault",
    }

    bucket_key_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    server_side_encryption_by_default: Optional[ServerSideEncryptionByDefault] = None

