"""PropertyTypes for AWS::EntityResolution::MatchingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IncrementalRunConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "incremental_run_type": "IncrementalRunType",
    }

    incremental_run_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "apply_normalization": "ApplyNormalization",
        "input_source_arn": "InputSourceARN",
        "schema_arn": "SchemaArn",
    }

    apply_normalization: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntermediateSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intermediate_s3_path": "IntermediateS3Path",
    }

    intermediate_s3_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputAttribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hashed": "Hashed",
        "name": "Name",
    }

    hashed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_arn": "KMSArn",
        "output_s3_path": "OutputS3Path",
        "output": "Output",
        "apply_normalization": "ApplyNormalization",
    }

    kms_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output: Optional[list[OutputAttribute]] = None
    apply_normalization: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ProviderProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intermediate_source_configuration": "IntermediateSourceConfiguration",
        "provider_service_arn": "ProviderServiceArn",
        "provider_configuration": "ProviderConfiguration",
    }

    intermediate_source_configuration: Optional[IntermediateSourceConfiguration] = None
    provider_service_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provider_configuration: Optional[dict[str, str]] = None


@dataclass
class ResolutionTechniques(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_based_properties": "RuleBasedProperties",
        "provider_properties": "ProviderProperties",
        "resolution_type": "ResolutionType",
        "rule_condition_properties": "RuleConditionProperties",
    }

    rule_based_properties: Optional[RuleBasedProperties] = None
    provider_properties: Optional[ProviderProperties] = None
    resolution_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_condition_properties: Optional[RuleConditionProperties] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "matching_keys": "MatchingKeys",
        "rule_name": "RuleName",
    }

    matching_keys: Optional[Union[list[str], Ref]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleBasedProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_matching_model": "AttributeMatchingModel",
        "match_purpose": "MatchPurpose",
        "rules": "Rules",
    }

    attribute_matching_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_purpose: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[Rule]] = None


@dataclass
class RuleCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "rule_name": "RuleName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleConditionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[RuleCondition]] = None

