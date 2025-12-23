"""PropertyTypes for AWS::IoTFleetWise::DecoderManifest."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CanInterface(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol_name": "ProtocolName",
        "protocol_version": "ProtocolVersion",
        "name": "Name",
    }

    protocol_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CanSignal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_big_endian": "IsBigEndian",
        "length": "Length",
        "factor": "Factor",
        "is_signed": "IsSigned",
        "signal_value_type": "SignalValueType",
        "start_bit": "StartBit",
        "message_id": "MessageId",
        "offset": "Offset",
        "name": "Name",
    }

    is_big_endian: Optional[Union[str, Ref, GetAtt, Sub]] = None
    length: Optional[Union[str, Ref, GetAtt, Sub]] = None
    factor: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_signed: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signal_value_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_bit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomDecodingInterface(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomDecodingSignal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterfacesItems(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "can_interface": "CanInterface",
        "custom_decoding_interface": "CustomDecodingInterface",
        "interface_id": "InterfaceId",
        "obd_interface": "ObdInterface",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    can_interface: Optional[CanInterface] = None
    custom_decoding_interface: Optional[CustomDecodingInterface] = None
    interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    obd_interface: Optional[ObdInterface] = None


@dataclass
class ObdInterface(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "has_transmission_ecu": "HasTransmissionEcu",
        "pid_request_interval_seconds": "PidRequestIntervalSeconds",
        "use_extended_ids": "UseExtendedIds",
        "request_message_id": "RequestMessageId",
        "obd_standard": "ObdStandard",
        "name": "Name",
        "dtc_request_interval_seconds": "DtcRequestIntervalSeconds",
    }

    has_transmission_ecu: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pid_request_interval_seconds: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_extended_ids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    request_message_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    obd_standard: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dtc_request_interval_seconds: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObdSignal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bit_right_shift": "BitRightShift",
        "bit_mask_length": "BitMaskLength",
        "start_byte": "StartByte",
        "byte_length": "ByteLength",
        "pid_response_length": "PidResponseLength",
        "scaling": "Scaling",
        "pid": "Pid",
        "is_signed": "IsSigned",
        "signal_value_type": "SignalValueType",
        "service_mode": "ServiceMode",
        "offset": "Offset",
    }

    bit_right_shift: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bit_mask_length: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_byte: Optional[Union[str, Ref, GetAtt, Sub]] = None
    byte_length: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pid_response_length: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scaling: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_signed: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signal_value_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SignalDecodersItems(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "obd_signal": "ObdSignal",
        "fully_qualified_name": "FullyQualifiedName",
        "custom_decoding_signal": "CustomDecodingSignal",
        "can_signal": "CanSignal",
        "interface_id": "InterfaceId",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    obd_signal: Optional[ObdSignal] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_decoding_signal: Optional[CustomDecodingSignal] = None
    can_signal: Optional[CanSignal] = None
    interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

