"""PropertyTypes for AWS::BedrockAgentCore::Memory."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomConfigurationInput(PropertyType):
    SUMMARY_OVERRIDE = "SummaryOverride"
    USER_PREFERENCE_OVERRIDE = "UserPreferenceOverride"
    SEMANTIC_OVERRIDE = "SemanticOverride"
    SELF_MANAGED_CONFIGURATION = "SelfManagedConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "summary_override": "SummaryOverride",
        "user_preference_override": "UserPreferenceOverride",
        "semantic_override": "SemanticOverride",
        "self_managed_configuration": "SelfManagedConfiguration",
    }

    summary_override: Optional[SummaryOverride] = None
    user_preference_override: Optional[UserPreferenceOverride] = None
    semantic_override: Optional[SemanticOverride] = None
    self_managed_configuration: Optional[SelfManagedConfiguration] = None


@dataclass
class CustomMemoryStrategy(PropertyType):
    STATUS = "Status"
    NAMESPACES = "Namespaces"
    TYPE = "Type"
    DESCRIPTION = "Description"
    CONFIGURATION = "Configuration"
    CREATED_AT = "CreatedAt"
    STRATEGY_ID = "StrategyId"
    UPDATED_AT = "UpdatedAt"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "namespaces": "Namespaces",
        "type_": "Type",
        "description": "Description",
        "configuration": "Configuration",
        "created_at": "CreatedAt",
        "strategy_id": "StrategyId",
        "updated_at": "UpdatedAt",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespaces: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration: Optional[CustomConfigurationInput] = None
    created_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    strategy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    updated_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InvocationConfigurationInput(PropertyType):
    TOPIC_ARN = "TopicArn"
    PAYLOAD_DELIVERY_BUCKET_NAME = "PayloadDeliveryBucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
        "payload_delivery_bucket_name": "PayloadDeliveryBucketName",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_delivery_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryStrategy(PropertyType):
    SUMMARY_MEMORY_STRATEGY = "SummaryMemoryStrategy"
    CUSTOM_MEMORY_STRATEGY = "CustomMemoryStrategy"
    SEMANTIC_MEMORY_STRATEGY = "SemanticMemoryStrategy"
    USER_PREFERENCE_MEMORY_STRATEGY = "UserPreferenceMemoryStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "summary_memory_strategy": "SummaryMemoryStrategy",
        "custom_memory_strategy": "CustomMemoryStrategy",
        "semantic_memory_strategy": "SemanticMemoryStrategy",
        "user_preference_memory_strategy": "UserPreferenceMemoryStrategy",
    }

    summary_memory_strategy: Optional[SummaryMemoryStrategy] = None
    custom_memory_strategy: Optional[CustomMemoryStrategy] = None
    semantic_memory_strategy: Optional[SemanticMemoryStrategy] = None
    user_preference_memory_strategy: Optional[UserPreferenceMemoryStrategy] = None


@dataclass
class MessageBasedTriggerInput(PropertyType):
    MESSAGE_COUNT = "MessageCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_count": "MessageCount",
    }

    message_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SelfManagedConfiguration(PropertyType):
    TRIGGER_CONDITIONS = "TriggerConditions"
    INVOCATION_CONFIGURATION = "InvocationConfiguration"
    HISTORICAL_CONTEXT_WINDOW_SIZE = "HistoricalContextWindowSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "trigger_conditions": "TriggerConditions",
        "invocation_configuration": "InvocationConfiguration",
        "historical_context_window_size": "HistoricalContextWindowSize",
    }

    trigger_conditions: Optional[list[TriggerConditionInput]] = None
    invocation_configuration: Optional[InvocationConfigurationInput] = None
    historical_context_window_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticMemoryStrategy(PropertyType):
    STATUS = "Status"
    NAMESPACES = "Namespaces"
    TYPE = "Type"
    DESCRIPTION = "Description"
    CREATED_AT = "CreatedAt"
    STRATEGY_ID = "StrategyId"
    UPDATED_AT = "UpdatedAt"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "namespaces": "Namespaces",
        "type_": "Type",
        "description": "Description",
        "created_at": "CreatedAt",
        "strategy_id": "StrategyId",
        "updated_at": "UpdatedAt",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespaces: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    strategy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    updated_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticOverride(PropertyType):
    CONSOLIDATION = "Consolidation"
    EXTRACTION = "Extraction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consolidation": "Consolidation",
        "extraction": "Extraction",
    }

    consolidation: Optional[SemanticOverrideConsolidationConfigurationInput] = None
    extraction: Optional[SemanticOverrideExtractionConfigurationInput] = None


@dataclass
class SemanticOverrideConsolidationConfigurationInput(PropertyType):
    APPEND_TO_PROMPT = "AppendToPrompt"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "append_to_prompt": "AppendToPrompt",
        "model_id": "ModelId",
    }

    append_to_prompt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticOverrideExtractionConfigurationInput(PropertyType):
    APPEND_TO_PROMPT = "AppendToPrompt"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "append_to_prompt": "AppendToPrompt",
        "model_id": "ModelId",
    }

    append_to_prompt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SummaryMemoryStrategy(PropertyType):
    STATUS = "Status"
    NAMESPACES = "Namespaces"
    TYPE = "Type"
    DESCRIPTION = "Description"
    CREATED_AT = "CreatedAt"
    STRATEGY_ID = "StrategyId"
    UPDATED_AT = "UpdatedAt"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "namespaces": "Namespaces",
        "type_": "Type",
        "description": "Description",
        "created_at": "CreatedAt",
        "strategy_id": "StrategyId",
        "updated_at": "UpdatedAt",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespaces: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    strategy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    updated_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SummaryOverride(PropertyType):
    CONSOLIDATION = "Consolidation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consolidation": "Consolidation",
    }

    consolidation: Optional[SummaryOverrideConsolidationConfigurationInput] = None


@dataclass
class SummaryOverrideConsolidationConfigurationInput(PropertyType):
    APPEND_TO_PROMPT = "AppendToPrompt"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "append_to_prompt": "AppendToPrompt",
        "model_id": "ModelId",
    }

    append_to_prompt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedTriggerInput(PropertyType):
    IDLE_SESSION_TIMEOUT = "IdleSessionTimeout"

    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_session_timeout": "IdleSessionTimeout",
    }

    idle_session_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TokenBasedTriggerInput(PropertyType):
    TOKEN_COUNT = "TokenCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "token_count": "TokenCount",
    }

    token_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TriggerConditionInput(PropertyType):
    MESSAGE_BASED_TRIGGER = "MessageBasedTrigger"
    TOKEN_BASED_TRIGGER = "TokenBasedTrigger"
    TIME_BASED_TRIGGER = "TimeBasedTrigger"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_based_trigger": "MessageBasedTrigger",
        "token_based_trigger": "TokenBasedTrigger",
        "time_based_trigger": "TimeBasedTrigger",
    }

    message_based_trigger: Optional[MessageBasedTriggerInput] = None
    token_based_trigger: Optional[TokenBasedTriggerInput] = None
    time_based_trigger: Optional[TimeBasedTriggerInput] = None


@dataclass
class UserPreferenceMemoryStrategy(PropertyType):
    STATUS = "Status"
    NAMESPACES = "Namespaces"
    TYPE = "Type"
    DESCRIPTION = "Description"
    CREATED_AT = "CreatedAt"
    STRATEGY_ID = "StrategyId"
    UPDATED_AT = "UpdatedAt"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "namespaces": "Namespaces",
        "type_": "Type",
        "description": "Description",
        "created_at": "CreatedAt",
        "strategy_id": "StrategyId",
        "updated_at": "UpdatedAt",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespaces: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    strategy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    updated_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserPreferenceOverride(PropertyType):
    CONSOLIDATION = "Consolidation"
    EXTRACTION = "Extraction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consolidation": "Consolidation",
        "extraction": "Extraction",
    }

    consolidation: Optional[UserPreferenceOverrideConsolidationConfigurationInput] = None
    extraction: Optional[UserPreferenceOverrideExtractionConfigurationInput] = None


@dataclass
class UserPreferenceOverrideConsolidationConfigurationInput(PropertyType):
    APPEND_TO_PROMPT = "AppendToPrompt"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "append_to_prompt": "AppendToPrompt",
        "model_id": "ModelId",
    }

    append_to_prompt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserPreferenceOverrideExtractionConfigurationInput(PropertyType):
    APPEND_TO_PROMPT = "AppendToPrompt"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "append_to_prompt": "AppendToPrompt",
        "model_id": "ModelId",
    }

    append_to_prompt: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

