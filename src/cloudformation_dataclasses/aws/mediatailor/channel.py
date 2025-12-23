"""PropertyTypes for AWS::MediaTailor::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

