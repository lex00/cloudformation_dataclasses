"""PropertyTypes for AWS::MediaLive::Multiplexprogram."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MultiplexProgramPacketIdentifiersMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "etv_platform_pid": "EtvPlatformPid",
        "dvb_teletext_pid": "DvbTeletextPid",
        "klv_data_pids": "KlvDataPids",
        "pcr_pid": "PcrPid",
        "video_pid": "VideoPid",
        "pmt_pid": "PmtPid",
        "scte27_pids": "Scte27Pids",
        "dvb_sub_pids": "DvbSubPids",
        "scte35_pid": "Scte35Pid",
        "etv_signal_pid": "EtvSignalPid",
        "private_metadata_pid": "PrivateMetadataPid",
        "timed_metadata_pid": "TimedMetadataPid",
        "audio_pids": "AudioPids",
    }

    etv_platform_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dvb_teletext_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    klv_data_pids: Optional[Union[list[int], Ref]] = None
    pcr_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    video_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    pmt_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scte27_pids: Optional[Union[list[int], Ref]] = None
    dvb_sub_pids: Optional[Union[list[int], Ref]] = None
    scte35_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    etv_signal_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    private_metadata_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timed_metadata_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    audio_pids: Optional[Union[list[int], Ref]] = None


@dataclass
class MultiplexProgramPipelineDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "active_channel_pipeline": "ActiveChannelPipeline",
        "pipeline_id": "PipelineId",
    }

    active_channel_pipeline: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pipeline_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexProgramServiceDescriptor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provider_name": "ProviderName",
        "service_name": "ServiceName",
    }

    provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexProgramSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "preferred_channel_pipeline": "PreferredChannelPipeline",
        "service_descriptor": "ServiceDescriptor",
        "video_settings": "VideoSettings",
        "program_number": "ProgramNumber",
    }

    preferred_channel_pipeline: Optional[Union[str, PreferredChannelPipeline, Ref, GetAtt, Sub]] = None
    service_descriptor: Optional[MultiplexProgramServiceDescriptor] = None
    video_settings: Optional[MultiplexVideoSettings] = None
    program_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexStatmuxVideoSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "maximum_bitrate": "MaximumBitrate",
        "minimum_bitrate": "MinimumBitrate",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexVideoSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "statmux_settings": "StatmuxSettings",
        "constant_bitrate": "ConstantBitrate",
    }

    statmux_settings: Optional[MultiplexStatmuxVideoSettings] = None
    constant_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None

