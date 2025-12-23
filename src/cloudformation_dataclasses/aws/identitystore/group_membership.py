"""PropertyTypes for AWS::IdentityStore::GroupMembership."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MemberId(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "user_id": "UserId",
    }

    user_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

