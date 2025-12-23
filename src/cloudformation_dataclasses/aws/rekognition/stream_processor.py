"""PropertyTypes for AWS::Rekognition::StreamProcessor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

