"""PropertyTypes for AWS::EC2::NetworkAclEntry."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Icmp(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "code": "Code",
    }

    type_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PortRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
    }

    from_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to: Optional[Union[int, Ref, GetAtt, Sub]] = None

