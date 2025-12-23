"""PropertyTypes for AWS::Timestream::InfluxDBInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LogDeliveryConfiguration(PropertyType):
    S3_CONFIGURATION = "S3Configuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_configuration": "S3Configuration",
    }

    s3_configuration: Optional[S3Configuration] = None


@dataclass
class S3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "enabled": "Enabled",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

