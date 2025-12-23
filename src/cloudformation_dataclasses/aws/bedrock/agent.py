"""PropertyTypes for AWS::Bedrock::Agent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class APISchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "payload": "Payload",
    }

    s3: Optional[S3Identifier] = None
    payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ActionGroupExecutor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_control": "CustomControl",
        "lambda_": "Lambda",
    }

    custom_control: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentActionGroup(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias_arn": "AliasArn",
    }

    alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentKnowledgeBase(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "executor": "Executor",
    }

    executor: Optional[OrchestrationExecutor] = None


@dataclass
class Function(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "functions": "Functions",
    }

    functions: Optional[list[Function]] = None


@dataclass
class GuardrailConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_identifier": "GuardrailIdentifier",
        "guardrail_version": "GuardrailVersion",
    }

    guardrail_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    guardrail_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_": "Lambda",
    }

    lambda_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterDetail(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_configurations": "PromptConfigurations",
        "override_lambda": "OverrideLambda",
    }

    prompt_configurations: Optional[list[PromptConfiguration]] = None
    override_lambda: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Identifier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_name": "S3BucketName",
        "s3_object_key": "S3ObjectKey",
    }

    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionSummaryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_recent_sessions": "MaxRecentSessions",
    }

    max_recent_sessions: Optional[Union[float, Ref, GetAtt, Sub]] = None

