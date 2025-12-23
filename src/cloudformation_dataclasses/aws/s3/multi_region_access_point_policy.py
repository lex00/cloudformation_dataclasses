"""PropertyTypes for AWS::S3::MultiRegionAccessPointPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PolicyStatus(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_public": "IsPublic",
    }

    is_public: Optional[Union[str, Ref, GetAtt, Sub]] = None

