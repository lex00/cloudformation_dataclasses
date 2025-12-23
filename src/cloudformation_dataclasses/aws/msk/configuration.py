"""PropertyTypes for AWS::MSK::Configuration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LatestRevision(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "revision": "Revision",
        "creation_time": "CreationTime",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    creation_time: Optional[Union[str, Ref, GetAtt, Sub]] = None

