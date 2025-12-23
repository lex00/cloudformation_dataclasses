"""PropertyTypes for AWS::Bedrock::Agent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class APISchema(PropertyType):
    S3 = "S3"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "payload": "Payload",
    }

    s3: Optional[S3Identifier] = None
    payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ActionGroupExecutor(PropertyType):
    CUSTOM_CONTROL = "CustomControl"
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_control": "CustomControl",
        "lambda_": "Lambda",
    }

    custom_control: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentActionGroup(PropertyType):
    DESCRIPTION = "Description"
    API_SCHEMA = "ApiSchema"
    FUNCTION_SCHEMA = "FunctionSchema"
    SKIP_RESOURCE_IN_USE_CHECK_ON_DELETE = "SkipResourceInUseCheckOnDelete"
    PARENT_ACTION_GROUP_SIGNATURE = "ParentActionGroupSignature"
    ACTION_GROUP_EXECUTOR = "ActionGroupExecutor"
    ACTION_GROUP_NAME = "ActionGroupName"
    ACTION_GROUP_STATE = "ActionGroupState"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "api_schema": "ApiSchema",
        "function_schema": "FunctionSchema",
        "skip_resource_in_use_check_on_delete": "SkipResourceInUseCheckOnDelete",
        "parent_action_group_signature": "ParentActionGroupSignature",
        "action_group_executor": "ActionGroupExecutor",
        "action_group_name": "ActionGroupName",
        "action_group_state": "ActionGroupState",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_schema: Optional[APISchema] = None
    function_schema: Optional[FunctionSchema] = None
    skip_resource_in_use_check_on_delete: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    parent_action_group_signature: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_group_executor: Optional[ActionGroupExecutor] = None
    action_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_group_state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentCollaborator(PropertyType):
    AGENT_DESCRIPTOR = "AgentDescriptor"
    COLLABORATION_INSTRUCTION = "CollaborationInstruction"
    RELAY_CONVERSATION_HISTORY = "RelayConversationHistory"
    COLLABORATOR_NAME = "CollaboratorName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_descriptor": "AgentDescriptor",
        "collaboration_instruction": "CollaborationInstruction",
        "relay_conversation_history": "RelayConversationHistory",
        "collaborator_name": "CollaboratorName",
    }

    agent_descriptor: Optional[AgentDescriptor] = None
    collaboration_instruction: Optional[Union[str, Ref, GetAtt, Sub]] = None
    relay_conversation_history: Optional[Union[str, Ref, GetAtt, Sub]] = None
    collaborator_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentDescriptor(PropertyType):
    ALIAS_ARN = "AliasArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias_arn": "AliasArn",
    }

    alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentKnowledgeBase(PropertyType):
    DESCRIPTION = "Description"
    KNOWLEDGE_BASE_STATE = "KnowledgeBaseState"
    KNOWLEDGE_BASE_ID = "KnowledgeBaseId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "knowledge_base_state": "KnowledgeBaseState",
        "knowledge_base_id": "KnowledgeBaseId",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    knowledge_base_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    knowledge_base_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomOrchestration(PropertyType):
    EXECUTOR = "Executor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "executor": "Executor",
    }

    executor: Optional[OrchestrationExecutor] = None


@dataclass
class Function(PropertyType):
    DESCRIPTION = "Description"
    PARAMETERS = "Parameters"
    REQUIRE_CONFIRMATION = "RequireConfirmation"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "parameters": "Parameters",
        "require_confirmation": "RequireConfirmation",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[dict[str, Any]] = None
    require_confirmation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FunctionSchema(PropertyType):
    FUNCTIONS = "Functions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "functions": "Functions",
    }

    functions: Optional[list[Function]] = None


@dataclass
class GuardrailConfiguration(PropertyType):
    GUARDRAIL_IDENTIFIER = "GuardrailIdentifier"
    GUARDRAIL_VERSION = "GuardrailVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_identifier": "GuardrailIdentifier",
        "guardrail_version": "GuardrailVersion",
    }

    guardrail_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    guardrail_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceConfiguration(PropertyType):
    TOP_K = "TopK"
    TEMPERATURE = "Temperature"
    MAXIMUM_LENGTH = "MaximumLength"
    STOP_SEQUENCES = "StopSequences"
    TOP_P = "TopP"

    _property_mappings: ClassVar[dict[str, str]] = {
        "top_k": "TopK",
        "temperature": "Temperature",
        "maximum_length": "MaximumLength",
        "stop_sequences": "StopSequences",
        "top_p": "TopP",
    }

    top_k: Optional[Union[float, Ref, GetAtt, Sub]] = None
    temperature: Optional[Union[float, Ref, GetAtt, Sub]] = None
    maximum_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    stop_sequences: Optional[Union[list[str], Ref]] = None
    top_p: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryConfiguration(PropertyType):
    SESSION_SUMMARY_CONFIGURATION = "SessionSummaryConfiguration"
    ENABLED_MEMORY_TYPES = "EnabledMemoryTypes"
    STORAGE_DAYS = "StorageDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_summary_configuration": "SessionSummaryConfiguration",
        "enabled_memory_types": "EnabledMemoryTypes",
        "storage_days": "StorageDays",
    }

    session_summary_configuration: Optional[SessionSummaryConfiguration] = None
    enabled_memory_types: Optional[Union[list[str], Ref]] = None
    storage_days: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OrchestrationExecutor(PropertyType):
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_": "Lambda",
    }

    lambda_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterDetail(PropertyType):
    TYPE = "Type"
    DESCRIPTION = "Description"
    REQUIRED = "Required"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "required": "Required",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PromptConfiguration(PropertyType):
    PROMPT_TYPE = "PromptType"
    PROMPT_STATE = "PromptState"
    ADDITIONAL_MODEL_REQUEST_FIELDS = "AdditionalModelRequestFields"
    BASE_PROMPT_TEMPLATE = "BasePromptTemplate"
    FOUNDATION_MODEL = "FoundationModel"
    INFERENCE_CONFIGURATION = "InferenceConfiguration"
    PROMPT_CREATION_MODE = "PromptCreationMode"
    PARSER_MODE = "ParserMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_type": "PromptType",
        "prompt_state": "PromptState",
        "additional_model_request_fields": "AdditionalModelRequestFields",
        "base_prompt_template": "BasePromptTemplate",
        "foundation_model": "FoundationModel",
        "inference_configuration": "InferenceConfiguration",
        "prompt_creation_mode": "PromptCreationMode",
        "parser_mode": "ParserMode",
    }

    prompt_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prompt_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    base_prompt_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    foundation_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inference_configuration: Optional[InferenceConfiguration] = None
    prompt_creation_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parser_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptOverrideConfiguration(PropertyType):
    PROMPT_CONFIGURATIONS = "PromptConfigurations"
    OVERRIDE_LAMBDA = "OverrideLambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_configurations": "PromptConfigurations",
        "override_lambda": "OverrideLambda",
    }

    prompt_configurations: Optional[list[PromptConfiguration]] = None
    override_lambda: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Identifier(PropertyType):
    S3_BUCKET_NAME = "S3BucketName"
    S3_OBJECT_KEY = "S3ObjectKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_name": "S3BucketName",
        "s3_object_key": "S3ObjectKey",
    }

    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionSummaryConfiguration(PropertyType):
    MAX_RECENT_SESSIONS = "MaxRecentSessions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_recent_sessions": "MaxRecentSessions",
    }

    max_recent_sessions: Optional[Union[float, Ref, GetAtt, Sub]] = None

