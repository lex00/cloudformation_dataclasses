"""PropertyTypes for AWS::MediaConvert::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AacAudioDescriptionBroadcasterMix:
    """AacAudioDescriptionBroadcasterMix enum values."""

    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NORMAL = "NORMAL"


class AacCodecProfile:
    """AacCodecProfile enum values."""

    LC = "LC"
    HEV1 = "HEV1"
    HEV2 = "HEV2"
    XHE = "XHE"


class AacCodingMode:
    """AacCodingMode enum values."""

    AD_RECEIVER_MIX = "AD_RECEIVER_MIX"
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_5_1 = "CODING_MODE_5_1"


class AacLoudnessMeasurementMode:
    """AacLoudnessMeasurementMode enum values."""

    PROGRAM = "PROGRAM"
    ANCHOR = "ANCHOR"


class AacRateControlMode:
    """AacRateControlMode enum values."""

    CBR = "CBR"
    VBR = "VBR"


class AacRawFormat:
    """AacRawFormat enum values."""

    LATM_LOAS = "LATM_LOAS"
    NONE = "NONE"


class AacSpecification:
    """AacSpecification enum values."""

    MPEG2 = "MPEG2"
    MPEG4 = "MPEG4"


class AacVbrQuality:
    """AacVbrQuality enum values."""

    LOW = "LOW"
    MEDIUM_LOW = "MEDIUM_LOW"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    HIGH = "HIGH"


class Ac3BitstreamMode:
    """Ac3BitstreamMode enum values."""

    COMPLETE_MAIN = "COMPLETE_MAIN"
    COMMENTARY = "COMMENTARY"
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


class Ac3DynamicRangeCompressionLine:
    """Ac3DynamicRangeCompressionLine enum values."""

    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"
    NONE = "NONE"


class Ac3DynamicRangeCompressionProfile:
    """Ac3DynamicRangeCompressionProfile enum values."""

    FILM_STANDARD = "FILM_STANDARD"
    NONE = "NONE"


class Ac3DynamicRangeCompressionRf:
    """Ac3DynamicRangeCompressionRf enum values."""

    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"
    NONE = "NONE"


class Ac3LfeFilter:
    """Ac3LfeFilter enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Ac3MetadataControl:
    """Ac3MetadataControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AccelerationMode:
    """AccelerationMode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    PREFERRED = "PREFERRED"


class AccelerationStatus:
    """AccelerationStatus enum values."""

    NOT_APPLICABLE = "NOT_APPLICABLE"
    IN_PROGRESS = "IN_PROGRESS"
    ACCELERATED = "ACCELERATED"
    NOT_ACCELERATED = "NOT_ACCELERATED"


class AdvancedInputFilter:
    """AdvancedInputFilter enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AdvancedInputFilterAddTexture:
    """AdvancedInputFilterAddTexture enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AdvancedInputFilterSharpen:
    """AdvancedInputFilterSharpen enum values."""

    OFF = "OFF"
    LOW = "LOW"
    HIGH = "HIGH"


class AfdSignaling:
    """AfdSignaling enum values."""

    NONE = "NONE"
    AUTO = "AUTO"
    FIXED = "FIXED"


class AlphaBehavior:
    """AlphaBehavior enum values."""

    DISCARD = "DISCARD"
    REMAP_TO_LUMA = "REMAP_TO_LUMA"


class AncillaryConvert608To708:
    """AncillaryConvert608To708 enum values."""

    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class AncillaryTerminateCaptions:
    """AncillaryTerminateCaptions enum values."""

    END_OF_INPUT = "END_OF_INPUT"
    DISABLED = "DISABLED"


class AntiAlias:
    """AntiAlias enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AudioChannelTag:
    """AudioChannelTag enum values."""

    L = "L"
    R = "R"
    C = "C"
    LFE = "LFE"
    LS = "LS"
    RS = "RS"
    LC = "LC"
    RC = "RC"
    CS = "CS"
    LSD = "LSD"
    RSD = "RSD"
    TCS = "TCS"
    VHL = "VHL"
    VHC = "VHC"
    VHR = "VHR"
    TBL = "TBL"
    TBC = "TBC"
    TBR = "TBR"
    RSL = "RSL"
    RSR = "RSR"
    LW = "LW"
    RW = "RW"
    LFE2 = "LFE2"
    LT = "LT"
    RT = "RT"
    HI = "HI"
    NAR = "NAR"
    M = "M"


class AudioCodec:
    """AudioCodec enum values."""

    AAC = "AAC"
    MP2 = "MP2"
    MP3 = "MP3"
    WAV = "WAV"
    AIFF = "AIFF"
    AC3 = "AC3"
    EAC3 = "EAC3"
    EAC3_ATMOS = "EAC3_ATMOS"
    VORBIS = "VORBIS"
    OPUS = "OPUS"
    PASSTHROUGH = "PASSTHROUGH"
    FLAC = "FLAC"


class AudioDefaultSelection:
    """AudioDefaultSelection enum values."""

    DEFAULT = "DEFAULT"
    NOT_DEFAULT = "NOT_DEFAULT"


class AudioDurationCorrection:
    """AudioDurationCorrection enum values."""

    DISABLED = "DISABLED"
    AUTO = "AUTO"
    TRACK = "TRACK"
    FRAME = "FRAME"
    FORCE = "FORCE"


class AudioLanguageCodeControl:
    """AudioLanguageCodeControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioNormalizationAlgorithm:
    """AudioNormalizationAlgorithm enum values."""

    ITU_BS_1770_1 = "ITU_BS_1770_1"
    ITU_BS_1770_2 = "ITU_BS_1770_2"
    ITU_BS_1770_3 = "ITU_BS_1770_3"
    ITU_BS_1770_4 = "ITU_BS_1770_4"


class AudioNormalizationAlgorithmControl:
    """AudioNormalizationAlgorithmControl enum values."""

    CORRECT_AUDIO = "CORRECT_AUDIO"
    MEASURE_ONLY = "MEASURE_ONLY"


class AudioNormalizationLoudnessLogging:
    """AudioNormalizationLoudnessLogging enum values."""

    LOG = "LOG"
    DONT_LOG = "DONT_LOG"


class AudioNormalizationPeakCalculation:
    """AudioNormalizationPeakCalculation enum values."""

    TRUE_PEAK = "TRUE_PEAK"
    NONE = "NONE"


class AudioSelectorType:
    """AudioSelectorType enum values."""

    PID = "PID"
    TRACK = "TRACK"
    LANGUAGE_CODE = "LANGUAGE_CODE"
    HLS_RENDITION_GROUP = "HLS_RENDITION_GROUP"
    ALL_PCM = "ALL_PCM"
    STREAM = "STREAM"


class AudioTypeControl:
    """AudioTypeControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Av1AdaptiveQuantization:
    """Av1AdaptiveQuantization enum values."""

    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class Av1BitDepth:
    """Av1BitDepth enum values."""

    BIT_8 = "BIT_8"
    BIT_10 = "BIT_10"


class Av1FilmGrainSynthesis:
    """Av1FilmGrainSynthesis enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Av1FramerateControl:
    """Av1FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Av1FramerateConversionAlgorithm:
    """Av1FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Av1RateControlMode:
    """Av1RateControlMode enum values."""

    QVBR = "QVBR"


class Av1SpatialAdaptiveQuantization:
    """Av1SpatialAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AvcIntraClass:
    """AvcIntraClass enum values."""

    CLASS_50 = "CLASS_50"
    CLASS_100 = "CLASS_100"
    CLASS_200 = "CLASS_200"
    CLASS_4K_2K = "CLASS_4K_2K"


class AvcIntraFramerateControl:
    """AvcIntraFramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class AvcIntraFramerateConversionAlgorithm:
    """AvcIntraFramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class AvcIntraInterlaceMode:
    """AvcIntraInterlaceMode enum values."""

    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class AvcIntraScanTypeConversionMode:
    """AvcIntraScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class AvcIntraSlowPal:
    """AvcIntraSlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AvcIntraTelecine:
    """AvcIntraTelecine enum values."""

    NONE = "NONE"
    HARD = "HARD"


class AvcIntraUhdQualityTuningLevel:
    """AvcIntraUhdQualityTuningLevel enum values."""

    SINGLE_PASS = "SINGLE_PASS"
    MULTI_PASS = "MULTI_PASS"


class BandwidthReductionFilterSharpening:
    """BandwidthReductionFilterSharpening enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    OFF = "OFF"


class BandwidthReductionFilterStrength:
    """BandwidthReductionFilterStrength enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    AUTO = "AUTO"
    OFF = "OFF"


class BillingTagsSource:
    """BillingTagsSource enum values."""

    QUEUE = "QUEUE"
    PRESET = "PRESET"
    JOB_TEMPLATE = "JOB_TEMPLATE"
    JOB = "JOB"


class BurnInSubtitleStylePassthrough:
    """BurnInSubtitleStylePassthrough enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BurninSubtitleAlignment:
    """BurninSubtitleAlignment enum values."""

    CENTERED = "CENTERED"
    LEFT = "LEFT"
    AUTO = "AUTO"


class BurninSubtitleApplyFontColor:
    """BurninSubtitleApplyFontColor enum values."""

    WHITE_TEXT_ONLY = "WHITE_TEXT_ONLY"
    ALL_TEXT = "ALL_TEXT"


class BurninSubtitleBackgroundColor:
    """BurninSubtitleBackgroundColor enum values."""

    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class BurninSubtitleFallbackFont:
    """BurninSubtitleFallbackFont enum values."""

    BEST_MATCH = "BEST_MATCH"
    MONOSPACED_SANSSERIF = "MONOSPACED_SANSSERIF"
    MONOSPACED_SERIF = "MONOSPACED_SERIF"
    PROPORTIONAL_SANSSERIF = "PROPORTIONAL_SANSSERIF"
    PROPORTIONAL_SERIF = "PROPORTIONAL_SERIF"


class BurninSubtitleFontColor:
    """BurninSubtitleFontColor enum values."""

    WHITE = "WHITE"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    HEX = "HEX"
    AUTO = "AUTO"


class BurninSubtitleOutlineColor:
    """BurninSubtitleOutlineColor enum values."""

    BLACK = "BLACK"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    AUTO = "AUTO"


class BurninSubtitleShadowColor:
    """BurninSubtitleShadowColor enum values."""

    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class BurninSubtitleTeletextSpacing:
    """BurninSubtitleTeletextSpacing enum values."""

    FIXED_GRID = "FIXED_GRID"
    PROPORTIONAL = "PROPORTIONAL"
    AUTO = "AUTO"


