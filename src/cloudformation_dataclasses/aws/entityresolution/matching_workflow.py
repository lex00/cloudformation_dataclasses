"""PropertyTypes for AWS::EntityResolution::MatchingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AttributeMatchingModel:
    """AttributeMatchingModel enum values."""

    ONE_TO_ONE = "ONE_TO_ONE"
    MANY_TO_MANY = "MANY_TO_MANY"


class DeleteUniqueIdErrorType:
    """DeleteUniqueIdErrorType enum values."""

    SERVICE_ERROR = "SERVICE_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"


class DeleteUniqueIdStatus:
    """DeleteUniqueIdStatus enum values."""

    COMPLETED = "COMPLETED"
    ACCEPTED = "ACCEPTED"


class IdMappingIncrementalRunType:
    """IdMappingIncrementalRunType enum values."""

    ON_DEMAND = "ON_DEMAND"


class IdMappingType:
    """IdMappingType enum values."""

    PROVIDER = "PROVIDER"
    RULE_BASED = "RULE_BASED"


class IdMappingWorkflowRuleDefinitionType:
    """IdMappingWorkflowRuleDefinitionType enum values."""

    SOURCE = "SOURCE"
    TARGET = "TARGET"


class IdNamespaceType:
    """IdNamespaceType enum values."""

    SOURCE = "SOURCE"
    TARGET = "TARGET"


class IncrementalRunType:
    """IncrementalRunType enum values."""

    IMMEDIATE = "IMMEDIATE"


class JobStatus:
    """JobStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    QUEUED = "QUEUED"


class JobType:
    """JobType enum values."""

    BATCH = "BATCH"
    INCREMENTAL = "INCREMENTAL"
    DELETE_ONLY = "DELETE_ONLY"


class MatchPurpose:
    """MatchPurpose enum values."""

    IDENTIFIER_GENERATION = "IDENTIFIER_GENERATION"
    INDEXING = "INDEXING"


class ProcessingType:
    """ProcessingType enum values."""

    CONSISTENT = "CONSISTENT"
    EVENTUAL = "EVENTUAL"
    EVENTUAL_NO_LOOKUP = "EVENTUAL_NO_LOOKUP"


class RecordMatchingModel:
    """RecordMatchingModel enum values."""

    ONE_SOURCE_TO_ONE_TARGET = "ONE_SOURCE_TO_ONE_TARGET"
    MANY_SOURCE_TO_ONE_TARGET = "MANY_SOURCE_TO_ONE_TARGET"


class ResolutionType:
    """ResolutionType enum values."""

    RULE_MATCHING = "RULE_MATCHING"
    ML_MATCHING = "ML_MATCHING"
    PROVIDER = "PROVIDER"


class SchemaAttributeType:
    """SchemaAttributeType enum values."""

    NAME = "NAME"
    NAME_FIRST = "NAME_FIRST"
    NAME_MIDDLE = "NAME_MIDDLE"
    NAME_LAST = "NAME_LAST"
    ADDRESS = "ADDRESS"
    ADDRESS_STREET1 = "ADDRESS_STREET1"
    ADDRESS_STREET2 = "ADDRESS_STREET2"
    ADDRESS_STREET3 = "ADDRESS_STREET3"
    ADDRESS_CITY = "ADDRESS_CITY"
    ADDRESS_STATE = "ADDRESS_STATE"
    ADDRESS_COUNTRY = "ADDRESS_COUNTRY"
    ADDRESS_POSTALCODE = "ADDRESS_POSTALCODE"
    PHONE = "PHONE"
    PHONE_NUMBER = "PHONE_NUMBER"
    PHONE_COUNTRYCODE = "PHONE_COUNTRYCODE"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    UNIQUE_ID = "UNIQUE_ID"
    DATE = "DATE"
    STRING = "STRING"
    PROVIDER_ID = "PROVIDER_ID"
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    MAID = "MAID"


class ServiceType:
    """ServiceType enum values."""

    ASSIGNMENT = "ASSIGNMENT"
    ID_MAPPING = "ID_MAPPING"


class StatementEffect:
    """StatementEffect enum values."""

    ALLOW = "Allow"
    DENY = "Deny"


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

