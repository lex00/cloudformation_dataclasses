"""PropertyTypes for AWS::IVS::Stage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoParticipantRecordingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_configuration_arn": "StorageConfigurationArn",
        "recording_reconnect_window_seconds": "RecordingReconnectWindowSeconds",
        "media_types": "MediaTypes",
        "hls_configuration": "HlsConfiguration",
        "thumbnail_configuration": "ThumbnailConfiguration",
    }

    storage_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recording_reconnect_window_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    media_types: Optional[Union[list[str], Ref]] = None
    hls_configuration: Optional[HlsConfiguration] = None
    thumbnail_configuration: Optional[ThumbnailConfiguration] = None


@dataclass
class HlsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "participant_recording_hls_configuration": "ParticipantRecordingHlsConfiguration",
    }

    participant_recording_hls_configuration: Optional[ParticipantRecordingHlsConfiguration] = None


@dataclass
class ParticipantRecordingHlsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_segment_duration_seconds": "TargetSegmentDurationSeconds",
    }

    target_segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ParticipantThumbnailConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_interval_seconds": "TargetIntervalSeconds",
        "storage": "Storage",
        "recording_mode": "RecordingMode",
    }

    target_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    storage: Optional[Union[list[str], Ref]] = None
    recording_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "participant_thumbnail_configuration": "ParticipantThumbnailConfiguration",
    }

    participant_thumbnail_configuration: Optional[ParticipantThumbnailConfiguration] = None

