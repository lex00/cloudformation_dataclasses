"""PropertyTypes for AWS::EC2::IPAMScope."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IpamScopeExternalAuthorityConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "external_resource_identifier": "ExternalResourceIdentifier",
        "ipam_scope_external_authority_type": "IpamScopeExternalAuthorityType",
    }

    external_resource_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipam_scope_external_authority_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

