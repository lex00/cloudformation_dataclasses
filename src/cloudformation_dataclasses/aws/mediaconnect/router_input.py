"""PropertyTypes for AWS::MediaConnect::RouterInput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Algorithm:
    """Algorithm enum values."""

    AES128 = "aes128"
    AES192 = "aes192"
    AES256 = "aes256"


class BridgePlacement:
    """BridgePlacement enum values."""

    AVAILABLE = "AVAILABLE"
    LOCKED = "LOCKED"


class BridgeState:
    """BridgeState enum values."""

    CREATING = "CREATING"
    STANDBY = "STANDBY"
    STARTING = "STARTING"
    DEPLOYING = "DEPLOYING"
    ACTIVE = "ACTIVE"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    START_FAILED = "START_FAILED"
    START_PENDING = "START_PENDING"
    STOP_FAILED = "STOP_FAILED"
    UPDATING = "UPDATING"


class Colorimetry:
    """Colorimetry enum values."""

    BT601 = "BT601"
    BT709 = "BT709"
    BT2020 = "BT2020"
    BT2100 = "BT2100"
    ST2065_1 = "ST2065-1"
    ST2065_3 = "ST2065-3"
    XYZ = "XYZ"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"


class ContentQualityAnalysisState:
    """ContentQualityAnalysisState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Day:
    """Day enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DesiredState:
    """DesiredState enum values."""

    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    DELETED = "DELETED"


class DurationUnits:
    """DurationUnits enum values."""

    MONTHS = "MONTHS"


class EncoderProfile:
    """EncoderProfile enum values."""

    MAIN = "main"
    HIGH = "high"


class EncodingName:
    """EncodingName enum values."""

    JXSV = "jxsv"
    RAW = "raw"
    SMPTE291 = "smpte291"
    PCM = "pcm"


class EntitlementStatus:
    """EntitlementStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FailoverInputSourcePriorityMode:
    """FailoverInputSourcePriorityMode enum values."""

    NO_PRIORITY = "NO_PRIORITY"
    PRIMARY_SECONDARY = "PRIMARY_SECONDARY"


class FailoverMode:
    """FailoverMode enum values."""

    MERGE = "MERGE"
    FAILOVER = "FAILOVER"


class FlowSize:
    """FlowSize enum values."""

    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class FlowTransitEncryptionKeyType:
    """FlowTransitEncryptionKeyType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"
    AUTOMATIC = "AUTOMATIC"


class ForwardErrorCorrectionState:
    """ForwardErrorCorrectionState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GatewayState:
    """GatewayState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    ERROR = "ERROR"
    DELETING = "DELETING"
    DELETED = "DELETED"


class InstanceState:
    """InstanceState enum values."""

    REGISTERING = "REGISTERING"
    ACTIVE = "ACTIVE"
    DEREGISTERING = "DEREGISTERING"
    DEREGISTERED = "DEREGISTERED"
    REGISTRATION_ERROR = "REGISTRATION_ERROR"
    DEREGISTRATION_ERROR = "DEREGISTRATION_ERROR"


class KeyType:
    """KeyType enum values."""

    SPEKE = "speke"
    STATIC_KEY = "static-key"
    SRT_PASSWORD = "srt-password"


class MaintenanceDay:
    """MaintenanceDay enum values."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class MaintenanceScheduleType:
    """MaintenanceScheduleType enum values."""

    WINDOW = "WINDOW"


class MaintenanceType:
    """MaintenanceType enum values."""

    PREFERRED_DAY_TIME = "PREFERRED_DAY_TIME"
    DEFAULT = "DEFAULT"


class MediaLiveInputPipelineId:
    """MediaLiveInputPipelineId enum values."""

    PIPELINE_0 = "PIPELINE_0"
    PIPELINE_1 = "PIPELINE_1"


class MediaLiveTransitEncryptionKeyType:
    """MediaLiveTransitEncryptionKeyType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"
    AUTOMATIC = "AUTOMATIC"


class MediaStreamType:
    """MediaStreamType enum values."""

    VIDEO = "video"
    AUDIO = "audio"
    ANCILLARY_DATA = "ancillary-data"


class NdiState:
    """NdiState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class NetworkInterfaceType:
    """NetworkInterfaceType enum values."""

    ENA = "ena"
    EFA = "efa"


