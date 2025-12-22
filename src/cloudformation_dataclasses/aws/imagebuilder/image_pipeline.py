"""PropertyTypes for AWS::ImageBuilder::ImagePipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BuildType:
    """BuildType enum values."""

    USER_INITIATED = "USER_INITIATED"
    SCHEDULED = "SCHEDULED"
    IMPORT = "IMPORT"
    IMPORT_ISO = "IMPORT_ISO"


class ComponentFormat:
    """ComponentFormat enum values."""

    SHELL = "SHELL"


class ComponentStatus:
    """ComponentStatus enum values."""

    DEPRECATED = "DEPRECATED"
    DISABLED = "DISABLED"
    ACTIVE = "ACTIVE"


class ComponentType:
    """ComponentType enum values."""

    BUILD = "BUILD"
    TEST = "TEST"


class ContainerRepositoryService:
    """ContainerRepositoryService enum values."""

    ECR = "ECR"


class ContainerType:
    """ContainerType enum values."""

    DOCKER = "DOCKER"


class DiskImageFormat:
    """DiskImageFormat enum values."""

    VMDK = "VMDK"
    RAW = "RAW"
    VHD = "VHD"


class EbsVolumeType:
    """EbsVolumeType enum values."""

    STANDARD = "standard"
    IO1 = "io1"
    IO2 = "io2"
    GP2 = "gp2"
    GP3 = "gp3"
    SC1 = "sc1"
    ST1 = "st1"


class ImageScanStatus:
    """ImageScanStatus enum values."""

    PENDING = "PENDING"
    SCANNING = "SCANNING"
    COLLECTING = "COLLECTING"
    COMPLETED = "COMPLETED"
    ABANDONED = "ABANDONED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"


class ImageSource:
    """ImageSource enum values."""

    AMAZON_MANAGED = "AMAZON_MANAGED"
    AWS_MARKETPLACE = "AWS_MARKETPLACE"
    IMPORTED = "IMPORTED"
    CUSTOM = "CUSTOM"


class ImageStatus:
    """ImageStatus enum values."""

    PENDING = "PENDING"
    CREATING = "CREATING"
    BUILDING = "BUILDING"
    TESTING = "TESTING"
    DISTRIBUTING = "DISTRIBUTING"
    INTEGRATING = "INTEGRATING"
    AVAILABLE = "AVAILABLE"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    DEPRECATED = "DEPRECATED"
    DELETED = "DELETED"
    DISABLED = "DISABLED"


class ImageType:
    """ImageType enum values."""

    AMI = "AMI"
    DOCKER = "DOCKER"


class LifecycleExecutionResourceActionName:
    """LifecycleExecutionResourceActionName enum values."""

    AVAILABLE = "AVAILABLE"
    DELETE = "DELETE"
    DEPRECATE = "DEPRECATE"
    DISABLE = "DISABLE"


class LifecycleExecutionResourceStatus:
    """LifecycleExecutionResourceStatus enum values."""

    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SKIPPED = "SKIPPED"
    SUCCESS = "SUCCESS"


class LifecycleExecutionStatus:
    """LifecycleExecutionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    CANCELLING = "CANCELLING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    PENDING = "PENDING"


class LifecyclePolicyDetailActionType:
    """LifecyclePolicyDetailActionType enum values."""

    DELETE = "DELETE"
    DEPRECATE = "DEPRECATE"
    DISABLE = "DISABLE"


class LifecyclePolicyDetailFilterType:
    """LifecyclePolicyDetailFilterType enum values."""

    AGE = "AGE"
    COUNT = "COUNT"


class LifecyclePolicyResourceType:
    """LifecyclePolicyResourceType enum values."""

    AMI_IMAGE = "AMI_IMAGE"
    CONTAINER_IMAGE = "CONTAINER_IMAGE"


class LifecyclePolicyStatus:
    """LifecyclePolicyStatus enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class LifecyclePolicyTimeUnit:
    """LifecyclePolicyTimeUnit enum values."""

    DAYS = "DAYS"
    WEEKS = "WEEKS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"


class MarketplaceResourceType:
    """MarketplaceResourceType enum values."""

    COMPONENT_DATA = "COMPONENT_DATA"
    COMPONENT_ARTIFACT = "COMPONENT_ARTIFACT"


class OnWorkflowFailure:
    """OnWorkflowFailure enum values."""

    CONTINUE = "CONTINUE"
    ABORT = "ABORT"


class Ownership:
    """Ownership enum values."""

    SELF = "Self"
    SHARED = "Shared"
    AMAZON = "Amazon"
    THIRDPARTY = "ThirdParty"
    AWSMARKETPLACE = "AWSMarketplace"


class PipelineExecutionStartCondition:
    """PipelineExecutionStartCondition enum values."""

    EXPRESSION_MATCH_ONLY = "EXPRESSION_MATCH_ONLY"
    EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE = "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"


class PipelineStatus:
    """PipelineStatus enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Platform:
    """Platform enum values."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "macOS"


class ProductCodeType:
    """ProductCodeType enum values."""

    MARKETPLACE = "marketplace"


class ResourceStatus:
    """ResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    DELETED = "DELETED"
    DEPRECATED = "DEPRECATED"
    DISABLED = "DISABLED"


class SsmParameterDataType:
    """SsmParameterDataType enum values."""

    TEXT = "text"
    AWS_EC2_IMAGE = "aws:ec2:image"


class TenancyType:
    """TenancyType enum values."""

    DEFAULT = "default"
    DEDICATED = "dedicated"
    HOST = "host"


class WorkflowExecutionStatus:
    """WorkflowExecutionStatus enum values."""

    PENDING = "PENDING"
    SKIPPED = "SKIPPED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_COMPLETED = "ROLLBACK_COMPLETED"
    CANCELLED = "CANCELLED"


class WorkflowStatus:
    """WorkflowStatus enum values."""

    DEPRECATED = "DEPRECATED"


class WorkflowStepActionType:
    """WorkflowStepActionType enum values."""

    RESUME = "RESUME"
    STOP = "STOP"


class WorkflowStepExecutionRollbackStatus:
    """WorkflowStepExecutionRollbackStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    SKIPPED = "SKIPPED"
    FAILED = "FAILED"


class WorkflowStepExecutionStatus:
    """WorkflowStepExecutionStatus enum values."""

    PENDING = "PENDING"
    SKIPPED = "SKIPPED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class WorkflowType:
    """WorkflowType enum values."""

    BUILD = "BUILD"
    TEST = "TEST"
    DISTRIBUTION = "DISTRIBUTION"


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

