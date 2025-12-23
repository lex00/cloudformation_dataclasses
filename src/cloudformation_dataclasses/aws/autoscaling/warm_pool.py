"""PropertyTypes for AWS::AutoScaling::WarmPool."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InstanceReusePolicy(PropertyType):
    REUSE_ON_SCALE_IN = "ReuseOnScaleIn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "reuse_on_scale_in": "ReuseOnScaleIn",
    }

    reuse_on_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None

