"""PropertyTypes for AWS::SES::ReceiptFilter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Filter(PropertyType):
    IP_FILTER = "IpFilter"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_filter": "IpFilter",
        "name": "Name",
    }

    ip_filter: Optional[IpFilter] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IpFilter(PropertyType):
    POLICY = "Policy"
    CIDR = "Cidr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
        "cidr": "Cidr",
    }

    policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None