class OutputStatus:
    """OutputStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PriceUnits:
    """PriceUnits enum values."""

    HOURLY = "HOURLY"


class Protocol:
    """Protocol enum values."""

    ZIXI_PUSH = "zixi-push"
    RTP_FEC = "rtp-fec"
    RTP = "rtp"
    ZIXI_PULL = "zixi-pull"
    RIST = "rist"
    ST2110_JPEGXS = "st2110-jpegxs"
    CDI = "cdi"
    SRT_LISTENER = "srt-listener"
    SRT_CALLER = "srt-caller"
    FUJITSU_QOS = "fujitsu-qos"
    UDP = "udp"
    NDI_SPEED_HQ = "ndi-speed-hq"


class Range:
    """Range enum values."""

    NARROW = "NARROW"
    FULL = "FULL"
    FULLPROTECT = "FULLPROTECT"


class ReservationState:
    """ReservationState enum values."""

    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    PROCESSING = "PROCESSING"
    CANCELED = "CANCELED"


class ResourceType:
    """ResourceType enum values."""

    MBPS_OUTBOUND_BANDWIDTH = "Mbps_Outbound_Bandwidth"


class RouterInputProtocol:
    """RouterInputProtocol enum values."""

    RTP = "RTP"
    RIST = "RIST"
    SRT_CALLER = "SRT_CALLER"
    SRT_LISTENER = "SRT_LISTENER"


class RouterInputState:
    """RouterInputState enum values."""

    CREATING = "CREATING"
    STANDBY = "STANDBY"
    STARTING = "STARTING"
    ACTIVE = "ACTIVE"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ERROR = "ERROR"
    RECOVERING = "RECOVERING"
    MIGRATING = "MIGRATING"


class RouterInputTier:
    """RouterInputTier enum values."""

    INPUT_100 = "INPUT_100"
    INPUT_50 = "INPUT_50"
    INPUT_20 = "INPUT_20"


class RouterInputTransitEncryptionKeyType:
    """RouterInputTransitEncryptionKeyType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"
    AUTOMATIC = "AUTOMATIC"


class RouterInputType:
    """RouterInputType enum values."""

    STANDARD = "STANDARD"
    FAILOVER = "FAILOVER"
    MERGE = "MERGE"
    MEDIACONNECT_FLOW = "MEDIACONNECT_FLOW"


class RouterNetworkInterfaceState:
    """RouterNetworkInterfaceState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ERROR = "ERROR"
    RECOVERING = "RECOVERING"


class RouterNetworkInterfaceType:
    """RouterNetworkInterfaceType enum values."""

    PUBLIC = "PUBLIC"
    VPC = "VPC"


class RouterOutputProtocol:
    """RouterOutputProtocol enum values."""

    RTP = "RTP"
    RIST = "RIST"
    SRT_CALLER = "SRT_CALLER"
    SRT_LISTENER = "SRT_LISTENER"


class RouterOutputRoutedState:
    """RouterOutputRoutedState enum values."""

    ROUTED = "ROUTED"
    ROUTING = "ROUTING"
    UNROUTED = "UNROUTED"


class RouterOutputState:
    """RouterOutputState enum values."""

    CREATING = "CREATING"
    STANDBY = "STANDBY"
    STARTING = "STARTING"
    ACTIVE = "ACTIVE"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ERROR = "ERROR"
    RECOVERING = "RECOVERING"
    MIGRATING = "MIGRATING"


class RouterOutputTier:
    """RouterOutputTier enum values."""

    OUTPUT_100 = "OUTPUT_100"
    OUTPUT_50 = "OUTPUT_50"
    OUTPUT_20 = "OUTPUT_20"


class RouterOutputType:
    """RouterOutputType enum values."""

    STANDARD = "STANDARD"
    MEDIACONNECT_FLOW = "MEDIACONNECT_FLOW"
    MEDIALIVE_INPUT = "MEDIALIVE_INPUT"


class RoutingScope:
    """RoutingScope enum values."""

    REGIONAL = "REGIONAL"
    GLOBAL = "GLOBAL"


class ScanMode:
    """ScanMode enum values."""

    PROGRESSIVE = "progressive"
    INTERLACE = "interlace"
    PROGRESSIVE_SEGMENTED_FRAME = "progressive-segmented-frame"


class SourceType:
    """SourceType enum values."""

    OWNED = "OWNED"
    ENTITLED = "ENTITLED"


class State:
    """State enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Status:
    """Status enum values."""

    STANDBY = "STANDBY"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    ERROR = "ERROR"


class Tcs:
    """Tcs enum values."""

    SDR = "SDR"
    PQ = "PQ"
    HLG = "HLG"
    LINEAR = "LINEAR"
    BT2100LINPQ = "BT2100LINPQ"
    BT2100LINHLG = "BT2100LINHLG"
    ST2065_1 = "ST2065-1"
    ST428_1 = "ST428-1"
    DENSITY = "DENSITY"


