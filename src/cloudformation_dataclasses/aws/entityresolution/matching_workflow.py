"""PropertyTypes for AWS::EntityResolution::MatchingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IncrementalRunConfig(PropertyType):
    INCREMENTAL_RUN_TYPE = "IncrementalRunType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "incremental_run_type": "IncrementalRunType",
    }

    incremental_run_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSource(PropertyType):
    APPLY_NORMALIZATION = "ApplyNormalization"
    INPUT_SOURCE_ARN = "InputSourceARN"
    SCHEMA_ARN = "SchemaArn"

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
    INTERMEDIATE_S3_PATH = "IntermediateS3Path"

    _property_mappings: ClassVar[dict[str, str]] = {
        "intermediate_s3_path": "IntermediateS3Path",
    }

    intermediate_s3_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputAttribute(PropertyType):
    HASHED = "Hashed"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hashed": "Hashed",
        "name": "Name",
    }

    hashed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputSource(PropertyType):
    KMS_ARN = "KMSArn"
    OUTPUT_S3_PATH = "OutputS3Path"
    OUTPUT = "Output"
    APPLY_NORMALIZATION = "ApplyNormalization"

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
    INTERMEDIATE_SOURCE_CONFIGURATION = "IntermediateSourceConfiguration"
    PROVIDER_SERVICE_ARN = "ProviderServiceArn"
    PROVIDER_CONFIGURATION = "ProviderConfiguration"

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
    RULE_BASED_PROPERTIES = "RuleBasedProperties"
    PROVIDER_PROPERTIES = "ProviderProperties"
    RESOLUTION_TYPE = "ResolutionType"
    RULE_CONDITION_PROPERTIES = "RuleConditionProperties"

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
    MATCHING_KEYS = "MatchingKeys"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "matching_keys": "MatchingKeys",
        "rule_name": "RuleName",
    }

    matching_keys: Optional[Union[list[str], Ref]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleBasedProperties(PropertyType):
    ATTRIBUTE_MATCHING_MODEL = "AttributeMatchingModel"
    MATCH_PURPOSE = "MatchPurpose"
    RULES = "Rules"

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
    CONDITION = "Condition"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "rule_name": "RuleName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleConditionProperties(PropertyType):
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[RuleCondition]] = None

