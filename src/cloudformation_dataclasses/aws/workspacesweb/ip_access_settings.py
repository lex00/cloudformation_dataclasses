"""PropertyTypes for AWS::WorkSpacesWeb::IpAccessSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IpRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_range": "IpRange",
        "description": "Description",
    }

    ip_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None

