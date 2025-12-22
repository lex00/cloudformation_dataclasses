"""PropertyTypes for AWS::WorkspacesInstances::Volume."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TagSpecification(PropertyType):
    RESOURCE_TYPE = "ResourceType"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None

