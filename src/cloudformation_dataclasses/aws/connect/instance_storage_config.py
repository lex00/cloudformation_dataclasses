"""PropertyTypes for AWS::Connect::InstanceStorageConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EncryptionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "key_id": "KeyId",
    }

    encryption_type: Optional[Union[str, EncryptionType, Ref, GetAtt, Sub]] = None
    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisFirehoseConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "firehose_arn": "FirehoseArn",
    }

    firehose_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_arn": "StreamArn",
    }

    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisVideoStreamConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix": "Prefix",
        "retention_period_hours": "RetentionPeriodHours",
        "encryption_config": "EncryptionConfig",
    }

    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retention_period_hours: Optional[Union[float, Ref, GetAtt, Sub]] = None
    encryption_config: Optional[EncryptionConfig] = None


@dataclass
class S3Config(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
        "encryption_config": "EncryptionConfig",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_config: Optional[EncryptionConfig] = None