class CaptionDestinationType:
    """CaptionDestinationType enum values."""

    BURN_IN = "BURN_IN"
    DVB_SUB = "DVB_SUB"
    EMBEDDED = "EMBEDDED"
    EMBEDDED_PLUS_SCTE20 = "EMBEDDED_PLUS_SCTE20"
    IMSC = "IMSC"
    SCTE20_PLUS_EMBEDDED = "SCTE20_PLUS_EMBEDDED"
    SCC = "SCC"
    SRT = "SRT"
    SMI = "SMI"
    TELETEXT = "TELETEXT"
    TTML = "TTML"
    WEBVTT = "WEBVTT"


class CaptionSourceByteRateLimit:
    """CaptionSourceByteRateLimit enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CaptionSourceConvertPaintOnToPopOn:
    """CaptionSourceConvertPaintOnToPopOn enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CaptionSourceType:
    """CaptionSourceType enum values."""

    ANCILLARY = "ANCILLARY"
    DVB_SUB = "DVB_SUB"
    EMBEDDED = "EMBEDDED"
    SCTE20 = "SCTE20"
    SCC = "SCC"
    TTML = "TTML"
    STL = "STL"
    SRT = "SRT"
    SMI = "SMI"
    SMPTE_TT = "SMPTE_TT"
    TELETEXT = "TELETEXT"
    NULL_SOURCE = "NULL_SOURCE"
    IMSC = "IMSC"
    WEBVTT = "WEBVTT"
    TT_3GPP = "TT_3GPP"


class CaptionSourceUpconvertSTLToTeletext:
    """CaptionSourceUpconvertSTLToTeletext enum values."""

    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class ChromaPositionMode:
    """ChromaPositionMode enum values."""

    AUTO = "AUTO"
    FORCE_CENTER = "FORCE_CENTER"
    FORCE_TOP_LEFT = "FORCE_TOP_LEFT"


class CmafClientCache:
    """CmafClientCache enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafCodecSpecification:
    """CmafCodecSpecification enum values."""

    RFC_6381 = "RFC_6381"
    RFC_4281 = "RFC_4281"


class CmafEncryptionType:
    """CmafEncryptionType enum values."""

    SAMPLE_AES = "SAMPLE_AES"
    AES_CTR = "AES_CTR"


class CmafImageBasedTrickPlay:
    """CmafImageBasedTrickPlay enum values."""

    NONE = "NONE"
    THUMBNAIL = "THUMBNAIL"
    THUMBNAIL_AND_FULLFRAME = "THUMBNAIL_AND_FULLFRAME"
    ADVANCED = "ADVANCED"


class CmafInitializationVectorInManifest:
    """CmafInitializationVectorInManifest enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmafIntervalCadence:
    """CmafIntervalCadence enum values."""

    FOLLOW_IFRAME = "FOLLOW_IFRAME"
    FOLLOW_CUSTOM = "FOLLOW_CUSTOM"


class CmafKeyProviderType:
    """CmafKeyProviderType enum values."""

    SPEKE = "SPEKE"
    STATIC_KEY = "STATIC_KEY"


class CmafManifestCompression:
    """CmafManifestCompression enum values."""

    GZIP = "GZIP"
    NONE = "NONE"


class CmafManifestDurationFormat:
    """CmafManifestDurationFormat enum values."""

    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class CmafMpdManifestBandwidthType:
    """CmafMpdManifestBandwidthType enum values."""

    AVERAGE = "AVERAGE"
    MAX = "MAX"


class CmafMpdProfile:
    """CmafMpdProfile enum values."""

    MAIN_PROFILE = "MAIN_PROFILE"
    ON_DEMAND_PROFILE = "ON_DEMAND_PROFILE"


class CmafPtsOffsetHandlingForBFrames:
    """CmafPtsOffsetHandlingForBFrames enum values."""

    ZERO_BASED = "ZERO_BASED"
    MATCH_INITIAL_PTS = "MATCH_INITIAL_PTS"


class CmafSegmentControl:
    """CmafSegmentControl enum values."""

    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class CmafSegmentLengthControl:
    """CmafSegmentLengthControl enum values."""

    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"
    MATCH = "MATCH"


class CmafStreamInfResolution:
    """CmafStreamInfResolution enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmafTargetDurationCompatibilityMode:
    """CmafTargetDurationCompatibilityMode enum values."""

    LEGACY = "LEGACY"
    SPEC_COMPLIANT = "SPEC_COMPLIANT"


class CmafVideoCompositionOffsets:
    """CmafVideoCompositionOffsets enum values."""

    SIGNED = "SIGNED"
    UNSIGNED = "UNSIGNED"


class CmafWriteDASHManifest:
    """CmafWriteDASHManifest enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafWriteHLSManifest:
    """CmafWriteHLSManifest enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafWriteSegmentTimelineInRepresentation:
    """CmafWriteSegmentTimelineInRepresentation enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CmfcAudioDuration:
    """CmfcAudioDuration enum values."""

    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class CmfcAudioTrackType:
    """CmfcAudioTrackType enum values."""

    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


class CmfcC2paManifest:
    """CmfcC2paManifest enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmfcDescriptiveVideoServiceFlag:
    """CmfcDescriptiveVideoServiceFlag enum values."""

    DONT_FLAG = "DONT_FLAG"
    FLAG = "FLAG"


class CmfcIFrameOnlyManifest:
    """CmfcIFrameOnlyManifest enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmfcKlvMetadata:
    """CmfcKlvMetadata enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class CmfcManifestMetadataSignaling:
    """CmfcManifestMetadataSignaling enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CmfcScte35Esam:
    """CmfcScte35Esam enum values."""

    INSERT = "INSERT"
    NONE = "NONE"


class CmfcScte35Source:
    """CmfcScte35Source enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class CmfcTimedMetadata:
    """CmfcTimedMetadata enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class CmfcTimedMetadataBoxVersion:
    """CmfcTimedMetadataBoxVersion enum values."""

    VERSION_0 = "VERSION_0"
    VERSION_1 = "VERSION_1"


class Codec:
    """Codec enum values."""

    UNKNOWN = "UNKNOWN"
    AAC = "AAC"
    AC3 = "AC3"
    EAC3 = "EAC3"
    FLAC = "FLAC"
    MP3 = "MP3"
    OPUS = "OPUS"
    PCM = "PCM"
    VORBIS = "VORBIS"
    AV1 = "AV1"
    AVC = "AVC"
    HEVC = "HEVC"
    JPEG2000 = "JPEG2000"
    MJPEG = "MJPEG"
    MPEG1 = "MPEG1"
    MP4V = "MP4V"
    MPEG2 = "MPEG2"
    PRORES = "PRORES"
    THEORA = "THEORA"
    VFW = "VFW"
    VP8 = "VP8"
    VP9 = "VP9"
    QTRLE = "QTRLE"
    C608 = "C608"
    C708 = "C708"
    WEBVTT = "WEBVTT"


class ColorMetadata:
    """ColorMetadata enum values."""

    IGNORE = "IGNORE"
    INSERT = "INSERT"


class ColorPrimaries:
    """ColorPrimaries enum values."""

    ITU_709 = "ITU_709"
    UNSPECIFIED = "UNSPECIFIED"
    RESERVED = "RESERVED"
    ITU_470M = "ITU_470M"
    ITU_470BG = "ITU_470BG"
    SMPTE_170M = "SMPTE_170M"
    SMPTE_240M = "SMPTE_240M"
    GENERIC_FILM = "GENERIC_FILM"
    ITU_2020 = "ITU_2020"
    SMPTE_428_1 = "SMPTE_428_1"
    SMPTE_431_2 = "SMPTE_431_2"
    SMPTE_EG_432_1 = "SMPTE_EG_432_1"
    IPT = "IPT"
    SMPTE_2067XYZ = "SMPTE_2067XYZ"
    EBU_3213_E = "EBU_3213_E"
    LAST = "LAST"


class ColorSpace:
    """ColorSpace enum values."""

    FOLLOW = "FOLLOW"
    REC_601 = "REC_601"
    REC_709 = "REC_709"
    HDR10 = "HDR10"
    HLG_2020 = "HLG_2020"
    P3DCI = "P3DCI"
    P3D65_SDR = "P3D65_SDR"
    P3D65_HDR = "P3D65_HDR"


class ColorSpaceConversion:
    """ColorSpaceConversion enum values."""

    NONE = "NONE"
    FORCE_601 = "FORCE_601"
    FORCE_709 = "FORCE_709"
    FORCE_HDR10 = "FORCE_HDR10"
    FORCE_HLG_2020 = "FORCE_HLG_2020"
    FORCE_P3DCI = "FORCE_P3DCI"
    FORCE_P3D65_SDR = "FORCE_P3D65_SDR"
    FORCE_P3D65_HDR = "FORCE_P3D65_HDR"


class ColorSpaceUsage:
    """ColorSpaceUsage enum values."""

    FORCE = "FORCE"
    FALLBACK = "FALLBACK"


class Commitment:
    """Commitment enum values."""

    ONE_YEAR = "ONE_YEAR"


class ContainerType:
    """ContainerType enum values."""

    F4V = "F4V"
    GIF = "GIF"
    ISMV = "ISMV"
    M2TS = "M2TS"
    M3U8 = "M3U8"
    CMFC = "CMFC"
    MOV = "MOV"
    MP4 = "MP4"
    MPD = "MPD"
    MXF = "MXF"
    OGG = "OGG"
    WEBM = "WEBM"
    RAW = "RAW"
    Y4M = "Y4M"