class ThumbnailState:
    """ThumbnailState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclass
class FailoverRouterInputConfiguration(PropertyType):
    NETWORK_INTERFACE_ARN = "NetworkInterfaceArn"
    SOURCE_PRIORITY_MODE = "SourcePriorityMode"
    PROTOCOL_CONFIGURATIONS = "ProtocolConfigurations"
    PRIMARY_SOURCE_INDEX = "PrimarySourceIndex"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_interface_arn": "NetworkInterfaceArn",
        "source_priority_mode": "SourcePriorityMode",
        "protocol_configurations": "ProtocolConfigurations",
        "primary_source_index": "PrimarySourceIndex",
    }

    network_interface_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_priority_mode: Optional[Union[str, FailoverInputSourcePriorityMode, Ref, GetAtt, Sub]] = None
    protocol_configurations: Optional[list[FailoverRouterInputProtocolConfiguration]] = None
    primary_source_index: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FailoverRouterInputProtocolConfiguration(PropertyType):
    SRT_CALLER = "SrtCaller"
    SRT_LISTENER = "SrtListener"
    RIST = "Rist"
    RTP = "Rtp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_caller": "SrtCaller",
        "srt_listener": "SrtListener",
        "rist": "Rist",
        "rtp": "Rtp",
    }

    srt_caller: Optional[SrtCallerRouterInputConfiguration] = None
    srt_listener: Optional[SrtListenerRouterInputConfiguration] = None
    rist: Optional[RistRouterInputConfiguration] = None
    rtp: Optional[RtpRouterInputConfiguration] = None


@dataclass
class FlowTransitEncryption(PropertyType):
    ENCRYPTION_KEY_TYPE = "EncryptionKeyType"
    ENCRYPTION_KEY_CONFIGURATION = "EncryptionKeyConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_type": "EncryptionKeyType",
        "encryption_key_configuration": "EncryptionKeyConfiguration",
    }

    encryption_key_type: Optional[Union[str, FlowTransitEncryptionKeyType, Ref, GetAtt, Sub]] = None
    encryption_key_configuration: Optional[FlowTransitEncryptionKeyConfiguration] = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    SECRETS_MANAGER = "SecretsManager"
    AUTOMATIC = "Automatic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager": "SecretsManager",
        "automatic": "Automatic",
    }

    secrets_manager: Optional[SecretsManagerEncryptionKeyConfiguration] = None
    automatic: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceConfiguration(PropertyType):
    DEFAULT = "Default"
    PREFERRED_DAY_TIME = "PreferredDayTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default": "Default",
        "preferred_day_time": "PreferredDayTime",
    }

    default: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    preferred_day_time: Optional[PreferredDayTimeMaintenanceConfiguration] = None


@dataclass
class MediaConnectFlowRouterInputConfiguration(PropertyType):
    FLOW_OUTPUT_ARN = "FlowOutputArn"
    SOURCE_TRANSIT_DECRYPTION = "SourceTransitDecryption"
    FLOW_ARN = "FlowArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_output_arn": "FlowOutputArn",
        "source_transit_decryption": "SourceTransitDecryption",
        "flow_arn": "FlowArn",
    }

    flow_output_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_transit_decryption: Optional[FlowTransitEncryption] = None
    flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MergeRouterInputConfiguration(PropertyType):
    MERGE_RECOVERY_WINDOW_MILLISECONDS = "MergeRecoveryWindowMilliseconds"
    NETWORK_INTERFACE_ARN = "NetworkInterfaceArn"
    PROTOCOL_CONFIGURATIONS = "ProtocolConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "merge_recovery_window_milliseconds": "MergeRecoveryWindowMilliseconds",
        "network_interface_arn": "NetworkInterfaceArn",
        "protocol_configurations": "ProtocolConfigurations",
    }

    merge_recovery_window_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    network_interface_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol_configurations: Optional[list[MergeRouterInputProtocolConfiguration]] = None


@dataclass
class MergeRouterInputProtocolConfiguration(PropertyType):
    RIST = "Rist"
    RTP = "Rtp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rist": "Rist",
        "rtp": "Rtp",
    }

    rist: Optional[RistRouterInputConfiguration] = None
    rtp: Optional[RtpRouterInputConfiguration] = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    TIME = "Time"
    DAY = "Day"

    _property_mappings: ClassVar[dict[str, str]] = {
        "time": "Time",
        "day": "Day",
    }

    time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    day: Optional[Union[str, Day, Ref, GetAtt, Sub]] = None


@dataclass
class RistRouterInputConfiguration(PropertyType):
    PORT = "Port"
    RECOVERY_LATENCY_MILLISECONDS = "RecoveryLatencyMilliseconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "recovery_latency_milliseconds": "RecoveryLatencyMilliseconds",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    recovery_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RouterInputConfiguration(PropertyType):
    MEDIA_CONNECT_FLOW = "MediaConnectFlow"
    FAILOVER = "Failover"
    MERGE = "Merge"
    STANDARD = "Standard"

    _property_mappings: ClassVar[dict[str, str]] = {
        "media_connect_flow": "MediaConnectFlow",
        "failover": "Failover",
        "merge": "Merge",
        "standard": "Standard",
    }

    media_connect_flow: Optional[MediaConnectFlowRouterInputConfiguration] = None
    failover: Optional[FailoverRouterInputConfiguration] = None
    merge: Optional[MergeRouterInputConfiguration] = None
    standard: Optional[StandardRouterInputConfiguration] = None


@dataclass
class RouterInputProtocolConfiguration(PropertyType):
    SRT_CALLER = "SrtCaller"
    SRT_LISTENER = "SrtListener"
    RIST = "Rist"
    RTP = "Rtp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_caller": "SrtCaller",
        "srt_listener": "SrtListener",
        "rist": "Rist",
        "rtp": "Rtp",
    }

    srt_caller: Optional[SrtCallerRouterInputConfiguration] = None
    srt_listener: Optional[SrtListenerRouterInputConfiguration] = None
    rist: Optional[RistRouterInputConfiguration] = None
    rtp: Optional[RtpRouterInputConfiguration] = None


@dataclass
class RouterInputTransitEncryption(PropertyType):
    ENCRYPTION_KEY_TYPE = "EncryptionKeyType"
    ENCRYPTION_KEY_CONFIGURATION = "EncryptionKeyConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_type": "EncryptionKeyType",
        "encryption_key_configuration": "EncryptionKeyConfiguration",
    }

    encryption_key_type: Optional[Union[str, RouterInputTransitEncryptionKeyType, Ref, GetAtt, Sub]] = None
    encryption_key_configuration: Optional[RouterInputTransitEncryptionKeyConfiguration] = None


@dataclass
class RouterInputTransitEncryptionKeyConfiguration(PropertyType):
    SECRETS_MANAGER = "SecretsManager"
    AUTOMATIC = "Automatic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager": "SecretsManager",
        "automatic": "Automatic",
    }

    secrets_manager: Optional[SecretsManagerEncryptionKeyConfiguration] = None
    automatic: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class RtpRouterInputConfiguration(PropertyType):
    FORWARD_ERROR_CORRECTION = "ForwardErrorCorrection"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "forward_error_correction": "ForwardErrorCorrection",
        "port": "Port",
    }

    forward_error_correction: Optional[Union[str, ForwardErrorCorrectionState, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    SECRET_ARN = "SecretArn"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerRouterInputConfiguration(PropertyType):
    SOURCE_ADDRESS = "SourceAddress"
    STREAM_ID = "StreamId"
    DECRYPTION_CONFIGURATION = "DecryptionConfiguration"
    SOURCE_PORT = "SourcePort"
    MINIMUM_LATENCY_MILLISECONDS = "MinimumLatencyMilliseconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_address": "SourceAddress",
        "stream_id": "StreamId",
        "decryption_configuration": "DecryptionConfiguration",
        "source_port": "SourcePort",
        "minimum_latency_milliseconds": "MinimumLatencyMilliseconds",
    }

    source_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    decryption_configuration: Optional[SrtDecryptionConfiguration] = None
    source_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SrtDecryptionConfiguration(PropertyType):
    ENCRYPTION_KEY = "EncryptionKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key": "EncryptionKey",
    }

    encryption_key: Optional[SecretsManagerEncryptionKeyConfiguration] = None


@dataclass
class SrtListenerRouterInputConfiguration(PropertyType):
    PORT = "Port"
    DECRYPTION_CONFIGURATION = "DecryptionConfiguration"
    MINIMUM_LATENCY_MILLISECONDS = "MinimumLatencyMilliseconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "decryption_configuration": "DecryptionConfiguration",
        "minimum_latency_milliseconds": "MinimumLatencyMilliseconds",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    decryption_configuration: Optional[SrtDecryptionConfiguration] = None
    minimum_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StandardRouterInputConfiguration(PropertyType):
    PROTOCOL_CONFIGURATION = "ProtocolConfiguration"
    NETWORK_INTERFACE_ARN = "NetworkInterfaceArn"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol_configuration": "ProtocolConfiguration",
        "network_interface_arn": "NetworkInterfaceArn",
        "protocol": "Protocol",
    }

    protocol_configuration: Optional[RouterInputProtocolConfiguration] = None
    network_interface_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, RouterInputProtocol, Ref, GetAtt, Sub]] = None

