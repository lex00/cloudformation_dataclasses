"""PropertyTypes for AWS::QuickSight::Folder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourcePermission(PropertyType):
    ACTIONS = "Actions"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "principal": "Principal",
    }

    actions: Optional[Union[list[str], Ref]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None

