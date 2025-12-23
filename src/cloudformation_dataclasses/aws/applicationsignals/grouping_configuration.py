"""PropertyTypes for AWS::ApplicationSignals::GroupingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GroupingAttributeDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grouping_name": "GroupingName",
        "grouping_source_keys": "GroupingSourceKeys",
        "default_grouping_value": "DefaultGroupingValue",
    }

    grouping_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    grouping_source_keys: Optional[Union[list[str], Ref]] = None
    default_grouping_value: Optional[Union[str, Ref, GetAtt, Sub]] = None

