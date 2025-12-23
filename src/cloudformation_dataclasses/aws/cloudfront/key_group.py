"""PropertyTypes for AWS::CloudFront::KeyGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class KeyGroupConfig(PropertyType):
    COMMENT = "Comment"
    ITEMS = "Items"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "items": "Items",
        "name": "Name",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    items: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

