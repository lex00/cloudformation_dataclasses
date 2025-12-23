"""PropertyTypes for AWS::MediaConnect::Flow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

