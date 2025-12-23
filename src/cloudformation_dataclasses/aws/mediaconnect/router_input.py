"""PropertyTypes for AWS::MediaConnect::RouterInput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