class CopyProtectionAction:
    """CopyProtectionAction enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    STRIP = "STRIP"


class DashIsoGroupAudioChannelConfigSchemeIdUri:
    """DashIsoGroupAudioChannelConfigSchemeIdUri enum values."""

    MPEG_CHANNEL_CONFIGURATION = "MPEG_CHANNEL_CONFIGURATION"
    DOLBY_CHANNEL_CONFIGURATION = "DOLBY_CHANNEL_CONFIGURATION"


class DashIsoHbbtvCompliance:
    """DashIsoHbbtvCompliance enum values."""

    HBBTV_1_5 = "HBBTV_1_5"
    NONE = "NONE"


class DashIsoImageBasedTrickPlay:
    """DashIsoImageBasedTrickPlay enum values."""

    NONE = "NONE"
    THUMBNAIL = "THUMBNAIL"
    THUMBNAIL_AND_FULLFRAME = "THUMBNAIL_AND_FULLFRAME"
    ADVANCED = "ADVANCED"


class DashIsoIntervalCadence:
    """DashIsoIntervalCadence enum values."""

    FOLLOW_IFRAME = "FOLLOW_IFRAME"
    FOLLOW_CUSTOM = "FOLLOW_CUSTOM"


class DashIsoMpdManifestBandwidthType:
    """DashIsoMpdManifestBandwidthType enum values."""

    AVERAGE = "AVERAGE"
    MAX = "MAX"


class DashIsoMpdProfile:
    """DashIsoMpdProfile enum values."""

    MAIN_PROFILE = "MAIN_PROFILE"
    ON_DEMAND_PROFILE = "ON_DEMAND_PROFILE"


class DashIsoPlaybackDeviceCompatibility:
    """DashIsoPlaybackDeviceCompatibility enum values."""

    CENC_V1 = "CENC_V1"
    UNENCRYPTED_SEI = "UNENCRYPTED_SEI"


class DashIsoPtsOffsetHandlingForBFrames:
    """DashIsoPtsOffsetHandlingForBFrames enum values."""

    ZERO_BASED = "ZERO_BASED"
    MATCH_INITIAL_PTS = "MATCH_INITIAL_PTS"


class DashIsoSegmentControl:
    """DashIsoSegmentControl enum values."""

    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class DashIsoSegmentLengthControl:
    """DashIsoSegmentLengthControl enum values."""

    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"
    MATCH = "MATCH"


class DashIsoVideoCompositionOffsets:
    """DashIsoVideoCompositionOffsets enum values."""

    SIGNED = "SIGNED"
    UNSIGNED = "UNSIGNED"


class DashIsoWriteSegmentTimelineInRepresentation:
    """DashIsoWriteSegmentTimelineInRepresentation enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DashManifestStyle:
    """DashManifestStyle enum values."""

    BASIC = "BASIC"
    COMPACT = "COMPACT"
    DISTINCT = "DISTINCT"
    FULL = "FULL"


class DecryptionMode:
    """DecryptionMode enum values."""

    AES_CTR = "AES_CTR"
    AES_CBC = "AES_CBC"
    AES_GCM = "AES_GCM"


class DeinterlaceAlgorithm:
    """DeinterlaceAlgorithm enum values."""

    INTERPOLATE = "INTERPOLATE"
    INTERPOLATE_TICKER = "INTERPOLATE_TICKER"
    BLEND = "BLEND"
    BLEND_TICKER = "BLEND_TICKER"
    LINEAR_INTERPOLATION = "LINEAR_INTERPOLATION"


class DeinterlacerControl:
    """DeinterlacerControl enum values."""

    FORCE_ALL_FRAMES = "FORCE_ALL_FRAMES"
    NORMAL = "NORMAL"


class DeinterlacerMode:
    """DeinterlacerMode enum values."""

    DEINTERLACE = "DEINTERLACE"
    INVERSE_TELECINE = "INVERSE_TELECINE"
    ADAPTIVE = "ADAPTIVE"


class DescribeEndpointsMode:
    """DescribeEndpointsMode enum values."""

    DEFAULT = "DEFAULT"
    GET_ONLY = "GET_ONLY"


class DolbyVisionLevel6Mode:
    """DolbyVisionLevel6Mode enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    RECALCULATE = "RECALCULATE"
    SPECIFY = "SPECIFY"


class DolbyVisionMapping:
    """DolbyVisionMapping enum values."""

    HDR10_NOMAP = "HDR10_NOMAP"
    HDR10_1000 = "HDR10_1000"


class DolbyVisionProfile:
    """DolbyVisionProfile enum values."""

    PROFILE_5 = "PROFILE_5"
    PROFILE_8_1 = "PROFILE_8_1"


class DropFrameTimecode:
    """DropFrameTimecode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class DvbSubSubtitleFallbackFont:
    """DvbSubSubtitleFallbackFont enum values."""

    BEST_MATCH = "BEST_MATCH"
    MONOSPACED_SANSSERIF = "MONOSPACED_SANSSERIF"
    MONOSPACED_SERIF = "MONOSPACED_SERIF"
    PROPORTIONAL_SANSSERIF = "PROPORTIONAL_SANSSERIF"
    PROPORTIONAL_SERIF = "PROPORTIONAL_SERIF"


class DvbSubtitleAlignment:
    """DvbSubtitleAlignment enum values."""

    CENTERED = "CENTERED"
    LEFT = "LEFT"
    AUTO = "AUTO"


class DvbSubtitleApplyFontColor:
    """DvbSubtitleApplyFontColor enum values."""

    WHITE_TEXT_ONLY = "WHITE_TEXT_ONLY"
    ALL_TEXT = "ALL_TEXT"


class DvbSubtitleBackgroundColor:
    """DvbSubtitleBackgroundColor enum values."""

    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class DvbSubtitleFontColor:
    """DvbSubtitleFontColor enum values."""

    WHITE = "WHITE"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    HEX = "HEX"
    AUTO = "AUTO"


class DvbSubtitleOutlineColor:
    """DvbSubtitleOutlineColor enum values."""

    BLACK = "BLACK"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    AUTO = "AUTO"


class DvbSubtitleShadowColor:
    """DvbSubtitleShadowColor enum values."""

    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    AUTO = "AUTO"


class DvbSubtitleStylePassthrough:
    """DvbSubtitleStylePassthrough enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DvbSubtitleTeletextSpacing:
    """DvbSubtitleTeletextSpacing enum values."""

    FIXED_GRID = "FIXED_GRID"
    PROPORTIONAL = "PROPORTIONAL"
    AUTO = "AUTO"


class DvbSubtitlingType:
    """DvbSubtitlingType enum values."""

    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    STANDARD = "STANDARD"


class DvbddsHandling:
    """DvbddsHandling enum values."""

    NONE = "NONE"
    SPECIFIED = "SPECIFIED"
    NO_DISPLAY_WINDOW = "NO_DISPLAY_WINDOW"
    SPECIFIED_OPTIMAL = "SPECIFIED_OPTIMAL"


class DynamicAudioSelectorType:
    """DynamicAudioSelectorType enum values."""

    ALL_TRACKS = "ALL_TRACKS"
    LANGUAGE_CODE = "LANGUAGE_CODE"


class Eac3AtmosBitstreamMode:
    """Eac3AtmosBitstreamMode enum values."""

    COMPLETE_MAIN = "COMPLETE_MAIN"


class Eac3AtmosCodingMode:
    """Eac3AtmosCodingMode enum values."""

    CODING_MODE_AUTO = "CODING_MODE_AUTO"
    CODING_MODE_5_1_4 = "CODING_MODE_5_1_4"
    CODING_MODE_7_1_4 = "CODING_MODE_7_1_4"
    CODING_MODE_9_1_6 = "CODING_MODE_9_1_6"


class Eac3AtmosDialogueIntelligence:
    """Eac3AtmosDialogueIntelligence enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3AtmosDownmixControl:
    """Eac3AtmosDownmixControl enum values."""

    SPECIFIED = "SPECIFIED"
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"


class Eac3AtmosDynamicRangeCompressionLine:
    """Eac3AtmosDynamicRangeCompressionLine enum values."""

    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3AtmosDynamicRangeCompressionRf:
    """Eac3AtmosDynamicRangeCompressionRf enum values."""

    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3AtmosDynamicRangeControl:
    """Eac3AtmosDynamicRangeControl enum values."""

    SPECIFIED = "SPECIFIED"
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"


class Eac3AtmosMeteringMode:
    """Eac3AtmosMeteringMode enum values."""

    LEQ_A = "LEQ_A"
    ITU_BS_1770_1 = "ITU_BS_1770_1"
    ITU_BS_1770_2 = "ITU_BS_1770_2"
    ITU_BS_1770_3 = "ITU_BS_1770_3"
    ITU_BS_1770_4 = "ITU_BS_1770_4"


class Eac3AtmosStereoDownmix:
    """Eac3AtmosStereoDownmix enum values."""

    NOT_INDICATED = "NOT_INDICATED"
    STEREO = "STEREO"
    SURROUND = "SURROUND"
    DPL2 = "DPL2"


class Eac3AtmosSurroundExMode:
    """Eac3AtmosSurroundExMode enum values."""

    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3AttenuationControl:
    """Eac3AttenuationControl enum values."""

    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Eac3BitstreamMode:
    """Eac3BitstreamMode enum values."""

    COMPLETE_MAIN = "COMPLETE_MAIN"
    COMMENTARY = "COMMENTARY"
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

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3DynamicRangeCompressionLine:
    """Eac3DynamicRangeCompressionLine enum values."""

    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3DynamicRangeCompressionRf:
    """Eac3DynamicRangeCompressionRf enum values."""

    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3LfeControl:
    """Eac3LfeControl enum values."""

    LFE = "LFE"
    NO_LFE = "NO_LFE"


