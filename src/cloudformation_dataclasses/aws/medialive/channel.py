"""PropertyTypes for AWS::MediaLive::Channel."""

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
class AacSettings(PropertyType):
    CODING_MODE = "CodingMode"
    RATE_CONTROL_MODE = "RateControlMode"
    SAMPLE_RATE = "SampleRate"
    INPUT_TYPE = "InputType"
    VBR_QUALITY = "VbrQuality"
    RAW_FORMAT = "RawFormat"
    SPEC = "Spec"
    BITRATE = "Bitrate"
    PROFILE = "Profile"

    _property_mappings: ClassVar[dict[str, str]] = {
        "coding_mode": "CodingMode",
        "rate_control_mode": "RateControlMode",
        "sample_rate": "SampleRate",
        "input_type": "InputType",
        "vbr_quality": "VbrQuality",
        "raw_format": "RawFormat",
        "spec": "Spec",
        "bitrate": "Bitrate",
        "profile": "Profile",
    }

    coding_mode: Optional[Union[str, AacCodingMode, Ref, GetAtt, Sub]] = None
    rate_control_mode: Optional[Union[str, AacRateControlMode, Ref, GetAtt, Sub]] = None
    sample_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    input_type: Optional[Union[str, AacInputType, Ref, GetAtt, Sub]] = None
    vbr_quality: Optional[Union[str, AacVbrQuality, Ref, GetAtt, Sub]] = None
    raw_format: Optional[Union[str, AacRawFormat, Ref, GetAtt, Sub]] = None
    spec: Optional[Union[str, AacSpec, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    profile: Optional[Union[str, AacProfile, Ref, GetAtt, Sub]] = None


@dataclass
class Ac3Settings(PropertyType):
    CODING_MODE = "CodingMode"
    DRC_PROFILE = "DrcProfile"
    METADATA_CONTROL = "MetadataControl"
    DIALNORM = "Dialnorm"
    LFE_FILTER = "LfeFilter"
    BITSTREAM_MODE = "BitstreamMode"
    ATTENUATION_CONTROL = "AttenuationControl"
    BITRATE = "Bitrate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "coding_mode": "CodingMode",
        "drc_profile": "DrcProfile",
        "metadata_control": "MetadataControl",
        "dialnorm": "Dialnorm",
        "lfe_filter": "LfeFilter",
        "bitstream_mode": "BitstreamMode",
        "attenuation_control": "AttenuationControl",
        "bitrate": "Bitrate",
    }

    coding_mode: Optional[Union[str, Ac3CodingMode, Ref, GetAtt, Sub]] = None
    drc_profile: Optional[Union[str, Ac3DrcProfile, Ref, GetAtt, Sub]] = None
    metadata_control: Optional[Union[str, Ac3MetadataControl, Ref, GetAtt, Sub]] = None
    dialnorm: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lfe_filter: Optional[Union[str, Ac3LfeFilter, Ref, GetAtt, Sub]] = None
    bitstream_mode: Optional[Union[str, Ac3BitstreamMode, Ref, GetAtt, Sub]] = None
    attenuation_control: Optional[Union[str, Ac3AttenuationControl, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class AdditionalDestinations(PropertyType):
    DESTINATION = "Destination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
    }

    destination: Optional[OutputLocationRef] = None


@dataclass
class AncillarySourceSettings(PropertyType):
    SOURCE_ANCILLARY_CHANNEL_NUMBER = "SourceAncillaryChannelNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_ancillary_channel_number": "SourceAncillaryChannelNumber",
    }

    source_ancillary_channel_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AnywhereSettings(PropertyType):
    CHANNEL_PLACEMENT_GROUP_ID = "ChannelPlacementGroupId"
    CLUSTER_ID = "ClusterId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_placement_group_id": "ChannelPlacementGroupId",
        "cluster_id": "ClusterId",
    }

    channel_placement_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cluster_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArchiveCdnSettings(PropertyType):
    ARCHIVE_S3_SETTINGS = "ArchiveS3Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "archive_s3_settings": "ArchiveS3Settings",
    }

    archive_s3_settings: Optional[ArchiveS3Settings] = None


@dataclass
class ArchiveContainerSettings(PropertyType):
    RAW_SETTINGS = "RawSettings"
    M2TS_SETTINGS = "M2tsSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "raw_settings": "RawSettings",
        "m2ts_settings": "M2tsSettings",
    }

    raw_settings: Optional[RawSettings] = None
    m2ts_settings: Optional[M2tsSettings] = None


@dataclass
class ArchiveGroupSettings(PropertyType):
    DESTINATION = "Destination"
    ARCHIVE_CDN_SETTINGS = "ArchiveCdnSettings"
    ROLLOVER_INTERVAL = "RolloverInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "archive_cdn_settings": "ArchiveCdnSettings",
        "rollover_interval": "RolloverInterval",
    }

    destination: Optional[OutputLocationRef] = None
    archive_cdn_settings: Optional[ArchiveCdnSettings] = None
    rollover_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ArchiveOutputSettings(PropertyType):
    EXTENSION = "Extension"
    NAME_MODIFIER = "NameModifier"
    CONTAINER_SETTINGS = "ContainerSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "extension": "Extension",
        "name_modifier": "NameModifier",
        "container_settings": "ContainerSettings",
    }

    extension: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_settings: Optional[ArchiveContainerSettings] = None


@dataclass
class ArchiveS3Settings(PropertyType):
    CANNED_ACL = "CannedAcl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canned_acl": "CannedAcl",
    }

    canned_acl: Optional[Union[str, S3CannedAcl, Ref, GetAtt, Sub]] = None


@dataclass
class AribDestinationSettings(PropertyType):
    pass


@dataclass
class AribSourceSettings(PropertyType):
    pass


@dataclass
class AudioChannelMapping(PropertyType):
    OUTPUT_CHANNEL = "OutputChannel"
    INPUT_CHANNEL_LEVELS = "InputChannelLevels"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_channel": "OutputChannel",
        "input_channel_levels": "InputChannelLevels",
    }

    output_channel: Optional[Union[int, Ref, GetAtt, Sub]] = None
    input_channel_levels: Optional[list[InputChannelLevel]] = None


@dataclass
class AudioCodecSettings(PropertyType):
    EAC3_SETTINGS = "Eac3Settings"
    AC3_SETTINGS = "Ac3Settings"
    MP2_SETTINGS = "Mp2Settings"
    EAC3_ATMOS_SETTINGS = "Eac3AtmosSettings"
    PASS_THROUGH_SETTINGS = "PassThroughSettings"
    WAV_SETTINGS = "WavSettings"
    AAC_SETTINGS = "AacSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "eac3_settings": "Eac3Settings",
        "ac3_settings": "Ac3Settings",
        "mp2_settings": "Mp2Settings",
        "eac3_atmos_settings": "Eac3AtmosSettings",
        "pass_through_settings": "PassThroughSettings",
        "wav_settings": "WavSettings",
        "aac_settings": "AacSettings",
    }

    eac3_settings: Optional[Eac3Settings] = None
    ac3_settings: Optional[Ac3Settings] = None
    mp2_settings: Optional[Mp2Settings] = None
    eac3_atmos_settings: Optional[Eac3AtmosSettings] = None
    pass_through_settings: Optional[PassThroughSettings] = None
    wav_settings: Optional[WavSettings] = None
    aac_settings: Optional[AacSettings] = None


@dataclass
class AudioDescription(PropertyType):
    AUDIO_DASH_ROLES = "AudioDashRoles"
    LANGUAGE_CODE_CONTROL = "LanguageCodeControl"
    CODEC_SETTINGS = "CodecSettings"
    NAME = "Name"
    AUDIO_WATERMARKING_SETTINGS = "AudioWatermarkingSettings"
    AUDIO_NORMALIZATION_SETTINGS = "AudioNormalizationSettings"
    LANGUAGE_CODE = "LanguageCode"
    REMIX_SETTINGS = "RemixSettings"
    AUDIO_SELECTOR_NAME = "AudioSelectorName"
    STREAM_NAME = "StreamName"
    DVB_DASH_ACCESSIBILITY = "DvbDashAccessibility"
    AUDIO_TYPE = "AudioType"
    AUDIO_TYPE_CONTROL = "AudioTypeControl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_dash_roles": "AudioDashRoles",
        "language_code_control": "LanguageCodeControl",
        "codec_settings": "CodecSettings",
        "name": "Name",
        "audio_watermarking_settings": "AudioWatermarkingSettings",
        "audio_normalization_settings": "AudioNormalizationSettings",
        "language_code": "LanguageCode",
        "remix_settings": "RemixSettings",
        "audio_selector_name": "AudioSelectorName",
        "stream_name": "StreamName",
        "dvb_dash_accessibility": "DvbDashAccessibility",
        "audio_type": "AudioType",
        "audio_type_control": "AudioTypeControl",
    }

    audio_dash_roles: Optional[Union[list[str], Ref]] = None
    language_code_control: Optional[Union[str, AudioDescriptionLanguageCodeControl, Ref, GetAtt, Sub]] = None
    codec_settings: Optional[AudioCodecSettings] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_watermarking_settings: Optional[AudioWatermarkSettings] = None
    audio_normalization_settings: Optional[AudioNormalizationSettings] = None
    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remix_settings: Optional[RemixSettings] = None
    audio_selector_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dvb_dash_accessibility: Optional[Union[str, DvbDashAccessibility, Ref, GetAtt, Sub]] = None
    audio_type: Optional[Union[str, AudioType, Ref, GetAtt, Sub]] = None
    audio_type_control: Optional[Union[str, AudioDescriptionAudioTypeControl, Ref, GetAtt, Sub]] = None


@dataclass
class AudioDolbyEDecode(PropertyType):
    PROGRAM_SELECTION = "ProgramSelection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "program_selection": "ProgramSelection",
    }

    program_selection: Optional[Union[str, DolbyEProgramSelection, Ref, GetAtt, Sub]] = None


@dataclass
class AudioHlsRenditionSelection(PropertyType):
    GROUP_ID = "GroupId"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_id": "GroupId",
        "name": "Name",
    }

    group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AudioLanguageSelection(PropertyType):
    LANGUAGE_CODE = "LanguageCode"
    LANGUAGE_SELECTION_POLICY = "LanguageSelectionPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language_code": "LanguageCode",
        "language_selection_policy": "LanguageSelectionPolicy",
    }

    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    language_selection_policy: Optional[Union[str, AudioLanguageSelectionPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class AudioNormalizationSettings(PropertyType):
    TARGET_LKFS = "TargetLkfs"
    ALGORITHM = "Algorithm"
    ALGORITHM_CONTROL = "AlgorithmControl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_lkfs": "TargetLkfs",
        "algorithm": "Algorithm",
        "algorithm_control": "AlgorithmControl",
    }

    target_lkfs: Optional[Union[float, Ref, GetAtt, Sub]] = None
    algorithm: Optional[Union[str, AudioNormalizationAlgorithm, Ref, GetAtt, Sub]] = None
    algorithm_control: Optional[Union[str, AudioNormalizationAlgorithmControl, Ref, GetAtt, Sub]] = None


@dataclass
class AudioOnlyHlsSettings(PropertyType):
    SEGMENT_TYPE = "SegmentType"
    AUDIO_TRACK_TYPE = "AudioTrackType"
    AUDIO_ONLY_IMAGE = "AudioOnlyImage"
    AUDIO_GROUP_ID = "AudioGroupId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_type": "SegmentType",
        "audio_track_type": "AudioTrackType",
        "audio_only_image": "AudioOnlyImage",
        "audio_group_id": "AudioGroupId",
    }

    segment_type: Optional[Union[str, AudioOnlyHlsSegmentType, Ref, GetAtt, Sub]] = None
    audio_track_type: Optional[Union[str, AudioOnlyHlsTrackType, Ref, GetAtt, Sub]] = None
    audio_only_image: Optional[InputLocation] = None
    audio_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AudioPidSelection(PropertyType):
    PID = "Pid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pid": "Pid",
    }

    pid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AudioSelector(PropertyType):
    SELECTOR_SETTINGS = "SelectorSettings"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "selector_settings": "SelectorSettings",
        "name": "Name",
    }

    selector_settings: Optional[AudioSelectorSettings] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AudioSelectorSettings(PropertyType):
    AUDIO_PID_SELECTION = "AudioPidSelection"
    AUDIO_LANGUAGE_SELECTION = "AudioLanguageSelection"
    AUDIO_TRACK_SELECTION = "AudioTrackSelection"
    AUDIO_HLS_RENDITION_SELECTION = "AudioHlsRenditionSelection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_pid_selection": "AudioPidSelection",
        "audio_language_selection": "AudioLanguageSelection",
        "audio_track_selection": "AudioTrackSelection",
        "audio_hls_rendition_selection": "AudioHlsRenditionSelection",
    }

    audio_pid_selection: Optional[AudioPidSelection] = None
    audio_language_selection: Optional[AudioLanguageSelection] = None
    audio_track_selection: Optional[AudioTrackSelection] = None
    audio_hls_rendition_selection: Optional[AudioHlsRenditionSelection] = None


@dataclass
class AudioSilenceFailoverSettings(PropertyType):
    AUDIO_SELECTOR_NAME = "AudioSelectorName"
    AUDIO_SILENCE_THRESHOLD_MSEC = "AudioSilenceThresholdMsec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_selector_name": "AudioSelectorName",
        "audio_silence_threshold_msec": "AudioSilenceThresholdMsec",
    }

    audio_selector_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_silence_threshold_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AudioTrack(PropertyType):
    TRACK = "Track"

    _property_mappings: ClassVar[dict[str, str]] = {
        "track": "Track",
    }

    track: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AudioTrackSelection(PropertyType):
    DOLBY_E_DECODE = "DolbyEDecode"
    TRACKS = "Tracks"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dolby_e_decode": "DolbyEDecode",
        "tracks": "Tracks",
    }

    dolby_e_decode: Optional[AudioDolbyEDecode] = None
    tracks: Optional[list[AudioTrack]] = None


@dataclass
class AudioWatermarkSettings(PropertyType):
    NIELSEN_WATERMARKS_SETTINGS = "NielsenWatermarksSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "nielsen_watermarks_settings": "NielsenWatermarksSettings",
    }

    nielsen_watermarks_settings: Optional[NielsenWatermarksSettings] = None


@dataclass
class AutomaticInputFailoverSettings(PropertyType):
    FAILOVER_CONDITIONS = "FailoverConditions"
    INPUT_PREFERENCE = "InputPreference"
    SECONDARY_INPUT_ID = "SecondaryInputId"
    ERROR_CLEAR_TIME_MSEC = "ErrorClearTimeMsec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "failover_conditions": "FailoverConditions",
        "input_preference": "InputPreference",
        "secondary_input_id": "SecondaryInputId",
        "error_clear_time_msec": "ErrorClearTimeMsec",
    }

    failover_conditions: Optional[list[FailoverCondition]] = None
    input_preference: Optional[Union[str, InputPreference, Ref, GetAtt, Sub]] = None
    secondary_input_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_clear_time_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Av1ColorSpaceSettings(PropertyType):
    REC601_SETTINGS = "Rec601Settings"
    REC709_SETTINGS = "Rec709Settings"
    COLOR_SPACE_PASSTHROUGH_SETTINGS = "ColorSpacePassthroughSettings"
    HDR10_SETTINGS = "Hdr10Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rec601_settings": "Rec601Settings",
        "rec709_settings": "Rec709Settings",
        "color_space_passthrough_settings": "ColorSpacePassthroughSettings",
        "hdr10_settings": "Hdr10Settings",
    }

    rec601_settings: Optional[Rec601Settings] = None
    rec709_settings: Optional[Rec709Settings] = None
    color_space_passthrough_settings: Optional[ColorSpacePassthroughSettings] = None
    hdr10_settings: Optional[Hdr10Settings] = None


@dataclass
class Av1Settings(PropertyType):
    TIMECODE_BURNIN_SETTINGS = "TimecodeBurninSettings"
    COLOR_SPACE_SETTINGS = "ColorSpaceSettings"
    SPATIAL_AQ = "SpatialAq"
    TEMPORAL_AQ = "TemporalAq"
    QVBR_QUALITY_LEVEL = "QvbrQualityLevel"
    PAR_DENOMINATOR = "ParDenominator"
    FIXED_AFD = "FixedAfd"
    GOP_SIZE_UNITS = "GopSizeUnits"
    FRAMERATE_NUMERATOR = "FramerateNumerator"
    AFD_SIGNALING = "AfdSignaling"
    BITRATE = "Bitrate"
    PAR_NUMERATOR = "ParNumerator"
    RATE_CONTROL_MODE = "RateControlMode"
    BUF_SIZE = "BufSize"
    MIN_BITRATE = "MinBitrate"
    MIN_I_INTERVAL = "MinIInterval"
    SCENE_CHANGE_DETECT = "SceneChangeDetect"
    FRAMERATE_DENOMINATOR = "FramerateDenominator"
    LOOK_AHEAD_RATE_CONTROL = "LookAheadRateControl"
    LEVEL = "Level"
    MAX_BITRATE = "MaxBitrate"
    GOP_SIZE = "GopSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timecode_burnin_settings": "TimecodeBurninSettings",
        "color_space_settings": "ColorSpaceSettings",
        "spatial_aq": "SpatialAq",
        "temporal_aq": "TemporalAq",
        "qvbr_quality_level": "QvbrQualityLevel",
        "par_denominator": "ParDenominator",
        "fixed_afd": "FixedAfd",
        "gop_size_units": "GopSizeUnits",
        "framerate_numerator": "FramerateNumerator",
        "afd_signaling": "AfdSignaling",
        "bitrate": "Bitrate",
        "par_numerator": "ParNumerator",
        "rate_control_mode": "RateControlMode",
        "buf_size": "BufSize",
        "min_bitrate": "MinBitrate",
        "min_i_interval": "MinIInterval",
        "scene_change_detect": "SceneChangeDetect",
        "framerate_denominator": "FramerateDenominator",
        "look_ahead_rate_control": "LookAheadRateControl",
        "level": "Level",
        "max_bitrate": "MaxBitrate",
        "gop_size": "GopSize",
    }

    timecode_burnin_settings: Optional[TimecodeBurninSettings] = None
    color_space_settings: Optional[Av1ColorSpaceSettings] = None
    spatial_aq: Optional[Union[str, Av1SpatialAq, Ref, GetAtt, Sub]] = None
    temporal_aq: Optional[Union[str, Av1TemporalAq, Ref, GetAtt, Sub]] = None
    qvbr_quality_level: Optional[Union[int, Ref, GetAtt, Sub]] = None
    par_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    fixed_afd: Optional[Union[str, FixedAfd, Ref, GetAtt, Sub]] = None
    gop_size_units: Optional[Union[str, Av1GopSizeUnits, Ref, GetAtt, Sub]] = None
    framerate_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    afd_signaling: Optional[Union[str, AfdSignaling, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    par_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rate_control_mode: Optional[Union[str, Av1RateControlMode, Ref, GetAtt, Sub]] = None
    buf_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_i_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scene_change_detect: Optional[Union[str, Av1SceneChangeDetect, Ref, GetAtt, Sub]] = None
    framerate_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    look_ahead_rate_control: Optional[Union[str, Av1LookAheadRateControl, Ref, GetAtt, Sub]] = None
    level: Optional[Union[str, Av1Level, Ref, GetAtt, Sub]] = None
    max_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_size: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class AvailBlanking(PropertyType):
    STATE = "State"
    AVAIL_BLANKING_IMAGE = "AvailBlankingImage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "avail_blanking_image": "AvailBlankingImage",
    }

    state: Optional[Union[str, AvailBlankingState, Ref, GetAtt, Sub]] = None
    avail_blanking_image: Optional[InputLocation] = None


@dataclass
class AvailConfiguration(PropertyType):
    AVAIL_SETTINGS = "AvailSettings"
    SCTE35_SEGMENTATION_SCOPE = "Scte35SegmentationScope"

    _property_mappings: ClassVar[dict[str, str]] = {
        "avail_settings": "AvailSettings",
        "scte35_segmentation_scope": "Scte35SegmentationScope",
    }

    avail_settings: Optional[AvailSettings] = None
    scte35_segmentation_scope: Optional[Union[str, Scte35SegmentationScope, Ref, GetAtt, Sub]] = None


@dataclass
class AvailSettings(PropertyType):
    SCTE35_SPLICE_INSERT = "Scte35SpliceInsert"
    SCTE35_TIME_SIGNAL_APOS = "Scte35TimeSignalApos"
    ESAM = "Esam"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scte35_splice_insert": "Scte35SpliceInsert",
        "scte35_time_signal_apos": "Scte35TimeSignalApos",
        "esam": "Esam",
    }

    scte35_splice_insert: Optional[Scte35SpliceInsert] = None
    scte35_time_signal_apos: Optional[Scte35TimeSignalApos] = None
    esam: Optional[Esam] = None


