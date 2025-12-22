"""PropertyTypes for AWS::CodeStar::GitHubRepository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Code(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[S3] = None


@dataclass
class S3(PropertyType):
    OBJECT_VERSION = "ObjectVersion"
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_version": "ObjectVersion",
        "bucket": "Bucket",
        "key": "Key",
    }

    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

