"""PropertyTypes for AWS::MediaConnect::RouterInput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FailoverRouterInputConfiguration(PropertyType):
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
class MediaConnectFlowRouterInputConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "rist": "Rist",
        "rtp": "Rtp",
    }

    rist: Optional[RistRouterInputConfiguration] = None
    rtp: Optional[RtpRouterInputConfiguration] = None


@dataclass
class PreferredDayTimeMaintenanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time": "Time",
        "day": "Day",
    }

    time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    day: Optional[Union[str, Day, Ref, GetAtt, Sub]] = None


@dataclass
class RistRouterInputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "recovery_latency_milliseconds": "RecoveryLatencyMilliseconds",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    recovery_latency_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RouterInputConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_type": "EncryptionKeyType",
        "encryption_key_configuration": "EncryptionKeyConfiguration",
    }

    encryption_key_type: Optional[Union[str, RouterInputTransitEncryptionKeyType, Ref, GetAtt, Sub]] = None
    encryption_key_configuration: Optional[RouterInputTransitEncryptionKeyConfiguration] = None


@dataclass
class RouterInputTransitEncryptionKeyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager": "SecretsManager",
        "automatic": "Automatic",
    }

    secrets_manager: Optional[SecretsManagerEncryptionKeyConfiguration] = None
    automatic: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class RtpRouterInputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forward_error_correction": "ForwardErrorCorrection",
        "port": "Port",
    }

    forward_error_correction: Optional[Union[str, ForwardErrorCorrectionState, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtCallerRouterInputConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key": "EncryptionKey",
    }

    encryption_key: Optional[SecretsManagerEncryptionKeyConfiguration] = None


@dataclass
class SrtListenerRouterInputConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol_configuration": "ProtocolConfiguration",
        "network_interface_arn": "NetworkInterfaceArn",
        "protocol": "Protocol",
    }

    protocol_configuration: Optional[RouterInputProtocolConfiguration] = None
    network_interface_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, RouterInputProtocol, Ref, GetAtt, Sub]] = None

