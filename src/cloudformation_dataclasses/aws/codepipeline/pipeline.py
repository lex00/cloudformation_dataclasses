"""PropertyTypes for AWS::CodePipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionDeclaration(PropertyType):
    ACTION_TYPE_ID = "ActionTypeId"
    CONFIGURATION = "Configuration"
    OUTPUT_ARTIFACTS = "OutputArtifacts"
    OUTPUT_VARIABLES = "OutputVariables"
    NAMESPACE = "Namespace"
    ROLE_ARN = "RoleArn"
    NAME = "Name"
    ENVIRONMENT_VARIABLES = "EnvironmentVariables"
    INPUT_ARTIFACTS = "InputArtifacts"
    COMMANDS = "Commands"
    REGION = "Region"
    RUN_ORDER = "RunOrder"
    TIMEOUT_IN_MINUTES = "TimeoutInMinutes"

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
    OWNER = "Owner"
    CATEGORY = "Category"
    VERSION = "Version"
    PROVIDER = "Provider"

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
    TYPE = "Type"
    ENCRYPTION_KEY = "EncryptionKey"
    LOCATION = "Location"

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
    ARTIFACT_STORE = "ArtifactStore"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "artifact_store": "ArtifactStore",
        "region": "Region",
    }

    artifact_store: Optional[ArtifactStore] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BeforeEntryConditions(PropertyType):
    CONDITIONS = "Conditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "conditions": "Conditions",
    }

    conditions: Optional[list[Condition]] = None


@dataclass
class BlockerDeclaration(PropertyType):
    TYPE = "Type"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Condition(PropertyType):
    RULES = "Rules"
    RESULT = "Result"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
        "result": "Result",
    }

    rules: Optional[list[RuleDeclaration]] = None
    result: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionKey(PropertyType):
    TYPE = "Type"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id": "Id",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class FailureConditions(PropertyType):
    RETRY_CONFIGURATION = "RetryConfiguration"
    CONDITIONS = "Conditions"
    RESULT = "Result"

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
    INCLUDES = "Includes"
    EXCLUDES = "Excludes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "includes": "Includes",
        "excludes": "Excludes",
    }

    includes: Optional[Union[list[str], Ref]] = None
    excludes: Optional[Union[list[str], Ref]] = None


@dataclass
class GitConfiguration(PropertyType):
    PULL_REQUEST = "PullRequest"
    PUSH = "Push"
    SOURCE_ACTION_NAME = "SourceActionName"

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
    INCLUDES = "Includes"
    EXCLUDES = "Excludes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "includes": "Includes",
        "excludes": "Excludes",
    }

    includes: Optional[Union[list[str], Ref]] = None
    excludes: Optional[Union[list[str], Ref]] = None


@dataclass
class GitPullRequestFilter(PropertyType):
    FILE_PATHS = "FilePaths"
    EVENTS = "Events"
    BRANCHES = "Branches"

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
    FILE_PATHS = "FilePaths"
    BRANCHES = "Branches"
    TAGS = "Tags"

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
    INCLUDES = "Includes"
    EXCLUDES = "Excludes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "includes": "Includes",
        "excludes": "Excludes",
    }

    includes: Optional[Union[list[str], Ref]] = None
    excludes: Optional[Union[list[str], Ref]] = None


@dataclass
class InputArtifact(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputArtifact(PropertyType):
    FILES = "Files"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "files": "Files",
        "name": "Name",
    }

    files: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineTriggerDeclaration(PropertyType):
    GIT_CONFIGURATION = "GitConfiguration"
    PROVIDER_TYPE = "ProviderType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "git_configuration": "GitConfiguration",
        "provider_type": "ProviderType",
    }

    git_configuration: Optional[GitConfiguration] = None
    provider_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetryConfiguration(PropertyType):
    RETRY_MODE = "RetryMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_mode": "RetryMode",
    }

    retry_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleDeclaration(PropertyType):
    RULE_TYPE_ID = "RuleTypeId"
    CONFIGURATION = "Configuration"
    INPUT_ARTIFACTS = "InputArtifacts"
    COMMANDS = "Commands"
    REGION = "Region"
    ROLE_ARN = "RoleArn"
    NAME = "Name"

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
    OWNER = "Owner"
    CATEGORY = "Category"
    VERSION = "Version"
    PROVIDER = "Provider"

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
    BLOCKERS = "Blockers"
    ACTIONS = "Actions"
    BEFORE_ENTRY = "BeforeEntry"
    ON_SUCCESS = "OnSuccess"
    NAME = "Name"
    ON_FAILURE = "OnFailure"

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
    STAGE_NAME = "StageName"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stage_name": "StageName",
        "reason": "Reason",
    }

    stage_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SuccessConditions(PropertyType):
    CONDITIONS = "Conditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "conditions": "Conditions",
    }

    conditions: Optional[list[Condition]] = None


@dataclass
class VariableDeclaration(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    DESCRIPTION = "Description"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "description": "Description",
        "name": "Name",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