class Eac3LfeFilter:
    """Eac3LfeFilter enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3MetadataControl:
    """Eac3MetadataControl enum values."""

    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Eac3PassthroughControl:
    """Eac3PassthroughControl enum values."""

    WHEN_POSSIBLE = "WHEN_POSSIBLE"
    NO_PASSTHROUGH = "NO_PASSTHROUGH"


class Eac3PhaseControl:
    """Eac3PhaseControl enum values."""

    SHIFT_90_DEGREES = "SHIFT_90_DEGREES"
    NO_SHIFT = "NO_SHIFT"


class Eac3StereoDownmix:
    """Eac3StereoDownmix enum values."""

    NOT_INDICATED = "NOT_INDICATED"
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    DPL2 = "DPL2"


class Eac3SurroundExMode:
    """Eac3SurroundExMode enum values."""

    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3SurroundMode:
    """Eac3SurroundMode enum values."""

    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EmbeddedConvert608To708:
    """EmbeddedConvert608To708 enum values."""

    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class EmbeddedTerminateCaptions:
    """EmbeddedTerminateCaptions enum values."""

    END_OF_INPUT = "END_OF_INPUT"
    DISABLED = "DISABLED"


class EmbeddedTimecodeOverride:
    """EmbeddedTimecodeOverride enum values."""

    NONE = "NONE"
    USE_MDPM = "USE_MDPM"


class F4vMoovPlacement:
    """F4vMoovPlacement enum values."""

    PROGRESSIVE_DOWNLOAD = "PROGRESSIVE_DOWNLOAD"
    NORMAL = "NORMAL"


class FileSourceConvert608To708:
    """FileSourceConvert608To708 enum values."""

    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


class FileSourceTimeDeltaUnits:
    """FileSourceTimeDeltaUnits enum values."""

    SECONDS = "SECONDS"
    MILLISECONDS = "MILLISECONDS"


class FontScript:
    """FontScript enum values."""

    AUTOMATIC = "AUTOMATIC"
    HANS = "HANS"
    HANT = "HANT"


class Format:
    """Format enum values."""

    MP4 = "mp4"
    QUICKTIME = "quicktime"
    MATROSKA = "matroska"
    WEBM = "webm"
    MXF = "mxf"


class FrameControl:
    """FrameControl enum values."""

    NEAREST_IDRFRAME = "NEAREST_IDRFRAME"
    NEAREST_IFRAME = "NEAREST_IFRAME"


class FrameMetricType:
    """FrameMetricType enum values."""

    PSNR = "PSNR"
    SSIM = "SSIM"
    MS_SSIM = "MS_SSIM"
    PSNR_HVS = "PSNR_HVS"
    VMAF = "VMAF"
    QVBR = "QVBR"
    SHOT_CHANGE = "SHOT_CHANGE"


class GifFramerateControl:
    """GifFramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class GifFramerateConversionAlgorithm:
    """GifFramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"


class H264AdaptiveQuantization:
    """H264AdaptiveQuantization enum values."""

    OFF = "OFF"
    AUTO = "AUTO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class H264CodecLevel:
    """H264CodecLevel enum values."""

    AUTO = "AUTO"
    LEVEL_1 = "LEVEL_1"
    LEVEL_1_1 = "LEVEL_1_1"
    LEVEL_1_2 = "LEVEL_1_2"
    LEVEL_1_3 = "LEVEL_1_3"
    LEVEL_2 = "LEVEL_2"
    LEVEL_2_1 = "LEVEL_2_1"
    LEVEL_2_2 = "LEVEL_2_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_3_1 = "LEVEL_3_1"
    LEVEL_3_2 = "LEVEL_3_2"
    LEVEL_4 = "LEVEL_4"
    LEVEL_4_1 = "LEVEL_4_1"
    LEVEL_4_2 = "LEVEL_4_2"
    LEVEL_5 = "LEVEL_5"
    LEVEL_5_1 = "LEVEL_5_1"
    LEVEL_5_2 = "LEVEL_5_2"


class H264CodecProfile:
    """H264CodecProfile enum values."""

    BASELINE = "BASELINE"
    HIGH = "HIGH"
    HIGH_10BIT = "HIGH_10BIT"
    HIGH_422 = "HIGH_422"
    HIGH_422_10BIT = "HIGH_422_10BIT"
    MAIN = "MAIN"


class H264DynamicSubGop:
    """H264DynamicSubGop enum values."""

    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class H264EndOfStreamMarkers:
    """H264EndOfStreamMarkers enum values."""

    INCLUDE = "INCLUDE"
    SUPPRESS = "SUPPRESS"


class H264EntropyEncoding:
    """H264EntropyEncoding enum values."""

    CABAC = "CABAC"
    CAVLC = "CAVLC"


class H264FieldEncoding:
    """H264FieldEncoding enum values."""

    PAFF = "PAFF"
    FORCE_FIELD = "FORCE_FIELD"
    MBAFF = "MBAFF"


class H264FlickerAdaptiveQuantization:
    """H264FlickerAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264FramerateControl:
    """H264FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264FramerateConversionAlgorithm:
    """H264FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class H264GopBReference:
    """H264GopBReference enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264GopSizeUnits:
    """H264GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"
    AUTO = "AUTO"


class H264InterlaceMode:
    """H264InterlaceMode enum values."""

    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class H264ParControl:
    """H264ParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264QualityTuningLevel:
    """H264QualityTuningLevel enum values."""

    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class H264RateControlMode:
    """H264RateControlMode enum values."""

    VBR = "VBR"
    CBR = "CBR"
    QVBR = "QVBR"


class H264RepeatPps:
    """H264RepeatPps enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SaliencyAwareEncoding:
    """H264SaliencyAwareEncoding enum values."""

    DISABLED = "DISABLED"
    PREFERRED = "PREFERRED"


class H264ScanTypeConversionMode:
    """H264ScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class H264SceneChangeDetect:
    """H264SceneChangeDetect enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    TRANSITION_DETECTION = "TRANSITION_DETECTION"


class H264SlowPal:
    """H264SlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SpatialAdaptiveQuantization:
    """H264SpatialAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264Syntax:
    """H264Syntax enum values."""

    DEFAULT = "DEFAULT"
    RP2027 = "RP2027"


class H264Telecine:
    """H264Telecine enum values."""

    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class H264TemporalAdaptiveQuantization:
    """H264TemporalAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264UnregisteredSeiTimecode:
    """H264UnregisteredSeiTimecode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264WriteMp4PackagingType:
    """H264WriteMp4PackagingType enum values."""

    AVC1 = "AVC1"
    AVC3 = "AVC3"


class H265AdaptiveQuantization:
    """H265AdaptiveQuantization enum values."""

    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"
    AUTO = "AUTO"


class H265AlternateTransferFunctionSei:
    """H265AlternateTransferFunctionSei enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265CodecLevel:
    """H265CodecLevel enum values."""

    AUTO = "AUTO"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_2_1 = "LEVEL_2_1"
    LEVEL_3 = "LEVEL_3"
    LEVEL_3_1 = "LEVEL_3_1"
    LEVEL_4 = "LEVEL_4"
    LEVEL_4_1 = "LEVEL_4_1"
    LEVEL_5 = "LEVEL_5"
    LEVEL_5_1 = "LEVEL_5_1"
    LEVEL_5_2 = "LEVEL_5_2"
    LEVEL_6 = "LEVEL_6"
    LEVEL_6_1 = "LEVEL_6_1"
    LEVEL_6_2 = "LEVEL_6_2"


class H265CodecProfile:
    """H265CodecProfile enum values."""

    MAIN_MAIN = "MAIN_MAIN"
    MAIN_HIGH = "MAIN_HIGH"
    MAIN10_MAIN = "MAIN10_MAIN"
    MAIN10_HIGH = "MAIN10_HIGH"
    MAIN_422_8BIT_MAIN = "MAIN_422_8BIT_MAIN"
    MAIN_422_8BIT_HIGH = "MAIN_422_8BIT_HIGH"
    MAIN_422_10BIT_MAIN = "MAIN_422_10BIT_MAIN"
    MAIN_422_10BIT_HIGH = "MAIN_422_10BIT_HIGH"


class H265Deblocking:
    """H265Deblocking enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class H265DynamicSubGop:
    """H265DynamicSubGop enum values."""

    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class H265EndOfStreamMarkers:
    """H265EndOfStreamMarkers enum values."""

    INCLUDE = "INCLUDE"
    SUPPRESS = "SUPPRESS"


class H265FlickerAdaptiveQuantization:
    """H265FlickerAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265FramerateControl:
    """H265FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H265FramerateConversionAlgorithm:
    """H265FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class H265GopBReference:
    """H265GopBReference enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265GopSizeUnits:
    """H265GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"
    AUTO = "AUTO"


class H265InterlaceMode:
    """H265InterlaceMode enum values."""

    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class H265MvOverPictureBoundaries:
    """H265MvOverPictureBoundaries enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class H265MvTemporalPredictor:
    """H265MvTemporalPredictor enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class H265ParControl:
    """H265ParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H265QualityTuningLevel:
    """H265QualityTuningLevel enum values."""

    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class H265RateControlMode:
    """H265RateControlMode enum values."""

    VBR = "VBR"
    CBR = "CBR"
    QVBR = "QVBR"


class H265SampleAdaptiveOffsetFilterMode:
    """H265SampleAdaptiveOffsetFilterMode enum values."""

    DEFAULT = "DEFAULT"
    ADAPTIVE = "ADAPTIVE"
    OFF = "OFF"


class H265ScanTypeConversionMode:
    """H265ScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class H265SceneChangeDetect:
    """H265SceneChangeDetect enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    TRANSITION_DETECTION = "TRANSITION_DETECTION"


class H265SlowPal:
    """H265SlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265SpatialAdaptiveQuantization:
    """H265SpatialAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265Telecine:
    """H265Telecine enum values."""

    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class H265TemporalAdaptiveQuantization:
    """H265TemporalAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265TemporalIds:
    """H265TemporalIds enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265TilePadding:
    """H265TilePadding enum values."""

    NONE = "NONE"
    PADDED = "PADDED"


class H265Tiles:
    """H265Tiles enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265TreeBlockSize:
    """H265TreeBlockSize enum values."""

    AUTO = "AUTO"
    TREE_SIZE_32X32 = "TREE_SIZE_32X32"


class H265UnregisteredSeiTimecode:
    """H265UnregisteredSeiTimecode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265WriteMp4PackagingType:
    """H265WriteMp4PackagingType enum values."""

    HVC1 = "HVC1"
    HEV1 = "HEV1"


class HDRToSDRToneMapper:
    """HDRToSDRToneMapper enum values."""

    PRESERVE_DETAILS = "PRESERVE_DETAILS"
    VIBRANT = "VIBRANT"


class HlsAdMarkers:
    """HlsAdMarkers enum values."""

    ELEMENTAL = "ELEMENTAL"
    ELEMENTAL_SCTE35 = "ELEMENTAL_SCTE35"


class HlsAudioOnlyContainer:
    """HlsAudioOnlyContainer enum values."""

    AUTOMATIC = "AUTOMATIC"
    M2TS = "M2TS"


class HlsAudioOnlyHeader:
    """HlsAudioOnlyHeader enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsAudioTrackType:
    """HlsAudioTrackType enum values."""

    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


class HlsCaptionLanguageSetting:
    """HlsCaptionLanguageSetting enum values."""

    INSERT = "INSERT"
    OMIT = "OMIT"
    NONE = "NONE"


class HlsCaptionSegmentLengthControl:
    """HlsCaptionSegmentLengthControl enum values."""

    LARGE_SEGMENTS = "LARGE_SEGMENTS"
    MATCH_VIDEO = "MATCH_VIDEO"


class HlsClientCache:
    """HlsClientCache enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsCodecSpecification:
    """HlsCodecSpecification enum values."""

    RFC_6381 = "RFC_6381"
    RFC_4281 = "RFC_4281"


