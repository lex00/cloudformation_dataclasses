"""PropertyTypes for AWS::CertificateManager::Certificate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DomainValidationOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_name": "DomainName",
        "hosted_zone_id": "HostedZoneId",
        "validation_domain": "ValidationDomain",
    }

    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    validation_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None

