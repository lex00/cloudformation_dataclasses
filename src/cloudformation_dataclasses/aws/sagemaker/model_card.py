"""PropertyTypes for AWS::SageMaker::ModelCard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalInformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ethical_considerations": "EthicalConsiderations",
        "caveats_and_recommendations": "CaveatsAndRecommendations",
        "custom_details": "CustomDetails",
    }

    ethical_considerations: Optional[Union[str, Ref, GetAtt, Sub]] = None
    caveats_and_recommendations: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_details: Optional[dict[str, str]] = None


@dataclass
class BusinessDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "business_stakeholders": "BusinessStakeholders",
        "line_of_business": "LineOfBusiness",
        "business_problem": "BusinessProblem",
    }

    business_stakeholders: Optional[Union[str, Ref, GetAtt, Sub]] = None
    line_of_business: Optional[Union[str, Ref, GetAtt, Sub]] = None
    business_problem: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Container(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nearest_model_name": "NearestModelName",
        "model_data_url": "ModelDataUrl",
        "image": "Image",
    }

    nearest_model_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_data_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Content(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intended_uses": "IntendedUses",
        "additional_information": "AdditionalInformation",
        "model_overview": "ModelOverview",
        "training_details": "TrainingDetails",
        "evaluation_details": "EvaluationDetails",
        "model_package_details": "ModelPackageDetails",
        "business_details": "BusinessDetails",
    }

    intended_uses: Optional[IntendedUses] = None
    additional_information: Optional[AdditionalInformation] = None
    model_overview: Optional[ModelOverview] = None
    training_details: Optional[TrainingDetails] = None
    evaluation_details: Optional[list[EvaluationDetail]] = None
    model_package_details: Optional[ModelPackageDetails] = None
    business_details: Optional[BusinessDetails] = None


@dataclass
class EvaluationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "datasets": "Datasets",
        "evaluation_observation": "EvaluationObservation",
        "metric_groups": "MetricGroups",
        "metadata": "Metadata",
        "evaluation_job_arn": "EvaluationJobArn",
        "name": "Name",
    }

    datasets: Optional[Union[list[str], Ref]] = None
    evaluation_observation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_groups: Optional[list[MetricGroup]] = None
    metadata: Optional[dict[str, str]] = None
    evaluation_job_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Function(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "function": "Function",
        "facet": "Facet",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    facet: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceEnvironment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_image": "ContainerImage",
    }

    container_image: Optional[Union[list[str], Ref]] = None


@dataclass
class InferenceSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "containers": "Containers",
    }

    containers: Optional[list[Container]] = None


@dataclass
class IntendedUses(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intended_uses": "IntendedUses",
        "factors_affecting_model_efficiency": "FactorsAffectingModelEfficiency",
        "purpose_of_model": "PurposeOfModel",
        "risk_rating": "RiskRating",
        "explanations_for_risk_rating": "ExplanationsForRiskRating",
    }

    intended_uses: Optional[Union[str, Ref, GetAtt, Sub]] = None
    factors_affecting_model_efficiency: Optional[Union[str, Ref, GetAtt, Sub]] = None
    purpose_of_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    risk_rating: Optional[Union[str, Ref, GetAtt, Sub]] = None
    explanations_for_risk_rating: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDataItems(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "x_axis_name": "XAxisName",
        "type_": "Type",
        "value": "Value",
        "y_axis_name": "YAxisName",
        "notes": "Notes",
        "name": "Name",
    }

    x_axis_name: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    y_axis_name: Optional[Union[list[str], Ref]] = None
    notes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "metric_data": "MetricData",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_data: Optional[list[MetricDataItems]] = None


@dataclass
class ModelOverview(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_owner": "ModelOwner",
        "model_artifact": "ModelArtifact",
        "algorithm_type": "AlgorithmType",
        "model_name": "ModelName",
        "inference_environment": "InferenceEnvironment",
        "problem_type": "ProblemType",
        "model_description": "ModelDescription",
        "model_version": "ModelVersion",
        "model_creator": "ModelCreator",
        "model_id": "ModelId",
    }

    model_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_artifact: Optional[Union[list[str], Ref]] = None
    algorithm_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inference_environment: Optional[InferenceEnvironment] = None
    problem_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_version: Optional[Union[float, Ref, GetAtt, Sub]] = None
    model_creator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelPackageCreator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "user_profile_name": "UserProfileName",
    }

    user_profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelPackageDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_package_group_name": "ModelPackageGroupName",
        "task": "Task",
        "created_by": "CreatedBy",
        "approval_description": "ApprovalDescription",
        "model_approval_status": "ModelApprovalStatus",
        "model_package_version": "ModelPackageVersion",
        "model_package_description": "ModelPackageDescription",
        "model_package_name": "ModelPackageName",
        "model_package_status": "ModelPackageStatus",
        "source_algorithms": "SourceAlgorithms",
        "inference_specification": "InferenceSpecification",
        "model_package_arn": "ModelPackageArn",
        "domain": "Domain",
    }

    model_package_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_by: Optional[ModelPackageCreator] = None
    approval_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_approval_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_package_version: Optional[Union[float, Ref, GetAtt, Sub]] = None
    model_package_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_package_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_package_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_algorithms: Optional[list[SourceAlgorithm]] = None
    inference_specification: Optional[InferenceSpecification] = None
    model_package_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectiveFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "notes": "Notes",
    }

    function: Optional[Function] = None
    notes: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecurityConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceAlgorithm(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_data_url": "ModelDataUrl",
        "algorithm_name": "AlgorithmName",
    }

    model_data_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    algorithm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrainingDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "objective_function": "ObjectiveFunction",
        "training_observations": "TrainingObservations",
        "training_job_details": "TrainingJobDetails",
    }

    objective_function: Optional[ObjectiveFunction] = None
    training_observations: Optional[Union[str, Ref, GetAtt, Sub]] = None
    training_job_details: Optional[TrainingJobDetails] = None


@dataclass
class TrainingEnvironment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_image": "ContainerImage",
    }

    container_image: Optional[Union[list[str], Ref]] = None


@dataclass
class TrainingHyperParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrainingJobDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "training_metrics": "TrainingMetrics",
        "hyper_parameters": "HyperParameters",
        "training_arn": "TrainingArn",
        "user_provided_training_metrics": "UserProvidedTrainingMetrics",
        "training_environment": "TrainingEnvironment",
        "training_datasets": "TrainingDatasets",
        "user_provided_hyper_parameters": "UserProvidedHyperParameters",
    }

    training_metrics: Optional[list[TrainingMetric]] = None
    hyper_parameters: Optional[list[TrainingHyperParameter]] = None
    training_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_provided_training_metrics: Optional[list[TrainingMetric]] = None
    training_environment: Optional[TrainingEnvironment] = None
    training_datasets: Optional[Union[list[str], Ref]] = None
    user_provided_hyper_parameters: Optional[list[TrainingHyperParameter]] = None


@dataclass
class TrainingMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "notes": "Notes",
        "name": "Name",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    notes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_id": "DomainId",
        "user_profile_arn": "UserProfileArn",
        "user_profile_name": "UserProfileName",
    }

    domain_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

