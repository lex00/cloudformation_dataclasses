"""PropertyTypes for AWS::Scheduler::Schedule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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
    weight: Optional[Union[float, Ref, GetAtt, Sub]] = None
    base: Optional[Union[float, Ref, GetAtt, Sub]] = None


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
    TASK_COUNT = "TaskCount"
    ENABLE_EXECUTE_COMMAND = "EnableExecuteCommand"
    PLACEMENT_CONSTRAINTS = "PlacementConstraints"
    PROPAGATE_TAGS = "PropagateTags"
    PLACEMENT_STRATEGY = "PlacementStrategy"
    LAUNCH_TYPE = "LaunchType"
    CAPACITY_PROVIDER_STRATEGY = "CapacityProviderStrategy"
    REFERENCE_ID = "ReferenceId"
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
        "network_configuration": "NetworkConfiguration",
        "tags": "Tags",
        "task_definition_arn": "TaskDefinitionArn",
    }

    platform_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_ecs_managed_tags: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    task_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    enable_execute_command: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    placement_constraints: Optional[list[PlacementConstraint]] = None
    propagate_tags: Optional[Union[str, PropagateTags, Ref, GetAtt, Sub]] = None
    placement_strategy: Optional[list[PlacementStrategy]] = None
    launch_type: Optional[Union[str, LaunchType, Ref, GetAtt, Sub]] = None
    capacity_provider_strategy: Optional[list[CapacityProviderStrategyItem]] = None
    reference_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_configuration: Optional[NetworkConfiguration] = None
    tags: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    task_definition_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeParameters(PropertyType):
    DETAIL_TYPE = "DetailType"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "detail_type": "DetailType",
        "source": "Source",
    }

    detail_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlexibleTimeWindow(PropertyType):
    MODE = "Mode"
    MAXIMUM_WINDOW_IN_MINUTES = "MaximumWindowInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "maximum_window_in_minutes": "MaximumWindowInMinutes",
    }

    mode: Optional[Union[str, FlexibleTimeWindowMode, Ref, GetAtt, Sub]] = None
    maximum_window_in_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisParameters(PropertyType):
    PARTITION_KEY = "PartitionKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partition_key": "PartitionKey",
    }

    partition_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    AWSVPC_CONFIGURATION = "AwsvpcConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "awsvpc_configuration": "AwsvpcConfiguration",
    }

    awsvpc_configuration: Optional[AwsVpcConfiguration] = None


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
class RetryPolicy(PropertyType):
    MAXIMUM_RETRY_ATTEMPTS = "MaximumRetryAttempts"
    MAXIMUM_EVENT_AGE_IN_SECONDS = "MaximumEventAgeInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_retry_attempts": "MaximumRetryAttempts",
        "maximum_event_age_in_seconds": "MaximumEventAgeInSeconds",
    }

    maximum_retry_attempts: Optional[Union[float, Ref, GetAtt, Sub]] = None
    maximum_event_age_in_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None


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
    INPUT = "Input"
    SQS_PARAMETERS = "SqsParameters"
    DEAD_LETTER_CONFIG = "DeadLetterConfig"
    ECS_PARAMETERS = "EcsParameters"
    EVENT_BRIDGE_PARAMETERS = "EventBridgeParameters"
    ARN = "Arn"
    KINESIS_PARAMETERS = "KinesisParameters"
    SAGE_MAKER_PIPELINE_PARAMETERS = "SageMakerPipelineParameters"
    RETRY_POLICY = "RetryPolicy"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input": "Input",
        "sqs_parameters": "SqsParameters",
        "dead_letter_config": "DeadLetterConfig",
        "ecs_parameters": "EcsParameters",
        "event_bridge_parameters": "EventBridgeParameters",
        "arn": "Arn",
        "kinesis_parameters": "KinesisParameters",
        "sage_maker_pipeline_parameters": "SageMakerPipelineParameters",
        "retry_policy": "RetryPolicy",
        "role_arn": "RoleArn",
    }

    input: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sqs_parameters: Optional[SqsParameters] = None
    dead_letter_config: Optional[DeadLetterConfig] = None
    ecs_parameters: Optional[EcsParameters] = None
    event_bridge_parameters: Optional[EventBridgeParameters] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kinesis_parameters: Optional[KinesisParameters] = None
    sage_maker_pipeline_parameters: Optional[SageMakerPipelineParameters] = None
    retry_policy: Optional[RetryPolicy] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

