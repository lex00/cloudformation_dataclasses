"""PropertyTypes for AWS::ImageBuilder::Image."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeletionSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role": "ExecutionRole",
    }

    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EcrConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_tags": "ContainerTags",
        "repository_name": "RepositoryName",
    }

    container_tags: Optional[Union[list[str], Ref]] = None
    repository_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageLoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_name": "LogGroupName",
    }

    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImagePipelineExecutionSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "deployment_id": "DeploymentId",
        "on_update": "OnUpdate",
    }

    deployment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_update: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ecr_configuration": "EcrConfiguration",
        "image_scanning_enabled": "ImageScanningEnabled",
    }

    ecr_configuration: Optional[EcrConfiguration] = None
    image_scanning_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ImageTestsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_minutes": "TimeoutMinutes",
        "image_tests_enabled": "ImageTestsEnabled",
    }

    timeout_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    image_tests_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LatestVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "major": "Major",
        "minor": "Minor",
        "arn": "Arn",
        "patch": "Patch",
    }

    major: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minor: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    patch: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

