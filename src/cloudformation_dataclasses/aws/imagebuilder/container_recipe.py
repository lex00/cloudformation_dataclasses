"""PropertyTypes for AWS::ImageBuilder::ContainerRecipe."""

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
class ComponentConfiguration(PropertyType):
    PARAMETERS = "Parameters"
    COMPONENT_ARN = "ComponentArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "component_arn": "ComponentArn",
    }

    parameters: Optional[list[ComponentParameter]] = None
    component_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentParameter(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EbsInstanceBlockDeviceSpecification(PropertyType):
    SNAPSHOT_ID = "SnapshotId"
    VOLUME_TYPE = "VolumeType"
    KMS_KEY_ID = "KmsKeyId"
    ENCRYPTED = "Encrypted"
    THROUGHPUT = "Throughput"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"
    DELETE_ON_TERMINATION = "DeleteOnTermination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "iops": "Iops",
        "volume_size": "VolumeSize",
        "delete_on_termination": "DeleteOnTermination",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceBlockDeviceMapping(PropertyType):
    EBS = "Ebs"
    NO_DEVICE = "NoDevice"
    VIRTUAL_NAME = "VirtualName"
    DEVICE_NAME = "DeviceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs": "Ebs",
        "no_device": "NoDevice",
        "virtual_name": "VirtualName",
        "device_name": "DeviceName",
    }

    ebs: Optional[EbsInstanceBlockDeviceSpecification] = None
    no_device: Optional[Union[str, Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceConfiguration(PropertyType):
    BLOCK_DEVICE_MAPPINGS = "BlockDeviceMappings"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "block_device_mappings": "BlockDeviceMappings",
        "image": "Image",
    }

    block_device_mappings: Optional[list[InstanceBlockDeviceMapping]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LatestVersion(PropertyType):
    MAJOR = "Major"
    MINOR = "Minor"
    ARN = "Arn"
    PATCH = "Patch"

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
class TargetContainerRepository(PropertyType):
    SERVICE = "Service"
    REPOSITORY_NAME = "RepositoryName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service": "Service",
        "repository_name": "RepositoryName",
    }

    service: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

