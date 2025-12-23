"""PropertyTypes for AWS::IoTWireless::MulticastGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoRaWAN(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_devices_requested": "NumberOfDevicesRequested",
        "number_of_devices_in_group": "NumberOfDevicesInGroup",
        "rf_region": "RfRegion",
        "dl_class": "DlClass",
    }

    number_of_devices_requested: Optional[Union[int, Ref, GetAtt, Sub]] = None
    number_of_devices_in_group: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rf_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dl_class: Optional[Union[str, Ref, GetAtt, Sub]] = None

