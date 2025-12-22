"""PropertyTypes for AWS::MediaLive::SdiSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AacCodingMode:
    """AacCodingMode enum values."""

    AD_RECEIVER_MIX = "AD_RECEIVER_MIX"
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_5_1 = "CODING_MODE_5_1"


class AacInputType:
    """AacInputType enum values."""

    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NORMAL = "NORMAL"


class AacProfile:
    """AacProfile enum values."""

    HEV1 = "HEV1"
    HEV2 = "HEV2"
    LC = "LC"


class AacRateControlMode:
    """AacRateControlMode enum values."""

    CBR = "CBR"
    VBR = "VBR"


class AacRawFormat:
    """AacRawFormat enum values."""

    LATM_LOAS = "LATM_LOAS"
    NONE = "NONE"


class AacSpec:
    """AacSpec enum values."""

    MPEG2 = "MPEG2"
    MPEG4 = "MPEG4"


class AacVbrQuality:
    """AacVbrQuality enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    MEDIUM_LOW = "MEDIUM_LOW"


class Ac3AttenuationControl:
    """Ac3AttenuationControl enum values."""

    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Ac3BitstreamMode:
    """Ac3BitstreamMode enum values."""

    COMMENTARY = "COMMENTARY"
    COMPLETE_MAIN = "COMPLETE_MAIN"
    DIALOGUE = "DIALOGUE"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    MUSIC_AND_EFFECTS = "MUSIC_AND_EFFECTS"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"
    VOICE_OVER = "VOICE_OVER"


class Ac3CodingMode:
    """Ac3CodingMode enum values."""

    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2_LFE = "CODING_MODE_3_2_LFE"


class Ac3DrcProfile:
    """Ac3DrcProfile enum values."""

    FILM_STANDARD = "FILM_STANDARD"
    NONE = "NONE"


class Ac3LfeFilter:
    """Ac3LfeFilter enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Ac3MetadataControl:
    """Ac3MetadataControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AcceptHeader:
    """AcceptHeader enum values."""

    IMAGE_JPEG = "image/jpeg"


class AccessibilityType:
    """AccessibilityType enum values."""

    DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES = "DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES"
    IMPLEMENTS_ACCESSIBILITY_FEATURES = "IMPLEMENTS_ACCESSIBILITY_FEATURES"


class AfdSignaling:
    """AfdSignaling enum values."""

    AUTO = "AUTO"
    FIXED = "FIXED"
    NONE = "NONE"


class Algorithm:
    """Algorithm enum values."""

    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"


class ArchiveS3LogUploads:
    """ArchiveS3LogUploads enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AudioDescriptionAudioTypeControl:
    """AudioDescriptionAudioTypeControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioDescriptionLanguageCodeControl:
    """AudioDescriptionLanguageCodeControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioLanguageSelectionPolicy:
    """AudioLanguageSelectionPolicy enum values."""

    LOOSE = "LOOSE"
    STRICT = "STRICT"


class AudioNormalizationAlgorithm:
    """AudioNormalizationAlgorithm enum values."""

    ITU_1770_1 = "ITU_1770_1"
    ITU_1770_2 = "ITU_1770_2"


class AudioNormalizationAlgorithmControl:
    """AudioNormalizationAlgorithmControl enum values."""

    CORRECT_AUDIO = "CORRECT_AUDIO"


class AudioOnlyHlsSegmentType:
    """AudioOnlyHlsSegmentType enum values."""

    AAC = "AAC"
    FMP4 = "FMP4"


class AudioOnlyHlsTrackType:
    """AudioOnlyHlsTrackType enum values."""

    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


class AudioType:
    """AudioType enum values."""

    CLEAN_EFFECTS = "CLEAN_EFFECTS"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    UNDEFINED = "UNDEFINED"
    VISUAL_IMPAIRED_COMMENTARY = "VISUAL_IMPAIRED_COMMENTARY"


class AuthenticationScheme:
    """AuthenticationScheme enum values."""

    AKAMAI = "AKAMAI"
    COMMON = "COMMON"


class Av1GopSizeUnits:
    """Av1GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class Av1Level:
    """Av1Level enum values."""

    AV1_LEVEL_2 = "AV1_LEVEL_2"
    AV1_LEVEL_2_1 = "AV1_LEVEL_2_1"
    AV1_LEVEL_3 = "AV1_LEVEL_3"
    AV1_LEVEL_3_1 = "AV1_LEVEL_3_1"
    AV1_LEVEL_4 = "AV1_LEVEL_4"
    AV1_LEVEL_4_1 = "AV1_LEVEL_4_1"
    AV1_LEVEL_5 = "AV1_LEVEL_5"
    AV1_LEVEL_5_1 = "AV1_LEVEL_5_1"
    AV1_LEVEL_5_2 = "AV1_LEVEL_5_2"
    AV1_LEVEL_5_3 = "AV1_LEVEL_5_3"
    AV1_LEVEL_6 = "AV1_LEVEL_6"
    AV1_LEVEL_6_1 = "AV1_LEVEL_6_1"
    AV1_LEVEL_6_2 = "AV1_LEVEL_6_2"
    AV1_LEVEL_6_3 = "AV1_LEVEL_6_3"
    AV1_LEVEL_AUTO = "AV1_LEVEL_AUTO"


class Av1LookAheadRateControl:
    """Av1LookAheadRateControl enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class Av1RateControlMode:
    """Av1RateControlMode enum values."""

    CBR = "CBR"
    QVBR = "QVBR"


class Av1SceneChangeDetect:
    """Av1SceneChangeDetect enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Av1SpatialAq:
    """Av1SpatialAq enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Av1TemporalAq:
    """Av1TemporalAq enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AvailBlankingState:
    """AvailBlankingState enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BandwidthReductionFilterStrength:
    """BandwidthReductionFilterStrength enum values."""

    AUTO = "AUTO"
    STRENGTH_1 = "STRENGTH_1"
    STRENGTH_2 = "STRENGTH_2"
    STRENGTH_3 = "STRENGTH_3"
    STRENGTH_4 = "STRENGTH_4"


class BandwidthReductionPostFilterSharpening:
    """BandwidthReductionPostFilterSharpening enum values."""

    DISABLED = "DISABLED"
    SHARPENING_1 = "SHARPENING_1"
    SHARPENING_2 = "SHARPENING_2"
    SHARPENING_3 = "SHARPENING_3"


class BlackoutSlateNetworkEndBlackout:
    """BlackoutSlateNetworkEndBlackout enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BlackoutSlateState:
    """BlackoutSlateState enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BurnInAlignment:
    """BurnInAlignment enum values."""

    CENTERED = "CENTERED"
    LEFT = "LEFT"
    SMART = "SMART"


class BurnInBackgroundColor:
    """BurnInBackgroundColor enum values."""

    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class BurnInDestinationSubtitleRows:
    """BurnInDestinationSubtitleRows enum values."""

    ROWS_16 = "ROWS_16"
    ROWS_20 = "ROWS_20"
    ROWS_24 = "ROWS_24"


class BurnInFontColor:
    """BurnInFontColor enum values."""

    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class BurnInOutlineColor:
    """BurnInOutlineColor enum values."""

    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class BurnInShadowColor:
    """BurnInShadowColor enum values."""

    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class BurnInTeletextGridControl:
    """BurnInTeletextGridControl enum values."""

    FIXED = "FIXED"
    SCALED = "SCALED"


class CdiInputResolution:
    """CdiInputResolution enum values."""

    SD = "SD"
    HD = "HD"
    FHD = "FHD"
    UHD = "UHD"


class ChannelAlertState:
    """ChannelAlertState enum values."""

    SET = "SET"
    CLEARED = "CLEARED"


class ChannelClass:
    """ChannelClass enum values."""

    STANDARD = "STANDARD"
    SINGLE_PIPELINE = "SINGLE_PIPELINE"


class ChannelPipelineIdToRestart:
    """ChannelPipelineIdToRestart enum values."""

    PIPELINE_0 = "PIPELINE_0"
    PIPELINE_1 = "PIPELINE_1"


class ChannelPlacementGroupState:
    """ChannelPlacementGroupState enum values."""

    UNASSIGNED = "UNASSIGNED"
    ASSIGNING = "ASSIGNING"
    ASSIGNED = "ASSIGNED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"
    UNASSIGNING = "UNASSIGNING"


class ChannelState:
    """ChannelState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    IDLE = "IDLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    RECOVERING = "RECOVERING"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"


