"""PropertyTypes for AWS::Pipes::Pipe."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BatchJobDependencyType:
    """BatchJobDependencyType enum values."""

    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


class BatchResourceRequirementType:
    """BatchResourceRequirementType enum values."""

    GPU = "GPU"
    MEMORY = "MEMORY"
    VCPU = "VCPU"


class DimensionValueType:
    """DimensionValueType enum values."""

    VARCHAR = "VARCHAR"


class DynamoDBStreamStartPosition:
    """DynamoDBStreamStartPosition enum values."""

    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class EcsEnvironmentFileType:
    """EcsEnvironmentFileType enum values."""

    S3 = "s3"


class EcsResourceRequirementType:
    """EcsResourceRequirementType enum values."""

    GPU = "GPU"
    INFERENCEACCELERATOR = "InferenceAccelerator"


class EpochTimeUnit:
    """EpochTimeUnit enum values."""

    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MICROSECONDS = "MICROSECONDS"
    NANOSECONDS = "NANOSECONDS"


class IncludeExecutionDataOption:
    """IncludeExecutionDataOption enum values."""

    ALL = "ALL"


class KinesisStreamStartPosition:
    """KinesisStreamStartPosition enum values."""

    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


class LaunchType:
    """LaunchType enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class LogLevel:
    """LogLevel enum values."""

    OFF = "OFF"
    ERROR = "ERROR"
    INFO = "INFO"
    TRACE = "TRACE"


class MSKStartPosition:
    """MSKStartPosition enum values."""

    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class MeasureValueType:
    """MeasureValueType enum values."""

    DOUBLE = "DOUBLE"
    BIGINT = "BIGINT"
    VARCHAR = "VARCHAR"
    BOOLEAN = "BOOLEAN"
    TIMESTAMP = "TIMESTAMP"


class OnPartialBatchItemFailureStreams:
    """OnPartialBatchItemFailureStreams enum values."""

    AUTOMATIC_BISECT = "AUTOMATIC_BISECT"


class PipeState:
    """PipeState enum values."""

    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    START_FAILED = "START_FAILED"
    STOP_FAILED = "STOP_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    CREATE_ROLLBACK_FAILED = "CREATE_ROLLBACK_FAILED"
    DELETE_ROLLBACK_FAILED = "DELETE_ROLLBACK_FAILED"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"


class PipeTargetInvocationType:
    """PipeTargetInvocationType enum values."""

    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    FIRE_AND_FORGET = "FIRE_AND_FORGET"


class PlacementConstraintType:
    """PlacementConstraintType enum values."""

    DISTINCTINSTANCE = "distinctInstance"
    MEMBEROF = "memberOf"


class PlacementStrategyType:
    """PlacementStrategyType enum values."""

    RANDOM = "random"
    SPREAD = "spread"
    BINPACK = "binpack"


class PropagateTags:
    """PropagateTags enum values."""

    TASK_DEFINITION = "TASK_DEFINITION"


class RequestedPipeState:
    """RequestedPipeState enum values."""

    RUNNING = "RUNNING"
    STOPPED = "STOPPED"


class RequestedPipeStateDescribeResponse:
    """RequestedPipeStateDescribeResponse enum values."""

    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    DELETED = "DELETED"


class S3OutputFormat:
    """S3OutputFormat enum values."""

    JSON = "json"
    PLAIN = "plain"
    W3C = "w3c"


class SelfManagedKafkaStartPosition:
    """SelfManagedKafkaStartPosition enum values."""

    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class TimeFieldType:
    """TimeFieldType enum values."""

    EPOCH = "EPOCH"
    TIMESTAMP_FORMAT = "TIMESTAMP_FORMAT"


@dataclass
class AwsVpcConfiguration(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"
    ASSIGN_PUBLIC_IP = "AssignPublicIp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
        "assign_public_ip": "AssignPublicIp",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None
    assign_public_ip: Optional[Union[str, AssignPublicIp, Ref, GetAtt, Sub]] = None


@dataclass
class BatchArrayProperties(PropertyType):
    SIZE = "Size"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size": "Size",
    }

    size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BatchContainerOverrides(PropertyType):
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    INSTANCE_TYPE = "InstanceType"
    RESOURCE_REQUIREMENTS = "ResourceRequirements"

    _property_mappings: ClassVar[dict[str, str]] = {
        "command": "Command",
        "environment": "Environment",
        "instance_type": "InstanceType",
        "resource_requirements": "ResourceRequirements",
    }

    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[BatchEnvironmentVariable]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_requirements: Optional[list[BatchResourceRequirement]] = None


