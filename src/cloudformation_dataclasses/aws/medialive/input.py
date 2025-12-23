"""PropertyTypes for AWS::MediaLive::Input."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InputDestinationRequest(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputDeviceSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputRequestDestinationRoute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
        "gateway": "Gateway",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    gateway: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSdpLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "media_index": "MediaIndex",
        "sdp_url": "SdpUrl",
    }

    media_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    sdp_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSourceRequest(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class MediaConnectFlowRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_arn": "FlowArn",
    }

    flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastSettingsCreateRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sources": "Sources",
    }

    sources: Optional[list[MulticastSourceCreateRequest]] = None


@dataclass
class MulticastSettingsUpdateRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sources": "Sources",
    }

    sources: Optional[list[MulticastSourceUpdateRequest]] = None


@dataclass
class MulticastSourceCreateRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_ip": "SourceIp",
        "url": "Url",
    }

    source_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastSourceUpdateRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_ip": "SourceIp",
        "url": "Url",
    }

    source_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouterDestinationSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone_name": "AvailabilityZoneName",
    }

    availability_zone_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouterSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "sdp_settings": "SdpSettings",
    }

    sdp_settings: Optional[Smpte2110ReceiverGroupSdpSettings] = None


@dataclass
class Smpte2110ReceiverGroupSdpSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "smpte2110_receiver_groups": "Smpte2110ReceiverGroups",
    }

    smpte2110_receiver_groups: Optional[list[Smpte2110ReceiverGroup]] = None


@dataclass
class SpecialRouterSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "router_arn": "RouterArn",
    }

    router_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerDecryptionRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "algorithm": "Algorithm",
        "passphrase_secret_arn": "PassphraseSecretArn",
    }

    algorithm: Optional[Union[str, Algorithm, Ref, GetAtt, Sub]] = None
    passphrase_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerSourceRequest(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_caller_sources": "SrtCallerSources",
    }

    srt_caller_sources: Optional[list[SrtCallerSourceRequest]] = None

