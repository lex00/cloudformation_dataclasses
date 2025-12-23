"""PropertyTypes for AWS::Bedrock::Prompt."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CachePointBlock(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ChatPromptTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "messages": "Messages",
        "input_variables": "InputVariables",
        "tool_configuration": "ToolConfiguration",
        "system": "System",
    }

    messages: Optional[list[Message]] = None
    input_variables: Optional[list[PromptInputVariable]] = None
    tool_configuration: Optional[ToolConfiguration] = None
    system: Optional[list[SystemContentBlock]] = None


@dataclass
class ContentBlock(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_point": "CachePoint",
        "text": "Text",
    }

    cache_point: Optional[CachePointBlock] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Message(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "content": "Content",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content: Optional[list[ContentBlock]] = None


@dataclass
class PromptAgentResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_identifier": "AgentIdentifier",
    }

    agent_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptGenAiResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "agent": "Agent",
    }

    agent: Optional[PromptAgentResource] = None


@dataclass
class PromptInferenceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
    }

    text: Optional[PromptModelInferenceConfiguration] = None


@dataclass
class PromptInputVariable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptMetadataEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptModelInferenceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "temperature": "Temperature",
        "stop_sequences": "StopSequences",
        "max_tokens": "MaxTokens",
        "top_p": "TopP",
    }

    temperature: Optional[Union[float, Ref, GetAtt, Sub]] = None
    stop_sequences: Optional[Union[list[str], Ref]] = None
    max_tokens: Optional[Union[float, Ref, GetAtt, Sub]] = None
    top_p: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PromptTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "chat": "Chat",
        "text": "Text",
    }

    chat: Optional[ChatPromptTemplateConfiguration] = None
    text: Optional[TextPromptTemplateConfiguration] = None


@dataclass
class PromptVariant(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_model_request_fields": "AdditionalModelRequestFields",
        "inference_configuration": "InferenceConfiguration",
        "metadata": "Metadata",
        "gen_ai_resource": "GenAiResource",
        "template_configuration": "TemplateConfiguration",
        "template_type": "TemplateType",
        "model_id": "ModelId",
        "name": "Name",
    }

    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    inference_configuration: Optional[PromptInferenceConfiguration] = None
    metadata: Optional[list[PromptMetadataEntry]] = None
    gen_ai_resource: Optional[PromptGenAiResource] = None
    template_configuration: Optional[PromptTemplateConfiguration] = None
    template_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpecificToolChoice(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SystemContentBlock(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_point": "CachePoint",
        "text": "Text",
    }

    cache_point: Optional[CachePointBlock] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_variables": "InputVariables",
        "text_s3_location": "TextS3Location",
        "cache_point": "CachePoint",
        "text": "Text",
    }

    input_variables: Optional[list[PromptInputVariable]] = None
    text_s3_location: Optional[TextS3Location] = None
    cache_point: Optional[CachePointBlock] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TextS3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_point": "CachePoint",
        "tool_spec": "ToolSpec",
    }

    cache_point: Optional[CachePointBlock] = None
    tool_spec: Optional[ToolSpecification] = None


@dataclass
class ToolChoice(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto": "Auto",
        "any": "Any",
        "tool": "Tool",
    }

    auto: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    any: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    tool: Optional[SpecificToolChoice] = None


@dataclass
class ToolConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tool_choice": "ToolChoice",
        "tools": "Tools",
    }

    tool_choice: Optional[ToolChoice] = None
    tools: Optional[list[Tool]] = None


@dataclass
class ToolInputSchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "json": "Json",
    }

    json: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class ToolSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "input_schema": "InputSchema",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_schema: Optional[ToolInputSchema] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

