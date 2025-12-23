"""PropertyTypes for AWS::AccessAnalyzer::Analyzer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnalysisRule(PropertyType):
    EXCLUSIONS = "Exclusions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclusions": "Exclusions",
    }

    exclusions: Optional[list[AnalysisRuleCriteria]] = None


@dataclass
class AnalysisRuleCriteria(PropertyType):
    ACCOUNT_IDS = "AccountIds"
    RESOURCE_TAGS = "ResourceTags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_ids": "AccountIds",
        "resource_tags": "ResourceTags",
    }

    account_ids: Optional[Union[list[str], Ref]] = None
    resource_tags: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class AnalyzerConfiguration(PropertyType):
    INTERNAL_ACCESS_CONFIGURATION = "InternalAccessConfiguration"
    UNUSED_ACCESS_CONFIGURATION = "UnusedAccessConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "internal_access_configuration": "InternalAccessConfiguration",
        "unused_access_configuration": "UnusedAccessConfiguration",
    }

    internal_access_configuration: Optional[InternalAccessConfiguration] = None
    unused_access_configuration: Optional[UnusedAccessConfiguration] = None


@dataclass
class ArchiveRule(PropertyType):
    FILTER = "Filter"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "rule_name": "RuleName",
    }

    filter: Optional[list[Filter]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Filter(PropertyType):
    EXISTS = "Exists"
    CONTAINS = "Contains"
    NEQ = "Neq"
    EQ = "Eq"
    PROPERTY = "Property"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exists": "Exists",
        "contains": "Contains",
        "neq": "Neq",
        "eq": "Eq",
        "property": "Property",
    }

    exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    contains: Optional[Union[list[str], Ref]] = None
    neq: Optional[Union[list[str], Ref]] = None
    eq: Optional[Union[list[str], Ref]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InternalAccessAnalysisRule(PropertyType):
    INCLUSIONS = "Inclusions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inclusions": "Inclusions",
    }

    inclusions: Optional[list[InternalAccessAnalysisRuleCriteria]] = None


@dataclass
class InternalAccessAnalysisRuleCriteria(PropertyType):
    RESOURCE_TYPES = "ResourceTypes"
    ACCOUNT_IDS = "AccountIds"
    RESOURCE_ARNS = "ResourceArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_types": "ResourceTypes",
        "account_ids": "AccountIds",
        "resource_arns": "ResourceArns",
    }

    resource_types: Optional[Union[list[str], Ref]] = None
    account_ids: Optional[Union[list[str], Ref]] = None
    resource_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class InternalAccessConfiguration(PropertyType):
    INTERNAL_ACCESS_ANALYSIS_RULE = "InternalAccessAnalysisRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "internal_access_analysis_rule": "InternalAccessAnalysisRule",
    }

    internal_access_analysis_rule: Optional[InternalAccessAnalysisRule] = None


@dataclass
class UnusedAccessConfiguration(PropertyType):
    UNUSED_ACCESS_AGE = "UnusedAccessAge"
    ANALYSIS_RULE = "AnalysisRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unused_access_age": "UnusedAccessAge",
        "analysis_rule": "AnalysisRule",
    }

    unused_access_age: Optional[Union[int, Ref, GetAtt, Sub]] = None
    analysis_rule: Optional[AnalysisRule] = None

