"""PropertyTypes for AWS::MediaTailor::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DashPlaylistSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_window_seconds": "ManifestWindowSeconds",
        "ad_markup_type": "AdMarkupType",
    }

    manifest_window_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ad_markup_type: Optional[Union[list[str], Ref]] = None


@dataclass
class LogConfigurationForChannel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_types": "LogTypes",
    }

    log_types: Optional[Union[list[str], Ref]] = None


@dataclass
class RequestOutputItem(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "vod_source_name": "VodSourceName",
        "source_location_name": "SourceLocationName",
    }

    vod_source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_location_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeShiftConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_time_delay_seconds": "MaxTimeDelaySeconds",
    }

    max_time_delay_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None

