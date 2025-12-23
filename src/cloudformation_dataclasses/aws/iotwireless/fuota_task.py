"""PropertyTypes for AWS::IoTWireless::FuotaTask."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoRaWAN(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rf_region": "RfRegion",
        "start_time": "StartTime",
    }

    rf_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None

