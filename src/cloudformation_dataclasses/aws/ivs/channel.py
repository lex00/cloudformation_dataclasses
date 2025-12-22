"""PropertyTypes for AWS::IVS::Channel."""

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
class MultitrackInputConfiguration(PropertyType):
    MAXIMUM_RESOLUTION = "MaximumResolution"
    POLICY = "Policy"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_resolution": "MaximumResolution",
        "policy": "Policy",
        "enabled": "Enabled",
    }

    maximum_resolution: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

