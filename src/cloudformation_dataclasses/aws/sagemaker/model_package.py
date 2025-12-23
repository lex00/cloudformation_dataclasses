"""PropertyTypes for AWS::SageMaker::ModelPackage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalInferenceSpecificationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "supported_content_types": "SupportedContentTypes",
        "supported_realtime_inference_instance_types": "SupportedRealtimeInferenceInstanceTypes",
        "containers": "Containers",
        "supported_transform_instance_types": "SupportedTransformInstanceTypes",
        "name": "Name",
        "supported_response_mime_types": "SupportedResponseMIMETypes",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    supported_content_types: Optional[Union[list[str], Ref]] = None
    supported_realtime_inference_instance_types: Optional[Union[list[str], Ref]] = None
    containers: Optional[list[ModelPackageContainerDefinition]] = None
    supported_transform_instance_types: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    supported_response_mime_types: Optional[Union[list[str], Ref]] = None


@dataclass
class Bias(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "report": "Report",
        "pre_training_report": "PreTrainingReport",
        "post_training_report": "PostTrainingReport",
    }

    report: Optional[MetricsSource] = None
    pre_training_report: Optional[MetricsSource] = None
    post_training_report: Optional[MetricsSource] = None


@dataclass
class DataSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_source": "S3DataSource",
    }

    s3_data_source: Optional[S3DataSource] = None


@dataclass
class DriftCheckBaselines(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_data_quality": "ModelDataQuality",
        "bias": "Bias",
        "model_quality": "ModelQuality",
        "explainability": "Explainability",
    }

    model_data_quality: Optional[DriftCheckModelDataQuality] = None
    bias: Optional[DriftCheckBias] = None
    model_quality: Optional[DriftCheckModelQuality] = None
    explainability: Optional[DriftCheckExplainability] = None


@dataclass
class DriftCheckBias(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pre_training_constraints": "PreTrainingConstraints",
        "config_file": "ConfigFile",
        "post_training_constraints": "PostTrainingConstraints",
    }

    pre_training_constraints: Optional[MetricsSource] = None
    config_file: Optional[FileSource] = None
    post_training_constraints: Optional[MetricsSource] = None


@dataclass
class DriftCheckExplainability(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "config_file": "ConfigFile",
    }

    constraints: Optional[MetricsSource] = None
    config_file: Optional[FileSource] = None


@dataclass
class DriftCheckModelDataQuality(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class DriftCheckModelQuality(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class Explainability(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "report": "Report",
    }

    report: Optional[MetricsSource] = None


@dataclass
class FileSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_type": "ContentType",
        "s3_uri": "S3Uri",
        "content_digest": "ContentDigest",
    }

    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_digest: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_content_types": "SupportedContentTypes",
        "supported_realtime_inference_instance_types": "SupportedRealtimeInferenceInstanceTypes",
        "containers": "Containers",
        "supported_transform_instance_types": "SupportedTransformInstanceTypes",
        "supported_response_mime_types": "SupportedResponseMIMETypes",
    }

    supported_content_types: Optional[Union[list[str], Ref]] = None
    supported_realtime_inference_instance_types: Optional[Union[list[str], Ref]] = None
    containers: Optional[list[ModelPackageContainerDefinition]] = None
    supported_transform_instance_types: Optional[Union[list[str], Ref]] = None
    supported_response_mime_types: Optional[Union[list[str], Ref]] = None


@dataclass
class MetadataProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "generated_by": "GeneratedBy",
        "repository": "Repository",
        "commit_id": "CommitId",
        "project_id": "ProjectId",
    }

    generated_by: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository: Optional[Union[str, Ref, GetAtt, Sub]] = None
    commit_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    project_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_type": "ContentType",
        "s3_uri": "S3Uri",
        "content_digest": "ContentDigest",
    }

    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_digest: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelAccessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "accept_eula": "AcceptEula",
    }

    accept_eula: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ModelCard(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_card_status": "ModelCardStatus",
        "model_card_content": "ModelCardContent",
    }

    model_card_status: Optional[Union[str, ModelCardStatus, Ref, GetAtt, Sub]] = None
    model_card_content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelDataQuality(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class ModelDataSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_source": "S3DataSource",
    }

    s3_data_source: Optional[S3ModelDataSource] = None


@dataclass
class ModelInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_input_config": "DataInputConfig",
    }

    data_input_config: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelMetrics(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_data_quality": "ModelDataQuality",
        "bias": "Bias",
        "model_quality": "ModelQuality",
        "explainability": "Explainability",
    }

    model_data_quality: Optional[ModelDataQuality] = None
    bias: Optional[Bias] = None
    model_quality: Optional[ModelQuality] = None
    explainability: Optional[Explainability] = None


@dataclass
class ModelPackageContainerDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_input": "ModelInput",
        "nearest_model_name": "NearestModelName",
        "container_hostname": "ContainerHostname",
        "image_digest": "ImageDigest",
        "framework_version": "FrameworkVersion",
        "environment": "Environment",
        "model_data_url": "ModelDataUrl",
        "image": "Image",
        "model_data_source": "ModelDataSource",
        "framework": "Framework",
    }

    model_input: Optional[ModelInput] = None
    nearest_model_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_digest: Optional[Union[str, Ref, GetAtt, Sub]] = None
    framework_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment: Optional[dict[str, str]] = None
    model_data_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_data_source: Optional[ModelDataSource] = None
    framework: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelPackageStatusDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validation_statuses": "ValidationStatuses",
    }

    validation_statuses: Optional[list[ModelPackageStatusItem]] = None


@dataclass
class ModelPackageStatusItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "failure_reason": "FailureReason",
        "name": "Name",
    }

    status: Optional[Union[str, DetailedModelPackageStatus, Ref, GetAtt, Sub]] = None
    failure_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelQuality(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class S3DataSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "s3_data_type": "S3DataType",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_data_type: Optional[Union[str, S3DataType, Ref, GetAtt, Sub]] = None


@dataclass
class S3ModelDataSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_access_config": "ModelAccessConfig",
        "s3_data_type": "S3DataType",
        "compression_type": "CompressionType",
        "s3_uri": "S3Uri",
    }

    model_access_config: Optional[ModelAccessConfig] = None
    s3_data_type: Optional[Union[str, S3ModelDataType, Ref, GetAtt, Sub]] = None
    compression_type: Optional[Union[str, ModelCompressionType, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class SourceAlgorithmSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_algorithms": "SourceAlgorithms",
    }

    source_algorithms: Optional[list[SourceAlgorithm]] = None


@dataclass
class TransformInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_type": "ContentType",
        "split_type": "SplitType",
        "compression_type": "CompressionType",
        "data_source": "DataSource",
    }

    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    split_type: Optional[Union[str, SplitType, Ref, GetAtt, Sub]] = None
    compression_type: Optional[Union[str, CompressionType, Ref, GetAtt, Sub]] = None
    data_source: Optional[DataSource] = None


@dataclass
class TransformJobDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transform_resources": "TransformResources",
        "max_concurrent_transforms": "MaxConcurrentTransforms",
        "max_payload_in_mb": "MaxPayloadInMB",
        "transform_output": "TransformOutput",
        "environment": "Environment",
        "transform_input": "TransformInput",
        "batch_strategy": "BatchStrategy",
    }

    transform_resources: Optional[TransformResources] = None
    max_concurrent_transforms: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_payload_in_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transform_output: Optional[TransformOutput] = None
    environment: Optional[dict[str, str]] = None
    transform_input: Optional[TransformInput] = None
    batch_strategy: Optional[Union[str, BatchStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class TransformOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "assemble_with": "AssembleWith",
        "accept": "Accept",
        "kms_key_id": "KmsKeyId",
        "s3_output_path": "S3OutputPath",
    }

    assemble_with: Optional[Union[str, AssemblyType, Ref, GetAtt, Sub]] = None
    accept: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TransformResources(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_count": "InstanceCount",
        "volume_kms_key_id": "VolumeKmsKeyId",
        "instance_type": "InstanceType",
    }

    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, TransformInstanceType, Ref, GetAtt, Sub]] = None


@dataclass
class ValidationProfile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "profile_name": "ProfileName",
        "transform_job_definition": "TransformJobDefinition",
    }

    profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transform_job_definition: Optional[TransformJobDefinition] = None


@dataclass
class ValidationSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validation_role": "ValidationRole",
        "validation_profiles": "ValidationProfiles",
    }

    validation_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    validation_profiles: Optional[list[ValidationProfile]] = None