@dataclass
class BatchEnvironmentVariable(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BatchJobDependency(PropertyType):
    TYPE = "Type"
    JOB_ID = "JobId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "job_id": "JobId",
    }

    type_: Optional[Union[str, BatchJobDependencyType, Ref, GetAtt, Sub]] = None
    job_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BatchResourceRequirement(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, BatchResourceRequirementType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BatchRetryStrategy(PropertyType):
    ATTEMPTS = "Attempts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attempts": "Attempts",
    }

    attempts: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    CAPACITY_PROVIDER = "CapacityProvider"
    WEIGHT = "Weight"
    BASE = "Base"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "weight": "Weight",
        "base": "Base",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CloudwatchLogsLogDestination(PropertyType):
    LOG_GROUP_ARN = "LogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeadLetterConfig(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DimensionMapping(PropertyType):
    DIMENSION_VALUE_TYPE = "DimensionValueType"
    DIMENSION_VALUE = "DimensionValue"
    DIMENSION_NAME = "DimensionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_value_type": "DimensionValueType",
        "dimension_value": "DimensionValue",
        "dimension_name": "DimensionName",
    }

    dimension_value_type: Optional[Union[str, DimensionValueType, Ref, GetAtt, Sub]] = None
    dimension_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsContainerOverride(PropertyType):
    MEMORY_RESERVATION = "MemoryReservation"
    COMMAND = "Command"
    MEMORY = "Memory"
    CPU = "Cpu"
    ENVIRONMENT = "Environment"
    RESOURCE_REQUIREMENTS = "ResourceRequirements"
    ENVIRONMENT_FILES = "EnvironmentFiles"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_reservation": "MemoryReservation",
        "command": "Command",
        "memory": "Memory",
        "cpu": "Cpu",
        "environment": "Environment",
        "resource_requirements": "ResourceRequirements",
        "environment_files": "EnvironmentFiles",
        "name": "Name",
    }

    memory_reservation: Optional[Union[int, Ref, GetAtt, Sub]] = None
    command: Optional[Union[list[str], Ref]] = None
    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[int, Ref, GetAtt, Sub]] = None
    environment: Optional[list[EcsEnvironmentVariable]] = None
    resource_requirements: Optional[list[EcsResourceRequirement]] = None
    environment_files: Optional[list[EcsEnvironmentFile]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsEnvironmentFile(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsEnvironmentVariable(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsEphemeralStorage(PropertyType):
    SIZE_IN_GI_B = "SizeInGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gi_b": "SizeInGiB",
    }

    size_in_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EcsInferenceAcceleratorOverride(PropertyType):
    DEVICE_TYPE = "DeviceType"
    DEVICE_NAME = "DeviceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "device_type": "DeviceType",
        "device_name": "DeviceName",
    }

    device_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsResourceRequirement(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsTaskOverride(PropertyType):
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    TASK_ROLE_ARN = "TaskRoleArn"
    MEMORY = "Memory"
    CPU = "Cpu"
    INFERENCE_ACCELERATOR_OVERRIDES = "InferenceAcceleratorOverrides"
    EPHEMERAL_STORAGE = "EphemeralStorage"
    CONTAINER_OVERRIDES = "ContainerOverrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role_arn": "ExecutionRoleArn",
        "task_role_arn": "TaskRoleArn",
        "memory": "Memory",
        "cpu": "Cpu",
        "inference_accelerator_overrides": "InferenceAcceleratorOverrides",
        "ephemeral_storage": "EphemeralStorage",
        "container_overrides": "ContainerOverrides",
    }

    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inference_accelerator_overrides: Optional[list[EcsInferenceAcceleratorOverride]] = None
    ephemeral_storage: Optional[EcsEphemeralStorage] = None
    container_overrides: Optional[list[EcsContainerOverride]] = None


@dataclass
class Filter(PropertyType):
    PATTERN = "Pattern"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterCriteria(PropertyType):
    FILTERS = "Filters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
    }

    filters: Optional[list[Filter]] = None


