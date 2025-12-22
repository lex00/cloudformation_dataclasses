"""PropertyTypes for AWS::Evidently::Feature."""

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
class EntityOverride(PropertyType):
    ENTITY_ID = "EntityId"
    VARIATION = "Variation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id": "EntityId",
        "variation": "Variation",
    }

    entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variation: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VariationObject(PropertyType):
    VARIATION_NAME = "VariationName"
    DOUBLE_VALUE = "DoubleValue"
    BOOLEAN_VALUE = "BooleanValue"
    LONG_VALUE = "LongValue"
    STRING_VALUE = "StringValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variation_name": "VariationName",
        "double_value": "DoubleValue",
        "boolean_value": "BooleanValue",
        "long_value": "LongValue",
        "string_value": "StringValue",
    }

    variation_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    double_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    boolean_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    long_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None

