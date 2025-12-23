"""PropertyTypes for AWS::RDS::GlobalCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GlobalEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None

