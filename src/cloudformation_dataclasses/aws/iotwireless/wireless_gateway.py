"""PropertyTypes for AWS::IoTWireless::WirelessGateway."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoRaWANGateway(PropertyType):
    RF_REGION = "RfRegion"
    GATEWAY_EUI = "GatewayEui"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rf_region": "RfRegion",
        "gateway_eui": "GatewayEui",
    }

    rf_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    gateway_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None

