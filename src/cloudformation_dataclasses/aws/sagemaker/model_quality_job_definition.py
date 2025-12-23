"""PropertyTypes for AWS::SageMaker::ModelQualityJobDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BatchTransformInput(PropertyType):
    DATASET_FORMAT = "DatasetFormat"
    S3_DATA_DISTRIBUTION_TYPE = "S3DataDistributionType"
    START_TIME_OFFSET = "StartTimeOffset"
    END_TIME_OFFSET = "EndTimeOffset"
    PROBABILITY_THRESHOLD_ATTRIBUTE = "ProbabilityThresholdAttribute"
    INFERENCE_ATTRIBUTE = "InferenceAttribute"
    DATA_CAPTURED_DESTINATION_S3_URI = "DataCapturedDestinationS3Uri"
    S3_INPUT_MODE = "S3InputMode"
    LOCAL_PATH = "LocalPath"
    PROBABILITY_ATTRIBUTE = "ProbabilityAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_format": "DatasetFormat",
        "s3_data_distribution_type": "S3DataDistributionType",
        "start_time_offset": "StartTimeOffset",
        "end_time_offset": "EndTimeOffset",
        "probability_threshold_attribute": "ProbabilityThresholdAttribute",
        "inference_attribute": "InferenceAttribute",
        "data_captured_destination_s3_uri": "DataCapturedDestinationS3Uri",
        "s3_input_mode": "S3InputMode",
        "local_path": "LocalPath",
        "probability_attribute": "ProbabilityAttribute",
    }

    dataset_format: Optional[DatasetFormat] = None
    s3_data_distribution_type: Optional[Union[str, ProcessingS3DataDistributionType, Ref, GetAtt, Sub]] = None
    start_time_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_time_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    probability_threshold_attribute: Optional[Union[float, Ref, GetAtt, Sub]] = None
    inference_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_captured_destination_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_input_mode: Optional[Union[str, ProcessingS3InputMode, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    probability_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterConfig(PropertyType):
    INSTANCE_COUNT = "InstanceCount"
    VOLUME_SIZE_IN_GB = "VolumeSizeInGB"
    VOLUME_KMS_KEY_ID = "VolumeKmsKeyId"
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_count": "InstanceCount",
        "volume_size_in_gb": "VolumeSizeInGB",
        "volume_kms_key_id": "VolumeKmsKeyId",
        "instance_type": "InstanceType",
    }

    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConstraintsResource(PropertyType):
    S3_URI = "S3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Csv(PropertyType):
    HEADER = "Header"

    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
    }

    header: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetFormat(PropertyType):
    PARQUET = "Parquet"
    CSV = "Csv"
    JSON = "Json"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parquet": "Parquet",
        "csv": "Csv",
        "json": "Json",
    }

    parquet: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    csv: Optional[Csv] = None
    json: Optional[Json] = None


@dataclass
class EndpointInput(PropertyType):
    S3_DATA_DISTRIBUTION_TYPE = "S3DataDistributionType"
    START_TIME_OFFSET = "StartTimeOffset"
    END_TIME_OFFSET = "EndTimeOffset"
    PROBABILITY_THRESHOLD_ATTRIBUTE = "ProbabilityThresholdAttribute"
    ENDPOINT_NAME = "EndpointName"
    INFERENCE_ATTRIBUTE = "InferenceAttribute"
    S3_INPUT_MODE = "S3InputMode"
    LOCAL_PATH = "LocalPath"
    PROBABILITY_ATTRIBUTE = "ProbabilityAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_distribution_type": "S3DataDistributionType",
        "start_time_offset": "StartTimeOffset",
        "end_time_offset": "EndTimeOffset",
        "probability_threshold_attribute": "ProbabilityThresholdAttribute",
        "endpoint_name": "EndpointName",
        "inference_attribute": "InferenceAttribute",
        "s3_input_mode": "S3InputMode",
        "local_path": "LocalPath",
        "probability_attribute": "ProbabilityAttribute",
    }

    s3_data_distribution_type: Optional[Union[str, ProcessingS3DataDistributionType, Ref, GetAtt, Sub]] = None
    start_time_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_time_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    probability_threshold_attribute: Optional[Union[float, Ref, GetAtt, Sub]] = None
    endpoint_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inference_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_input_mode: Optional[Union[str, ProcessingS3InputMode, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    probability_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Json(PropertyType):
    LINE = "Line"

    _property_mappings: ClassVar[dict[str, str]] = {
        "line": "Line",
    }

    line: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ModelQualityAppSpecification(PropertyType):
    CONTAINER_ENTRYPOINT = "ContainerEntrypoint"
    PROBLEM_TYPE = "ProblemType"
    POST_ANALYTICS_PROCESSOR_SOURCE_URI = "PostAnalyticsProcessorSourceUri"
    RECORD_PREPROCESSOR_SOURCE_URI = "RecordPreprocessorSourceUri"
    ENVIRONMENT = "Environment"
    IMAGE_URI = "ImageUri"
    CONTAINER_ARGUMENTS = "ContainerArguments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_entrypoint": "ContainerEntrypoint",
        "problem_type": "ProblemType",
        "post_analytics_processor_source_uri": "PostAnalyticsProcessorSourceUri",
        "record_preprocessor_source_uri": "RecordPreprocessorSourceUri",
        "environment": "Environment",
        "image_uri": "ImageUri",
        "container_arguments": "ContainerArguments",
    }

    container_entrypoint: Optional[Union[list[str], Ref]] = None
    problem_type: Optional[Union[str, MonitoringProblemType, Ref, GetAtt, Sub]] = None
    post_analytics_processor_source_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_preprocessor_source_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment: Optional[dict[str, str]] = None
    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_arguments: Optional[Union[list[str], Ref]] = None


@dataclass
class ModelQualityBaselineConfig(PropertyType):
    CONSTRAINTS_RESOURCE = "ConstraintsResource"
    BASELINING_JOB_NAME = "BaseliningJobName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constraints_resource": "ConstraintsResource",
        "baselining_job_name": "BaseliningJobName",
    }

    constraints_resource: Optional[ConstraintsResource] = None
    baselining_job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModelQualityJobInput(PropertyType):
    GROUND_TRUTH_S3_INPUT = "GroundTruthS3Input"
    BATCH_TRANSFORM_INPUT = "BatchTransformInput"
    ENDPOINT_INPUT = "EndpointInput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ground_truth_s3_input": "GroundTruthS3Input",
        "batch_transform_input": "BatchTransformInput",
        "endpoint_input": "EndpointInput",
    }

    ground_truth_s3_input: Optional[MonitoringGroundTruthS3Input] = None
    batch_transform_input: Optional[BatchTransformInput] = None
    endpoint_input: Optional[EndpointInput] = None


@dataclass
class MonitoringGroundTruthS3Input(PropertyType):
    S3_URI = "S3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringOutput(PropertyType):
    S3_OUTPUT = "S3Output"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_output": "S3Output",
    }

    s3_output: Optional[S3Output] = None


@dataclass
class MonitoringOutputConfig(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    MONITORING_OUTPUTS = "MonitoringOutputs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "monitoring_outputs": "MonitoringOutputs",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring_outputs: Optional[list[MonitoringOutput]] = None


@dataclass
class MonitoringResources(PropertyType):
    CLUSTER_CONFIG = "ClusterConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_config": "ClusterConfig",
    }

    cluster_config: Optional[ClusterConfig] = None


@dataclass
class NetworkConfig(PropertyType):
    ENABLE_NETWORK_ISOLATION = "EnableNetworkIsolation"
    ENABLE_INTER_CONTAINER_TRAFFIC_ENCRYPTION = "EnableInterContainerTrafficEncryption"
    VPC_CONFIG = "VpcConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_network_isolation": "EnableNetworkIsolation",
        "enable_inter_container_traffic_encryption": "EnableInterContainerTrafficEncryption",
        "vpc_config": "VpcConfig",
    }

    enable_network_isolation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_inter_container_traffic_encryption: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    vpc_config: Optional[VpcConfig] = None


@dataclass
class S3Output(PropertyType):
    S3_URI = "S3Uri"
    LOCAL_PATH = "LocalPath"
    S3_UPLOAD_MODE = "S3UploadMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "local_path": "LocalPath",
        "s3_upload_mode": "S3UploadMode",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_upload_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StoppingCondition(PropertyType):
    MAX_RUNTIME_IN_SECONDS = "MaxRuntimeInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_runtime_in_seconds": "MaxRuntimeInSeconds",
    }

    max_runtime_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    SUBNETS = "Subnets"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

