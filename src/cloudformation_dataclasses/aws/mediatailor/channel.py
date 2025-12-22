"""PropertyTypes for AWS::MediaTailor::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessType:
    """AccessType enum values."""

    S3_SIGV4 = "S3_SIGV4"
    SECRETS_MANAGER_ACCESS_TOKEN = "SECRETS_MANAGER_ACCESS_TOKEN"
    AUTODETECT_SIGV4 = "AUTODETECT_SIGV4"


class AdMarkupType:
    """AdMarkupType enum values."""

    DATERANGE = "DATERANGE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"


class AdsInteractionExcludeEventType:
    """AdsInteractionExcludeEventType enum values."""

    AD_MARKER_FOUND = "AD_MARKER_FOUND"
    NON_AD_MARKER_FOUND = "NON_AD_MARKER_FOUND"
    MAKING_ADS_REQUEST = "MAKING_ADS_REQUEST"
    MODIFIED_TARGET_URL = "MODIFIED_TARGET_URL"
    VAST_REDIRECT = "VAST_REDIRECT"
    EMPTY_VAST_RESPONSE = "EMPTY_VAST_RESPONSE"
    EMPTY_VMAP_RESPONSE = "EMPTY_VMAP_RESPONSE"
    VAST_RESPONSE = "VAST_RESPONSE"
    REDIRECTED_VAST_RESPONSE = "REDIRECTED_VAST_RESPONSE"
    FILLED_AVAIL = "FILLED_AVAIL"
    FILLED_OVERLAY_AVAIL = "FILLED_OVERLAY_AVAIL"
    BEACON_FIRED = "BEACON_FIRED"
    WARNING_NO_ADVERTISEMENTS = "WARNING_NO_ADVERTISEMENTS"
    WARNING_VPAID_AD_DROPPED = "WARNING_VPAID_AD_DROPPED"
    WARNING_URL_VARIABLE_SUBSTITUTION_FAILED = "WARNING_URL_VARIABLE_SUBSTITUTION_FAILED"
    ERROR_UNKNOWN = "ERROR_UNKNOWN"
    ERROR_UNKNOWN_HOST = "ERROR_UNKNOWN_HOST"
    ERROR_DISALLOWED_HOST = "ERROR_DISALLOWED_HOST"
    ERROR_ADS_IO = "ERROR_ADS_IO"
    ERROR_ADS_TIMEOUT = "ERROR_ADS_TIMEOUT"
    ERROR_ADS_RESPONSE_PARSE = "ERROR_ADS_RESPONSE_PARSE"
    ERROR_ADS_RESPONSE_UNKNOWN_ROOT_ELEMENT = "ERROR_ADS_RESPONSE_UNKNOWN_ROOT_ELEMENT"
    ERROR_ADS_INVALID_RESPONSE = "ERROR_ADS_INVALID_RESPONSE"
    ERROR_VAST_REDIRECT_EMPTY_RESPONSE = "ERROR_VAST_REDIRECT_EMPTY_RESPONSE"
    ERROR_VAST_REDIRECT_MULTIPLE_VAST = "ERROR_VAST_REDIRECT_MULTIPLE_VAST"
    ERROR_VAST_REDIRECT_FAILED = "ERROR_VAST_REDIRECT_FAILED"
    ERROR_VAST_MISSING_MEDIAFILES = "ERROR_VAST_MISSING_MEDIAFILES"
    ERROR_VAST_MISSING_CREATIVES = "ERROR_VAST_MISSING_CREATIVES"
    ERROR_VAST_MISSING_OVERLAYS = "ERROR_VAST_MISSING_OVERLAYS"
    ERROR_VAST_MISSING_IMPRESSION = "ERROR_VAST_MISSING_IMPRESSION"
    ERROR_VAST_INVALID_VAST_AD_TAG_URI = "ERROR_VAST_INVALID_VAST_AD_TAG_URI"
    ERROR_VAST_MULTIPLE_TRACKING_EVENTS = "ERROR_VAST_MULTIPLE_TRACKING_EVENTS"
    ERROR_VAST_MULTIPLE_LINEAR = "ERROR_VAST_MULTIPLE_LINEAR"
    ERROR_VAST_INVALID_MEDIA_FILE = "ERROR_VAST_INVALID_MEDIA_FILE"
    ERROR_FIRING_BEACON_FAILED = "ERROR_FIRING_BEACON_FAILED"
    ERROR_PERSONALIZATION_DISABLED = "ERROR_PERSONALIZATION_DISABLED"
    VOD_TIME_BASED_AVAIL_PLAN_VAST_RESPONSE_FOR_OFFSET = "VOD_TIME_BASED_AVAIL_PLAN_VAST_RESPONSE_FOR_OFFSET"
    VOD_TIME_BASED_AVAIL_PLAN_SUCCESS = "VOD_TIME_BASED_AVAIL_PLAN_SUCCESS"
    VOD_TIME_BASED_AVAIL_PLAN_WARNING_NO_ADVERTISEMENTS = "VOD_TIME_BASED_AVAIL_PLAN_WARNING_NO_ADVERTISEMENTS"
    INTERSTITIAL_VOD_SUCCESS = "INTERSTITIAL_VOD_SUCCESS"
    INTERSTITIAL_VOD_FAILURE = "INTERSTITIAL_VOD_FAILURE"


class AdsInteractionPublishOptInEventType:
    """AdsInteractionPublishOptInEventType enum values."""

    RAW_ADS_RESPONSE = "RAW_ADS_RESPONSE"


class AlertCategory:
    """AlertCategory enum values."""

    SCHEDULING_ERROR = "SCHEDULING_ERROR"
    PLAYBACK_WARNING = "PLAYBACK_WARNING"
    INFO = "INFO"


class ChannelState:
    """ChannelState enum values."""

    RUNNING = "RUNNING"
    STOPPED = "STOPPED"


class CompressionMethod:
    """CompressionMethod enum values."""

    NONE = "NONE"
    GZIP = "GZIP"


class FillPolicy:
    """FillPolicy enum values."""

    FULL_AVAIL_ONLY = "FULL_AVAIL_ONLY"
    PARTIAL_AVAIL = "PARTIAL_AVAIL"


class InsertionMode:
    """InsertionMode enum values."""

    STITCHED_ONLY = "STITCHED_ONLY"
    PLAYER_SELECT = "PLAYER_SELECT"


class ListPrefetchScheduleType:
    """ListPrefetchScheduleType enum values."""

    SINGLE = "SINGLE"
    RECURRING = "RECURRING"
    ALL = "ALL"


class LogType:
    """LogType enum values."""

    AS_RUN = "AS_RUN"


class LoggingStrategy:
    """LoggingStrategy enum values."""

    VENDED_LOGS = "VENDED_LOGS"
    LEGACY_CLOUDWATCH = "LEGACY_CLOUDWATCH"


class ManifestServiceExcludeEventType:
    """ManifestServiceExcludeEventType enum values."""

    GENERATED_MANIFEST = "GENERATED_MANIFEST"
    ORIGIN_MANIFEST = "ORIGIN_MANIFEST"
    SESSION_INITIALIZED = "SESSION_INITIALIZED"
    TRACKING_RESPONSE = "TRACKING_RESPONSE"
    CONFIG_SYNTAX_ERROR = "CONFIG_SYNTAX_ERROR"
    CONFIG_SECURITY_ERROR = "CONFIG_SECURITY_ERROR"
    UNKNOWN_HOST = "UNKNOWN_HOST"
    TIMEOUT_ERROR = "TIMEOUT_ERROR"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    IO_ERROR = "IO_ERROR"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"
    HOST_DISALLOWED = "HOST_DISALLOWED"
    PARSING_ERROR = "PARSING_ERROR"
    MANIFEST_ERROR = "MANIFEST_ERROR"
    NO_MASTER_OR_MEDIA_PLAYLIST = "NO_MASTER_OR_MEDIA_PLAYLIST"
    NO_MASTER_PLAYLIST = "NO_MASTER_PLAYLIST"
    NO_MEDIA_PLAYLIST = "NO_MEDIA_PLAYLIST"
    INCOMPATIBLE_HLS_VERSION = "INCOMPATIBLE_HLS_VERSION"
    SCTE35_PARSING_ERROR = "SCTE35_PARSING_ERROR"
    INVALID_SINGLE_PERIOD_DASH_MANIFEST = "INVALID_SINGLE_PERIOD_DASH_MANIFEST"
    UNSUPPORTED_SINGLE_PERIOD_DASH_MANIFEST = "UNSUPPORTED_SINGLE_PERIOD_DASH_MANIFEST"
    LAST_PERIOD_MISSING_AUDIO = "LAST_PERIOD_MISSING_AUDIO"
    LAST_PERIOD_MISSING_AUDIO_WARNING = "LAST_PERIOD_MISSING_AUDIO_WARNING"
    ERROR_ORIGIN_PREFIX_INTERPOLATION = "ERROR_ORIGIN_PREFIX_INTERPOLATION"
    ERROR_ADS_INTERPOLATION = "ERROR_ADS_INTERPOLATION"
    ERROR_LIVE_PRE_ROLL_ADS_INTERPOLATION = "ERROR_LIVE_PRE_ROLL_ADS_INTERPOLATION"
    ERROR_CDN_AD_SEGMENT_INTERPOLATION = "ERROR_CDN_AD_SEGMENT_INTERPOLATION"
    ERROR_CDN_CONTENT_SEGMENT_INTERPOLATION = "ERROR_CDN_CONTENT_SEGMENT_INTERPOLATION"
    ERROR_SLATE_AD_URL_INTERPOLATION = "ERROR_SLATE_AD_URL_INTERPOLATION"
    ERROR_PROFILE_NAME_INTERPOLATION = "ERROR_PROFILE_NAME_INTERPOLATION"
    ERROR_BUMPER_START_INTERPOLATION = "ERROR_BUMPER_START_INTERPOLATION"
    ERROR_BUMPER_END_INTERPOLATION = "ERROR_BUMPER_END_INTERPOLATION"


class MessageType:
    """MessageType enum values."""

    SPLICE_INSERT = "SPLICE_INSERT"
    TIME_SIGNAL = "TIME_SIGNAL"


class Method:
    """Method enum values."""

    GET = "GET"
    POST = "POST"


class Mode:
    """Mode enum values."""

    OFF = "OFF"
    BEHIND_LIVE_EDGE = "BEHIND_LIVE_EDGE"
    AFTER_LIVE_EDGE = "AFTER_LIVE_EDGE"


class Operator:
    """Operator enum values."""

    EQUALS = "EQUALS"


class OriginManifestType:
    """OriginManifestType enum values."""

    SINGLE_PERIOD = "SINGLE_PERIOD"
    MULTI_PERIOD = "MULTI_PERIOD"


class PlaybackMode:
    """PlaybackMode enum values."""

    LOOP = "LOOP"
    LINEAR = "LINEAR"


class PrefetchScheduleType:
    """PrefetchScheduleType enum values."""

    SINGLE = "SINGLE"
    RECURRING = "RECURRING"


class RelativePosition:
    """RelativePosition enum values."""

    BEFORE_PROGRAM = "BEFORE_PROGRAM"
    AFTER_PROGRAM = "AFTER_PROGRAM"


class ScheduleEntryType:
    """ScheduleEntryType enum values."""

    PROGRAM = "PROGRAM"
    FILLER_SLATE = "FILLER_SLATE"
    ALTERNATE_MEDIA = "ALTERNATE_MEDIA"


class StreamingMediaFileConditioning:
    """StreamingMediaFileConditioning enum values."""

    TRANSCODE = "TRANSCODE"
    NONE = "NONE"


class Tier:
    """Tier enum values."""

    BASIC = "BASIC"
    STANDARD = "STANDARD"


class TrafficShapingType:
    """TrafficShapingType enum values."""

    RETRIEVAL_WINDOW = "RETRIEVAL_WINDOW"
    TPS = "TPS"


class Type:
    """Type enum values."""

    DASH = "DASH"
    HLS = "HLS"


@dataclass
class DashPlaylistSettings(PropertyType):
    MANIFEST_WINDOW_SECONDS = "ManifestWindowSeconds"
    SUGGESTED_PRESENTATION_DELAY_SECONDS = "SuggestedPresentationDelaySeconds"
    MIN_BUFFER_TIME_SECONDS = "MinBufferTimeSeconds"
    MIN_UPDATE_PERIOD_SECONDS = "MinUpdatePeriodSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "suggested_presentation_delay_seconds": "SuggestedPresentationDelaySeconds",
        "min_buffer_time_seconds": "MinBufferTimeSeconds",
        "min_update_period_seconds": "MinUpdatePeriodSeconds",
    }

    manifest_window_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    suggested_presentation_delay_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    min_buffer_time_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    min_update_period_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class HlsPlaylistSettings(PropertyType):
    MANIFEST_WINDOW_SECONDS = "ManifestWindowSeconds"
    AD_MARKUP_TYPE = "AdMarkupType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "ad_markup_type": "AdMarkupType",
    }

    manifest_window_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ad_markup_type: Optional[Union[list[str], Ref]] = None


@dataclass
class LogConfigurationForChannel(PropertyType):
    LOG_TYPES = "LogTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_types": "LogTypes",
    }

    log_types: Optional[Union[list[str], Ref]] = None


@dataclass
class RequestOutputItem(PropertyType):
    MANIFEST_NAME = "ManifestName"
    DASH_PLAYLIST_SETTINGS = "DashPlaylistSettings"
    HLS_PLAYLIST_SETTINGS = "HlsPlaylistSettings"
    SOURCE_GROUP = "SourceGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_name": "ManifestName",
        "dash_playlist_settings": "DashPlaylistSettings",
        "hls_playlist_settings": "HlsPlaylistSettings",
        "source_group": "SourceGroup",
    }

    manifest_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dash_playlist_settings: Optional[DashPlaylistSettings] = None
    hls_playlist_settings: Optional[HlsPlaylistSettings] = None
    source_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlateSource(PropertyType):
    VOD_SOURCE_NAME = "VodSourceName"
    SOURCE_LOCATION_NAME = "SourceLocationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vod_source_name": "VodSourceName",
        "source_location_name": "SourceLocationName",
    }

    vod_source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_location_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeShiftConfiguration(PropertyType):
    MAX_TIME_DELAY_SECONDS = "MaxTimeDelaySeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_time_delay_seconds": "MaxTimeDelaySeconds",
    }

    max_time_delay_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None

