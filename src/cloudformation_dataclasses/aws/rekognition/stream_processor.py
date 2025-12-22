"""PropertyTypes for AWS::Rekognition::StreamProcessor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Attribute:
    """Attribute enum values."""

    DEFAULT = "DEFAULT"
    ALL = "ALL"
    AGE_RANGE = "AGE_RANGE"
    BEARD = "BEARD"
    EMOTIONS = "EMOTIONS"
    EYE_DIRECTION = "EYE_DIRECTION"
    EYEGLASSES = "EYEGLASSES"
    EYES_OPEN = "EYES_OPEN"
    GENDER = "GENDER"
    MOUTH_OPEN = "MOUTH_OPEN"
    MUSTACHE = "MUSTACHE"
    FACE_OCCLUDED = "FACE_OCCLUDED"
    SMILE = "SMILE"
    SUNGLASSES = "SUNGLASSES"


class BodyPart:
    """BodyPart enum values."""

    FACE = "FACE"
    HEAD = "HEAD"
    LEFT_HAND = "LEFT_HAND"
    RIGHT_HAND = "RIGHT_HAND"


class CelebrityRecognitionSortBy:
    """CelebrityRecognitionSortBy enum values."""

    ID = "ID"
    TIMESTAMP = "TIMESTAMP"


class ChallengeType:
    """ChallengeType enum values."""

    FACEMOVEMENTANDLIGHTCHALLENGE = "FaceMovementAndLightChallenge"
    FACEMOVEMENTCHALLENGE = "FaceMovementChallenge"


class ContentClassifier:
    """ContentClassifier enum values."""

    FREEOFPERSONALLYIDENTIFIABLEINFORMATION = "FreeOfPersonallyIdentifiableInformation"
    FREEOFADULTCONTENT = "FreeOfAdultContent"


class ContentModerationAggregateBy:
    """ContentModerationAggregateBy enum values."""

    TIMESTAMPS = "TIMESTAMPS"
    SEGMENTS = "SEGMENTS"


class ContentModerationSortBy:
    """ContentModerationSortBy enum values."""

    NAME = "NAME"
    TIMESTAMP = "TIMESTAMP"


class CustomizationFeature:
    """CustomizationFeature enum values."""

    CONTENT_MODERATION = "CONTENT_MODERATION"
    CUSTOM_LABELS = "CUSTOM_LABELS"


class DatasetStatus:
    """DatasetStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"


class DatasetStatusMessageCode:
    """DatasetStatusMessageCode enum values."""

    SUCCESS = "SUCCESS"
    SERVICE_ERROR = "SERVICE_ERROR"
    CLIENT_ERROR = "CLIENT_ERROR"


class DatasetType:
    """DatasetType enum values."""

    TRAIN = "TRAIN"
    TEST = "TEST"


class DetectLabelsFeatureName:
    """DetectLabelsFeatureName enum values."""

    GENERAL_LABELS = "GENERAL_LABELS"
    IMAGE_PROPERTIES = "IMAGE_PROPERTIES"


class EmotionName:
    """EmotionName enum values."""

    HAPPY = "HAPPY"
    SAD = "SAD"
    ANGRY = "ANGRY"
    CONFUSED = "CONFUSED"
    DISGUSTED = "DISGUSTED"
    SURPRISED = "SURPRISED"
    CALM = "CALM"
    UNKNOWN = "UNKNOWN"
    FEAR = "FEAR"


class FaceAttributes:
    """FaceAttributes enum values."""

    DEFAULT = "DEFAULT"
    ALL = "ALL"


class FaceSearchSortBy:
    """FaceSearchSortBy enum values."""

    INDEX = "INDEX"
    TIMESTAMP = "TIMESTAMP"


class GenderType:
    """GenderType enum values."""

    MALE = "Male"
    FEMALE = "Female"


class KnownGenderType:
    """KnownGenderType enum values."""

    MALE = "Male"
    FEMALE = "Female"
    NONBINARY = "Nonbinary"
    UNLISTED = "Unlisted"


class LabelDetectionAggregateBy:
    """LabelDetectionAggregateBy enum values."""

    TIMESTAMPS = "TIMESTAMPS"
    SEGMENTS = "SEGMENTS"


class LabelDetectionFeatureName:
    """LabelDetectionFeatureName enum values."""

    GENERAL_LABELS = "GENERAL_LABELS"


class LabelDetectionSortBy:
    """LabelDetectionSortBy enum values."""

    NAME = "NAME"
    TIMESTAMP = "TIMESTAMP"


