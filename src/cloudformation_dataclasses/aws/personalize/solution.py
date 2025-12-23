"""PropertyTypes for AWS::Personalize::Solution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AlgorithmHyperParameterRanges(PropertyType):
    INTEGER_HYPER_PARAMETER_RANGES = "IntegerHyperParameterRanges"
    CATEGORICAL_HYPER_PARAMETER_RANGES = "CategoricalHyperParameterRanges"
    CONTINUOUS_HYPER_PARAMETER_RANGES = "ContinuousHyperParameterRanges"

    _property_mappings: ClassVar[dict[str, str]] = {
        "integer_hyper_parameter_ranges": "IntegerHyperParameterRanges",
        "categorical_hyper_parameter_ranges": "CategoricalHyperParameterRanges",
        "continuous_hyper_parameter_ranges": "ContinuousHyperParameterRanges",
    }

    integer_hyper_parameter_ranges: Optional[list[IntegerHyperParameterRange]] = None
    categorical_hyper_parameter_ranges: Optional[list[CategoricalHyperParameterRange]] = None
    continuous_hyper_parameter_ranges: Optional[list[ContinuousHyperParameterRange]] = None


@dataclass
class AutoMLConfig(PropertyType):
    METRIC_NAME = "MetricName"
    RECIPE_LIST = "RecipeList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "recipe_list": "RecipeList",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recipe_list: Optional[Union[list[str], Ref]] = None


@dataclass
class CategoricalHyperParameterRange(PropertyType):
    VALUES = "Values"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContinuousHyperParameterRange(PropertyType):
    MIN_VALUE = "MinValue"
    MAX_VALUE = "MaxValue"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_value": "MinValue",
        "max_value": "MaxValue",
        "name": "Name",
    }

    min_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HpoConfig(PropertyType):
    HPO_RESOURCE_CONFIG = "HpoResourceConfig"
    ALGORITHM_HYPER_PARAMETER_RANGES = "AlgorithmHyperParameterRanges"
    HPO_OBJECTIVE = "HpoObjective"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hpo_resource_config": "HpoResourceConfig",
        "algorithm_hyper_parameter_ranges": "AlgorithmHyperParameterRanges",
        "hpo_objective": "HpoObjective",
    }

    hpo_resource_config: Optional[HpoResourceConfig] = None
    algorithm_hyper_parameter_ranges: Optional[AlgorithmHyperParameterRanges] = None
    hpo_objective: Optional[HpoObjective] = None


@dataclass
class HpoObjective(PropertyType):
    METRIC_NAME = "MetricName"
    TYPE = "Type"
    METRIC_REGEX = "MetricRegex"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "type_": "Type",
        "metric_regex": "MetricRegex",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HpoResourceConfig(PropertyType):
    MAX_PARALLEL_TRAINING_JOBS = "MaxParallelTrainingJobs"
    MAX_NUMBER_OF_TRAINING_JOBS = "MaxNumberOfTrainingJobs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_parallel_training_jobs": "MaxParallelTrainingJobs",
        "max_number_of_training_jobs": "MaxNumberOfTrainingJobs",
    }

    max_parallel_training_jobs: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_number_of_training_jobs: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerHyperParameterRange(PropertyType):
    MIN_VALUE = "MinValue"
    MAX_VALUE = "MaxValue"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_value": "MinValue",
        "max_value": "MaxValue",
        "name": "Name",
    }

    min_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SolutionConfig(PropertyType):
    EVENT_VALUE_THRESHOLD = "EventValueThreshold"
    HPO_CONFIG = "HpoConfig"
    ALGORITHM_HYPER_PARAMETERS = "AlgorithmHyperParameters"
    FEATURE_TRANSFORMATION_PARAMETERS = "FeatureTransformationParameters"
    AUTO_ML_CONFIG = "AutoMLConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_value_threshold": "EventValueThreshold",
        "hpo_config": "HpoConfig",
        "algorithm_hyper_parameters": "AlgorithmHyperParameters",
        "feature_transformation_parameters": "FeatureTransformationParameters",
        "auto_ml_config": "AutoMLConfig",
    }

    event_value_threshold: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hpo_config: Optional[HpoConfig] = None
    algorithm_hyper_parameters: Optional[dict[str, str]] = None
    feature_transformation_parameters: Optional[dict[str, str]] = None
    auto_ml_config: Optional[AutoMLConfig] = None

