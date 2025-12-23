"""PropertyTypes for AWS::SSMGuiConnect::Preferences."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionRecordingPreferences(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
        "recording_destinations": "RecordingDestinations",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recording_destinations: Optional[RecordingDestinations] = None


@dataclass
class RecordingDestinations(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_buckets": "S3Buckets",
    }

    s3_buckets: Optional[list[S3Bucket]] = None


@dataclass
class S3Bucket(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_owner": "BucketOwner",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None

