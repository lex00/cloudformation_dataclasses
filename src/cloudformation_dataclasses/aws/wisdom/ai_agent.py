"""PropertyTypes for AWS::Wisdom::AIAgent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "manual_search_ai_agent_configuration": "ManualSearchAIAgentConfiguration",
        "email_overview_ai_agent_configuration": "EmailOverviewAIAgentConfiguration",
        "self_service_ai_agent_configuration": "SelfServiceAIAgentConfiguration",
        "email_response_ai_agent_configuration": "EmailResponseAIAgentConfiguration",
        "answer_recommendation_ai_agent_configuration": "AnswerRecommendationAIAgentConfiguration",
        "email_generative_answer_ai_agent_configuration": "EmailGenerativeAnswerAIAgentConfiguration",
    }

    manual_search_ai_agent_configuration: Optional[ManualSearchAIAgentConfiguration] = None
    email_overview_ai_agent_configuration: Optional[EmailOverviewAIAgentConfiguration] = None
    self_service_ai_agent_configuration: Optional[SelfServiceAIAgentConfiguration] = None
    email_response_ai_agent_configuration: Optional[EmailResponseAIAgentConfiguration] = None
    answer_recommendation_ai_agent_configuration: Optional[AnswerRecommendationAIAgentConfiguration] = None
    email_generative_answer_ai_agent_configuration: Optional[EmailGenerativeAnswerAIAgentConfiguration] = None


@dataclass
class AnswerRecommendationAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale": "Locale",
        "answer_generation_ai_prompt_id": "AnswerGenerationAIPromptId",
        "intent_labeling_generation_ai_prompt_id": "IntentLabelingGenerationAIPromptId",
        "query_reformulation_ai_prompt_id": "QueryReformulationAIPromptId",
        "answer_generation_ai_guardrail_id": "AnswerGenerationAIGuardrailId",
        "association_configurations": "AssociationConfigurations",
    }

    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    answer_generation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    intent_labeling_generation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_reformulation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    answer_generation_ai_guardrail_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_configurations: Optional[list[AssociationConfiguration]] = None


@dataclass
class AssociationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "association_type": "AssociationType",
        "association_configuration_data": "AssociationConfigurationData",
        "association_id": "AssociationId",
    }

    association_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_configuration_data: Optional[AssociationConfigurationData] = None
    association_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssociationConfigurationData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "knowledge_base_association_configuration_data": "KnowledgeBaseAssociationConfigurationData",
    }

    knowledge_base_association_configuration_data: Optional[KnowledgeBaseAssociationConfigurationData] = None


@dataclass
class EmailGenerativeAnswerAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "email_generative_answer_ai_prompt_id": "EmailGenerativeAnswerAIPromptId",
        "locale": "Locale",
        "email_query_reformulation_ai_prompt_id": "EmailQueryReformulationAIPromptId",
        "association_configurations": "AssociationConfigurations",
    }

    email_generative_answer_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_query_reformulation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_configurations: Optional[list[AssociationConfiguration]] = None


@dataclass
class EmailOverviewAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale": "Locale",
        "email_overview_ai_prompt_id": "EmailOverviewAIPromptId",
    }

    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_overview_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmailResponseAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale": "Locale",
        "email_response_ai_prompt_id": "EmailResponseAIPromptId",
        "email_query_reformulation_ai_prompt_id": "EmailQueryReformulationAIPromptId",
        "association_configurations": "AssociationConfigurations",
    }

    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_response_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_query_reformulation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_configurations: Optional[list[AssociationConfiguration]] = None


@dataclass
class KnowledgeBaseAssociationConfigurationData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_results": "MaxResults",
        "content_tag_filter": "ContentTagFilter",
        "override_knowledge_base_search_type": "OverrideKnowledgeBaseSearchType",
    }

    max_results: Optional[Union[float, Ref, GetAtt, Sub]] = None
    content_tag_filter: Optional[TagFilter] = None
    override_knowledge_base_search_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManualSearchAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale": "Locale",
        "answer_generation_ai_prompt_id": "AnswerGenerationAIPromptId",
        "answer_generation_ai_guardrail_id": "AnswerGenerationAIGuardrailId",
        "association_configurations": "AssociationConfigurations",
    }

    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    answer_generation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    answer_generation_ai_guardrail_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_configurations: Optional[list[AssociationConfiguration]] = None


@dataclass
class OrCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "and_conditions": "AndConditions",
        "tag_condition": "TagCondition",
    }

    and_conditions: Optional[list[TagCondition]] = None
    tag_condition: Optional[TagCondition] = None


@dataclass
class SelfServiceAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "self_service_ai_guardrail_id": "SelfServiceAIGuardrailId",
        "self_service_pre_processing_ai_prompt_id": "SelfServicePreProcessingAIPromptId",
        "self_service_answer_generation_ai_prompt_id": "SelfServiceAnswerGenerationAIPromptId",
        "association_configurations": "AssociationConfigurations",
    }

    self_service_ai_guardrail_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    self_service_pre_processing_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    self_service_answer_generation_ai_prompt_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_configurations: Optional[list[AssociationConfiguration]] = None


@dataclass
class TagCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "or_conditions": "OrConditions",
        "and_conditions": "AndConditions",
        "tag_condition": "TagCondition",
    }

    or_conditions: Optional[list[OrCondition]] = None
    and_conditions: Optional[list[TagCondition]] = None
    tag_condition: Optional[TagCondition] = None

