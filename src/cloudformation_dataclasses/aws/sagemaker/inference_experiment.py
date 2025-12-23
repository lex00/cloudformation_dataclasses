"""PropertyTypes for AWS::SageMaker::InferenceExperiment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CaptureContentTypeHeader(PropertyType):
    JSON_CONTENT_TYPES = "JsonContentTypes"
    CSV_CONTENT_TYPES = "CsvContentTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json_content_types": "JsonContentTypes",
        "csv_content_types": "CsvContentTypes",
    }

    json_content_types: Optional[Union[list[str], Ref]] = None
    csv_content_types: Optional[Union[list[str], Ref]] = None


@dataclass
class DataStorageConfig(PropertyType):
    DESTINATION = "Destination"
    CONTENT_TYPE = "ContentType"
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "content_type": "ContentType",
        "kms_key": "KmsKey",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_type: Optional[CaptureContentTypeHeader] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EndpointMetadata(PropertyType):
    ENDPOINT_STATUS = "EndpointStatus"
    ENDPOINT_NAME = "EndpointName"
    ENDPOINT_CONFIG_NAME = "EndpointConfigName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_status": "EndpointStatus",
        "endpoint_name": "EndpointName",
        "endpoint_config_name": "EndpointConfigName",
    }

    endpoint_status: Optional[Union[str, EndpointStatus, Ref, GetAtt, Sub]] = None
    endpoint_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_config_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceExperimentSchedule(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelInfrastructureConfig(PropertyType):
    INFRASTRUCTURE_TYPE = "InfrastructureType"
    REAL_TIME_INFERENCE_CONFIG = "RealTimeInferenceConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "infrastructure_type": "InfrastructureType",
        "real_time_inference_config": "RealTimeInferenceConfig",
    }

    infrastructure_type: Optional[Union[str, ModelInfrastructureType, Ref, GetAtt, Sub]] = None
    real_time_inference_config: Optional[RealTimeInferenceConfig] = None


@dataclass
class ModelVariantConfig(PropertyType):
    MODEL_NAME = "ModelName"
    VARIANT_NAME = "VariantName"
    INFRASTRUCTURE_CONFIG = "InfrastructureConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_name": "ModelName",
        "variant_name": "VariantName",
        "infrastructure_config": "InfrastructureConfig",
    }

    model_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variant_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    infrastructure_config: Optional[ModelInfrastructureConfig] = None


@dataclass
class RealTimeInferenceConfig(PropertyType):
    INSTANCE_COUNT = "InstanceCount"
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_count": "InstanceCount",
        "instance_type": "InstanceType",
    }

    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, InstanceType, Ref, GetAtt, Sub]] = None


@dataclass
class ShadowModeConfig(PropertyType):
    SOURCE_MODEL_VARIANT_NAME = "SourceModelVariantName"
    SHADOW_MODEL_VARIANTS = "ShadowModelVariants"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_model_variant_name": "SourceModelVariantName",
        "shadow_model_variants": "ShadowModelVariants",
    }

    source_model_variant_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shadow_model_variants: Optional[list[ShadowModelVariantConfig]] = None


@dataclass
class ShadowModelVariantConfig(PropertyType):
    SHADOW_MODEL_VARIANT_NAME = "ShadowModelVariantName"
    SAMPLING_PERCENTAGE = "SamplingPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "shadow_model_variant_name": "ShadowModelVariantName",
        "sampling_percentage": "SamplingPercentage",
    }

    shadow_model_variant_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sampling_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None

