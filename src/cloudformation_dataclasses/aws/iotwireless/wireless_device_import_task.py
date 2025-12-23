"""PropertyTypes for AWS::IoTWireless::WirelessDeviceImportTask."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Sidewalk(PropertyType):
    ROLE = "Role"
    SIDEWALK_MANUFACTURING_SN = "SidewalkManufacturingSn"
    DEVICE_CREATION_FILE = "DeviceCreationFile"
    DEVICE_CREATION_FILE_LIST = "DeviceCreationFileList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "sidewalk_manufacturing_sn": "SidewalkManufacturingSn",
        "device_creation_file": "DeviceCreationFile",
        "device_creation_file_list": "DeviceCreationFileList",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sidewalk_manufacturing_sn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_creation_file: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_creation_file_list: Optional[Union[list[str], Ref]] = None