class CloudWatchAlarmTemplateComparisonOperator:
    """CloudWatchAlarmTemplateComparisonOperator enum values."""

    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"


class CloudWatchAlarmTemplateStatistic:
    """CloudWatchAlarmTemplateStatistic enum values."""

    SAMPLECOUNT = "SampleCount"
    AVERAGE = "Average"
    SUM = "Sum"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"


class CloudWatchAlarmTemplateTargetResourceType:
    """CloudWatchAlarmTemplateTargetResourceType enum values."""

    CLOUDFRONT_DISTRIBUTION = "CLOUDFRONT_DISTRIBUTION"
    MEDIALIVE_MULTIPLEX = "MEDIALIVE_MULTIPLEX"
    MEDIALIVE_CHANNEL = "MEDIALIVE_CHANNEL"
    MEDIALIVE_INPUT_DEVICE = "MEDIALIVE_INPUT_DEVICE"
    MEDIAPACKAGE_CHANNEL = "MEDIAPACKAGE_CHANNEL"
    MEDIAPACKAGE_ORIGIN_ENDPOINT = "MEDIAPACKAGE_ORIGIN_ENDPOINT"
    MEDIACONNECT_FLOW = "MEDIACONNECT_FLOW"
    S3_BUCKET = "S3_BUCKET"
    MEDIATAILOR_PLAYBACK_CONFIGURATION = "MEDIATAILOR_PLAYBACK_CONFIGURATION"


class CloudWatchAlarmTemplateTreatMissingData:
    """CloudWatchAlarmTemplateTreatMissingData enum values."""

    NOTBREACHING = "notBreaching"
    BREACHING = "breaching"
    IGNORE = "ignore"
    MISSING = "missing"


class ClusterAlertState:
    """ClusterAlertState enum values."""

    SET = "SET"
    CLEARED = "CLEARED"


class ClusterState:
    """ClusterState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"


class ClusterType:
    """ClusterType enum values."""

    ON_PREMISES = "ON_PREMISES"


class CmafId3Behavior:
    """CmafId3Behavior enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafIngestSegmentLengthUnits:
    """CmafIngestSegmentLengthUnits enum values."""

    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"


class CmafKLVBehavior:
    """CmafKLVBehavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class CmafNielsenId3Behavior:
    """CmafNielsenId3Behavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class CmafTimedMetadataId3Frame:
    """CmafTimedMetadataId3Frame enum values."""

    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class CmafTimedMetadataPassthrough:
    """CmafTimedMetadataPassthrough enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ColorSpace:
    """ColorSpace enum values."""

    HDR10 = "HDR10"
    HLG_2020 = "HLG_2020"
    REC_601 = "REC_601"
    REC_709 = "REC_709"


class ContentType:
    """ContentType enum values."""

    IMAGE_JPEG = "image/jpeg"


class DashRoleAudio:
    """DashRoleAudio enum values."""

    ALTERNATE = "ALTERNATE"
    COMMENTARY = "COMMENTARY"
    DESCRIPTION = "DESCRIPTION"
    DUB = "DUB"
    EMERGENCY = "EMERGENCY"
    ENHANCED_AUDIO_INTELLIGIBILITY = "ENHANCED-AUDIO-INTELLIGIBILITY"
    KARAOKE = "KARAOKE"
    MAIN = "MAIN"
    SUPPLEMENTARY = "SUPPLEMENTARY"


class DashRoleCaption:
    """DashRoleCaption enum values."""

    ALTERNATE = "ALTERNATE"
    CAPTION = "CAPTION"
    COMMENTARY = "COMMENTARY"
    DESCRIPTION = "DESCRIPTION"
    DUB = "DUB"
    EASYREADER = "EASYREADER"
    EMERGENCY = "EMERGENCY"
    FORCED_SUBTITLE = "FORCED-SUBTITLE"
    KARAOKE = "KARAOKE"
    MAIN = "MAIN"
    METADATA = "METADATA"
    SUBTITLE = "SUBTITLE"
    SUPPLEMENTARY = "SUPPLEMENTARY"


class DeviceSettingsSyncState:
    """DeviceSettingsSyncState enum values."""

    SYNCED = "SYNCED"
    SYNCING = "SYNCING"


class DeviceUpdateStatus:
    """DeviceUpdateStatus enum values."""

    UP_TO_DATE = "UP_TO_DATE"
    NOT_UP_TO_DATE = "NOT_UP_TO_DATE"
    UPDATING = "UPDATING"


class DolbyEProgramSelection:
    """DolbyEProgramSelection enum values."""

    ALL_CHANNELS = "ALL_CHANNELS"
    PROGRAM_1 = "PROGRAM_1"
    PROGRAM_2 = "PROGRAM_2"
    PROGRAM_3 = "PROGRAM_3"
    PROGRAM_4 = "PROGRAM_4"
    PROGRAM_5 = "PROGRAM_5"
    PROGRAM_6 = "PROGRAM_6"
    PROGRAM_7 = "PROGRAM_7"
    PROGRAM_8 = "PROGRAM_8"


class DvbDashAccessibility:
    """DvbDashAccessibility enum values."""

    DVBDASH_1_VISUALLY_IMPAIRED = "DVBDASH_1_VISUALLY_IMPAIRED"
    DVBDASH_2_HARD_OF_HEARING = "DVBDASH_2_HARD_OF_HEARING"
    DVBDASH_3_SUPPLEMENTAL_COMMENTARY = "DVBDASH_3_SUPPLEMENTAL_COMMENTARY"
    DVBDASH_4_DIRECTORS_COMMENTARY = "DVBDASH_4_DIRECTORS_COMMENTARY"
    DVBDASH_5_EDUCATIONAL_NOTES = "DVBDASH_5_EDUCATIONAL_NOTES"
    DVBDASH_6_MAIN_PROGRAM = "DVBDASH_6_MAIN_PROGRAM"
    DVBDASH_7_CLEAN_FEED = "DVBDASH_7_CLEAN_FEED"


class DvbSdtOutputSdt:
    """DvbSdtOutputSdt enum values."""

    SDT_FOLLOW = "SDT_FOLLOW"
    SDT_FOLLOW_IF_PRESENT = "SDT_FOLLOW_IF_PRESENT"
    SDT_MANUAL = "SDT_MANUAL"
    SDT_NONE = "SDT_NONE"


class DvbSubDestinationAlignment:
    """DvbSubDestinationAlignment enum values."""

    CENTERED = "CENTERED"
    LEFT = "LEFT"
    SMART = "SMART"


class DvbSubDestinationBackgroundColor:
    """DvbSubDestinationBackgroundColor enum values."""

    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class DvbSubDestinationFontColor:
    """DvbSubDestinationFontColor enum values."""

    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class DvbSubDestinationOutlineColor:
    """DvbSubDestinationOutlineColor enum values."""

    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class DvbSubDestinationShadowColor:
    """DvbSubDestinationShadowColor enum values."""

    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class DvbSubDestinationSubtitleRows:
    """DvbSubDestinationSubtitleRows enum values."""

    ROWS_16 = "ROWS_16"
    ROWS_20 = "ROWS_20"
    ROWS_24 = "ROWS_24"


class DvbSubDestinationTeletextGridControl:
    """DvbSubDestinationTeletextGridControl enum values."""

    FIXED = "FIXED"
    SCALED = "SCALED"


class DvbSubOcrLanguage:
    """DvbSubOcrLanguage enum values."""

    DEU = "DEU"
    ENG = "ENG"
    FRA = "FRA"
    NLD = "NLD"
    POR = "POR"
    SPA = "SPA"


class Eac3AtmosCodingMode:
    """Eac3AtmosCodingMode enum values."""

    CODING_MODE_5_1_4 = "CODING_MODE_5_1_4"
    CODING_MODE_7_1_4 = "CODING_MODE_7_1_4"
    CODING_MODE_9_1_6 = "CODING_MODE_9_1_6"


class Eac3AtmosDrcLine:
    """Eac3AtmosDrcLine enum values."""

    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3AtmosDrcRf:
    """Eac3AtmosDrcRf enum values."""

    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3AttenuationControl:
    """Eac3AttenuationControl enum values."""

    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Eac3BitstreamMode:
    """Eac3BitstreamMode enum values."""

    COMMENTARY = "COMMENTARY"
    COMPLETE_MAIN = "COMPLETE_MAIN"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"


class Eac3CodingMode:
    """Eac3CodingMode enum values."""

    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2 = "CODING_MODE_3_2"


class Eac3DcFilter:
    """Eac3DcFilter enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Eac3DrcLine:
    """Eac3DrcLine enum values."""

    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3DrcRf:
    """Eac3DrcRf enum values."""

    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3LfeControl:
    """Eac3LfeControl enum values."""

    LFE = "LFE"
    NO_LFE = "NO_LFE"


