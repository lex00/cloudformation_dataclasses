"""PropertyTypes for AWS::Evidently::Project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppConfigResourceObject(PropertyType):
    ENVIRONMENT_ID = "EnvironmentId"
    APPLICATION_ID = "ApplicationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "environment_id": "EnvironmentId",
        "application_id": "ApplicationId",
    }

    environment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataDeliveryObject(PropertyType):
    S3 = "S3"
    LOG_GROUP = "LogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "log_group": "LogGroup",
    }

    s3: Optional[S3Destination] = None
    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Destination(PropertyType):
    BUCKET_NAME = "BucketName"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "prefix": "Prefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

