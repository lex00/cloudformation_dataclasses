"""PropertyTypes for AWS::CodePipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_type_id": "ActionTypeId",
        "configuration": "Configuration",
        "output_artifacts": "OutputArtifacts",
        "output_variables": "OutputVariables",
        "namespace": "Namespace",
        "role_arn": "RoleArn",
        "name": "Name",
        "environment_variables": "EnvironmentVariables",
        "input_artifacts": "InputArtifacts",
        "commands": "Commands",
        "region": "Region",
        "run_order": "RunOrder",
        "timeout_in_minutes": "TimeoutInMinutes",
    }

    action_type_id: Optional[ActionTypeId] = None
    configuration: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    output_artifacts: Optional[list[OutputArtifact]] = None
    output_variables: Optional[Union[list[str], Ref]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment_variables: Optional[list[EnvironmentVariable]] = None
    input_artifacts: Optional[list[InputArtifact]] = None
    commands: Optional[Union[list[str], Ref]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    run_order: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ActionTypeId(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
        "category": "Category",
        "version": "Version",
        "provider": "Provider",
    }

    owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provider: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArtifactStore(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "encryption_key": "EncryptionKey",
        "location": "Location",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_key: Optional[EncryptionKey] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArtifactStoreMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "artifact_store": "ArtifactStore",
        "region": "Region",
    }

    artifact_store: Optional[ArtifactStore] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BeforeEntryConditions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditions": "Conditions",
    }

    conditions: Optional[list[Condition]] = None


@dataclass
class BlockerDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Condition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
        "result": "Result",
    }

    rules: Optional[list[RuleDeclaration]] = None
    result: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id": "Id",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class FailureConditions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_configuration": "RetryConfiguration",
        "conditions": "Conditions",
        "result": "Result",
    }

    retry_configuration: Optional[RetryConfiguration] = None
    conditions: Optional[list[Condition]] = None
    result: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GitBranchFilterCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "includes": "Includes",
        "excludes": "Excludes",
    }

    includes: Optional[Union[list[str], Ref]] = None
    excludes: Optional[Union[list[str], Ref]] = None


@dataclass
class GitConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pull_request": "PullRequest",
        "push": "Push",
        "source_action_name": "SourceActionName",
    }

    pull_request: Optional[list[GitPullRequestFilter]] = None
    push: Optional[list[GitPushFilter]] = None
    source_action_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GitFilePathFilterCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "includes": "Includes",
        "excludes": "Excludes",
    }

    includes: Optional[Union[list[str], Ref]] = None
    excludes: Optional[Union[list[str], Ref]] = None


@dataclass
class GitPullRequestFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_paths": "FilePaths",
        "events": "Events",
        "branches": "Branches",
    }

    file_paths: Optional[GitFilePathFilterCriteria] = None
    events: Optional[Union[list[str], Ref]] = None
    branches: Optional[GitBranchFilterCriteria] = None


@dataclass
class GitPushFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_paths": "FilePaths",
        "branches": "Branches",
        "tags": "Tags",
    }

    file_paths: Optional[GitFilePathFilterCriteria] = None
    branches: Optional[GitBranchFilterCriteria] = None
    tags: Optional[GitTagFilterCriteria] = None


@dataclass
class GitTagFilterCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "includes": "Includes",
        "excludes": "Excludes",
    }

    includes: Optional[Union[list[str], Ref]] = None
    excludes: Optional[Union[list[str], Ref]] = None


@dataclass
class InputArtifact(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputArtifact(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "files": "Files",
        "name": "Name",
    }

    files: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineTriggerDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "git_configuration": "GitConfiguration",
        "provider_type": "ProviderType",
    }

    git_configuration: Optional[GitConfiguration] = None
    provider_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_mode": "RetryMode",
    }

    retry_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_type_id": "RuleTypeId",
        "configuration": "Configuration",
        "input_artifacts": "InputArtifacts",
        "commands": "Commands",
        "region": "Region",
        "role_arn": "RoleArn",
        "name": "Name",
    }

    rule_type_id: Optional[RuleTypeId] = None
    configuration: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    input_artifacts: Optional[list[InputArtifact]] = None
    commands: Optional[Union[list[str], Ref]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleTypeId(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
        "category": "Category",
        "version": "Version",
        "provider": "Provider",
    }

    owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provider: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StageDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "blockers": "Blockers",
        "actions": "Actions",
        "before_entry": "BeforeEntry",
        "on_success": "OnSuccess",
        "name": "Name",
        "on_failure": "OnFailure",
    }

    blockers: Optional[list[BlockerDeclaration]] = None
    actions: Optional[list[ActionDeclaration]] = None
    before_entry: Optional[BeforeEntryConditions] = None
    on_success: Optional[SuccessConditions] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_failure: Optional[FailureConditions] = None


@dataclass
class StageTransition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stage_name": "StageName",
        "reason": "Reason",
    }

    stage_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SuccessConditions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditions": "Conditions",
    }

    conditions: Optional[list[Condition]] = None


@dataclass
class VariableDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "description": "Description",
        "name": "Name",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

