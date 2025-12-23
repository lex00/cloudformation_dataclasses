"""PropertyTypes for AWS::MediaTailor::PlaybackConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