class Eac3LfeFilter:
    """Eac3LfeFilter enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Eac3MetadataControl:
    """Eac3MetadataControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Eac3PassthroughControl:
    """Eac3PassthroughControl enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    WHEN_POSSIBLE = "WHEN_POSSIBLE"


class Eac3PhaseControl:
    """Eac3PhaseControl enum values."""

    NO_SHIFT = "NO_SHIFT"
    SHIFT_90_DEGREES = "SHIFT_90_DEGREES"


class Eac3StereoDownmix:
    """Eac3StereoDownmix enum values."""

    DPL2 = "DPL2"
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    NOT_INDICATED = "NOT_INDICATED"


class Eac3SurroundExMode:
    """Eac3SurroundExMode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    NOT_INDICATED = "NOT_INDICATED"


class Eac3SurroundMode:
    """Eac3SurroundMode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    NOT_INDICATED = "NOT_INDICATED"


class EbuTtDDestinationStyleControl:
    """EbuTtDDestinationStyleControl enum values."""

    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class EbuTtDFillLineGapControl:
    """EbuTtDFillLineGapControl enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class EmbeddedConvert608To708:
    """EmbeddedConvert608To708 enum values."""

    DISABLED = "DISABLED"
    UPCONVERT = "UPCONVERT"


class EmbeddedScte20Detection:
    """EmbeddedScte20Detection enum values."""

    AUTO = "AUTO"
    OFF = "OFF"


class EventBridgeRuleTemplateEventType:
    """EventBridgeRuleTemplateEventType enum values."""

    MEDIALIVE_MULTIPLEX_ALERT = "MEDIALIVE_MULTIPLEX_ALERT"
    MEDIALIVE_MULTIPLEX_STATE_CHANGE = "MEDIALIVE_MULTIPLEX_STATE_CHANGE"
    MEDIALIVE_CHANNEL_ALERT = "MEDIALIVE_CHANNEL_ALERT"
    MEDIALIVE_CHANNEL_INPUT_CHANGE = "MEDIALIVE_CHANNEL_INPUT_CHANGE"
    MEDIALIVE_CHANNEL_STATE_CHANGE = "MEDIALIVE_CHANNEL_STATE_CHANGE"
    MEDIAPACKAGE_INPUT_NOTIFICATION = "MEDIAPACKAGE_INPUT_NOTIFICATION"
    MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION = "MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION"
    MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION = "MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION"
    SIGNAL_MAP_ACTIVE_ALARM = "SIGNAL_MAP_ACTIVE_ALARM"
    MEDIACONNECT_ALERT = "MEDIACONNECT_ALERT"
    MEDIACONNECT_SOURCE_HEALTH = "MEDIACONNECT_SOURCE_HEALTH"
    MEDIACONNECT_OUTPUT_HEALTH = "MEDIACONNECT_OUTPUT_HEALTH"
    MEDIACONNECT_FLOW_STATUS_CHANGE = "MEDIACONNECT_FLOW_STATUS_CHANGE"


class FeatureActivationsInputPrepareScheduleActions:
    """FeatureActivationsInputPrepareScheduleActions enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class FeatureActivationsOutputStaticImageOverlayScheduleActions:
    """FeatureActivationsOutputStaticImageOverlayScheduleActions enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class FecOutputIncludeFec:
    """FecOutputIncludeFec enum values."""

    COLUMN = "COLUMN"
    COLUMN_AND_ROW = "COLUMN_AND_ROW"


class FixedAfd:
    """FixedAfd enum values."""

    AFD_0000 = "AFD_0000"
    AFD_0010 = "AFD_0010"
    AFD_0011 = "AFD_0011"
    AFD_0100 = "AFD_0100"
    AFD_1000 = "AFD_1000"
    AFD_1001 = "AFD_1001"
    AFD_1010 = "AFD_1010"
    AFD_1011 = "AFD_1011"
    AFD_1101 = "AFD_1101"
    AFD_1110 = "AFD_1110"
    AFD_1111 = "AFD_1111"


class Fmp4NielsenId3Behavior:
    """Fmp4NielsenId3Behavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class Fmp4TimedMetadataBehavior:
    """Fmp4TimedMetadataBehavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class FollowPoint:
    """FollowPoint enum values."""

    END = "END"
    START = "START"


class FrameCaptureIntervalUnit:
    """FrameCaptureIntervalUnit enum values."""

    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"


class FrameCaptureS3LogUploads:
    """FrameCaptureS3LogUploads enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class GlobalConfigurationInputEndAction:
    """GlobalConfigurationInputEndAction enum values."""

    NONE = "NONE"
    SWITCH_AND_LOOP_INPUTS = "SWITCH_AND_LOOP_INPUTS"


class GlobalConfigurationLowFramerateInputs:
    """GlobalConfigurationLowFramerateInputs enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class GlobalConfigurationOutputLockingMode:
    """GlobalConfigurationOutputLockingMode enum values."""

    EPOCH_LOCKING = "EPOCH_LOCKING"
    PIPELINE_LOCKING = "PIPELINE_LOCKING"
    DISABLED = "DISABLED"


class GlobalConfigurationOutputTimingSource:
    """GlobalConfigurationOutputTimingSource enum values."""

    INPUT_CLOCK = "INPUT_CLOCK"
    SYSTEM_CLOCK = "SYSTEM_CLOCK"


class H264AdaptiveQuantization:
    """H264AdaptiveQuantization enum values."""

    AUTO = "AUTO"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    LOW = "LOW"
    MAX = "MAX"
    MEDIUM = "MEDIUM"
    OFF = "OFF"


class H264ColorMetadata:
    """H264ColorMetadata enum values."""

    IGNORE = "IGNORE"
    INSERT = "INSERT"


class H264EntropyEncoding:
    """H264EntropyEncoding enum values."""

    CABAC = "CABAC"
    CAVLC = "CAVLC"


