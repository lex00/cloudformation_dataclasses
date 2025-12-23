"""PropertyTypes for AWS::MediaPackage::PackagingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CmafEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "speke_key_provider": "SpekeKeyProvider",
    }

    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class CmafPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
        "hls_manifests": "HlsManifests",
        "include_encoder_configuration_in_segments": "IncludeEncoderConfigurationInSegments",
    }

    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[CmafEncryption] = None
    hls_manifests: Optional[list[HlsManifest]] = None
    include_encoder_configuration_in_segments: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DashEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "speke_key_provider": "SpekeKeyProvider",
    }

    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class DashManifest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scte_markers_source": "ScteMarkersSource",
        "manifest_name": "ManifestName",
        "manifest_layout": "ManifestLayout",
        "stream_selection": "StreamSelection",
        "min_buffer_time_seconds": "MinBufferTimeSeconds",
        "profile": "Profile",
    }

    scte_markers_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_layout: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None
    min_buffer_time_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    profile: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DashPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "period_triggers": "PeriodTriggers",
        "include_iframe_only_stream": "IncludeIframeOnlyStream",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
        "segment_template_format": "SegmentTemplateFormat",
        "include_encoder_configuration_in_segments": "IncludeEncoderConfigurationInSegments",
        "dash_manifests": "DashManifests",
    }

    period_triggers: Optional[Union[list[str], Ref]] = None
    include_iframe_only_stream: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[DashEncryption] = None
    segment_template_format: Optional[Union[str, SegmentTemplateFormat, Ref, GetAtt, Sub]] = None
    include_encoder_configuration_in_segments: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dash_manifests: Optional[list[DashManifest]] = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "preset_speke20_audio": "PresetSpeke20Audio",
        "preset_speke20_video": "PresetSpeke20Video",
    }

    preset_speke20_audio: Optional[Union[str, PresetSpeke20Audio, Ref, GetAtt, Sub]] = None
    preset_speke20_video: Optional[Union[str, PresetSpeke20Video, Ref, GetAtt, Sub]] = None


@dataclass
class HlsEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constant_initialization_vector": "ConstantInitializationVector",
        "speke_key_provider": "SpekeKeyProvider",
        "encryption_method": "EncryptionMethod",
    }

    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    speke_key_provider: Optional[SpekeKeyProvider] = None
    encryption_method: Optional[Union[str, EncryptionMethod, Ref, GetAtt, Sub]] = None


@dataclass
class HlsManifest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_markers": "AdMarkers",
        "manifest_name": "ManifestName",
        "program_date_time_interval_seconds": "ProgramDateTimeIntervalSeconds",
        "stream_selection": "StreamSelection",
        "repeat_ext_x_key": "RepeatExtXKey",
        "include_iframe_only_stream": "IncludeIframeOnlyStream",
    }

    ad_markers: Optional[Union[str, AdMarkers, Ref, GetAtt, Sub]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    program_date_time_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None
    repeat_ext_x_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_iframe_only_stream: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HlsPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "use_audio_rendition_group": "UseAudioRenditionGroup",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
        "hls_manifests": "HlsManifests",
        "include_dvb_subtitles": "IncludeDvbSubtitles",
    }

    use_audio_rendition_group: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[HlsEncryption] = None
    hls_manifests: Optional[list[HlsManifest]] = None
    include_dvb_subtitles: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MssEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "speke_key_provider": "SpekeKeyProvider",
    }

    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class MssManifest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_name": "ManifestName",
        "stream_selection": "StreamSelection",
    }

    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None


@dataclass
class MssPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mss_manifests": "MssManifests",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
    }

    mss_manifests: Optional[list[MssManifest]] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[MssEncryption] = None


@dataclass
class SpekeKeyProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "system_ids": "SystemIds",
        "encryption_contract_configuration": "EncryptionContractConfiguration",
        "role_arn": "RoleArn",
        "url": "Url",
    }

    system_ids: Optional[Union[list[str], Ref]] = None
    encryption_contract_configuration: Optional[EncryptionContractConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamSelection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_video_bits_per_second": "MinVideoBitsPerSecond",
        "stream_order": "StreamOrder",
        "max_video_bits_per_second": "MaxVideoBitsPerSecond",
    }

    min_video_bits_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stream_order: Optional[Union[str, StreamOrder, Ref, GetAtt, Sub]] = None
    max_video_bits_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None

