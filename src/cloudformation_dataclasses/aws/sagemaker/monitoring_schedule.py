"""PropertyTypes for AWS::SageMaker::MonitoringSchedule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BaselineConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "statistics_resource": "StatisticsResource",
        "constraints_resource": "ConstraintsResource",
    }

    statistics_resource: Optional[StatisticsResource] = None
    constraints_resource: Optional[ConstraintsResource] = None


@dataclass
class BatchTransformInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_format": "DatasetFormat",
        "s3_data_distribution_type": "S3DataDistributionType",
        "data_captured_destination_s3_uri": "DataCapturedDestinationS3Uri",
        "s3_input_mode": "S3InputMode",
        "local_path": "LocalPath",
        "exclude_features_attribute": "ExcludeFeaturesAttribute",
    }

    dataset_format: Optional[DatasetFormat] = None
    s3_data_distribution_type: Optional[Union[str, ProcessingS3DataDistributionType, Ref, GetAtt, Sub]] = None
    data_captured_destination_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_input_mode: Optional[Union[str, ProcessingS3InputMode, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_features_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Csv(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
    }

    header: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetFormat(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_data_distribution_type": "S3DataDistributionType",
        "endpoint_name": "EndpointName",
        "s3_input_mode": "S3InputMode",
        "local_path": "LocalPath",
        "exclude_features_attribute": "ExcludeFeaturesAttribute",
    }

    s3_data_distribution_type: Optional[Union[str, ProcessingS3DataDistributionType, Ref, GetAtt, Sub]] = None
    endpoint_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_input_mode: Optional[Union[str, ProcessingS3InputMode, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_features_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Json(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line": "Line",
    }

    line: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringAppSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_entrypoint": "ContainerEntrypoint",
        "post_analytics_processor_source_uri": "PostAnalyticsProcessorSourceUri",
        "record_preprocessor_source_uri": "RecordPreprocessorSourceUri",
        "image_uri": "ImageUri",
        "container_arguments": "ContainerArguments",
    }

    container_entrypoint: Optional[Union[list[str], Ref]] = None
    post_analytics_processor_source_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_preprocessor_source_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_arguments: Optional[Union[list[str], Ref]] = None


@dataclass
class MonitoringExecutionSummary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scheduled_time": "ScheduledTime",
        "endpoint_name": "EndpointName",
        "monitoring_schedule_name": "MonitoringScheduleName",
        "processing_job_arn": "ProcessingJobArn",
        "failure_reason": "FailureReason",
        "creation_time": "CreationTime",
        "last_modified_time": "LastModifiedTime",
        "monitoring_execution_status": "MonitoringExecutionStatus",
    }

    scheduled_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring_schedule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    processing_job_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    failure_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_modified_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring_execution_status: Optional[Union[str, ExecutionStatus, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_transform_input": "BatchTransformInput",
        "endpoint_input": "EndpointInput",
    }

    batch_transform_input: Optional[BatchTransformInput] = None
    endpoint_input: Optional[EndpointInput] = None


@dataclass
class MonitoringJobDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "monitoring_inputs": "MonitoringInputs",
        "monitoring_resources": "MonitoringResources",
        "baseline_config": "BaselineConfig",
        "stopping_condition": "StoppingCondition",
        "monitoring_app_specification": "MonitoringAppSpecification",
        "network_config": "NetworkConfig",
        "environment": "Environment",
        "monitoring_output_config": "MonitoringOutputConfig",
        "role_arn": "RoleArn",
    }

    monitoring_inputs: Optional[list[MonitoringInput]] = None
    monitoring_resources: Optional[MonitoringResources] = None
    baseline_config: Optional[BaselineConfig] = None
    stopping_condition: Optional[StoppingCondition] = None
    monitoring_app_specification: Optional[MonitoringAppSpecification] = None
    network_config: Optional[NetworkConfig] = None
    environment: Optional[dict[str, str]] = None
    monitoring_output_config: Optional[MonitoringOutputConfig] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_output": "S3Output",
    }

    s3_output: Optional[S3Output] = None


@dataclass
class MonitoringOutputConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "monitoring_outputs": "MonitoringOutputs",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring_outputs: Optional[list[MonitoringOutput]] = None


@dataclass
class MonitoringResources(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_config": "ClusterConfig",
    }

    cluster_config: Optional[ClusterConfig] = None


@dataclass
class MonitoringScheduleConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_config": "ScheduleConfig",
        "monitoring_job_definition": "MonitoringJobDefinition",
        "monitoring_job_definition_name": "MonitoringJobDefinitionName",
        "monitoring_type": "MonitoringType",
    }

    schedule_config: Optional[ScheduleConfig] = None
    monitoring_job_definition: Optional[MonitoringJobDefinition] = None
    monitoring_job_definition_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    monitoring_type: Optional[Union[str, MonitoringType, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "local_path": "LocalPath",
        "s3_upload_mode": "S3UploadMode",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_upload_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduleConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
        "data_analysis_start_time": "DataAnalysisStartTime",
        "data_analysis_end_time": "DataAnalysisEndTime",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_analysis_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_analysis_end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StatisticsResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StoppingCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_runtime_in_seconds": "MaxRuntimeInSeconds",
    }

    max_runtime_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

