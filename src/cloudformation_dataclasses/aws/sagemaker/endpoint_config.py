"""PropertyTypes for AWS::SageMaker::EndpointConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AsyncInferenceClientConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_concurrent_invocations_per_instance": "MaxConcurrentInvocationsPerInstance",
    }

    max_concurrent_invocations_per_instance: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AsyncInferenceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_config": "OutputConfig",
        "client_config": "ClientConfig",
    }

    output_config: Optional[AsyncInferenceOutputConfig] = None
    client_config: Optional[AsyncInferenceClientConfig] = None


@dataclass
class AsyncInferenceNotificationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_inference_response_in": "IncludeInferenceResponseIn",
        "success_topic": "SuccessTopic",
        "error_topic": "ErrorTopic",
    }

    include_inference_response_in: Optional[Union[list[str], Ref]] = None
    success_topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_topic: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AsyncInferenceOutputConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "notification_config": "NotificationConfig",
        "s3_output_path": "S3OutputPath",
        "s3_failure_path": "S3FailurePath",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_config: Optional[AsyncInferenceNotificationConfig] = None
    s3_output_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_failure_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityReservationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_reservation_arn": "MlReservationArn",
        "capacity_reservation_preference": "CapacityReservationPreference",
    }

    ml_reservation_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capacity_reservation_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CaptureContentTypeHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "json_content_types": "JsonContentTypes",
        "csv_content_types": "CsvContentTypes",
    }

    json_content_types: Optional[Union[list[str], Ref]] = None
    csv_content_types: Optional[Union[list[str], Ref]] = None


@dataclass
class CaptureOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capture_mode": "CaptureMode",
    }

    capture_mode: Optional[Union[str, CaptureMode, Ref, GetAtt, Sub]] = None


@dataclass
class ClarifyExplainerConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_config": "InferenceConfig",
        "enable_explanations": "EnableExplanations",
        "shap_config": "ShapConfig",
    }

    inference_config: Optional[ClarifyInferenceConfig] = None
    enable_explanations: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shap_config: Optional[ClarifyShapConfig] = None


@dataclass
class ClarifyFeatureType(PropertyType):
    pass


@dataclass
class ClarifyHeader(PropertyType):
    pass


@dataclass
class ClarifyInferenceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_template": "ContentTemplate",
        "label_headers": "LabelHeaders",
        "max_payload_in_mb": "MaxPayloadInMB",
        "probability_index": "ProbabilityIndex",
        "label_attribute": "LabelAttribute",
        "feature_types": "FeatureTypes",
        "feature_headers": "FeatureHeaders",
        "label_index": "LabelIndex",
        "probability_attribute": "ProbabilityAttribute",
        "features_attribute": "FeaturesAttribute",
        "max_record_count": "MaxRecordCount",
    }

    content_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label_headers: Optional[list[ClarifyHeader]] = None
    max_payload_in_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    probability_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    label_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    feature_types: Optional[list[ClarifyFeatureType]] = None
    feature_headers: Optional[list[ClarifyHeader]] = None
    label_index: Optional[Union[int, Ref, GetAtt, Sub]] = None
    probability_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    features_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_record_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ClarifyShapBaselineConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "shap_baseline": "ShapBaseline",
        "shap_baseline_uri": "ShapBaselineUri",
        "mime_type": "MimeType",
    }

    shap_baseline: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shap_baseline_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mime_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClarifyShapConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_config": "TextConfig",
        "use_logit": "UseLogit",
        "seed": "Seed",
        "shap_baseline_config": "ShapBaselineConfig",
        "number_of_samples": "NumberOfSamples",
    }

    text_config: Optional[ClarifyTextConfig] = None
    use_logit: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    seed: Optional[Union[int, Ref, GetAtt, Sub]] = None
    shap_baseline_config: Optional[ClarifyShapBaselineConfig] = None
    number_of_samples: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ClarifyTextConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "language": "Language",
        "granularity": "Granularity",
    }

    language: Optional[Union[str, ClarifyTextLanguage, Ref, GetAtt, Sub]] = None
    granularity: Optional[Union[str, ClarifyTextGranularity, Ref, GetAtt, Sub]] = None


@dataclass
class DataCaptureConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capture_options": "CaptureOptions",
        "kms_key_id": "KmsKeyId",
        "destination_s3_uri": "DestinationS3Uri",
        "initial_sampling_percentage": "InitialSamplingPercentage",
        "capture_content_type_header": "CaptureContentTypeHeader",
        "enable_capture": "EnableCapture",
    }

    capture_options: Optional[list[CaptureOption]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    initial_sampling_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    capture_content_type_header: Optional[CaptureContentTypeHeader] = None
    enable_capture: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ExplainerConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "clarify_explainer_config": "ClarifyExplainerConfig",
    }

    clarify_explainer_config: Optional[ClarifyExplainerConfig] = None


@dataclass
class ManagedInstanceScaling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "max_instance_count": "MaxInstanceCount",
        "min_instance_count": "MinInstanceCount",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ProductionVariant(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_instance_scaling": "ManagedInstanceScaling",
        "model_name": "ModelName",
        "volume_size_in_gb": "VolumeSizeInGB",
        "enable_ssm_access": "EnableSSMAccess",
        "variant_name": "VariantName",
        "initial_instance_count": "InitialInstanceCount",
        "routing_config": "RoutingConfig",
        "initial_variant_weight": "InitialVariantWeight",
        "model_data_download_timeout_in_seconds": "ModelDataDownloadTimeoutInSeconds",
        "capacity_reservation_config": "CapacityReservationConfig",
        "inference_ami_version": "InferenceAmiVersion",
        "container_startup_health_check_timeout_in_seconds": "ContainerStartupHealthCheckTimeoutInSeconds",
        "serverless_config": "ServerlessConfig",
        "instance_type": "InstanceType",
    }

    managed_instance_scaling: Optional[ManagedInstanceScaling] = None
    model_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enable_ssm_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    variant_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    initial_instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    routing_config: Optional[RoutingConfig] = None
    initial_variant_weight: Optional[Union[float, Ref, GetAtt, Sub]] = None
    model_data_download_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    capacity_reservation_config: Optional[CapacityReservationConfig] = None
    inference_ami_version: Optional[Union[str, ProductionVariantInferenceAmiVersion, Ref, GetAtt, Sub]] = None
    container_startup_health_check_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    serverless_config: Optional[ServerlessConfig] = None
    instance_type: Optional[Union[str, ProductionVariantInstanceType, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "routing_strategy": "RoutingStrategy",
    }

    routing_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerlessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_concurrency": "MaxConcurrency",
        "memory_size_in_mb": "MemorySizeInMB",
        "provisioned_concurrency": "ProvisionedConcurrency",
    }

    max_concurrency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    memory_size_in_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    provisioned_concurrency: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