class HlsDescriptiveVideoServiceFlag:
    """HlsDescriptiveVideoServiceFlag enum values."""

    DONT_FLAG = "DONT_FLAG"
    FLAG = "FLAG"


class HlsDirectoryStructure:
    """HlsDirectoryStructure enum values."""

    SINGLE_DIRECTORY = "SINGLE_DIRECTORY"
    SUBDIRECTORY_PER_STREAM = "SUBDIRECTORY_PER_STREAM"


class HlsEncryptionType:
    """HlsEncryptionType enum values."""

    AES128 = "AES128"
    SAMPLE_AES = "SAMPLE_AES"


class HlsIFrameOnlyManifest:
    """HlsIFrameOnlyManifest enum values."""

    INCLUDE = "INCLUDE"
    INCLUDE_AS_TS = "INCLUDE_AS_TS"
    EXCLUDE = "EXCLUDE"


class HlsImageBasedTrickPlay:
    """HlsImageBasedTrickPlay enum values."""

    NONE = "NONE"
    THUMBNAIL = "THUMBNAIL"
    THUMBNAIL_AND_FULLFRAME = "THUMBNAIL_AND_FULLFRAME"
    ADVANCED = "ADVANCED"


class HlsInitializationVectorInManifest:
    """HlsInitializationVectorInManifest enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsIntervalCadence:
    """HlsIntervalCadence enum values."""

    FOLLOW_IFRAME = "FOLLOW_IFRAME"
    FOLLOW_CUSTOM = "FOLLOW_CUSTOM"


class HlsKeyProviderType:
    """HlsKeyProviderType enum values."""

    SPEKE = "SPEKE"
    STATIC_KEY = "STATIC_KEY"


class HlsManifestCompression:
    """HlsManifestCompression enum values."""

    GZIP = "GZIP"
    NONE = "NONE"


class HlsManifestDurationFormat:
    """HlsManifestDurationFormat enum values."""

    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class HlsOfflineEncrypted:
    """HlsOfflineEncrypted enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class HlsOutputSelection:
    """HlsOutputSelection enum values."""

    MANIFESTS_AND_SEGMENTS = "MANIFESTS_AND_SEGMENTS"
    SEGMENTS_ONLY = "SEGMENTS_ONLY"


class HlsProgramDateTime:
    """HlsProgramDateTime enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsProgressiveWriteHlsManifest:
    """HlsProgressiveWriteHlsManifest enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class HlsSegmentControl:
    """HlsSegmentControl enum values."""

    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class HlsSegmentLengthControl:
    """HlsSegmentLengthControl enum values."""

    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"
    MATCH = "MATCH"


class HlsStreamInfResolution:
    """HlsStreamInfResolution enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsTargetDurationCompatibilityMode:
    """HlsTargetDurationCompatibilityMode enum values."""

    LEGACY = "LEGACY"
    SPEC_COMPLIANT = "SPEC_COMPLIANT"


class HlsTimedMetadataId3Frame:
    """HlsTimedMetadataId3Frame enum values."""

    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class ImscAccessibilitySubs:
    """ImscAccessibilitySubs enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ImscStylePassthrough:
    """ImscStylePassthrough enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputDeblockFilter:
    """InputDeblockFilter enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputDenoiseFilter:
    """InputDenoiseFilter enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputFilterEnable:
    """InputFilterEnable enum values."""

    AUTO = "AUTO"
    DISABLE = "DISABLE"
    FORCE = "FORCE"


class InputPolicy:
    """InputPolicy enum values."""

    ALLOWED = "ALLOWED"
    DISALLOWED = "DISALLOWED"


class InputPsiControl:
    """InputPsiControl enum values."""

    IGNORE_PSI = "IGNORE_PSI"
    USE_PSI = "USE_PSI"


class InputRotate:
    """InputRotate enum values."""

    DEGREE_0 = "DEGREE_0"
    DEGREES_90 = "DEGREES_90"
    DEGREES_180 = "DEGREES_180"
    DEGREES_270 = "DEGREES_270"
    AUTO = "AUTO"


class InputSampleRange:
    """InputSampleRange enum values."""

    FOLLOW = "FOLLOW"
    FULL_RANGE = "FULL_RANGE"
    LIMITED_RANGE = "LIMITED_RANGE"


class InputScanType:
    """InputScanType enum values."""

    AUTO = "AUTO"
    PSF = "PSF"


class InputTimecodeSource:
    """InputTimecodeSource enum values."""

    EMBEDDED = "EMBEDDED"
    ZEROBASED = "ZEROBASED"
    SPECIFIEDSTART = "SPECIFIEDSTART"


class JobPhase:
    """JobPhase enum values."""

    PROBING = "PROBING"
    TRANSCODING = "TRANSCODING"
    UPLOADING = "UPLOADING"


class JobStatus:
    """JobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PROGRESSING = "PROGRESSING"
    COMPLETE = "COMPLETE"
    CANCELED = "CANCELED"
    ERROR = "ERROR"


class JobTemplateListBy:
    """JobTemplateListBy enum values."""

    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    SYSTEM = "SYSTEM"


class JobsQueryFilterKey:
    """JobsQueryFilterKey enum values."""

    QUEUE = "queue"
    STATUS = "status"
    FILEINPUT = "fileInput"
    JOBENGINEVERSIONREQUESTED = "jobEngineVersionRequested"
    JOBENGINEVERSIONUSED = "jobEngineVersionUsed"
    AUDIOCODEC = "audioCodec"
    VIDEOCODEC = "videoCodec"


class JobsQueryStatus:
    """JobsQueryStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PROGRESSING = "PROGRESSING"
    COMPLETE = "COMPLETE"
    ERROR = "ERROR"


class LanguageCode:
    """LanguageCode enum values."""

    ENG = "ENG"
    SPA = "SPA"
    FRA = "FRA"
    DEU = "DEU"
    GER = "GER"
    ZHO = "ZHO"
    ARA = "ARA"
    HIN = "HIN"
    JPN = "JPN"
    RUS = "RUS"
    POR = "POR"
    ITA = "ITA"
    URD = "URD"
    VIE = "VIE"
    KOR = "KOR"
    PAN = "PAN"
    ABK = "ABK"
    AAR = "AAR"
    AFR = "AFR"
    AKA = "AKA"
    SQI = "SQI"
    AMH = "AMH"
    ARG = "ARG"
    HYE = "HYE"
    ASM = "ASM"
    AVA = "AVA"
    AVE = "AVE"
    AYM = "AYM"
    AZE = "AZE"
    BAM = "BAM"
    BAK = "BAK"
    EUS = "EUS"
    BEL = "BEL"
    BEN = "BEN"
    BIH = "BIH"
    BIS = "BIS"
    BOS = "BOS"
    BRE = "BRE"
    BUL = "BUL"
    MYA = "MYA"
    CAT = "CAT"
    KHM = "KHM"
    CHA = "CHA"
    CHE = "CHE"
    NYA = "NYA"
    CHU = "CHU"
    CHV = "CHV"
    COR = "COR"
    COS = "COS"
    CRE = "CRE"
    HRV = "HRV"
    CES = "CES"
    DAN = "DAN"
    DIV = "DIV"
    NLD = "NLD"
    DZO = "DZO"
    ENM = "ENM"
    EPO = "EPO"
    EST = "EST"
    EWE = "EWE"
    FAO = "FAO"
    FIJ = "FIJ"
    FIN = "FIN"
    FRM = "FRM"
    FUL = "FUL"
    GLA = "GLA"
    GLG = "GLG"
    LUG = "LUG"
    KAT = "KAT"
    ELL = "ELL"
    GRN = "GRN"
    GUJ = "GUJ"
    HAT = "HAT"
    HAU = "HAU"
    HEB = "HEB"
    HER = "HER"
    HMO = "HMO"
    HUN = "HUN"
    ISL = "ISL"
    IDO = "IDO"
    IBO = "IBO"
    IND = "IND"
    INA = "INA"
    ILE = "ILE"
    IKU = "IKU"
    IPK = "IPK"
    GLE = "GLE"
    JAV = "JAV"
    KAL = "KAL"
    KAN = "KAN"
    KAU = "KAU"
    KAS = "KAS"
    KAZ = "KAZ"
    KIK = "KIK"
    KIN = "KIN"
    KIR = "KIR"
    KOM = "KOM"
    KON = "KON"
    KUA = "KUA"
    KUR = "KUR"
    LAO = "LAO"
    LAT = "LAT"
    LAV = "LAV"
    LIM = "LIM"
    LIN = "LIN"
    LIT = "LIT"
    LUB = "LUB"
    LTZ = "LTZ"
    MKD = "MKD"
    MLG = "MLG"
    MSA = "MSA"
    MAL = "MAL"
    MLT = "MLT"
    GLV = "GLV"
    MRI = "MRI"
    MAR = "MAR"
    MAH = "MAH"
    MON = "MON"
    NAU = "NAU"
    NAV = "NAV"
    NDE = "NDE"
    NBL = "NBL"
    NDO = "NDO"
    NEP = "NEP"
    SME = "SME"
    NOR = "NOR"
    NOB = "NOB"
    NNO = "NNO"
    OCI = "OCI"
    OJI = "OJI"
    ORI = "ORI"
    ORM = "ORM"
    OSS = "OSS"
    PLI = "PLI"
    FAS = "FAS"
    POL = "POL"
    PUS = "PUS"
    QUE = "QUE"
    QAA = "QAA"
    RON = "RON"
    ROH = "ROH"
    RUN = "RUN"
    SMO = "SMO"
    SAG = "SAG"
    SAN = "SAN"
    SRD = "SRD"
    SRB = "SRB"
    SNA = "SNA"
    III = "III"
    SND = "SND"
    SIN = "SIN"
    SLK = "SLK"
    SLV = "SLV"
    SOM = "SOM"
    SOT = "SOT"
    SUN = "SUN"
    SWA = "SWA"
    SSW = "SSW"
    SWE = "SWE"
    TGL = "TGL"
    TAH = "TAH"
    TGK = "TGK"
    TAM = "TAM"
    TAT = "TAT"
    TEL = "TEL"
    THA = "THA"
    BOD = "BOD"
    TIR = "TIR"
    TON = "TON"
    TSO = "TSO"
    TSN = "TSN"
    TUR = "TUR"
    TUK = "TUK"
    TWI = "TWI"
    UIG = "UIG"
    UKR = "UKR"
    UZB = "UZB"
    VEN = "VEN"
    VOL = "VOL"
    WLN = "WLN"
    CYM = "CYM"
    FRY = "FRY"
    WOL = "WOL"
    XHO = "XHO"
    YID = "YID"
    YOR = "YOR"
    ZHA = "ZHA"
    ZUL = "ZUL"
    ORJ = "ORJ"
    QPC = "QPC"
    TNG = "TNG"
    SRP = "SRP"


class M2tsAudioBufferModel:
    """M2tsAudioBufferModel enum values."""

    DVB = "DVB"
    ATSC = "ATSC"


class M2tsAudioDuration:
    """M2tsAudioDuration enum values."""

    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class M2tsBufferModel:
    """M2tsBufferModel enum values."""

    MULTIPLEX = "MULTIPLEX"
    NONE = "NONE"


class M2tsDataPtsControl:
    """M2tsDataPtsControl enum values."""

    AUTO = "AUTO"
    ALIGN_TO_VIDEO = "ALIGN_TO_VIDEO"


class M2tsEbpAudioInterval:
    """M2tsEbpAudioInterval enum values."""

    VIDEO_AND_FIXED_INTERVALS = "VIDEO_AND_FIXED_INTERVALS"
    VIDEO_INTERVAL = "VIDEO_INTERVAL"


class M2tsEbpPlacement:
    """M2tsEbpPlacement enum values."""

    VIDEO_AND_AUDIO_PIDS = "VIDEO_AND_AUDIO_PIDS"
    VIDEO_PID = "VIDEO_PID"


class M2tsEsRateInPes:
    """M2tsEsRateInPes enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class M2tsForceTsVideoEbpOrder:
    """M2tsForceTsVideoEbpOrder enum values."""

    FORCE = "FORCE"
    DEFAULT = "DEFAULT"


