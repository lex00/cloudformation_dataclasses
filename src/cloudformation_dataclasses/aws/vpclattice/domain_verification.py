"""PropertyTypes for AWS::VpcLattice::DomainVerification."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TxtMethodConfig(PropertyType):
    NAME = "name"
    VALUE = "value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "name",
        "value": "value",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None

