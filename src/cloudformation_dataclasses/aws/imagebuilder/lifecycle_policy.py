"""PropertyTypes for AWS::ImageBuilder::LifecyclePolicy."""

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
class Action(PropertyType):
    TYPE = "Type"
    INCLUDE_RESOURCES = "IncludeResources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "include_resources": "IncludeResources",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_resources: Optional[IncludeResources] = None


@dataclass
class AmiExclusionRules(PropertyType):
    IS_PUBLIC = "IsPublic"
    LAST_LAUNCHED = "LastLaunched"
    REGIONS = "Regions"
    SHARED_ACCOUNTS = "SharedAccounts"
    TAG_MAP = "TagMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_public": "IsPublic",
        "last_launched": "LastLaunched",
        "regions": "Regions",
        "shared_accounts": "SharedAccounts",
        "tag_map": "TagMap",
    }

    is_public: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    last_launched: Optional[LastLaunched] = None
    regions: Optional[Union[list[str], Ref]] = None
    shared_accounts: Optional[Union[list[str], Ref]] = None
    tag_map: Optional[dict[str, str]] = None


@dataclass
class ExclusionRules(PropertyType):
    AMIS = "Amis"
    TAG_MAP = "TagMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amis": "Amis",
        "tag_map": "TagMap",
    }

    amis: Optional[AmiExclusionRules] = None
    tag_map: Optional[dict[str, str]] = None


@dataclass
class Filter(PropertyType):
    TYPE = "Type"
    VALUE = "Value"
    RETAIN_AT_LEAST = "RetainAtLeast"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "retain_at_least": "RetainAtLeast",
        "unit": "Unit",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    retain_at_least: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IncludeResources(PropertyType):
    CONTAINERS = "Containers"
    AMIS = "Amis"
    SNAPSHOTS = "Snapshots"

    _property_mappings: ClassVar[dict[str, str]] = {
        "containers": "Containers",
        "amis": "Amis",
        "snapshots": "Snapshots",
    }

    containers: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    amis: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    snapshots: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LastLaunched(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDetail(PropertyType):
    ACTION = "Action"
    EXCLUSION_RULES = "ExclusionRules"
    FILTER = "Filter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "exclusion_rules": "ExclusionRules",
        "filter": "Filter",
    }

    action: Optional[Action] = None
    exclusion_rules: Optional[ExclusionRules] = None
    filter: Optional[Filter] = None


@dataclass
class RecipeSelection(PropertyType):
    NAME = "Name"
    SEMANTIC_VERSION = "SemanticVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "semantic_version": "SemanticVersion",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    semantic_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceSelection(PropertyType):
    RECIPES = "Recipes"
    TAG_MAP = "TagMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recipes": "Recipes",
        "tag_map": "TagMap",
    }

    recipes: Optional[list[RecipeSelection]] = None
    tag_map: Optional[dict[str, str]] = None

