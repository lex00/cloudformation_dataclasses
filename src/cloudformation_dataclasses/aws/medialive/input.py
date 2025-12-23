"""PropertyTypes for AWS::MediaLive::Input."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InputDestinationRequest(PropertyType):
    STREAM_NAME = "StreamName"
    NETWORK = "Network"
    NETWORK_ROUTES = "NetworkRoutes"
    STATIC_IP_ADDRESS = "StaticIpAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_name": "StreamName",
        "network": "Network",
        "network_routes": "NetworkRoutes",
        "static_ip_address": "StaticIpAddress",
    }

    stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_routes: Optional[list[InputRequestDestinationRoute]] = None
    static_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputDeviceRequest(PropertyType):
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputDeviceSettings(PropertyType):
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputRequestDestinationRoute(PropertyType):
    CIDR = "Cidr"
    GATEWAY = "Gateway"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
        "gateway": "Gateway",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    gateway: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSdpLocation(PropertyType):
    MEDIA_INDEX = "MediaIndex"
    SDP_URL = "SdpUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "media_index": "MediaIndex",
        "sdp_url": "SdpUrl",
    }

    media_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    sdp_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSourceRequest(PropertyType):
    USERNAME = "Username"
    PASSWORD_PARAM = "PasswordParam"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password_param": "PasswordParam",
        "url": "Url",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_param: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputVpcRequest(PropertyType):
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class MediaConnectFlowRequest(PropertyType):
    FLOW_ARN = "FlowArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_arn": "FlowArn",
    }

    flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastSettingsCreateRequest(PropertyType):
    SOURCES = "Sources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sources": "Sources",
    }

    sources: Optional[list[MulticastSourceCreateRequest]] = None


@dataclass
class MulticastSettingsUpdateRequest(PropertyType):
    SOURCES = "Sources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sources": "Sources",
    }

    sources: Optional[list[MulticastSourceUpdateRequest]] = None


@dataclass
class MulticastSourceCreateRequest(PropertyType):
    SOURCE_IP = "SourceIp"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_ip": "SourceIp",
        "url": "Url",
    }

    source_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastSourceUpdateRequest(PropertyType):
    SOURCE_IP = "SourceIp"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_ip": "SourceIp",
        "url": "Url",
    }

    source_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouterDestinationSettings(PropertyType):
    AVAILABILITY_ZONE_NAME = "AvailabilityZoneName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_name": "AvailabilityZoneName",
    }

    availability_zone_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouterSettings(PropertyType):
    SECRET_ARN = "SecretArn"
    ENCRYPTION_TYPE = "EncryptionType"
    DESTINATIONS = "Destinations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "encryption_type": "EncryptionType",
        "destinations": "Destinations",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_type: Optional[Union[str, RouterEncryptionType, Ref, GetAtt, Sub]] = None
    destinations: Optional[list[RouterDestinationSettings]] = None


@dataclass
class Smpte2110ReceiverGroup(PropertyType):
    SDP_SETTINGS = "SdpSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sdp_settings": "SdpSettings",
    }

    sdp_settings: Optional[Smpte2110ReceiverGroupSdpSettings] = None


@dataclass
class Smpte2110ReceiverGroupSdpSettings(PropertyType):
    AUDIO_SDPS = "AudioSdps"
    ANCILLARY_SDPS = "AncillarySdps"
    VIDEO_SDP = "VideoSdp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_sdps": "AudioSdps",
        "ancillary_sdps": "AncillarySdps",
        "video_sdp": "VideoSdp",
    }

    audio_sdps: Optional[list[InputSdpLocation]] = None
    ancillary_sdps: Optional[list[InputSdpLocation]] = None
    video_sdp: Optional[InputSdpLocation] = None


@dataclass
class Smpte2110ReceiverGroupSettings(PropertyType):
    SMPTE2110_RECEIVER_GROUPS = "Smpte2110ReceiverGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "smpte2110_receiver_groups": "Smpte2110ReceiverGroups",
    }

    smpte2110_receiver_groups: Optional[list[Smpte2110ReceiverGroup]] = None


@dataclass
class SpecialRouterSettings(PropertyType):
    ROUTER_ARN = "RouterArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "router_arn": "RouterArn",
    }

    router_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerDecryptionRequest(PropertyType):
    ALGORITHM = "Algorithm"
    PASSPHRASE_SECRET_ARN = "PassphraseSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "algorithm": "Algorithm",
        "passphrase_secret_arn": "PassphraseSecretArn",
    }

    algorithm: Optional[Union[str, Algorithm, Ref, GetAtt, Sub]] = None
    passphrase_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerSourceRequest(PropertyType):
    SRT_LISTENER_PORT = "SrtListenerPort"
    STREAM_ID = "StreamId"
    MINIMUM_LATENCY = "MinimumLatency"
    SRT_LISTENER_ADDRESS = "SrtListenerAddress"
    DECRYPTION = "Decryption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_listener_port": "SrtListenerPort",
        "stream_id": "StreamId",
        "minimum_latency": "MinimumLatency",
        "srt_listener_address": "SrtListenerAddress",
        "decryption": "Decryption",
    }

    srt_listener_port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_latency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    srt_listener_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    decryption: Optional[SrtCallerDecryptionRequest] = None


@dataclass
class SrtSettingsRequest(PropertyType):
    SRT_CALLER_SOURCES = "SrtCallerSources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_caller_sources": "SrtCallerSources",
    }

    srt_caller_sources: Optional[list[SrtCallerSourceRequest]] = None

