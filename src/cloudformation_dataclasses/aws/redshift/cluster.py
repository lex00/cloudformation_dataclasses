"""PropertyTypes for AWS::Redshift::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Endpoint(PropertyType):
    ADDRESS = "Address"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingProperties(PropertyType):
    BUCKET_NAME = "BucketName"
    S3_KEY_PREFIX = "S3KeyPrefix"
    LOG_DESTINATION_TYPE = "LogDestinationType"
    LOG_EXPORTS = "LogExports"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "s3_key_prefix": "S3KeyPrefix",
        "log_destination_type": "LogDestinationType",
        "log_exports": "LogExports",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_destination_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_exports: Optional[Union[list[str], Ref]] = None