class M2tsKlvMetadata:
    """M2tsKlvMetadata enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class M2tsNielsenId3:
    """M2tsNielsenId3 enum values."""

    INSERT = "INSERT"
    NONE = "NONE"


class M2tsPcrControl:
    """M2tsPcrControl enum values."""

    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"


class M2tsPreventBufferUnderflow:
    """M2tsPreventBufferUnderflow enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsRateMode:
    """M2tsRateMode enum values."""

    VBR = "VBR"
    CBR = "CBR"


class M2tsScte35Source:
    """M2tsScte35Source enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class M2tsSegmentationMarkers:
    """M2tsSegmentationMarkers enum values."""

    NONE = "NONE"
    RAI_SEGSTART = "RAI_SEGSTART"
    RAI_ADAPT = "RAI_ADAPT"
    PSI_SEGSTART = "PSI_SEGSTART"
    EBP = "EBP"
    EBP_LEGACY = "EBP_LEGACY"


class M2tsSegmentationStyle:
    """M2tsSegmentationStyle enum values."""

    MAINTAIN_CADENCE = "MAINTAIN_CADENCE"
    RESET_CADENCE = "RESET_CADENCE"


class M3u8AudioDuration:
    """M3u8AudioDuration enum values."""

    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class M3u8DataPtsControl:
    """M3u8DataPtsControl enum values."""

    AUTO = "AUTO"
    ALIGN_TO_VIDEO = "ALIGN_TO_VIDEO"


class M3u8NielsenId3:
    """M3u8NielsenId3 enum values."""

    INSERT = "INSERT"
    NONE = "NONE"


class M3u8PcrControl:
    """M3u8PcrControl enum values."""

    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"


class M3u8Scte35Source:
    """M3u8Scte35Source enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class MatrixCoefficients:
    """MatrixCoefficients enum values."""

    RGB = "RGB"
    ITU_709 = "ITU_709"
    UNSPECIFIED = "UNSPECIFIED"
    RESERVED = "RESERVED"
    FCC = "FCC"
    ITU_470BG = "ITU_470BG"
    SMPTE_170M = "SMPTE_170M"
    SMPTE_240M = "SMPTE_240M"
    YCGCO = "YCgCo"
    ITU_2020_NCL = "ITU_2020_NCL"
    ITU_2020_CL = "ITU_2020_CL"
    SMPTE_2085 = "SMPTE_2085"
    CD_NCL = "CD_NCL"
    CD_CL = "CD_CL"
    ITU_2100ICTCP = "ITU_2100ICtCp"
    IPT = "IPT"
    EBU3213 = "EBU3213"
    LAST = "LAST"


class MotionImageInsertionMode:
    """MotionImageInsertionMode enum values."""

    MOV = "MOV"
    PNG = "PNG"


class MotionImagePlayback:
    """MotionImagePlayback enum values."""

    ONCE = "ONCE"
    REPEAT = "REPEAT"


class MovClapAtom:
    """MovClapAtom enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MovCslgAtom:
    """MovCslgAtom enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MovMpeg2FourCCControl:
    """MovMpeg2FourCCControl enum values."""

    XDCAM = "XDCAM"
    MPEG = "MPEG"


class MovPaddingControl:
    """MovPaddingControl enum values."""

    OMNEON = "OMNEON"
    NONE = "NONE"


class MovReference:
    """MovReference enum values."""

    SELF_CONTAINED = "SELF_CONTAINED"
    EXTERNAL = "EXTERNAL"


class Mp2AudioDescriptionMix:
    """Mp2AudioDescriptionMix enum values."""

    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NONE = "NONE"


class Mp3RateControlMode:
    """Mp3RateControlMode enum values."""

    CBR = "CBR"
    VBR = "VBR"


class Mp4C2paManifest:
    """Mp4C2paManifest enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4CslgAtom:
    """Mp4CslgAtom enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4FreeSpaceBox:
    """Mp4FreeSpaceBox enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4MoovPlacement:
    """Mp4MoovPlacement enum values."""

    PROGRESSIVE_DOWNLOAD = "PROGRESSIVE_DOWNLOAD"
    NORMAL = "NORMAL"


class MpdAccessibilityCaptionHints:
    """MpdAccessibilityCaptionHints enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MpdAudioDuration:
    """MpdAudioDuration enum values."""

    DEFAULT_CODEC_DURATION = "DEFAULT_CODEC_DURATION"
    MATCH_VIDEO_DURATION = "MATCH_VIDEO_DURATION"


class MpdC2paManifest:
    """MpdC2paManifest enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MpdCaptionContainerType:
    """MpdCaptionContainerType enum values."""

    RAW = "RAW"
    FRAGMENTED_MP4 = "FRAGMENTED_MP4"


class MpdKlvMetadata:
    """MpdKlvMetadata enum values."""

    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class MpdManifestMetadataSignaling:
    """MpdManifestMetadataSignaling enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MpdScte35Esam:
    """MpdScte35Esam enum values."""

    INSERT = "INSERT"
    NONE = "NONE"


class MpdScte35Source:
    """MpdScte35Source enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class MpdTimedMetadata:
    """MpdTimedMetadata enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class MpdTimedMetadataBoxVersion:
    """MpdTimedMetadataBoxVersion enum values."""

    VERSION_0 = "VERSION_0"
    VERSION_1 = "VERSION_1"


class Mpeg2AdaptiveQuantization:
    """Mpeg2AdaptiveQuantization enum values."""

    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Mpeg2CodecLevel:
    """Mpeg2CodecLevel enum values."""

    AUTO = "AUTO"
    LOW = "LOW"
    MAIN = "MAIN"
    HIGH1440 = "HIGH1440"
    HIGH = "HIGH"


class Mpeg2CodecProfile:
    """Mpeg2CodecProfile enum values."""

    MAIN = "MAIN"
    PROFILE_422 = "PROFILE_422"


class Mpeg2DynamicSubGop:
    """Mpeg2DynamicSubGop enum values."""

    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class Mpeg2FramerateControl:
    """Mpeg2FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Mpeg2FramerateConversionAlgorithm:
    """Mpeg2FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Mpeg2GopSizeUnits:
    """Mpeg2GopSizeUnits enum values."""

    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class Mpeg2InterlaceMode:
    """Mpeg2InterlaceMode enum values."""

    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class Mpeg2IntraDcPrecision:
    """Mpeg2IntraDcPrecision enum values."""

    AUTO = "AUTO"
    INTRA_DC_PRECISION_8 = "INTRA_DC_PRECISION_8"
    INTRA_DC_PRECISION_9 = "INTRA_DC_PRECISION_9"
    INTRA_DC_PRECISION_10 = "INTRA_DC_PRECISION_10"
    INTRA_DC_PRECISION_11 = "INTRA_DC_PRECISION_11"


class Mpeg2ParControl:
    """Mpeg2ParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Mpeg2QualityTuningLevel:
    """Mpeg2QualityTuningLevel enum values."""

    SINGLE_PASS = "SINGLE_PASS"
    MULTI_PASS = "MULTI_PASS"


class Mpeg2RateControlMode:
    """Mpeg2RateControlMode enum values."""

    VBR = "VBR"
    CBR = "CBR"


class Mpeg2ScanTypeConversionMode:
    """Mpeg2ScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class Mpeg2SceneChangeDetect:
    """Mpeg2SceneChangeDetect enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2SlowPal:
    """Mpeg2SlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2SpatialAdaptiveQuantization:
    """Mpeg2SpatialAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2Syntax:
    """Mpeg2Syntax enum values."""

    DEFAULT = "DEFAULT"
    D_10 = "D_10"


class Mpeg2Telecine:
    """Mpeg2Telecine enum values."""

    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class Mpeg2TemporalAdaptiveQuantization:
    """Mpeg2TemporalAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class MsSmoothAudioDeduplication:
    """MsSmoothAudioDeduplication enum values."""

    COMBINE_DUPLICATE_STREAMS = "COMBINE_DUPLICATE_STREAMS"
    NONE = "NONE"


class MsSmoothFragmentLengthControl:
    """MsSmoothFragmentLengthControl enum values."""

    EXACT = "EXACT"
    GOP_MULTIPLE = "GOP_MULTIPLE"


class MsSmoothManifestEncoding:
    """MsSmoothManifestEncoding enum values."""

    UTF8 = "UTF8"
    UTF16 = "UTF16"


class MxfAfdSignaling:
    """MxfAfdSignaling enum values."""

    NO_COPY = "NO_COPY"
    COPY_FROM_VIDEO = "COPY_FROM_VIDEO"


class MxfProfile:
    """MxfProfile enum values."""

    D_10 = "D_10"
    XDCAM = "XDCAM"
    OP1A = "OP1A"
    XAVC = "XAVC"
    XDCAM_RDD9 = "XDCAM_RDD9"


