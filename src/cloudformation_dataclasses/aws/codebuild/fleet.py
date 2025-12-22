"""PropertyTypes for AWS::CodeBuild::Fleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ArtifactNamespace:
    """ArtifactNamespace enum values."""

    NONE = "NONE"
    BUILD_ID = "BUILD_ID"


class ArtifactPackaging:
    """ArtifactPackaging enum values."""

    NONE = "NONE"
    ZIP = "ZIP"


class ArtifactsType:
    """ArtifactsType enum values."""

    CODEPIPELINE = "CODEPIPELINE"
    S3 = "S3"
    NO_ARTIFACTS = "NO_ARTIFACTS"


class AuthType:
    """AuthType enum values."""

    OAUTH = "OAUTH"
    BASIC_AUTH = "BASIC_AUTH"
    PERSONAL_ACCESS_TOKEN = "PERSONAL_ACCESS_TOKEN"
    CODECONNECTIONS = "CODECONNECTIONS"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class BatchReportModeType:
    """BatchReportModeType enum values."""

    REPORT_INDIVIDUAL_BUILDS = "REPORT_INDIVIDUAL_BUILDS"
    REPORT_AGGREGATED_BATCH = "REPORT_AGGREGATED_BATCH"


class BucketOwnerAccess:
    """BucketOwnerAccess enum values."""

    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    FULL = "FULL"


class BuildBatchPhaseType:
    """BuildBatchPhaseType enum values."""

    SUBMITTED = "SUBMITTED"
    DOWNLOAD_BATCHSPEC = "DOWNLOAD_BATCHSPEC"
    IN_PROGRESS = "IN_PROGRESS"
    COMBINE_ARTIFACTS = "COMBINE_ARTIFACTS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class BuildPhaseType:
    """BuildPhaseType enum values."""

    SUBMITTED = "SUBMITTED"
    QUEUED = "QUEUED"
    PROVISIONING = "PROVISIONING"
    DOWNLOAD_SOURCE = "DOWNLOAD_SOURCE"
    INSTALL = "INSTALL"
    PRE_BUILD = "PRE_BUILD"
    BUILD = "BUILD"
    POST_BUILD = "POST_BUILD"
    UPLOAD_ARTIFACTS = "UPLOAD_ARTIFACTS"
    FINALIZING = "FINALIZING"
    COMPLETED = "COMPLETED"


class CacheMode:
    """CacheMode enum values."""

    LOCAL_DOCKER_LAYER_CACHE = "LOCAL_DOCKER_LAYER_CACHE"
    LOCAL_SOURCE_CACHE = "LOCAL_SOURCE_CACHE"
    LOCAL_CUSTOM_CACHE = "LOCAL_CUSTOM_CACHE"


class CacheType:
    """CacheType enum values."""

    NO_CACHE = "NO_CACHE"
    S3 = "S3"
    LOCAL = "LOCAL"


class CommandType:
    """CommandType enum values."""

    SHELL = "SHELL"


class ComputeType:
    """ComputeType enum values."""

    BUILD_GENERAL1_SMALL = "BUILD_GENERAL1_SMALL"
    BUILD_GENERAL1_MEDIUM = "BUILD_GENERAL1_MEDIUM"
    BUILD_GENERAL1_LARGE = "BUILD_GENERAL1_LARGE"
    BUILD_GENERAL1_XLARGE = "BUILD_GENERAL1_XLARGE"
    BUILD_GENERAL1_2XLARGE = "BUILD_GENERAL1_2XLARGE"
    BUILD_LAMBDA_1GB = "BUILD_LAMBDA_1GB"
    BUILD_LAMBDA_2GB = "BUILD_LAMBDA_2GB"
    BUILD_LAMBDA_4GB = "BUILD_LAMBDA_4GB"
    BUILD_LAMBDA_8GB = "BUILD_LAMBDA_8GB"
    BUILD_LAMBDA_10GB = "BUILD_LAMBDA_10GB"
    ATTRIBUTE_BASED_COMPUTE = "ATTRIBUTE_BASED_COMPUTE"
    CUSTOM_INSTANCE_TYPE = "CUSTOM_INSTANCE_TYPE"


class CredentialProviderType:
    """CredentialProviderType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"