@dataclass
class BandwidthReductionFilterSettings(PropertyType):
    POST_FILTER_SHARPENING = "PostFilterSharpening"
    STRENGTH = "Strength"

    _property_mappings: ClassVar[dict[str, str]] = {
        "post_filter_sharpening": "PostFilterSharpening",
        "strength": "Strength",
    }

    post_filter_sharpening: Optional[Union[str, BandwidthReductionPostFilterSharpening, Ref, GetAtt, Sub]] = None
    strength: Optional[Union[str, BandwidthReductionFilterStrength, Ref, GetAtt, Sub]] = None


@dataclass
class BlackoutSlate(PropertyType):
    NETWORK_END_BLACKOUT = "NetworkEndBlackout"
    STATE = "State"
    NETWORK_ID = "NetworkId"
    NETWORK_END_BLACKOUT_IMAGE = "NetworkEndBlackoutImage"
    BLACKOUT_SLATE_IMAGE = "BlackoutSlateImage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_end_blackout": "NetworkEndBlackout",
        "state": "State",
        "network_id": "NetworkId",
        "network_end_blackout_image": "NetworkEndBlackoutImage",
        "blackout_slate_image": "BlackoutSlateImage",
    }

    network_end_blackout: Optional[Union[str, BlackoutSlateNetworkEndBlackout, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, BlackoutSlateState, Ref, GetAtt, Sub]] = None
    network_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_end_blackout_image: Optional[InputLocation] = None
    blackout_slate_image: Optional[InputLocation] = None


@dataclass
class BurnInDestinationSettings(PropertyType):
    BACKGROUND_OPACITY = "BackgroundOpacity"
    FONT_RESOLUTION = "FontResolution"
    OUTLINE_COLOR = "OutlineColor"
    FONT_COLOR = "FontColor"
    SHADOW_COLOR = "ShadowColor"
    SHADOW_OPACITY = "ShadowOpacity"
    FONT = "Font"
    SHADOW_Y_OFFSET = "ShadowYOffset"
    ALIGNMENT = "Alignment"
    X_POSITION = "XPosition"
    FONT_SIZE = "FontSize"
    Y_POSITION = "YPosition"
    OUTLINE_SIZE = "OutlineSize"
    TELETEXT_GRID_CONTROL = "TeletextGridControl"
    SUBTITLE_ROWS = "SubtitleRows"
    FONT_OPACITY = "FontOpacity"
    SHADOW_X_OFFSET = "ShadowXOffset"
    BACKGROUND_COLOR = "BackgroundColor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "background_opacity": "BackgroundOpacity",
        "font_resolution": "FontResolution",
        "outline_color": "OutlineColor",
        "font_color": "FontColor",
        "shadow_color": "ShadowColor",
        "shadow_opacity": "ShadowOpacity",
        "font": "Font",
        "shadow_y_offset": "ShadowYOffset",
        "alignment": "Alignment",
        "x_position": "XPosition",
        "font_size": "FontSize",
        "y_position": "YPosition",
        "outline_size": "OutlineSize",
        "teletext_grid_control": "TeletextGridControl",
        "subtitle_rows": "SubtitleRows",
        "font_opacity": "FontOpacity",
        "shadow_x_offset": "ShadowXOffset",
        "background_color": "BackgroundColor",
    }

    background_opacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    font_resolution: Optional[Union[int, Ref, GetAtt, Sub]] = None
    outline_color: Optional[Union[str, BurnInOutlineColor, Ref, GetAtt, Sub]] = None
    font_color: Optional[Union[str, BurnInFontColor, Ref, GetAtt, Sub]] = None
    shadow_color: Optional[Union[str, BurnInShadowColor, Ref, GetAtt, Sub]] = None
    shadow_opacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    font: Optional[InputLocation] = None
    shadow_y_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    alignment: Optional[Union[str, BurnInAlignment, Ref, GetAtt, Sub]] = None
    x_position: Optional[Union[int, Ref, GetAtt, Sub]] = None
    font_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    y_position: Optional[Union[int, Ref, GetAtt, Sub]] = None
    outline_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    teletext_grid_control: Optional[Union[str, BurnInTeletextGridControl, Ref, GetAtt, Sub]] = None
    subtitle_rows: Optional[Union[str, BurnInDestinationSubtitleRows, Ref, GetAtt, Sub]] = None
    font_opacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    shadow_x_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, BurnInBackgroundColor, Ref, GetAtt, Sub]] = None


@dataclass
class CaptionDescription(PropertyType):
    DESTINATION_SETTINGS = "DestinationSettings"
    LANGUAGE_CODE = "LanguageCode"
    LANGUAGE_DESCRIPTION = "LanguageDescription"
    ACCESSIBILITY = "Accessibility"
    DVB_DASH_ACCESSIBILITY = "DvbDashAccessibility"
    CAPTION_SELECTOR_NAME = "CaptionSelectorName"
    CAPTION_DASH_ROLES = "CaptionDashRoles"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_settings": "DestinationSettings",
        "language_code": "LanguageCode",
        "language_description": "LanguageDescription",
        "accessibility": "Accessibility",
        "dvb_dash_accessibility": "DvbDashAccessibility",
        "caption_selector_name": "CaptionSelectorName",
        "caption_dash_roles": "CaptionDashRoles",
        "name": "Name",
    }

    destination_settings: Optional[CaptionDestinationSettings] = None
    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    language_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    accessibility: Optional[Union[str, AccessibilityType, Ref, GetAtt, Sub]] = None
    dvb_dash_accessibility: Optional[Union[str, DvbDashAccessibility, Ref, GetAtt, Sub]] = None
    caption_selector_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    caption_dash_roles: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CaptionDestinationSettings(PropertyType):
    ARIB_DESTINATION_SETTINGS = "AribDestinationSettings"
    EBU_TT_D_DESTINATION_SETTINGS = "EbuTtDDestinationSettings"
    SMPTE_TT_DESTINATION_SETTINGS = "SmpteTtDestinationSettings"
    EMBEDDED_PLUS_SCTE20_DESTINATION_SETTINGS = "EmbeddedPlusScte20DestinationSettings"
    TTML_DESTINATION_SETTINGS = "TtmlDestinationSettings"
    SCTE20_PLUS_EMBEDDED_DESTINATION_SETTINGS = "Scte20PlusEmbeddedDestinationSettings"
    DVB_SUB_DESTINATION_SETTINGS = "DvbSubDestinationSettings"
    TELETEXT_DESTINATION_SETTINGS = "TeletextDestinationSettings"
    BURN_IN_DESTINATION_SETTINGS = "BurnInDestinationSettings"
    WEBVTT_DESTINATION_SETTINGS = "WebvttDestinationSettings"
    EMBEDDED_DESTINATION_SETTINGS = "EmbeddedDestinationSettings"
    RTMP_CAPTION_INFO_DESTINATION_SETTINGS = "RtmpCaptionInfoDestinationSettings"
    SCTE27_DESTINATION_SETTINGS = "Scte27DestinationSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arib_destination_settings": "AribDestinationSettings",
        "ebu_tt_d_destination_settings": "EbuTtDDestinationSettings",
        "smpte_tt_destination_settings": "SmpteTtDestinationSettings",
        "embedded_plus_scte20_destination_settings": "EmbeddedPlusScte20DestinationSettings",
        "ttml_destination_settings": "TtmlDestinationSettings",
        "scte20_plus_embedded_destination_settings": "Scte20PlusEmbeddedDestinationSettings",
        "dvb_sub_destination_settings": "DvbSubDestinationSettings",
        "teletext_destination_settings": "TeletextDestinationSettings",
        "burn_in_destination_settings": "BurnInDestinationSettings",
        "webvtt_destination_settings": "WebvttDestinationSettings",
        "embedded_destination_settings": "EmbeddedDestinationSettings",
        "rtmp_caption_info_destination_settings": "RtmpCaptionInfoDestinationSettings",
        "scte27_destination_settings": "Scte27DestinationSettings",
    }

    arib_destination_settings: Optional[AribDestinationSettings] = None
    ebu_tt_d_destination_settings: Optional[EbuTtDDestinationSettings] = None
    smpte_tt_destination_settings: Optional[SmpteTtDestinationSettings] = None
    embedded_plus_scte20_destination_settings: Optional[EmbeddedPlusScte20DestinationSettings] = None
    ttml_destination_settings: Optional[TtmlDestinationSettings] = None
    scte20_plus_embedded_destination_settings: Optional[Scte20PlusEmbeddedDestinationSettings] = None
    dvb_sub_destination_settings: Optional[DvbSubDestinationSettings] = None
    teletext_destination_settings: Optional[TeletextDestinationSettings] = None
    burn_in_destination_settings: Optional[BurnInDestinationSettings] = None
    webvtt_destination_settings: Optional[WebvttDestinationSettings] = None
    embedded_destination_settings: Optional[EmbeddedDestinationSettings] = None
    rtmp_caption_info_destination_settings: Optional[RtmpCaptionInfoDestinationSettings] = None
    scte27_destination_settings: Optional[Scte27DestinationSettings] = None


@dataclass
class CaptionLanguageMapping(PropertyType):
    LANGUAGE_CODE = "LanguageCode"
    LANGUAGE_DESCRIPTION = "LanguageDescription"
    CAPTION_CHANNEL = "CaptionChannel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language_code": "LanguageCode",
        "language_description": "LanguageDescription",
        "caption_channel": "CaptionChannel",
    }

    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    language_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    caption_channel: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CaptionRectangle(PropertyType):
    TOP_OFFSET = "TopOffset"
    HEIGHT = "Height"
    WIDTH = "Width"
    LEFT_OFFSET = "LeftOffset"

    _property_mappings: ClassVar[dict[str, str]] = {
        "top_offset": "TopOffset",
        "height": "Height",
        "width": "Width",
        "left_offset": "LeftOffset",
    }

    top_offset: Optional[Union[float, Ref, GetAtt, Sub]] = None
    height: Optional[Union[float, Ref, GetAtt, Sub]] = None
    width: Optional[Union[float, Ref, GetAtt, Sub]] = None
    left_offset: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class CaptionSelector(PropertyType):
    LANGUAGE_CODE = "LanguageCode"
    SELECTOR_SETTINGS = "SelectorSettings"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language_code": "LanguageCode",
        "selector_settings": "SelectorSettings",
        "name": "Name",
    }

    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    selector_settings: Optional[CaptionSelectorSettings] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CaptionSelectorSettings(PropertyType):
    DVB_SUB_SOURCE_SETTINGS = "DvbSubSourceSettings"
    SCTE27_SOURCE_SETTINGS = "Scte27SourceSettings"
    ARIB_SOURCE_SETTINGS = "AribSourceSettings"
    EMBEDDED_SOURCE_SETTINGS = "EmbeddedSourceSettings"
    SCTE20_SOURCE_SETTINGS = "Scte20SourceSettings"
    TELETEXT_SOURCE_SETTINGS = "TeletextSourceSettings"
    ANCILLARY_SOURCE_SETTINGS = "AncillarySourceSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dvb_sub_source_settings": "DvbSubSourceSettings",
        "scte27_source_settings": "Scte27SourceSettings",
        "arib_source_settings": "AribSourceSettings",
        "embedded_source_settings": "EmbeddedSourceSettings",
        "scte20_source_settings": "Scte20SourceSettings",
        "teletext_source_settings": "TeletextSourceSettings",
        "ancillary_source_settings": "AncillarySourceSettings",
    }

    dvb_sub_source_settings: Optional[DvbSubSourceSettings] = None
    scte27_source_settings: Optional[Scte27SourceSettings] = None
    arib_source_settings: Optional[AribSourceSettings] = None
    embedded_source_settings: Optional[EmbeddedSourceSettings] = None
    scte20_source_settings: Optional[Scte20SourceSettings] = None
    teletext_source_settings: Optional[TeletextSourceSettings] = None
    ancillary_source_settings: Optional[AncillarySourceSettings] = None


@dataclass
class CdiInputSpecification(PropertyType):
    RESOLUTION = "Resolution"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resolution": "Resolution",
    }

    resolution: Optional[Union[str, CdiInputResolution, Ref, GetAtt, Sub]] = None


@dataclass
class ChannelEngineVersionRequest(PropertyType):
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CmafIngestCaptionLanguageMapping(PropertyType):
    LANGUAGE_CODE = "LanguageCode"
    CAPTION_CHANNEL = "CaptionChannel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language_code": "LanguageCode",
        "caption_channel": "CaptionChannel",
    }

    language_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    caption_channel: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CmafIngestGroupSettings(PropertyType):
    DESTINATION = "Destination"
    KLV_NAME_MODIFIER = "KlvNameModifier"
    SCTE35_TYPE = "Scte35Type"
    TIMED_METADATA_ID3_FRAME = "TimedMetadataId3Frame"
    TIMED_METADATA_PASSTHROUGH = "TimedMetadataPassthrough"
    NIELSEN_ID3_BEHAVIOR = "NielsenId3Behavior"
    SCTE35_NAME_MODIFIER = "Scte35NameModifier"
    CAPTION_LANGUAGE_MAPPINGS = "CaptionLanguageMappings"
    SEGMENT_LENGTH_UNITS = "SegmentLengthUnits"
    TIMED_METADATA_ID3_PERIOD = "TimedMetadataId3Period"
    ADDITIONAL_DESTINATIONS = "AdditionalDestinations"
    NIELSEN_ID3_NAME_MODIFIER = "NielsenId3NameModifier"
    KLV_BEHAVIOR = "KlvBehavior"
    SEGMENT_LENGTH = "SegmentLength"
    ID3_BEHAVIOR = "Id3Behavior"
    SEND_DELAY_MS = "SendDelayMs"
    ID3_NAME_MODIFIER = "Id3NameModifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "klv_name_modifier": "KlvNameModifier",
        "scte35_type": "Scte35Type",
        "timed_metadata_id3_frame": "TimedMetadataId3Frame",
        "timed_metadata_passthrough": "TimedMetadataPassthrough",
        "nielsen_id3_behavior": "NielsenId3Behavior",
        "scte35_name_modifier": "Scte35NameModifier",
        "caption_language_mappings": "CaptionLanguageMappings",
        "segment_length_units": "SegmentLengthUnits",
        "timed_metadata_id3_period": "TimedMetadataId3Period",
        "additional_destinations": "AdditionalDestinations",
        "nielsen_id3_name_modifier": "NielsenId3NameModifier",
        "klv_behavior": "KlvBehavior",
        "segment_length": "SegmentLength",
        "id3_behavior": "Id3Behavior",
        "send_delay_ms": "SendDelayMs",
        "id3_name_modifier": "Id3NameModifier",
    }

    destination: Optional[OutputLocationRef] = None
    klv_name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte35_type: Optional[Union[str, Scte35Type, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_frame: Optional[Union[str, CmafTimedMetadataId3Frame, Ref, GetAtt, Sub]] = None
    timed_metadata_passthrough: Optional[Union[str, CmafTimedMetadataPassthrough, Ref, GetAtt, Sub]] = None
    nielsen_id3_behavior: Optional[Union[str, CmafNielsenId3Behavior, Ref, GetAtt, Sub]] = None
    scte35_name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    caption_language_mappings: Optional[list[CmafIngestCaptionLanguageMapping]] = None
    segment_length_units: Optional[Union[str, CmafIngestSegmentLengthUnits, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    additional_destinations: Optional[list[AdditionalDestinations]] = None
    nielsen_id3_name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    klv_behavior: Optional[Union[str, CmafKLVBehavior, Ref, GetAtt, Sub]] = None
    segment_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id3_behavior: Optional[Union[str, CmafId3Behavior, Ref, GetAtt, Sub]] = None
    send_delay_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id3_name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CmafIngestOutputSettings(PropertyType):
    NAME_MODIFIER = "NameModifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name_modifier": "NameModifier",
    }

    name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColorCorrection(PropertyType):
    OUTPUT_COLOR_SPACE = "OutputColorSpace"
    INPUT_COLOR_SPACE = "InputColorSpace"
    URI = "Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_color_space": "OutputColorSpace",
        "input_color_space": "InputColorSpace",
        "uri": "Uri",
    }

    output_color_space: Optional[Union[str, ColorSpace, Ref, GetAtt, Sub]] = None
    input_color_space: Optional[Union[str, ColorSpace, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColorCorrectionSettings(PropertyType):
    GLOBAL_COLOR_CORRECTIONS = "GlobalColorCorrections"

    _property_mappings: ClassVar[dict[str, str]] = {
        "global_color_corrections": "GlobalColorCorrections",
    }

    global_color_corrections: Optional[list[ColorCorrection]] = None


@dataclass
class ColorSpacePassthroughSettings(PropertyType):
    pass


@dataclass
class DolbyVision81Settings(PropertyType):
    pass


@dataclass
class DvbNitSettings(PropertyType):
    NETWORK_NAME = "NetworkName"
    REP_INTERVAL = "RepInterval"
    NETWORK_ID = "NetworkId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_name": "NetworkName",
        "rep_interval": "RepInterval",
        "network_id": "NetworkId",
    }

    network_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rep_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    network_id: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DvbSdtSettings(PropertyType):
    SERVICE_PROVIDER_NAME = "ServiceProviderName"
    OUTPUT_SDT = "OutputSdt"
    SERVICE_NAME = "ServiceName"
    REP_INTERVAL = "RepInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_provider_name": "ServiceProviderName",
        "output_sdt": "OutputSdt",
        "service_name": "ServiceName",
        "rep_interval": "RepInterval",
    }

    service_provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_sdt: Optional[Union[str, DvbSdtOutputSdt, Ref, GetAtt, Sub]] = None
    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rep_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DvbSubDestinationSettings(PropertyType):
    BACKGROUND_OPACITY = "BackgroundOpacity"
    FONT_RESOLUTION = "FontResolution"
    OUTLINE_COLOR = "OutlineColor"
    FONT_COLOR = "FontColor"
    SHADOW_COLOR = "ShadowColor"
    SHADOW_OPACITY = "ShadowOpacity"
    FONT = "Font"
    SHADOW_Y_OFFSET = "ShadowYOffset"
    ALIGNMENT = "Alignment"
    X_POSITION = "XPosition"
    FONT_SIZE = "FontSize"
    Y_POSITION = "YPosition"
    OUTLINE_SIZE = "OutlineSize"
    TELETEXT_GRID_CONTROL = "TeletextGridControl"
    SUBTITLE_ROWS = "SubtitleRows"
    FONT_OPACITY = "FontOpacity"
    SHADOW_X_OFFSET = "ShadowXOffset"
    BACKGROUND_COLOR = "BackgroundColor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "background_opacity": "BackgroundOpacity",
        "font_resolution": "FontResolution",
        "outline_color": "OutlineColor",
        "font_color": "FontColor",
        "shadow_color": "ShadowColor",
        "shadow_opacity": "ShadowOpacity",
        "font": "Font",
        "shadow_y_offset": "ShadowYOffset",
        "alignment": "Alignment",
        "x_position": "XPosition",
        "font_size": "FontSize",
        "y_position": "YPosition",
        "outline_size": "OutlineSize",
        "teletext_grid_control": "TeletextGridControl",
        "subtitle_rows": "SubtitleRows",
        "font_opacity": "FontOpacity",
        "shadow_x_offset": "ShadowXOffset",
        "background_color": "BackgroundColor",
    }

    background_opacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    font_resolution: Optional[Union[int, Ref, GetAtt, Sub]] = None
    outline_color: Optional[Union[str, DvbSubDestinationOutlineColor, Ref, GetAtt, Sub]] = None
    font_color: Optional[Union[str, DvbSubDestinationFontColor, Ref, GetAtt, Sub]] = None
    shadow_color: Optional[Union[str, DvbSubDestinationShadowColor, Ref, GetAtt, Sub]] = None
    shadow_opacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    font: Optional[InputLocation] = None
    shadow_y_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    alignment: Optional[Union[str, DvbSubDestinationAlignment, Ref, GetAtt, Sub]] = None
    x_position: Optional[Union[int, Ref, GetAtt, Sub]] = None
    font_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    y_position: Optional[Union[int, Ref, GetAtt, Sub]] = None
    outline_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    teletext_grid_control: Optional[Union[str, DvbSubDestinationTeletextGridControl, Ref, GetAtt, Sub]] = None
    subtitle_rows: Optional[Union[str, DvbSubDestinationSubtitleRows, Ref, GetAtt, Sub]] = None
    font_opacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    shadow_x_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, DvbSubDestinationBackgroundColor, Ref, GetAtt, Sub]] = None


