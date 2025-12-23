"""PropertyTypes for AWS::ApiGateway::DomainNameV2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EndpointConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "types": "Types",
    }

    ip_address_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    types: Optional[Union[list[str], Ref]] = None

