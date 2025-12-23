"""PropertyTypes for AWS::ApiGatewayV2::Api."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BodyS3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "etag": "Etag",
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    etag: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Cors(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_origins": "AllowOrigins",
        "allow_credentials": "AllowCredentials",
        "expose_headers": "ExposeHeaders",
        "allow_headers": "AllowHeaders",
        "max_age": "MaxAge",
        "allow_methods": "AllowMethods",
    }

    allow_origins: Optional[Union[list[str], Ref]] = None
    allow_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expose_headers: Optional[Union[list[str], Ref]] = None
    allow_headers: Optional[Union[list[str], Ref]] = None
    max_age: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allow_methods: Optional[Union[list[str], Ref]] = None

