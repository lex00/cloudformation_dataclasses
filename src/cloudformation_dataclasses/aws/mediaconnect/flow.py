"""PropertyTypes for AWS::MediaConnect::Flow."""

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
class AudioMonitoringSetting(PropertyType):
    SILENT_AUDIO = "SilentAudio"

    _property_mappings: ClassVar[dict[str, str]] = {
        "silent_audio": "SilentAudio",
    }

    silent_audio: Optional[SilentAudio] = None


@dataclass
class BlackFrames(PropertyType):
    STATE = "State"
    THRESHOLD_SECONDS = "ThresholdSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "threshold_seconds": "ThresholdSeconds",
    }

    state: Optional[Union[str, State, Ref, GetAtt, Sub]] = None
    threshold_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Encryption(PropertyType):
    SECRET_ARN = "SecretArn"
    KEY_TYPE = "KeyType"
    RESOURCE_ID = "ResourceId"
    DEVICE_ID = "DeviceId"
    REGION = "Region"
    CONSTANT_INITIALIZATION_VECTOR = "ConstantInitializationVector"
    ALGORITHM = "Algorithm"
    ROLE_ARN = "RoleArn"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "key_type": "KeyType",
        "resource_id": "ResourceId",
        "device_id": "DeviceId",
        "region": "Region",
        "constant_initialization_vector": "ConstantInitializationVector",
        "algorithm": "Algorithm",
        "role_arn": "RoleArn",
        "url": "Url",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    algorithm: Optional[Union[str, Algorithm, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FailoverConfig(PropertyType):
    STATE = "State"
    SOURCE_PRIORITY = "SourcePriority"
    FAILOVER_MODE = "FailoverMode"
    RECOVERY_WINDOW = "RecoveryWindow"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "source_priority": "SourcePriority",
        "failover_mode": "FailoverMode",
        "recovery_window": "RecoveryWindow",
    }

    state: Optional[Union[str, State, Ref, GetAtt, Sub]] = None
    source_priority: Optional[SourcePriority] = None
    failover_mode: Optional[Union[str, FailoverMode, Ref, GetAtt, Sub]] = None
    recovery_window: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
class Fmtp(PropertyType):
    PAR = "Par"
    SCAN_MODE = "ScanMode"
    TCS = "Tcs"
    EXACT_FRAMERATE = "ExactFramerate"
    CHANNEL_ORDER = "ChannelOrder"
    COLORIMETRY = "Colorimetry"
    RANGE = "Range"

    _property_mappings: ClassVar[dict[str, str]] = {
        "par": "Par",
        "scan_mode": "ScanMode",
        "tcs": "Tcs",
        "exact_framerate": "ExactFramerate",
        "channel_order": "ChannelOrder",
        "colorimetry": "Colorimetry",
        "range": "Range",
    }

    par: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scan_mode: Optional[Union[str, ScanMode, Ref, GetAtt, Sub]] = None
    tcs: Optional[Union[str, Tcs, Ref, GetAtt, Sub]] = None
    exact_framerate: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_order: Optional[Union[str, Ref, GetAtt, Sub]] = None
    colorimetry: Optional[Union[str, Colorimetry, Ref, GetAtt, Sub]] = None
    range: Optional[Union[str, Range, Ref, GetAtt, Sub]] = None


@dataclass
class FrozenFrames(PropertyType):
    STATE = "State"
    THRESHOLD_SECONDS = "ThresholdSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "threshold_seconds": "ThresholdSeconds",
    }

    state: Optional[Union[str, State, Ref, GetAtt, Sub]] = None
    threshold_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class GatewayBridgeSource(PropertyType):
    BRIDGE_ARN = "BridgeArn"
    VPC_INTERFACE_ATTACHMENT = "VpcInterfaceAttachment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bridge_arn": "BridgeArn",
        "vpc_interface_attachment": "VpcInterfaceAttachment",
    }

    bridge_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_interface_attachment: Optional[VpcInterfaceAttachment] = None


@dataclass
class InputConfiguration(PropertyType):
    INPUT_PORT = "InputPort"
    INTERFACE = "Interface"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_port": "InputPort",
        "interface": "Interface",
    }

    input_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interface: Optional[Interface] = None


