"""PropertyTypes for AWS::SSM::Association."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InstanceAssociationOutputLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_location": "S3Location",
    }

    s3_location: Optional[S3OutputLocation] = None


@dataclass
class S3OutputLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_s3_key_prefix": "OutputS3KeyPrefix",
        "output_s3_region": "OutputS3Region",
        "output_s3_bucket_name": "OutputS3BucketName",
    }

    output_s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Target(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