@dataclass
class DvbSubSourceSettings(PropertyType):
    OCR_LANGUAGE = "OcrLanguage"
    PID = "Pid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ocr_language": "OcrLanguage",
        "pid": "Pid",
    }

    ocr_language: Optional[Union[str, DvbSubOcrLanguage, Ref, GetAtt, Sub]] = None
    pid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DvbTdtSettings(PropertyType):
    REP_INTERVAL = "RepInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rep_interval": "RepInterval",
    }

    rep_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Eac3AtmosSettings(PropertyType):
    CODING_MODE = "CodingMode"
    DIALNORM = "Dialnorm"
    SURROUND_TRIM = "SurroundTrim"
    DRC_RF = "DrcRf"
    BITRATE = "Bitrate"
    DRC_LINE = "DrcLine"
    HEIGHT_TRIM = "HeightTrim"

    _property_mappings: ClassVar[dict[str, str]] = {
        "coding_mode": "CodingMode",
        "dialnorm": "Dialnorm",
        "surround_trim": "SurroundTrim",
        "drc_rf": "DrcRf",
        "bitrate": "Bitrate",
        "drc_line": "DrcLine",
        "height_trim": "HeightTrim",
    }

    coding_mode: Optional[Union[str, Eac3AtmosCodingMode, Ref, GetAtt, Sub]] = None
    dialnorm: Optional[Union[int, Ref, GetAtt, Sub]] = None
    surround_trim: Optional[Union[float, Ref, GetAtt, Sub]] = None
    drc_rf: Optional[Union[str, Eac3AtmosDrcRf, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    drc_line: Optional[Union[str, Eac3AtmosDrcLine, Ref, GetAtt, Sub]] = None
    height_trim: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Eac3Settings(PropertyType):
    CODING_MODE = "CodingMode"
    SURROUND_MODE = "SurroundMode"
    PASSTHROUGH_CONTROL = "PassthroughControl"
    DIALNORM = "Dialnorm"
    LO_RO_SURROUND_MIX_LEVEL = "LoRoSurroundMixLevel"
    PHASE_CONTROL = "PhaseControl"
    LT_RT_CENTER_MIX_LEVEL = "LtRtCenterMixLevel"
    LFE_FILTER = "LfeFilter"
    LFE_CONTROL = "LfeControl"
    BITRATE = "Bitrate"
    DRC_LINE = "DrcLine"
    DC_FILTER = "DcFilter"
    METADATA_CONTROL = "MetadataControl"
    LT_RT_SURROUND_MIX_LEVEL = "LtRtSurroundMixLevel"
    LO_RO_CENTER_MIX_LEVEL = "LoRoCenterMixLevel"
    DRC_RF = "DrcRf"
    ATTENUATION_CONTROL = "AttenuationControl"
    BITSTREAM_MODE = "BitstreamMode"
    SURROUND_EX_MODE = "SurroundExMode"
    STEREO_DOWNMIX = "StereoDownmix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "coding_mode": "CodingMode",
        "surround_mode": "SurroundMode",
        "passthrough_control": "PassthroughControl",
        "dialnorm": "Dialnorm",
        "lo_ro_surround_mix_level": "LoRoSurroundMixLevel",
        "phase_control": "PhaseControl",
        "lt_rt_center_mix_level": "LtRtCenterMixLevel",
        "lfe_filter": "LfeFilter",
        "lfe_control": "LfeControl",
        "bitrate": "Bitrate",
        "drc_line": "DrcLine",
        "dc_filter": "DcFilter",
        "metadata_control": "MetadataControl",
        "lt_rt_surround_mix_level": "LtRtSurroundMixLevel",
        "lo_ro_center_mix_level": "LoRoCenterMixLevel",
        "drc_rf": "DrcRf",
        "attenuation_control": "AttenuationControl",
        "bitstream_mode": "BitstreamMode",
        "surround_ex_mode": "SurroundExMode",
        "stereo_downmix": "StereoDownmix",
    }

    coding_mode: Optional[Union[str, Eac3CodingMode, Ref, GetAtt, Sub]] = None
    surround_mode: Optional[Union[str, Eac3SurroundMode, Ref, GetAtt, Sub]] = None
    passthrough_control: Optional[Union[str, Eac3PassthroughControl, Ref, GetAtt, Sub]] = None
    dialnorm: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lo_ro_surround_mix_level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    phase_control: Optional[Union[str, Eac3PhaseControl, Ref, GetAtt, Sub]] = None
    lt_rt_center_mix_level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    lfe_filter: Optional[Union[str, Eac3LfeFilter, Ref, GetAtt, Sub]] = None
    lfe_control: Optional[Union[str, Eac3LfeControl, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    drc_line: Optional[Union[str, Eac3DrcLine, Ref, GetAtt, Sub]] = None
    dc_filter: Optional[Union[str, Eac3DcFilter, Ref, GetAtt, Sub]] = None
    metadata_control: Optional[Union[str, Eac3MetadataControl, Ref, GetAtt, Sub]] = None
    lt_rt_surround_mix_level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    lo_ro_center_mix_level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    drc_rf: Optional[Union[str, Eac3DrcRf, Ref, GetAtt, Sub]] = None
    attenuation_control: Optional[Union[str, Eac3AttenuationControl, Ref, GetAtt, Sub]] = None
    bitstream_mode: Optional[Union[str, Eac3BitstreamMode, Ref, GetAtt, Sub]] = None
    surround_ex_mode: Optional[Union[str, Eac3SurroundExMode, Ref, GetAtt, Sub]] = None
    stereo_downmix: Optional[Union[str, Eac3StereoDownmix, Ref, GetAtt, Sub]] = None


@dataclass
class EbuTtDDestinationSettings(PropertyType):
    FONT_FAMILY = "FontFamily"
    DEFAULT_FONT_SIZE = "DefaultFontSize"
    DEFAULT_LINE_HEIGHT = "DefaultLineHeight"
    FILL_LINE_GAP = "FillLineGap"
    STYLE_CONTROL = "StyleControl"
    COPYRIGHT_HOLDER = "CopyrightHolder"

    _property_mappings: ClassVar[dict[str, str]] = {
        "font_family": "FontFamily",
        "default_font_size": "DefaultFontSize",
        "default_line_height": "DefaultLineHeight",
        "fill_line_gap": "FillLineGap",
        "style_control": "StyleControl",
        "copyright_holder": "CopyrightHolder",
    }

    font_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_font_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_line_height: Optional[Union[int, Ref, GetAtt, Sub]] = None
    fill_line_gap: Optional[Union[str, EbuTtDFillLineGapControl, Ref, GetAtt, Sub]] = None
    style_control: Optional[Union[str, EbuTtDDestinationStyleControl, Ref, GetAtt, Sub]] = None
    copyright_holder: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmbeddedDestinationSettings(PropertyType):
    pass


@dataclass
class EmbeddedPlusScte20DestinationSettings(PropertyType):
    pass


@dataclass
class EmbeddedSourceSettings(PropertyType):
    SOURCE608_CHANNEL_NUMBER = "Source608ChannelNumber"
    SCTE20_DETECTION = "Scte20Detection"
    SOURCE608_TRACK_NUMBER = "Source608TrackNumber"
    CONVERT608_TO708 = "Convert608To708"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source608_channel_number": "Source608ChannelNumber",
        "scte20_detection": "Scte20Detection",
        "source608_track_number": "Source608TrackNumber",
        "convert608_to708": "Convert608To708",
    }

    source608_channel_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scte20_detection: Optional[Union[str, EmbeddedScte20Detection, Ref, GetAtt, Sub]] = None
    source608_track_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    convert608_to708: Optional[Union[str, EmbeddedConvert608To708, Ref, GetAtt, Sub]] = None


@dataclass
class EncoderSettings(PropertyType):
    AUDIO_DESCRIPTIONS = "AudioDescriptions"
    VIDEO_DESCRIPTIONS = "VideoDescriptions"
    GLOBAL_CONFIGURATION = "GlobalConfiguration"
    MOTION_GRAPHICS_CONFIGURATION = "MotionGraphicsConfiguration"
    THUMBNAIL_CONFIGURATION = "ThumbnailConfiguration"
    FEATURE_ACTIVATIONS = "FeatureActivations"
    CAPTION_DESCRIPTIONS = "CaptionDescriptions"
    AVAIL_CONFIGURATION = "AvailConfiguration"
    COLOR_CORRECTION_SETTINGS = "ColorCorrectionSettings"
    OUTPUT_GROUPS = "OutputGroups"
    AVAIL_BLANKING = "AvailBlanking"
    NIELSEN_CONFIGURATION = "NielsenConfiguration"
    BLACKOUT_SLATE = "BlackoutSlate"
    TIMECODE_CONFIG = "TimecodeConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_descriptions": "AudioDescriptions",
        "video_descriptions": "VideoDescriptions",
        "global_configuration": "GlobalConfiguration",
        "motion_graphics_configuration": "MotionGraphicsConfiguration",
        "thumbnail_configuration": "ThumbnailConfiguration",
        "feature_activations": "FeatureActivations",
        "caption_descriptions": "CaptionDescriptions",
        "avail_configuration": "AvailConfiguration",
        "color_correction_settings": "ColorCorrectionSettings",
        "output_groups": "OutputGroups",
        "avail_blanking": "AvailBlanking",
        "nielsen_configuration": "NielsenConfiguration",
        "blackout_slate": "BlackoutSlate",
        "timecode_config": "TimecodeConfig",
    }

    audio_descriptions: Optional[list[AudioDescription]] = None
    video_descriptions: Optional[list[VideoDescription]] = None
    global_configuration: Optional[GlobalConfiguration] = None
    motion_graphics_configuration: Optional[MotionGraphicsConfiguration] = None
    thumbnail_configuration: Optional[ThumbnailConfiguration] = None
    feature_activations: Optional[FeatureActivations] = None
    caption_descriptions: Optional[list[CaptionDescription]] = None
    avail_configuration: Optional[AvailConfiguration] = None
    color_correction_settings: Optional[ColorCorrectionSettings] = None
    output_groups: Optional[list[OutputGroup]] = None
    avail_blanking: Optional[AvailBlanking] = None
    nielsen_configuration: Optional[NielsenConfiguration] = None
    blackout_slate: Optional[BlackoutSlate] = None
    timecode_config: Optional[TimecodeConfig] = None


@dataclass
class EpochLockingSettings(PropertyType):
    JAM_SYNC_TIME = "JamSyncTime"
    CUSTOM_EPOCH = "CustomEpoch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jam_sync_time": "JamSyncTime",
        "custom_epoch": "CustomEpoch",
    }

    jam_sync_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_epoch: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Esam(PropertyType):
    AD_AVAIL_OFFSET = "AdAvailOffset"
    ZONE_IDENTITY = "ZoneIdentity"
    ACQUISITION_POINT_ID = "AcquisitionPointId"
    POIS_ENDPOINT = "PoisEndpoint"
    USERNAME = "Username"
    PASSWORD_PARAM = "PasswordParam"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_avail_offset": "AdAvailOffset",
        "zone_identity": "ZoneIdentity",
        "acquisition_point_id": "AcquisitionPointId",
        "pois_endpoint": "PoisEndpoint",
        "username": "Username",
        "password_param": "PasswordParam",
    }

    ad_avail_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    zone_identity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    acquisition_point_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pois_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_param: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FailoverCondition(PropertyType):
    FAILOVER_CONDITION_SETTINGS = "FailoverConditionSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "failover_condition_settings": "FailoverConditionSettings",
    }

    failover_condition_settings: Optional[FailoverConditionSettings] = None


@dataclass
class FailoverConditionSettings(PropertyType):
    AUDIO_SILENCE_SETTINGS = "AudioSilenceSettings"
    VIDEO_BLACK_SETTINGS = "VideoBlackSettings"
    INPUT_LOSS_SETTINGS = "InputLossSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_silence_settings": "AudioSilenceSettings",
        "video_black_settings": "VideoBlackSettings",
        "input_loss_settings": "InputLossSettings",
    }

    audio_silence_settings: Optional[AudioSilenceFailoverSettings] = None
    video_black_settings: Optional[VideoBlackFailoverSettings] = None
    input_loss_settings: Optional[InputLossFailoverSettings] = None


@dataclass
class FeatureActivations(PropertyType):
    INPUT_PREPARE_SCHEDULE_ACTIONS = "InputPrepareScheduleActions"
    OUTPUT_STATIC_IMAGE_OVERLAY_SCHEDULE_ACTIONS = "OutputStaticImageOverlayScheduleActions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_prepare_schedule_actions": "InputPrepareScheduleActions",
        "output_static_image_overlay_schedule_actions": "OutputStaticImageOverlayScheduleActions",
    }

    input_prepare_schedule_actions: Optional[Union[str, FeatureActivationsInputPrepareScheduleActions, Ref, GetAtt, Sub]] = None
    output_static_image_overlay_schedule_actions: Optional[Union[str, FeatureActivationsOutputStaticImageOverlayScheduleActions, Ref, GetAtt, Sub]] = None


@dataclass
class FecOutputSettings(PropertyType):
    ROW_LENGTH = "RowLength"
    COLUMN_DEPTH = "ColumnDepth"
    INCLUDE_FEC = "IncludeFec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "row_length": "RowLength",
        "column_depth": "ColumnDepth",
        "include_fec": "IncludeFec",
    }

    row_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    column_depth: Optional[Union[int, Ref, GetAtt, Sub]] = None
    include_fec: Optional[Union[str, FecOutputIncludeFec, Ref, GetAtt, Sub]] = None


@dataclass
class Fmp4HlsSettings(PropertyType):
    AUDIO_RENDITION_SETS = "AudioRenditionSets"
    NIELSEN_ID3_BEHAVIOR = "NielsenId3Behavior"
    TIMED_METADATA_BEHAVIOR = "TimedMetadataBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_rendition_sets": "AudioRenditionSets",
        "nielsen_id3_behavior": "NielsenId3Behavior",
        "timed_metadata_behavior": "TimedMetadataBehavior",
    }

    audio_rendition_sets: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nielsen_id3_behavior: Optional[Union[str, Fmp4NielsenId3Behavior, Ref, GetAtt, Sub]] = None
    timed_metadata_behavior: Optional[Union[str, Fmp4TimedMetadataBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class FrameCaptureCdnSettings(PropertyType):
    FRAME_CAPTURE_S3_SETTINGS = "FrameCaptureS3Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "frame_capture_s3_settings": "FrameCaptureS3Settings",
    }

    frame_capture_s3_settings: Optional[FrameCaptureS3Settings] = None


@dataclass
class FrameCaptureGroupSettings(PropertyType):
    FRAME_CAPTURE_CDN_SETTINGS = "FrameCaptureCdnSettings"
    DESTINATION = "Destination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "frame_capture_cdn_settings": "FrameCaptureCdnSettings",
        "destination": "Destination",
    }

    frame_capture_cdn_settings: Optional[FrameCaptureCdnSettings] = None
    destination: Optional[OutputLocationRef] = None


@dataclass
class FrameCaptureHlsSettings(PropertyType):
    pass


@dataclass
class FrameCaptureOutputSettings(PropertyType):
    NAME_MODIFIER = "NameModifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name_modifier": "NameModifier",
    }

    name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FrameCaptureS3Settings(PropertyType):
    CANNED_ACL = "CannedAcl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canned_acl": "CannedAcl",
    }

    canned_acl: Optional[Union[str, S3CannedAcl, Ref, GetAtt, Sub]] = None


@dataclass
class FrameCaptureSettings(PropertyType):
    TIMECODE_BURNIN_SETTINGS = "TimecodeBurninSettings"
    CAPTURE_INTERVAL = "CaptureInterval"
    CAPTURE_INTERVAL_UNITS = "CaptureIntervalUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timecode_burnin_settings": "TimecodeBurninSettings",
        "capture_interval": "CaptureInterval",
        "capture_interval_units": "CaptureIntervalUnits",
    }

    timecode_burnin_settings: Optional[TimecodeBurninSettings] = None
    capture_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    capture_interval_units: Optional[Union[str, FrameCaptureIntervalUnit, Ref, GetAtt, Sub]] = None