class H264FlickerAq:
    """H264FlickerAq enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264ForceFieldPictures:
    """H264ForceFieldPictures enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264FramerateControl:
    """H264FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264GopBReference:
    """H264GopBReference enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264GopSizeUnits:
    """H264GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class H264Level:
    """H264Level enum values."""

    H264_LEVEL_1 = "H264_LEVEL_1"
    H264_LEVEL_1_1 = "H264_LEVEL_1_1"
    H264_LEVEL_1_2 = "H264_LEVEL_1_2"
    H264_LEVEL_1_3 = "H264_LEVEL_1_3"
    H264_LEVEL_2 = "H264_LEVEL_2"
    H264_LEVEL_2_1 = "H264_LEVEL_2_1"
    H264_LEVEL_2_2 = "H264_LEVEL_2_2"
    H264_LEVEL_3 = "H264_LEVEL_3"
    H264_LEVEL_3_1 = "H264_LEVEL_3_1"
    H264_LEVEL_3_2 = "H264_LEVEL_3_2"
    H264_LEVEL_4 = "H264_LEVEL_4"
    H264_LEVEL_4_1 = "H264_LEVEL_4_1"
    H264_LEVEL_4_2 = "H264_LEVEL_4_2"
    H264_LEVEL_5 = "H264_LEVEL_5"
    H264_LEVEL_5_1 = "H264_LEVEL_5_1"
    H264_LEVEL_5_2 = "H264_LEVEL_5_2"
    H264_LEVEL_AUTO = "H264_LEVEL_AUTO"


class H264LookAheadRateControl:
    """H264LookAheadRateControl enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class H264ParControl:
    """H264ParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264Profile:
    """H264Profile enum values."""

    BASELINE = "BASELINE"
    HIGH = "HIGH"
    HIGH_10BIT = "HIGH_10BIT"
    HIGH_422 = "HIGH_422"
    HIGH_422_10BIT = "HIGH_422_10BIT"
    MAIN = "MAIN"


class H264QualityLevel:
    """H264QualityLevel enum values."""

    ENHANCED_QUALITY = "ENHANCED_QUALITY"
    STANDARD_QUALITY = "STANDARD_QUALITY"


class H264RateControlMode:
    """H264RateControlMode enum values."""

    CBR = "CBR"
    MULTIPLEX = "MULTIPLEX"
    QVBR = "QVBR"
    VBR = "VBR"


class H264ScanType:
    """H264ScanType enum values."""

    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class H264SceneChangeDetect:
    """H264SceneChangeDetect enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SpatialAq:
    """H264SpatialAq enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SubGopLength:
    """H264SubGopLength enum values."""

    DYNAMIC = "DYNAMIC"
    FIXED = "FIXED"


class H264Syntax:
    """H264Syntax enum values."""

    DEFAULT = "DEFAULT"
    RP2027 = "RP2027"


class H264TemporalAq:
    """H264TemporalAq enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264TimecodeInsertionBehavior:
    """H264TimecodeInsertionBehavior enum values."""

    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class H265AdaptiveQuantization:
    """H265AdaptiveQuantization enum values."""

    AUTO = "AUTO"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    LOW = "LOW"
    MAX = "MAX"
    MEDIUM = "MEDIUM"
    OFF = "OFF"


class H265AlternativeTransferFunction:
    """H265AlternativeTransferFunction enum values."""

    INSERT = "INSERT"
    OMIT = "OMIT"


class H265ColorMetadata:
    """H265ColorMetadata enum values."""

    IGNORE = "IGNORE"
    INSERT = "INSERT"


class H265Deblocking:
    """H265Deblocking enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265FlickerAq:
    """H265FlickerAq enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265GopBReference:
    """H265GopBReference enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265GopSizeUnits:
    """H265GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class H265Level:
    """H265Level enum values."""

    H265_LEVEL_1 = "H265_LEVEL_1"
    H265_LEVEL_2 = "H265_LEVEL_2"
    H265_LEVEL_2_1 = "H265_LEVEL_2_1"
    H265_LEVEL_3 = "H265_LEVEL_3"
    H265_LEVEL_3_1 = "H265_LEVEL_3_1"
    H265_LEVEL_4 = "H265_LEVEL_4"
    H265_LEVEL_4_1 = "H265_LEVEL_4_1"
    H265_LEVEL_5 = "H265_LEVEL_5"
    H265_LEVEL_5_1 = "H265_LEVEL_5_1"
    H265_LEVEL_5_2 = "H265_LEVEL_5_2"
    H265_LEVEL_6 = "H265_LEVEL_6"
    H265_LEVEL_6_1 = "H265_LEVEL_6_1"
    H265_LEVEL_6_2 = "H265_LEVEL_6_2"
    H265_LEVEL_AUTO = "H265_LEVEL_AUTO"


class H265LookAheadRateControl:
    """H265LookAheadRateControl enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class H265MvOverPictureBoundaries:
    """H265MvOverPictureBoundaries enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265MvTemporalPredictor:
    """H265MvTemporalPredictor enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265Profile:
    """H265Profile enum values."""

    MAIN = "MAIN"
    MAIN_10BIT = "MAIN_10BIT"


class H265RateControlMode:
    """H265RateControlMode enum values."""

    CBR = "CBR"
    MULTIPLEX = "MULTIPLEX"
    QVBR = "QVBR"


class H265ScanType:
    """H265ScanType enum values."""

    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class H265SceneChangeDetect:
    """H265SceneChangeDetect enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265SubGopLength:
    """H265SubGopLength enum values."""

    DYNAMIC = "DYNAMIC"
    FIXED = "FIXED"


class H265Tier:
    """H265Tier enum values."""

    HIGH = "HIGH"
    MAIN = "MAIN"


class H265TilePadding:
    """H265TilePadding enum values."""

    NONE = "NONE"
    PADDED = "PADDED"


class H265TimecodeInsertionBehavior:
    """H265TimecodeInsertionBehavior enum values."""

    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class H265TreeblockSize:
    """H265TreeblockSize enum values."""

    AUTO = "AUTO"
    TREE_SIZE_32X32 = "TREE_SIZE_32X32"


class HlsAdMarkers:
    """HlsAdMarkers enum values."""

    ADOBE = "ADOBE"
    ELEMENTAL = "ELEMENTAL"
    ELEMENTAL_SCTE35 = "ELEMENTAL_SCTE35"


class HlsAkamaiHttpTransferMode:
    """HlsAkamaiHttpTransferMode enum values."""

    CHUNKED = "CHUNKED"
    NON_CHUNKED = "NON_CHUNKED"


class HlsAutoSelect:
    """HlsAutoSelect enum values."""

    NO = "NO"
    OMIT = "OMIT"
    YES = "YES"


class HlsCaptionLanguageSetting:
    """HlsCaptionLanguageSetting enum values."""

    INSERT = "INSERT"
    NONE = "NONE"
    OMIT = "OMIT"


class HlsClientCache:
    """HlsClientCache enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsCodecSpecification:
    """HlsCodecSpecification enum values."""

    RFC_4281 = "RFC_4281"
    RFC_6381 = "RFC_6381"


class HlsDefault:
    """HlsDefault enum values."""

    NO = "NO"
    OMIT = "OMIT"
    YES = "YES"


class HlsDirectoryStructure:
    """HlsDirectoryStructure enum values."""

    SINGLE_DIRECTORY = "SINGLE_DIRECTORY"
    SUBDIRECTORY_PER_STREAM = "SUBDIRECTORY_PER_STREAM"


class HlsDiscontinuityTags:
    """HlsDiscontinuityTags enum values."""

    INSERT = "INSERT"
    NEVER_INSERT = "NEVER_INSERT"


class HlsEncryptionType:
    """HlsEncryptionType enum values."""

    AES128 = "AES128"
    SAMPLE_AES = "SAMPLE_AES"


class HlsH265PackagingType:
    """HlsH265PackagingType enum values."""

    HEV1 = "HEV1"
    HVC1 = "HVC1"


class HlsId3SegmentTaggingState:
    """HlsId3SegmentTaggingState enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsIncompleteSegmentBehavior:
    """HlsIncompleteSegmentBehavior enum values."""

    AUTO = "AUTO"
    SUPPRESS = "SUPPRESS"


class HlsIvInManifest:
    """HlsIvInManifest enum values."""

    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsIvSource:
    """HlsIvSource enum values."""

    EXPLICIT = "EXPLICIT"
    FOLLOWS_SEGMENT_NUMBER = "FOLLOWS_SEGMENT_NUMBER"


class HlsManifestCompression:
    """HlsManifestCompression enum values."""

    GZIP = "GZIP"
    NONE = "NONE"


class HlsManifestDurationFormat:
    """HlsManifestDurationFormat enum values."""

    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class HlsMediaStoreStorageClass:
    """HlsMediaStoreStorageClass enum values."""

    TEMPORAL = "TEMPORAL"


