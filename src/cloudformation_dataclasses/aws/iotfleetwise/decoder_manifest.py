"""PropertyTypes for AWS::IoTFleetWise::DecoderManifest."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CampaignStatus:
    """CampaignStatus enum values."""

    CREATING = "CREATING"
    WAITING_FOR_APPROVAL = "WAITING_FOR_APPROVAL"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"


class Compression:
    """Compression enum values."""

    OFF = "OFF"
    SNAPPY = "SNAPPY"


class DataFormat:
    """DataFormat enum values."""

    JSON = "JSON"
    PARQUET = "PARQUET"


class DefaultForUnmappedSignalsType:
    """DefaultForUnmappedSignalsType enum values."""

    CUSTOM_DECODING = "CUSTOM_DECODING"


class DiagnosticsMode:
    """DiagnosticsMode enum values."""

    OFF = "OFF"
    SEND_ACTIVE_DTCS = "SEND_ACTIVE_DTCS"


class EncryptionStatus:
    """EncryptionStatus enum values."""

    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class EncryptionType:
    """EncryptionType enum values."""

    KMS_BASED_ENCRYPTION = "KMS_BASED_ENCRYPTION"
    FLEETWISE_DEFAULT_ENCRYPTION = "FLEETWISE_DEFAULT_ENCRYPTION"


class ListResponseScope:
    """ListResponseScope enum values."""

    METADATA_ONLY = "METADATA_ONLY"


class LogType:
    """LogType enum values."""

    OFF = "OFF"
    ERROR = "ERROR"


class ManifestStatus:
    """ManifestStatus enum values."""

    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    INVALID = "INVALID"
    VALIDATING = "VALIDATING"


class NetworkInterfaceFailureReason:
    """NetworkInterfaceFailureReason enum values."""

    DUPLICATE_NETWORK_INTERFACE = "DUPLICATE_NETWORK_INTERFACE"
    CONFLICTING_NETWORK_INTERFACE = "CONFLICTING_NETWORK_INTERFACE"
    NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS = "NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS"
    CAN_NETWORK_INTERFACE_INFO_IS_NULL = "CAN_NETWORK_INTERFACE_INFO_IS_NULL"
    OBD_NETWORK_INTERFACE_INFO_IS_NULL = "OBD_NETWORK_INTERFACE_INFO_IS_NULL"
    NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS = "NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS"
    VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL = "VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL"
    CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL = "CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL"


class NetworkInterfaceType:
    """NetworkInterfaceType enum values."""

    CAN_INTERFACE = "CAN_INTERFACE"
    OBD_INTERFACE = "OBD_INTERFACE"
    VEHICLE_MIDDLEWARE = "VEHICLE_MIDDLEWARE"
    CUSTOM_DECODING_INTERFACE = "CUSTOM_DECODING_INTERFACE"


class NodeDataEncoding:
    """NodeDataEncoding enum values."""

    BINARY = "BINARY"
    TYPED = "TYPED"


class NodeDataType:
    """NodeDataType enum values."""

    INT8 = "INT8"
    UINT8 = "UINT8"
    INT16 = "INT16"
    UINT16 = "UINT16"
    INT32 = "INT32"
    UINT32 = "UINT32"
    INT64 = "INT64"
    UINT64 = "UINT64"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    UNIX_TIMESTAMP = "UNIX_TIMESTAMP"
    INT8_ARRAY = "INT8_ARRAY"
    UINT8_ARRAY = "UINT8_ARRAY"
    INT16_ARRAY = "INT16_ARRAY"
    UINT16_ARRAY = "UINT16_ARRAY"
    INT32_ARRAY = "INT32_ARRAY"
    UINT32_ARRAY = "UINT32_ARRAY"
    INT64_ARRAY = "INT64_ARRAY"
    UINT64_ARRAY = "UINT64_ARRAY"
    BOOLEAN_ARRAY = "BOOLEAN_ARRAY"
    FLOAT_ARRAY = "FLOAT_ARRAY"
    DOUBLE_ARRAY = "DOUBLE_ARRAY"
    STRING_ARRAY = "STRING_ARRAY"
    UNIX_TIMESTAMP_ARRAY = "UNIX_TIMESTAMP_ARRAY"
    UNKNOWN = "UNKNOWN"
    STRUCT = "STRUCT"
    STRUCT_ARRAY = "STRUCT_ARRAY"


class ROS2PrimitiveType:
    """ROS2PrimitiveType enum values."""

    BOOL = "BOOL"
    BYTE = "BYTE"
    CHAR = "CHAR"
    FLOAT32 = "FLOAT32"
    FLOAT64 = "FLOAT64"
    INT8 = "INT8"
    UINT8 = "UINT8"
    INT16 = "INT16"
    UINT16 = "UINT16"
    INT32 = "INT32"
    UINT32 = "UINT32"
    INT64 = "INT64"
    UINT64 = "UINT64"
    STRING = "STRING"
    WSTRING = "WSTRING"


class RegistrationStatus:
    """RegistrationStatus enum values."""

    REGISTRATION_PENDING = "REGISTRATION_PENDING"
    REGISTRATION_SUCCESS = "REGISTRATION_SUCCESS"
    REGISTRATION_FAILURE = "REGISTRATION_FAILURE"


class SignalDecoderFailureReason:
    """SignalDecoderFailureReason enum values."""

    DUPLICATE_SIGNAL = "DUPLICATE_SIGNAL"
    CONFLICTING_SIGNAL = "CONFLICTING_SIGNAL"
    SIGNAL_TO_ADD_ALREADY_EXISTS = "SIGNAL_TO_ADD_ALREADY_EXISTS"
    SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE = "SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE"
    NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE = "NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE"
    SIGNAL_NOT_IN_MODEL = "SIGNAL_NOT_IN_MODEL"
    CAN_SIGNAL_INFO_IS_NULL = "CAN_SIGNAL_INFO_IS_NULL"
    OBD_SIGNAL_INFO_IS_NULL = "OBD_SIGNAL_INFO_IS_NULL"
    NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL = "NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL"
    MESSAGE_SIGNAL_INFO_IS_NULL = "MESSAGE_SIGNAL_INFO_IS_NULL"
    SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE = "SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE"
    STRUCT_SIZE_MISMATCH = "STRUCT_SIZE_MISMATCH"
    NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL = "NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL"
    SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG = "SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG"
    EMPTY_MESSAGE_SIGNAL = "EMPTY_MESSAGE_SIGNAL"
    CUSTOM_DECODING_SIGNAL_INFO_IS_NULL = "CUSTOM_DECODING_SIGNAL_INFO_IS_NULL"


class SignalDecoderType:
    """SignalDecoderType enum values."""

    CAN_SIGNAL = "CAN_SIGNAL"
    OBD_SIGNAL = "OBD_SIGNAL"
    MESSAGE_SIGNAL = "MESSAGE_SIGNAL"
    CUSTOM_DECODING_SIGNAL = "CUSTOM_DECODING_SIGNAL"


class SignalNodeType:
    """SignalNodeType enum values."""

    SENSOR = "SENSOR"
    ACTUATOR = "ACTUATOR"
    ATTRIBUTE = "ATTRIBUTE"
    BRANCH = "BRANCH"
    CUSTOM_STRUCT = "CUSTOM_STRUCT"
    CUSTOM_PROPERTY = "CUSTOM_PROPERTY"


class SignalValueType:
    """SignalValueType enum values."""

    INTEGER = "INTEGER"
    FLOATING_POINT = "FLOATING_POINT"


class SpoolingMode:
    """SpoolingMode enum values."""

    OFF = "OFF"
    TO_DISK = "TO_DISK"


class StorageCompressionFormat:
    """StorageCompressionFormat enum values."""

    NONE = "NONE"
    GZIP = "GZIP"


class StorageMaximumSizeUnit:
    """StorageMaximumSizeUnit enum values."""

    MB = "MB"
    GB = "GB"
    TB = "TB"


class StorageMinimumTimeToLiveUnit:
    """StorageMinimumTimeToLiveUnit enum values."""

    HOURS = "HOURS"
    DAYS = "DAYS"
    WEEKS = "WEEKS"


class StructuredMessageListType:
    """StructuredMessageListType enum values."""

    FIXED_CAPACITY = "FIXED_CAPACITY"
    DYNAMIC_UNBOUNDED_CAPACITY = "DYNAMIC_UNBOUNDED_CAPACITY"
    DYNAMIC_BOUNDED_CAPACITY = "DYNAMIC_BOUNDED_CAPACITY"


class TimeUnit:
    """TimeUnit enum values."""

    MILLISECOND = "MILLISECOND"
    SECOND = "SECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"


class TriggerMode:
    """TriggerMode enum values."""

    ALWAYS = "ALWAYS"
    RISING_EDGE = "RISING_EDGE"


class UpdateCampaignAction:
    """UpdateCampaignAction enum values."""

    APPROVE = "APPROVE"
    SUSPEND = "SUSPEND"
    RESUME = "RESUME"
    UPDATE = "UPDATE"


class UpdateMode:
    """UpdateMode enum values."""

    OVERWRITE = "Overwrite"
    MERGE = "Merge"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


class VehicleAssociationBehavior:
    """VehicleAssociationBehavior enum values."""

    CREATEIOTTHING = "CreateIotThing"
    VALIDATEIOTTHINGEXISTS = "ValidateIotThingExists"


class VehicleMiddlewareProtocol:
    """VehicleMiddlewareProtocol enum values."""

    ROS_2 = "ROS_2"


class VehicleState:
    """VehicleState enum values."""

    CREATED = "CREATED"
    READY = "READY"
    HEALTHY = "HEALTHY"
    SUSPENDED = "SUSPENDED"
    DELETING = "DELETING"
    READY_FOR_CHECKIN = "READY_FOR_CHECKIN"


@dataclass
class CanInterface(PropertyType):
    PROTOCOL_NAME = "ProtocolName"
    PROTOCOL_VERSION = "ProtocolVersion"
    NAME = "Name"

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
    IS_BIG_ENDIAN = "IsBigEndian"
    LENGTH = "Length"
    FACTOR = "Factor"
    IS_SIGNED = "IsSigned"
    SIGNAL_VALUE_TYPE = "SignalValueType"
    START_BIT = "StartBit"
    MESSAGE_ID = "MessageId"
    OFFSET = "Offset"
    NAME = "Name"

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
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomDecodingSignal(PropertyType):
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterfacesItems(PropertyType):
    TYPE = "Type"
    CAN_INTERFACE = "CanInterface"
    CUSTOM_DECODING_INTERFACE = "CustomDecodingInterface"
    INTERFACE_ID = "InterfaceId"
    OBD_INTERFACE = "ObdInterface"

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
    HAS_TRANSMISSION_ECU = "HasTransmissionEcu"
    PID_REQUEST_INTERVAL_SECONDS = "PidRequestIntervalSeconds"
    USE_EXTENDED_IDS = "UseExtendedIds"
    REQUEST_MESSAGE_ID = "RequestMessageId"
    OBD_STANDARD = "ObdStandard"
    NAME = "Name"
    DTC_REQUEST_INTERVAL_SECONDS = "DtcRequestIntervalSeconds"

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
    BIT_RIGHT_SHIFT = "BitRightShift"
    BIT_MASK_LENGTH = "BitMaskLength"
    START_BYTE = "StartByte"
    BYTE_LENGTH = "ByteLength"
    PID_RESPONSE_LENGTH = "PidResponseLength"
    SCALING = "Scaling"
    PID = "Pid"
    IS_SIGNED = "IsSigned"
    SIGNAL_VALUE_TYPE = "SignalValueType"
    SERVICE_MODE = "ServiceMode"
    OFFSET = "Offset"

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
    TYPE = "Type"
    OBD_SIGNAL = "ObdSignal"
    FULLY_QUALIFIED_NAME = "FullyQualifiedName"
    CUSTOM_DECODING_SIGNAL = "CustomDecodingSignal"
    CAN_SIGNAL = "CanSignal"
    INTERFACE_ID = "InterfaceId"

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