class EnvironmentType:
    """EnvironmentType enum values."""

    WINDOWS_CONTAINER = "WINDOWS_CONTAINER"
    LINUX_CONTAINER = "LINUX_CONTAINER"
    LINUX_GPU_CONTAINER = "LINUX_GPU_CONTAINER"
    ARM_CONTAINER = "ARM_CONTAINER"
    WINDOWS_SERVER_2019_CONTAINER = "WINDOWS_SERVER_2019_CONTAINER"
    WINDOWS_SERVER_2022_CONTAINER = "WINDOWS_SERVER_2022_CONTAINER"
    LINUX_LAMBDA_CONTAINER = "LINUX_LAMBDA_CONTAINER"
    ARM_LAMBDA_CONTAINER = "ARM_LAMBDA_CONTAINER"
    LINUX_EC2 = "LINUX_EC2"
    ARM_EC2 = "ARM_EC2"
    WINDOWS_EC2 = "WINDOWS_EC2"
    MAC_ARM = "MAC_ARM"


class EnvironmentVariableType:
    """EnvironmentVariableType enum values."""

    PLAINTEXT = "PLAINTEXT"
    PARAMETER_STORE = "PARAMETER_STORE"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class FileSystemType:
    """FileSystemType enum values."""

    EFS = "EFS"


class FleetContextCode:
    """FleetContextCode enum values."""

    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    ACTION_REQUIRED = "ACTION_REQUIRED"
    PENDING_DELETION = "PENDING_DELETION"
    INSUFFICIENT_CAPACITY = "INSUFFICIENT_CAPACITY"


class FleetOverflowBehavior:
    """FleetOverflowBehavior enum values."""

    QUEUE = "QUEUE"
    ON_DEMAND = "ON_DEMAND"


class FleetProxyRuleBehavior:
    """FleetProxyRuleBehavior enum values."""

    ALLOW_ALL = "ALLOW_ALL"
    DENY_ALL = "DENY_ALL"


class FleetProxyRuleEffectType:
    """FleetProxyRuleEffectType enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class FleetProxyRuleType:
    """FleetProxyRuleType enum values."""

    DOMAIN = "DOMAIN"
    IP = "IP"


class FleetScalingMetricType:
    """FleetScalingMetricType enum values."""

    FLEET_UTILIZATION_RATE = "FLEET_UTILIZATION_RATE"


class FleetScalingType:
    """FleetScalingType enum values."""

    TARGET_TRACKING_SCALING = "TARGET_TRACKING_SCALING"


class FleetSortByType:
    """FleetSortByType enum values."""

    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class FleetStatusCode:
    """FleetStatusCode enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    ROTATING = "ROTATING"
    PENDING_DELETION = "PENDING_DELETION"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    ACTIVE = "ACTIVE"


class ImagePullCredentialsType:
    """ImagePullCredentialsType enum values."""

    CODEBUILD = "CODEBUILD"
    SERVICE_ROLE = "SERVICE_ROLE"


class LanguageType:
    """LanguageType enum values."""

    JAVA = "JAVA"
    PYTHON = "PYTHON"
    NODE_JS = "NODE_JS"
    RUBY = "RUBY"
    GOLANG = "GOLANG"
    DOCKER = "DOCKER"
    ANDROID = "ANDROID"
    DOTNET = "DOTNET"
    BASE = "BASE"
    PHP = "PHP"


