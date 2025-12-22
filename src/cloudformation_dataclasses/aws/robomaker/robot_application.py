"""PropertyTypes for AWS::RoboMaker::RobotApplication."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RobotSoftwareSuite(PropertyType):
    VERSION = "Version"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "name": "Name",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConfig(PropertyType):
    S3_BUCKET = "S3Bucket"
    ARCHITECTURE = "Architecture"
    S3_KEY = "S3Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "architecture": "Architecture",
        "s3_key": "S3Key",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    architecture: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

