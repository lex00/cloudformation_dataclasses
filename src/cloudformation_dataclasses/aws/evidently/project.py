"""PropertyTypes for AWS::Evidently::Project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChangeDirectionEnum:
    """ChangeDirectionEnum enum values."""

    INCREASE = "INCREASE"
    DECREASE = "DECREASE"


class EventType:
    """EventType enum values."""

    AWS_EVIDENTLY_EVALUATION = "aws.evidently.evaluation"
    AWS_EVIDENTLY_CUSTOM = "aws.evidently.custom"


class ExperimentBaseStat:
    """ExperimentBaseStat enum values."""

    MEAN = "Mean"


class ExperimentReportName:
    """ExperimentReportName enum values."""

    BAYESIANINFERENCE = "BayesianInference"


class ExperimentResultRequestType:
    """ExperimentResultRequestType enum values."""

    BASESTAT = "BaseStat"
    TREATMENTEFFECT = "TreatmentEffect"
    CONFIDENCEINTERVAL = "ConfidenceInterval"
    PVALUE = "PValue"


class ExperimentResultResponseType:
    """ExperimentResultResponseType enum values."""

    MEAN = "Mean"
    TREATMENTEFFECT = "TreatmentEffect"
    CONFIDENCEINTERVALUPPERBOUND = "ConfidenceIntervalUpperBound"
    CONFIDENCEINTERVALLOWERBOUND = "ConfidenceIntervalLowerBound"
    PVALUE = "PValue"


class ExperimentStatus:
    """ExperimentStatus enum values."""

    CREATED = "CREATED"
    UPDATING = "UPDATING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ExperimentStopDesiredState:
    """ExperimentStopDesiredState enum values."""

    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ExperimentType:
    """ExperimentType enum values."""

    AWS_EVIDENTLY_ONLINEAB = "aws.evidently.onlineab"


class FeatureEvaluationStrategy:
    """FeatureEvaluationStrategy enum values."""

    ALL_RULES = "ALL_RULES"
    DEFAULT_VARIATION = "DEFAULT_VARIATION"


class FeatureStatus:
    """FeatureStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"


class LaunchStatus:
    """LaunchStatus enum values."""

    CREATED = "CREATED"
    UPDATING = "UPDATING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class LaunchStopDesiredState:
    """LaunchStopDesiredState enum values."""

    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class LaunchType:
    """LaunchType enum values."""

    AWS_EVIDENTLY_SPLITS = "aws.evidently.splits"


class ProjectStatus:
    """ProjectStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"


class SegmentReferenceResourceType:
    """SegmentReferenceResourceType enum values."""

    EXPERIMENT = "EXPERIMENT"
    LAUNCH = "LAUNCH"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


class VariationValueType:
    """VariationValueType enum values."""

    STRING = "STRING"
    LONG = "LONG"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"


@dataclass
class AppConfigResourceObject(PropertyType):
    ENVIRONMENT_ID = "EnvironmentId"
    APPLICATION_ID = "ApplicationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "environment_id": "EnvironmentId",
        "application_id": "ApplicationId",
    }

    environment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataDeliveryObject(PropertyType):
    S3 = "S3"
    LOG_GROUP = "LogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "log_group": "LogGroup",
    }

    s3: Optional[S3Destination] = None
    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Destination(PropertyType):
    BUCKET_NAME = "BucketName"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "prefix": "Prefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