@dataclass
class GlobalConfiguration(PropertyType):
    INPUT_END_ACTION = "InputEndAction"
    OUTPUT_LOCKING_SETTINGS = "OutputLockingSettings"
    OUTPUT_TIMING_SOURCE = "OutputTimingSource"
    OUTPUT_LOCKING_MODE = "OutputLockingMode"
    SUPPORT_LOW_FRAMERATE_INPUTS = "SupportLowFramerateInputs"
    INITIAL_AUDIO_GAIN = "InitialAudioGain"
    INPUT_LOSS_BEHAVIOR = "InputLossBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_end_action": "InputEndAction",
        "output_locking_settings": "OutputLockingSettings",
        "output_timing_source": "OutputTimingSource",
        "output_locking_mode": "OutputLockingMode",
        "support_low_framerate_inputs": "SupportLowFramerateInputs",
        "initial_audio_gain": "InitialAudioGain",
        "input_loss_behavior": "InputLossBehavior",
    }

    input_end_action: Optional[Union[str, GlobalConfigurationInputEndAction, Ref, GetAtt, Sub]] = None
    output_locking_settings: Optional[OutputLockingSettings] = None
    output_timing_source: Optional[Union[str, GlobalConfigurationOutputTimingSource, Ref, GetAtt, Sub]] = None
    output_locking_mode: Optional[Union[str, GlobalConfigurationOutputLockingMode, Ref, GetAtt, Sub]] = None
    support_low_framerate_inputs: Optional[Union[str, GlobalConfigurationLowFramerateInputs, Ref, GetAtt, Sub]] = None
    initial_audio_gain: Optional[Union[int, Ref, GetAtt, Sub]] = None
    input_loss_behavior: Optional[InputLossBehavior] = None


@dataclass
class H264ColorSpaceSettings(PropertyType):
    REC601_SETTINGS = "Rec601Settings"
    REC709_SETTINGS = "Rec709Settings"
    COLOR_SPACE_PASSTHROUGH_SETTINGS = "ColorSpacePassthroughSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rec601_settings": "Rec601Settings",
        "rec709_settings": "Rec709Settings",
        "color_space_passthrough_settings": "ColorSpacePassthroughSettings",
    }

    rec601_settings: Optional[Rec601Settings] = None
    rec709_settings: Optional[Rec709Settings] = None
    color_space_passthrough_settings: Optional[ColorSpacePassthroughSettings] = None


@dataclass
class H264FilterSettings(PropertyType):
    TEMPORAL_FILTER_SETTINGS = "TemporalFilterSettings"
    BANDWIDTH_REDUCTION_FILTER_SETTINGS = "BandwidthReductionFilterSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "temporal_filter_settings": "TemporalFilterSettings",
        "bandwidth_reduction_filter_settings": "BandwidthReductionFilterSettings",
    }

    temporal_filter_settings: Optional[TemporalFilterSettings] = None
    bandwidth_reduction_filter_settings: Optional[BandwidthReductionFilterSettings] = None


@dataclass
class H264Settings(PropertyType):
    TIMECODE_BURNIN_SETTINGS = "TimecodeBurninSettings"
    NUM_REF_FRAMES = "NumRefFrames"
    TEMPORAL_AQ = "TemporalAq"
    SLICES = "Slices"
    FRAMERATE_CONTROL = "FramerateControl"
    QVBR_QUALITY_LEVEL = "QvbrQualityLevel"
    FRAMERATE_NUMERATOR = "FramerateNumerator"
    PAR_CONTROL = "ParControl"
    GOP_CLOSED_CADENCE = "GopClosedCadence"
    FLICKER_AQ = "FlickerAq"
    PROFILE = "Profile"
    QUALITY_LEVEL = "QualityLevel"
    MIN_BITRATE = "MinBitrate"
    MIN_I_INTERVAL = "MinIInterval"
    SCENE_CHANGE_DETECT = "SceneChangeDetect"
    FORCE_FIELD_PICTURES = "ForceFieldPictures"
    FRAMERATE_DENOMINATOR = "FramerateDenominator"
    SOFTNESS = "Softness"
    GOP_SIZE = "GopSize"
    ADAPTIVE_QUANTIZATION = "AdaptiveQuantization"
    FILTER_SETTINGS = "FilterSettings"
    MIN_QP = "MinQp"
    COLOR_SPACE_SETTINGS = "ColorSpaceSettings"
    ENTROPY_ENCODING = "EntropyEncoding"
    SPATIAL_AQ = "SpatialAq"
    PAR_DENOMINATOR = "ParDenominator"
    FIXED_AFD = "FixedAfd"
    GOP_SIZE_UNITS = "GopSizeUnits"
    AFD_SIGNALING = "AfdSignaling"
    BITRATE = "Bitrate"
    PAR_NUMERATOR = "ParNumerator"
    RATE_CONTROL_MODE = "RateControlMode"
    SCAN_TYPE = "ScanType"
    BUF_SIZE = "BufSize"
    TIMECODE_INSERTION = "TimecodeInsertion"
    COLOR_METADATA = "ColorMetadata"
    BUF_FILL_PCT = "BufFillPct"
    GOP_B_REFERENCE = "GopBReference"
    LOOK_AHEAD_RATE_CONTROL = "LookAheadRateControl"
    LEVEL = "Level"
    MAX_BITRATE = "MaxBitrate"
    SYNTAX = "Syntax"
    SUBGOP_LENGTH = "SubgopLength"
    GOP_NUM_B_FRAMES = "GopNumBFrames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timecode_burnin_settings": "TimecodeBurninSettings",
        "num_ref_frames": "NumRefFrames",
        "temporal_aq": "TemporalAq",
        "slices": "Slices",
        "framerate_control": "FramerateControl",
        "qvbr_quality_level": "QvbrQualityLevel",
        "framerate_numerator": "FramerateNumerator",
        "par_control": "ParControl",
        "gop_closed_cadence": "GopClosedCadence",
        "flicker_aq": "FlickerAq",
        "profile": "Profile",
        "quality_level": "QualityLevel",
        "min_bitrate": "MinBitrate",
        "min_i_interval": "MinIInterval",
        "scene_change_detect": "SceneChangeDetect",
        "force_field_pictures": "ForceFieldPictures",
        "framerate_denominator": "FramerateDenominator",
        "softness": "Softness",
        "gop_size": "GopSize",
        "adaptive_quantization": "AdaptiveQuantization",
        "filter_settings": "FilterSettings",
        "min_qp": "MinQp",
        "color_space_settings": "ColorSpaceSettings",
        "entropy_encoding": "EntropyEncoding",
        "spatial_aq": "SpatialAq",
        "par_denominator": "ParDenominator",
        "fixed_afd": "FixedAfd",
        "gop_size_units": "GopSizeUnits",
        "afd_signaling": "AfdSignaling",
        "bitrate": "Bitrate",
        "par_numerator": "ParNumerator",
        "rate_control_mode": "RateControlMode",
        "scan_type": "ScanType",
        "buf_size": "BufSize",
        "timecode_insertion": "TimecodeInsertion",
        "color_metadata": "ColorMetadata",
        "buf_fill_pct": "BufFillPct",
        "gop_b_reference": "GopBReference",
        "look_ahead_rate_control": "LookAheadRateControl",
        "level": "Level",
        "max_bitrate": "MaxBitrate",
        "syntax": "Syntax",
        "subgop_length": "SubgopLength",
        "gop_num_b_frames": "GopNumBFrames",
    }

    timecode_burnin_settings: Optional[TimecodeBurninSettings] = None
    num_ref_frames: Optional[Union[int, Ref, GetAtt, Sub]] = None
    temporal_aq: Optional[Union[str, H264TemporalAq, Ref, GetAtt, Sub]] = None
    slices: Optional[Union[int, Ref, GetAtt, Sub]] = None
    framerate_control: Optional[Union[str, H264FramerateControl, Ref, GetAtt, Sub]] = None
    qvbr_quality_level: Optional[Union[int, Ref, GetAtt, Sub]] = None
    framerate_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    par_control: Optional[Union[str, H264ParControl, Ref, GetAtt, Sub]] = None
    gop_closed_cadence: Optional[Union[int, Ref, GetAtt, Sub]] = None
    flicker_aq: Optional[Union[str, H264FlickerAq, Ref, GetAtt, Sub]] = None
    profile: Optional[Union[str, H264Profile, Ref, GetAtt, Sub]] = None
    quality_level: Optional[Union[str, H264QualityLevel, Ref, GetAtt, Sub]] = None
    min_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_i_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scene_change_detect: Optional[Union[str, H264SceneChangeDetect, Ref, GetAtt, Sub]] = None
    force_field_pictures: Optional[Union[str, H264ForceFieldPictures, Ref, GetAtt, Sub]] = None
    framerate_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    softness: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    adaptive_quantization: Optional[Union[str, H264AdaptiveQuantization, Ref, GetAtt, Sub]] = None
    filter_settings: Optional[H264FilterSettings] = None
    min_qp: Optional[Union[int, Ref, GetAtt, Sub]] = None
    color_space_settings: Optional[H264ColorSpaceSettings] = None
    entropy_encoding: Optional[Union[str, H264EntropyEncoding, Ref, GetAtt, Sub]] = None
    spatial_aq: Optional[Union[str, H264SpatialAq, Ref, GetAtt, Sub]] = None
    par_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    fixed_afd: Optional[Union[str, FixedAfd, Ref, GetAtt, Sub]] = None
    gop_size_units: Optional[Union[str, H264GopSizeUnits, Ref, GetAtt, Sub]] = None
    afd_signaling: Optional[Union[str, AfdSignaling, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    par_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rate_control_mode: Optional[Union[str, H264RateControlMode, Ref, GetAtt, Sub]] = None
    scan_type: Optional[Union[str, H264ScanType, Ref, GetAtt, Sub]] = None
    buf_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timecode_insertion: Optional[Union[str, H264TimecodeInsertionBehavior, Ref, GetAtt, Sub]] = None
    color_metadata: Optional[Union[str, H264ColorMetadata, Ref, GetAtt, Sub]] = None
    buf_fill_pct: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_b_reference: Optional[Union[str, H264GopBReference, Ref, GetAtt, Sub]] = None
    look_ahead_rate_control: Optional[Union[str, H264LookAheadRateControl, Ref, GetAtt, Sub]] = None
    level: Optional[Union[str, H264Level, Ref, GetAtt, Sub]] = None
    max_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    syntax: Optional[Union[str, H264Syntax, Ref, GetAtt, Sub]] = None
    subgop_length: Optional[Union[str, H264SubGopLength, Ref, GetAtt, Sub]] = None
    gop_num_b_frames: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class H265ColorSpaceSettings(PropertyType):
    REC601_SETTINGS = "Rec601Settings"
    REC709_SETTINGS = "Rec709Settings"
    COLOR_SPACE_PASSTHROUGH_SETTINGS = "ColorSpacePassthroughSettings"
    DOLBY_VISION81_SETTINGS = "DolbyVision81Settings"
    HDR10_SETTINGS = "Hdr10Settings"
    HLG2020_SETTINGS = "Hlg2020Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rec601_settings": "Rec601Settings",
        "rec709_settings": "Rec709Settings",
        "color_space_passthrough_settings": "ColorSpacePassthroughSettings",
        "dolby_vision81_settings": "DolbyVision81Settings",
        "hdr10_settings": "Hdr10Settings",
        "hlg2020_settings": "Hlg2020Settings",
    }

    rec601_settings: Optional[Rec601Settings] = None
    rec709_settings: Optional[Rec709Settings] = None
    color_space_passthrough_settings: Optional[ColorSpacePassthroughSettings] = None
    dolby_vision81_settings: Optional[DolbyVision81Settings] = None
    hdr10_settings: Optional[Hdr10Settings] = None
    hlg2020_settings: Optional[Hlg2020Settings] = None


@dataclass
class H265FilterSettings(PropertyType):
    TEMPORAL_FILTER_SETTINGS = "TemporalFilterSettings"
    BANDWIDTH_REDUCTION_FILTER_SETTINGS = "BandwidthReductionFilterSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "temporal_filter_settings": "TemporalFilterSettings",
        "bandwidth_reduction_filter_settings": "BandwidthReductionFilterSettings",
    }

    temporal_filter_settings: Optional[TemporalFilterSettings] = None
    bandwidth_reduction_filter_settings: Optional[BandwidthReductionFilterSettings] = None


@dataclass
class H265Settings(PropertyType):
    MV_OVER_PICTURE_BOUNDARIES = "MvOverPictureBoundaries"
    TIMECODE_BURNIN_SETTINGS = "TimecodeBurninSettings"
    SLICES = "Slices"
    QVBR_QUALITY_LEVEL = "QvbrQualityLevel"
    TILE_HEIGHT = "TileHeight"
    FRAMERATE_NUMERATOR = "FramerateNumerator"
    GOP_CLOSED_CADENCE = "GopClosedCadence"
    FLICKER_AQ = "FlickerAq"
    PROFILE = "Profile"
    MV_TEMPORAL_PREDICTOR = "MvTemporalPredictor"
    MIN_BITRATE = "MinBitrate"
    MIN_I_INTERVAL = "MinIInterval"
    SCENE_CHANGE_DETECT = "SceneChangeDetect"
    FRAMERATE_DENOMINATOR = "FramerateDenominator"
    GOP_SIZE = "GopSize"
    ADAPTIVE_QUANTIZATION = "AdaptiveQuantization"
    TILE_WIDTH = "TileWidth"
    FILTER_SETTINGS = "FilterSettings"
    MIN_QP = "MinQp"
    ALTERNATIVE_TRANSFER_FUNCTION = "AlternativeTransferFunction"
    COLOR_SPACE_SETTINGS = "ColorSpaceSettings"
    TIER = "Tier"
    PAR_DENOMINATOR = "ParDenominator"
    FIXED_AFD = "FixedAfd"
    GOP_SIZE_UNITS = "GopSizeUnits"
    TILE_PADDING = "TilePadding"
    AFD_SIGNALING = "AfdSignaling"
    BITRATE = "Bitrate"
    PAR_NUMERATOR = "ParNumerator"
    RATE_CONTROL_MODE = "RateControlMode"
    SCAN_TYPE = "ScanType"
    BUF_SIZE = "BufSize"
    TIMECODE_INSERTION = "TimecodeInsertion"
    DEBLOCKING = "Deblocking"
    COLOR_METADATA = "ColorMetadata"
    LOOK_AHEAD_RATE_CONTROL = "LookAheadRateControl"
    GOP_B_REFERENCE = "GopBReference"
    LEVEL = "Level"
    MAX_BITRATE = "MaxBitrate"
    TREEBLOCK_SIZE = "TreeblockSize"
    SUBGOP_LENGTH = "SubgopLength"
    GOP_NUM_B_FRAMES = "GopNumBFrames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mv_over_picture_boundaries": "MvOverPictureBoundaries",
        "timecode_burnin_settings": "TimecodeBurninSettings",
        "slices": "Slices",
        "qvbr_quality_level": "QvbrQualityLevel",
        "tile_height": "TileHeight",
        "framerate_numerator": "FramerateNumerator",
        "gop_closed_cadence": "GopClosedCadence",
        "flicker_aq": "FlickerAq",
        "profile": "Profile",
        "mv_temporal_predictor": "MvTemporalPredictor",
        "min_bitrate": "MinBitrate",
        "min_i_interval": "MinIInterval",
        "scene_change_detect": "SceneChangeDetect",
        "framerate_denominator": "FramerateDenominator",
        "gop_size": "GopSize",
        "adaptive_quantization": "AdaptiveQuantization",
        "tile_width": "TileWidth",
        "filter_settings": "FilterSettings",
        "min_qp": "MinQp",
        "alternative_transfer_function": "AlternativeTransferFunction",
        "color_space_settings": "ColorSpaceSettings",
        "tier": "Tier",
        "par_denominator": "ParDenominator",
        "fixed_afd": "FixedAfd",
        "gop_size_units": "GopSizeUnits",
        "tile_padding": "TilePadding",
        "afd_signaling": "AfdSignaling",
        "bitrate": "Bitrate",
        "par_numerator": "ParNumerator",
        "rate_control_mode": "RateControlMode",
        "scan_type": "ScanType",
        "buf_size": "BufSize",
        "timecode_insertion": "TimecodeInsertion",
        "deblocking": "Deblocking",
        "color_metadata": "ColorMetadata",
        "look_ahead_rate_control": "LookAheadRateControl",
        "gop_b_reference": "GopBReference",
        "level": "Level",
        "max_bitrate": "MaxBitrate",
        "treeblock_size": "TreeblockSize",
        "subgop_length": "SubgopLength",
        "gop_num_b_frames": "GopNumBFrames",
    }

    mv_over_picture_boundaries: Optional[Union[str, H265MvOverPictureBoundaries, Ref, GetAtt, Sub]] = None
    timecode_burnin_settings: Optional[TimecodeBurninSettings] = None
    slices: Optional[Union[int, Ref, GetAtt, Sub]] = None
    qvbr_quality_level: Optional[Union[int, Ref, GetAtt, Sub]] = None
    tile_height: Optional[Union[int, Ref, GetAtt, Sub]] = None
    framerate_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_closed_cadence: Optional[Union[int, Ref, GetAtt, Sub]] = None
    flicker_aq: Optional[Union[str, H265FlickerAq, Ref, GetAtt, Sub]] = None
    profile: Optional[Union[str, H265Profile, Ref, GetAtt, Sub]] = None
    mv_temporal_predictor: Optional[Union[str, H265MvTemporalPredictor, Ref, GetAtt, Sub]] = None
    min_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_i_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scene_change_detect: Optional[Union[str, H265SceneChangeDetect, Ref, GetAtt, Sub]] = None
    framerate_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    adaptive_quantization: Optional[Union[str, H265AdaptiveQuantization, Ref, GetAtt, Sub]] = None
    tile_width: Optional[Union[int, Ref, GetAtt, Sub]] = None
    filter_settings: Optional[H265FilterSettings] = None
    min_qp: Optional[Union[int, Ref, GetAtt, Sub]] = None
    alternative_transfer_function: Optional[Union[str, H265AlternativeTransferFunction, Ref, GetAtt, Sub]] = None
    color_space_settings: Optional[H265ColorSpaceSettings] = None
    tier: Optional[Union[str, H265Tier, Ref, GetAtt, Sub]] = None
    par_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    fixed_afd: Optional[Union[str, FixedAfd, Ref, GetAtt, Sub]] = None
    gop_size_units: Optional[Union[str, H265GopSizeUnits, Ref, GetAtt, Sub]] = None
    tile_padding: Optional[Union[str, H265TilePadding, Ref, GetAtt, Sub]] = None
    afd_signaling: Optional[Union[str, AfdSignaling, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    par_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rate_control_mode: Optional[Union[str, H265RateControlMode, Ref, GetAtt, Sub]] = None
    scan_type: Optional[Union[str, H265ScanType, Ref, GetAtt, Sub]] = None
    buf_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timecode_insertion: Optional[Union[str, H265TimecodeInsertionBehavior, Ref, GetAtt, Sub]] = None
    deblocking: Optional[Union[str, H265Deblocking, Ref, GetAtt, Sub]] = None
    color_metadata: Optional[Union[str, H265ColorMetadata, Ref, GetAtt, Sub]] = None
    look_ahead_rate_control: Optional[Union[str, H265LookAheadRateControl, Ref, GetAtt, Sub]] = None
    gop_b_reference: Optional[Union[str, H265GopBReference, Ref, GetAtt, Sub]] = None
    level: Optional[Union[str, H265Level, Ref, GetAtt, Sub]] = None
    max_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    treeblock_size: Optional[Union[str, H265TreeblockSize, Ref, GetAtt, Sub]] = None
    subgop_length: Optional[Union[str, H265SubGopLength, Ref, GetAtt, Sub]] = None
    gop_num_b_frames: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Hdr10Settings(PropertyType):
    MAX_CLL = "MaxCll"
    MAX_FALL = "MaxFall"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_cll": "MaxCll",
        "max_fall": "MaxFall",
    }

    max_cll: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_fall: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Hlg2020Settings(PropertyType):
    pass


@dataclass
class HlsAkamaiSettings(PropertyType):
    SALT = "Salt"
    FILECACHE_DURATION = "FilecacheDuration"
    NUM_RETRIES = "NumRetries"
    TOKEN = "Token"
    RESTART_DELAY = "RestartDelay"
    CONNECTION_RETRY_INTERVAL = "ConnectionRetryInterval"
    HTTP_TRANSFER_MODE = "HttpTransferMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "salt": "Salt",
        "filecache_duration": "FilecacheDuration",
        "num_retries": "NumRetries",
        "token": "Token",
        "restart_delay": "RestartDelay",
        "connection_retry_interval": "ConnectionRetryInterval",
        "http_transfer_mode": "HttpTransferMode",
    }

    salt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filecache_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    num_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    restart_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    connection_retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_transfer_mode: Optional[Union[str, HlsAkamaiHttpTransferMode, Ref, GetAtt, Sub]] = None


