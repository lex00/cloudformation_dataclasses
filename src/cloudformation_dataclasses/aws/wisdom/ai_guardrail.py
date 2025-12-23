"""PropertyTypes for AWS::Wisdom::AIGuardrail."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AIGuardrailContentPolicyConfig(PropertyType):
    FILTERS_CONFIG = "FiltersConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters_config": "FiltersConfig",
    }

    filters_config: Optional[list[GuardrailContentFilterConfig]] = None


@dataclass
class AIGuardrailContextualGroundingPolicyConfig(PropertyType):
    FILTERS_CONFIG = "FiltersConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters_config": "FiltersConfig",
    }

    filters_config: Optional[list[GuardrailContextualGroundingFilterConfig]] = None


@dataclass
class AIGuardrailSensitiveInformationPolicyConfig(PropertyType):
    REGEXES_CONFIG = "RegexesConfig"
    PII_ENTITIES_CONFIG = "PiiEntitiesConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regexes_config": "RegexesConfig",
        "pii_entities_config": "PiiEntitiesConfig",
    }

    regexes_config: Optional[list[GuardrailRegexConfig]] = None
    pii_entities_config: Optional[list[GuardrailPiiEntityConfig]] = None


@dataclass
class AIGuardrailTopicPolicyConfig(PropertyType):
    TOPICS_CONFIG = "TopicsConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topics_config": "TopicsConfig",
    }

    topics_config: Optional[list[GuardrailTopicConfig]] = None


@dataclass
class AIGuardrailWordPolicyConfig(PropertyType):
    MANAGED_WORD_LISTS_CONFIG = "ManagedWordListsConfig"
    WORDS_CONFIG = "WordsConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_word_lists_config": "ManagedWordListsConfig",
        "words_config": "WordsConfig",
    }

    managed_word_lists_config: Optional[list[GuardrailManagedWordsConfig]] = None
    words_config: Optional[list[GuardrailWordConfig]] = None


@dataclass
class GuardrailContentFilterConfig(PropertyType):
    OUTPUT_STRENGTH = "OutputStrength"
    TYPE = "Type"
    INPUT_STRENGTH = "InputStrength"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_strength": "OutputStrength",
        "type_": "Type",
        "input_strength": "InputStrength",
    }

    output_strength: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_strength: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailContextualGroundingFilterConfig(PropertyType):
    TYPE = "Type"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "threshold": "Threshold",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailManagedWordsConfig(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailPiiEntityConfig(PropertyType):
    TYPE = "Type"
    ACTION = "Action"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "action": "Action",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailRegexConfig(PropertyType):
    PATTERN = "Pattern"
    ACTION = "Action"
    DESCRIPTION = "Description"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
        "action": "Action",
        "description": "Description",
        "name": "Name",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailTopicConfig(PropertyType):
    TYPE = "Type"
    DEFINITION = "Definition"
    EXAMPLES = "Examples"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "definition": "Definition",
        "examples": "Examples",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    definition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    examples: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GuardrailWordConfig(PropertyType):
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None

