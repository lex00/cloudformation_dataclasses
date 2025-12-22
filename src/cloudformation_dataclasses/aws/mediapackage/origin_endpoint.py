"""PropertyTypes for AWS::MediaPackage::OriginEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AdMarkers:
    """AdMarkers enum values."""

    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"
    DATERANGE = "DATERANGE"


class AdsOnDeliveryRestrictions:
    """AdsOnDeliveryRestrictions enum values."""

    NONE = "NONE"
    RESTRICTED = "RESTRICTED"
    UNRESTRICTED = "UNRESTRICTED"
    BOTH = "BOTH"


class CmafEncryptionMethod:
    """CmafEncryptionMethod enum values."""

    SAMPLE_AES = "SAMPLE_AES"
    AES_CTR = "AES_CTR"


class EncryptionMethod:
    """EncryptionMethod enum values."""

    AES_128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"


class ManifestLayout:
    """ManifestLayout enum values."""

    FULL = "FULL"
    COMPACT = "COMPACT"
    DRM_TOP_LEVEL_COMPACT = "DRM_TOP_LEVEL_COMPACT"


class Origination:
    """Origination enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class PlaylistType:
    """PlaylistType enum values."""

    NONE = "NONE"
    EVENT = "EVENT"
    VOD = "VOD"


class PresetSpeke20Audio:
    """PresetSpeke20Audio enum values."""

    PRESET_AUDIO_1 = "PRESET-AUDIO-1"
    PRESET_AUDIO_2 = "PRESET-AUDIO-2"
    PRESET_AUDIO_3 = "PRESET-AUDIO-3"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class PresetSpeke20Video:
    """PresetSpeke20Video enum values."""

    PRESET_VIDEO_1 = "PRESET-VIDEO-1"
    PRESET_VIDEO_2 = "PRESET-VIDEO-2"
    PRESET_VIDEO_3 = "PRESET-VIDEO-3"
    PRESET_VIDEO_4 = "PRESET-VIDEO-4"
    PRESET_VIDEO_5 = "PRESET-VIDEO-5"
    PRESET_VIDEO_6 = "PRESET-VIDEO-6"
    PRESET_VIDEO_7 = "PRESET-VIDEO-7"
    PRESET_VIDEO_8 = "PRESET-VIDEO-8"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class Profile:
    """Profile enum values."""

    NONE = "NONE"
    HBBTV_1_5 = "HBBTV_1_5"
    HYBRIDCAST = "HYBRIDCAST"
    DVB_DASH_2014 = "DVB_DASH_2014"


class SegmentTemplateFormat:
    """SegmentTemplateFormat enum values."""

    NUMBER_WITH_TIMELINE = "NUMBER_WITH_TIMELINE"
    TIME_WITH_TIMELINE = "TIME_WITH_TIMELINE"
    NUMBER_WITH_DURATION = "NUMBER_WITH_DURATION"


