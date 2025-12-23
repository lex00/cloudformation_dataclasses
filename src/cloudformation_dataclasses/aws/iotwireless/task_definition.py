"""PropertyTypes for AWS::IoTWireless::TaskDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoRaWANGatewayVersion(PropertyType):
    STATION = "Station"
    MODEL = "Model"
    PACKAGE_VERSION = "PackageVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "station": "Station",
        "model": "Model",
        "package_version": "PackageVersion",
    }

    station: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    package_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoRaWANUpdateGatewayTaskCreate(PropertyType):
    UPDATE_SIGNATURE = "UpdateSignature"
    SIG_KEY_CRC = "SigKeyCrc"
    UPDATE_VERSION = "UpdateVersion"
    CURRENT_VERSION = "CurrentVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "update_signature": "UpdateSignature",
        "sig_key_crc": "SigKeyCrc",
        "update_version": "UpdateVersion",
        "current_version": "CurrentVersion",
    }

    update_signature: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sig_key_crc: Optional[Union[int, Ref, GetAtt, Sub]] = None
    update_version: Optional[LoRaWANGatewayVersion] = None
    current_version: Optional[LoRaWANGatewayVersion] = None


@dataclass
class LoRaWANUpdateGatewayTaskEntry(PropertyType):
    UPDATE_VERSION = "UpdateVersion"
    CURRENT_VERSION = "CurrentVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "update_version": "UpdateVersion",
        "current_version": "CurrentVersion",
    }

    update_version: Optional[LoRaWANGatewayVersion] = None
    current_version: Optional[LoRaWANGatewayVersion] = None


@dataclass
class UpdateWirelessGatewayTaskCreate(PropertyType):
    LO_RA_WAN = "LoRaWAN"
    UPDATE_DATA_SOURCE = "UpdateDataSource"
    UPDATE_DATA_ROLE = "UpdateDataRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lo_ra_wan": "LoRaWAN",
        "update_data_source": "UpdateDataSource",
        "update_data_role": "UpdateDataRole",
    }

    lo_ra_wan: Optional[LoRaWANUpdateGatewayTaskCreate] = None
    update_data_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    update_data_role: Optional[Union[str, Ref, GetAtt, Sub]] = None

