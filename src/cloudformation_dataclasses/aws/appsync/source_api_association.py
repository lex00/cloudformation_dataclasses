"""PropertyTypes for AWS::AppSync::SourceApiAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SourceApiAssociationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "merge_type": "MergeType",
    }

    merge_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