class Status:
    """Status enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class StreamOrder:
    """StreamOrder enum values."""

    ORIGINAL = "ORIGINAL"
    VIDEO_BITRATE_ASCENDING = "VIDEO_BITRATE_ASCENDING"
    VIDEO_BITRATE_DESCENDING = "VIDEO_BITRATE_DESCENDING"


class UtcTiming:
    """UtcTiming enum values."""

    NONE = "NONE"
    HTTP_HEAD = "HTTP-HEAD"
    HTTP_ISO = "HTTP-ISO"
    HTTP_XSDATE = "HTTP-XSDATE"


class __AdTriggersElement:
    """__AdTriggersElement enum values."""

    SPLICE_INSERT = "SPLICE_INSERT"
    BREAK = "BREAK"
    PROVIDER_ADVERTISEMENT = "PROVIDER_ADVERTISEMENT"
    DISTRIBUTOR_ADVERTISEMENT = "DISTRIBUTOR_ADVERTISEMENT"
    PROVIDER_PLACEMENT_OPPORTUNITY = "PROVIDER_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_PLACEMENT_OPPORTUNITY"
    PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY = "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"


class __PeriodTriggersElement:
    """__PeriodTriggersElement enum values."""

    ADS = "ADS"


@dataclass
class Authorization(PropertyType):
    SECRETS_ROLE_ARN = "SecretsRoleArn"
    CDN_IDENTIFIER_SECRET = "CdnIdentifierSecret"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_role_arn": "SecretsRoleArn",
        "cdn_identifier_secret": "CdnIdentifierSecret",
    }

    secrets_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdn_identifier_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CmafEncryption(PropertyType):
    KEY_ROTATION_INTERVAL_SECONDS = "KeyRotationIntervalSeconds"
    SPEKE_KEY_PROVIDER = "SpekeKeyProvider"
    CONSTANT_INITIALIZATION_VECTOR = "ConstantInitializationVector"
    ENCRYPTION_METHOD = "EncryptionMethod"

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
    SEGMENT_PREFIX = "SegmentPrefix"
    STREAM_SELECTION = "StreamSelection"
    SEGMENT_DURATION_SECONDS = "SegmentDurationSeconds"
    ENCRYPTION = "Encryption"
    HLS_MANIFESTS = "HlsManifests"

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
    KEY_ROTATION_INTERVAL_SECONDS = "KeyRotationIntervalSeconds"
    SPEKE_KEY_PROVIDER = "SpekeKeyProvider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_rotation_interval_seconds": "KeyRotationIntervalSeconds",
        "speke_key_provider": "SpekeKeyProvider",
    }

    key_rotation_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class DashPackage(PropertyType):
    MANIFEST_WINDOW_SECONDS = "ManifestWindowSeconds"
    ADS_ON_DELIVERY_RESTRICTIONS = "AdsOnDeliveryRestrictions"
    MANIFEST_LAYOUT = "ManifestLayout"
    STREAM_SELECTION = "StreamSelection"
    INCLUDE_IFRAME_ONLY_STREAM = "IncludeIframeOnlyStream"
    SEGMENT_TEMPLATE_FORMAT = "SegmentTemplateFormat"
    ENCRYPTION = "Encryption"
    AD_TRIGGERS = "AdTriggers"
    PROFILE = "Profile"
    PERIOD_TRIGGERS = "PeriodTriggers"
    SUGGESTED_PRESENTATION_DELAY_SECONDS = "SuggestedPresentationDelaySeconds"
    UTC_TIMING = "UtcTiming"
    MIN_BUFFER_TIME_SECONDS = "MinBufferTimeSeconds"
    SEGMENT_DURATION_SECONDS = "SegmentDurationSeconds"
    MIN_UPDATE_PERIOD_SECONDS = "MinUpdatePeriodSeconds"
    UTC_TIMING_URI = "UtcTimingUri"

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
    KEY_ROTATION_INTERVAL_SECONDS = "KeyRotationIntervalSeconds"
    REPEAT_EXT_X_KEY = "RepeatExtXKey"
    CONSTANT_INITIALIZATION_VECTOR = "ConstantInitializationVector"
    SPEKE_KEY_PROVIDER = "SpekeKeyProvider"
    ENCRYPTION_METHOD = "EncryptionMethod"

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
    ADS_ON_DELIVERY_RESTRICTIONS = "AdsOnDeliveryRestrictions"
    MANIFEST_NAME = "ManifestName"
    AD_MARKERS = "AdMarkers"
    PROGRAM_DATE_TIME_INTERVAL_SECONDS = "ProgramDateTimeIntervalSeconds"
    PLAYLIST_WINDOW_SECONDS = "PlaylistWindowSeconds"
    INCLUDE_IFRAME_ONLY_STREAM = "IncludeIframeOnlyStream"
    ID = "Id"
    PLAYLIST_TYPE = "PlaylistType"
    AD_TRIGGERS = "AdTriggers"
    URL = "Url"

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
    ADS_ON_DELIVERY_RESTRICTIONS = "AdsOnDeliveryRestrictions"
    AD_MARKERS = "AdMarkers"
    PROGRAM_DATE_TIME_INTERVAL_SECONDS = "ProgramDateTimeIntervalSeconds"
    STREAM_SELECTION = "StreamSelection"
    PLAYLIST_WINDOW_SECONDS = "PlaylistWindowSeconds"
    INCLUDE_IFRAME_ONLY_STREAM = "IncludeIframeOnlyStream"
    USE_AUDIO_RENDITION_GROUP = "UseAudioRenditionGroup"
    SEGMENT_DURATION_SECONDS = "SegmentDurationSeconds"
    ENCRYPTION = "Encryption"
    PLAYLIST_TYPE = "PlaylistType"
    AD_TRIGGERS = "AdTriggers"
    INCLUDE_DVB_SUBTITLES = "IncludeDvbSubtitles"

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
    SPEKE_KEY_PROVIDER = "SpekeKeyProvider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "speke_key_provider": "SpekeKeyProvider",
    }

    speke_key_provider: Optional[SpekeKeyProvider] = None


@dataclass
class MssPackage(PropertyType):
    MANIFEST_WINDOW_SECONDS = "ManifestWindowSeconds"
    STREAM_SELECTION = "StreamSelection"
    SEGMENT_DURATION_SECONDS = "SegmentDurationSeconds"
    ENCRYPTION = "Encryption"

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
    RESOURCE_ID = "ResourceId"
    SYSTEM_IDS = "SystemIds"
    ENCRYPTION_CONTRACT_CONFIGURATION = "EncryptionContractConfiguration"
    URL = "Url"
    ROLE_ARN = "RoleArn"
    CERTIFICATE_ARN = "CertificateArn"

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
    MIN_VIDEO_BITS_PER_SECOND = "MinVideoBitsPerSecond"
    STREAM_ORDER = "StreamOrder"
    MAX_VIDEO_BITS_PER_SECOND = "MaxVideoBitsPerSecond"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_video_bits_per_second": "MinVideoBitsPerSecond",
        "stream_order": "StreamOrder",
        "max_video_bits_per_second": "MaxVideoBitsPerSecond",
    }

    min_video_bits_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stream_order: Optional[Union[str, StreamOrder, Ref, GetAtt, Sub]] = None
    max_video_bits_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None

