"""PropertyTypes for AWS::Events::Rule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppSyncParameters(PropertyType):
    GRAPH_QL_OPERATION = "GraphQLOperation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "graph_ql_operation": "GraphQLOperation",
    }

    graph_ql_operation: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class BatchParameters(PropertyType):
    ARRAY_PROPERTIES = "ArrayProperties"
    JOB_NAME = "JobName"
    RETRY_STRATEGY = "RetryStrategy"
    JOB_DEFINITION = "JobDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "array_properties": "ArrayProperties",
        "job_name": "JobName",
        "retry_strategy": "RetryStrategy",
        "job_definition": "JobDefinition",
    }

    array_properties: Optional[BatchArrayProperties] = None
    job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retry_strategy: Optional[BatchRetryStrategy] = None
    job_definition: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
    BASE = "Base"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "base": "Base",
        "weight": "Weight",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeadLetterConfig(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcsParameters(PropertyType):
    PLATFORM_VERSION = "PlatformVersion"
    GROUP = "Group"
    ENABLE_ECS_MANAGED_TAGS = "EnableECSManagedTags"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    PLACEMENT_CONSTRAINTS = "PlacementConstraints"
    PROPAGATE_TAGS = "PropagateTags"
    TASK_COUNT = "TaskCount"
    PLACEMENT_STRATEGIES = "PlacementStrategies"
    CAPACITY_PROVIDER_STRATEGY = "CapacityProviderStrategy"
    LAUNCH_TYPE = "LaunchType"
    REFERENCE_ID = "ReferenceId"
    TAG_LIST = "TagList"
    NETWORK_CONFIGURATION = "NetworkConfiguration"
    TASK_DEFINITION_ARN = "TaskDefinitionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "platform_version": "PlatformVersion",
        "group": "Group",
        "enable_ecs_managed_tags": "EnableECSManagedTags",
        "enable_execute_command": "EnableExecuteCommand",
        "placement_constraints": "PlacementConstraints",
        "propagate_tags": "PropagateTags",
        "task_count": "TaskCount",
        "placement_strategies": "PlacementStrategies",
        "capacity_provider_strategy": "CapacityProviderStrategy",
        "launch_type": "LaunchType",
        "reference_id": "ReferenceId",
        "tag_list": "TagList",
        "network_configuration": "NetworkConfiguration",
        "task_definition_arn": "TaskDefinitionArn",
    }

    platform_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_ecs_managed_tags: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    placement_constraints: Optional[list[PlacementConstraint]] = None
    propagate_tags: Optional[Union[str, PropagateTags, Ref, GetAtt, Sub]] = None
    task_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    placement_strategies: Optional[list[PlacementStrategy]] = None
    capacity_provider_strategy: Optional[list[CapacityProviderStrategyItem]] = None
    launch_type: Optional[Union[str, LaunchType, Ref, GetAtt, Sub]] = None
    reference_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_list: Optional[list[Tag]] = None
    network_configuration: Optional[NetworkConfiguration] = None
    task_definition_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpParameters(PropertyType):
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
class InputTransformer(PropertyType):
    INPUT_PATHS_MAP = "InputPathsMap"
    INPUT_TEMPLATE = "InputTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_paths_map": "InputPathsMap",
        "input_template": "InputTemplate",
    }

    input_paths_map: Optional[dict[str, str]] = None
    input_template: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisParameters(PropertyType):
    PARTITION_KEY_PATH = "PartitionKeyPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partition_key_path": "PartitionKeyPath",
    }

    partition_key_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    AWS_VPC_CONFIGURATION = "AwsVpcConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_vpc_configuration": "AwsVpcConfiguration",
    }

    aws_vpc_configuration: Optional[AwsVpcConfiguration] = None


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
class RedshiftDataParameters(PropertyType):
    STATEMENT_NAME = "StatementName"
    SQLS = "Sqls"
    DATABASE = "Database"
    SECRET_MANAGER_ARN = "SecretManagerArn"
    DB_USER = "DbUser"
    SQL = "Sql"
    WITH_EVENT = "WithEvent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statement_name": "StatementName",
        "sqls": "Sqls",
        "database": "Database",
        "secret_manager_arn": "SecretManagerArn",
        "db_user": "DbUser",
        "sql": "Sql",
        "with_event": "WithEvent",
    }

    statement_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sqls: Optional[Union[list[str], Ref]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_manager_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql: Optional[Union[str, Ref, GetAtt, Sub]] = None
    with_event: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RetryPolicy(PropertyType):
    MAXIMUM_RETRY_ATTEMPTS = "MaximumRetryAttempts"
    MAXIMUM_EVENT_AGE_IN_SECONDS = "MaximumEventAgeInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_retry_attempts": "MaximumRetryAttempts",
        "maximum_event_age_in_seconds": "MaximumEventAgeInSeconds",
    }

    maximum_retry_attempts: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_event_age_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RunCommandParameters(PropertyType):
    RUN_COMMAND_TARGETS = "RunCommandTargets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "run_command_targets": "RunCommandTargets",
    }

    run_command_targets: Optional[list[RunCommandTarget]] = None


@dataclass
class RunCommandTarget(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class SageMakerPipelineParameters(PropertyType):
    PIPELINE_PARAMETER_LIST = "PipelineParameterList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pipeline_parameter_list": "PipelineParameterList",
    }

    pipeline_parameter_list: Optional[list[SageMakerPipelineParameter]] = None


@dataclass
class SqsParameters(PropertyType):
    MESSAGE_GROUP_ID = "MessageGroupId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_group_id": "MessageGroupId",
    }

    message_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Target(PropertyType):
    INPUT_PATH = "InputPath"
    HTTP_PARAMETERS = "HttpParameters"
    DEAD_LETTER_CONFIG = "DeadLetterConfig"
    RUN_COMMAND_PARAMETERS = "RunCommandParameters"
    INPUT_TRANSFORMER = "InputTransformer"
    KINESIS_PARAMETERS = "KinesisParameters"
    ROLE_ARN = "RoleArn"
    REDSHIFT_DATA_PARAMETERS = "RedshiftDataParameters"
    APP_SYNC_PARAMETERS = "AppSyncParameters"
    INPUT = "Input"
    SQS_PARAMETERS = "SqsParameters"
    ECS_PARAMETERS = "EcsParameters"
    BATCH_PARAMETERS = "BatchParameters"
    ID = "Id"
    ARN = "Arn"
    SAGE_MAKER_PIPELINE_PARAMETERS = "SageMakerPipelineParameters"
    RETRY_POLICY = "RetryPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_path": "InputPath",
        "http_parameters": "HttpParameters",
        "dead_letter_config": "DeadLetterConfig",
        "run_command_parameters": "RunCommandParameters",
        "input_transformer": "InputTransformer",
        "kinesis_parameters": "KinesisParameters",
        "role_arn": "RoleArn",
        "redshift_data_parameters": "RedshiftDataParameters",
        "app_sync_parameters": "AppSyncParameters",
        "input": "Input",
        "sqs_parameters": "SqsParameters",
        "ecs_parameters": "EcsParameters",
        "batch_parameters": "BatchParameters",
        "id": "Id",
        "arn": "Arn",
        "sage_maker_pipeline_parameters": "SageMakerPipelineParameters",
        "retry_policy": "RetryPolicy",
    }

    input_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_parameters: Optional[HttpParameters] = None
    dead_letter_config: Optional[DeadLetterConfig] = None
    run_command_parameters: Optional[RunCommandParameters] = None
    input_transformer: Optional[InputTransformer] = None
    kinesis_parameters: Optional[KinesisParameters] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redshift_data_parameters: Optional[RedshiftDataParameters] = None
    app_sync_parameters: Optional[AppSyncParameters] = None
    input: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sqs_parameters: Optional[SqsParameters] = None
    ecs_parameters: Optional[EcsParameters] = None
    batch_parameters: Optional[BatchParameters] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sage_maker_pipeline_parameters: Optional[SageMakerPipelineParameters] = None
    retry_policy: Optional[RetryPolicy] = None