class LandmarkType:
    """LandmarkType enum values."""

    EYELEFT = "eyeLeft"
    EYERIGHT = "eyeRight"
    NOSE = "nose"
    MOUTHLEFT = "mouthLeft"
    MOUTHRIGHT = "mouthRight"
    LEFTEYEBROWLEFT = "leftEyeBrowLeft"
    LEFTEYEBROWRIGHT = "leftEyeBrowRight"
    LEFTEYEBROWUP = "leftEyeBrowUp"
    RIGHTEYEBROWLEFT = "rightEyeBrowLeft"
    RIGHTEYEBROWRIGHT = "rightEyeBrowRight"
    RIGHTEYEBROWUP = "rightEyeBrowUp"
    LEFTEYELEFT = "leftEyeLeft"
    LEFTEYERIGHT = "leftEyeRight"
    LEFTEYEUP = "leftEyeUp"
    LEFTEYEDOWN = "leftEyeDown"
    RIGHTEYELEFT = "rightEyeLeft"
    RIGHTEYERIGHT = "rightEyeRight"
    RIGHTEYEUP = "rightEyeUp"
    RIGHTEYEDOWN = "rightEyeDown"
    NOSELEFT = "noseLeft"
    NOSERIGHT = "noseRight"
    MOUTHUP = "mouthUp"
    MOUTHDOWN = "mouthDown"
    LEFTPUPIL = "leftPupil"
    RIGHTPUPIL = "rightPupil"
    UPPERJAWLINELEFT = "upperJawlineLeft"
    MIDJAWLINELEFT = "midJawlineLeft"
    CHINBOTTOM = "chinBottom"
    MIDJAWLINERIGHT = "midJawlineRight"
    UPPERJAWLINERIGHT = "upperJawlineRight"


class LivenessSessionStatus:
    """LivenessSessionStatus enum values."""

    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"


