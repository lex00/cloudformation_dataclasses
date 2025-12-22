"""PropertyTypes for AWS::ImageBuilder::InfrastructureConfiguration."""

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
class InstanceMetadataOptions(PropertyType):
    HTTP_PUT_RESPONSE_HOP_LIMIT = "HttpPutResponseHopLimit"
    HTTP_TOKENS = "HttpTokens"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_put_response_hop_limit": "HttpPutResponseHopLimit",
        "http_tokens": "HttpTokens",
    }

    http_put_response_hop_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_tokens: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Logging(PropertyType):
    S3_LOGS = "S3Logs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_logs": "S3Logs",
    }

    s3_logs: Optional[S3Logs] = None


@dataclass
class Placement(PropertyType):
    TENANCY = "Tenancy"
    AVAILABILITY_ZONE = "AvailabilityZone"
    HOST_ID = "HostId"
    HOST_RESOURCE_GROUP_ARN = "HostResourceGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tenancy": "Tenancy",
        "availability_zone": "AvailabilityZone",
        "host_id": "HostId",
        "host_resource_group_arn": "HostResourceGroupArn",
    }

    tenancy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Logs(PropertyType):
    S3_KEY_PREFIX = "S3KeyPrefix"
    S3_BUCKET_NAME = "S3BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_key_prefix": "S3KeyPrefix",
        "s3_bucket_name": "S3BucketName",
    }

    s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