@dataclass
class Interface(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Maintenance(PropertyType):
    MAINTENANCE_DAY = "MaintenanceDay"
    MAINTENANCE_START_HOUR = "MaintenanceStartHour"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maintenance_day": "MaintenanceDay",
        "maintenance_start_hour": "MaintenanceStartHour",
    }

    maintenance_day: Optional[Union[str, MaintenanceDay, Ref, GetAtt, Sub]] = None
    maintenance_start_hour: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaStream(PropertyType):
    MEDIA_STREAM_TYPE = "MediaStreamType"
    MEDIA_STREAM_ID = "MediaStreamId"
    DESCRIPTION = "Description"
    MEDIA_STREAM_NAME = "MediaStreamName"
    ATTRIBUTES = "Attributes"
    CLOCK_RATE = "ClockRate"
    VIDEO_FORMAT = "VideoFormat"
    FMT = "Fmt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "media_stream_type": "MediaStreamType",
        "media_stream_id": "MediaStreamId",
        "description": "Description",
        "media_stream_name": "MediaStreamName",
        "attributes": "Attributes",
        "clock_rate": "ClockRate",
        "video_format": "VideoFormat",
        "fmt": "Fmt",
    }

    media_stream_type: Optional[Union[str, MediaStreamType, Ref, GetAtt, Sub]] = None
    media_stream_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    media_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[MediaStreamAttributes] = None
    clock_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    video_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fmt: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MediaStreamAttributes(PropertyType):
    FMTP = "Fmtp"
    LANG = "Lang"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fmtp": "Fmtp",
        "lang": "Lang",
    }

    fmtp: Optional[Fmtp] = None
    lang: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaStreamSourceConfiguration(PropertyType):
    MEDIA_STREAM_NAME = "MediaStreamName"
    INPUT_CONFIGURATIONS = "InputConfigurations"
    ENCODING_NAME = "EncodingName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "media_stream_name": "MediaStreamName",
        "input_configurations": "InputConfigurations",
        "encoding_name": "EncodingName",
    }

    media_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_configurations: Optional[list[InputConfiguration]] = None
    encoding_name: Optional[Union[str, EncodingName, Ref, GetAtt, Sub]] = None


@dataclass
class NdiConfig(PropertyType):
    NDI_STATE = "NdiState"
    MACHINE_NAME = "MachineName"
    NDI_DISCOVERY_SERVERS = "NdiDiscoveryServers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ndi_state": "NdiState",
        "machine_name": "MachineName",
        "ndi_discovery_servers": "NdiDiscoveryServers",
    }

    ndi_state: Optional[Union[str, NdiState, Ref, GetAtt, Sub]] = None
    machine_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ndi_discovery_servers: Optional[list[NdiDiscoveryServerConfig]] = None


