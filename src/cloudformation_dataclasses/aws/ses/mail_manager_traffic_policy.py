"""PropertyTypes for AWS::SES::MailManagerTrafficPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IngressAnalysis(PropertyType):
    ANALYZER = "Analyzer"
    RESULT_FIELD = "ResultField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "analyzer": "Analyzer",
        "result_field": "ResultField",
    }

    analyzer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    result_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressBooleanExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[IngressBooleanToEvaluate] = None


@dataclass
class IngressBooleanToEvaluate(PropertyType):
    IS_IN_ADDRESS_LIST = "IsInAddressList"
    ANALYSIS = "Analysis"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_in_address_list": "IsInAddressList",
        "analysis": "Analysis",
    }

    is_in_address_list: Optional[IngressIsInAddressList] = None
    analysis: Optional[IngressAnalysis] = None


@dataclass
class IngressIpToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressIpv4Expression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[IngressIpToEvaluate] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class IngressIpv6Expression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[IngressIpv6ToEvaluate] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class IngressIpv6ToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressIsInAddressList(PropertyType):
    ATTRIBUTE = "Attribute"
    ADDRESS_LISTS = "AddressLists"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "address_lists": "AddressLists",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address_lists: Optional[Union[list[str], Ref]] = None


@dataclass
class IngressStringExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[IngressStringToEvaluate] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class IngressStringToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"
    ANALYSIS = "Analysis"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "analysis": "Analysis",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    analysis: Optional[IngressAnalysis] = None


@dataclass
class IngressTlsProtocolExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "value": "Value",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[IngressTlsProtocolToEvaluate] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressTlsProtocolToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyCondition(PropertyType):
    IPV6_EXPRESSION = "Ipv6Expression"
    BOOLEAN_EXPRESSION = "BooleanExpression"
    STRING_EXPRESSION = "StringExpression"
    TLS_EXPRESSION = "TlsExpression"
    IP_EXPRESSION = "IpExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_expression": "Ipv6Expression",
        "boolean_expression": "BooleanExpression",
        "string_expression": "StringExpression",
        "tls_expression": "TlsExpression",
        "ip_expression": "IpExpression",
    }

    ipv6_expression: Optional[IngressIpv6Expression] = None
    boolean_expression: Optional[IngressBooleanExpression] = None
    string_expression: Optional[IngressStringExpression] = None
    tls_expression: Optional[IngressTlsProtocolExpression] = None
    ip_expression: Optional[IngressIpv4Expression] = None


@dataclass
class PolicyStatement(PropertyType):
    ACTION = "Action"
    CONDITIONS = "Conditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "conditions": "Conditions",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    conditions: Optional[list[PolicyCondition]] = None

