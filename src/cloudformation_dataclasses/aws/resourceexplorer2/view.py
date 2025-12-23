"""PropertyTypes for AWS::ResourceExplorer2::View."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IncludedProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SearchFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_string": "FilterString",
    }

    filter_string: Optional[Union[str, Ref, GetAtt, Sub]] = None

