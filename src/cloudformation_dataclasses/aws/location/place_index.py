"""PropertyTypes for AWS::Location::PlaceIndex."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intended_use": "IntendedUse",
    }

    intended_use: Optional[Union[str, IntendedUse, Ref, GetAtt, Sub]] = None

