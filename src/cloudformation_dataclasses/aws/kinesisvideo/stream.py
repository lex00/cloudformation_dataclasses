"""PropertyTypes for AWS::KinesisVideo::Stream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class APIName:
    """APIName enum values."""

    PUT_MEDIA = "PUT_MEDIA"
    GET_MEDIA = "GET_MEDIA"
    LIST_FRAGMENTS = "LIST_FRAGMENTS"
    GET_MEDIA_FOR_FRAGMENT_LIST = "GET_MEDIA_FOR_FRAGMENT_LIST"
    GET_HLS_STREAMING_SESSION_URL = "GET_HLS_STREAMING_SESSION_URL"
    GET_DASH_STREAMING_SESSION_URL = "GET_DASH_STREAMING_SESSION_URL"
    GET_CLIP = "GET_CLIP"
    GET_IMAGES = "GET_IMAGES"


class ChannelProtocol:
    """ChannelProtocol enum values."""

    WSS = "WSS"
    HTTPS = "HTTPS"
    WEBRTC = "WEBRTC"


class ChannelRole:
    """ChannelRole enum values."""

    MASTER = "MASTER"
    VIEWER = "VIEWER"


class ChannelType:
    """ChannelType enum values."""

    SINGLE_MASTER = "SINGLE_MASTER"
    FULL_MESH = "FULL_MESH"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    BEGINS_WITH = "BEGINS_WITH"


class ConfigurationStatus:
    """ConfigurationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DefaultStorageTier:
    """DefaultStorageTier enum values."""

    HOT = "HOT"
    WARM = "WARM"


class Format:
    """Format enum values."""

    JPEG = "JPEG"
    PNG = "PNG"


class FormatConfigKey:
    """FormatConfigKey enum values."""

    JPEGQUALITY = "JPEGQuality"


class ImageSelectorType:
    """ImageSelectorType enum values."""

    SERVER_TIMESTAMP = "SERVER_TIMESTAMP"
    PRODUCER_TIMESTAMP = "PRODUCER_TIMESTAMP"


class MediaStorageConfigurationStatus:
    """MediaStorageConfigurationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MediaUriType:
    """MediaUriType enum values."""

    RTSP_URI = "RTSP_URI"
    FILE_URI = "FILE_URI"


class RecorderStatus:
    """RecorderStatus enum values."""

    SUCCESS = "SUCCESS"
    USER_ERROR = "USER_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"


class Status:
    """Status enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"


class StrategyOnFullSize:
    """StrategyOnFullSize enum values."""

    DELETE_OLDEST_MEDIA = "DELETE_OLDEST_MEDIA"
    DENY_NEW_MEDIA = "DENY_NEW_MEDIA"


class SyncStatus:
    """SyncStatus enum values."""

    SYNCING = "SYNCING"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    IN_SYNC = "IN_SYNC"
    SYNC_FAILED = "SYNC_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    DELETING_ACKNOWLEDGED = "DELETING_ACKNOWLEDGED"


class UpdateDataRetentionOperation:
    """UpdateDataRetentionOperation enum values."""

    INCREASE_DATA_RETENTION = "INCREASE_DATA_RETENTION"
    DECREASE_DATA_RETENTION = "DECREASE_DATA_RETENTION"


class UploaderStatus:
    """UploaderStatus enum values."""

    SUCCESS = "SUCCESS"
    USER_ERROR = "USER_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"


@dataclass
class StreamStorageConfiguration(PropertyType):
    DEFAULT_STORAGE_TIER = "DefaultStorageTier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_storage_tier": "DefaultStorageTier",
    }

    default_storage_tier: Optional[Union[str, DefaultStorageTier, Ref, GetAtt, Sub]] = None

