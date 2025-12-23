"""PropertyTypes for AWS::IoTWireless::DeviceProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoRaWANDeviceProfile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ping_slot_period": "PingSlotPeriod",
        "class_c_timeout": "ClassCTimeout",
        "rx_freq2": "RxFreq2",
        "rf_region": "RfRegion",
        "class_b_timeout": "ClassBTimeout",
        "rx_delay1": "RxDelay1",
        "supports_class_c": "SupportsClassC",
        "supports_class_b": "SupportsClassB",
        "rx_dr_offset1": "RxDrOffset1",
        "max_eirp": "MaxEirp",
        "factory_preset_freqs_list": "FactoryPresetFreqsList",
        "supports_join": "SupportsJoin",
        "ping_slot_dr": "PingSlotDr",
        "mac_version": "MacVersion",
        "ping_slot_freq": "PingSlotFreq",
        "reg_params_revision": "RegParamsRevision",
        "rx_data_rate2": "RxDataRate2",
        "supports32_bit_f_cnt": "Supports32BitFCnt",
        "max_duty_cycle": "MaxDutyCycle",
    }

    ping_slot_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    class_c_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rx_freq2: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rf_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    class_b_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rx_delay1: Optional[Union[int, Ref, GetAtt, Sub]] = None
    supports_class_c: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    supports_class_b: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rx_dr_offset1: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_eirp: Optional[Union[int, Ref, GetAtt, Sub]] = None
    factory_preset_freqs_list: Optional[Union[list[int], Ref]] = None
    supports_join: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ping_slot_dr: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mac_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ping_slot_freq: Optional[Union[int, Ref, GetAtt, Sub]] = None
    reg_params_revision: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rx_data_rate2: Optional[Union[int, Ref, GetAtt, Sub]] = None
    supports32_bit_f_cnt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_duty_cycle: Optional[Union[int, Ref, GetAtt, Sub]] = None

