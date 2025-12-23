"""PropertyTypes for AWS::Bedrock::Flow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AgentFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_alias_arn": "AgentAliasArn",
    }

    agent_alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditions": "Conditions",
    }

    conditions: Optional[list[FlowCondition]] = None


@dataclass
class FieldForReranking(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_name": "FieldName",
    }

    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "name": "Name",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowConditionalConnectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowConnection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "target": "Target",
        "configuration": "Configuration",
        "source": "Source",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration: Optional[FlowConnectionConfiguration] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowConnectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data": "Data",
        "conditional": "Conditional",
    }

    data: Optional[FlowDataConnectionConfiguration] = None
    conditional: Optional[FlowConditionalConnectionConfiguration] = None


@dataclass
class FlowDataConnectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_output": "SourceOutput",
        "target_input": "TargetInput",
    }

    source_output: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_input: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connections": "Connections",
        "nodes": "Nodes",
    }

    connections: Optional[list[FlowConnection]] = None
    nodes: Optional[list[FlowNode]] = None


@dataclass
class FlowNode(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "configuration": "Configuration",
        "outputs": "Outputs",
        "inputs": "Inputs",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration: Optional[FlowNodeConfiguration] = None
    outputs: Optional[list[FlowNodeOutput]] = None
    inputs: Optional[list[FlowNodeInput]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "retrieval": "Retrieval",
        "loop": "Loop",
        "agent": "Agent",
        "lambda_function": "LambdaFunction",
        "inline_code": "InlineCode",
        "loop_controller": "LoopController",
        "input": "Input",
        "storage": "Storage",
        "knowledge_base": "KnowledgeBase",
        "output": "Output",
        "iterator": "Iterator",
        "collector": "Collector",
        "loop_input": "LoopInput",
        "prompt": "Prompt",
        "lex": "Lex",
    }

    condition: Optional[ConditionFlowNodeConfiguration] = None
    retrieval: Optional[RetrievalFlowNodeConfiguration] = None
    loop: Optional[LoopFlowNodeConfiguration] = None
    agent: Optional[AgentFlowNodeConfiguration] = None
    lambda_function: Optional[LambdaFunctionFlowNodeConfiguration] = None
    inline_code: Optional[InlineCodeFlowNodeConfiguration] = None
    loop_controller: Optional[LoopControllerFlowNodeConfiguration] = None
    input: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    storage: Optional[StorageFlowNodeConfiguration] = None
    knowledge_base: Optional[KnowledgeBaseFlowNodeConfiguration] = None
    output: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    iterator: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    collector: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    loop_input: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    prompt: Optional[PromptFlowNodeConfiguration] = None
    lex: Optional[LexFlowNodeConfiguration] = None


@dataclass
class FlowNodeInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "category": "Category",
        "expression": "Expression",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowNodeOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowValidation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_identifier": "GuardrailIdentifier",
        "guardrail_version": "GuardrailVersion",
    }

    guardrail_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    guardrail_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InlineCodeFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "language": "Language",
        "code": "Code",
    }

    language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "orchestration_configuration": "OrchestrationConfiguration",
        "guardrail_configuration": "GuardrailConfiguration",
        "inference_configuration": "InferenceConfiguration",
        "knowledge_base_id": "KnowledgeBaseId",
        "prompt_template": "PromptTemplate",
        "reranking_configuration": "RerankingConfiguration",
        "number_of_results": "NumberOfResults",
        "model_id": "ModelId",
    }

    orchestration_configuration: Optional[KnowledgeBaseOrchestrationConfiguration] = None
    guardrail_configuration: Optional[GuardrailConfiguration] = None
    inference_configuration: Optional[PromptInferenceConfiguration] = None
    knowledge_base_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prompt_template: Optional[KnowledgeBasePromptTemplate] = None
    reranking_configuration: Optional[VectorSearchRerankingConfiguration] = None
    number_of_results: Optional[Union[float, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseOrchestrationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_config": "InferenceConfig",
        "additional_model_request_fields": "AdditionalModelRequestFields",
        "performance_config": "PerformanceConfig",
        "prompt_template": "PromptTemplate",
    }

    inference_config: Optional[PromptInferenceConfiguration] = None
    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    performance_config: Optional[PerformanceConfiguration] = None
    prompt_template: Optional[KnowledgeBasePromptTemplate] = None


@dataclass
class KnowledgeBasePromptTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_prompt_template": "TextPromptTemplate",
    }

    text_prompt_template: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaFunctionFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LexFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bot_alias_arn": "BotAliasArn",
        "locale_id": "LocaleId",
    }

    bot_alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    locale_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoopControllerFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "continue_condition": "ContinueCondition",
        "max_iterations": "MaxIterations",
    }

    continue_condition: Optional[FlowCondition] = None
    max_iterations: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LoopFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
    }

    definition: Optional[FlowDefinition] = None


@dataclass
class MetadataConfigurationForReranking(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selective_mode_configuration": "SelectiveModeConfiguration",
        "selection_mode": "SelectionMode",
    }

    selective_mode_configuration: Optional[RerankingMetadataSelectiveModeConfiguration] = None
    selection_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PerformanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "latency": "Latency",
    }

    latency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_configuration": "GuardrailConfiguration",
        "source_configuration": "SourceConfiguration",
    }

    guardrail_configuration: Optional[GuardrailConfiguration] = None
    source_configuration: Optional[PromptFlowNodeSourceConfiguration] = None


@dataclass
class PromptFlowNodeInlineConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_configuration": "InferenceConfiguration",
        "template_configuration": "TemplateConfiguration",
        "template_type": "TemplateType",
        "model_id": "ModelId",
    }

    inference_configuration: Optional[PromptInferenceConfiguration] = None
    template_configuration: Optional[PromptTemplateConfiguration] = None
    template_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptFlowNodeResourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_arn": "PromptArn",
    }

    prompt_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptFlowNodeSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource": "Resource",
        "inline": "Inline",
    }

    resource: Optional[PromptFlowNodeResourceConfiguration] = None
    inline: Optional[PromptFlowNodeInlineConfiguration] = None


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
        "text": "Text",
    }

    text: Optional[TextPromptTemplateConfiguration] = None


@dataclass
class RerankingMetadataSelectiveModeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fields_to_include": "FieldsToInclude",
        "fields_to_exclude": "FieldsToExclude",
    }

    fields_to_include: Optional[list[FieldForReranking]] = None
    fields_to_exclude: Optional[list[FieldForReranking]] = None


@dataclass
class RetrievalFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_configuration": "ServiceConfiguration",
    }

    service_configuration: Optional[RetrievalFlowNodeServiceConfiguration] = None


@dataclass
class RetrievalFlowNodeS3Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetrievalFlowNodeServiceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[RetrievalFlowNodeS3Configuration] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageFlowNodeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_configuration": "ServiceConfiguration",
    }

    service_configuration: Optional[StorageFlowNodeServiceConfiguration] = None


@dataclass
class StorageFlowNodeS3Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageFlowNodeServiceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[StorageFlowNodeS3Configuration] = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_variables": "InputVariables",
        "text": "Text",
    }

    input_variables: Optional[list[PromptInputVariable]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VectorSearchBedrockRerankingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_reranked_results": "NumberOfRerankedResults",
        "metadata_configuration": "MetadataConfiguration",
        "model_configuration": "ModelConfiguration",
    }

    number_of_reranked_results: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metadata_configuration: Optional[MetadataConfigurationForReranking] = None
    model_configuration: Optional[VectorSearchBedrockRerankingModelConfiguration] = None


@dataclass
class VectorSearchBedrockRerankingModelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
        "additional_model_request_fields": "AdditionalModelRequestFields",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class VectorSearchRerankingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "bedrock_reranking_configuration": "BedrockRerankingConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_reranking_configuration: Optional[VectorSearchBedrockRerankingConfiguration] = None

