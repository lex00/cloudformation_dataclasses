"""PropertyTypes for AWS::SimSpaceWeaver::Simulation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class S3Location(PropertyType):
    BUCKET_NAME = "BucketName"
    OBJECT_KEY = "ObjectKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "object_key": "ObjectKey",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

