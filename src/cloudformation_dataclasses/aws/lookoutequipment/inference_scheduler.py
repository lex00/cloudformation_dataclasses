"""PropertyTypes for AWS::LookoutEquipment::InferenceScheduler."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AutoPromotionResult:
    """AutoPromotionResult enum values."""

    MODEL_PROMOTED = "MODEL_PROMOTED"
    MODEL_NOT_PROMOTED = "MODEL_NOT_PROMOTED"
    RETRAINING_INTERNAL_ERROR = "RETRAINING_INTERNAL_ERROR"
    RETRAINING_CUSTOMER_ERROR = "RETRAINING_CUSTOMER_ERROR"
    RETRAINING_CANCELLED = "RETRAINING_CANCELLED"


class DataUploadFrequency:
    """DataUploadFrequency enum values."""

    PT5M = "PT5M"
    PT10M = "PT10M"
    PT15M = "PT15M"
    PT30M = "PT30M"
    PT1H = "PT1H"


class DatasetStatus:
    """DatasetStatus enum values."""

    CREATED = "CREATED"
    INGESTION_IN_PROGRESS = "INGESTION_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"


class InferenceDataImportStrategy:
    """InferenceDataImportStrategy enum values."""

    NO_IMPORT = "NO_IMPORT"
    ADD_WHEN_EMPTY = "ADD_WHEN_EMPTY"
    OVERWRITE = "OVERWRITE"


class InferenceExecutionStatus:
    """InferenceExecutionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class InferenceSchedulerStatus:
    """InferenceSchedulerStatus enum values."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class IngestionJobStatus:
    """IngestionJobStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"


class LabelRating:
    """LabelRating enum values."""

    ANOMALY = "ANOMALY"
    NO_ANOMALY = "NO_ANOMALY"
    NEUTRAL = "NEUTRAL"


class LatestInferenceResult:
    """LatestInferenceResult enum values."""

    ANOMALOUS = "ANOMALOUS"
    NORMAL = "NORMAL"


class ModelPromoteMode:
    """ModelPromoteMode enum values."""

    MANAGED = "MANAGED"
    MANUAL = "MANUAL"


class ModelQuality:
    """ModelQuality enum values."""

    QUALITY_THRESHOLD_MET = "QUALITY_THRESHOLD_MET"
    CANNOT_DETERMINE_QUALITY = "CANNOT_DETERMINE_QUALITY"
    POOR_QUALITY_DETECTED = "POOR_QUALITY_DETECTED"


class ModelStatus:
    """ModelStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"


class ModelVersionSourceType:
    """ModelVersionSourceType enum values."""

    TRAINING = "TRAINING"
    RETRAINING = "RETRAINING"
    IMPORT = "IMPORT"


class ModelVersionStatus:
    """ModelVersionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"
    CANCELED = "CANCELED"


class Monotonicity:
    """Monotonicity enum values."""

    DECREASING = "DECREASING"
    INCREASING = "INCREASING"
    STATIC = "STATIC"


class RetrainingSchedulerStatus:
    """RetrainingSchedulerStatus enum values."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class StatisticalIssueStatus:
    """StatisticalIssueStatus enum values."""

    POTENTIAL_ISSUE_DETECTED = "POTENTIAL_ISSUE_DETECTED"
    NO_ISSUE_DETECTED = "NO_ISSUE_DETECTED"


class TargetSamplingRate:
    """TargetSamplingRate enum values."""

    PT1S = "PT1S"
    PT5S = "PT5S"
    PT10S = "PT10S"
    PT15S = "PT15S"
    PT30S = "PT30S"
    PT1M = "PT1M"
    PT5M = "PT5M"
    PT10M = "PT10M"
    PT15M = "PT15M"
    PT30M = "PT30M"
    PT1H = "PT1H"


@dataclass
class DataInputConfiguration(PropertyType):
    INFERENCE_INPUT_NAME_CONFIGURATION = "InferenceInputNameConfiguration"
    S3_INPUT_CONFIGURATION = "S3InputConfiguration"
    INPUT_TIME_ZONE_OFFSET = "InputTimeZoneOffset"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_input_name_configuration": "InferenceInputNameConfiguration",
        "s3_input_configuration": "S3InputConfiguration",
        "input_time_zone_offset": "InputTimeZoneOffset",
    }

    inference_input_name_configuration: Optional[InputNameConfiguration] = None
    s3_input_configuration: Optional[S3InputConfiguration] = None
    input_time_zone_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataOutputConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    S3_OUTPUT_CONFIGURATION = "S3OutputConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "s3_output_configuration": "S3OutputConfiguration",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_configuration: Optional[S3OutputConfiguration] = None


@dataclass
class InputNameConfiguration(PropertyType):
    COMPONENT_TIMESTAMP_DELIMITER = "ComponentTimestampDelimiter"
    TIMESTAMP_FORMAT = "TimestampFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "component_timestamp_delimiter": "ComponentTimestampDelimiter",
        "timestamp_format": "TimestampFormat",
    }

    component_timestamp_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3InputConfiguration(PropertyType):
    BUCKET = "Bucket"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3OutputConfiguration(PropertyType):
    BUCKET = "Bucket"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