@dataclass
class FirehoseLogDestination(PropertyType):
    DELIVERY_STREAM_ARN = "DeliveryStreamArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_arn": "DeliveryStreamArn",
    }

    delivery_stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MQBrokerAccessCredentials(PropertyType):
    BASIC_AUTH = "BasicAuth"

    _property_mappings: ClassVar[dict[str, str]] = {
        "basic_auth": "BasicAuth",
    }

    basic_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MSKAccessCredentials(PropertyType):
    CLIENT_CERTIFICATE_TLS_AUTH = "ClientCertificateTlsAuth"
    SASL_SCRAM512_AUTH = "SaslScram512Auth"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_certificate_tls_auth": "ClientCertificateTlsAuth",
        "sasl_scram512_auth": "SaslScram512Auth",
    }

    client_certificate_tls_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sasl_scram512_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiMeasureAttributeMapping(PropertyType):
    MULTI_MEASURE_ATTRIBUTE_NAME = "MultiMeasureAttributeName"
    MEASURE_VALUE_TYPE = "MeasureValueType"
    MEASURE_VALUE = "MeasureValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_measure_attribute_name": "MultiMeasureAttributeName",
        "measure_value_type": "MeasureValueType",
        "measure_value": "MeasureValue",
    }

    multi_measure_attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure_value_type: Optional[Union[str, MeasureValueType, Ref, GetAtt, Sub]] = None
    measure_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiMeasureMapping(PropertyType):
    MULTI_MEASURE_NAME = "MultiMeasureName"
    MULTI_MEASURE_ATTRIBUTE_MAPPINGS = "MultiMeasureAttributeMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_measure_name": "MultiMeasureName",
        "multi_measure_attribute_mappings": "MultiMeasureAttributeMappings",
    }

    multi_measure_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multi_measure_attribute_mappings: Optional[list[MultiMeasureAttributeMapping]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    AWSVPC_CONFIGURATION = "AwsvpcConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "awsvpc_configuration": "AwsvpcConfiguration",
    }

    awsvpc_configuration: Optional[AwsVpcConfiguration] = None


@dataclass
class PipeEnrichmentHttpParameters(PropertyType):
    PATH_PARAMETER_VALUES = "PathParameterValues"
    HEADER_PARAMETERS = "HeaderParameters"
    QUERY_STRING_PARAMETERS = "QueryStringParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path_parameter_values": "PathParameterValues",
        "header_parameters": "HeaderParameters",
        "query_string_parameters": "QueryStringParameters",
    }

    path_parameter_values: Optional[Union[list[str], Ref]] = None
    header_parameters: Optional[dict[str, str]] = None
    query_string_parameters: Optional[dict[str, str]] = None


