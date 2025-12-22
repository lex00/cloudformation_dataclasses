"""PropertyTypes for AWS::IVS::Stage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChannelLatencyMode:
    """ChannelLatencyMode enum values."""

    NORMAL = "NORMAL"
    LOW = "LOW"


class ChannelType:
    """ChannelType enum values."""

    BASIC = "BASIC"
    STANDARD = "STANDARD"
    ADVANCED_SD = "ADVANCED_SD"
    ADVANCED_HD = "ADVANCED_HD"


class ContainerFormat:
    """ContainerFormat enum values."""

    TS = "TS"
    FRAGMENTED_MP4 = "FRAGMENTED_MP4"


class MultitrackMaximumResolution:
    """MultitrackMaximumResolution enum values."""

    SD = "SD"
    HD = "HD"
    FULL_HD = "FULL_HD"


class MultitrackPolicy:
    """MultitrackPolicy enum values."""

    ALLOW = "ALLOW"
    REQUIRE = "REQUIRE"


class RecordingConfigurationState:
    """RecordingConfigurationState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"


class RecordingMode:
    """RecordingMode enum values."""

    DISABLED = "DISABLED"
    INTERVAL = "INTERVAL"


class RenditionConfigurationRendition:
    """RenditionConfigurationRendition enum values."""

    SD = "SD"
    HD = "HD"
    FULL_HD = "FULL_HD"
    LOWEST_RESOLUTION = "LOWEST_RESOLUTION"


class RenditionConfigurationRenditionSelection:
    """RenditionConfigurationRenditionSelection enum values."""

    ALL = "ALL"
    NONE = "NONE"
    CUSTOM = "CUSTOM"


class StreamHealth:
    """StreamHealth enum values."""

    HEALTHY = "HEALTHY"
    STARVING = "STARVING"
    UNKNOWN = "UNKNOWN"


class StreamState:
    """StreamState enum values."""

    LIVE = "LIVE"
    OFFLINE = "OFFLINE"


class ThumbnailConfigurationResolution:
    """ThumbnailConfigurationResolution enum values."""

    SD = "SD"
    HD = "HD"
    FULL_HD = "FULL_HD"
    LOWEST_RESOLUTION = "LOWEST_RESOLUTION"


class ThumbnailConfigurationStorage:
    """ThumbnailConfigurationStorage enum values."""

    SEQUENTIAL = "SEQUENTIAL"
    LATEST = "LATEST"


class TranscodePreset:
    """TranscodePreset enum values."""

    HIGHER_BANDWIDTH_DELIVERY = "HIGHER_BANDWIDTH_DELIVERY"
    CONSTRAINED_BANDWIDTH_DELIVERY = "CONSTRAINED_BANDWIDTH_DELIVERY"


@dataclass
class AutoParticipantRecordingConfiguration(PropertyType):
    STORAGE_CONFIGURATION_ARN = "StorageConfigurationArn"
    RECORDING_RECONNECT_WINDOW_SECONDS = "RecordingReconnectWindowSeconds"
    MEDIA_TYPES = "MediaTypes"
    HLS_CONFIGURATION = "HlsConfiguration"
    THUMBNAIL_CONFIGURATION = "ThumbnailConfiguration"

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
    PARTICIPANT_RECORDING_HLS_CONFIGURATION = "ParticipantRecordingHlsConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "participant_recording_hls_configuration": "ParticipantRecordingHlsConfiguration",
    }

    participant_recording_hls_configuration: Optional[ParticipantRecordingHlsConfiguration] = None


@dataclass
class ParticipantRecordingHlsConfiguration(PropertyType):
    TARGET_SEGMENT_DURATION_SECONDS = "TargetSegmentDurationSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_segment_duration_seconds": "TargetSegmentDurationSeconds",
    }

    target_segment_duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ParticipantThumbnailConfiguration(PropertyType):
    TARGET_INTERVAL_SECONDS = "TargetIntervalSeconds"
    STORAGE = "Storage"
    RECORDING_MODE = "RecordingMode"

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
    PARTICIPANT_THUMBNAIL_CONFIGURATION = "ParticipantThumbnailConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "participant_thumbnail_configuration": "ParticipantThumbnailConfiguration",
    }

    participant_thumbnail_configuration: Optional[ParticipantThumbnailConfiguration] = None

