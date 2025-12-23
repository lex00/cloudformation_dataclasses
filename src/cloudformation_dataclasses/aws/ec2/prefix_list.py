"""PropertyTypes for AWS::EC2::PrefixList."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Entry(PropertyType):
    DESCRIPTION = "Description"
    CIDR = "Cidr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "cidr": "Cidr",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None

