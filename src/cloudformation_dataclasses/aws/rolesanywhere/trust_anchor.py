"""PropertyTypes for AWS::RolesAnywhere::TrustAnchor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NotificationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel": "Channel",
        "enabled": "Enabled",
        "event": "Event",
        "threshold": "Threshold",
    }

    channel: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_type": "SourceType",
        "source_data": "SourceData",
    }

    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_data: Optional[SourceData] = None


@dataclass
class SourceData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm_pca_arn": "AcmPcaArn",
        "x509_certificate_data": "X509CertificateData",
    }

    acm_pca_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    x509_certificate_data: Optional[Union[str, Ref, GetAtt, Sub]] = None

