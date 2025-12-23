"""PropertyTypes for AWS::DataZone::FormType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Model(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "smithy": "Smithy",
    }

    smithy: Optional[Union[str, Ref, GetAtt, Sub]] = None

