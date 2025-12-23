"""PropertyTypes for AWS::EntityResolution::IdMappingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IdMappingIncrementalRunConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "incremental_run_type": "IncrementalRunType",
    }

    incremental_run_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdMappingRuleBasedProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_matching_model": "AttributeMatchingModel",
        "rule_definition_type": "RuleDefinitionType",
        "rules": "Rules",
        "record_matching_model": "RecordMatchingModel",
    }

    attribute_matching_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_definition_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[Rule]] = None
    record_matching_model: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdMappingTechniques(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_based_properties": "RuleBasedProperties",
        "provider_properties": "ProviderProperties",
        "id_mapping_type": "IdMappingType",
        "normalization_version": "NormalizationVersion",
    }

    rule_based_properties: Optional[IdMappingRuleBasedProperties] = None
    provider_properties: Optional[ProviderProperties] = None
    id_mapping_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    normalization_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdMappingWorkflowInputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_source_arn": "InputSourceARN",
        "schema_arn": "SchemaArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdMappingWorkflowOutputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_arn": "KMSArn",
        "output_s3_path": "OutputS3Path",
    }

    kms_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntermediateSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intermediate_s3_path": "IntermediateS3Path",
    }

    intermediate_s3_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "matching_keys": "MatchingKeys",
        "rule_name": "RuleName",
    }

    matching_keys: Optional[Union[list[str], Ref]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