class HlsMode:
    """HlsMode enum values."""

    LIVE = "LIVE"
    VOD = "VOD"


class HlsOutputSelection:
    """HlsOutputSelection enum values."""

    MANIFESTS_AND_SEGMENTS = "MANIFESTS_AND_SEGMENTS"
    SEGMENTS_ONLY = "SEGMENTS_ONLY"
    VARIANT_MANIFESTS_AND_SEGMENTS = "VARIANT_MANIFESTS_AND_SEGMENTS"


class HlsProgramDateTime:
    """HlsProgramDateTime enum values."""

    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsProgramDateTimeClock:
    """HlsProgramDateTimeClock enum values."""

    INITIALIZE_FROM_OUTPUT_TIMECODE = "INITIALIZE_FROM_OUTPUT_TIMECODE"
    SYSTEM_CLOCK = "SYSTEM_CLOCK"


class HlsRedundantManifest:
    """HlsRedundantManifest enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsS3LogUploads:
    """HlsS3LogUploads enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsScte35SourceType:
    """HlsScte35SourceType enum values."""

    MANIFEST = "MANIFEST"
    SEGMENTS = "SEGMENTS"


class HlsSegmentationMode:
    """HlsSegmentationMode enum values."""

    USE_INPUT_SEGMENTATION = "USE_INPUT_SEGMENTATION"
    USE_SEGMENT_DURATION = "USE_SEGMENT_DURATION"


class HlsStreamInfResolution:
    """HlsStreamInfResolution enum values."""

    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsTimedMetadataId3Frame:
    """HlsTimedMetadataId3Frame enum values."""

    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class HlsTsFileMode:
    """HlsTsFileMode enum values."""

    SEGMENTED_FILES = "SEGMENTED_FILES"
    SINGLE_FILE = "SINGLE_FILE"


class HlsWebdavHttpTransferMode:
    """HlsWebdavHttpTransferMode enum values."""

    CHUNKED = "CHUNKED"
    NON_CHUNKED = "NON_CHUNKED"


class IFrameOnlyPlaylistType:
    """IFrameOnlyPlaylistType enum values."""

    DISABLED = "DISABLED"
    STANDARD = "STANDARD"


class IncludeFillerNalUnits:
    """IncludeFillerNalUnits enum values."""

    AUTO = "AUTO"
    DROP = "DROP"
    INCLUDE = "INCLUDE"


class InputClass:
    """InputClass enum values."""

    STANDARD = "STANDARD"
    SINGLE_PIPELINE = "SINGLE_PIPELINE"


class InputCodec:
    """InputCodec enum values."""

    MPEG2 = "MPEG2"
    AVC = "AVC"
    HEVC = "HEVC"


class InputDeblockFilter:
    """InputDeblockFilter enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class InputDenoiseFilter:
    """InputDenoiseFilter enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class InputDeviceActiveInput:
    """InputDeviceActiveInput enum values."""

    HDMI = "HDMI"
    SDI = "SDI"


class InputDeviceCodec:
    """InputDeviceCodec enum values."""

    HEVC = "HEVC"
    AVC = "AVC"


class InputDeviceConfigurableAudioChannelPairProfile:
    """InputDeviceConfigurableAudioChannelPairProfile enum values."""

    DISABLED = "DISABLED"
    VBR_AAC_HHE_16000 = "VBR-AAC_HHE-16000"
    VBR_AAC_HE_64000 = "VBR-AAC_HE-64000"
    VBR_AAC_LC_128000 = "VBR-AAC_LC-128000"
    CBR_AAC_HQ_192000 = "CBR-AAC_HQ-192000"
    CBR_AAC_HQ_256000 = "CBR-AAC_HQ-256000"
    CBR_AAC_HQ_384000 = "CBR-AAC_HQ-384000"
    CBR_AAC_HQ_512000 = "CBR-AAC_HQ-512000"


class InputDeviceConfiguredInput:
    """InputDeviceConfiguredInput enum values."""

    AUTO = "AUTO"
    HDMI = "HDMI"
    SDI = "SDI"


class InputDeviceConnectionState:
    """InputDeviceConnectionState enum values."""

    DISCONNECTED = "DISCONNECTED"
    CONNECTED = "CONNECTED"


class InputDeviceIpScheme:
    """InputDeviceIpScheme enum values."""

    STATIC = "STATIC"
    DHCP = "DHCP"


class InputDeviceOutputType:
    """InputDeviceOutputType enum values."""

    NONE = "NONE"
    MEDIALIVE_INPUT = "MEDIALIVE_INPUT"
    MEDIACONNECT_FLOW = "MEDIACONNECT_FLOW"


class InputDeviceScanType:
    """InputDeviceScanType enum values."""

    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class InputDeviceState:
    """InputDeviceState enum values."""

    IDLE = "IDLE"
    STREAMING = "STREAMING"


class InputDeviceTransferType:
    """InputDeviceTransferType enum values."""

    OUTGOING = "OUTGOING"
    INCOMING = "INCOMING"


class InputDeviceType:
    """InputDeviceType enum values."""

    HD = "HD"
    UHD = "UHD"


class InputDeviceUhdAudioChannelPairProfile:
    """InputDeviceUhdAudioChannelPairProfile enum values."""

    DISABLED = "DISABLED"
    VBR_AAC_HHE_16000 = "VBR-AAC_HHE-16000"
    VBR_AAC_HE_64000 = "VBR-AAC_HE-64000"
    VBR_AAC_LC_128000 = "VBR-AAC_LC-128000"
    CBR_AAC_HQ_192000 = "CBR-AAC_HQ-192000"
    CBR_AAC_HQ_256000 = "CBR-AAC_HQ-256000"
    CBR_AAC_HQ_384000 = "CBR-AAC_HQ-384000"
    CBR_AAC_HQ_512000 = "CBR-AAC_HQ-512000"


class InputFilter:
    """InputFilter enum values."""

    AUTO = "AUTO"
    DISABLED = "DISABLED"
    FORCED = "FORCED"


class InputLossActionForHlsOut:
    """InputLossActionForHlsOut enum values."""

    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForMsSmoothOut:
    """InputLossActionForMsSmoothOut enum values."""

    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForRtmpOut:
    """InputLossActionForRtmpOut enum values."""

    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForUdpOut:
    """InputLossActionForUdpOut enum values."""

    DROP_PROGRAM = "DROP_PROGRAM"
    DROP_TS = "DROP_TS"
    EMIT_PROGRAM = "EMIT_PROGRAM"


class InputLossImageType:
    """InputLossImageType enum values."""

    COLOR = "COLOR"
    SLATE = "SLATE"


class InputMaximumBitrate:
    """InputMaximumBitrate enum values."""

    MAX_10_MBPS = "MAX_10_MBPS"
    MAX_20_MBPS = "MAX_20_MBPS"
    MAX_50_MBPS = "MAX_50_MBPS"


class InputNetworkLocation:
    """InputNetworkLocation enum values."""

    AWS = "AWS"
    ON_PREMISES = "ON_PREMISES"


class InputPreference:
    """InputPreference enum values."""

    EQUAL_INPUT_PREFERENCE = "EQUAL_INPUT_PREFERENCE"
    PRIMARY_INPUT_PREFERRED = "PRIMARY_INPUT_PREFERRED"


class InputResolution:
    """InputResolution enum values."""

    SD = "SD"
    HD = "HD"
    UHD = "UHD"


class InputSecurityGroupState:
    """InputSecurityGroupState enum values."""

    IDLE = "IDLE"
    IN_USE = "IN_USE"
    UPDATING = "UPDATING"
    DELETED = "DELETED"


class InputSourceEndBehavior:
    """InputSourceEndBehavior enum values."""

    CONTINUE = "CONTINUE"
    LOOP = "LOOP"


class InputSourceType:
    """InputSourceType enum values."""

    STATIC = "STATIC"
    DYNAMIC = "DYNAMIC"


