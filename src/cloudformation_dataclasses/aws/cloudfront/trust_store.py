"""PropertyTypes for AWS::CloudFront::TrustStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CaCertificatesBundleS3Location(PropertyType):
    BUCKET = "Bucket"
    VERSION = "Version"
    REGION = "Region"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "region": "Region",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CaCertificatesBundleSource(PropertyType):
    CA_CERTIFICATES_BUNDLE_S3_LOCATION = "CaCertificatesBundleS3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ca_certificates_bundle_s3_location": "CaCertificatesBundleS3Location",
    }

    ca_certificates_bundle_s3_location: Optional[CaCertificatesBundleS3Location] = None

