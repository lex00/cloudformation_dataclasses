"""PropertyTypes for AWS::Kendra::Index."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityUnitsConfiguration(PropertyType):
    QUERY_CAPACITY_UNITS = "QueryCapacityUnits"
    STORAGE_CAPACITY_UNITS = "StorageCapacityUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_capacity_units": "QueryCapacityUnits",
        "storage_capacity_units": "StorageCapacityUnits",
    }

    query_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    storage_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentMetadataConfiguration(PropertyType):
    RELEVANCE = "Relevance"
    TYPE = "Type"
    SEARCH = "Search"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "relevance": "Relevance",
        "type_": "Type",
        "search": "Search",
        "name": "Name",
    }

    relevance: Optional[Relevance] = None
    type_: Optional[Union[str, DocumentAttributeValueType, Ref, GetAtt, Sub]] = None
    search: Optional[Search] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JsonTokenTypeConfiguration(PropertyType):
    GROUP_ATTRIBUTE_FIELD = "GroupAttributeField"
    USER_NAME_ATTRIBUTE_FIELD = "UserNameAttributeField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_attribute_field": "GroupAttributeField",
        "user_name_attribute_field": "UserNameAttributeField",
    }

    group_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_name_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JwtTokenTypeConfiguration(PropertyType):
    CLAIM_REGEX = "ClaimRegex"
    ISSUER = "Issuer"
    KEY_LOCATION = "KeyLocation"
    SECRET_MANAGER_ARN = "SecretManagerArn"
    GROUP_ATTRIBUTE_FIELD = "GroupAttributeField"
    URL = "URL"
    USER_NAME_ATTRIBUTE_FIELD = "UserNameAttributeField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "claim_regex": "ClaimRegex",
        "issuer": "Issuer",
        "key_location": "KeyLocation",
        "secret_manager_arn": "SecretManagerArn",
        "group_attribute_field": "GroupAttributeField",
        "url": "URL",
        "user_name_attribute_field": "UserNameAttributeField",
    }

    claim_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_location: Optional[Union[str, KeyLocation, Ref, GetAtt, Sub]] = None
    secret_manager_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_name_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Relevance(PropertyType):
    IMPORTANCE = "Importance"
    RANK_ORDER = "RankOrder"
    VALUE_IMPORTANCE_ITEMS = "ValueImportanceItems"
    FRESHNESS = "Freshness"
    DURATION = "Duration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "importance": "Importance",
        "rank_order": "RankOrder",
        "value_importance_items": "ValueImportanceItems",
        "freshness": "Freshness",
        "duration": "Duration",
    }

    importance: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rank_order: Optional[Union[str, Order, Ref, GetAtt, Sub]] = None
    value_importance_items: Optional[list[ValueImportanceItem]] = None
    freshness: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    duration: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Search(PropertyType):
    DISPLAYABLE = "Displayable"
    SORTABLE = "Sortable"
    FACETABLE = "Facetable"
    SEARCHABLE = "Searchable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "displayable": "Displayable",
        "sortable": "Sortable",
        "facetable": "Facetable",
        "searchable": "Searchable",
    }

    displayable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sortable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    facetable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    searchable: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserTokenConfiguration(PropertyType):
    JWT_TOKEN_TYPE_CONFIGURATION = "JwtTokenTypeConfiguration"
    JSON_TOKEN_TYPE_CONFIGURATION = "JsonTokenTypeConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jwt_token_type_configuration": "JwtTokenTypeConfiguration",
        "json_token_type_configuration": "JsonTokenTypeConfiguration",
    }

    jwt_token_type_configuration: Optional[JwtTokenTypeConfiguration] = None
    json_token_type_configuration: Optional[JsonTokenTypeConfiguration] = None


@dataclass
class ValueImportanceItem(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

