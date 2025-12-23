"""PropertyTypes for AWS::ApiGatewayV2::Authorizer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class JWTConfiguration(PropertyType):
    ISSUER = "Issuer"
    AUDIENCE = "Audience"

    _property_mappings: ClassVar[dict[str, str]] = {
        "issuer": "Issuer",
        "audience": "Audience",
    }

    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audience: Optional[Union[list[str], Ref]] = None

