"""PropertyTypes for AWS::IoTWireless::NetworkAnalyzerConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TraceContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "wireless_device_frame_info": "WirelessDeviceFrameInfo",
        "log_level": "LogLevel",
    }

    wireless_device_frame_info: Optional[Union[str, WirelessDeviceFrameInfo, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, LogLevel, Ref, GetAtt, Sub]] = None

