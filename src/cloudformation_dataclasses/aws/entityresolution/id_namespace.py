"""PropertyTypes for AWS::EntityResolution::IdNamespace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IdNamespaceIdMappingWorkflowProperties(PropertyType):
    RULE_BASED_PROPERTIES = "RuleBasedProperties"
    PROVIDER_PROPERTIES = "ProviderProperties"
    ID_MAPPING_TYPE = "IdMappingType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_based_properties": "RuleBasedProperties",
        "provider_properties": "ProviderProperties",
        "id_mapping_type": "IdMappingType",
    }

    rule_based_properties: Optional[NamespaceRuleBasedProperties] = None
    provider_properties: Optional[NamespaceProviderProperties] = None
    id_mapping_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdNamespaceInputSource(PropertyType):
    INPUT_SOURCE_ARN = "InputSourceARN"
    SCHEMA_NAME = "SchemaName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
        "schema_name": "SchemaName",
    }

    input_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NamespaceProviderProperties(PropertyType):
    PROVIDER_SERVICE_ARN = "ProviderServiceArn"
    PROVIDER_CONFIGURATION = "ProviderConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "provider_service_arn": "ProviderServiceArn",
        "provider_configuration": "ProviderConfiguration",
    }

    provider_service_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provider_configuration: Optional[dict[str, str]] = None


@dataclass
class NamespaceRuleBasedProperties(PropertyType):
    ATTRIBUTE_MATCHING_MODEL = "AttributeMatchingModel"
    RULE_DEFINITION_TYPES = "RuleDefinitionTypes"
    RECORD_MATCHING_MODELS = "RecordMatchingModels"
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_matching_model": "AttributeMatchingModel",
        "rule_definition_types": "RuleDefinitionTypes",
        "record_matching_models": "RecordMatchingModels",
        "rules": "Rules",
    }

    attribute_matching_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_definition_types: Optional[Union[list[str], Ref]] = None
    record_matching_models: Optional[Union[list[str], Ref]] = None
    rules: Optional[list[Rule]] = None


@dataclass
class Rule(PropertyType):
    MATCHING_KEYS = "MatchingKeys"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "matching_keys": "MatchingKeys",
        "rule_name": "RuleName",
    }

    matching_keys: Optional[Union[list[str], Ref]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