@dataclass
class HlsBasicPutSettings(PropertyType):
    FILECACHE_DURATION = "FilecacheDuration"
    NUM_RETRIES = "NumRetries"
    RESTART_DELAY = "RestartDelay"
    CONNECTION_RETRY_INTERVAL = "ConnectionRetryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filecache_duration": "FilecacheDuration",
        "num_retries": "NumRetries",
        "restart_delay": "RestartDelay",
        "connection_retry_interval": "ConnectionRetryInterval",
    }

    filecache_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    num_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    restart_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    connection_retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HlsCdnSettings(PropertyType):
    HLS_WEBDAV_SETTINGS = "HlsWebdavSettings"
    HLS_S3_SETTINGS = "HlsS3Settings"
    HLS_AKAMAI_SETTINGS = "HlsAkamaiSettings"
    HLS_BASIC_PUT_SETTINGS = "HlsBasicPutSettings"
    HLS_MEDIA_STORE_SETTINGS = "HlsMediaStoreSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hls_webdav_settings": "HlsWebdavSettings",
        "hls_s3_settings": "HlsS3Settings",
        "hls_akamai_settings": "HlsAkamaiSettings",
        "hls_basic_put_settings": "HlsBasicPutSettings",
        "hls_media_store_settings": "HlsMediaStoreSettings",
    }

    hls_webdav_settings: Optional[HlsWebdavSettings] = None
    hls_s3_settings: Optional[HlsS3Settings] = None
    hls_akamai_settings: Optional[HlsAkamaiSettings] = None
    hls_basic_put_settings: Optional[HlsBasicPutSettings] = None
    hls_media_store_settings: Optional[HlsMediaStoreSettings] = None


@dataclass
class HlsGroupSettings(PropertyType):
    SEGMENTATION_MODE = "SegmentationMode"
    DESTINATION = "Destination"
    CODEC_SPECIFICATION = "CodecSpecification"
    IV_SOURCE = "IvSource"
    TIMED_METADATA_ID3_FRAME = "TimedMetadataId3Frame"
    KEY_FORMAT_VERSIONS = "KeyFormatVersions"
    REDUNDANT_MANIFEST = "RedundantManifest"
    OUTPUT_SELECTION = "OutputSelection"
    KEY_PROVIDER_SETTINGS = "KeyProviderSettings"
    STREAM_INF_RESOLUTION = "StreamInfResolution"
    CAPTION_LANGUAGE_MAPPINGS = "CaptionLanguageMappings"
    HLS_ID3_SEGMENT_TAGGING = "HlsId3SegmentTagging"
    I_FRAME_ONLY_PLAYLISTS = "IFrameOnlyPlaylists"
    CAPTION_LANGUAGE_SETTING = "CaptionLanguageSetting"
    KEEP_SEGMENTS = "KeepSegments"
    CONSTANT_IV = "ConstantIv"
    DIRECTORY_STRUCTURE = "DirectoryStructure"
    ENCRYPTION_TYPE = "EncryptionType"
    AD_MARKERS = "AdMarkers"
    HLS_CDN_SETTINGS = "HlsCdnSettings"
    INDEX_N_SEGMENTS = "IndexNSegments"
    DISCONTINUITY_TAGS = "DiscontinuityTags"
    INPUT_LOSS_ACTION = "InputLossAction"
    MODE = "Mode"
    TS_FILE_MODE = "TsFileMode"
    BASE_URL_MANIFEST1 = "BaseUrlManifest1"
    CLIENT_CACHE = "ClientCache"
    MIN_SEGMENT_LENGTH = "MinSegmentLength"
    KEY_FORMAT = "KeyFormat"
    IV_IN_MANIFEST = "IvInManifest"
    BASE_URL_CONTENT1 = "BaseUrlContent1"
    PROGRAM_DATE_TIME_CLOCK = "ProgramDateTimeClock"
    MANIFEST_COMPRESSION = "ManifestCompression"
    MANIFEST_DURATION_FORMAT = "ManifestDurationFormat"
    TIMED_METADATA_ID3_PERIOD = "TimedMetadataId3Period"
    INCOMPLETE_SEGMENT_BEHAVIOR = "IncompleteSegmentBehavior"
    PROGRAM_DATE_TIME_PERIOD = "ProgramDateTimePeriod"
    SEGMENT_LENGTH = "SegmentLength"
    TIMESTAMP_DELTA_MILLISECONDS = "TimestampDeltaMilliseconds"
    PROGRAM_DATE_TIME = "ProgramDateTime"
    SEGMENTS_PER_SUBDIRECTORY = "SegmentsPerSubdirectory"
    BASE_URL_CONTENT = "BaseUrlContent"
    BASE_URL_MANIFEST = "BaseUrlManifest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_mode": "SegmentationMode",
        "destination": "Destination",
        "codec_specification": "CodecSpecification",
        "iv_source": "IvSource",
        "timed_metadata_id3_frame": "TimedMetadataId3Frame",
        "key_format_versions": "KeyFormatVersions",
        "redundant_manifest": "RedundantManifest",
        "output_selection": "OutputSelection",
        "key_provider_settings": "KeyProviderSettings",
        "stream_inf_resolution": "StreamInfResolution",
        "caption_language_mappings": "CaptionLanguageMappings",
        "hls_id3_segment_tagging": "HlsId3SegmentTagging",
        "i_frame_only_playlists": "IFrameOnlyPlaylists",
        "caption_language_setting": "CaptionLanguageSetting",
        "keep_segments": "KeepSegments",
        "constant_iv": "ConstantIv",
        "directory_structure": "DirectoryStructure",
        "encryption_type": "EncryptionType",
        "ad_markers": "AdMarkers",
        "hls_cdn_settings": "HlsCdnSettings",
        "index_n_segments": "IndexNSegments",
        "discontinuity_tags": "DiscontinuityTags",
        "input_loss_action": "InputLossAction",
        "mode": "Mode",
        "ts_file_mode": "TsFileMode",
        "base_url_manifest1": "BaseUrlManifest1",
        "client_cache": "ClientCache",
        "min_segment_length": "MinSegmentLength",
        "key_format": "KeyFormat",
        "iv_in_manifest": "IvInManifest",
        "base_url_content1": "BaseUrlContent1",
        "program_date_time_clock": "ProgramDateTimeClock",
        "manifest_compression": "ManifestCompression",
        "manifest_duration_format": "ManifestDurationFormat",
        "timed_metadata_id3_period": "TimedMetadataId3Period",
        "incomplete_segment_behavior": "IncompleteSegmentBehavior",
        "program_date_time_period": "ProgramDateTimePeriod",
        "segment_length": "SegmentLength",
        "timestamp_delta_milliseconds": "TimestampDeltaMilliseconds",
        "program_date_time": "ProgramDateTime",
        "segments_per_subdirectory": "SegmentsPerSubdirectory",
        "base_url_content": "BaseUrlContent",
        "base_url_manifest": "BaseUrlManifest",
    }

    segmentation_mode: Optional[Union[str, HlsSegmentationMode, Ref, GetAtt, Sub]] = None
    destination: Optional[OutputLocationRef] = None
    codec_specification: Optional[Union[str, HlsCodecSpecification, Ref, GetAtt, Sub]] = None
    iv_source: Optional[Union[str, HlsIvSource, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_frame: Optional[Union[str, HlsTimedMetadataId3Frame, Ref, GetAtt, Sub]] = None
    key_format_versions: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redundant_manifest: Optional[Union[str, HlsRedundantManifest, Ref, GetAtt, Sub]] = None
    output_selection: Optional[Union[str, HlsOutputSelection, Ref, GetAtt, Sub]] = None
    key_provider_settings: Optional[KeyProviderSettings] = None
    stream_inf_resolution: Optional[Union[str, HlsStreamInfResolution, Ref, GetAtt, Sub]] = None
    caption_language_mappings: Optional[list[CaptionLanguageMapping]] = None
    hls_id3_segment_tagging: Optional[Union[str, HlsId3SegmentTaggingState, Ref, GetAtt, Sub]] = None
    i_frame_only_playlists: Optional[Union[str, IFrameOnlyPlaylistType, Ref, GetAtt, Sub]] = None
    caption_language_setting: Optional[Union[str, HlsCaptionLanguageSetting, Ref, GetAtt, Sub]] = None
    keep_segments: Optional[Union[int, Ref, GetAtt, Sub]] = None
    constant_iv: Optional[Union[str, Ref, GetAtt, Sub]] = None
    directory_structure: Optional[Union[str, HlsDirectoryStructure, Ref, GetAtt, Sub]] = None
    encryption_type: Optional[Union[str, HlsEncryptionType, Ref, GetAtt, Sub]] = None
    ad_markers: Optional[Union[list[str], Ref]] = None
    hls_cdn_settings: Optional[HlsCdnSettings] = None
    index_n_segments: Optional[Union[int, Ref, GetAtt, Sub]] = None
    discontinuity_tags: Optional[Union[str, HlsDiscontinuityTags, Ref, GetAtt, Sub]] = None
    input_loss_action: Optional[Union[str, InputLossActionForHlsOut, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, HlsMode, Ref, GetAtt, Sub]] = None
    ts_file_mode: Optional[Union[str, HlsTsFileMode, Ref, GetAtt, Sub]] = None
    base_url_manifest1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_cache: Optional[Union[str, HlsClientCache, Ref, GetAtt, Sub]] = None
    min_segment_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    key_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iv_in_manifest: Optional[Union[str, HlsIvInManifest, Ref, GetAtt, Sub]] = None
    base_url_content1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    program_date_time_clock: Optional[Union[str, HlsProgramDateTimeClock, Ref, GetAtt, Sub]] = None
    manifest_compression: Optional[Union[str, HlsManifestCompression, Ref, GetAtt, Sub]] = None
    manifest_duration_format: Optional[Union[str, HlsManifestDurationFormat, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    incomplete_segment_behavior: Optional[Union[str, HlsIncompleteSegmentBehavior, Ref, GetAtt, Sub]] = None
    program_date_time_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    segment_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timestamp_delta_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    program_date_time: Optional[Union[str, HlsProgramDateTime, Ref, GetAtt, Sub]] = None
    segments_per_subdirectory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    base_url_content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base_url_manifest: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HlsInputSettings(PropertyType):
    SCTE35_SOURCE = "Scte35Source"
    BUFFER_SEGMENTS = "BufferSegments"
    RETRIES = "Retries"
    BANDWIDTH = "Bandwidth"
    RETRY_INTERVAL = "RetryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scte35_source": "Scte35Source",
        "buffer_segments": "BufferSegments",
        "retries": "Retries",
        "bandwidth": "Bandwidth",
        "retry_interval": "RetryInterval",
    }

    scte35_source: Optional[Union[str, HlsScte35SourceType, Ref, GetAtt, Sub]] = None
    buffer_segments: Optional[Union[int, Ref, GetAtt, Sub]] = None
    retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    bandwidth: Optional[Union[int, Ref, GetAtt, Sub]] = None
    retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HlsMediaStoreSettings(PropertyType):
    FILECACHE_DURATION = "FilecacheDuration"
    NUM_RETRIES = "NumRetries"
    MEDIA_STORE_STORAGE_CLASS = "MediaStoreStorageClass"
    RESTART_DELAY = "RestartDelay"
    CONNECTION_RETRY_INTERVAL = "ConnectionRetryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filecache_duration": "FilecacheDuration",
        "num_retries": "NumRetries",
        "media_store_storage_class": "MediaStoreStorageClass",
        "restart_delay": "RestartDelay",
        "connection_retry_interval": "ConnectionRetryInterval",
    }

    filecache_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    num_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    media_store_storage_class: Optional[Union[str, HlsMediaStoreStorageClass, Ref, GetAtt, Sub]] = None
    restart_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    connection_retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HlsOutputSettings(PropertyType):
    NAME_MODIFIER = "NameModifier"
    HLS_SETTINGS = "HlsSettings"
    H265_PACKAGING_TYPE = "H265PackagingType"
    SEGMENT_MODIFIER = "SegmentModifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name_modifier": "NameModifier",
        "hls_settings": "HlsSettings",
        "h265_packaging_type": "H265PackagingType",
        "segment_modifier": "SegmentModifier",
    }

    name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hls_settings: Optional[HlsSettings] = None
    h265_packaging_type: Optional[Union[str, HlsH265PackagingType, Ref, GetAtt, Sub]] = None
    segment_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HlsS3Settings(PropertyType):
    CANNED_ACL = "CannedAcl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canned_acl": "CannedAcl",
    }

    canned_acl: Optional[Union[str, S3CannedAcl, Ref, GetAtt, Sub]] = None


@dataclass
class HlsSettings(PropertyType):
    STANDARD_HLS_SETTINGS = "StandardHlsSettings"
    AUDIO_ONLY_HLS_SETTINGS = "AudioOnlyHlsSettings"
    FMP4_HLS_SETTINGS = "Fmp4HlsSettings"
    FRAME_CAPTURE_HLS_SETTINGS = "FrameCaptureHlsSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "standard_hls_settings": "StandardHlsSettings",
        "audio_only_hls_settings": "AudioOnlyHlsSettings",
        "fmp4_hls_settings": "Fmp4HlsSettings",
        "frame_capture_hls_settings": "FrameCaptureHlsSettings",
    }

    standard_hls_settings: Optional[StandardHlsSettings] = None
    audio_only_hls_settings: Optional[AudioOnlyHlsSettings] = None
    fmp4_hls_settings: Optional[Fmp4HlsSettings] = None
    frame_capture_hls_settings: Optional[FrameCaptureHlsSettings] = None


@dataclass
class HlsWebdavSettings(PropertyType):
    FILECACHE_DURATION = "FilecacheDuration"
    NUM_RETRIES = "NumRetries"
    RESTART_DELAY = "RestartDelay"
    CONNECTION_RETRY_INTERVAL = "ConnectionRetryInterval"
    HTTP_TRANSFER_MODE = "HttpTransferMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filecache_duration": "FilecacheDuration",
        "num_retries": "NumRetries",
        "restart_delay": "RestartDelay",
        "connection_retry_interval": "ConnectionRetryInterval",
        "http_transfer_mode": "HttpTransferMode",
    }

    filecache_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    num_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    restart_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    connection_retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_transfer_mode: Optional[Union[str, HlsWebdavHttpTransferMode, Ref, GetAtt, Sub]] = None


@dataclass
class HtmlMotionGraphicsSettings(PropertyType):
    pass


@dataclass
class InputAttachment(PropertyType):
    INPUT_ATTACHMENT_NAME = "InputAttachmentName"
    LOGICAL_INTERFACE_NAMES = "LogicalInterfaceNames"
    INPUT_ID = "InputId"
    AUTOMATIC_INPUT_FAILOVER_SETTINGS = "AutomaticInputFailoverSettings"
    INPUT_SETTINGS = "InputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_attachment_name": "InputAttachmentName",
        "logical_interface_names": "LogicalInterfaceNames",
        "input_id": "InputId",
        "automatic_input_failover_settings": "AutomaticInputFailoverSettings",
        "input_settings": "InputSettings",
    }

    input_attachment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logical_interface_names: Optional[Union[list[str], Ref]] = None
    input_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    automatic_input_failover_settings: Optional[AutomaticInputFailoverSettings] = None
    input_settings: Optional[InputSettings] = None


@dataclass
class InputChannelLevel(PropertyType):
    INPUT_CHANNEL = "InputChannel"
    GAIN = "Gain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_channel": "InputChannel",
        "gain": "Gain",
    }

    input_channel: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gain: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InputLocation(PropertyType):
    USERNAME = "Username"
    PASSWORD_PARAM = "PasswordParam"
    URI = "Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password_param": "PasswordParam",
        "uri": "Uri",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_param: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputLossBehavior(PropertyType):
    INPUT_LOSS_IMAGE_COLOR = "InputLossImageColor"
    BLACK_FRAME_MSEC = "BlackFrameMsec"
    INPUT_LOSS_IMAGE_TYPE = "InputLossImageType"
    INPUT_LOSS_IMAGE_SLATE = "InputLossImageSlate"
    REPEAT_FRAME_MSEC = "RepeatFrameMsec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_loss_image_color": "InputLossImageColor",
        "black_frame_msec": "BlackFrameMsec",
        "input_loss_image_type": "InputLossImageType",
        "input_loss_image_slate": "InputLossImageSlate",
        "repeat_frame_msec": "RepeatFrameMsec",
    }

    input_loss_image_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    black_frame_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None
    input_loss_image_type: Optional[Union[str, InputLossImageType, Ref, GetAtt, Sub]] = None
    input_loss_image_slate: Optional[InputLocation] = None
    repeat_frame_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InputLossFailoverSettings(PropertyType):
    INPUT_LOSS_THRESHOLD_MSEC = "InputLossThresholdMsec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_loss_threshold_msec": "InputLossThresholdMsec",
    }

    input_loss_threshold_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InputSettings(PropertyType):
    SCTE35_PID = "Scte35Pid"
    DEBLOCK_FILTER = "DeblockFilter"
    FILTER_STRENGTH = "FilterStrength"
    INPUT_FILTER = "InputFilter"
    SOURCE_END_BEHAVIOR = "SourceEndBehavior"
    VIDEO_SELECTOR = "VideoSelector"
    SMPTE2038_DATA_PREFERENCE = "Smpte2038DataPreference"
    AUDIO_SELECTORS = "AudioSelectors"
    CAPTION_SELECTORS = "CaptionSelectors"
    DENOISE_FILTER = "DenoiseFilter"
    NETWORK_INPUT_SETTINGS = "NetworkInputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scte35_pid": "Scte35Pid",
        "deblock_filter": "DeblockFilter",
        "filter_strength": "FilterStrength",
        "input_filter": "InputFilter",
        "source_end_behavior": "SourceEndBehavior",
        "video_selector": "VideoSelector",
        "smpte2038_data_preference": "Smpte2038DataPreference",
        "audio_selectors": "AudioSelectors",
        "caption_selectors": "CaptionSelectors",
        "denoise_filter": "DenoiseFilter",
        "network_input_settings": "NetworkInputSettings",
    }

    scte35_pid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    deblock_filter: Optional[Union[str, InputDeblockFilter, Ref, GetAtt, Sub]] = None
    filter_strength: Optional[Union[int, Ref, GetAtt, Sub]] = None
    input_filter: Optional[Union[str, InputFilter, Ref, GetAtt, Sub]] = None
    source_end_behavior: Optional[Union[str, InputSourceEndBehavior, Ref, GetAtt, Sub]] = None
    video_selector: Optional[VideoSelector] = None
    smpte2038_data_preference: Optional[Union[str, Smpte2038DataPreference, Ref, GetAtt, Sub]] = None
    audio_selectors: Optional[list[AudioSelector]] = None
    caption_selectors: Optional[list[CaptionSelector]] = None
    denoise_filter: Optional[Union[str, InputDenoiseFilter, Ref, GetAtt, Sub]] = None
    network_input_settings: Optional[NetworkInputSettings] = None


