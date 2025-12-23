"""PropertyTypes for AWS::DataZone::Owner."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OwnerGroupProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_identifier": "GroupIdentifier",
    }

    group_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OwnerProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group": "Group",
        "user": "User",
    }

    group: Optional[OwnerGroupProperties] = None
    user: Optional[OwnerUserProperties] = None


@dataclass
class OwnerUserProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "user_identifier": "UserIdentifier",
    }

    user_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