class InputState:
    """InputState enum values."""

    CREATING = "CREATING"
    DETACHED = "DETACHED"
    ATTACHED = "ATTACHED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class InputTimecodeSource:
    """InputTimecodeSource enum values."""

    ZEROBASED = "ZEROBASED"
    EMBEDDED = "EMBEDDED"


class InputType:
    """InputType enum values."""

    UDP_PUSH = "UDP_PUSH"
    RTP_PUSH = "RTP_PUSH"
    RTMP_PUSH = "RTMP_PUSH"
    RTMP_PULL = "RTMP_PULL"
    URL_PULL = "URL_PULL"
    MP4_FILE = "MP4_FILE"
    MEDIACONNECT = "MEDIACONNECT"
    INPUT_DEVICE = "INPUT_DEVICE"
    AWS_CDI = "AWS_CDI"
    TS_FILE = "TS_FILE"
    SRT_CALLER = "SRT_CALLER"
    MULTICAST = "MULTICAST"
    SMPTE_2110_RECEIVER_GROUP = "SMPTE_2110_RECEIVER_GROUP"
    SDI = "SDI"
    MEDIACONNECT_ROUTER = "MEDIACONNECT_ROUTER"


class LastFrameClippingBehavior:
    """LastFrameClippingBehavior enum values."""

    EXCLUDE_LAST_FRAME = "EXCLUDE_LAST_FRAME"
    INCLUDE_LAST_FRAME = "INCLUDE_LAST_FRAME"


class LogLevel:
    """LogLevel enum values."""

    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    DISABLED = "DISABLED"


class M2tsAbsentInputAudioBehavior:
    """M2tsAbsentInputAudioBehavior enum values."""

    DROP = "DROP"
    ENCODE_SILENCE = "ENCODE_SILENCE"


class M2tsArib:
    """M2tsArib enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsAribCaptionsPidControl:
    """M2tsAribCaptionsPidControl enum values."""

    AUTO = "AUTO"
    USE_CONFIGURED = "USE_CONFIGURED"


class M2tsAudioBufferModel:
    """M2tsAudioBufferModel enum values."""

    ATSC = "ATSC"
    DVB = "DVB"


class M2tsAudioInterval:
    """M2tsAudioInterval enum values."""

    VIDEO_AND_FIXED_INTERVALS = "VIDEO_AND_FIXED_INTERVALS"
    VIDEO_INTERVAL = "VIDEO_INTERVAL"


class M2tsAudioStreamType:
    """M2tsAudioStreamType enum values."""

    ATSC = "ATSC"
    DVB = "DVB"


class M2tsBufferModel:
    """M2tsBufferModel enum values."""

    MULTIPLEX = "MULTIPLEX"
    NONE = "NONE"


class M2tsCcDescriptor:
    """M2tsCcDescriptor enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsEbifControl:
    """M2tsEbifControl enum values."""

    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsEbpPlacement:
    """M2tsEbpPlacement enum values."""

    VIDEO_AND_AUDIO_PIDS = "VIDEO_AND_AUDIO_PIDS"
    VIDEO_PID = "VIDEO_PID"


class M2tsEsRateInPes:
    """M2tsEsRateInPes enum values."""

    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class M2tsKlv:
    """M2tsKlv enum values."""

    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsNielsenId3Behavior:
    """M2tsNielsenId3Behavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsPcrControl:
    """M2tsPcrControl enum values."""

    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"


class M2tsRateMode:
    """M2tsRateMode enum values."""

    CBR = "CBR"
    VBR = "VBR"


class M2tsScte35Control:
    """M2tsScte35Control enum values."""

    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsSegmentationMarkers:
    """M2tsSegmentationMarkers enum values."""

    EBP = "EBP"
    EBP_LEGACY = "EBP_LEGACY"
    NONE = "NONE"
    PSI_SEGSTART = "PSI_SEGSTART"
    RAI_ADAPT = "RAI_ADAPT"
    RAI_SEGSTART = "RAI_SEGSTART"


class M2tsSegmentationStyle:
    """M2tsSegmentationStyle enum values."""

    MAINTAIN_CADENCE = "MAINTAIN_CADENCE"
    RESET_CADENCE = "RESET_CADENCE"


class M2tsTimedMetadataBehavior:
    """M2tsTimedMetadataBehavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M3u8KlvBehavior:
    """M3u8KlvBehavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M3u8NielsenId3Behavior:
    """M3u8NielsenId3Behavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M3u8PcrControl:
    """M3u8PcrControl enum values."""

    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"


class M3u8Scte35Behavior:
    """M3u8Scte35Behavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M3u8TimedMetadataBehavior:
    """M3u8TimedMetadataBehavior enum values."""

    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class MaintenanceDay:
    """MaintenanceDay enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class MotionGraphicsInsertion:
    """MotionGraphicsInsertion enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mp2CodingMode:
    """Mp2CodingMode enum values."""

    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"


class Mpeg2AdaptiveQuantization:
    """Mpeg2AdaptiveQuantization enum values."""

    AUTO = "AUTO"
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    OFF = "OFF"


class Mpeg2ColorMetadata:
    """Mpeg2ColorMetadata enum values."""

    IGNORE = "IGNORE"
    INSERT = "INSERT"


class Mpeg2ColorSpace:
    """Mpeg2ColorSpace enum values."""

    AUTO = "AUTO"
    PASSTHROUGH = "PASSTHROUGH"


class Mpeg2DisplayRatio:
    """Mpeg2DisplayRatio enum values."""

    DISPLAYRATIO16X9 = "DISPLAYRATIO16X9"
    DISPLAYRATIO4X3 = "DISPLAYRATIO4X3"


class Mpeg2GopSizeUnits:
    """Mpeg2GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class Mpeg2ScanType:
    """Mpeg2ScanType enum values."""

    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class Mpeg2SubGopLength:
    """Mpeg2SubGopLength enum values."""

    DYNAMIC = "DYNAMIC"
    FIXED = "FIXED"


class Mpeg2TimecodeInsertionBehavior:
    """Mpeg2TimecodeInsertionBehavior enum values."""

    DISABLED = "DISABLED"
    GOP_TIMECODE = "GOP_TIMECODE"


class MsSmoothH265PackagingType:
    """MsSmoothH265PackagingType enum values."""

    HEV1 = "HEV1"
    HVC1 = "HVC1"


class MultiplexAlertState:
    """MultiplexAlertState enum values."""

    SET = "SET"
    CLEARED = "CLEARED"


class MultiplexState:
    """MultiplexState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    IDLE = "IDLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    RECOVERING = "RECOVERING"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    DELETED = "DELETED"


class NetworkInputServerValidation:
    """NetworkInputServerValidation enum values."""

    CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME = "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME"
    CHECK_CRYPTOGRAPHY_ONLY = "CHECK_CRYPTOGRAPHY_ONLY"


class NetworkInterfaceMode:
    """NetworkInterfaceMode enum values."""

    NAT = "NAT"
    BRIDGE = "BRIDGE"


class NetworkState:
    """NetworkState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    IDLE = "IDLE"
    IN_USE = "IN_USE"
    UPDATING = "UPDATING"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"


class NielsenPcmToId3TaggingState:
    """NielsenPcmToId3TaggingState enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class NielsenWatermarkTimezones:
    """NielsenWatermarkTimezones enum values."""

    AMERICA_PUERTO_RICO = "AMERICA_PUERTO_RICO"
    US_ALASKA = "US_ALASKA"
    US_ARIZONA = "US_ARIZONA"
    US_CENTRAL = "US_CENTRAL"
    US_EASTERN = "US_EASTERN"
    US_HAWAII = "US_HAWAII"
    US_MOUNTAIN = "US_MOUNTAIN"
    US_PACIFIC = "US_PACIFIC"
    US_SAMOA = "US_SAMOA"
    UTC = "UTC"


class NielsenWatermarksCbetStepaside:
    """NielsenWatermarksCbetStepaside enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class NielsenWatermarksDistributionTypes:
    """NielsenWatermarksDistributionTypes enum values."""

    FINAL_DISTRIBUTOR = "FINAL_DISTRIBUTOR"
    PROGRAM_CONTENT = "PROGRAM_CONTENT"