@dataclass
class InputSpecification(PropertyType):
    CODEC = "Codec"
    MAXIMUM_BITRATE = "MaximumBitrate"
    RESOLUTION = "Resolution"

    _property_mappings: ClassVar[dict[str, str]] = {
        "codec": "Codec",
        "maximum_bitrate": "MaximumBitrate",
        "resolution": "Resolution",
    }

    codec: Optional[Union[str, InputCodec, Ref, GetAtt, Sub]] = None
    maximum_bitrate: Optional[Union[str, InputMaximumBitrate, Ref, GetAtt, Sub]] = None
    resolution: Optional[Union[str, InputResolution, Ref, GetAtt, Sub]] = None


@dataclass
class KeyProviderSettings(PropertyType):
    STATIC_KEY_SETTINGS = "StaticKeySettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_key_settings": "StaticKeySettings",
    }

    static_key_settings: Optional[StaticKeySettings] = None


@dataclass
class M2tsSettings(PropertyType):
    ETV_PLATFORM_PID = "EtvPlatformPid"
    PAT_INTERVAL = "PatInterval"
    PROGRAM_NUM = "ProgramNum"
    RATE_MODE = "RateMode"
    KLV_DATA_PIDS = "KlvDataPids"
    NULL_PACKET_BITRATE = "NullPacketBitrate"
    PMT_INTERVAL = "PmtInterval"
    ARIB_CAPTIONS_PID = "AribCaptionsPid"
    ES_RATE_IN_PES = "EsRateInPes"
    VIDEO_PID = "VideoPid"
    TRANSPORT_STREAM_ID = "TransportStreamId"
    EBP_PLACEMENT = "EbpPlacement"
    DVB_SUB_PIDS = "DvbSubPids"
    SEGMENTATION_STYLE = "SegmentationStyle"
    SCTE35_PID = "Scte35Pid"
    AUDIO_STREAM_TYPE = "AudioStreamType"
    KLV = "Klv"
    EBP_LOOKAHEAD_MS = "EbpLookaheadMs"
    SCTE35_PREROLL_PULLUP_MILLISECONDS = "Scte35PrerollPullupMilliseconds"
    DVB_TDT_SETTINGS = "DvbTdtSettings"
    TIMED_METADATA_BEHAVIOR = "TimedMetadataBehavior"
    EBP_AUDIO_INTERVAL = "EbpAudioInterval"
    FRAGMENT_TIME = "FragmentTime"
    DVB_TELETEXT_PID = "DvbTeletextPid"
    SCTE35_CONTROL = "Scte35Control"
    PCR_PERIOD = "PcrPeriod"
    NIELSEN_ID3_BEHAVIOR = "NielsenId3Behavior"
    PCR_PID = "PcrPid"
    SEGMENTATION_TIME = "SegmentationTime"
    CC_DESCRIPTOR = "CcDescriptor"
    AUDIO_FRAMES_PER_PES = "AudioFramesPerPes"
    ABSENT_INPUT_AUDIO_BEHAVIOR = "AbsentInputAudioBehavior"
    BITRATE = "Bitrate"
    PMT_PID = "PmtPid"
    SCTE27_PIDS = "Scte27Pids"
    SEGMENTATION_MARKERS = "SegmentationMarkers"
    DVB_NIT_SETTINGS = "DvbNitSettings"
    DVB_SDT_SETTINGS = "DvbSdtSettings"
    ETV_SIGNAL_PID = "EtvSignalPid"
    ARIB = "Arib"
    BUFFER_MODEL = "BufferModel"
    ECM_PID = "EcmPid"
    TIMED_METADATA_PID = "TimedMetadataPid"
    AUDIO_PIDS = "AudioPids"
    AUDIO_BUFFER_MODEL = "AudioBufferModel"
    EBIF = "Ebif"
    ARIB_CAPTIONS_PID_CONTROL = "AribCaptionsPidControl"
    PCR_CONTROL = "PcrControl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "etv_platform_pid": "EtvPlatformPid",
        "pat_interval": "PatInterval",
        "program_num": "ProgramNum",
        "rate_mode": "RateMode",
        "klv_data_pids": "KlvDataPids",
        "null_packet_bitrate": "NullPacketBitrate",
        "pmt_interval": "PmtInterval",
        "arib_captions_pid": "AribCaptionsPid",
        "es_rate_in_pes": "EsRateInPes",
        "video_pid": "VideoPid",
        "transport_stream_id": "TransportStreamId",
        "ebp_placement": "EbpPlacement",
        "dvb_sub_pids": "DvbSubPids",
        "segmentation_style": "SegmentationStyle",
        "scte35_pid": "Scte35Pid",
        "audio_stream_type": "AudioStreamType",
        "klv": "Klv",
        "ebp_lookahead_ms": "EbpLookaheadMs",
        "scte35_preroll_pullup_milliseconds": "Scte35PrerollPullupMilliseconds",
        "dvb_tdt_settings": "DvbTdtSettings",
        "timed_metadata_behavior": "TimedMetadataBehavior",
        "ebp_audio_interval": "EbpAudioInterval",
        "fragment_time": "FragmentTime",
        "dvb_teletext_pid": "DvbTeletextPid",
        "scte35_control": "Scte35Control",
        "pcr_period": "PcrPeriod",
        "nielsen_id3_behavior": "NielsenId3Behavior",
        "pcr_pid": "PcrPid",
        "segmentation_time": "SegmentationTime",
        "cc_descriptor": "CcDescriptor",
        "audio_frames_per_pes": "AudioFramesPerPes",
        "absent_input_audio_behavior": "AbsentInputAudioBehavior",
        "bitrate": "Bitrate",
        "pmt_pid": "PmtPid",
        "scte27_pids": "Scte27Pids",
        "segmentation_markers": "SegmentationMarkers",
        "dvb_nit_settings": "DvbNitSettings",
        "dvb_sdt_settings": "DvbSdtSettings",
        "etv_signal_pid": "EtvSignalPid",
        "arib": "Arib",
        "buffer_model": "BufferModel",
        "ecm_pid": "EcmPid",
        "timed_metadata_pid": "TimedMetadataPid",
        "audio_pids": "AudioPids",
        "audio_buffer_model": "AudioBufferModel",
        "ebif": "Ebif",
        "arib_captions_pid_control": "AribCaptionsPidControl",
        "pcr_control": "PcrControl",
    }

    etv_platform_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pat_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    program_num: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rate_mode: Optional[Union[str, M2tsRateMode, Ref, GetAtt, Sub]] = None
    klv_data_pids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    null_packet_bitrate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    pmt_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    arib_captions_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    es_rate_in_pes: Optional[Union[str, M2tsEsRateInPes, Ref, GetAtt, Sub]] = None
    video_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transport_stream_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ebp_placement: Optional[Union[str, M2tsEbpPlacement, Ref, GetAtt, Sub]] = None
    dvb_sub_pids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    segmentation_style: Optional[Union[str, M2tsSegmentationStyle, Ref, GetAtt, Sub]] = None
    scte35_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_stream_type: Optional[Union[str, M2tsAudioStreamType, Ref, GetAtt, Sub]] = None
    klv: Optional[Union[str, M2tsKlv, Ref, GetAtt, Sub]] = None
    ebp_lookahead_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scte35_preroll_pullup_milliseconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    dvb_tdt_settings: Optional[DvbTdtSettings] = None
    timed_metadata_behavior: Optional[Union[str, M2tsTimedMetadataBehavior, Ref, GetAtt, Sub]] = None
    ebp_audio_interval: Optional[Union[str, M2tsAudioInterval, Ref, GetAtt, Sub]] = None
    fragment_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    dvb_teletext_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte35_control: Optional[Union[str, M2tsScte35Control, Ref, GetAtt, Sub]] = None
    pcr_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    nielsen_id3_behavior: Optional[Union[str, M2tsNielsenId3Behavior, Ref, GetAtt, Sub]] = None
    pcr_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    segmentation_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    cc_descriptor: Optional[Union[str, M2tsCcDescriptor, Ref, GetAtt, Sub]] = None
    audio_frames_per_pes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    absent_input_audio_behavior: Optional[Union[str, M2tsAbsentInputAudioBehavior, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    pmt_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte27_pids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    segmentation_markers: Optional[Union[str, M2tsSegmentationMarkers, Ref, GetAtt, Sub]] = None
    dvb_nit_settings: Optional[DvbNitSettings] = None
    dvb_sdt_settings: Optional[DvbSdtSettings] = None
    etv_signal_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arib: Optional[Union[str, M2tsArib, Ref, GetAtt, Sub]] = None
    buffer_model: Optional[Union[str, M2tsBufferModel, Ref, GetAtt, Sub]] = None
    ecm_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timed_metadata_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_pids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_buffer_model: Optional[Union[str, M2tsAudioBufferModel, Ref, GetAtt, Sub]] = None
    ebif: Optional[Union[str, M2tsEbifControl, Ref, GetAtt, Sub]] = None
    arib_captions_pid_control: Optional[Union[str, M2tsAribCaptionsPidControl, Ref, GetAtt, Sub]] = None
    pcr_control: Optional[Union[str, M2tsPcrControl, Ref, GetAtt, Sub]] = None


@dataclass
class M3u8Settings(PropertyType):
    PAT_INTERVAL = "PatInterval"
    PROGRAM_NUM = "ProgramNum"
    PCR_PERIOD = "PcrPeriod"
    PMT_INTERVAL = "PmtInterval"
    KLV_DATA_PIDS = "KlvDataPids"
    NIELSEN_ID3_BEHAVIOR = "NielsenId3Behavior"
    PCR_PID = "PcrPid"
    VIDEO_PID = "VideoPid"
    AUDIO_FRAMES_PER_PES = "AudioFramesPerPes"
    TRANSPORT_STREAM_ID = "TransportStreamId"
    PMT_PID = "PmtPid"
    SCTE35_PID = "Scte35Pid"
    SCTE35_BEHAVIOR = "Scte35Behavior"
    KLV_BEHAVIOR = "KlvBehavior"
    ECM_PID = "EcmPid"
    TIMED_METADATA_PID = "TimedMetadataPid"
    AUDIO_PIDS = "AudioPids"
    PCR_CONTROL = "PcrControl"
    TIMED_METADATA_BEHAVIOR = "TimedMetadataBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pat_interval": "PatInterval",
        "program_num": "ProgramNum",
        "pcr_period": "PcrPeriod",
        "pmt_interval": "PmtInterval",
        "klv_data_pids": "KlvDataPids",
        "nielsen_id3_behavior": "NielsenId3Behavior",
        "pcr_pid": "PcrPid",
        "video_pid": "VideoPid",
        "audio_frames_per_pes": "AudioFramesPerPes",
        "transport_stream_id": "TransportStreamId",
        "pmt_pid": "PmtPid",
        "scte35_pid": "Scte35Pid",
        "scte35_behavior": "Scte35Behavior",
        "klv_behavior": "KlvBehavior",
        "ecm_pid": "EcmPid",
        "timed_metadata_pid": "TimedMetadataPid",
        "audio_pids": "AudioPids",
        "pcr_control": "PcrControl",
        "timed_metadata_behavior": "TimedMetadataBehavior",
    }

    pat_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    program_num: Optional[Union[int, Ref, GetAtt, Sub]] = None
    pcr_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    pmt_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    klv_data_pids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nielsen_id3_behavior: Optional[Union[str, M3u8NielsenId3Behavior, Ref, GetAtt, Sub]] = None
    pcr_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    video_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_frames_per_pes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transport_stream_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    pmt_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte35_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scte35_behavior: Optional[Union[str, M3u8Scte35Behavior, Ref, GetAtt, Sub]] = None
    klv_behavior: Optional[Union[str, M3u8KlvBehavior, Ref, GetAtt, Sub]] = None
    ecm_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timed_metadata_pid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audio_pids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pcr_control: Optional[Union[str, M3u8PcrControl, Ref, GetAtt, Sub]] = None
    timed_metadata_behavior: Optional[Union[str, M3u8TimedMetadataBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceCreateSettings(PropertyType):
    MAINTENANCE_DAY = "MaintenanceDay"
    MAINTENANCE_START_TIME = "MaintenanceStartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maintenance_day": "MaintenanceDay",
        "maintenance_start_time": "MaintenanceStartTime",
    }

    maintenance_day: Optional[Union[str, MaintenanceDay, Ref, GetAtt, Sub]] = None
    maintenance_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceUpdateSettings(PropertyType):
    MAINTENANCE_DAY = "MaintenanceDay"
    MAINTENANCE_SCHEDULED_DATE = "MaintenanceScheduledDate"
    MAINTENANCE_START_TIME = "MaintenanceStartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maintenance_day": "MaintenanceDay",
        "maintenance_scheduled_date": "MaintenanceScheduledDate",
        "maintenance_start_time": "MaintenanceStartTime",
    }

    maintenance_day: Optional[Union[str, MaintenanceDay, Ref, GetAtt, Sub]] = None
    maintenance_scheduled_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maintenance_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaPackageGroupSettings(PropertyType):
    DESTINATION = "Destination"
    MEDIAPACKAGE_V2_GROUP_SETTINGS = "MediapackageV2GroupSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "mediapackage_v2_group_settings": "MediapackageV2GroupSettings",
    }

    destination: Optional[OutputLocationRef] = None
    mediapackage_v2_group_settings: Optional[MediaPackageV2GroupSettings] = None


@dataclass
class MediaPackageOutputDestinationSettings(PropertyType):
    CHANNEL_NAME = "ChannelName"
    CHANNEL_ID = "ChannelId"
    CHANNEL_GROUP = "ChannelGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_name": "ChannelName",
        "channel_id": "ChannelId",
        "channel_group": "ChannelGroup",
    }

    channel_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaPackageOutputSettings(PropertyType):
    MEDIA_PACKAGE_V2_DESTINATION_SETTINGS = "MediaPackageV2DestinationSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "media_package_v2_destination_settings": "MediaPackageV2DestinationSettings",
    }

    media_package_v2_destination_settings: Optional[MediaPackageV2DestinationSettings] = None


@dataclass
class MediaPackageV2DestinationSettings(PropertyType):
    AUDIO_RENDITION_SETS = "AudioRenditionSets"
    HLS_DEFAULT = "HlsDefault"
    AUDIO_GROUP_ID = "AudioGroupId"
    HLS_AUTO_SELECT = "HlsAutoSelect"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_rendition_sets": "AudioRenditionSets",
        "hls_default": "HlsDefault",
        "audio_group_id": "AudioGroupId",
        "hls_auto_select": "HlsAutoSelect",
    }

    audio_rendition_sets: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hls_default: Optional[Union[str, HlsDefault, Ref, GetAtt, Sub]] = None
    audio_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hls_auto_select: Optional[Union[str, HlsAutoSelect, Ref, GetAtt, Sub]] = None


@dataclass
class MediaPackageV2GroupSettings(PropertyType):
    CAPTION_LANGUAGE_MAPPINGS = "CaptionLanguageMappings"
    SCTE35_TYPE = "Scte35Type"
    SEGMENT_LENGTH_UNITS = "SegmentLengthUnits"
    TIMED_METADATA_ID3_FRAME = "TimedMetadataId3Frame"
    TIMED_METADATA_ID3_PERIOD = "TimedMetadataId3Period"
    TIMED_METADATA_PASSTHROUGH = "TimedMetadataPassthrough"
    NIELSEN_ID3_BEHAVIOR = "NielsenId3Behavior"
    KLV_BEHAVIOR = "KlvBehavior"
    ID3_BEHAVIOR = "Id3Behavior"
    SEGMENT_LENGTH = "SegmentLength"

    _property_mappings: ClassVar[dict[str, str]] = {
        "caption_language_mappings": "CaptionLanguageMappings",
        "scte35_type": "Scte35Type",
        "segment_length_units": "SegmentLengthUnits",
        "timed_metadata_id3_frame": "TimedMetadataId3Frame",
        "timed_metadata_id3_period": "TimedMetadataId3Period",
        "timed_metadata_passthrough": "TimedMetadataPassthrough",
        "nielsen_id3_behavior": "NielsenId3Behavior",
        "klv_behavior": "KlvBehavior",
        "id3_behavior": "Id3Behavior",
        "segment_length": "SegmentLength",
    }

    caption_language_mappings: Optional[list[CaptionLanguageMapping]] = None
    scte35_type: Optional[Union[str, Scte35Type, Ref, GetAtt, Sub]] = None
    segment_length_units: Optional[Union[str, CmafIngestSegmentLengthUnits, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_frame: Optional[Union[str, CmafTimedMetadataId3Frame, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timed_metadata_passthrough: Optional[Union[str, CmafTimedMetadataPassthrough, Ref, GetAtt, Sub]] = None
    nielsen_id3_behavior: Optional[Union[str, CmafNielsenId3Behavior, Ref, GetAtt, Sub]] = None
    klv_behavior: Optional[Union[str, CmafKLVBehavior, Ref, GetAtt, Sub]] = None
    id3_behavior: Optional[Union[str, CmafId3Behavior, Ref, GetAtt, Sub]] = None
    segment_length: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MotionGraphicsConfiguration(PropertyType):
    MOTION_GRAPHICS_SETTINGS = "MotionGraphicsSettings"
    MOTION_GRAPHICS_INSERTION = "MotionGraphicsInsertion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "motion_graphics_settings": "MotionGraphicsSettings",
        "motion_graphics_insertion": "MotionGraphicsInsertion",
    }

    motion_graphics_settings: Optional[MotionGraphicsSettings] = None
    motion_graphics_insertion: Optional[Union[str, MotionGraphicsInsertion, Ref, GetAtt, Sub]] = None


@dataclass
class MotionGraphicsSettings(PropertyType):
    HTML_MOTION_GRAPHICS_SETTINGS = "HtmlMotionGraphicsSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "html_motion_graphics_settings": "HtmlMotionGraphicsSettings",
    }

    html_motion_graphics_settings: Optional[HtmlMotionGraphicsSettings] = None


@dataclass
class Mp2Settings(PropertyType):
    CODING_MODE = "CodingMode"
    SAMPLE_RATE = "SampleRate"
    BITRATE = "Bitrate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "coding_mode": "CodingMode",
        "sample_rate": "SampleRate",
        "bitrate": "Bitrate",
    }

    coding_mode: Optional[Union[str, Mp2CodingMode, Ref, GetAtt, Sub]] = None
    sample_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Mpeg2FilterSettings(PropertyType):
    TEMPORAL_FILTER_SETTINGS = "TemporalFilterSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "temporal_filter_settings": "TemporalFilterSettings",
    }

    temporal_filter_settings: Optional[TemporalFilterSettings] = None


