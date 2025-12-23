"""PropertyTypes for AWS::KafkaConnect::CustomPlugin."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomPluginFileDescription(PropertyType):
    FILE_MD5 = "FileMd5"
    FILE_SIZE = "FileSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "file_md5": "FileMd5",
        "file_size": "FileSize",
    }

    file_md5: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPluginLocation(PropertyType):
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_location": "S3Location",
    }

    s3_location: Optional[S3Location] = None


@dataclass
class S3Location(PropertyType):
    BUCKET_ARN = "BucketArn"
    FILE_KEY = "FileKey"
    OBJECT_VERSION = "ObjectVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "file_key": "FileKey",
        "object_version": "ObjectVersion",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

