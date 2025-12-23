"""PropertyTypes for AWS::SageMaker::ProcessingJob."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppSpecification(PropertyType):
    CONTAINER_ENTRYPOINT = "ContainerEntrypoint"
    IMAGE_URI = "ImageUri"
    CONTAINER_ARGUMENTS = "ContainerArguments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_entrypoint": "ContainerEntrypoint",
        "image_uri": "ImageUri",
        "container_arguments": "ContainerArguments",
    }

    container_entrypoint: Optional[Union[list[str], Ref]] = None
    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_arguments: Optional[Union[list[str], Ref]] = None


@dataclass
class AthenaDatasetDefinition(PropertyType):
    WORK_GROUP = "WorkGroup"
    OUTPUT_S3_URI = "OutputS3Uri"
    KMS_KEY_ID = "KmsKeyId"
    QUERY_STRING = "QueryString"
    DATABASE = "Database"
    OUTPUT_FORMAT = "OutputFormat"
    OUTPUT_COMPRESSION = "OutputCompression"
    CATALOG = "Catalog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "work_group": "WorkGroup",
        "output_s3_uri": "OutputS3Uri",
        "kms_key_id": "KmsKeyId",
        "query_string": "QueryString",
        "database": "Database",
        "output_format": "OutputFormat",
        "output_compression": "OutputCompression",
        "catalog": "Catalog",
    }

    work_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_format: Optional[Union[str, AthenaResultFormat, Ref, GetAtt, Sub]] = None
    output_compression: Optional[Union[str, AthenaResultCompressionType, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class DatasetDefinition(PropertyType):
    INPUT_MODE = "InputMode"
    REDSHIFT_DATASET_DEFINITION = "RedshiftDatasetDefinition"
    ATHENA_DATASET_DEFINITION = "AthenaDatasetDefinition"
    LOCAL_PATH = "LocalPath"
    DATA_DISTRIBUTION_TYPE = "DataDistributionType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_mode": "InputMode",
        "redshift_dataset_definition": "RedshiftDatasetDefinition",
        "athena_dataset_definition": "AthenaDatasetDefinition",
        "local_path": "LocalPath",
        "data_distribution_type": "DataDistributionType",
    }

    input_mode: Optional[Union[str, InputMode, Ref, GetAtt, Sub]] = None
    redshift_dataset_definition: Optional[RedshiftDatasetDefinition] = None
    athena_dataset_definition: Optional[AthenaDatasetDefinition] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_distribution_type: Optional[Union[str, DataDistributionType, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentConfig(PropertyType):
    TRIAL_NAME = "TrialName"
    EXPERIMENT_NAME = "ExperimentName"
    TRIAL_COMPONENT_DISPLAY_NAME = "TrialComponentDisplayName"
    RUN_NAME = "RunName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "trial_name": "TrialName",
        "experiment_name": "ExperimentName",
        "trial_component_display_name": "TrialComponentDisplayName",
        "run_name": "RunName",
    }

    trial_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    experiment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trial_component_display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    run_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FeatureStoreOutput(PropertyType):
    FEATURE_GROUP_NAME = "FeatureGroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "feature_group_name": "FeatureGroupName",
    }

    feature_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class ProcessingInputsObject(PropertyType):
    APP_MANAGED = "AppManaged"
    INPUT_NAME = "InputName"
    DATASET_DEFINITION = "DatasetDefinition"
    S3_INPUT = "S3Input"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_managed": "AppManaged",
        "input_name": "InputName",
        "dataset_definition": "DatasetDefinition",
        "s3_input": "S3Input",
    }

    app_managed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataset_definition: Optional[DatasetDefinition] = None
    s3_input: Optional[S3Input] = None


@dataclass
class ProcessingOutputConfig(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    OUTPUTS = "Outputs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "outputs": "Outputs",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    outputs: Optional[list[ProcessingOutputsObject]] = None


@dataclass
class ProcessingOutputsObject(PropertyType):
    S3_OUTPUT = "S3Output"
    APP_MANAGED = "AppManaged"
    FEATURE_STORE_OUTPUT = "FeatureStoreOutput"
    OUTPUT_NAME = "OutputName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_output": "S3Output",
        "app_managed": "AppManaged",
        "feature_store_output": "FeatureStoreOutput",
        "output_name": "OutputName",
    }

    s3_output: Optional[S3Output] = None
    app_managed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    feature_store_output: Optional[FeatureStoreOutput] = None
    output_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProcessingResources(PropertyType):
    CLUSTER_CONFIG = "ClusterConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_config": "ClusterConfig",
    }

    cluster_config: Optional[ClusterConfig] = None


@dataclass
class RedshiftDatasetDefinition(PropertyType):
    OUTPUT_S3_URI = "OutputS3Uri"
    KMS_KEY_ID = "KmsKeyId"
    CLUSTER_ID = "ClusterId"
    QUERY_STRING = "QueryString"
    DATABASE = "Database"
    OUTPUT_FORMAT = "OutputFormat"
    OUTPUT_COMPRESSION = "OutputCompression"
    CLUSTER_ROLE_ARN = "ClusterRoleArn"
    DB_USER = "DbUser"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_s3_uri": "OutputS3Uri",
        "kms_key_id": "KmsKeyId",
        "cluster_id": "ClusterId",
        "query_string": "QueryString",
        "database": "Database",
        "output_format": "OutputFormat",
        "output_compression": "OutputCompression",
        "cluster_role_arn": "ClusterRoleArn",
        "db_user": "DbUser",
    }

    output_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cluster_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_format: Optional[Union[str, RedshiftResultFormat, Ref, GetAtt, Sub]] = None
    output_compression: Optional[Union[str, RedshiftResultCompressionType, Ref, GetAtt, Sub]] = None
    cluster_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_user: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Input(PropertyType):
    S3_COMPRESSION_TYPE = "S3CompressionType"
    S3_DATA_DISTRIBUTION_TYPE = "S3DataDistributionType"
    S3_URI = "S3Uri"
    S3_INPUT_MODE = "S3InputMode"
    LOCAL_PATH = "LocalPath"
    S3_DATA_TYPE = "S3DataType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_compression_type": "S3CompressionType",
        "s3_data_distribution_type": "S3DataDistributionType",
        "s3_uri": "S3Uri",
        "s3_input_mode": "S3InputMode",
        "local_path": "LocalPath",
        "s3_data_type": "S3DataType",
    }

    s3_compression_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_data_distribution_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_input_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

