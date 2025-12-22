"""PropertyTypes for AWS::IVS::RecordingConfiguration."""

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
class DestinationConfiguration(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[S3DestinationConfiguration] = None


@dataclass
class RenditionConfiguration(PropertyType):
    RENDITION_SELECTION = "RenditionSelection"
    RENDITIONS = "Renditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rendition_selection": "RenditionSelection",
        "renditions": "Renditions",
    }

    rendition_selection: Optional[Union[str, Ref, GetAtt, Sub]] = None
    renditions: Optional[Union[list[str], Ref]] = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    BUCKET_NAME = "BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    TARGET_INTERVAL_SECONDS = "TargetIntervalSeconds"
    STORAGE = "Storage"
    RECORDING_MODE = "RecordingMode"
    RESOLUTION = "Resolution"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_interval_seconds": "TargetIntervalSeconds",
        "storage": "Storage",
        "recording_mode": "RecordingMode",
        "resolution": "Resolution",
    }

    target_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    storage: Optional[Union[list[str], Ref]] = None
    recording_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resolution: Optional[Union[str, Ref, GetAtt, Sub]] = None