@dataclass
class PipeEnrichmentParameters(PropertyType):
    HTTP_PARAMETERS = "HttpParameters"
    INPUT_TEMPLATE = "InputTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_parameters": "HttpParameters",
        "input_template": "InputTemplate",
    }

    http_parameters: Optional[PipeEnrichmentHttpParameters] = None
    input_template: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipeLogConfiguration(PropertyType):
    FIREHOSE_LOG_DESTINATION = "FirehoseLogDestination"
    CLOUDWATCH_LOGS_LOG_DESTINATION = "CloudwatchLogsLogDestination"
    INCLUDE_EXECUTION_DATA = "IncludeExecutionData"
    S3_LOG_DESTINATION = "S3LogDestination"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "firehose_log_destination": "FirehoseLogDestination",
        "cloudwatch_logs_log_destination": "CloudwatchLogsLogDestination",
        "include_execution_data": "IncludeExecutionData",
        "s3_log_destination": "S3LogDestination",
        "level": "Level",
    }

    firehose_log_destination: Optional[FirehoseLogDestination] = None
    cloudwatch_logs_log_destination: Optional[CloudwatchLogsLogDestination] = None
    include_execution_data: Optional[Union[list[str], Ref]] = None
    s3_log_destination: Optional[S3LogDestination] = None
    level: Optional[Union[str, LogLevel, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceActiveMQBrokerParameters(PropertyType):
    BATCH_SIZE = "BatchSize"
    QUEUE_NAME = "QueueName"
    CREDENTIALS = "Credentials"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_size": "BatchSize",
        "queue_name": "QueueName",
        "credentials": "Credentials",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    queue_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials: Optional[MQBrokerAccessCredentials] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceDynamoDBStreamParameters(PropertyType):
    STARTING_POSITION = "StartingPosition"
    BATCH_SIZE = "BatchSize"
    MAXIMUM_RETRY_ATTEMPTS = "MaximumRetryAttempts"
    ON_PARTIAL_BATCH_ITEM_FAILURE = "OnPartialBatchItemFailure"
    DEAD_LETTER_CONFIG = "DeadLetterConfig"
    PARALLELIZATION_FACTOR = "ParallelizationFactor"
    MAXIMUM_RECORD_AGE_IN_SECONDS = "MaximumRecordAgeInSeconds"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "starting_position": "StartingPosition",
        "batch_size": "BatchSize",
        "maximum_retry_attempts": "MaximumRetryAttempts",
        "on_partial_batch_item_failure": "OnPartialBatchItemFailure",
        "dead_letter_config": "DeadLetterConfig",
        "parallelization_factor": "ParallelizationFactor",
        "maximum_record_age_in_seconds": "MaximumRecordAgeInSeconds",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    starting_position: Optional[Union[str, DynamoDBStreamStartPosition, Ref, GetAtt, Sub]] = None
    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_retry_attempts: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_partial_batch_item_failure: Optional[Union[str, OnPartialBatchItemFailureStreams, Ref, GetAtt, Sub]] = None
    dead_letter_config: Optional[DeadLetterConfig] = None
    parallelization_factor: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_record_age_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceKinesisStreamParameters(PropertyType):
    STARTING_POSITION = "StartingPosition"
    BATCH_SIZE = "BatchSize"
    MAXIMUM_RETRY_ATTEMPTS = "MaximumRetryAttempts"
    ON_PARTIAL_BATCH_ITEM_FAILURE = "OnPartialBatchItemFailure"
    DEAD_LETTER_CONFIG = "DeadLetterConfig"
    PARALLELIZATION_FACTOR = "ParallelizationFactor"
    MAXIMUM_RECORD_AGE_IN_SECONDS = "MaximumRecordAgeInSeconds"
    STARTING_POSITION_TIMESTAMP = "StartingPositionTimestamp"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "starting_position": "StartingPosition",
        "batch_size": "BatchSize",
        "maximum_retry_attempts": "MaximumRetryAttempts",
        "on_partial_batch_item_failure": "OnPartialBatchItemFailure",
        "dead_letter_config": "DeadLetterConfig",
        "parallelization_factor": "ParallelizationFactor",
        "maximum_record_age_in_seconds": "MaximumRecordAgeInSeconds",
        "starting_position_timestamp": "StartingPositionTimestamp",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    starting_position: Optional[Union[str, KinesisStreamStartPosition, Ref, GetAtt, Sub]] = None
    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_retry_attempts: Optional[Union[int, Ref, GetAtt, Sub]] = None
    on_partial_batch_item_failure: Optional[Union[str, OnPartialBatchItemFailureStreams, Ref, GetAtt, Sub]] = None
    dead_letter_config: Optional[DeadLetterConfig] = None
    parallelization_factor: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_record_age_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    starting_position_timestamp: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceManagedStreamingKafkaParameters(PropertyType):
    STARTING_POSITION = "StartingPosition"
    BATCH_SIZE = "BatchSize"
    CONSUMER_GROUP_ID = "ConsumerGroupID"
    CREDENTIALS = "Credentials"
    TOPIC_NAME = "TopicName"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "starting_position": "StartingPosition",
        "batch_size": "BatchSize",
        "consumer_group_id": "ConsumerGroupID",
        "credentials": "Credentials",
        "topic_name": "TopicName",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    starting_position: Optional[Union[str, MSKStartPosition, Ref, GetAtt, Sub]] = None
    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    consumer_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials: Optional[MSKAccessCredentials] = None
    topic_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceParameters(PropertyType):
    MANAGED_STREAMING_KAFKA_PARAMETERS = "ManagedStreamingKafkaParameters"
    DYNAMO_DB_STREAM_PARAMETERS = "DynamoDBStreamParameters"
    SELF_MANAGED_KAFKA_PARAMETERS = "SelfManagedKafkaParameters"
    RABBIT_MQ_BROKER_PARAMETERS = "RabbitMQBrokerParameters"
    SQS_QUEUE_PARAMETERS = "SqsQueueParameters"
    KINESIS_STREAM_PARAMETERS = "KinesisStreamParameters"
    FILTER_CRITERIA = "FilterCriteria"
    ACTIVE_MQ_BROKER_PARAMETERS = "ActiveMQBrokerParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_streaming_kafka_parameters": "ManagedStreamingKafkaParameters",
        "dynamo_db_stream_parameters": "DynamoDBStreamParameters",
        "self_managed_kafka_parameters": "SelfManagedKafkaParameters",
        "rabbit_mq_broker_parameters": "RabbitMQBrokerParameters",
        "sqs_queue_parameters": "SqsQueueParameters",
        "kinesis_stream_parameters": "KinesisStreamParameters",
        "filter_criteria": "FilterCriteria",
        "active_mq_broker_parameters": "ActiveMQBrokerParameters",
    }

    managed_streaming_kafka_parameters: Optional[PipeSourceManagedStreamingKafkaParameters] = None
    dynamo_db_stream_parameters: Optional[PipeSourceDynamoDBStreamParameters] = None
    self_managed_kafka_parameters: Optional[PipeSourceSelfManagedKafkaParameters] = None
    rabbit_mq_broker_parameters: Optional[PipeSourceRabbitMQBrokerParameters] = None
    sqs_queue_parameters: Optional[PipeSourceSqsQueueParameters] = None
    kinesis_stream_parameters: Optional[PipeSourceKinesisStreamParameters] = None
    filter_criteria: Optional[FilterCriteria] = None
    active_mq_broker_parameters: Optional[PipeSourceActiveMQBrokerParameters] = None


@dataclass
class PipeSourceRabbitMQBrokerParameters(PropertyType):
    BATCH_SIZE = "BatchSize"
    VIRTUAL_HOST = "VirtualHost"
    QUEUE_NAME = "QueueName"
    CREDENTIALS = "Credentials"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_size": "BatchSize",
        "virtual_host": "VirtualHost",
        "queue_name": "QueueName",
        "credentials": "Credentials",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    virtual_host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    queue_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials: Optional[MQBrokerAccessCredentials] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceSelfManagedKafkaParameters(PropertyType):
    STARTING_POSITION = "StartingPosition"
    BATCH_SIZE = "BatchSize"
    CONSUMER_GROUP_ID = "ConsumerGroupID"
    ADDITIONAL_BOOTSTRAP_SERVERS = "AdditionalBootstrapServers"
    VPC = "Vpc"
    CREDENTIALS = "Credentials"
    SERVER_ROOT_CA_CERTIFICATE = "ServerRootCaCertificate"
    TOPIC_NAME = "TopicName"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "starting_position": "StartingPosition",
        "batch_size": "BatchSize",
        "consumer_group_id": "ConsumerGroupID",
        "additional_bootstrap_servers": "AdditionalBootstrapServers",
        "vpc": "Vpc",
        "credentials": "Credentials",
        "server_root_ca_certificate": "ServerRootCaCertificate",
        "topic_name": "TopicName",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    starting_position: Optional[Union[str, SelfManagedKafkaStartPosition, Ref, GetAtt, Sub]] = None
    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    consumer_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_bootstrap_servers: Optional[Union[list[str], Ref]] = None
    vpc: Optional[SelfManagedKafkaAccessConfigurationVpc] = None
    credentials: Optional[SelfManagedKafkaAccessConfigurationCredentials] = None
    server_root_ca_certificate: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeSourceSqsQueueParameters(PropertyType):
    BATCH_SIZE = "BatchSize"
    MAXIMUM_BATCHING_WINDOW_IN_SECONDS = "MaximumBatchingWindowInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_size": "BatchSize",
        "maximum_batching_window_in_seconds": "MaximumBatchingWindowInSeconds",
    }

    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_batching_window_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetBatchJobParameters(PropertyType):
    DEPENDS_ON = "DependsOn"
    PARAMETERS = "Parameters"
    ARRAY_PROPERTIES = "ArrayProperties"
    JOB_NAME = "JobName"
    RETRY_STRATEGY = "RetryStrategy"
    JOB_DEFINITION = "JobDefinition"
    CONTAINER_OVERRIDES = "ContainerOverrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "depends_on": "DependsOn",
        "parameters": "Parameters",
        "array_properties": "ArrayProperties",
        "job_name": "JobName",
        "retry_strategy": "RetryStrategy",
        "job_definition": "JobDefinition",
        "container_overrides": "ContainerOverrides",
    }

    depends_on: Optional[list[BatchJobDependency]] = None
    parameters: Optional[dict[str, str]] = None
    array_properties: Optional[BatchArrayProperties] = None
    job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retry_strategy: Optional[BatchRetryStrategy] = None
    job_definition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_overrides: Optional[BatchContainerOverrides] = None


