"""PropertyTypes for AWS::MediaPackageV2::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DashBaseUrl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_location": "ServiceLocation",
        "dvb_weight": "DvbWeight",
        "dvb_priority": "DvbPriority",
        "url": "Url",
    }

    service_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dvb_weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dvb_priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DashDvbFontDownload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "font_family": "FontFamily",
        "url": "Url",
        "mime_type": "MimeType",
    }

    font_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mime_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DashDvbMetricsReporting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "reporting_url": "ReportingUrl",
        "probability": "Probability",
    }

    reporting_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    probability: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DashDvbSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "font_download": "FontDownload",
        "error_metrics": "ErrorMetrics",
    }

    font_download: Optional[DashDvbFontDownload] = None
    error_metrics: Optional[list[DashDvbMetricsReporting]] = None


@dataclass
class DashManifestConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "drm_signaling": "DrmSignaling",
        "compactness": "Compactness",
        "program_information": "ProgramInformation",
        "filter_configuration": "FilterConfiguration",
        "segment_template_format": "SegmentTemplateFormat",
        "base_urls": "BaseUrls",
        "manifest_name": "ManifestName",
        "period_triggers": "PeriodTriggers",
        "suggested_presentation_delay_seconds": "SuggestedPresentationDelaySeconds",
        "utc_timing": "UtcTiming",
        "subtitle_configuration": "SubtitleConfiguration",
        "min_buffer_time_seconds": "MinBufferTimeSeconds",
        "profiles": "Profiles",
        "dvb_settings": "DvbSettings",
        "min_update_period_seconds": "MinUpdatePeriodSeconds",
        "scte_dash": "ScteDash",
    }

    manifest_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    drm_signaling: Optional[Union[str, Ref, GetAtt, Sub]] = None
    compactness: Optional[Union[str, Ref, GetAtt, Sub]] = None
    program_information: Optional[DashProgramInformation] = None
    filter_configuration: Optional[FilterConfiguration] = None
    segment_template_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base_urls: Optional[list[DashBaseUrl]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period_triggers: Optional[Union[list[str], Ref]] = None
    suggested_presentation_delay_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    utc_timing: Optional[DashUtcTiming] = None
    subtitle_configuration: Optional[DashSubtitleConfiguration] = None
    min_buffer_time_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    profiles: Optional[Union[list[str], Ref]] = None
    dvb_settings: Optional[DashDvbSettings] = None
    min_update_period_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scte_dash: Optional[ScteDash] = None


@dataclass
class DashProgramInformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "copyright": "Copyright",
        "language_code": "LanguageCode",
        "title": "Title",
        "more_information_url": "MoreInformationUrl",
        "source": "Source",
    }

    copyright: Optional[Union[str, Ref, GetAtt, Sub]] = None
    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    more_information_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DashSubtitleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ttml_configuration": "TtmlConfiguration",
    }

    ttml_configuration: Optional[DashTtmlConfiguration] = None


@dataclass
class DashTtmlConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ttml_profile": "TtmlProfile",
    }

    ttml_profile: Optional[Union[str, DashTtmlProfile, Ref, GetAtt, Sub]] = None


@dataclass
class DashUtcTiming(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timing_mode": "TimingMode",
        "timing_source": "TimingSource",
    }

    timing_mode: Optional[Union[str, DashUtcTimingMode, Ref, GetAtt, Sub]] = None
    timing_source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Encryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_rotation_interval_seconds": "KeyRotationIntervalSeconds",
        "cmaf_exclude_segment_drm_metadata": "CmafExcludeSegmentDrmMetadata",
        "constant_initialization_vector": "ConstantInitializationVector",
        "speke_key_provider": "SpekeKeyProvider",
        "encryption_method": "EncryptionMethod",
    }

    key_rotation_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cmaf_exclude_segment_drm_metadata: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    speke_key_provider: Optional[SpekeKeyProvider] = None
    encryption_method: Optional[EncryptionMethod] = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "preset_speke20_audio": "PresetSpeke20Audio",
        "preset_speke20_video": "PresetSpeke20Video",
    }

    preset_speke20_audio: Optional[Union[str, PresetSpeke20Audio, Ref, GetAtt, Sub]] = None
    preset_speke20_video: Optional[Union[str, PresetSpeke20Video, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionMethod(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ism_encryption_method": "IsmEncryptionMethod",
        "cmaf_encryption_method": "CmafEncryptionMethod",
        "ts_encryption_method": "TsEncryptionMethod",
    }

    ism_encryption_method: Optional[Union[str, IsmEncryptionMethod, Ref, GetAtt, Sub]] = None
    cmaf_encryption_method: Optional[Union[str, CmafEncryptionMethod, Ref, GetAtt, Sub]] = None
    ts_encryption_method: Optional[Union[str, TsEncryptionMethod, Ref, GetAtt, Sub]] = None


@dataclass
class FilterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
        "time_delay_seconds": "TimeDelaySeconds",
        "clip_start_time": "ClipStartTime",
        "manifest_filter": "ManifestFilter",
    }

    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_delay_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    clip_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_filter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ForceEndpointErrorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_error_conditions": "EndpointErrorConditions",
    }

    endpoint_error_conditions: Optional[Union[list[str], Ref]] = None


@dataclass
class HlsManifestConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "manifest_name": "ManifestName",
        "program_date_time_interval_seconds": "ProgramDateTimeIntervalSeconds",
        "child_manifest_name": "ChildManifestName",
        "scte_hls": "ScteHls",
        "filter_configuration": "FilterConfiguration",
        "url_encode_child_manifest": "UrlEncodeChildManifest",
        "url": "Url",
        "start_tag": "StartTag",
    }

    manifest_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    program_date_time_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    child_manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte_hls: Optional[ScteHls] = None
    filter_configuration: Optional[FilterConfiguration] = None
    url_encode_child_manifest: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_tag: Optional[StartTag] = None


@dataclass
class LowLatencyHlsManifestConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "manifest_name": "ManifestName",
        "program_date_time_interval_seconds": "ProgramDateTimeIntervalSeconds",
        "child_manifest_name": "ChildManifestName",
        "scte_hls": "ScteHls",
        "filter_configuration": "FilterConfiguration",
        "url_encode_child_manifest": "UrlEncodeChildManifest",
        "url": "Url",
        "start_tag": "StartTag",
    }

    manifest_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    program_date_time_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    child_manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte_hls: Optional[ScteHls] = None
    filter_configuration: Optional[FilterConfiguration] = None
    url_encode_child_manifest: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_tag: Optional[StartTag] = None


@dataclass
class MssManifestConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "manifest_name": "ManifestName",
        "manifest_layout": "ManifestLayout",
        "filter_configuration": "FilterConfiguration",
    }

    manifest_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_layout: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter_configuration: Optional[FilterConfiguration] = None


@dataclass
class Scte(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scte_filter": "ScteFilter",
    }

    scte_filter: Optional[Union[list[str], Ref]] = None


@dataclass
class ScteDash(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_marker_dash": "AdMarkerDash",
    }

    ad_marker_dash: Optional[Union[str, AdMarkerDash, Ref, GetAtt, Sub]] = None


@dataclass
class ScteHls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_marker_hls": "AdMarkerHls",
    }

    ad_marker_hls: Optional[Union[str, AdMarkerHls, Ref, GetAtt, Sub]] = None


@dataclass
class Segment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_name": "SegmentName",
        "ts_use_audio_rendition_group": "TsUseAudioRenditionGroup",
        "include_iframe_only_streams": "IncludeIframeOnlyStreams",
        "scte": "Scte",
        "ts_include_dvb_subtitles": "TsIncludeDvbSubtitles",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
    }

    segment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ts_use_audio_rendition_group: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_iframe_only_streams: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scte: Optional[Scte] = None
    ts_include_dvb_subtitles: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[Encryption] = None


@dataclass
class SpekeKeyProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "drm_systems": "DrmSystems",
        "resource_id": "ResourceId",
        "encryption_contract_configuration": "EncryptionContractConfiguration",
        "role_arn": "RoleArn",
        "url": "Url",
    }

    drm_systems: Optional[Union[list[str], Ref]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_contract_configuration: Optional[EncryptionContractConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StartTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "precise": "Precise",
        "time_offset": "TimeOffset",
    }

    precise: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    time_offset: Optional[Union[float, Ref, GetAtt, Sub]] = None

