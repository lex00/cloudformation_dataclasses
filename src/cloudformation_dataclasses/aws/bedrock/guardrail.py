"""PropertyTypes for AWS::Bedrock::Guardrail."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutomatedReasoningPolicyConfig(PropertyType):
    POLICIES = "Policies"
    CONFIDENCE_THRESHOLD = "ConfidenceThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policies": "Policies",
        "confidence_threshold": "ConfidenceThreshold",
    }

    policies: Optional[Union[list[str], Ref]] = None
    confidence_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ContentFilterConfig(PropertyType):
    OUTPUT_STRENGTH = "OutputStrength"
    TYPE = "Type"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    INPUT_STRENGTH = "InputStrength"
    INPUT_MODALITIES = "InputModalities"
    OUTPUT_ENABLED = "OutputEnabled"
    OUTPUT_MODALITIES = "OutputModalities"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_strength": "OutputStrength",
        "type_": "Type",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "input_strength": "InputStrength",
        "input_modalities": "InputModalities",
        "output_enabled": "OutputEnabled",
        "output_modalities": "OutputModalities",
    }

    output_strength: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_strength: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_modalities: Optional[Union[list[str], Ref]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    output_modalities: Optional[Union[list[str], Ref]] = None


@dataclass
class ContentFiltersTierConfig(PropertyType):
    TIER_NAME = "TierName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tier_name": "TierName",
    }

    tier_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContentPolicyConfig(PropertyType):
    CONTENT_FILTERS_TIER_CONFIG = "ContentFiltersTierConfig"
    FILTERS_CONFIG = "FiltersConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_filters_tier_config": "ContentFiltersTierConfig",
        "filters_config": "FiltersConfig",
    }

    content_filters_tier_config: Optional[ContentFiltersTierConfig] = None
    filters_config: Optional[list[ContentFilterConfig]] = None


@dataclass
class ContextualGroundingFilterConfig(PropertyType):
    TYPE = "Type"
    ACTION = "Action"
    ENABLED = "Enabled"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "action": "Action",
        "enabled": "Enabled",
        "threshold": "Threshold",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ContextualGroundingPolicyConfig(PropertyType):
    FILTERS_CONFIG = "FiltersConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters_config": "FiltersConfig",
    }

    filters_config: Optional[list[ContextualGroundingFilterConfig]] = None


@dataclass
class GuardrailCrossRegionConfig(PropertyType):
    GUARDRAIL_PROFILE_ARN = "GuardrailProfileArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_profile_arn": "GuardrailProfileArn",
    }

    guardrail_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedWordsConfig(PropertyType):
    TYPE = "Type"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PiiEntityConfig(PropertyType):
    TYPE = "Type"
    ACTION = "Action"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "action": "Action",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RegexConfig(PropertyType):
    PATTERN = "Pattern"
    ACTION = "Action"
    INPUT_ENABLED = "InputEnabled"
    DESCRIPTION = "Description"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
        "action": "Action",
        "input_enabled": "InputEnabled",
        "description": "Description",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
        "name": "Name",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SensitiveInformationPolicyConfig(PropertyType):
    REGEXES_CONFIG = "RegexesConfig"
    PII_ENTITIES_CONFIG = "PiiEntitiesConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regexes_config": "RegexesConfig",
        "pii_entities_config": "PiiEntitiesConfig",
    }

    regexes_config: Optional[list[RegexConfig]] = None
    pii_entities_config: Optional[list[PiiEntityConfig]] = None


@dataclass
class TopicConfig(PropertyType):
    TYPE = "Type"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    DEFINITION = "Definition"
    OUTPUT_ENABLED = "OutputEnabled"
    EXAMPLES = "Examples"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "definition": "Definition",
        "output_enabled": "OutputEnabled",
        "examples": "Examples",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    definition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    examples: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TopicPolicyConfig(PropertyType):
    TOPICS_TIER_CONFIG = "TopicsTierConfig"
    TOPICS_CONFIG = "TopicsConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topics_tier_config": "TopicsTierConfig",
        "topics_config": "TopicsConfig",
    }

    topics_tier_config: Optional[TopicsTierConfig] = None
    topics_config: Optional[list[TopicConfig]] = None


@dataclass
class TopicsTierConfig(PropertyType):
    TIER_NAME = "TierName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tier_name": "TierName",
    }

    tier_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WordConfig(PropertyType):
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
        "text": "Text",
    }

    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WordPolicyConfig(PropertyType):
    MANAGED_WORD_LISTS_CONFIG = "ManagedWordListsConfig"
    WORDS_CONFIG = "WordsConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_word_lists_config": "ManagedWordListsConfig",
        "words_config": "WordsConfig",
    }

    managed_word_lists_config: Optional[list[ManagedWordsConfig]] = None
    words_config: Optional[list[WordConfig]] = None