@dataclass
class PipeTargetCloudWatchLogsParameters(PropertyType):
    LOG_STREAM_NAME = "LogStreamName"
    TIMESTAMP = "Timestamp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_name": "LogStreamName",
        "timestamp": "Timestamp",
    }

    log_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetEcsTaskParameters(PropertyType):
    PLATFORM_VERSION = "PlatformVersion"
    GROUP = "Group"
    ENABLE_ECS_MANAGED_TAGS = "EnableECSManagedTags"
    TASK_COUNT = "TaskCount"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    PLACEMENT_CONSTRAINTS = "PlacementConstraints"
    PROPAGATE_TAGS = "PropagateTags"
    PLACEMENT_STRATEGY = "PlacementStrategy"
    LAUNCH_TYPE = "LaunchType"
    CAPACITY_PROVIDER_STRATEGY = "CapacityProviderStrategy"
    REFERENCE_ID = "ReferenceId"
    OVERRIDES = "Overrides"
    NETWORK_CONFIGURATION = "NetworkConfiguration"
    TAGS = "Tags"
    TASK_DEFINITION_ARN = "TaskDefinitionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "platform_version": "PlatformVersion",
        "group": "Group",
        "enable_ecs_managed_tags": "EnableECSManagedTags",
        "task_count": "TaskCount",
        "enable_execute_command": "EnableExecuteCommand",
        "placement_constraints": "PlacementConstraints",
        "propagate_tags": "PropagateTags",
        "placement_strategy": "PlacementStrategy",
        "launch_type": "LaunchType",
        "capacity_provider_strategy": "CapacityProviderStrategy",
        "reference_id": "ReferenceId",
        "overrides": "Overrides",
        "network_configuration": "NetworkConfiguration",
        "tags": "Tags",
        "task_definition_arn": "TaskDefinitionArn",
    }

    platform_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_ecs_managed_tags: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    task_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    placement_constraints: Optional[list[PlacementConstraint]] = None
    propagate_tags: Optional[Union[str, PropagateTags, Ref, GetAtt, Sub]] = None
    placement_strategy: Optional[list[PlacementStrategy]] = None
    launch_type: Optional[Union[str, LaunchType, Ref, GetAtt, Sub]] = None
    capacity_provider_strategy: Optional[list[CapacityProviderStrategyItem]] = None
    reference_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overrides: Optional[EcsTaskOverride] = None
    network_configuration: Optional[NetworkConfiguration] = None
    tags: Optional[list[Tag]] = None
    task_definition_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetEventBridgeEventBusParameters(PropertyType):
    DETAIL_TYPE = "DetailType"
    ENDPOINT_ID = "EndpointId"
    TIME = "Time"
    RESOURCES = "Resources"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "detail_type": "DetailType",
        "endpoint_id": "EndpointId",
        "time": "Time",
        "resources": "Resources",
        "source": "Source",
    }

    detail_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resources: Optional[Union[list[str], Ref]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetHttpParameters(PropertyType):
    PATH_PARAMETER_VALUES = "PathParameterValues"
    HEADER_PARAMETERS = "HeaderParameters"
    QUERY_STRING_PARAMETERS = "QueryStringParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path_parameter_values": "PathParameterValues",
        "header_parameters": "HeaderParameters",
        "query_string_parameters": "QueryStringParameters",
    }

    path_parameter_values: Optional[Union[list[str], Ref]] = None
    header_parameters: Optional[dict[str, str]] = None
    query_string_parameters: Optional[dict[str, str]] = None