class MxfXavcDurationMode:
    """MxfXavcDurationMode enum values."""

    ALLOW_ANY_DURATION = "ALLOW_ANY_DURATION"
    DROP_FRAMES_FOR_COMPLIANCE = "DROP_FRAMES_FOR_COMPLIANCE"


class NielsenActiveWatermarkProcessType:
    """NielsenActiveWatermarkProcessType enum values."""

    NAES2_AND_NW = "NAES2_AND_NW"
    CBET = "CBET"
    NAES2_AND_NW_AND_CBET = "NAES2_AND_NW_AND_CBET"


class NielsenSourceWatermarkStatusType:
    """NielsenSourceWatermarkStatusType enum values."""

    CLEAN = "CLEAN"
    WATERMARKED = "WATERMARKED"


class NielsenUniqueTicPerAudioTrackType:
    """NielsenUniqueTicPerAudioTrackType enum values."""

    RESERVE_UNIQUE_TICS_PER_TRACK = "RESERVE_UNIQUE_TICS_PER_TRACK"
    SAME_TICS_PER_TRACK = "SAME_TICS_PER_TRACK"


class NoiseFilterPostTemporalSharpening:
    """NoiseFilterPostTemporalSharpening enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    AUTO = "AUTO"


class NoiseFilterPostTemporalSharpeningStrength:
    """NoiseFilterPostTemporalSharpeningStrength enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class NoiseReducerFilter:
    """NoiseReducerFilter enum values."""

    BILATERAL = "BILATERAL"
    MEAN = "MEAN"
    GAUSSIAN = "GAUSSIAN"
    LANCZOS = "LANCZOS"
    SHARPEN = "SHARPEN"
    CONSERVE = "CONSERVE"
    SPATIAL = "SPATIAL"
    TEMPORAL = "TEMPORAL"


class Order:
    """Order enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class OutputGroupType:
    """OutputGroupType enum values."""

    HLS_GROUP_SETTINGS = "HLS_GROUP_SETTINGS"
    DASH_ISO_GROUP_SETTINGS = "DASH_ISO_GROUP_SETTINGS"
    FILE_GROUP_SETTINGS = "FILE_GROUP_SETTINGS"
    MS_SMOOTH_GROUP_SETTINGS = "MS_SMOOTH_GROUP_SETTINGS"
    CMAF_GROUP_SETTINGS = "CMAF_GROUP_SETTINGS"


class OutputSdt:
    """OutputSdt enum values."""

    SDT_FOLLOW = "SDT_FOLLOW"
    SDT_FOLLOW_IF_PRESENT = "SDT_FOLLOW_IF_PRESENT"
    SDT_MANUAL = "SDT_MANUAL"
    SDT_NONE = "SDT_NONE"


class PadVideo:
    """PadVideo enum values."""

    DISABLED = "DISABLED"
    BLACK = "BLACK"


class PresetListBy:
    """PresetListBy enum values."""

    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    SYSTEM = "SYSTEM"


class PresetSpeke20Audio:
    """PresetSpeke20Audio enum values."""

    PRESET_AUDIO_1 = "PRESET_AUDIO_1"
    PRESET_AUDIO_2 = "PRESET_AUDIO_2"
    PRESET_AUDIO_3 = "PRESET_AUDIO_3"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class PresetSpeke20Video:
    """PresetSpeke20Video enum values."""

    PRESET_VIDEO_1 = "PRESET_VIDEO_1"
    PRESET_VIDEO_2 = "PRESET_VIDEO_2"
    PRESET_VIDEO_3 = "PRESET_VIDEO_3"
    PRESET_VIDEO_4 = "PRESET_VIDEO_4"
    PRESET_VIDEO_5 = "PRESET_VIDEO_5"
    PRESET_VIDEO_6 = "PRESET_VIDEO_6"
    PRESET_VIDEO_7 = "PRESET_VIDEO_7"
    PRESET_VIDEO_8 = "PRESET_VIDEO_8"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class PricingPlan:
    """PricingPlan enum values."""

    ON_DEMAND = "ON_DEMAND"
    RESERVED = "RESERVED"


class ProresChromaSampling:
    """ProresChromaSampling enum values."""

    PRESERVE_444_SAMPLING = "PRESERVE_444_SAMPLING"
    SUBSAMPLE_TO_422 = "SUBSAMPLE_TO_422"


class ProresCodecProfile:
    """ProresCodecProfile enum values."""

    APPLE_PRORES_422 = "APPLE_PRORES_422"
    APPLE_PRORES_422_HQ = "APPLE_PRORES_422_HQ"
    APPLE_PRORES_422_LT = "APPLE_PRORES_422_LT"
    APPLE_PRORES_422_PROXY = "APPLE_PRORES_422_PROXY"
    APPLE_PRORES_4444 = "APPLE_PRORES_4444"
    APPLE_PRORES_4444_XQ = "APPLE_PRORES_4444_XQ"


class ProresFramerateControl:
    """ProresFramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class ProresFramerateConversionAlgorithm:
    """ProresFramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class ProresInterlaceMode:
    """ProresInterlaceMode enum values."""

    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class ProresParControl:
    """ProresParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class ProresScanTypeConversionMode:
    """ProresScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class ProresSlowPal:
    """ProresSlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ProresTelecine:
    """ProresTelecine enum values."""

    NONE = "NONE"
    HARD = "HARD"


class QueueListBy:
    """QueueListBy enum values."""

    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"


class QueueStatus:
    """QueueStatus enum values."""

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class RemoveRubyReserveAttributes:
    """RemoveRubyReserveAttributes enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class RenewalType:
    """RenewalType enum values."""

    AUTO_RENEW = "AUTO_RENEW"
    EXPIRE = "EXPIRE"


class RequiredFlag:
    """RequiredFlag enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ReservationPlanStatus:
    """ReservationPlanStatus enum values."""

    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"


class RespondToAfd:
    """RespondToAfd enum values."""

    NONE = "NONE"
    RESPOND = "RESPOND"
    PASSTHROUGH = "PASSTHROUGH"


class RuleType:
    """RuleType enum values."""

    MIN_TOP_RENDITION_SIZE = "MIN_TOP_RENDITION_SIZE"
    MIN_BOTTOM_RENDITION_SIZE = "MIN_BOTTOM_RENDITION_SIZE"
    FORCE_INCLUDE_RENDITIONS = "FORCE_INCLUDE_RENDITIONS"
    ALLOWED_RENDITIONS = "ALLOWED_RENDITIONS"


class S3ObjectCannedAcl:
    """S3ObjectCannedAcl enum values."""

    PUBLIC_READ = "PUBLIC_READ"
    AUTHENTICATED_READ = "AUTHENTICATED_READ"
    BUCKET_OWNER_READ = "BUCKET_OWNER_READ"
    BUCKET_OWNER_FULL_CONTROL = "BUCKET_OWNER_FULL_CONTROL"


class S3ServerSideEncryptionType:
    """S3ServerSideEncryptionType enum values."""

    SERVER_SIDE_ENCRYPTION_S3 = "SERVER_SIDE_ENCRYPTION_S3"
    SERVER_SIDE_ENCRYPTION_KMS = "SERVER_SIDE_ENCRYPTION_KMS"


class S3StorageClass:
    """S3StorageClass enum values."""

    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    GLACIER = "GLACIER"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"


class SampleRangeConversion:
    """SampleRangeConversion enum values."""

    LIMITED_RANGE_SQUEEZE = "LIMITED_RANGE_SQUEEZE"
    NONE = "NONE"
    LIMITED_RANGE_CLIP = "LIMITED_RANGE_CLIP"


class ScalingBehavior:
    """ScalingBehavior enum values."""

    DEFAULT = "DEFAULT"
    STRETCH_TO_OUTPUT = "STRETCH_TO_OUTPUT"
    FIT = "FIT"
    FIT_NO_UPSCALE = "FIT_NO_UPSCALE"
    FILL = "FILL"


class SccDestinationFramerate:
    """SccDestinationFramerate enum values."""

    FRAMERATE_23_97 = "FRAMERATE_23_97"
    FRAMERATE_24 = "FRAMERATE_24"
    FRAMERATE_25 = "FRAMERATE_25"
    FRAMERATE_29_97_DROPFRAME = "FRAMERATE_29_97_DROPFRAME"
    FRAMERATE_29_97_NON_DROPFRAME = "FRAMERATE_29_97_NON_DROPFRAME"


class ShareStatus:
    """ShareStatus enum values."""

    NOT_SHARED = "NOT_SHARED"
    INITIATED = "INITIATED"
    SHARED = "SHARED"


