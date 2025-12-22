"""PropertyTypes for AWS::MediaPackage::PackagingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AdMarkers:
    """AdMarkers enum values."""

    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"
    DATERANGE = "DATERANGE"


class AdsOnDeliveryRestrictions:
    """AdsOnDeliveryRestrictions enum values."""

    NONE = "NONE"
    RESTRICTED = "RESTRICTED"
    UNRESTRICTED = "UNRESTRICTED"
    BOTH = "BOTH"


class CmafEncryptionMethod:
    """CmafEncryptionMethod enum values."""

    SAMPLE_AES = "SAMPLE_AES"
    AES_CTR = "AES_CTR"


class EncryptionMethod:
    """EncryptionMethod enum values."""

    AES_128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"


class ManifestLayout:
    """ManifestLayout enum values."""

    FULL = "FULL"
    COMPACT = "COMPACT"
    DRM_TOP_LEVEL_COMPACT = "DRM_TOP_LEVEL_COMPACT"


class Origination:
    """Origination enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class PlaylistType:
    """PlaylistType enum values."""

    NONE = "NONE"
    EVENT = "EVENT"
    VOD = "VOD"


class PresetSpeke20Audio:
    """PresetSpeke20Audio enum values."""

    PRESET_AUDIO_1 = "PRESET-AUDIO-1"
    PRESET_AUDIO_2 = "PRESET-AUDIO-2"
    PRESET_AUDIO_3 = "PRESET-AUDIO-3"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class PresetSpeke20Video:
    """PresetSpeke20Video enum values."""

    PRESET_VIDEO_1 = "PRESET-VIDEO-1"
    PRESET_VIDEO_2 = "PRESET-VIDEO-2"
    PRESET_VIDEO_3 = "PRESET-VIDEO-3"
    PRESET_VIDEO_4 = "PRESET-VIDEO-4"
    PRESET_VIDEO_5 = "PRESET-VIDEO-5"
    PRESET_VIDEO_6 = "PRESET-VIDEO-6"
    PRESET_VIDEO_7 = "PRESET-VIDEO-7"
    PRESET_VIDEO_8 = "PRESET-VIDEO-8"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class Profile:
    """Profile enum values."""

    NONE = "NONE"
    HBBTV_1_5 = "HBBTV_1_5"
    HYBRIDCAST = "HYBRIDCAST"
    DVB_DASH_2014 = "DVB_DASH_2014"


class SegmentTemplateFormat:
    """SegmentTemplateFormat enum values."""

    NUMBER_WITH_TIMELINE = "NUMBER_WITH_TIMELINE"
    TIME_WITH_TIMELINE = "TIME_WITH_TIMELINE"
    NUMBER_WITH_DURATION = "NUMBER_WITH_DURATION"


class Status:
    """Status enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class StreamOrder:
    """StreamOrder enum values."""

    ORIGINAL = "ORIGINAL"
    VIDEO_BITRATE_ASCENDING = "VIDEO_BITRATE_ASCENDING"
    VIDEO_BITRATE_DESCENDING = "VIDEO_BITRATE_DESCENDING"


class UtcTiming:
    """UtcTiming enum values."""

    NONE = "NONE"
    HTTP_HEAD = "HTTP-HEAD"
    HTTP_ISO = "HTTP-ISO"
    HTTP_XSDATE = "HTTP-XSDATE"


class __AdTriggersElement:
    """__AdTriggersElement enum values."""

    SPLICE_INSERT = "SPLICE_INSERT"
    BREAK = "BREAK"
    PROVIDER_ADVERTISEMENT = "PROVIDER_ADVERTISEMENT"
    DISTRIBUTOR_ADVERTISEMENT = "DISTRIBUTOR_ADVERTISEMENT"
    PROVIDER_PLACEMENT_OPPORTUNITY = "PROVIDER_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_PLACEMENT_OPPORTUNITY"
    PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY = "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"


class __PeriodTriggersElement:
    """__PeriodTriggersElement enum values."""

    ADS = "ADS"


@dataclass
class Authorization(PropertyType):
    SECRETS_ROLE_ARN = "SecretsRoleArn"
    CDN_IDENTIFIER_SECRET = "CdnIdentifierSecret"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_role_arn": "SecretsRoleArn",
        "cdn_identifier_secret": "CdnIdentifierSecret",
    }

    secrets_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdn_identifier_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfiguration(PropertyType):
    LOG_GROUP_NAME = "LogGroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_name": "LogGroupName",
    }

    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