class NodeConnectionState:
    """NodeConnectionState enum values."""

    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"


class NodeRole:
    """NodeRole enum values."""

    BACKUP = "BACKUP"
    ACTIVE = "ACTIVE"


class NodeState:
    """NodeState enum values."""

    CREATED = "CREATED"
    REGISTERING = "REGISTERING"
    READY_TO_ACTIVATE = "READY_TO_ACTIVATE"
    REGISTRATION_FAILED = "REGISTRATION_FAILED"
    ACTIVATION_FAILED = "ACTIVATION_FAILED"
    ACTIVE = "ACTIVE"
    READY = "READY"
    IN_USE = "IN_USE"
    DEREGISTERING = "DEREGISTERING"
    DRAINING = "DRAINING"
    DEREGISTRATION_FAILED = "DEREGISTRATION_FAILED"
    DEREGISTERED = "DEREGISTERED"


class OfferingDurationUnits:
    """OfferingDurationUnits enum values."""

    MONTHS = "MONTHS"


class OfferingType:
    """OfferingType enum values."""

    NO_UPFRONT = "NO_UPFRONT"


class PipelineId:
    """PipelineId enum values."""

    PIPELINE_0 = "PIPELINE_0"
    PIPELINE_1 = "PIPELINE_1"


class PreferredChannelPipeline:
    """PreferredChannelPipeline enum values."""

    CURRENTLY_ACTIVE = "CURRENTLY_ACTIVE"
    PIPELINE_0 = "PIPELINE_0"
    PIPELINE_1 = "PIPELINE_1"


class RebootInputDeviceForce:
    """RebootInputDeviceForce enum values."""

    NO = "NO"
    YES = "YES"


class ReservationAutomaticRenewal:
    """ReservationAutomaticRenewal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    UNAVAILABLE = "UNAVAILABLE"


class ReservationCodec:
    """ReservationCodec enum values."""

    MPEG2 = "MPEG2"
    AVC = "AVC"
    HEVC = "HEVC"
    AUDIO = "AUDIO"
    LINK = "LINK"
    AV1 = "AV1"


class ReservationMaximumBitrate:
    """ReservationMaximumBitrate enum values."""

    MAX_10_MBPS = "MAX_10_MBPS"
    MAX_20_MBPS = "MAX_20_MBPS"
    MAX_50_MBPS = "MAX_50_MBPS"


class ReservationMaximumFramerate:
    """ReservationMaximumFramerate enum values."""

    MAX_30_FPS = "MAX_30_FPS"
    MAX_60_FPS = "MAX_60_FPS"


class ReservationResolution:
    """ReservationResolution enum values."""

    SD = "SD"
    HD = "HD"
    FHD = "FHD"
    UHD = "UHD"


class ReservationResourceType:
    """ReservationResourceType enum values."""

    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    MULTIPLEX = "MULTIPLEX"
    CHANNEL = "CHANNEL"


class ReservationSpecialFeature:
    """ReservationSpecialFeature enum values."""

    ADVANCED_AUDIO = "ADVANCED_AUDIO"
    AUDIO_NORMALIZATION = "AUDIO_NORMALIZATION"
    MGHD = "MGHD"
    MGUHD = "MGUHD"


class ReservationState:
    """ReservationState enum values."""

    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"


class ReservationVideoQuality:
    """ReservationVideoQuality enum values."""

    STANDARD = "STANDARD"
    ENHANCED = "ENHANCED"
    PREMIUM = "PREMIUM"


class RouterEncryptionType:
    """RouterEncryptionType enum values."""

    AUTOMATIC = "AUTOMATIC"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class RtmpAdMarkers:
    """RtmpAdMarkers enum values."""

    ON_CUE_POINT_SCTE35 = "ON_CUE_POINT_SCTE35"


class RtmpCacheFullBehavior:
    """RtmpCacheFullBehavior enum values."""

    DISCONNECT_IMMEDIATELY = "DISCONNECT_IMMEDIATELY"
    WAIT_FOR_SERVER = "WAIT_FOR_SERVER"


class RtmpCaptionData:
    """RtmpCaptionData enum values."""

    ALL = "ALL"
    FIELD1_608 = "FIELD1_608"
    FIELD1_AND_FIELD2_608 = "FIELD1_AND_FIELD2_608"


class RtmpOutputCertificateMode:
    """RtmpOutputCertificateMode enum values."""

    SELF_SIGNED = "SELF_SIGNED"
    VERIFY_AUTHENTICITY = "VERIFY_AUTHENTICITY"


class S3CannedAcl:
    """S3CannedAcl enum values."""

    AUTHENTICATED_READ = "AUTHENTICATED_READ"
    BUCKET_OWNER_FULL_CONTROL = "BUCKET_OWNER_FULL_CONTROL"
    BUCKET_OWNER_READ = "BUCKET_OWNER_READ"
    PUBLIC_READ = "PUBLIC_READ"


class Scte20Convert608To708:
    """Scte20Convert608To708 enum values."""

    DISABLED = "DISABLED"
    UPCONVERT = "UPCONVERT"


class Scte27OcrLanguage:
    """Scte27OcrLanguage enum values."""

    DEU = "DEU"
    ENG = "ENG"
    FRA = "FRA"
    NLD = "NLD"
    POR = "POR"
    SPA = "SPA"


class Scte35AposNoRegionalBlackoutBehavior:
    """Scte35AposNoRegionalBlackoutBehavior enum values."""

    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35AposWebDeliveryAllowedBehavior:
    """Scte35AposWebDeliveryAllowedBehavior enum values."""

    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35ArchiveAllowedFlag:
    """Scte35ArchiveAllowedFlag enum values."""

    ARCHIVE_NOT_ALLOWED = "ARCHIVE_NOT_ALLOWED"
    ARCHIVE_ALLOWED = "ARCHIVE_ALLOWED"


class Scte35DeviceRestrictions:
    """Scte35DeviceRestrictions enum values."""

    NONE = "NONE"
    RESTRICT_GROUP0 = "RESTRICT_GROUP0"
    RESTRICT_GROUP1 = "RESTRICT_GROUP1"
    RESTRICT_GROUP2 = "RESTRICT_GROUP2"


class Scte35InputMode:
    """Scte35InputMode enum values."""

    FIXED = "FIXED"
    FOLLOW_ACTIVE = "FOLLOW_ACTIVE"


class Scte35NoRegionalBlackoutFlag:
    """Scte35NoRegionalBlackoutFlag enum values."""

    REGIONAL_BLACKOUT = "REGIONAL_BLACKOUT"
    NO_REGIONAL_BLACKOUT = "NO_REGIONAL_BLACKOUT"


class Scte35SegmentationCancelIndicator:
    """Scte35SegmentationCancelIndicator enum values."""

    SEGMENTATION_EVENT_NOT_CANCELED = "SEGMENTATION_EVENT_NOT_CANCELED"
    SEGMENTATION_EVENT_CANCELED = "SEGMENTATION_EVENT_CANCELED"


class Scte35SegmentationScope:
    """Scte35SegmentationScope enum values."""

    ALL_OUTPUT_GROUPS = "ALL_OUTPUT_GROUPS"
    SCTE35_ENABLED_OUTPUT_GROUPS = "SCTE35_ENABLED_OUTPUT_GROUPS"


class Scte35SpliceInsertNoRegionalBlackoutBehavior:
    """Scte35SpliceInsertNoRegionalBlackoutBehavior enum values."""

    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35SpliceInsertWebDeliveryAllowedBehavior:
    """Scte35SpliceInsertWebDeliveryAllowedBehavior enum values."""

    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35Type:
    """Scte35Type enum values."""

    NONE = "NONE"
    SCTE_35_WITHOUT_SEGMENTATION = "SCTE_35_WITHOUT_SEGMENTATION"


class Scte35WebDeliveryAllowedFlag:
    """Scte35WebDeliveryAllowedFlag enum values."""

    WEB_DELIVERY_NOT_ALLOWED = "WEB_DELIVERY_NOT_ALLOWED"
    WEB_DELIVERY_ALLOWED = "WEB_DELIVERY_ALLOWED"


class SdiSourceMode:
    """SdiSourceMode enum values."""

    QUADRANT = "QUADRANT"
    INTERLEAVE = "INTERLEAVE"


class SdiSourceState:
    """SdiSourceState enum values."""

    IDLE = "IDLE"
    IN_USE = "IN_USE"
    DELETED = "DELETED"


class SdiSourceType:
    """SdiSourceType enum values."""

    SINGLE = "SINGLE"
    QUAD = "QUAD"


class SignalMapMonitorDeploymentStatus:
    """SignalMapMonitorDeploymentStatus enum values."""

    NOT_DEPLOYED = "NOT_DEPLOYED"
    DRY_RUN_DEPLOYMENT_COMPLETE = "DRY_RUN_DEPLOYMENT_COMPLETE"
    DRY_RUN_DEPLOYMENT_FAILED = "DRY_RUN_DEPLOYMENT_FAILED"
    DRY_RUN_DEPLOYMENT_IN_PROGRESS = "DRY_RUN_DEPLOYMENT_IN_PROGRESS"
    DEPLOYMENT_COMPLETE = "DEPLOYMENT_COMPLETE"
    DEPLOYMENT_FAILED = "DEPLOYMENT_FAILED"
    DEPLOYMENT_IN_PROGRESS = "DEPLOYMENT_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"


class SignalMapStatus:
    """SignalMapStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_REVERTED = "UPDATE_REVERTED"
    UPDATE_FAILED = "UPDATE_FAILED"
    READY = "READY"
    NOT_READY = "NOT_READY"


