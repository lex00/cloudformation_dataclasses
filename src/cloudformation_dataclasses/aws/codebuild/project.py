"""PropertyTypes for AWS::CodeBuild::Project."""

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
class Artifacts(PropertyType):
    PATH = "Path"
    TYPE = "Type"
    ARTIFACT_IDENTIFIER = "ArtifactIdentifier"
    OVERRIDE_ARTIFACT_NAME = "OverrideArtifactName"
    PACKAGING = "Packaging"
    ENCRYPTION_DISABLED = "EncryptionDisabled"
    LOCATION = "Location"
    NAME = "Name"
    NAMESPACE_TYPE = "NamespaceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "type_": "Type",
        "artifact_identifier": "ArtifactIdentifier",
        "override_artifact_name": "OverrideArtifactName",
        "packaging": "Packaging",
        "encryption_disabled": "EncryptionDisabled",
        "location": "Location",
        "name": "Name",
        "namespace_type": "NamespaceType",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    artifact_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override_artifact_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    packaging: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BatchRestrictions(PropertyType):
    COMPUTE_TYPES_ALLOWED = "ComputeTypesAllowed"
    MAXIMUM_BUILDS_ALLOWED = "MaximumBuildsAllowed"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_types_allowed": "ComputeTypesAllowed",
        "maximum_builds_allowed": "MaximumBuildsAllowed",
    }

    compute_types_allowed: Optional[Union[list[str], Ref]] = None
    maximum_builds_allowed: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BuildStatusConfig(PropertyType):
    CONTEXT = "Context"
    TARGET_URL = "TargetUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "context": "Context",
        "target_url": "TargetUrl",
    }

    context: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogsConfig(PropertyType):
    STATUS = "Status"
    GROUP_NAME = "GroupName"
    STREAM_NAME = "StreamName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "group_name": "GroupName",
        "stream_name": "StreamName",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DockerServer(PropertyType):
    COMPUTE_TYPE = "ComputeType"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_type": "ComputeType",
        "security_group_ids": "SecurityGroupIds",
    }

    compute_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class Environment(PropertyType):
    TYPE = "Type"
    ENVIRONMENT_VARIABLES = "EnvironmentVariables"
    FLEET = "Fleet"
    PRIVILEGED_MODE = "PrivilegedMode"
    IMAGE_PULL_CREDENTIALS_TYPE = "ImagePullCredentialsType"
    IMAGE = "Image"
    REGISTRY_CREDENTIAL = "RegistryCredential"
    COMPUTE_TYPE = "ComputeType"
    DOCKER_SERVER = "DockerServer"
    CERTIFICATE = "Certificate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "environment_variables": "EnvironmentVariables",
        "fleet": "Fleet",
        "privileged_mode": "PrivilegedMode",
        "image_pull_credentials_type": "ImagePullCredentialsType",
        "image": "Image",
        "registry_credential": "RegistryCredential",
        "compute_type": "ComputeType",
        "docker_server": "DockerServer",
        "certificate": "Certificate",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment_variables: Optional[list[EnvironmentVariable]] = None
    fleet: Optional[ProjectFleet] = None
    privileged_mode: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    image_pull_credentials_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    registry_credential: Optional[RegistryCredential] = None
    compute_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    docker_server: Optional[DockerServer] = None
    certificate: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentVariable(PropertyType):
    TYPE = "Type"
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterGroup(PropertyType):
    pass


@dataclass
class GitSubmodulesConfig(PropertyType):
    FETCH_SUBMODULES = "FetchSubmodules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fetch_submodules": "FetchSubmodules",
    }

    fetch_submodules: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LogsConfig(PropertyType):
    CLOUD_WATCH_LOGS = "CloudWatchLogs"
    S3_LOGS = "S3Logs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs": "CloudWatchLogs",
        "s3_logs": "S3Logs",
    }

    cloud_watch_logs: Optional[CloudWatchLogsConfig] = None
    s3_logs: Optional[S3LogsConfig] = None


@dataclass
class ProjectBuildBatchConfig(PropertyType):
    COMBINE_ARTIFACTS = "CombineArtifacts"
    SERVICE_ROLE = "ServiceRole"
    BATCH_REPORT_MODE = "BatchReportMode"
    TIMEOUT_IN_MINS = "TimeoutInMins"
    RESTRICTIONS = "Restrictions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "combine_artifacts": "CombineArtifacts",
        "service_role": "ServiceRole",
        "batch_report_mode": "BatchReportMode",
        "timeout_in_mins": "TimeoutInMins",
        "restrictions": "Restrictions",
    }

    combine_artifacts: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    service_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    batch_report_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_in_mins: Optional[Union[int, Ref, GetAtt, Sub]] = None
    restrictions: Optional[BatchRestrictions] = None


