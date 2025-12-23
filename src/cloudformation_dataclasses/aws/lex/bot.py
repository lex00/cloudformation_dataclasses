"""PropertyTypes for AWS::Lex::Bot."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedRecognitionSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_recognition_strategy": "AudioRecognitionStrategy",
    }

    audio_recognition_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AllowedInputTypes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_dtmf_input": "AllowDTMFInput",
        "allow_audio_input": "AllowAudioInput",
    }

    allow_dtmf_input: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    allow_audio_input: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AudioAndDTMFInputSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dtmf_specification": "DTMFSpecification",
        "audio_specification": "AudioSpecification",
        "start_timeout_ms": "StartTimeoutMs",
    }

    dtmf_specification: Optional[DTMFSpecification] = None
    audio_specification: Optional[AudioSpecification] = None
    start_timeout_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AudioLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
    }

    s3_bucket: Optional[S3BucketLogDestination] = None


@dataclass
class AudioLogSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "enabled": "Enabled",
    }

    destination: Optional[AudioLogDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AudioSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "end_timeout_ms": "EndTimeoutMs",
        "max_length_ms": "MaxLengthMs",
    }

    end_timeout_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_length_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BKBExactResponseFields(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "answer_field": "AnswerField",
    }

    answer_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_agent_id": "BedrockAgentId",
        "bedrock_agent_alias_id": "BedrockAgentAliasId",
    }

    bedrock_agent_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_agent_alias_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockAgentIntentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_agent_configuration": "BedrockAgentConfiguration",
        "bedrock_agent_intent_knowledge_base_configuration": "BedrockAgentIntentKnowledgeBaseConfiguration",
    }

    bedrock_agent_configuration: Optional[BedrockAgentConfiguration] = None
    bedrock_agent_intent_knowledge_base_configuration: Optional[BedrockAgentIntentKnowledgeBaseConfiguration] = None


@dataclass
class BedrockAgentIntentKnowledgeBaseConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_model_configuration": "BedrockModelConfiguration",
        "bedrock_knowledge_base_arn": "BedrockKnowledgeBaseArn",
    }

    bedrock_model_configuration: Optional[BedrockModelSpecification] = None
    bedrock_knowledge_base_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockGuardrailConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_guardrail_version": "BedrockGuardrailVersion",
        "bedrock_guardrail_identifier": "BedrockGuardrailIdentifier",
    }

    bedrock_guardrail_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_guardrail_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockKnowledgeStoreConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bkb_exact_response_fields": "BKBExactResponseFields",
        "exact_response": "ExactResponse",
        "bedrock_knowledge_base_arn": "BedrockKnowledgeBaseArn",
    }

    bkb_exact_response_fields: Optional[BKBExactResponseFields] = None
    exact_response: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bedrock_knowledge_base_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockModelSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
        "bedrock_trace_status": "BedrockTraceStatus",
        "bedrock_model_custom_prompt": "BedrockModelCustomPrompt",
        "bedrock_guardrail_configuration": "BedrockGuardrailConfiguration",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_trace_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_model_custom_prompt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_guardrail_configuration: Optional[BedrockGuardrailConfiguration] = None


@dataclass
class BotAliasLocaleSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code_hook_specification": "CodeHookSpecification",
        "enabled": "Enabled",
    }

    code_hook_specification: Optional[CodeHookSpecification] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class BotAliasLocaleSettingsItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale_id": "LocaleId",
        "bot_alias_locale_setting": "BotAliasLocaleSetting",
    }

    locale_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bot_alias_locale_setting: Optional[BotAliasLocaleSettings] = None


@dataclass
class BotLocale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nlu_confidence_threshold": "NluConfidenceThreshold",
        "locale_id": "LocaleId",
        "description": "Description",
        "generative_ai_settings": "GenerativeAISettings",
        "custom_vocabulary": "CustomVocabulary",
        "slot_types": "SlotTypes",
        "intents": "Intents",
        "voice_settings": "VoiceSettings",
    }

    nlu_confidence_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    locale_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    generative_ai_settings: Optional[GenerativeAISettings] = None
    custom_vocabulary: Optional[CustomVocabulary] = None
    slot_types: Optional[list[SlotType]] = None
    intents: Optional[list[Intent]] = None
    voice_settings: Optional[VoiceSettings] = None


@dataclass
class BuildtimeSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "descriptive_bot_builder_specification": "DescriptiveBotBuilderSpecification",
        "sample_utterance_generation_specification": "SampleUtteranceGenerationSpecification",
    }

    descriptive_bot_builder_specification: Optional[DescriptiveBotBuilderSpecification] = None
    sample_utterance_generation_specification: Optional[SampleUtteranceGenerationSpecification] = None


@dataclass
class Button(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "text": "Text",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogGroupLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_log_group_arn": "CloudWatchLogGroupArn",
        "log_prefix": "LogPrefix",
    }

    cloud_watch_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CodeHookSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_code_hook": "LambdaCodeHook",
    }

    lambda_code_hook: Optional[LambdaCodeHook] = None


@dataclass
class CompositeSlotTypeSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sub_slots": "SubSlots",
    }

    sub_slots: Optional[list[SubSlotTypeComposition]] = None


@dataclass
class Condition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression_string": "ExpressionString",
    }

    expression_string: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionalBranch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "response": "Response",
        "name": "Name",
        "next_step": "NextStep",
    }

    condition: Optional[Condition] = None
    response: Optional[ResponseSpecification] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next_step: Optional[DialogState] = None


@dataclass
class ConditionalSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_branch": "DefaultBranch",
        "is_active": "IsActive",
        "conditional_branches": "ConditionalBranches",
    }

    default_branch: Optional[DefaultConditionalBranch] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    conditional_branches: Optional[list[ConditionalBranch]] = None


@dataclass
class ConversationLogSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_log_settings": "TextLogSettings",
        "audio_log_settings": "AudioLogSettings",
    }

    text_log_settings: Optional[list[TextLogSetting]] = None
    audio_log_settings: Optional[list[AudioLogSetting]] = None


@dataclass
class CustomPayload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomVocabulary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_vocabulary_items": "CustomVocabularyItems",
    }

    custom_vocabulary_items: Optional[list[CustomVocabularyItem]] = None


@dataclass
class CustomVocabularyItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_as": "DisplayAs",
        "phrase": "Phrase",
        "weight": "Weight",
    }

    display_as: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phrase: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DTMFSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "deletion_character": "DeletionCharacter",
        "end_timeout_ms": "EndTimeoutMs",
        "end_character": "EndCharacter",
        "max_length": "MaxLength",
    }

    deletion_character: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_timeout_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end_character: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_length: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrivacy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "child_directed": "ChildDirected",
    }

    child_directed: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_knowledge_store_configuration": "BedrockKnowledgeStoreConfiguration",
        "kendra_configuration": "KendraConfiguration",
        "opensearch_configuration": "OpensearchConfiguration",
    }

    bedrock_knowledge_store_configuration: Optional[BedrockKnowledgeStoreConfiguration] = None
    kendra_configuration: Optional[QnAKendraConfiguration] = None
    opensearch_configuration: Optional[OpensearchConfiguration] = None


@dataclass
class DefaultConditionalBranch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "response": "Response",
        "next_step": "NextStep",
    }

    response: Optional[ResponseSpecification] = None
    next_step: Optional[DialogState] = None


@dataclass
class DescriptiveBotBuilderSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "bedrock_model_specification": "BedrockModelSpecification",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bedrock_model_specification: Optional[BedrockModelSpecification] = None


@dataclass
class DialogAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "slot_to_elicit": "SlotToElicit",
        "suppress_next_message": "SuppressNextMessage",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_to_elicit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    suppress_next_message: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DialogCodeHookInvocationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_code_hook_invocation": "EnableCodeHookInvocation",
        "invocation_label": "InvocationLabel",
        "is_active": "IsActive",
        "post_code_hook_specification": "PostCodeHookSpecification",
    }

    enable_code_hook_invocation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    invocation_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    post_code_hook_specification: Optional[PostDialogCodeHookInvocationSpecification] = None


@dataclass
class DialogCodeHookSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DialogState(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dialog_action": "DialogAction",
        "session_attributes": "SessionAttributes",
        "intent": "Intent",
    }

    dialog_action: Optional[DialogAction] = None
    session_attributes: Optional[list[SessionAttribute]] = None
    intent: Optional[IntentOverride] = None


@dataclass
class ElicitationCodeHookInvocationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_code_hook_invocation": "EnableCodeHookInvocation",
        "invocation_label": "InvocationLabel",
    }

    enable_code_hook_invocation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    invocation_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorLogSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ExactResponseFields(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "question_field": "QuestionField",
        "answer_field": "AnswerField",
    }

    question_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    answer_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExternalSourceSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grammar_slot_type_setting": "GrammarSlotTypeSetting",
    }

    grammar_slot_type_setting: Optional[GrammarSlotTypeSetting] = None


@dataclass
class FulfillmentCodeHookSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "post_fulfillment_status_specification": "PostFulfillmentStatusSpecification",
        "fulfillment_updates_specification": "FulfillmentUpdatesSpecification",
        "is_active": "IsActive",
        "enabled": "Enabled",
    }

    post_fulfillment_status_specification: Optional[PostFulfillmentStatusSpecification] = None
    fulfillment_updates_specification: Optional[FulfillmentUpdatesSpecification] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FulfillmentStartResponseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delay_in_seconds": "DelayInSeconds",
        "message_groups": "MessageGroups",
        "allow_interrupt": "AllowInterrupt",
    }

    delay_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    message_groups: Optional[list[MessageGroup]] = None
    allow_interrupt: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FulfillmentUpdateResponseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message_groups": "MessageGroups",
        "allow_interrupt": "AllowInterrupt",
        "frequency_in_seconds": "FrequencyInSeconds",
    }

    message_groups: Optional[list[MessageGroup]] = None
    allow_interrupt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    frequency_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FulfillmentUpdatesSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "update_response": "UpdateResponse",
        "active": "Active",
        "timeout_in_seconds": "TimeoutInSeconds",
        "start_response": "StartResponse",
    }

    update_response: Optional[FulfillmentUpdateResponseSpecification] = None
    active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    start_response: Optional[FulfillmentStartResponseSpecification] = None


@dataclass
class GenerativeAISettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime_settings": "RuntimeSettings",
        "buildtime_settings": "BuildtimeSettings",
    }

    runtime_settings: Optional[RuntimeSettings] = None
    buildtime_settings: Optional[BuildtimeSettings] = None


@dataclass
class GrammarSlotTypeSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[GrammarSlotTypeSource] = None


@dataclass
class GrammarSlotTypeSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "s3_bucket_name": "S3BucketName",
        "s3_object_key": "S3ObjectKey",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageResponseCard(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "title": "Title",
        "image_url": "ImageUrl",
        "buttons": "Buttons",
    }

    subtitle: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    buttons: Optional[list[Button]] = None


@dataclass
class InitialResponseSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code_hook": "CodeHook",
        "initial_response": "InitialResponse",
        "conditional": "Conditional",
        "next_step": "NextStep",
    }

    code_hook: Optional[DialogCodeHookInvocationSetting] = None
    initial_response: Optional[ResponseSpecification] = None
    conditional: Optional[ConditionalSpecification] = None
    next_step: Optional[DialogState] = None


@dataclass
class InputContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Intent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "q_in_connect_intent_configuration": "QInConnectIntentConfiguration",
        "description": "Description",
        "parent_intent_signature": "ParentIntentSignature",
        "initial_response_setting": "InitialResponseSetting",
        "bedrock_agent_intent_configuration": "BedrockAgentIntentConfiguration",
        "fulfillment_code_hook": "FulfillmentCodeHook",
        "intent_confirmation_setting": "IntentConfirmationSetting",
        "name": "Name",
        "slots": "Slots",
        "qn_a_intent_configuration": "QnAIntentConfiguration",
        "dialog_code_hook": "DialogCodeHook",
        "input_contexts": "InputContexts",
        "kendra_configuration": "KendraConfiguration",
        "intent_closing_setting": "IntentClosingSetting",
        "output_contexts": "OutputContexts",
        "slot_priorities": "SlotPriorities",
        "sample_utterances": "SampleUtterances",
    }

    q_in_connect_intent_configuration: Optional[QInConnectIntentConfiguration] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parent_intent_signature: Optional[Union[str, Ref, GetAtt, Sub]] = None
    initial_response_setting: Optional[InitialResponseSetting] = None
    bedrock_agent_intent_configuration: Optional[BedrockAgentIntentConfiguration] = None
    fulfillment_code_hook: Optional[FulfillmentCodeHookSetting] = None
    intent_confirmation_setting: Optional[IntentConfirmationSetting] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slots: Optional[list[Slot]] = None
    qn_a_intent_configuration: Optional[QnAIntentConfiguration] = None
    dialog_code_hook: Optional[DialogCodeHookSetting] = None
    input_contexts: Optional[list[InputContext]] = None
    kendra_configuration: Optional[KendraConfiguration] = None
    intent_closing_setting: Optional[IntentClosingSetting] = None
    output_contexts: Optional[list[OutputContext]] = None
    slot_priorities: Optional[list[SlotPriority]] = None
    sample_utterances: Optional[list[SampleUtterance]] = None


@dataclass
class IntentClosingSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_active": "IsActive",
        "closing_response": "ClosingResponse",
        "conditional": "Conditional",
        "next_step": "NextStep",
    }

    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    closing_response: Optional[ResponseSpecification] = None
    conditional: Optional[ConditionalSpecification] = None
    next_step: Optional[DialogState] = None


@dataclass
class IntentConfirmationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_specification": "PromptSpecification",
        "confirmation_response": "ConfirmationResponse",
        "declination_conditional": "DeclinationConditional",
        "failure_conditional": "FailureConditional",
        "confirmation_conditional": "ConfirmationConditional",
        "is_active": "IsActive",
        "failure_response": "FailureResponse",
        "code_hook": "CodeHook",
        "declination_next_step": "DeclinationNextStep",
        "elicitation_code_hook": "ElicitationCodeHook",
        "confirmation_next_step": "ConfirmationNextStep",
        "failure_next_step": "FailureNextStep",
        "declination_response": "DeclinationResponse",
    }

    prompt_specification: Optional[PromptSpecification] = None
    confirmation_response: Optional[ResponseSpecification] = None
    declination_conditional: Optional[ConditionalSpecification] = None
    failure_conditional: Optional[ConditionalSpecification] = None
    confirmation_conditional: Optional[ConditionalSpecification] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    failure_response: Optional[ResponseSpecification] = None
    code_hook: Optional[DialogCodeHookInvocationSetting] = None
    declination_next_step: Optional[DialogState] = None
    elicitation_code_hook: Optional[ElicitationCodeHookInvocationSetting] = None
    confirmation_next_step: Optional[DialogState] = None
    failure_next_step: Optional[DialogState] = None
    declination_response: Optional[ResponseSpecification] = None


@dataclass
class IntentOverride(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slots": "Slots",
        "name": "Name",
    }

    slots: Optional[list[SlotValueOverrideMap]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KendraConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "query_filter_string": "QueryFilterString",
        "query_filter_string_enabled": "QueryFilterStringEnabled",
        "kendra_index": "KendraIndex",
    }

    query_filter_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_filter_string_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kendra_index: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaCodeHook(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "code_hook_interface_version": "CodeHookInterfaceVersion",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code_hook_interface_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Message(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_payload": "CustomPayload",
        "image_response_card": "ImageResponseCard",
        "plain_text_message": "PlainTextMessage",
        "ssml_message": "SSMLMessage",
    }

    custom_payload: Optional[CustomPayload] = None
    image_response_card: Optional[ImageResponseCard] = None
    plain_text_message: Optional[PlainTextMessage] = None
    ssml_message: Optional[SSMLMessage] = None


@dataclass
class MessageGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "variations": "Variations",
    }

    message: Optional[Message] = None
    variations: Optional[list[Message]] = None


@dataclass
class MultipleValuesSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_multiple_values": "AllowMultipleValues",
    }

    allow_multiple_values: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class NluImprovementSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ObfuscationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "obfuscation_setting_type": "ObfuscationSettingType",
    }

    obfuscation_setting_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpensearchConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "domain_endpoint": "DomainEndpoint",
        "exact_response_fields": "ExactResponseFields",
        "exact_response": "ExactResponse",
        "include_fields": "IncludeFields",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact_response_fields: Optional[ExactResponseFields] = None
    exact_response: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_fields: Optional[Union[list[str], Ref]] = None


@dataclass
class OutputContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "turns_to_live": "TurnsToLive",
        "time_to_live_in_seconds": "TimeToLiveInSeconds",
        "name": "Name",
    }

    turns_to_live: Optional[Union[int, Ref, GetAtt, Sub]] = None
    time_to_live_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PlainTextMessage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PostDialogCodeHookInvocationSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "success_response": "SuccessResponse",
        "failure_conditional": "FailureConditional",
        "timeout_next_step": "TimeoutNextStep",
        "success_conditional": "SuccessConditional",
        "timeout_response": "TimeoutResponse",
        "success_next_step": "SuccessNextStep",
        "failure_response": "FailureResponse",
        "failure_next_step": "FailureNextStep",
        "timeout_conditional": "TimeoutConditional",
    }

    success_response: Optional[ResponseSpecification] = None
    failure_conditional: Optional[ConditionalSpecification] = None
    timeout_next_step: Optional[DialogState] = None
    success_conditional: Optional[ConditionalSpecification] = None
    timeout_response: Optional[ResponseSpecification] = None
    success_next_step: Optional[DialogState] = None
    failure_response: Optional[ResponseSpecification] = None
    failure_next_step: Optional[DialogState] = None
    timeout_conditional: Optional[ConditionalSpecification] = None


@dataclass
class PostFulfillmentStatusSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "success_response": "SuccessResponse",
        "failure_conditional": "FailureConditional",
        "timeout_next_step": "TimeoutNextStep",
        "success_conditional": "SuccessConditional",
        "timeout_response": "TimeoutResponse",
        "success_next_step": "SuccessNextStep",
        "failure_response": "FailureResponse",
        "failure_next_step": "FailureNextStep",
        "timeout_conditional": "TimeoutConditional",
    }

    success_response: Optional[ResponseSpecification] = None
    failure_conditional: Optional[ConditionalSpecification] = None
    timeout_next_step: Optional[DialogState] = None
    success_conditional: Optional[ConditionalSpecification] = None
    timeout_response: Optional[ResponseSpecification] = None
    success_next_step: Optional[DialogState] = None
    failure_response: Optional[ResponseSpecification] = None
    failure_next_step: Optional[DialogState] = None
    timeout_conditional: Optional[ConditionalSpecification] = None


@dataclass
class PromptAttemptSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_input_specification": "TextInputSpecification",
        "allow_interrupt": "AllowInterrupt",
        "allowed_input_types": "AllowedInputTypes",
        "audio_and_dtmf_input_specification": "AudioAndDTMFInputSpecification",
    }

    text_input_specification: Optional[TextInputSpecification] = None
    allow_interrupt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    allowed_input_types: Optional[AllowedInputTypes] = None
    audio_and_dtmf_input_specification: Optional[AudioAndDTMFInputSpecification] = None


@dataclass
class PromptSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_retries": "MaxRetries",
        "message_groups_list": "MessageGroupsList",
        "prompt_attempts_specification": "PromptAttemptsSpecification",
        "allow_interrupt": "AllowInterrupt",
        "message_selection_strategy": "MessageSelectionStrategy",
    }

    max_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    message_groups_list: Optional[list[MessageGroup]] = None
    prompt_attempts_specification: Optional[dict[str, Any]] = None
    allow_interrupt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    message_selection_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QInConnectAssistantConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "assistant_arn": "AssistantArn",
    }

    assistant_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QInConnectIntentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "q_in_connect_assistant_configuration": "QInConnectAssistantConfiguration",
    }

    q_in_connect_assistant_configuration: Optional[QInConnectAssistantConfiguration] = None


@dataclass
class QnAIntentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_model_configuration": "BedrockModelConfiguration",
        "data_source_configuration": "DataSourceConfiguration",
    }

    bedrock_model_configuration: Optional[BedrockModelSpecification] = None
    data_source_configuration: Optional[DataSourceConfiguration] = None


@dataclass
class QnAKendraConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "query_filter_string": "QueryFilterString",
        "query_filter_string_enabled": "QueryFilterStringEnabled",
        "kendra_index": "KendraIndex",
        "exact_response": "ExactResponse",
    }

    query_filter_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_filter_string_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kendra_index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact_response: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Replication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_regions": "ReplicaRegions",
    }

    replica_regions: Optional[Union[list[str], Ref]] = None


@dataclass
class ResponseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message_groups_list": "MessageGroupsList",
        "allow_interrupt": "AllowInterrupt",
    }

    message_groups_list: Optional[list[MessageGroup]] = None
    allow_interrupt: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RuntimeSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slot_resolution_improvement_specification": "SlotResolutionImprovementSpecification",
        "nlu_improvement_specification": "NluImprovementSpecification",
    }

    slot_resolution_improvement_specification: Optional[SlotResolutionImprovementSpecification] = None
    nlu_improvement_specification: Optional[NluImprovementSpecification] = None


@dataclass
class S3BucketLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "log_prefix": "LogPrefix",
        "s3_bucket_arn": "S3BucketArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_object_version": "S3ObjectVersion",
        "s3_bucket": "S3Bucket",
        "s3_object_key": "S3ObjectKey",
    }

    s3_object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SSMLMessage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SampleUtterance(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "utterance": "Utterance",
    }

    utterance: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SampleUtteranceGenerationSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "bedrock_model_specification": "BedrockModelSpecification",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bedrock_model_specification: Optional[BedrockModelSpecification] = None


@dataclass
class SampleValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SentimentAnalysisSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "detect_sentiment": "DetectSentiment",
    }

    detect_sentiment: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SessionAttribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Slot(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "slot_type_name": "SlotTypeName",
        "value_elicitation_setting": "ValueElicitationSetting",
        "sub_slot_setting": "SubSlotSetting",
        "obfuscation_setting": "ObfuscationSetting",
        "name": "Name",
        "multiple_values_setting": "MultipleValuesSetting",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_elicitation_setting: Optional[SlotValueElicitationSetting] = None
    sub_slot_setting: Optional[SubSlotSetting] = None
    obfuscation_setting: Optional[ObfuscationSetting] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multiple_values_setting: Optional[MultipleValuesSetting] = None


@dataclass
class SlotCaptureSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capture_conditional": "CaptureConditional",
        "failure_conditional": "FailureConditional",
        "capture_response": "CaptureResponse",
        "capture_next_step": "CaptureNextStep",
        "failure_response": "FailureResponse",
        "code_hook": "CodeHook",
        "failure_next_step": "FailureNextStep",
        "elicitation_code_hook": "ElicitationCodeHook",
    }

    capture_conditional: Optional[ConditionalSpecification] = None
    failure_conditional: Optional[ConditionalSpecification] = None
    capture_response: Optional[ResponseSpecification] = None
    capture_next_step: Optional[DialogState] = None
    failure_response: Optional[ResponseSpecification] = None
    code_hook: Optional[DialogCodeHookInvocationSetting] = None
    failure_next_step: Optional[DialogState] = None
    elicitation_code_hook: Optional[ElicitationCodeHookInvocationSetting] = None


@dataclass
class SlotDefaultValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlotDefaultValueSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value_list": "DefaultValueList",
    }

    default_value_list: Optional[list[SlotDefaultValue]] = None


@dataclass
class SlotPriority(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "slot_name": "SlotName",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    slot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlotResolutionImprovementSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "bedrock_model_specification": "BedrockModelSpecification",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bedrock_model_specification: Optional[BedrockModelSpecification] = None


@dataclass
class SlotType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slot_type_values": "SlotTypeValues",
        "description": "Description",
        "parent_slot_type_signature": "ParentSlotTypeSignature",
        "value_selection_setting": "ValueSelectionSetting",
        "composite_slot_type_setting": "CompositeSlotTypeSetting",
        "external_source_setting": "ExternalSourceSetting",
        "name": "Name",
    }

    slot_type_values: Optional[list[SlotTypeValue]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parent_slot_type_signature: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_selection_setting: Optional[SlotValueSelectionSetting] = None
    composite_slot_type_setting: Optional[CompositeSlotTypeSetting] = None
    external_source_setting: Optional[ExternalSourceSetting] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlotTypeValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "synonyms": "Synonyms",
        "sample_value": "SampleValue",
    }

    synonyms: Optional[list[SampleValue]] = None
    sample_value: Optional[SampleValue] = None


@dataclass
class SlotValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interpreted_value": "InterpretedValue",
    }

    interpreted_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlotValueElicitationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_specification": "PromptSpecification",
        "wait_and_continue_specification": "WaitAndContinueSpecification",
        "slot_constraint": "SlotConstraint",
        "slot_capture_setting": "SlotCaptureSetting",
        "sample_utterances": "SampleUtterances",
        "default_value_specification": "DefaultValueSpecification",
    }

    prompt_specification: Optional[PromptSpecification] = None
    wait_and_continue_specification: Optional[WaitAndContinueSpecification] = None
    slot_constraint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_capture_setting: Optional[SlotCaptureSetting] = None
    sample_utterances: Optional[list[SampleUtterance]] = None
    default_value_specification: Optional[SlotDefaultValueSpecification] = None


@dataclass
class SlotValueOverride(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "shape": "Shape",
        "value": "Value",
        "values": "Values",
    }

    shape: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[SlotValue] = None
    values: Optional[list[SlotValueOverride]] = None


@dataclass
class SlotValueOverrideMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slot_name": "SlotName",
        "slot_value_override": "SlotValueOverride",
    }

    slot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_value_override: Optional[SlotValueOverride] = None


@dataclass
class SlotValueRegexFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlotValueSelectionSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_recognition_setting": "AdvancedRecognitionSetting",
        "regex_filter": "RegexFilter",
        "resolution_strategy": "ResolutionStrategy",
    }

    advanced_recognition_setting: Optional[AdvancedRecognitionSetting] = None
    regex_filter: Optional[SlotValueRegexFilter] = None
    resolution_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Specifications(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_elicitation_setting": "ValueElicitationSetting",
        "slot_type_id": "SlotTypeId",
    }

    value_elicitation_setting: Optional[SubSlotValueElicitationSetting] = None
    slot_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StillWaitingResponseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message_groups_list": "MessageGroupsList",
        "timeout_in_seconds": "TimeoutInSeconds",
        "allow_interrupt": "AllowInterrupt",
        "frequency_in_seconds": "FrequencyInSeconds",
    }

    message_groups_list: Optional[list[MessageGroup]] = None
    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allow_interrupt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    frequency_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SubSlotSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "slot_specifications": "SlotSpecifications",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_specifications: Optional[dict[str, Any]] = None


@dataclass
class SubSlotTypeComposition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slot_type_id": "SlotTypeId",
        "name": "Name",
    }

    slot_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubSlotValueElicitationSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_specification": "PromptSpecification",
        "wait_and_continue_specification": "WaitAndContinueSpecification",
        "sample_utterances": "SampleUtterances",
        "default_value_specification": "DefaultValueSpecification",
    }

    prompt_specification: Optional[PromptSpecification] = None
    wait_and_continue_specification: Optional[WaitAndContinueSpecification] = None
    sample_utterances: Optional[list[SampleUtterance]] = None
    default_value_specification: Optional[SlotDefaultValueSpecification] = None


@dataclass
class TestBotAliasSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "bot_alias_locale_settings": "BotAliasLocaleSettings",
        "conversation_log_settings": "ConversationLogSettings",
        "sentiment_analysis_settings": "SentimentAnalysisSettings",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bot_alias_locale_settings: Optional[list[BotAliasLocaleSettingsItem]] = None
    conversation_log_settings: Optional[ConversationLogSettings] = None
    sentiment_analysis_settings: Optional[SentimentAnalysisSettings] = None


@dataclass
class TextInputSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start_timeout_ms": "StartTimeoutMs",
    }

    start_timeout_ms: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TextLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch": "CloudWatch",
    }

    cloud_watch: Optional[CloudWatchLogGroupLogDestination] = None


@dataclass
class TextLogSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "enabled": "Enabled",
    }

    destination: Optional[TextLogDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VoiceSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "voice_id": "VoiceId",
        "engine": "Engine",
    }

    voice_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    engine: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WaitAndContinueSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "waiting_response": "WaitingResponse",
        "still_waiting_response": "StillWaitingResponse",
        "is_active": "IsActive",
        "continue_response": "ContinueResponse",
    }

    waiting_response: Optional[ResponseSpecification] = None
    still_waiting_response: Optional[StillWaitingResponseSpecification] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    continue_response: Optional[ResponseSpecification] = None

