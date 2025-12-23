"""PropertyTypes for AWS::EC2::TransitGatewayConnect."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TransitGatewayConnectOptions(PropertyType):
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol": "Protocol",
    }

    protocol: Optional[Union[str, ProtocolValue, Ref, GetAtt, Sub]] = None