@dataclass
class ProjectCache(PropertyType):
    MODES = "Modes"
    TYPE = "Type"
    CACHE_NAMESPACE = "CacheNamespace"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "modes": "Modes",
        "type_": "Type",
        "cache_namespace": "CacheNamespace",
        "location": "Location",
    }

    modes: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cache_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectFileSystemLocation(PropertyType):
    MOUNT_POINT = "MountPoint"
    TYPE = "Type"
    IDENTIFIER = "Identifier"
    MOUNT_OPTIONS = "MountOptions"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_point": "MountPoint",
        "type_": "Type",
        "identifier": "Identifier",
        "mount_options": "MountOptions",
        "location": "Location",
    }

    mount_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mount_options: Optional[Union[str, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectFleet(PropertyType):
    FLEET_ARN = "FleetArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fleet_arn": "FleetArn",
    }

    fleet_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectSourceVersion(PropertyType):
    SOURCE_IDENTIFIER = "SourceIdentifier"
    SOURCE_VERSION = "SourceVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_identifier": "SourceIdentifier",
        "source_version": "SourceVersion",
    }

    source_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectTriggers(PropertyType):
    FILTER_GROUPS = "FilterGroups"
    BUILD_TYPE = "BuildType"
    WEBHOOK = "Webhook"
    SCOPE_CONFIGURATION = "ScopeConfiguration"
    PULL_REQUEST_BUILD_POLICY = "PullRequestBuildPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_groups": "FilterGroups",
        "build_type": "BuildType",
        "webhook": "Webhook",
        "scope_configuration": "ScopeConfiguration",
        "pull_request_build_policy": "PullRequestBuildPolicy",
    }

    filter_groups: Optional[list[FilterGroup]] = None
    build_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    webhook: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scope_configuration: Optional[ScopeConfiguration] = None
    pull_request_build_policy: Optional[PullRequestBuildPolicy] = None


@dataclass
class PullRequestBuildPolicy(PropertyType):
    REQUIRES_COMMENT_APPROVAL = "RequiresCommentApproval"
    APPROVER_ROLES = "ApproverRoles"

    _property_mappings: ClassVar[dict[str, str]] = {
        "requires_comment_approval": "RequiresCommentApproval",
        "approver_roles": "ApproverRoles",
    }

    requires_comment_approval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    approver_roles: Optional[Union[list[str], Ref]] = None


@dataclass
class RegistryCredential(PropertyType):
    CREDENTIAL = "Credential"
    CREDENTIAL_PROVIDER = "CredentialProvider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credential": "Credential",
        "credential_provider": "CredentialProvider",
    }

    credential: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3LogsConfig(PropertyType):
    STATUS = "Status"
    ENCRYPTION_DISABLED = "EncryptionDisabled"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "encryption_disabled": "EncryptionDisabled",
        "location": "Location",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScopeConfiguration(PropertyType):
    SCOPE = "Scope"
    DOMAIN = "Domain"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "domain": "Domain",
        "name": "Name",
    }

    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    TYPE = "Type"
    REPORT_BUILD_STATUS = "ReportBuildStatus"
    AUTH = "Auth"
    SOURCE_IDENTIFIER = "SourceIdentifier"
    BUILD_SPEC = "BuildSpec"
    GIT_CLONE_DEPTH = "GitCloneDepth"
    BUILD_STATUS_CONFIG = "BuildStatusConfig"
    GIT_SUBMODULES_CONFIG = "GitSubmodulesConfig"
    INSECURE_SSL = "InsecureSsl"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "report_build_status": "ReportBuildStatus",
        "auth": "Auth",
        "source_identifier": "SourceIdentifier",
        "build_spec": "BuildSpec",
        "git_clone_depth": "GitCloneDepth",
        "build_status_config": "BuildStatusConfig",
        "git_submodules_config": "GitSubmodulesConfig",
        "insecure_ssl": "InsecureSsl",
        "location": "Location",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    report_build_status: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    auth: Optional[SourceAuth] = None
    source_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    build_spec: Optional[Union[str, Ref, GetAtt, Sub]] = None
    git_clone_depth: Optional[Union[int, Ref, GetAtt, Sub]] = None
    build_status_config: Optional[BuildStatusConfig] = None
    git_submodules_config: Optional[GitSubmodulesConfig] = None
    insecure_ssl: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceAuth(PropertyType):
    TYPE = "Type"
    RESOURCE = "Resource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "resource": "Resource",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None


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


@dataclass
class WebhookFilter(PropertyType):
    PATTERN = "Pattern"
    TYPE = "Type"
    EXCLUDE_MATCHED_PATTERN = "ExcludeMatchedPattern"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
        "type_": "Type",
        "exclude_matched_pattern": "ExcludeMatchedPattern",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_matched_pattern: Optional[Union[bool, Ref, GetAtt, Sub]] = None