class SmoothGroupAudioOnlyTimecodeControl:
    """SmoothGroupAudioOnlyTimecodeControl enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    USE_CONFIGURED_CLOCK = "USE_CONFIGURED_CLOCK"


class SmoothGroupCertificateMode:
    """SmoothGroupCertificateMode enum values."""

    SELF_SIGNED = "SELF_SIGNED"
    VERIFY_AUTHENTICITY = "VERIFY_AUTHENTICITY"


class SmoothGroupEventIdMode:
    """SmoothGroupEventIdMode enum values."""

    NO_EVENT_ID = "NO_EVENT_ID"
    USE_CONFIGURED = "USE_CONFIGURED"
    USE_TIMESTAMP = "USE_TIMESTAMP"


class SmoothGroupEventStopBehavior:
    """SmoothGroupEventStopBehavior enum values."""

    NONE = "NONE"
    SEND_EOS = "SEND_EOS"


class SmoothGroupSegmentationMode:
    """SmoothGroupSegmentationMode enum values."""

    USE_INPUT_SEGMENTATION = "USE_INPUT_SEGMENTATION"
    USE_SEGMENT_DURATION = "USE_SEGMENT_DURATION"


class SmoothGroupSparseTrackType:
    """SmoothGroupSparseTrackType enum values."""

    NONE = "NONE"
    SCTE_35 = "SCTE_35"
    SCTE_35_WITHOUT_SEGMENTATION = "SCTE_35_WITHOUT_SEGMENTATION"


class SmoothGroupStreamManifestBehavior:
    """SmoothGroupStreamManifestBehavior enum values."""

    DO_NOT_SEND = "DO_NOT_SEND"
    SEND = "SEND"


class SmoothGroupTimestampOffsetMode:
    """SmoothGroupTimestampOffsetMode enum values."""

    USE_CONFIGURED_OFFSET = "USE_CONFIGURED_OFFSET"
    USE_EVENT_START_DATE = "USE_EVENT_START_DATE"


class Smpte2038DataPreference:
    """Smpte2038DataPreference enum values."""

    IGNORE = "IGNORE"
    PREFER = "PREFER"


class SrtEncryptionType:
    """SrtEncryptionType enum values."""

    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"


class TemporalFilterPostFilterSharpening:
    """TemporalFilterPostFilterSharpening enum values."""

    AUTO = "AUTO"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class TemporalFilterStrength:
    """TemporalFilterStrength enum values."""

    AUTO = "AUTO"
    STRENGTH_1 = "STRENGTH_1"
    STRENGTH_2 = "STRENGTH_2"
    STRENGTH_3 = "STRENGTH_3"
    STRENGTH_4 = "STRENGTH_4"
    STRENGTH_5 = "STRENGTH_5"
    STRENGTH_6 = "STRENGTH_6"
    STRENGTH_7 = "STRENGTH_7"
    STRENGTH_8 = "STRENGTH_8"
    STRENGTH_9 = "STRENGTH_9"
    STRENGTH_10 = "STRENGTH_10"
    STRENGTH_11 = "STRENGTH_11"
    STRENGTH_12 = "STRENGTH_12"
    STRENGTH_13 = "STRENGTH_13"
    STRENGTH_14 = "STRENGTH_14"
    STRENGTH_15 = "STRENGTH_15"
    STRENGTH_16 = "STRENGTH_16"


class ThumbnailState:
    """ThumbnailState enum values."""

    AUTO = "AUTO"
    DISABLED = "DISABLED"


class ThumbnailType:
    """ThumbnailType enum values."""

    UNSPECIFIED = "UNSPECIFIED"
    CURRENT_ACTIVE = "CURRENT_ACTIVE"


class TimecodeBurninFontSize:
    """TimecodeBurninFontSize enum values."""

    EXTRA_SMALL_10 = "EXTRA_SMALL_10"
    LARGE_48 = "LARGE_48"
    MEDIUM_32 = "MEDIUM_32"
    SMALL_16 = "SMALL_16"


class TimecodeBurninPosition:
    """TimecodeBurninPosition enum values."""

    BOTTOM_CENTER = "BOTTOM_CENTER"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    MIDDLE_CENTER = "MIDDLE_CENTER"
    MIDDLE_LEFT = "MIDDLE_LEFT"
    MIDDLE_RIGHT = "MIDDLE_RIGHT"
    TOP_CENTER = "TOP_CENTER"
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"


class TimecodeConfigSource:
    """TimecodeConfigSource enum values."""

    EMBEDDED = "EMBEDDED"
    SYSTEMCLOCK = "SYSTEMCLOCK"
    ZEROBASED = "ZEROBASED"


class TtmlDestinationStyleControl:
    """TtmlDestinationStyleControl enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    USE_CONFIGURED = "USE_CONFIGURED"


class UdpTimedMetadataId3Frame:
    """UdpTimedMetadataId3Frame enum values."""

    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class UpdateNodeState:
    """UpdateNodeState enum values."""

    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"


class VideoDescriptionRespondToAfd:
    """VideoDescriptionRespondToAfd enum values."""

    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"
    RESPOND = "RESPOND"


class VideoDescriptionScalingBehavior:
    """VideoDescriptionScalingBehavior enum values."""

    DEFAULT = "DEFAULT"
    STRETCH_TO_OUTPUT = "STRETCH_TO_OUTPUT"


class VideoSelectorColorSpace:
    """VideoSelectorColorSpace enum values."""

    FOLLOW = "FOLLOW"
    HDR10 = "HDR10"
    HLG_2020 = "HLG_2020"
    REC_601 = "REC_601"
    REC_709 = "REC_709"


class VideoSelectorColorSpaceUsage:
    """VideoSelectorColorSpaceUsage enum values."""

    FALLBACK = "FALLBACK"
    FORCE = "FORCE"


class WavCodingMode:
    """WavCodingMode enum values."""

    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_4_0 = "CODING_MODE_4_0"
    CODING_MODE_8_0 = "CODING_MODE_8_0"


class WebvttDestinationStyleControl:
    """WebvttDestinationStyleControl enum values."""

    NO_STYLE_DATA = "NO_STYLE_DATA"
    PASSTHROUGH = "PASSTHROUGH"


@dataclass
class Tags(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

