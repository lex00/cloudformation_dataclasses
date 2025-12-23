"""PropertyTypes for AWS::EKS::IdentityProviderConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OidcIdentityProviderConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username_prefix": "UsernamePrefix",
        "groups_prefix": "GroupsPrefix",
        "issuer_url": "IssuerUrl",
        "required_claims": "RequiredClaims",
        "client_id": "ClientId",
        "groups_claim": "GroupsClaim",
        "username_claim": "UsernameClaim",
    }

    username_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    groups_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required_claims: Optional[list[RequiredClaim]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    groups_claim: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_claim: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RequiredClaim(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