@dataclass
class PipeTargetKinesisStreamParameters(PropertyType):
    PARTITION_KEY = "PartitionKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partition_key": "PartitionKey",
    }

    partition_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetLambdaFunctionParameters(PropertyType):
    INVOCATION_TYPE = "InvocationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invocation_type": "InvocationType",
    }

    invocation_type: Optional[Union[str, PipeTargetInvocationType, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetParameters(PropertyType):
    STEP_FUNCTION_STATE_MACHINE_PARAMETERS = "StepFunctionStateMachineParameters"
    HTTP_PARAMETERS = "HttpParameters"
    TIMESTREAM_PARAMETERS = "TimestreamParameters"
    INPUT_TEMPLATE = "InputTemplate"
    EVENT_BRIDGE_EVENT_BUS_PARAMETERS = "EventBridgeEventBusParameters"
    LAMBDA_FUNCTION_PARAMETERS = "LambdaFunctionParameters"
    BATCH_JOB_PARAMETERS = "BatchJobParameters"
    REDSHIFT_DATA_PARAMETERS = "RedshiftDataParameters"
    SQS_QUEUE_PARAMETERS = "SqsQueueParameters"
    CLOUD_WATCH_LOGS_PARAMETERS = "CloudWatchLogsParameters"
    KINESIS_STREAM_PARAMETERS = "KinesisStreamParameters"
    SAGE_MAKER_PIPELINE_PARAMETERS = "SageMakerPipelineParameters"
    ECS_TASK_PARAMETERS = "EcsTaskParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "step_function_state_machine_parameters": "StepFunctionStateMachineParameters",
        "http_parameters": "HttpParameters",
        "timestream_parameters": "TimestreamParameters",
        "input_template": "InputTemplate",
        "event_bridge_event_bus_parameters": "EventBridgeEventBusParameters",
        "lambda_function_parameters": "LambdaFunctionParameters",
        "batch_job_parameters": "BatchJobParameters",
        "redshift_data_parameters": "RedshiftDataParameters",
        "sqs_queue_parameters": "SqsQueueParameters",
        "cloud_watch_logs_parameters": "CloudWatchLogsParameters",
        "kinesis_stream_parameters": "KinesisStreamParameters",
        "sage_maker_pipeline_parameters": "SageMakerPipelineParameters",
        "ecs_task_parameters": "EcsTaskParameters",
    }

    step_function_state_machine_parameters: Optional[PipeTargetStateMachineParameters] = None
    http_parameters: Optional[PipeTargetHttpParameters] = None
    timestream_parameters: Optional[PipeTargetTimestreamParameters] = None
    input_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_bridge_event_bus_parameters: Optional[PipeTargetEventBridgeEventBusParameters] = None
    lambda_function_parameters: Optional[PipeTargetLambdaFunctionParameters] = None
    batch_job_parameters: Optional[PipeTargetBatchJobParameters] = None
    redshift_data_parameters: Optional[PipeTargetRedshiftDataParameters] = None
    sqs_queue_parameters: Optional[PipeTargetSqsQueueParameters] = None
    cloud_watch_logs_parameters: Optional[PipeTargetCloudWatchLogsParameters] = None
    kinesis_stream_parameters: Optional[PipeTargetKinesisStreamParameters] = None
    sage_maker_pipeline_parameters: Optional[PipeTargetSageMakerPipelineParameters] = None
    ecs_task_parameters: Optional[PipeTargetEcsTaskParameters] = None


@dataclass
class PipeTargetRedshiftDataParameters(PropertyType):
    STATEMENT_NAME = "StatementName"
    SQLS = "Sqls"
    DATABASE = "Database"
    SECRET_MANAGER_ARN = "SecretManagerArn"
    DB_USER = "DbUser"
    WITH_EVENT = "WithEvent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statement_name": "StatementName",
        "sqls": "Sqls",
        "database": "Database",
        "secret_manager_arn": "SecretManagerArn",
        "db_user": "DbUser",
        "with_event": "WithEvent",
    }

    statement_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sqls: Optional[Union[list[str], Ref]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_manager_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    with_event: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetSageMakerPipelineParameters(PropertyType):
    PIPELINE_PARAMETER_LIST = "PipelineParameterList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pipeline_parameter_list": "PipelineParameterList",
    }

    pipeline_parameter_list: Optional[list[SageMakerPipelineParameter]] = None


