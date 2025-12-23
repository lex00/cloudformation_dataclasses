"""PropertyTypes for AWS::ImageBuilder::ImagePipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoDisablePolicy(PropertyType):
    FAILURE_COUNT = "FailureCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "failure_count": "FailureCount",
    }

    failure_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EcrConfiguration(PropertyType):
    CONTAINER_TAGS = "ContainerTags"
    REPOSITORY_NAME = "RepositoryName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_tags": "ContainerTags",
        "repository_name": "RepositoryName",
    }

    container_tags: Optional[Union[list[str], Ref]] = None
    repository_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    ECR_CONFIGURATION = "EcrConfiguration"
    IMAGE_SCANNING_ENABLED = "ImageScanningEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ecr_configuration": "EcrConfiguration",
        "image_scanning_enabled": "ImageScanningEnabled",
    }

    ecr_configuration: Optional[EcrConfiguration] = None
    image_scanning_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ImageTestsConfiguration(PropertyType):
    TIMEOUT_MINUTES = "TimeoutMinutes"
    IMAGE_TESTS_ENABLED = "ImageTestsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_minutes": "TimeoutMinutes",
        "image_tests_enabled": "ImageTestsEnabled",
    }

    timeout_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    image_tests_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineLoggingConfiguration(PropertyType):
    PIPELINE_LOG_GROUP_NAME = "PipelineLogGroupName"
    IMAGE_LOG_GROUP_NAME = "ImageLogGroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pipeline_log_group_name": "PipelineLogGroupName",
        "image_log_group_name": "ImageLogGroupName",
    }

    pipeline_log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    SCHEDULE_EXPRESSION = "ScheduleExpression"
    PIPELINE_EXECUTION_START_CONDITION = "PipelineExecutionStartCondition"
    AUTO_DISABLE_POLICY = "AutoDisablePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
        "pipeline_execution_start_condition": "PipelineExecutionStartCondition",
        "auto_disable_policy": "AutoDisablePolicy",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pipeline_execution_start_condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_disable_policy: Optional[AutoDisablePolicy] = None


@dataclass
class WorkflowConfiguration(PropertyType):
    PARALLEL_GROUP = "ParallelGroup"
    PARAMETERS = "Parameters"
    WORKFLOW_ARN = "WorkflowArn"
    ON_FAILURE = "OnFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parallel_group": "ParallelGroup",
        "parameters": "Parameters",
        "workflow_arn": "WorkflowArn",
        "on_failure": "OnFailure",
    }

    parallel_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[list[WorkflowParameter]] = None
    workflow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_failure: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowParameter(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