class SimulateReservedQueue:
    """SimulateReservedQueue enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class SlowPalPitchCorrection:
    """SlowPalPitchCorrection enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class SrtStylePassthrough:
    """SrtStylePassthrough enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class StatusUpdateInterval:
    """StatusUpdateInterval enum values."""

    SECONDS_10 = "SECONDS_10"
    SECONDS_12 = "SECONDS_12"
    SECONDS_15 = "SECONDS_15"
    SECONDS_20 = "SECONDS_20"
    SECONDS_30 = "SECONDS_30"
    SECONDS_60 = "SECONDS_60"
    SECONDS_120 = "SECONDS_120"
    SECONDS_180 = "SECONDS_180"
    SECONDS_240 = "SECONDS_240"
    SECONDS_300 = "SECONDS_300"
    SECONDS_360 = "SECONDS_360"
    SECONDS_420 = "SECONDS_420"
    SECONDS_480 = "SECONDS_480"
    SECONDS_540 = "SECONDS_540"
    SECONDS_600 = "SECONDS_600"


class TamsGapHandling:
    """TamsGapHandling enum values."""

    SKIP_GAPS = "SKIP_GAPS"
    FILL_WITH_BLACK = "FILL_WITH_BLACK"
    HOLD_LAST_FRAME = "HOLD_LAST_FRAME"


class TeletextPageType:
    """TeletextPageType enum values."""

    PAGE_TYPE_INITIAL = "PAGE_TYPE_INITIAL"
    PAGE_TYPE_SUBTITLE = "PAGE_TYPE_SUBTITLE"
    PAGE_TYPE_ADDL_INFO = "PAGE_TYPE_ADDL_INFO"
    PAGE_TYPE_PROGRAM_SCHEDULE = "PAGE_TYPE_PROGRAM_SCHEDULE"
    PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE = "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE"


class TimecodeBurninPosition:
    """TimecodeBurninPosition enum values."""

    TOP_CENTER = "TOP_CENTER"
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"
    MIDDLE_LEFT = "MIDDLE_LEFT"
    MIDDLE_CENTER = "MIDDLE_CENTER"
    MIDDLE_RIGHT = "MIDDLE_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_CENTER = "BOTTOM_CENTER"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"


class TimecodeSource:
    """TimecodeSource enum values."""

    EMBEDDED = "EMBEDDED"
    ZEROBASED = "ZEROBASED"
    SPECIFIEDSTART = "SPECIFIEDSTART"


class TimecodeTrack:
    """TimecodeTrack enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class TimedMetadata:
    """TimedMetadata enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class TrackType:
    """TrackType enum values."""

    VIDEO = "video"
    AUDIO = "audio"
    DATA = "data"


class TransferCharacteristics:
    """TransferCharacteristics enum values."""

    ITU_709 = "ITU_709"
    UNSPECIFIED = "UNSPECIFIED"
    RESERVED = "RESERVED"
    ITU_470M = "ITU_470M"
    ITU_470BG = "ITU_470BG"
    SMPTE_170M = "SMPTE_170M"
    SMPTE_240M = "SMPTE_240M"
    LINEAR = "LINEAR"
    LOG10_2 = "LOG10_2"
    LOC10_2_5 = "LOC10_2_5"
    IEC_61966_2_4 = "IEC_61966_2_4"
    ITU_1361 = "ITU_1361"
    IEC_61966_2_1 = "IEC_61966_2_1"
    ITU_2020_10BIT = "ITU_2020_10bit"
    ITU_2020_12BIT = "ITU_2020_12bit"
    SMPTE_2084 = "SMPTE_2084"
    SMPTE_428_1 = "SMPTE_428_1"
    ARIB_B67 = "ARIB_B67"
    LAST = "LAST"


class TsPtsOffset:
    """TsPtsOffset enum values."""

    AUTO = "AUTO"
    SECONDS = "SECONDS"
    MILLISECONDS = "MILLISECONDS"


class TtmlStylePassthrough:
    """TtmlStylePassthrough enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Type:
    """Type enum values."""

    SYSTEM = "SYSTEM"
    CUSTOM = "CUSTOM"


class UncompressedFourcc:
    """UncompressedFourcc enum values."""

    I420 = "I420"
    I422 = "I422"
    I444 = "I444"


class UncompressedFramerateControl:
    """UncompressedFramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class UncompressedFramerateConversionAlgorithm:
    """UncompressedFramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class UncompressedInterlaceMode:
    """UncompressedInterlaceMode enum values."""

    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class UncompressedScanTypeConversionMode:
    """UncompressedScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class UncompressedSlowPal:
    """UncompressedSlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class UncompressedTelecine:
    """UncompressedTelecine enum values."""

    NONE = "NONE"
    HARD = "HARD"


class Vc3Class:
    """Vc3Class enum values."""

    CLASS_145_8BIT = "CLASS_145_8BIT"
    CLASS_220_8BIT = "CLASS_220_8BIT"
    CLASS_220_10BIT = "CLASS_220_10BIT"


class Vc3FramerateControl:
    """Vc3FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vc3FramerateConversionAlgorithm:
    """Vc3FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Vc3InterlaceMode:
    """Vc3InterlaceMode enum values."""

    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class Vc3ScanTypeConversionMode:
    """Vc3ScanTypeConversionMode enum values."""

    INTERLACED = "INTERLACED"
    INTERLACED_OPTIMIZE = "INTERLACED_OPTIMIZE"


class Vc3SlowPal:
    """Vc3SlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Vc3Telecine:
    """Vc3Telecine enum values."""

    NONE = "NONE"
    HARD = "HARD"


class VchipAction:
    """VchipAction enum values."""

    PASSTHROUGH = "PASSTHROUGH"
    STRIP = "STRIP"


class VideoCodec:
    """VideoCodec enum values."""

    AV1 = "AV1"
    AVC_INTRA = "AVC_INTRA"
    FRAME_CAPTURE = "FRAME_CAPTURE"
    GIF = "GIF"
    H_264 = "H_264"
    H_265 = "H_265"
    MPEG2 = "MPEG2"
    PASSTHROUGH = "PASSTHROUGH"
    PRORES = "PRORES"
    UNCOMPRESSED = "UNCOMPRESSED"
    VC3 = "VC3"
    VP8 = "VP8"
    VP9 = "VP9"
    XAVC = "XAVC"


class VideoOverlayPlayBackMode:
    """VideoOverlayPlayBackMode enum values."""

    ONCE = "ONCE"
    REPEAT = "REPEAT"


class VideoOverlayUnit:
    """VideoOverlayUnit enum values."""

    PIXELS = "PIXELS"
    PERCENTAGE = "PERCENTAGE"


class VideoSelectorMode:
    """VideoSelectorMode enum values."""

    AUTO = "AUTO"
    REMUX_ALL = "REMUX_ALL"


class VideoSelectorType:
    """VideoSelectorType enum values."""

    AUTO = "AUTO"
    STREAM = "STREAM"


class VideoTimecodeInsertion:
    """VideoTimecodeInsertion enum values."""

    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class Vp8FramerateControl:
    """Vp8FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp8FramerateConversionAlgorithm:
    """Vp8FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Vp8ParControl:
    """Vp8ParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp8QualityTuningLevel:
    """Vp8QualityTuningLevel enum values."""

    MULTI_PASS = "MULTI_PASS"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class Vp8RateControlMode:
    """Vp8RateControlMode enum values."""

    VBR = "VBR"


class Vp9FramerateControl:
    """Vp9FramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp9FramerateConversionAlgorithm:
    """Vp9FramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class Vp9ParControl:
    """Vp9ParControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Vp9QualityTuningLevel:
    """Vp9QualityTuningLevel enum values."""

    MULTI_PASS = "MULTI_PASS"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class Vp9RateControlMode:
    """Vp9RateControlMode enum values."""

    VBR = "VBR"


class WatermarkingStrength:
    """WatermarkingStrength enum values."""

    LIGHTEST = "LIGHTEST"
    LIGHTER = "LIGHTER"
    DEFAULT = "DEFAULT"
    STRONGER = "STRONGER"
    STRONGEST = "STRONGEST"


class WavFormat:
    """WavFormat enum values."""

    RIFF = "RIFF"
    RF64 = "RF64"
    EXTENSIBLE = "EXTENSIBLE"


class WebvttAccessibilitySubs:
    """WebvttAccessibilitySubs enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class WebvttStylePassthrough:
    """WebvttStylePassthrough enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    STRICT = "STRICT"
    MERGE = "MERGE"


class Xavc4kIntraCbgProfileClass:
    """Xavc4kIntraCbgProfileClass enum values."""

    CLASS_100 = "CLASS_100"
    CLASS_300 = "CLASS_300"
    CLASS_480 = "CLASS_480"


class Xavc4kIntraVbrProfileClass:
    """Xavc4kIntraVbrProfileClass enum values."""

    CLASS_100 = "CLASS_100"
    CLASS_300 = "CLASS_300"
    CLASS_480 = "CLASS_480"


class Xavc4kProfileBitrateClass:
    """Xavc4kProfileBitrateClass enum values."""

    BITRATE_CLASS_100 = "BITRATE_CLASS_100"
    BITRATE_CLASS_140 = "BITRATE_CLASS_140"
    BITRATE_CLASS_200 = "BITRATE_CLASS_200"


class Xavc4kProfileCodecProfile:
    """Xavc4kProfileCodecProfile enum values."""

    HIGH = "HIGH"
    HIGH_422 = "HIGH_422"


class Xavc4kProfileQualityTuningLevel:
    """Xavc4kProfileQualityTuningLevel enum values."""

    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class XavcAdaptiveQuantization:
    """XavcAdaptiveQuantization enum values."""

    OFF = "OFF"
    AUTO = "AUTO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class XavcEntropyEncoding:
    """XavcEntropyEncoding enum values."""

    AUTO = "AUTO"
    CABAC = "CABAC"
    CAVLC = "CAVLC"


class XavcFlickerAdaptiveQuantization:
    """XavcFlickerAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcFramerateControl:
    """XavcFramerateControl enum values."""

    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class XavcFramerateConversionAlgorithm:
    """XavcFramerateConversionAlgorithm enum values."""

    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"
    FRAMEFORMER = "FRAMEFORMER"
    MAINTAIN_FRAME_COUNT = "MAINTAIN_FRAME_COUNT"


class XavcGopBReference:
    """XavcGopBReference enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcHdIntraCbgProfileClass:
    """XavcHdIntraCbgProfileClass enum values."""

    CLASS_50 = "CLASS_50"
    CLASS_100 = "CLASS_100"
    CLASS_200 = "CLASS_200"


class XavcHdProfileBitrateClass:
    """XavcHdProfileBitrateClass enum values."""

    BITRATE_CLASS_25 = "BITRATE_CLASS_25"
    BITRATE_CLASS_35 = "BITRATE_CLASS_35"
    BITRATE_CLASS_50 = "BITRATE_CLASS_50"


class XavcHdProfileQualityTuningLevel:
    """XavcHdProfileQualityTuningLevel enum values."""

    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


class XavcHdProfileTelecine:
    """XavcHdProfileTelecine enum values."""

    NONE = "NONE"
    HARD = "HARD"


class XavcInterlaceMode:
    """XavcInterlaceMode enum values."""

    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class XavcProfile:
    """XavcProfile enum values."""

    XAVC_HD_INTRA_CBG = "XAVC_HD_INTRA_CBG"
    XAVC_4K_INTRA_CBG = "XAVC_4K_INTRA_CBG"
    XAVC_4K_INTRA_VBR = "XAVC_4K_INTRA_VBR"
    XAVC_HD = "XAVC_HD"
    XAVC_4K = "XAVC_4K"


class XavcSlowPal:
    """XavcSlowPal enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcSpatialAdaptiveQuantization:
    """XavcSpatialAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class XavcTemporalAdaptiveQuantization:
    """XavcTemporalAdaptiveQuantization enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclass
class AccelerationSettings(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, AccelerationMode, Ref, GetAtt, Sub]] = None


@dataclass
class HopDestination(PropertyType):
    WAIT_MINUTES = "WaitMinutes"
    PRIORITY = "Priority"
    QUEUE = "Queue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "wait_minutes": "WaitMinutes",
        "priority": "Priority",
        "queue": "Queue",
    }

    wait_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    queue: Optional[Union[str, Ref, GetAtt, Sub]] = None

