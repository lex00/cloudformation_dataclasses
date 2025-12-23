"""PropertyTypes for AWS::CodeBuild::ReportGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ReportExportConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_destination": "S3Destination",
        "export_config_type": "ExportConfigType",
    }

    s3_destination: Optional[S3ReportExportConfig] = None
    export_config_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3ReportExportConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "bucket": "Bucket",
        "packaging": "Packaging",
        "encryption_key": "EncryptionKey",
        "bucket_owner": "BucketOwner",
        "encryption_disabled": "EncryptionDisabled",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    packaging: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

