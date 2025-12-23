"""PropertyTypes for AWS::Amplify::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Certificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_type": "CertificateType",
        "certificate_verification_dns_record": "CertificateVerificationDNSRecord",
        "certificate_arn": "CertificateArn",
    }

    certificate_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_verification_dns_record: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CertificateSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_type": "CertificateType",
        "custom_certificate_arn": "CustomCertificateArn",
    }

    certificate_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubDomainSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix": "Prefix",
        "branch_name": "BranchName",
    }

    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    branch_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

