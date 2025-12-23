"""PropertyTypes for AWS::IoTWireless::WirelessDevice."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AbpV10x(PropertyType):
    SESSION_KEYS = "SessionKeys"
    DEV_ADDR = "DevAddr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_keys": "SessionKeys",
        "dev_addr": "DevAddr",
    }

    session_keys: Optional[SessionKeysAbpV10x] = None
    dev_addr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AbpV11(PropertyType):
    SESSION_KEYS = "SessionKeys"
    DEV_ADDR = "DevAddr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_keys": "SessionKeys",
        "dev_addr": "DevAddr",
    }

    session_keys: Optional[SessionKeysAbpV11] = None
    dev_addr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Application(PropertyType):
    TYPE = "Type"
    F_PORT = "FPort"
    DESTINATION_NAME = "DestinationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "f_port": "FPort",
        "destination_name": "DestinationName",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    f_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FPorts(PropertyType):
    APPLICATIONS = "Applications"

    _property_mappings: ClassVar[dict[str, str]] = {
        "applications": "Applications",
    }

    applications: Optional[list[Application]] = None


@dataclass
class LoRaWANDevice(PropertyType):
    ABP_V10X = "AbpV10x"
    F_PORTS = "FPorts"
    OTAA_V11 = "OtaaV11"
    ABP_V11 = "AbpV11"
    DEVICE_PROFILE_ID = "DeviceProfileId"
    DEV_EUI = "DevEui"
    OTAA_V10X = "OtaaV10x"
    SERVICE_PROFILE_ID = "ServiceProfileId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "abp_v10x": "AbpV10x",
        "f_ports": "FPorts",
        "otaa_v11": "OtaaV11",
        "abp_v11": "AbpV11",
        "device_profile_id": "DeviceProfileId",
        "dev_eui": "DevEui",
        "otaa_v10x": "OtaaV10x",
        "service_profile_id": "ServiceProfileId",
    }

    abp_v10x: Optional[AbpV10x] = None
    f_ports: Optional[FPorts] = None
    otaa_v11: Optional[OtaaV11] = None
    abp_v11: Optional[AbpV11] = None
    device_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dev_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None
    otaa_v10x: Optional[OtaaV10x] = None
    service_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OtaaV10x(PropertyType):
    APP_EUI = "AppEui"
    APP_KEY = "AppKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_eui": "AppEui",
        "app_key": "AppKey",
    }

    app_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OtaaV11(PropertyType):
    NWK_KEY = "NwkKey"
    APP_KEY = "AppKey"
    JOIN_EUI = "JoinEui"

    _property_mappings: ClassVar[dict[str, str]] = {
        "nwk_key": "NwkKey",
        "app_key": "AppKey",
        "join_eui": "JoinEui",
    }

    nwk_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    join_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionKeysAbpV10x(PropertyType):
    APP_S_KEY = "AppSKey"
    NWK_S_KEY = "NwkSKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_s_key": "AppSKey",
        "nwk_s_key": "NwkSKey",
    }

    app_s_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nwk_s_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionKeysAbpV11(PropertyType):
    F_NWK_S_INT_KEY = "FNwkSIntKey"
    APP_S_KEY = "AppSKey"
    S_NWK_S_INT_KEY = "SNwkSIntKey"
    NWK_S_ENC_KEY = "NwkSEncKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "f_nwk_s_int_key": "FNwkSIntKey",
        "app_s_key": "AppSKey",
        "s_nwk_s_int_key": "SNwkSIntKey",
        "nwk_s_enc_key": "NwkSEncKey",
    }

    f_nwk_s_int_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_s_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s_nwk_s_int_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nwk_s_enc_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