@dataclass
class Mpeg2Settings(PropertyType):
    TIMECODE_BURNIN_SETTINGS = "TimecodeBurninSettings"
    COLOR_SPACE = "ColorSpace"
    FIXED_AFD = "FixedAfd"
    GOP_SIZE_UNITS = "GopSizeUnits"
    FRAMERATE_NUMERATOR = "FramerateNumerator"
    GOP_CLOSED_CADENCE = "GopClosedCadence"
    AFD_SIGNALING = "AfdSignaling"
    DISPLAY_ASPECT_RATIO = "DisplayAspectRatio"
    SCAN_TYPE = "ScanType"
    TIMECODE_INSERTION = "TimecodeInsertion"
    COLOR_METADATA = "ColorMetadata"
    FRAMERATE_DENOMINATOR = "FramerateDenominator"
    GOP_SIZE = "GopSize"
    ADAPTIVE_QUANTIZATION = "AdaptiveQuantization"
    SUBGOP_LENGTH = "SubgopLength"
    FILTER_SETTINGS = "FilterSettings"
    GOP_NUM_B_FRAMES = "GopNumBFrames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timecode_burnin_settings": "TimecodeBurninSettings",
        "color_space": "ColorSpace",
        "fixed_afd": "FixedAfd",
        "gop_size_units": "GopSizeUnits",
        "framerate_numerator": "FramerateNumerator",
        "gop_closed_cadence": "GopClosedCadence",
        "afd_signaling": "AfdSignaling",
        "display_aspect_ratio": "DisplayAspectRatio",
        "scan_type": "ScanType",
        "timecode_insertion": "TimecodeInsertion",
        "color_metadata": "ColorMetadata",
        "framerate_denominator": "FramerateDenominator",
        "gop_size": "GopSize",
        "adaptive_quantization": "AdaptiveQuantization",
        "subgop_length": "SubgopLength",
        "filter_settings": "FilterSettings",
        "gop_num_b_frames": "GopNumBFrames",
    }

    timecode_burnin_settings: Optional[TimecodeBurninSettings] = None
    color_space: Optional[Union[str, Mpeg2ColorSpace, Ref, GetAtt, Sub]] = None
    fixed_afd: Optional[Union[str, FixedAfd, Ref, GetAtt, Sub]] = None
    gop_size_units: Optional[Union[str, Mpeg2GopSizeUnits, Ref, GetAtt, Sub]] = None
    framerate_numerator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_closed_cadence: Optional[Union[int, Ref, GetAtt, Sub]] = None
    afd_signaling: Optional[Union[str, AfdSignaling, Ref, GetAtt, Sub]] = None
    display_aspect_ratio: Optional[Union[str, Mpeg2DisplayRatio, Ref, GetAtt, Sub]] = None
    scan_type: Optional[Union[str, Mpeg2ScanType, Ref, GetAtt, Sub]] = None
    timecode_insertion: Optional[Union[str, Mpeg2TimecodeInsertionBehavior, Ref, GetAtt, Sub]] = None
    color_metadata: Optional[Union[str, Mpeg2ColorMetadata, Ref, GetAtt, Sub]] = None
    framerate_denominator: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gop_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    adaptive_quantization: Optional[Union[str, Mpeg2AdaptiveQuantization, Ref, GetAtt, Sub]] = None
    subgop_length: Optional[Union[str, Mpeg2SubGopLength, Ref, GetAtt, Sub]] = None
    filter_settings: Optional[Mpeg2FilterSettings] = None
    gop_num_b_frames: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MsSmoothGroupSettings(PropertyType):
    SEGMENTATION_MODE = "SegmentationMode"
    DESTINATION = "Destination"
    EVENT_STOP_BEHAVIOR = "EventStopBehavior"
    FILECACHE_DURATION = "FilecacheDuration"
    CERTIFICATE_MODE = "CertificateMode"
    ACQUISITION_POINT_ID = "AcquisitionPointId"
    STREAM_MANIFEST_BEHAVIOR = "StreamManifestBehavior"
    INPUT_LOSS_ACTION = "InputLossAction"
    FRAGMENT_LENGTH = "FragmentLength"
    RESTART_DELAY = "RestartDelay"
    SPARSE_TRACK_TYPE = "SparseTrackType"
    EVENT_ID_MODE = "EventIdMode"
    TIMESTAMP_OFFSET_MODE = "TimestampOffsetMode"
    AUDIO_ONLY_TIMECODE_CONTROL = "AudioOnlyTimecodeControl"
    NUM_RETRIES = "NumRetries"
    TIMESTAMP_OFFSET = "TimestampOffset"
    EVENT_ID = "EventId"
    SEND_DELAY_MS = "SendDelayMs"
    CONNECTION_RETRY_INTERVAL = "ConnectionRetryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_mode": "SegmentationMode",
        "destination": "Destination",
        "event_stop_behavior": "EventStopBehavior",
        "filecache_duration": "FilecacheDuration",
        "certificate_mode": "CertificateMode",
        "acquisition_point_id": "AcquisitionPointId",
        "stream_manifest_behavior": "StreamManifestBehavior",
        "input_loss_action": "InputLossAction",
        "fragment_length": "FragmentLength",
        "restart_delay": "RestartDelay",
        "sparse_track_type": "SparseTrackType",
        "event_id_mode": "EventIdMode",
        "timestamp_offset_mode": "TimestampOffsetMode",
        "audio_only_timecode_control": "AudioOnlyTimecodeControl",
        "num_retries": "NumRetries",
        "timestamp_offset": "TimestampOffset",
        "event_id": "EventId",
        "send_delay_ms": "SendDelayMs",
        "connection_retry_interval": "ConnectionRetryInterval",
    }

    segmentation_mode: Optional[Union[str, SmoothGroupSegmentationMode, Ref, GetAtt, Sub]] = None
    destination: Optional[OutputLocationRef] = None
    event_stop_behavior: Optional[Union[str, SmoothGroupEventStopBehavior, Ref, GetAtt, Sub]] = None
    filecache_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    certificate_mode: Optional[Union[str, SmoothGroupCertificateMode, Ref, GetAtt, Sub]] = None
    acquisition_point_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_manifest_behavior: Optional[Union[str, SmoothGroupStreamManifestBehavior, Ref, GetAtt, Sub]] = None
    input_loss_action: Optional[Union[str, InputLossActionForMsSmoothOut, Ref, GetAtt, Sub]] = None
    fragment_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    restart_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    sparse_track_type: Optional[Union[str, SmoothGroupSparseTrackType, Ref, GetAtt, Sub]] = None
    event_id_mode: Optional[Union[str, SmoothGroupEventIdMode, Ref, GetAtt, Sub]] = None
    timestamp_offset_mode: Optional[Union[str, SmoothGroupTimestampOffsetMode, Ref, GetAtt, Sub]] = None
    audio_only_timecode_control: Optional[Union[str, SmoothGroupAudioOnlyTimecodeControl, Ref, GetAtt, Sub]] = None
    num_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timestamp_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    send_delay_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None
    connection_retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MsSmoothOutputSettings(PropertyType):
    NAME_MODIFIER = "NameModifier"
    H265_PACKAGING_TYPE = "H265PackagingType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name_modifier": "NameModifier",
        "h265_packaging_type": "H265PackagingType",
    }

    name_modifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    h265_packaging_type: Optional[Union[str, MsSmoothH265PackagingType, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastInputSettings(PropertyType):
    SOURCE_IP_ADDRESS = "SourceIpAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_ip_address": "SourceIpAddress",
    }

    source_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexContainerSettings(PropertyType):
    MULTIPLEX_M2TS_SETTINGS = "MultiplexM2tsSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multiplex_m2ts_settings": "MultiplexM2tsSettings",
    }

    multiplex_m2ts_settings: Optional[MultiplexM2tsSettings] = None


@dataclass
class MultiplexGroupSettings(PropertyType):
    pass


@dataclass
class MultiplexM2tsSettings(PropertyType):
    SCTE35_CONTROL = "Scte35Control"
    PCR_PERIOD = "PcrPeriod"
    NIELSEN_ID3_BEHAVIOR = "NielsenId3Behavior"
    ES_RATE_IN_PES = "EsRateInPes"
    CC_DESCRIPTOR = "CcDescriptor"
    AUDIO_FRAMES_PER_PES = "AudioFramesPerPes"
    ABSENT_INPUT_AUDIO_BEHAVIOR = "AbsentInputAudioBehavior"
    AUDIO_STREAM_TYPE = "AudioStreamType"
    KLV = "Klv"
    ARIB = "Arib"
    AUDIO_BUFFER_MODEL = "AudioBufferModel"
    EBIF = "Ebif"
    SCTE35_PREROLL_PULLUP_MILLISECONDS = "Scte35PrerollPullupMilliseconds"
    PCR_CONTROL = "PcrControl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scte35_control": "Scte35Control",
        "pcr_period": "PcrPeriod",
        "nielsen_id3_behavior": "NielsenId3Behavior",
        "es_rate_in_pes": "EsRateInPes",
        "cc_descriptor": "CcDescriptor",
        "audio_frames_per_pes": "AudioFramesPerPes",
        "absent_input_audio_behavior": "AbsentInputAudioBehavior",
        "audio_stream_type": "AudioStreamType",
        "klv": "Klv",
        "arib": "Arib",
        "audio_buffer_model": "AudioBufferModel",
        "ebif": "Ebif",
        "scte35_preroll_pullup_milliseconds": "Scte35PrerollPullupMilliseconds",
        "pcr_control": "PcrControl",
    }

    scte35_control: Optional[Union[str, M2tsScte35Control, Ref, GetAtt, Sub]] = None
    pcr_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    nielsen_id3_behavior: Optional[Union[str, M2tsNielsenId3Behavior, Ref, GetAtt, Sub]] = None
    es_rate_in_pes: Optional[Union[str, M2tsEsRateInPes, Ref, GetAtt, Sub]] = None
    cc_descriptor: Optional[Union[str, M2tsCcDescriptor, Ref, GetAtt, Sub]] = None
    audio_frames_per_pes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    absent_input_audio_behavior: Optional[Union[str, M2tsAbsentInputAudioBehavior, Ref, GetAtt, Sub]] = None
    audio_stream_type: Optional[Union[str, M2tsAudioStreamType, Ref, GetAtt, Sub]] = None
    klv: Optional[Union[str, M2tsKlv, Ref, GetAtt, Sub]] = None
    arib: Optional[Union[str, M2tsArib, Ref, GetAtt, Sub]] = None
    audio_buffer_model: Optional[Union[str, M2tsAudioBufferModel, Ref, GetAtt, Sub]] = None
    ebif: Optional[Union[str, M2tsEbifControl, Ref, GetAtt, Sub]] = None
    scte35_preroll_pullup_milliseconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    pcr_control: Optional[Union[str, M2tsPcrControl, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexOutputSettings(PropertyType):
    DESTINATION = "Destination"
    CONTAINER_SETTINGS = "ContainerSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "container_settings": "ContainerSettings",
    }

    destination: Optional[OutputLocationRef] = None
    container_settings: Optional[MultiplexContainerSettings] = None


@dataclass
class MultiplexProgramChannelDestinationSettings(PropertyType):
    MULTIPLEX_ID = "MultiplexId"
    PROGRAM_NAME = "ProgramName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multiplex_id": "MultiplexId",
        "program_name": "ProgramName",
    }

    multiplex_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    program_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInputSettings(PropertyType):
    SERVER_VALIDATION = "ServerValidation"
    HLS_INPUT_SETTINGS = "HlsInputSettings"
    MULTICAST_INPUT_SETTINGS = "MulticastInputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_validation": "ServerValidation",
        "hls_input_settings": "HlsInputSettings",
        "multicast_input_settings": "MulticastInputSettings",
    }

    server_validation: Optional[Union[str, NetworkInputServerValidation, Ref, GetAtt, Sub]] = None
    hls_input_settings: Optional[HlsInputSettings] = None
    multicast_input_settings: Optional[MulticastInputSettings] = None


@dataclass
class NielsenCBET(PropertyType):
    CBET_CHECK_DIGIT_STRING = "CbetCheckDigitString"
    CBET_STEPASIDE = "CbetStepaside"
    CSID = "Csid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cbet_check_digit_string": "CbetCheckDigitString",
        "cbet_stepaside": "CbetStepaside",
        "csid": "Csid",
    }

    cbet_check_digit_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cbet_stepaside: Optional[Union[str, NielsenWatermarksCbetStepaside, Ref, GetAtt, Sub]] = None
    csid: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NielsenConfiguration(PropertyType):
    DISTRIBUTOR_ID = "DistributorId"
    NIELSEN_PCM_TO_ID3_TAGGING = "NielsenPcmToId3Tagging"

    _property_mappings: ClassVar[dict[str, str]] = {
        "distributor_id": "DistributorId",
        "nielsen_pcm_to_id3_tagging": "NielsenPcmToId3Tagging",
    }

    distributor_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nielsen_pcm_to_id3_tagging: Optional[Union[str, NielsenPcmToId3TaggingState, Ref, GetAtt, Sub]] = None


@dataclass
class NielsenNaesIiNw(PropertyType):
    TIMEZONE = "Timezone"
    CHECK_DIGIT_STRING = "CheckDigitString"
    SID = "Sid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timezone": "Timezone",
        "check_digit_string": "CheckDigitString",
        "sid": "Sid",
    }

    timezone: Optional[Union[str, NielsenWatermarkTimezones, Ref, GetAtt, Sub]] = None
    check_digit_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sid: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class NielsenWatermarksSettings(PropertyType):
    NIELSEN_DISTRIBUTION_TYPE = "NielsenDistributionType"
    NIELSEN_CBET_SETTINGS = "NielsenCbetSettings"
    NIELSEN_NAES_II_NW_SETTINGS = "NielsenNaesIiNwSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "nielsen_distribution_type": "NielsenDistributionType",
        "nielsen_cbet_settings": "NielsenCbetSettings",
        "nielsen_naes_ii_nw_settings": "NielsenNaesIiNwSettings",
    }

    nielsen_distribution_type: Optional[Union[str, NielsenWatermarksDistributionTypes, Ref, GetAtt, Sub]] = None
    nielsen_cbet_settings: Optional[NielsenCBET] = None
    nielsen_naes_ii_nw_settings: Optional[NielsenNaesIiNw] = None


@dataclass
class Output(PropertyType):
    OUTPUT_SETTINGS = "OutputSettings"
    CAPTION_DESCRIPTION_NAMES = "CaptionDescriptionNames"
    AUDIO_DESCRIPTION_NAMES = "AudioDescriptionNames"
    OUTPUT_NAME = "OutputName"
    VIDEO_DESCRIPTION_NAME = "VideoDescriptionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_settings": "OutputSettings",
        "caption_description_names": "CaptionDescriptionNames",
        "audio_description_names": "AudioDescriptionNames",
        "output_name": "OutputName",
        "video_description_name": "VideoDescriptionName",
    }

    output_settings: Optional[OutputSettings] = None
    caption_description_names: Optional[Union[list[str], Ref]] = None
    audio_description_names: Optional[Union[list[str], Ref]] = None
    output_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    video_description_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputDestination(PropertyType):
    SRT_SETTINGS = "SrtSettings"
    LOGICAL_INTERFACE_NAMES = "LogicalInterfaceNames"
    MULTIPLEX_SETTINGS = "MultiplexSettings"
    ID = "Id"
    SETTINGS = "Settings"
    MEDIA_PACKAGE_SETTINGS = "MediaPackageSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "srt_settings": "SrtSettings",
        "logical_interface_names": "LogicalInterfaceNames",
        "multiplex_settings": "MultiplexSettings",
        "id": "Id",
        "settings": "Settings",
        "media_package_settings": "MediaPackageSettings",
    }

    srt_settings: Optional[list[SrtOutputDestinationSettings]] = None
    logical_interface_names: Optional[Union[list[str], Ref]] = None
    multiplex_settings: Optional[MultiplexProgramChannelDestinationSettings] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    settings: Optional[list[OutputDestinationSettings]] = None
    media_package_settings: Optional[list[MediaPackageOutputDestinationSettings]] = None


@dataclass
class OutputDestinationSettings(PropertyType):
    STREAM_NAME = "StreamName"
    USERNAME = "Username"
    PASSWORD_PARAM = "PasswordParam"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_name": "StreamName",
        "username": "Username",
        "password_param": "PasswordParam",
        "url": "Url",
    }

    stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_param: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputGroup(PropertyType):
    OUTPUTS = "Outputs"
    OUTPUT_GROUP_SETTINGS = "OutputGroupSettings"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outputs": "Outputs",
        "output_group_settings": "OutputGroupSettings",
        "name": "Name",
    }

    outputs: Optional[list[Output]] = None
    output_group_settings: Optional[OutputGroupSettings] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputGroupSettings(PropertyType):
    HLS_GROUP_SETTINGS = "HlsGroupSettings"
    FRAME_CAPTURE_GROUP_SETTINGS = "FrameCaptureGroupSettings"
    MULTIPLEX_GROUP_SETTINGS = "MultiplexGroupSettings"
    SRT_GROUP_SETTINGS = "SrtGroupSettings"
    ARCHIVE_GROUP_SETTINGS = "ArchiveGroupSettings"
    MEDIA_PACKAGE_GROUP_SETTINGS = "MediaPackageGroupSettings"
    UDP_GROUP_SETTINGS = "UdpGroupSettings"
    MS_SMOOTH_GROUP_SETTINGS = "MsSmoothGroupSettings"
    RTMP_GROUP_SETTINGS = "RtmpGroupSettings"
    CMAF_INGEST_GROUP_SETTINGS = "CmafIngestGroupSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hls_group_settings": "HlsGroupSettings",
        "frame_capture_group_settings": "FrameCaptureGroupSettings",
        "multiplex_group_settings": "MultiplexGroupSettings",
        "srt_group_settings": "SrtGroupSettings",
        "archive_group_settings": "ArchiveGroupSettings",
        "media_package_group_settings": "MediaPackageGroupSettings",
        "udp_group_settings": "UdpGroupSettings",
        "ms_smooth_group_settings": "MsSmoothGroupSettings",
        "rtmp_group_settings": "RtmpGroupSettings",
        "cmaf_ingest_group_settings": "CmafIngestGroupSettings",
    }

    hls_group_settings: Optional[HlsGroupSettings] = None
    frame_capture_group_settings: Optional[FrameCaptureGroupSettings] = None
    multiplex_group_settings: Optional[MultiplexGroupSettings] = None
    srt_group_settings: Optional[SrtGroupSettings] = None
    archive_group_settings: Optional[ArchiveGroupSettings] = None
    media_package_group_settings: Optional[MediaPackageGroupSettings] = None
    udp_group_settings: Optional[UdpGroupSettings] = None
    ms_smooth_group_settings: Optional[MsSmoothGroupSettings] = None
    rtmp_group_settings: Optional[RtmpGroupSettings] = None
    cmaf_ingest_group_settings: Optional[CmafIngestGroupSettings] = None


