"""PropertyTypes for AWS::Cognito::UserPoolResourceServer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourceServerScopeType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scope_name": "ScopeName",
        "scope_description": "ScopeDescription",
    }

    scope_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scope_description: Optional[Union[str, Ref, GetAtt, Sub]] = None