class LogsConfigStatusType:
    """LogsConfigStatusType enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MachineType:
    """MachineType enum values."""

    GENERAL = "GENERAL"
    NVME = "NVME"


class PlatformType:
    """PlatformType enum values."""

    DEBIAN = "DEBIAN"
    AMAZON_LINUX = "AMAZON_LINUX"
    UBUNTU = "UBUNTU"
    WINDOWS_SERVER = "WINDOWS_SERVER"


class ProjectSortByType:
    """ProjectSortByType enum values."""

    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ProjectVisibilityType:
    """ProjectVisibilityType enum values."""

    PUBLIC_READ = "PUBLIC_READ"
    PRIVATE = "PRIVATE"


class PullRequestBuildApproverRole:
    """PullRequestBuildApproverRole enum values."""

    GITHUB_READ = "GITHUB_READ"
    GITHUB_TRIAGE = "GITHUB_TRIAGE"
    GITHUB_WRITE = "GITHUB_WRITE"
    GITHUB_MAINTAIN = "GITHUB_MAINTAIN"
    GITHUB_ADMIN = "GITHUB_ADMIN"
    GITLAB_GUEST = "GITLAB_GUEST"
    GITLAB_PLANNER = "GITLAB_PLANNER"
    GITLAB_REPORTER = "GITLAB_REPORTER"
    GITLAB_DEVELOPER = "GITLAB_DEVELOPER"
    GITLAB_MAINTAINER = "GITLAB_MAINTAINER"
    GITLAB_OWNER = "GITLAB_OWNER"
    BITBUCKET_READ = "BITBUCKET_READ"
    BITBUCKET_WRITE = "BITBUCKET_WRITE"
    BITBUCKET_ADMIN = "BITBUCKET_ADMIN"


class PullRequestBuildCommentApproval:
    """PullRequestBuildCommentApproval enum values."""

    DISABLED = "DISABLED"
    ALL_PULL_REQUESTS = "ALL_PULL_REQUESTS"
    FORK_PULL_REQUESTS = "FORK_PULL_REQUESTS"


class ReportCodeCoverageSortByType:
    """ReportCodeCoverageSortByType enum values."""

    LINE_COVERAGE_PERCENTAGE = "LINE_COVERAGE_PERCENTAGE"
    FILE_PATH = "FILE_PATH"


class ReportExportConfigType:
    """ReportExportConfigType enum values."""

    S3 = "S3"
    NO_EXPORT = "NO_EXPORT"


class ReportGroupSortByType:
    """ReportGroupSortByType enum values."""

    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ReportGroupStatusType:
    """ReportGroupStatusType enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class ReportGroupTrendFieldType:
    """ReportGroupTrendFieldType enum values."""

    PASS_RATE = "PASS_RATE"
    DURATION = "DURATION"
    TOTAL = "TOTAL"
    LINE_COVERAGE = "LINE_COVERAGE"
    LINES_COVERED = "LINES_COVERED"
    LINES_MISSED = "LINES_MISSED"
    BRANCH_COVERAGE = "BRANCH_COVERAGE"
    BRANCHES_COVERED = "BRANCHES_COVERED"
    BRANCHES_MISSED = "BRANCHES_MISSED"


class ReportPackagingType:
    """ReportPackagingType enum values."""

    ZIP = "ZIP"
    NONE = "NONE"


class ReportStatusType:
    """ReportStatusType enum values."""

    GENERATING = "GENERATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    INCOMPLETE = "INCOMPLETE"
    DELETING = "DELETING"


class ReportType:
    """ReportType enum values."""

    TEST = "TEST"
    CODE_COVERAGE = "CODE_COVERAGE"


class RetryBuildBatchType:
    """RetryBuildBatchType enum values."""

    RETRY_ALL_BUILDS = "RETRY_ALL_BUILDS"
    RETRY_FAILED_BUILDS = "RETRY_FAILED_BUILDS"


class ServerType:
    """ServerType enum values."""

    GITHUB = "GITHUB"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    GITLAB = "GITLAB"
    GITLAB_SELF_MANAGED = "GITLAB_SELF_MANAGED"


class SharedResourceSortByType:
    """SharedResourceSortByType enum values."""

    ARN = "ARN"
    MODIFIED_TIME = "MODIFIED_TIME"


