"""PropertyTypes for AWS::IoTSiteWise::Gateway."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GatewayCapabilitySummary(PropertyType):
    CAPABILITY_NAMESPACE = "CapabilityNamespace"
    CAPABILITY_CONFIGURATION = "CapabilityConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capability_namespace": "CapabilityNamespace",
        "capability_configuration": "CapabilityConfiguration",
    }

    capability_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capability_configuration: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GatewayPlatform(PropertyType):
    GREENGRASS_V2 = "GreengrassV2"
    SIEMENS_IE = "SiemensIE"

    _property_mappings: ClassVar[dict[str, str]] = {
        "greengrass_v2": "GreengrassV2",
        "siemens_ie": "SiemensIE",
    }

    greengrass_v2: Optional[GreengrassV2] = None
    siemens_ie: Optional[SiemensIE] = None


@dataclass
class GreengrassV2(PropertyType):
    CORE_DEVICE_THING_NAME = "CoreDeviceThingName"
    CORE_DEVICE_OPERATING_SYSTEM = "CoreDeviceOperatingSystem"

    _property_mappings: ClassVar[dict[str, str]] = {
        "core_device_thing_name": "CoreDeviceThingName",
        "core_device_operating_system": "CoreDeviceOperatingSystem",
    }

    core_device_thing_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    core_device_operating_system: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SiemensIE(PropertyType):
    IOT_CORE_THING_NAME = "IotCoreThingName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iot_core_thing_name": "IotCoreThingName",
    }

    iot_core_thing_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