@dataclass
class PipeTargetSqsQueueParameters(PropertyType):
    MESSAGE_GROUP_ID = "MessageGroupId"
    MESSAGE_DEDUPLICATION_ID = "MessageDeduplicationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_group_id": "MessageGroupId",
        "message_deduplication_id": "MessageDeduplicationId",
    }

    message_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_deduplication_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetStateMachineParameters(PropertyType):
    INVOCATION_TYPE = "InvocationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invocation_type": "InvocationType",
    }

    invocation_type: Optional[Union[str, PipeTargetInvocationType, Ref, GetAtt, Sub]] = None


@dataclass
class PipeTargetTimestreamParameters(PropertyType):
    VERSION_VALUE = "VersionValue"
    DIMENSION_MAPPINGS = "DimensionMappings"
    EPOCH_TIME_UNIT = "EpochTimeUnit"
    TIME_FIELD_TYPE = "TimeFieldType"
    TIMESTAMP_FORMAT = "TimestampFormat"
    MULTI_MEASURE_MAPPINGS = "MultiMeasureMappings"
    TIME_VALUE = "TimeValue"
    SINGLE_MEASURE_MAPPINGS = "SingleMeasureMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version_value": "VersionValue",
        "dimension_mappings": "DimensionMappings",
        "epoch_time_unit": "EpochTimeUnit",
        "time_field_type": "TimeFieldType",
        "timestamp_format": "TimestampFormat",
        "multi_measure_mappings": "MultiMeasureMappings",
        "time_value": "TimeValue",
        "single_measure_mappings": "SingleMeasureMappings",
    }

    version_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_mappings: Optional[list[DimensionMapping]] = None
    epoch_time_unit: Optional[Union[str, EpochTimeUnit, Ref, GetAtt, Sub]] = None
    time_field_type: Optional[Union[str, TimeFieldType, Ref, GetAtt, Sub]] = None
    timestamp_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multi_measure_mappings: Optional[list[MultiMeasureMapping]] = None
    time_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    single_measure_mappings: Optional[list[SingleMeasureMapping]] = None