class SortOrderType:
    """SortOrderType enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SourceAuthType:
    """SourceAuthType enum values."""

    OAUTH = "OAUTH"
    CODECONNECTIONS = "CODECONNECTIONS"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class SourceType:
    """SourceType enum values."""

    CODECOMMIT = "CODECOMMIT"
    CODEPIPELINE = "CODEPIPELINE"
    GITHUB = "GITHUB"
    GITLAB = "GITLAB"
    GITLAB_SELF_MANAGED = "GITLAB_SELF_MANAGED"
    S3 = "S3"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    NO_SOURCE = "NO_SOURCE"


class StatusType:
    """StatusType enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    FAULT = "FAULT"
    TIMED_OUT = "TIMED_OUT"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"


class WebhookBuildType:
    """WebhookBuildType enum values."""

    BUILD = "BUILD"
    BUILD_BATCH = "BUILD_BATCH"
    RUNNER_BUILDKITE_BUILD = "RUNNER_BUILDKITE_BUILD"


class WebhookFilterType:
    """WebhookFilterType enum values."""

    EVENT = "EVENT"
    BASE_REF = "BASE_REF"
    HEAD_REF = "HEAD_REF"
    ACTOR_ACCOUNT_ID = "ACTOR_ACCOUNT_ID"
    FILE_PATH = "FILE_PATH"
    COMMIT_MESSAGE = "COMMIT_MESSAGE"
    WORKFLOW_NAME = "WORKFLOW_NAME"
    TAG_NAME = "TAG_NAME"
    RELEASE_NAME = "RELEASE_NAME"
    REPOSITORY_NAME = "REPOSITORY_NAME"
    ORGANIZATION_NAME = "ORGANIZATION_NAME"


class WebhookScopeType:
    """WebhookScopeType enum values."""

    GITHUB_ORGANIZATION = "GITHUB_ORGANIZATION"
    GITHUB_GLOBAL = "GITHUB_GLOBAL"
    GITLAB_GROUP = "GITLAB_GROUP"


class WebhookStatus:
    """WebhookStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclass
class ComputeConfiguration(PropertyType):
    DISK = "disk"
    MEMORY = "memory"
    V_CPU = "vCpu"
    INSTANCE_TYPE = "instanceType"
    MACHINE_TYPE = "machineType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disk": "disk",
        "memory": "memory",
        "v_cpu": "vCpu",
        "instance_type": "instanceType",
        "machine_type": "machineType",
    }

    disk: Optional[Union[int, Ref, GetAtt, Sub]] = None
    memory: Optional[Union[int, Ref, GetAtt, Sub]] = None
    v_cpu: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[str, MachineType, Ref, GetAtt, Sub]] = None


@dataclass
class FleetProxyRule(PropertyType):
    TYPE = "Type"
    EFFECT = "Effect"
    ENTITIES = "Entities"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "effect": "Effect",
        "entities": "Entities",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effect: Optional[Union[str, Ref, GetAtt, Sub]] = None
    entities: Optional[Union[list[str], Ref]] = None


@dataclass
class ProxyConfiguration(PropertyType):
    DEFAULT_BEHAVIOR = "DefaultBehavior"
    ORDERED_PROXY_RULES = "OrderedProxyRules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_behavior": "DefaultBehavior",
        "ordered_proxy_rules": "OrderedProxyRules",
    }

    default_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ordered_proxy_rules: Optional[list[FleetProxyRule]] = None


@dataclass
class ScalingConfigurationInput(PropertyType):
    TARGET_TRACKING_SCALING_CONFIGS = "TargetTrackingScalingConfigs"
    SCALING_TYPE = "ScalingType"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_tracking_scaling_configs": "TargetTrackingScalingConfigs",
        "scaling_type": "ScalingType",
        "max_capacity": "MaxCapacity",
    }

    target_tracking_scaling_configs: Optional[list[TargetTrackingScalingConfiguration]] = None
    scaling_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingScalingConfiguration(PropertyType):
    TARGET_VALUE = "TargetValue"
    METRIC_TYPE = "MetricType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
        "metric_type": "MetricType",
    }

    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metric_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    SUBNETS = "Subnets"
    VPC_ID = "VpcId"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "vpc_id": "VpcId",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

