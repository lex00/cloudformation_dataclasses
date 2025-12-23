"""PropertyTypes for AWS::QBusiness::DataAccessor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionConfiguration(PropertyType):
    ACTION = "Action"
    FILTER_CONFIGURATION = "FilterConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "filter_configuration": "FilterConfiguration",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter_configuration: Optional[ActionFilterConfiguration] = None


@dataclass
class ActionFilterConfiguration(PropertyType):
    DOCUMENT_ATTRIBUTE_FILTER = "DocumentAttributeFilter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "document_attribute_filter": "DocumentAttributeFilter",
    }

    document_attribute_filter: Optional[AttributeFilter] = None


@dataclass
class AttributeFilter(PropertyType):
    CONTAINS_ANY = "ContainsAny"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    NOT_FILTER = "NotFilter"
    LESS_THAN_OR_EQUALS = "LessThanOrEquals"
    OR_ALL_FILTERS = "OrAllFilters"
    EQUALS_TO = "EqualsTo"
    GREATER_THAN_OR_EQUALS = "GreaterThanOrEquals"
    AND_ALL_FILTERS = "AndAllFilters"
    CONTAINS_ALL = "ContainsAll"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contains_any": "ContainsAny",
        "less_than": "LessThan",
        "greater_than": "GreaterThan",
        "not_filter": "NotFilter",
        "less_than_or_equals": "LessThanOrEquals",
        "or_all_filters": "OrAllFilters",
        "equals_to": "EqualsTo",
        "greater_than_or_equals": "GreaterThanOrEquals",
        "and_all_filters": "AndAllFilters",
        "contains_all": "ContainsAll",
    }

    contains_any: Optional[DocumentAttribute] = None
    less_than: Optional[DocumentAttribute] = None
    greater_than: Optional[DocumentAttribute] = None
    not_filter: Optional[AttributeFilter] = None
    less_than_or_equals: Optional[DocumentAttribute] = None
    or_all_filters: Optional[list[AttributeFilter]] = None
    equals_to: Optional[DocumentAttribute] = None
    greater_than_or_equals: Optional[DocumentAttribute] = None
    and_all_filters: Optional[list[AttributeFilter]] = None
    contains_all: Optional[DocumentAttribute] = None


@dataclass
class DataAccessorAuthenticationConfiguration(PropertyType):
    IDC_TRUSTED_TOKEN_ISSUER_CONFIGURATION = "IdcTrustedTokenIssuerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "idc_trusted_token_issuer_configuration": "IdcTrustedTokenIssuerConfiguration",
    }

    idc_trusted_token_issuer_configuration: Optional[DataAccessorIdcTrustedTokenIssuerConfiguration] = None


@dataclass
class DataAccessorAuthenticationDetail(PropertyType):
    AUTHENTICATION_CONFIGURATION = "AuthenticationConfiguration"
    EXTERNAL_IDS = "ExternalIds"
    AUTHENTICATION_TYPE = "AuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_configuration": "AuthenticationConfiguration",
        "external_ids": "ExternalIds",
        "authentication_type": "AuthenticationType",
    }

    authentication_configuration: Optional[DataAccessorAuthenticationConfiguration] = None
    external_ids: Optional[Union[list[str], Ref]] = None
    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataAccessorIdcTrustedTokenIssuerConfiguration(PropertyType):
    IDC_TRUSTED_TOKEN_ISSUER_ARN = "IdcTrustedTokenIssuerArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "idc_trusted_token_issuer_arn": "IdcTrustedTokenIssuerArn",
    }

    idc_trusted_token_issuer_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentAttribute(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[DocumentAttributeValue] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentAttributeValue(PropertyType):
    DATE_VALUE = "DateValue"
    LONG_VALUE = "LongValue"
    STRING_VALUE = "StringValue"
    STRING_LIST_VALUE = "StringListValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "date_value": "DateValue",
        "long_value": "LongValue",
        "string_value": "StringValue",
        "string_list_value": "StringListValue",
    }

    date_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    long_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_list_value: Optional[Union[list[str], Ref]] = None

