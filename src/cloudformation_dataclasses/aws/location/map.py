"""PropertyTypes for AWS::Location::Map."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "political_view": "PoliticalView",
        "style": "Style",
        "custom_layers": "CustomLayers",
    }

    political_view: Optional[Union[str, Ref, GetAtt, Sub]] = None
    style: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_layers: Optional[Union[list[str], Ref]] = None

