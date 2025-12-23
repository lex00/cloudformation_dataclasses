"""PropertyTypes for AWS::CleanRooms::ConfiguredTableAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfiguredTableAssociationAnalysisRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
        "type_": "Type",
    }

    policy: Optional[ConfiguredTableAssociationAnalysisRulePolicy] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConfiguredTableAssociationAnalysisRuleAggregation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_result_receivers": "AllowedResultReceivers",
        "allowed_additional_analyses": "AllowedAdditionalAnalyses",
    }

    allowed_result_receivers: Optional[Union[list[str], Ref]] = None
    allowed_additional_analyses: Optional[Union[list[str], Ref]] = None


@dataclass
class ConfiguredTableAssociationAnalysisRuleCustom(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_result_receivers": "AllowedResultReceivers",
        "allowed_additional_analyses": "AllowedAdditionalAnalyses",
    }

    allowed_result_receivers: Optional[Union[list[str], Ref]] = None
    allowed_additional_analyses: Optional[Union[list[str], Ref]] = None


@dataclass
class ConfiguredTableAssociationAnalysisRuleList(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_result_receivers": "AllowedResultReceivers",
        "allowed_additional_analyses": "AllowedAdditionalAnalyses",
    }

    allowed_result_receivers: Optional[Union[list[str], Ref]] = None
    allowed_additional_analyses: Optional[Union[list[str], Ref]] = None


@dataclass
class ConfiguredTableAssociationAnalysisRulePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "v1": "V1",
    }

    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1] = None


@dataclass
class ConfiguredTableAssociationAnalysisRulePolicyV1(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation": "Aggregation",
        "list": "List",
        "custom": "Custom",
    }

    aggregation: Optional[ConfiguredTableAssociationAnalysisRuleAggregation] = None
    list: Optional[ConfiguredTableAssociationAnalysisRuleList] = None
    custom: Optional[ConfiguredTableAssociationAnalysisRuleCustom] = None