@dataclass
class OutputLocationRef(PropertyType):
    DESTINATION_REF_ID = "DestinationRefId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_ref_id": "DestinationRefId",
    }

    destination_ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputLockingSettings(PropertyType):
    PIPELINE_LOCKING_SETTINGS = "PipelineLockingSettings"
    EPOCH_LOCKING_SETTINGS = "EpochLockingSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pipeline_locking_settings": "PipelineLockingSettings",
        "epoch_locking_settings": "EpochLockingSettings",
    }

    pipeline_locking_settings: Optional[PipelineLockingSettings] = None
    epoch_locking_settings: Optional[EpochLockingSettings] = None


@dataclass
class OutputSettings(PropertyType):
    MEDIA_PACKAGE_OUTPUT_SETTINGS = "MediaPackageOutputSettings"
    MS_SMOOTH_OUTPUT_SETTINGS = "MsSmoothOutputSettings"
    FRAME_CAPTURE_OUTPUT_SETTINGS = "FrameCaptureOutputSettings"
    HLS_OUTPUT_SETTINGS = "HlsOutputSettings"
    RTMP_OUTPUT_SETTINGS = "RtmpOutputSettings"
    UDP_OUTPUT_SETTINGS = "UdpOutputSettings"
    MULTIPLEX_OUTPUT_SETTINGS = "MultiplexOutputSettings"
    CMAF_INGEST_OUTPUT_SETTINGS = "CmafIngestOutputSettings"
    SRT_OUTPUT_SETTINGS = "SrtOutputSettings"
    ARCHIVE_OUTPUT_SETTINGS = "ArchiveOutputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "media_package_output_settings": "MediaPackageOutputSettings",
        "ms_smooth_output_settings": "MsSmoothOutputSettings",
        "frame_capture_output_settings": "FrameCaptureOutputSettings",
        "hls_output_settings": "HlsOutputSettings",
        "rtmp_output_settings": "RtmpOutputSettings",
        "udp_output_settings": "UdpOutputSettings",
        "multiplex_output_settings": "MultiplexOutputSettings",
        "cmaf_ingest_output_settings": "CmafIngestOutputSettings",
        "srt_output_settings": "SrtOutputSettings",
        "archive_output_settings": "ArchiveOutputSettings",
    }

    media_package_output_settings: Optional[MediaPackageOutputSettings] = None
    ms_smooth_output_settings: Optional[MsSmoothOutputSettings] = None
    frame_capture_output_settings: Optional[FrameCaptureOutputSettings] = None
    hls_output_settings: Optional[HlsOutputSettings] = None
    rtmp_output_settings: Optional[RtmpOutputSettings] = None
    udp_output_settings: Optional[UdpOutputSettings] = None
    multiplex_output_settings: Optional[MultiplexOutputSettings] = None
    cmaf_ingest_output_settings: Optional[CmafIngestOutputSettings] = None
    srt_output_settings: Optional[SrtOutputSettings] = None
    archive_output_settings: Optional[ArchiveOutputSettings] = None


@dataclass
class PassThroughSettings(PropertyType):
    pass


@dataclass
class PipelineLockingSettings(PropertyType):
    pass


@dataclass
class RawSettings(PropertyType):
    pass


@dataclass
class Rec601Settings(PropertyType):
    pass


@dataclass
class Rec709Settings(PropertyType):
    pass


@dataclass
class RemixSettings(PropertyType):
    CHANNELS_OUT = "ChannelsOut"
    CHANNEL_MAPPINGS = "ChannelMappings"
    CHANNELS_IN = "ChannelsIn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channels_out": "ChannelsOut",
        "channel_mappings": "ChannelMappings",
        "channels_in": "ChannelsIn",
    }

    channels_out: Optional[Union[int, Ref, GetAtt, Sub]] = None
    channel_mappings: Optional[list[AudioChannelMapping]] = None
    channels_in: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RtmpCaptionInfoDestinationSettings(PropertyType):
    pass


@dataclass
class RtmpGroupSettings(PropertyType):
    AUTHENTICATION_SCHEME = "AuthenticationScheme"
    CACHE_LENGTH = "CacheLength"
    AD_MARKERS = "AdMarkers"
    INCLUDE_FILLER_NAL_UNITS = "IncludeFillerNalUnits"
    INPUT_LOSS_ACTION = "InputLossAction"
    RESTART_DELAY = "RestartDelay"
    CAPTION_DATA = "CaptionData"
    CACHE_FULL_BEHAVIOR = "CacheFullBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_scheme": "AuthenticationScheme",
        "cache_length": "CacheLength",
        "ad_markers": "AdMarkers",
        "include_filler_nal_units": "IncludeFillerNalUnits",
        "input_loss_action": "InputLossAction",
        "restart_delay": "RestartDelay",
        "caption_data": "CaptionData",
        "cache_full_behavior": "CacheFullBehavior",
    }

    authentication_scheme: Optional[Union[str, AuthenticationScheme, Ref, GetAtt, Sub]] = None
    cache_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ad_markers: Optional[Union[list[str], Ref]] = None
    include_filler_nal_units: Optional[Union[str, IncludeFillerNalUnits, Ref, GetAtt, Sub]] = None
    input_loss_action: Optional[Union[str, InputLossActionForRtmpOut, Ref, GetAtt, Sub]] = None
    restart_delay: Optional[Union[int, Ref, GetAtt, Sub]] = None
    caption_data: Optional[Union[str, RtmpCaptionData, Ref, GetAtt, Sub]] = None
    cache_full_behavior: Optional[Union[str, RtmpCacheFullBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class RtmpOutputSettings(PropertyType):
    DESTINATION = "Destination"
    CERTIFICATE_MODE = "CertificateMode"
    NUM_RETRIES = "NumRetries"
    CONNECTION_RETRY_INTERVAL = "ConnectionRetryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "certificate_mode": "CertificateMode",
        "num_retries": "NumRetries",
        "connection_retry_interval": "ConnectionRetryInterval",
    }

    destination: Optional[OutputLocationRef] = None
    certificate_mode: Optional[Union[str, RtmpOutputCertificateMode, Ref, GetAtt, Sub]] = None
    num_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    connection_retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Scte20PlusEmbeddedDestinationSettings(PropertyType):
    pass


@dataclass
class Scte20SourceSettings(PropertyType):
    SOURCE608_CHANNEL_NUMBER = "Source608ChannelNumber"
    CONVERT608_TO708 = "Convert608To708"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source608_channel_number": "Source608ChannelNumber",
        "convert608_to708": "Convert608To708",
    }

    source608_channel_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    convert608_to708: Optional[Union[str, Scte20Convert608To708, Ref, GetAtt, Sub]] = None


@dataclass
class Scte27DestinationSettings(PropertyType):
    pass


@dataclass
class Scte27SourceSettings(PropertyType):
    OCR_LANGUAGE = "OcrLanguage"
    PID = "Pid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ocr_language": "OcrLanguage",
        "pid": "Pid",
    }

    ocr_language: Optional[Union[str, Scte27OcrLanguage, Ref, GetAtt, Sub]] = None
    pid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Scte35SpliceInsert(PropertyType):
    AD_AVAIL_OFFSET = "AdAvailOffset"
    WEB_DELIVERY_ALLOWED_FLAG = "WebDeliveryAllowedFlag"
    NO_REGIONAL_BLACKOUT_FLAG = "NoRegionalBlackoutFlag"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_avail_offset": "AdAvailOffset",
        "web_delivery_allowed_flag": "WebDeliveryAllowedFlag",
        "no_regional_blackout_flag": "NoRegionalBlackoutFlag",
    }

    ad_avail_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    web_delivery_allowed_flag: Optional[Union[str, Scte35SpliceInsertWebDeliveryAllowedBehavior, Ref, GetAtt, Sub]] = None
    no_regional_blackout_flag: Optional[Union[str, Scte35SpliceInsertNoRegionalBlackoutBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class Scte35TimeSignalApos(PropertyType):
    AD_AVAIL_OFFSET = "AdAvailOffset"
    WEB_DELIVERY_ALLOWED_FLAG = "WebDeliveryAllowedFlag"
    NO_REGIONAL_BLACKOUT_FLAG = "NoRegionalBlackoutFlag"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_avail_offset": "AdAvailOffset",
        "web_delivery_allowed_flag": "WebDeliveryAllowedFlag",
        "no_regional_blackout_flag": "NoRegionalBlackoutFlag",
    }

    ad_avail_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None
    web_delivery_allowed_flag: Optional[Union[str, Scte35AposWebDeliveryAllowedBehavior, Ref, GetAtt, Sub]] = None
    no_regional_blackout_flag: Optional[Union[str, Scte35AposNoRegionalBlackoutBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class SmpteTtDestinationSettings(PropertyType):
    pass


@dataclass
class SrtGroupSettings(PropertyType):
    INPUT_LOSS_ACTION = "InputLossAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_loss_action": "InputLossAction",
    }

    input_loss_action: Optional[Union[str, InputLossActionForUdpOut, Ref, GetAtt, Sub]] = None


@dataclass
class SrtOutputDestinationSettings(PropertyType):
    STREAM_ID = "StreamId"
    ENCRYPTION_PASSPHRASE_SECRET_ARN = "EncryptionPassphraseSecretArn"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_id": "StreamId",
        "encryption_passphrase_secret_arn": "EncryptionPassphraseSecretArn",
        "url": "Url",
    }

    stream_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_passphrase_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SrtOutputSettings(PropertyType):
    ENCRYPTION_TYPE = "EncryptionType"
    DESTINATION = "Destination"
    CONTAINER_SETTINGS = "ContainerSettings"
    BUFFER_MSEC = "BufferMsec"
    LATENCY = "Latency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "destination": "Destination",
        "container_settings": "ContainerSettings",
        "buffer_msec": "BufferMsec",
        "latency": "Latency",
    }

    encryption_type: Optional[Union[str, SrtEncryptionType, Ref, GetAtt, Sub]] = None
    destination: Optional[OutputLocationRef] = None
    container_settings: Optional[UdpContainerSettings] = None
    buffer_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None
    latency: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StandardHlsSettings(PropertyType):
    AUDIO_RENDITION_SETS = "AudioRenditionSets"
    M3U8_SETTINGS = "M3u8Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_rendition_sets": "AudioRenditionSets",
        "m3u8_settings": "M3u8Settings",
    }

    audio_rendition_sets: Optional[Union[str, Ref, GetAtt, Sub]] = None
    m3u8_settings: Optional[M3u8Settings] = None


@dataclass
class StaticKeySettings(PropertyType):
    KEY_PROVIDER_SERVER = "KeyProviderServer"
    STATIC_KEY_VALUE = "StaticKeyValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_provider_server": "KeyProviderServer",
        "static_key_value": "StaticKeyValue",
    }

    key_provider_server: Optional[InputLocation] = None
    static_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TeletextDestinationSettings(PropertyType):
    pass


@dataclass
class TeletextSourceSettings(PropertyType):
    OUTPUT_RECTANGLE = "OutputRectangle"
    PAGE_NUMBER = "PageNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_rectangle": "OutputRectangle",
        "page_number": "PageNumber",
    }

    output_rectangle: Optional[CaptionRectangle] = None
    page_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TemporalFilterSettings(PropertyType):
    POST_FILTER_SHARPENING = "PostFilterSharpening"
    STRENGTH = "Strength"

    _property_mappings: ClassVar[dict[str, str]] = {
        "post_filter_sharpening": "PostFilterSharpening",
        "strength": "Strength",
    }

    post_filter_sharpening: Optional[Union[str, TemporalFilterPostFilterSharpening, Ref, GetAtt, Sub]] = None
    strength: Optional[Union[str, TemporalFilterStrength, Ref, GetAtt, Sub]] = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, ThumbnailState, Ref, GetAtt, Sub]] = None


@dataclass
class TimecodeBurninSettings(PropertyType):
    FONT_SIZE = "FontSize"
    POSITION = "Position"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "font_size": "FontSize",
        "position": "Position",
        "prefix": "Prefix",
    }

    font_size: Optional[Union[str, TimecodeBurninFontSize, Ref, GetAtt, Sub]] = None
    position: Optional[Union[str, TimecodeBurninPosition, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimecodeConfig(PropertyType):
    SYNC_THRESHOLD = "SyncThreshold"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sync_threshold": "SyncThreshold",
        "source": "Source",
    }

    sync_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, TimecodeConfigSource, Ref, GetAtt, Sub]] = None


@dataclass
class TtmlDestinationSettings(PropertyType):
    STYLE_CONTROL = "StyleControl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "style_control": "StyleControl",
    }

    style_control: Optional[Union[str, TtmlDestinationStyleControl, Ref, GetAtt, Sub]] = None


@dataclass
class UdpContainerSettings(PropertyType):
    M2TS_SETTINGS = "M2tsSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "m2ts_settings": "M2tsSettings",
    }

    m2ts_settings: Optional[M2tsSettings] = None


@dataclass
class UdpGroupSettings(PropertyType):
    TIMED_METADATA_ID3_FRAME = "TimedMetadataId3Frame"
    TIMED_METADATA_ID3_PERIOD = "TimedMetadataId3Period"
    INPUT_LOSS_ACTION = "InputLossAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timed_metadata_id3_frame": "TimedMetadataId3Frame",
        "timed_metadata_id3_period": "TimedMetadataId3Period",
        "input_loss_action": "InputLossAction",
    }

    timed_metadata_id3_frame: Optional[Union[str, UdpTimedMetadataId3Frame, Ref, GetAtt, Sub]] = None
    timed_metadata_id3_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    input_loss_action: Optional[Union[str, InputLossActionForUdpOut, Ref, GetAtt, Sub]] = None


@dataclass
class UdpOutputSettings(PropertyType):
    DESTINATION = "Destination"
    FEC_OUTPUT_SETTINGS = "FecOutputSettings"
    CONTAINER_SETTINGS = "ContainerSettings"
    BUFFER_MSEC = "BufferMsec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "fec_output_settings": "FecOutputSettings",
        "container_settings": "ContainerSettings",
        "buffer_msec": "BufferMsec",
    }

    destination: Optional[OutputLocationRef] = None
    fec_output_settings: Optional[FecOutputSettings] = None
    container_settings: Optional[UdpContainerSettings] = None
    buffer_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VideoBlackFailoverSettings(PropertyType):
    VIDEO_BLACK_THRESHOLD_MSEC = "VideoBlackThresholdMsec"
    BLACK_DETECT_THRESHOLD = "BlackDetectThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "video_black_threshold_msec": "VideoBlackThresholdMsec",
        "black_detect_threshold": "BlackDetectThreshold",
    }

    video_black_threshold_msec: Optional[Union[int, Ref, GetAtt, Sub]] = None
    black_detect_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class VideoCodecSettings(PropertyType):
    MPEG2_SETTINGS = "Mpeg2Settings"
    FRAME_CAPTURE_SETTINGS = "FrameCaptureSettings"
    H264_SETTINGS = "H264Settings"
    H265_SETTINGS = "H265Settings"
    AV1_SETTINGS = "Av1Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mpeg2_settings": "Mpeg2Settings",
        "frame_capture_settings": "FrameCaptureSettings",
        "h264_settings": "H264Settings",
        "h265_settings": "H265Settings",
        "av1_settings": "Av1Settings",
    }

    mpeg2_settings: Optional[Mpeg2Settings] = None
    frame_capture_settings: Optional[FrameCaptureSettings] = None
    h264_settings: Optional[H264Settings] = None
    h265_settings: Optional[H265Settings] = None
    av1_settings: Optional[Av1Settings] = None


@dataclass
class VideoDescription(PropertyType):
    SCALING_BEHAVIOR = "ScalingBehavior"
    RESPOND_TO_AFD = "RespondToAfd"
    HEIGHT = "Height"
    SHARPNESS = "Sharpness"
    WIDTH = "Width"
    CODEC_SETTINGS = "CodecSettings"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scaling_behavior": "ScalingBehavior",
        "respond_to_afd": "RespondToAfd",
        "height": "Height",
        "sharpness": "Sharpness",
        "width": "Width",
        "codec_settings": "CodecSettings",
        "name": "Name",
    }

    scaling_behavior: Optional[Union[str, VideoDescriptionScalingBehavior, Ref, GetAtt, Sub]] = None
    respond_to_afd: Optional[Union[str, VideoDescriptionRespondToAfd, Ref, GetAtt, Sub]] = None
    height: Optional[Union[int, Ref, GetAtt, Sub]] = None
    sharpness: Optional[Union[int, Ref, GetAtt, Sub]] = None
    width: Optional[Union[int, Ref, GetAtt, Sub]] = None
    codec_settings: Optional[VideoCodecSettings] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VideoSelector(PropertyType):
    COLOR_SPACE_SETTINGS = "ColorSpaceSettings"
    SELECTOR_SETTINGS = "SelectorSettings"
    COLOR_SPACE = "ColorSpace"
    COLOR_SPACE_USAGE = "ColorSpaceUsage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "color_space_settings": "ColorSpaceSettings",
        "selector_settings": "SelectorSettings",
        "color_space": "ColorSpace",
        "color_space_usage": "ColorSpaceUsage",
    }

    color_space_settings: Optional[VideoSelectorColorSpaceSettings] = None
    selector_settings: Optional[VideoSelectorSettings] = None
    color_space: Optional[Union[str, VideoSelectorColorSpace, Ref, GetAtt, Sub]] = None
    color_space_usage: Optional[Union[str, VideoSelectorColorSpaceUsage, Ref, GetAtt, Sub]] = None


@dataclass
class VideoSelectorColorSpaceSettings(PropertyType):
    HDR10_SETTINGS = "Hdr10Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hdr10_settings": "Hdr10Settings",
    }

    hdr10_settings: Optional[Hdr10Settings] = None


@dataclass
class VideoSelectorPid(PropertyType):
    PID = "Pid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pid": "Pid",
    }

    pid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VideoSelectorProgramId(PropertyType):
    PROGRAM_ID = "ProgramId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "program_id": "ProgramId",
    }

    program_id: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VideoSelectorSettings(PropertyType):
    VIDEO_SELECTOR_PROGRAM_ID = "VideoSelectorProgramId"
    VIDEO_SELECTOR_PID = "VideoSelectorPid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "video_selector_program_id": "VideoSelectorProgramId",
        "video_selector_pid": "VideoSelectorPid",
    }

    video_selector_program_id: Optional[VideoSelectorProgramId] = None
    video_selector_pid: Optional[VideoSelectorPid] = None


@dataclass
class VpcOutputSettings(PropertyType):
    PUBLIC_ADDRESS_ALLOCATION_IDS = "PublicAddressAllocationIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "public_address_allocation_ids": "PublicAddressAllocationIds",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    public_address_allocation_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class WavSettings(PropertyType):
    CODING_MODE = "CodingMode"
    SAMPLE_RATE = "SampleRate"
    BIT_DEPTH = "BitDepth"

    _property_mappings: ClassVar[dict[str, str]] = {
        "coding_mode": "CodingMode",
        "sample_rate": "SampleRate",
        "bit_depth": "BitDepth",
    }

    coding_mode: Optional[Union[str, WavCodingMode, Ref, GetAtt, Sub]] = None
    sample_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    bit_depth: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class WebvttDestinationSettings(PropertyType):
    STYLE_CONTROL = "StyleControl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "style_control": "StyleControl",
    }

    style_control: Optional[Union[str, WebvttDestinationStyleControl, Ref, GetAtt, Sub]] = None

