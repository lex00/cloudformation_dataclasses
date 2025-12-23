"""PropertyTypes for AWS::MediaPackage::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Authorization(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_role_arn": "SecretsRoleArn",
        "cdn_identifier_secret": "CdnIdentifierSecret",
    }

    secrets_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdn_identifier_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CmafEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_rotation_interval_seconds": "KeyRotationIntervalSeconds",
        "speke_key_provider": "SpekeKeyProvider",
        "constant_initialization_vector": "ConstantInitializationVector",
        "encryption_method": "EncryptionMethod",
    }

    key_rotation_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    speke_key_provider: Optional[SpekeKeyProvider] = None
    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_method: Optional[Union[str, CmafEncryptionMethod, Ref, GetAtt, Sub]] = None


@dataclass
class CmafPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_prefix": "SegmentPrefix",
        "stream_selection": "StreamSelection",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
        "hls_manifests": "HlsManifests",
    }

    segment_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[CmafEncryption] = None
    hls_manifests: Optional[list[HlsManifest]] = None


@dataclass
class DashEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_rotation_interval_seconds": "KeyRotationIntervalSeconds",
        "speke_key_provider": "SpekeKeyProvider",
    }

    key_rotation_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class DashPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "ads_on_delivery_restrictions": "AdsOnDeliveryRestrictions",
        "manifest_layout": "ManifestLayout",
        "stream_selection": "StreamSelection",
        "include_iframe_only_stream": "IncludeIframeOnlyStream",
        "segment_template_format": "SegmentTemplateFormat",
        "encryption": "Encryption",
        "ad_triggers": "AdTriggers",
        "profile": "Profile",
        "period_triggers": "PeriodTriggers",
        "suggested_presentation_delay_seconds": "SuggestedPresentationDelaySeconds",
        "utc_timing": "UtcTiming",
        "min_buffer_time_seconds": "MinBufferTimeSeconds",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "min_update_period_seconds": "MinUpdatePeriodSeconds",
        "utc_timing_uri": "UtcTimingUri",
    }

    manifest_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ads_on_delivery_restrictions: Optional[Union[str, AdsOnDeliveryRestrictions, Ref, GetAtt, Sub]] = None
    manifest_layout: Optional[Union[str, ManifestLayout, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None
    include_iframe_only_stream: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    segment_template_format: Optional[Union[str, SegmentTemplateFormat, Ref, GetAtt, Sub]] = None
    encryption: Optional[DashEncryption] = None
    ad_triggers: Optional[Union[list[str], Ref]] = None
    profile: Optional[Union[str, Profile, Ref, GetAtt, Sub]] = None
    period_triggers: Optional[Union[list[str], Ref]] = None
    suggested_presentation_delay_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    utc_timing: Optional[Union[str, UtcTiming, Ref, GetAtt, Sub]] = None
    min_buffer_time_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_update_period_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    utc_timing_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionContractConfiguration(PropertyType):
    pass


@dataclass
class HlsEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_rotation_interval_seconds": "KeyRotationIntervalSeconds",
        "repeat_ext_x_key": "RepeatExtXKey",
        "constant_initialization_vector": "ConstantInitializationVector",
        "speke_key_provider": "SpekeKeyProvider",
        "encryption_method": "EncryptionMethod",
    }

    key_rotation_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    repeat_ext_x_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    speke_key_provider: Optional[SpekeKeyProvider] = None
    encryption_method: Optional[Union[str, EncryptionMethod, Ref, GetAtt, Sub]] = None


@dataclass
class HlsManifest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ads_on_delivery_restrictions": "AdsOnDeliveryRestrictions",
        "manifest_name": "ManifestName",
        "ad_markers": "AdMarkers",
        "program_date_time_interval_seconds": "ProgramDateTimeIntervalSeconds",
        "playlist_window_seconds": "PlaylistWindowSeconds",
        "include_iframe_only_stream": "IncludeIframeOnlyStream",
        "id": "Id",
        "playlist_type": "PlaylistType",
        "ad_triggers": "AdTriggers",
        "url": "Url",
    }

    ads_on_delivery_restrictions: Optional[Union[str, AdsOnDeliveryRestrictions, Ref, GetAtt, Sub]] = None
    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ad_markers: Optional[Union[str, AdMarkers, Ref, GetAtt, Sub]] = None
    program_date_time_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    playlist_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    include_iframe_only_stream: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    playlist_type: Optional[Union[str, PlaylistType, Ref, GetAtt, Sub]] = None
    ad_triggers: Optional[Union[list[str], Ref]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HlsPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ads_on_delivery_restrictions": "AdsOnDeliveryRestrictions",
        "ad_markers": "AdMarkers",
        "program_date_time_interval_seconds": "ProgramDateTimeIntervalSeconds",
        "stream_selection": "StreamSelection",
        "playlist_window_seconds": "PlaylistWindowSeconds",
        "include_iframe_only_stream": "IncludeIframeOnlyStream",
        "use_audio_rendition_group": "UseAudioRenditionGroup",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
        "playlist_type": "PlaylistType",
        "ad_triggers": "AdTriggers",
        "include_dvb_subtitles": "IncludeDvbSubtitles",
    }

    ads_on_delivery_restrictions: Optional[Union[str, AdsOnDeliveryRestrictions, Ref, GetAtt, Sub]] = None
    ad_markers: Optional[Union[str, AdMarkers, Ref, GetAtt, Sub]] = None
    program_date_time_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None
    playlist_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    include_iframe_only_stream: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_audio_rendition_group: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[HlsEncryption] = None
    playlist_type: Optional[Union[str, PlaylistType, Ref, GetAtt, Sub]] = None
    ad_triggers: Optional[Union[list[str], Ref]] = None
    include_dvb_subtitles: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MssEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "speke_key_provider": "SpekeKeyProvider",
    }

    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class MssPackage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "stream_selection": "StreamSelection",
        "segment_duration_seconds": "SegmentDurationSeconds",
        "encryption": "Encryption",
    }

    manifest_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stream_selection: Optional[StreamSelection] = None
    segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    encryption: Optional[MssEncryption] = None


@dataclass
class SpekeKeyProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_id": "ResourceId",
        "system_ids": "SystemIds",
        "encryption_contract_configuration": "EncryptionContractConfiguration",
        "url": "Url",
        "role_arn": "RoleArn",
        "certificate_arn": "CertificateArn",
    }

    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    system_ids: Optional[Union[list[str], Ref]] = None
    encryption_contract_configuration: Optional[EncryptionContractConfiguration] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

