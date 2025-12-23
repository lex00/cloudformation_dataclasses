"""PropertyTypes for AWS::ElastiCache::User."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthenticationMode(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "passwords": "Passwords",
    }

    type_: Optional[Union[str, InputAuthenticationType, Ref, GetAtt, Sub]] = None
    passwords: Optional[Union[list[str], Ref]] = None

