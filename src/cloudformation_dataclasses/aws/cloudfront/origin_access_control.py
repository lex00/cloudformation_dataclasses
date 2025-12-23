"""PropertyTypes for AWS::CloudFront::OriginAccessControl."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OriginAccessControlConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "signing_behavior": "SigningBehavior",
        "description": "Description",
        "origin_access_control_origin_type": "OriginAccessControlOriginType",
        "signing_protocol": "SigningProtocol",
        "name": "Name",
    }

    signing_behavior: Optional[Union[str, OriginAccessControlSigningBehaviors, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_access_control_origin_type: Optional[Union[str, OriginAccessControlOriginTypes, Ref, GetAtt, Sub]] = None
    signing_protocol: Optional[Union[str, OriginAccessControlSigningProtocols, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

