"""PropertyTypes for AWS::CodeBuild::Project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Artifacts(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_types_allowed": "ComputeTypesAllowed",
        "maximum_builds_allowed": "MaximumBuildsAllowed",
    }

    compute_types_allowed: Optional[Union[list[str], Ref]] = None
    maximum_builds_allowed: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BuildStatusConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "context": "Context",
        "target_url": "TargetUrl",
    }

    context: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogsConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_type": "ComputeType",
        "security_group_ids": "SecurityGroupIds",
    }

    compute_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class Environment(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "fetch_submodules": "FetchSubmodules",
    }

    fetch_submodules: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LogsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs": "CloudWatchLogs",
        "s3_logs": "S3Logs",
    }

    cloud_watch_logs: Optional[CloudWatchLogsConfig] = None
    s3_logs: Optional[S3LogsConfig] = None


@dataclass
class ProjectBuildBatchConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "fleet_arn": "FleetArn",
    }

    fleet_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectSourceVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_identifier": "SourceIdentifier",
        "source_version": "SourceVersion",
    }

    source_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectTriggers(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "requires_comment_approval": "RequiresCommentApproval",
        "approver_roles": "ApproverRoles",
    }

    requires_comment_approval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    approver_roles: Optional[Union[list[str], Ref]] = None


@dataclass
class RegistryCredential(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "credential": "Credential",
        "credential_provider": "CredentialProvider",
    }

    credential: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3LogsConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "resource": "Resource",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
        "type_": "Type",
        "exclude_matched_pattern": "ExcludeMatchedPattern",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_matched_pattern: Optional[Union[bool, Ref, GetAtt, Sub]] = None