class MediaAnalysisJobFailureCode:
    """MediaAnalysisJobFailureCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_S3_OBJECT = "INVALID_S3_OBJECT"
    INVALID_MANIFEST = "INVALID_MANIFEST"
    INVALID_OUTPUT_CONFIG = "INVALID_OUTPUT_CONFIG"
    INVALID_KMS_KEY = "INVALID_KMS_KEY"
    ACCESS_DENIED = "ACCESS_DENIED"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    RESOURCE_NOT_READY = "RESOURCE_NOT_READY"
    THROTTLED = "THROTTLED"


class MediaAnalysisJobStatus:
    """MediaAnalysisJobStatus enum values."""

    CREATED = "CREATED"
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class OrientationCorrection:
    """OrientationCorrection enum values."""

    ROTATE_0 = "ROTATE_0"
    ROTATE_90 = "ROTATE_90"
    ROTATE_180 = "ROTATE_180"
    ROTATE_270 = "ROTATE_270"


class PersonTrackingSortBy:
    """PersonTrackingSortBy enum values."""

    INDEX = "INDEX"
    TIMESTAMP = "TIMESTAMP"


class ProjectAutoUpdate:
    """ProjectAutoUpdate enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ProjectStatus:
    """ProjectStatus enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    DELETING = "DELETING"


class ProjectVersionStatus:
    """ProjectVersionStatus enum values."""

    TRAINING_IN_PROGRESS = "TRAINING_IN_PROGRESS"
    TRAINING_COMPLETED = "TRAINING_COMPLETED"
    TRAINING_FAILED = "TRAINING_FAILED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    DELETING = "DELETING"
    COPYING_IN_PROGRESS = "COPYING_IN_PROGRESS"
    COPYING_COMPLETED = "COPYING_COMPLETED"
    COPYING_FAILED = "COPYING_FAILED"
    DEPRECATED = "DEPRECATED"
    EXPIRED = "EXPIRED"


class ProtectiveEquipmentType:
    """ProtectiveEquipmentType enum values."""

    FACE_COVER = "FACE_COVER"
    HAND_COVER = "HAND_COVER"
    HEAD_COVER = "HEAD_COVER"


class QualityFilter:
    """QualityFilter enum values."""

    NONE = "NONE"
    AUTO = "AUTO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Reason:
    """Reason enum values."""

    EXCEEDS_MAX_FACES = "EXCEEDS_MAX_FACES"
    EXTREME_POSE = "EXTREME_POSE"
    LOW_BRIGHTNESS = "LOW_BRIGHTNESS"
    LOW_SHARPNESS = "LOW_SHARPNESS"
    LOW_CONFIDENCE = "LOW_CONFIDENCE"
    SMALL_BOUNDING_BOX = "SMALL_BOUNDING_BOX"
    LOW_FACE_QUALITY = "LOW_FACE_QUALITY"


class SegmentType:
    """SegmentType enum values."""

    TECHNICAL_CUE = "TECHNICAL_CUE"
    SHOT = "SHOT"


class StreamProcessorParameterToDelete:
    """StreamProcessorParameterToDelete enum values."""

    CONNECTEDHOMEMINCONFIDENCE = "ConnectedHomeMinConfidence"
    REGIONSOFINTEREST = "RegionsOfInterest"


class StreamProcessorStatus:
    """StreamProcessorStatus enum values."""

    STOPPED = "STOPPED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    UPDATING = "UPDATING"


class TechnicalCueType:
    """TechnicalCueType enum values."""

    COLORBARS = "ColorBars"
    ENDCREDITS = "EndCredits"
    BLACKFRAMES = "BlackFrames"
    OPENINGCREDITS = "OpeningCredits"
    STUDIOLOGO = "StudioLogo"
    SLATE = "Slate"
    CONTENT = "Content"


class TextTypes:
    """TextTypes enum values."""

    LINE = "LINE"
    WORD = "WORD"


class UnsearchedFaceReason:
    """UnsearchedFaceReason enum values."""

    FACE_NOT_LARGEST = "FACE_NOT_LARGEST"
    EXCEEDS_MAX_FACES = "EXCEEDS_MAX_FACES"
    EXTREME_POSE = "EXTREME_POSE"
    LOW_BRIGHTNESS = "LOW_BRIGHTNESS"
    LOW_SHARPNESS = "LOW_SHARPNESS"
    LOW_CONFIDENCE = "LOW_CONFIDENCE"
    SMALL_BOUNDING_BOX = "SMALL_BOUNDING_BOX"
    LOW_FACE_QUALITY = "LOW_FACE_QUALITY"


class UnsuccessfulFaceAssociationReason:
    """UnsuccessfulFaceAssociationReason enum values."""

    FACE_NOT_FOUND = "FACE_NOT_FOUND"
    ASSOCIATED_TO_A_DIFFERENT_USER = "ASSOCIATED_TO_A_DIFFERENT_USER"
    LOW_MATCH_CONFIDENCE = "LOW_MATCH_CONFIDENCE"


class UnsuccessfulFaceDeletionReason:
    """UnsuccessfulFaceDeletionReason enum values."""

    ASSOCIATED_TO_AN_EXISTING_USER = "ASSOCIATED_TO_AN_EXISTING_USER"
    FACE_NOT_FOUND = "FACE_NOT_FOUND"


class UnsuccessfulFaceDisassociationReason:
    """UnsuccessfulFaceDisassociationReason enum values."""

    FACE_NOT_FOUND = "FACE_NOT_FOUND"
    ASSOCIATED_TO_A_DIFFERENT_USER = "ASSOCIATED_TO_A_DIFFERENT_USER"


class UserStatus:
    """UserStatus enum values."""

    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    CREATING = "CREATING"
    CREATED = "CREATED"


class VideoColorRange:
    """VideoColorRange enum values."""

    FULL = "FULL"
    LIMITED = "LIMITED"


class VideoJobStatus:
    """VideoJobStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclass
class BoundingBox(PropertyType):
    LEFT = "Left"
    TOP = "Top"
    HEIGHT = "Height"
    WIDTH = "Width"

    _property_mappings: ClassVar[dict[str, str]] = {
        "left": "Left",
        "top": "Top",
        "height": "Height",
        "width": "Width",
    }

    left: Optional[Union[float, Ref, GetAtt, Sub]] = None
    top: Optional[Union[float, Ref, GetAtt, Sub]] = None
    height: Optional[Union[float, Ref, GetAtt, Sub]] = None
    width: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectedHomeSettings(PropertyType):
    MIN_CONFIDENCE = "MinConfidence"
    LABELS = "Labels"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_confidence": "MinConfidence",
        "labels": "Labels",
    }

    min_confidence: Optional[Union[float, Ref, GetAtt, Sub]] = None
    labels: Optional[Union[list[str], Ref]] = None


@dataclass
class DataSharingPreference(PropertyType):
    OPT_IN = "OptIn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "opt_in": "OptIn",
    }

    opt_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FaceSearchSettings(PropertyType):
    COLLECTION_ID = "CollectionId"
    FACE_MATCH_THRESHOLD = "FaceMatchThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "collection_id": "CollectionId",
        "face_match_threshold": "FaceMatchThreshold",
    }

    collection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    face_match_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisDataStream(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisVideoStream(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationChannel(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Destination(PropertyType):
    BUCKET_NAME = "BucketName"
    OBJECT_KEY_PREFIX = "ObjectKeyPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "object_key_prefix": "ObjectKeyPrefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

