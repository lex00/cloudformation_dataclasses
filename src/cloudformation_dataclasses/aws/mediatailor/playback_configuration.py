"""PropertyTypes for AWS::MediaTailor::PlaybackConfiguration."""

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
class AdConditioningConfiguration(PropertyType):
    STREAMING_MEDIA_FILE_CONDITIONING = "StreamingMediaFileConditioning"

    _property_mappings: ClassVar[dict[str, str]] = {
        "streaming_media_file_conditioning": "StreamingMediaFileConditioning",
    }

    streaming_media_file_conditioning: Optional[Union[str, StreamingMediaFileConditioning, Ref, GetAtt, Sub]] = None


@dataclass
class AdMarkerPassthrough(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdsInteractionLog(PropertyType):
    EXCLUDE_EVENT_TYPES = "ExcludeEventTypes"
    PUBLISH_OPT_IN_EVENT_TYPES = "PublishOptInEventTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude_event_types": "ExcludeEventTypes",
        "publish_opt_in_event_types": "PublishOptInEventTypes",
    }

    exclude_event_types: Optional[Union[list[str], Ref]] = None
    publish_opt_in_event_types: Optional[Union[list[str], Ref]] = None


@dataclass
class AvailSuppression(PropertyType):
    MODE = "Mode"
    VALUE = "Value"
    FILL_POLICY = "FillPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "value": "Value",
        "fill_policy": "FillPolicy",
    }

    mode: Optional[Union[str, Mode, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fill_policy: Optional[Union[str, FillPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class Bumper(PropertyType):
    START_URL = "StartUrl"
    END_URL = "EndUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start_url": "StartUrl",
        "end_url": "EndUrl",
    }

    start_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CdnConfiguration(PropertyType):
    AD_SEGMENT_URL_PREFIX = "AdSegmentUrlPrefix"
    CONTENT_SEGMENT_URL_PREFIX = "ContentSegmentUrlPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_segment_url_prefix": "AdSegmentUrlPrefix",
        "content_segment_url_prefix": "ContentSegmentUrlPrefix",
    }

    ad_segment_url_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_segment_url_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DashConfiguration(PropertyType):
    MPD_LOCATION = "MpdLocation"
    MANIFEST_ENDPOINT_PREFIX = "ManifestEndpointPrefix"
    ORIGIN_MANIFEST_TYPE = "OriginManifestType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mpd_location": "MpdLocation",
        "manifest_endpoint_prefix": "ManifestEndpointPrefix",
        "origin_manifest_type": "OriginManifestType",
    }

    mpd_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_endpoint_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_manifest_type: Optional[Union[str, OriginManifestType, Ref, GetAtt, Sub]] = None


@dataclass
class HlsConfiguration(PropertyType):
    MANIFEST_ENDPOINT_PREFIX = "ManifestEndpointPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_endpoint_prefix": "ManifestEndpointPrefix",
    }

    manifest_endpoint_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LivePreRollConfiguration(PropertyType):
    AD_DECISION_SERVER_URL = "AdDecisionServerUrl"
    MAX_DURATION_SECONDS = "MaxDurationSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_decision_server_url": "AdDecisionServerUrl",
        "max_duration_seconds": "MaxDurationSeconds",
    }

    ad_decision_server_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfiguration(PropertyType):
    ENABLED_LOGGING_STRATEGIES = "EnabledLoggingStrategies"
    PERCENT_ENABLED = "PercentEnabled"
    ADS_INTERACTION_LOG = "AdsInteractionLog"
    MANIFEST_SERVICE_INTERACTION_LOG = "ManifestServiceInteractionLog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_logging_strategies": "EnabledLoggingStrategies",
        "percent_enabled": "PercentEnabled",
        "ads_interaction_log": "AdsInteractionLog",
        "manifest_service_interaction_log": "ManifestServiceInteractionLog",
    }

    enabled_logging_strategies: Optional[Union[list[str], Ref]] = None
    percent_enabled: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ads_interaction_log: Optional[AdsInteractionLog] = None
    manifest_service_interaction_log: Optional[ManifestServiceInteractionLog] = None


@dataclass
class ManifestProcessingRules(PropertyType):
    AD_MARKER_PASSTHROUGH = "AdMarkerPassthrough"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_marker_passthrough": "AdMarkerPassthrough",
    }

    ad_marker_passthrough: Optional[AdMarkerPassthrough] = None


@dataclass
class ManifestServiceInteractionLog(PropertyType):
    EXCLUDE_EVENT_TYPES = "ExcludeEventTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude_event_types": "ExcludeEventTypes",
    }

    exclude_event_types: Optional[Union[list[str], Ref]] = None

