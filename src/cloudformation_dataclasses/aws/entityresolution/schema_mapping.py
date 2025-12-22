"""PropertyTypes for AWS::EntityResolution::SchemaMapping."""

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
class SchemaInputAttribute(PropertyType):
    GROUP_NAME = "GroupName"
    TYPE = "Type"
    SUB_TYPE = "SubType"
    HASHED = "Hashed"
    MATCH_KEY = "MatchKey"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "type_": "Type",
        "sub_type": "SubType",
        "hashed": "Hashed",
        "match_key": "MatchKey",
        "field_name": "FieldName",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hashed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    match_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

