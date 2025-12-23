"""PropertyTypes for AWS::SageMaker::ModelPackage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalInferenceSpecificationDefinition(PropertyType):
    DESCRIPTION = "Description"
    SUPPORTED_CONTENT_TYPES = "SupportedContentTypes"
    SUPPORTED_REALTIME_INFERENCE_INSTANCE_TYPES = "SupportedRealtimeInferenceInstanceTypes"
    CONTAINERS = "Containers"
    SUPPORTED_TRANSFORM_INSTANCE_TYPES = "SupportedTransformInstanceTypes"
    NAME = "Name"
    SUPPORTED_RESPONSE_MIME_TYPES = "SupportedResponseMIMETypes"

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
    REPORT = "Report"
    PRE_TRAINING_REPORT = "PreTrainingReport"
    POST_TRAINING_REPORT = "PostTrainingReport"

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
    S3_DATA_SOURCE = "S3DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_source": "S3DataSource",
    }

    s3_data_source: Optional[S3DataSource] = None


@dataclass
class DriftCheckBaselines(PropertyType):
    MODEL_DATA_QUALITY = "ModelDataQuality"
    BIAS = "Bias"
    MODEL_QUALITY = "ModelQuality"
    EXPLAINABILITY = "Explainability"

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
    PRE_TRAINING_CONSTRAINTS = "PreTrainingConstraints"
    CONFIG_FILE = "ConfigFile"
    POST_TRAINING_CONSTRAINTS = "PostTrainingConstraints"

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
    CONSTRAINTS = "Constraints"
    CONFIG_FILE = "ConfigFile"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "config_file": "ConfigFile",
    }

    constraints: Optional[MetricsSource] = None
    config_file: Optional[FileSource] = None


@dataclass
class DriftCheckModelDataQuality(PropertyType):
    CONSTRAINTS = "Constraints"
    STATISTICS = "Statistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class DriftCheckModelQuality(PropertyType):
    CONSTRAINTS = "Constraints"
    STATISTICS = "Statistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class Explainability(PropertyType):
    REPORT = "Report"

    _property_mappings: ClassVar[dict[str, str]] = {
        "report": "Report",
    }

    report: Optional[MetricsSource] = None


@dataclass
class FileSource(PropertyType):
    CONTENT_TYPE = "ContentType"
    S3_URI = "S3Uri"
    CONTENT_DIGEST = "ContentDigest"

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
    SUPPORTED_CONTENT_TYPES = "SupportedContentTypes"
    SUPPORTED_REALTIME_INFERENCE_INSTANCE_TYPES = "SupportedRealtimeInferenceInstanceTypes"
    CONTAINERS = "Containers"
    SUPPORTED_TRANSFORM_INSTANCE_TYPES = "SupportedTransformInstanceTypes"
    SUPPORTED_RESPONSE_MIME_TYPES = "SupportedResponseMIMETypes"

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
    GENERATED_BY = "GeneratedBy"
    REPOSITORY = "Repository"
    COMMIT_ID = "CommitId"
    PROJECT_ID = "ProjectId"

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
    CONTENT_TYPE = "ContentType"
    S3_URI = "S3Uri"
    CONTENT_DIGEST = "ContentDigest"

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
    ACCEPT_EULA = "AcceptEula"

    _property_mappings: ClassVar[dict[str, str]] = {
        "accept_eula": "AcceptEula",
    }

    accept_eula: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ModelCard(PropertyType):
    MODEL_CARD_STATUS = "ModelCardStatus"
    MODEL_CARD_CONTENT = "ModelCardContent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_card_status": "ModelCardStatus",
        "model_card_content": "ModelCardContent",
    }

    model_card_status: Optional[Union[str, ModelCardStatus, Ref, GetAtt, Sub]] = None
    model_card_content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelDataQuality(PropertyType):
    CONSTRAINTS = "Constraints"
    STATISTICS = "Statistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class ModelDataSource(PropertyType):
    S3_DATA_SOURCE = "S3DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_source": "S3DataSource",
    }

    s3_data_source: Optional[S3ModelDataSource] = None


@dataclass
class ModelInput(PropertyType):
    DATA_INPUT_CONFIG = "DataInputConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_input_config": "DataInputConfig",
    }

    data_input_config: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelMetrics(PropertyType):
    MODEL_DATA_QUALITY = "ModelDataQuality"
    BIAS = "Bias"
    MODEL_QUALITY = "ModelQuality"
    EXPLAINABILITY = "Explainability"

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
    MODEL_INPUT = "ModelInput"
    NEAREST_MODEL_NAME = "NearestModelName"
    CONTAINER_HOSTNAME = "ContainerHostname"
    IMAGE_DIGEST = "ImageDigest"
    FRAMEWORK_VERSION = "FrameworkVersion"
    ENVIRONMENT = "Environment"
    MODEL_DATA_URL = "ModelDataUrl"
    IMAGE = "Image"
    MODEL_DATA_SOURCE = "ModelDataSource"
    FRAMEWORK = "Framework"

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
    VALIDATION_STATUSES = "ValidationStatuses"

    _property_mappings: ClassVar[dict[str, str]] = {
        "validation_statuses": "ValidationStatuses",
    }

    validation_statuses: Optional[list[ModelPackageStatusItem]] = None


@dataclass
class ModelPackageStatusItem(PropertyType):
    STATUS = "Status"
    FAILURE_REASON = "FailureReason"
    NAME = "Name"

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
    CONSTRAINTS = "Constraints"
    STATISTICS = "Statistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints": "Constraints",
        "statistics": "Statistics",
    }

    constraints: Optional[MetricsSource] = None
    statistics: Optional[MetricsSource] = None


@dataclass
class S3DataSource(PropertyType):
    S3_URI = "S3Uri"
    S3_DATA_TYPE = "S3DataType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "s3_data_type": "S3DataType",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_data_type: Optional[Union[str, S3DataType, Ref, GetAtt, Sub]] = None


@dataclass
class S3ModelDataSource(PropertyType):
    MODEL_ACCESS_CONFIG = "ModelAccessConfig"
    S3_DATA_TYPE = "S3DataType"
    COMPRESSION_TYPE = "CompressionType"
    S3_URI = "S3Uri"

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
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceAlgorithm(PropertyType):
    MODEL_DATA_URL = "ModelDataUrl"
    ALGORITHM_NAME = "AlgorithmName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_data_url": "ModelDataUrl",
        "algorithm_name": "AlgorithmName",
    }

    model_data_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    algorithm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceAlgorithmSpecification(PropertyType):
    SOURCE_ALGORITHMS = "SourceAlgorithms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_algorithms": "SourceAlgorithms",
    }

    source_algorithms: Optional[list[SourceAlgorithm]] = None


@dataclass
class TransformInput(PropertyType):
    CONTENT_TYPE = "ContentType"
    SPLIT_TYPE = "SplitType"
    COMPRESSION_TYPE = "CompressionType"
    DATA_SOURCE = "DataSource"

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
    TRANSFORM_RESOURCES = "TransformResources"
    MAX_CONCURRENT_TRANSFORMS = "MaxConcurrentTransforms"
    MAX_PAYLOAD_IN_MB = "MaxPayloadInMB"
    TRANSFORM_OUTPUT = "TransformOutput"
    ENVIRONMENT = "Environment"
    TRANSFORM_INPUT = "TransformInput"
    BATCH_STRATEGY = "BatchStrategy"

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
    ASSEMBLE_WITH = "AssembleWith"
    ACCEPT = "Accept"
    KMS_KEY_ID = "KmsKeyId"
    S3_OUTPUT_PATH = "S3OutputPath"

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
    INSTANCE_COUNT = "InstanceCount"
    VOLUME_KMS_KEY_ID = "VolumeKmsKeyId"
    INSTANCE_TYPE = "InstanceType"

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
    PROFILE_NAME = "ProfileName"
    TRANSFORM_JOB_DEFINITION = "TransformJobDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "profile_name": "ProfileName",
        "transform_job_definition": "TransformJobDefinition",
    }

    profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transform_job_definition: Optional[TransformJobDefinition] = None


@dataclass
class ValidationSpecification(PropertyType):
    VALIDATION_ROLE = "ValidationRole"
    VALIDATION_PROFILES = "ValidationProfiles"

    _property_mappings: ClassVar[dict[str, str]] = {
        "validation_role": "ValidationRole",
        "validation_profiles": "ValidationProfiles",
    }

    validation_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    validation_profiles: Optional[list[ValidationProfile]] = None