@dataclass
class NdiDiscoveryServerConfig(PropertyType):
    DISCOVERY_SERVER_ADDRESS = "DiscoveryServerAddress"
    DISCOVERY_SERVER_PORT = "DiscoveryServerPort"
    VPC_INTERFACE_ADAPTER = "VpcInterfaceAdapter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "discovery_server_address": "DiscoveryServerAddress",
        "discovery_server_port": "DiscoveryServerPort",
        "vpc_interface_adapter": "VpcInterfaceAdapter",
    }

    discovery_server_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    discovery_server_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    vpc_interface_adapter: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class SilentAudio(PropertyType):
    STATE = "State"
    THRESHOLD_SECONDS = "ThresholdSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "threshold_seconds": "ThresholdSeconds",
    }

    state: Optional[Union[str, State, Ref, GetAtt, Sub]] = None
    threshold_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    INGEST_IP = "IngestIp"
    MAX_SYNC_BUFFER = "MaxSyncBuffer"
    STREAM_ID = "StreamId"
    DESCRIPTION = "Description"
    SENDER_IP_ADDRESS = "SenderIpAddress"
    ROUTER_INTEGRATION_TRANSIT_DECRYPTION = "RouterIntegrationTransitDecryption"
    MEDIA_STREAM_SOURCE_CONFIGURATIONS = "MediaStreamSourceConfigurations"
    INGEST_PORT = "IngestPort"
    SENDER_CONTROL_PORT = "SenderControlPort"
    DECRYPTION = "Decryption"
    ROUTER_INTEGRATION_STATE = "RouterIntegrationState"
    GATEWAY_BRIDGE_SOURCE = "GatewayBridgeSource"
    SOURCE_LISTENER_ADDRESS = "SourceListenerAddress"
    SOURCE_LISTENER_PORT = "SourceListenerPort"
    NAME = "Name"
    WHITELIST_CIDR = "WhitelistCidr"
    ENTITLEMENT_ARN = "EntitlementArn"
    SOURCE_ARN = "SourceArn"
    MIN_LATENCY = "MinLatency"
    VPC_INTERFACE_NAME = "VpcInterfaceName"
    MAX_BITRATE = "MaxBitrate"
    PROTOCOL = "Protocol"
    MAX_LATENCY = "MaxLatency"
    SOURCE_INGEST_PORT = "SourceIngestPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ingest_ip": "IngestIp",
        "max_sync_buffer": "MaxSyncBuffer",
        "stream_id": "StreamId",
        "description": "Description",
        "sender_ip_address": "SenderIpAddress",
        "router_integration_transit_decryption": "RouterIntegrationTransitDecryption",
        "media_stream_source_configurations": "MediaStreamSourceConfigurations",
        "ingest_port": "IngestPort",
        "sender_control_port": "SenderControlPort",
        "decryption": "Decryption",
        "router_integration_state": "RouterIntegrationState",
        "gateway_bridge_source": "GatewayBridgeSource",
        "source_listener_address": "SourceListenerAddress",
        "source_listener_port": "SourceListenerPort",
        "name": "Name",
        "whitelist_cidr": "WhitelistCidr",
        "entitlement_arn": "EntitlementArn",
        "source_arn": "SourceArn",
        "min_latency": "MinLatency",
        "vpc_interface_name": "VpcInterfaceName",
        "max_bitrate": "MaxBitrate",
        "protocol": "Protocol",
        "max_latency": "MaxLatency",
        "source_ingest_port": "SourceIngestPort",
    }

    ingest_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_sync_buffer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stream_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sender_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    router_integration_transit_decryption: Optional[FlowTransitEncryption] = None
    media_stream_source_configurations: Optional[list[MediaStreamSourceConfiguration]] = None
    ingest_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    sender_control_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    decryption: Optional[Encryption] = None
    router_integration_state: Optional[Union[str, State, Ref, GetAtt, Sub]] = None
    gateway_bridge_source: Optional[GatewayBridgeSource] = None
    source_listener_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_listener_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    whitelist_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    entitlement_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_latency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    vpc_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_latency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source_ingest_port: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceMonitoringConfig(PropertyType):
    CONTENT_QUALITY_ANALYSIS_STATE = "ContentQualityAnalysisState"
    AUDIO_MONITORING_SETTINGS = "AudioMonitoringSettings"
    VIDEO_MONITORING_SETTINGS = "VideoMonitoringSettings"
    THUMBNAIL_STATE = "ThumbnailState"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_quality_analysis_state": "ContentQualityAnalysisState",
        "audio_monitoring_settings": "AudioMonitoringSettings",
        "video_monitoring_settings": "VideoMonitoringSettings",
        "thumbnail_state": "ThumbnailState",
    }

    content_quality_analysis_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_monitoring_settings: Optional[list[AudioMonitoringSetting]] = None
    video_monitoring_settings: Optional[list[VideoMonitoringSetting]] = None
    thumbnail_state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourcePriority(PropertyType):
    PRIMARY_SOURCE = "PrimarySource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_source": "PrimarySource",
    }

    primary_source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VideoMonitoringSetting(PropertyType):
    BLACK_FRAMES = "BlackFrames"
    FROZEN_FRAMES = "FrozenFrames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "black_frames": "BlackFrames",
        "frozen_frames": "FrozenFrames",
    }

    black_frames: Optional[BlackFrames] = None
    frozen_frames: Optional[FrozenFrames] = None


@dataclass
class VpcInterface(PropertyType):
    NETWORK_INTERFACE_TYPE = "NetworkInterfaceType"
    NETWORK_INTERFACE_IDS = "NetworkInterfaceIds"
    SUBNET_ID = "SubnetId"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    ROLE_ARN = "RoleArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_interface_type": "NetworkInterfaceType",
        "network_interface_ids": "NetworkInterfaceIds",
        "subnet_id": "SubnetId",
        "security_group_ids": "SecurityGroupIds",
        "role_arn": "RoleArn",
        "name": "Name",
    }

    network_interface_type: Optional[Union[str, NetworkInterfaceType, Ref, GetAtt, Sub]] = None
    network_interface_ids: Optional[Union[list[str], Ref]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    VPC_INTERFACE_NAME = "VpcInterfaceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_interface_name": "VpcInterfaceName",
    }

    vpc_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

