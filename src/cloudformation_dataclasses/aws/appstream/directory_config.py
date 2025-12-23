"""PropertyTypes for AWS::AppStream::DirectoryConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CertificateBasedAuthProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "certificate_authority_arn": "CertificateAuthorityArn",
    }

    status: Optional[Union[str, CertificateBasedAuthStatus, Ref, GetAtt, Sub]] = None
    certificate_authority_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceAccountCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "account_name": "AccountName",
        "account_password": "AccountPassword",
    }

    account_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_password: Optional[Union[str, Ref, GetAtt, Sub]] = None

