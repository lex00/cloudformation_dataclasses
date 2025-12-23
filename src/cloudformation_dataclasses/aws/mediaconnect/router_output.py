"""PropertyTypes for AWS::MediaConnect::RouterOutput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FlowTransitEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_type": "EncryptionKeyType",
        "encryption_key_configuration": "EncryptionKeyConfiguration",
    }

    encryption_key_type: Optional[Union[str, FlowTransitEncryptionKeyType, Ref, GetAtt, Sub]] = None
    encryption_key_configuration: Optional[FlowTransitEncryptionKeyConfiguration] = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager": "SecretsManager",
        "automatic": "Automatic",
    }

    secrets_manager: Optional[SecretsManagerEncryptionKeyConfiguration] = None
    automatic: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default": "Default",
        "preferred_day_time": "PreferredDayTime",
    }

    default: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    preferred_day_time: Optional[PreferredDayTimeMaintenanceConfiguration] = None


@dataclass
class MediaConnectFlowRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_source_arn": "FlowSourceArn",
        "flow_arn": "FlowArn",
        "destination_transit_encryption": "DestinationTransitEncryption",
    }

    flow_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_transit_encryption: Optional[FlowTransitEncryption] = None


@dataclass
class MediaLiveInputRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "media_live_input_arn": "MediaLiveInputArn",
        "media_live_pipeline_id": "MediaLivePipelineId",
        "destination_transit_encryption": "DestinationTransitEncryption",
    }

    media_live_input_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    media_live_pipeline_id: Optional[Union[str, MediaLiveInputPipelineId, Ref, GetAtt, Sub]] = None
    destination_transit_encryption: Optional[MediaLiveTransitEncryption] = None


@dataclass
class MediaLiveTransitEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_type": "EncryptionKeyType",
        "encryption_key_configuration": "EncryptionKeyConfiguration",
    }

    encryption_key_type: Optional[Union[str, MediaLiveTransitEncryptionKeyType, Ref, GetAtt, Sub]] = None
    encryption_key_configuration: Optional[MediaLiveTransitEncryptionKeyConfiguration] = None


@dataclass
class MediaLiveTransitEncryptionKeyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager": "SecretsManager",
        "automatic": "Automatic",
    }

    secrets_manager: Optional[SecretsManagerEncryptionKeyConfiguration] = None
    automatic: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time": "Time",
        "day": "Day",
    }

    time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    day: Optional[Union[str, Day, Ref, GetAtt, Sub]] = None


@dataclass
class RistRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_port": "DestinationPort",
        "destination_address": "DestinationAddress",
    }

    destination_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "media_live_input": "MediaLiveInput",
        "media_connect_flow": "MediaConnectFlow",
        "standard": "Standard",
    }

    media_live_input: Optional[MediaLiveInputRouterOutputConfiguration] = None
    media_connect_flow: Optional[MediaConnectFlowRouterOutputConfiguration] = None
    standard: Optional[StandardRouterOutputConfiguration] = None


@dataclass
class RouterOutputProtocolConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_caller": "SrtCaller",
        "srt_listener": "SrtListener",
        "rist": "Rist",
        "rtp": "Rtp",
    }

    srt_caller: Optional[SrtCallerRouterOutputConfiguration] = None
    srt_listener: Optional[SrtListenerRouterOutputConfiguration] = None
    rist: Optional[RistRouterOutputConfiguration] = None
    rtp: Optional[RtpRouterOutputConfiguration] = None


@dataclass
class RtpRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forward_error_correction": "ForwardErrorCorrection",
        "destination_port": "DestinationPort",
        "destination_address": "DestinationAddress",
    }

    forward_error_correction: Optional[Union[str, ForwardErrorCorrectionState, Ref, GetAtt, Sub]] = None
    destination_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_id": "StreamId",
        "encryption_configuration": "EncryptionConfiguration",
        "destination_port": "DestinationPort",
        "minimum_latency_milliseconds": "MinimumLatencyMilliseconds",
        "destination_address": "DestinationAddress",
    }

    stream_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[SrtEncryptionConfiguration] = None
    destination_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtEncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key": "EncryptionKey",
    }

    encryption_key: Optional[SecretsManagerEncryptionKeyConfiguration] = None


@dataclass
class SrtListenerRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_configuration": "EncryptionConfiguration",
        "port": "Port",
        "minimum_latency_milliseconds": "MinimumLatencyMilliseconds",
    }

    encryption_configuration: Optional[SrtEncryptionConfiguration] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StandardRouterOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol_configuration": "ProtocolConfiguration",
        "network_interface_arn": "NetworkInterfaceArn",
        "protocol": "Protocol",
    }

    protocol_configuration: Optional[RouterOutputProtocolConfiguration] = None
    network_interface_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, RouterOutputProtocol, Ref, GetAtt, Sub]] = None

