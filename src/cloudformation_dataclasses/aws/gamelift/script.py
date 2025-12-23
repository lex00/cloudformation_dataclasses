"""PropertyTypes for AWS::GameLift::Script."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class S3Location(PropertyType):
    OBJECT_VERSION = "ObjectVersion"
    BUCKET = "Bucket"
    KEY = "Key"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_version": "ObjectVersion",
        "bucket": "Bucket",
        "key": "Key",
        "role_arn": "RoleArn",
    }

    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

