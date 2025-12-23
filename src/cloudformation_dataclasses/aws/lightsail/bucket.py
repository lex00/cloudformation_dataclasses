"""PropertyTypes for AWS::Lightsail::Bucket."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessRules(PropertyType):
    ALLOW_PUBLIC_OVERRIDES = "AllowPublicOverrides"
    GET_OBJECT = "GetObject"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_public_overrides": "AllowPublicOverrides",
        "get_object": "GetObject",
    }

    allow_public_overrides: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    get_object: Optional[Union[str, Ref, GetAtt, Sub]] = None

