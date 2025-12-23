"""PropertyTypes for AWS::DataBrew::Project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Sample(PropertyType):
    TYPE = "Type"
    SIZE = "Size"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "size": "Size",
    }

    type_: Optional[Union[str, SampleType, Ref, GetAtt, Sub]] = None
    size: Optional[Union[int, Ref, GetAtt, Sub]] = None

