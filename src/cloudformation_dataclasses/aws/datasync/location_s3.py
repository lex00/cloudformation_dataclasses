"""PropertyTypes for AWS::DataSync::LocationS3."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class S3Config(PropertyType):
    BUCKET_ACCESS_ROLE_ARN = "BucketAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_access_role_arn": "BucketAccessRoleArn",
    }

    bucket_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