@dataclass
class PlacementConstraint(PropertyType):
    TYPE = "Type"
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "expression": "Expression",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PlacementStrategy(PropertyType):
    FIELD = "Field"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "type_": "Type",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3LogDestination(PropertyType):
    BUCKET_NAME = "BucketName"
    OUTPUT_FORMAT = "OutputFormat"
    PREFIX = "Prefix"
    BUCKET_OWNER = "BucketOwner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "output_format": "OutputFormat",
        "prefix": "Prefix",
        "bucket_owner": "BucketOwner",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_format: Optional[Union[str, S3OutputFormat, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SageMakerPipelineParameter(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelfManagedKafkaAccessConfigurationCredentials(PropertyType):
    BASIC_AUTH = "BasicAuth"
    SASL_SCRAM256_AUTH = "SaslScram256Auth"
    CLIENT_CERTIFICATE_TLS_AUTH = "ClientCertificateTlsAuth"
    SASL_SCRAM512_AUTH = "SaslScram512Auth"

    _property_mappings: ClassVar[dict[str, str]] = {
        "basic_auth": "BasicAuth",
        "sasl_scram256_auth": "SaslScram256Auth",
        "client_certificate_tls_auth": "ClientCertificateTlsAuth",
        "sasl_scram512_auth": "SaslScram512Auth",
    }

    basic_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sasl_scram256_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_certificate_tls_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sasl_scram512_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelfManagedKafkaAccessConfigurationVpc(PropertyType):
    SUBNETS = "Subnets"
    SECURITY_GROUP = "SecurityGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group": "SecurityGroup",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group: Optional[Union[list[str], Ref]] = None


@dataclass
class SingleMeasureMapping(PropertyType):
    MEASURE_NAME = "MeasureName"
    MEASURE_VALUE_TYPE = "MeasureValueType"
    MEASURE_VALUE = "MeasureValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "measure_name": "MeasureName",
        "measure_value_type": "MeasureValueType",
        "measure_value": "MeasureValue",
    }

    measure_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure_value_type: Optional[Union[str, MeasureValueType, Ref, GetAtt, Sub]] = None
    measure_value: Optional[Union[str, Ref, GetAtt, Sub]] = None

