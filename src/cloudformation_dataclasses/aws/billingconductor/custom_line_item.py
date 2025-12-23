"""PropertyTypes for AWS::BillingConductor::CustomLineItem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BillingPeriodRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exclusive_end_billing_period": "ExclusiveEndBillingPeriod",
        "inclusive_start_billing_period": "InclusiveStartBillingPeriod",
    }

    exclusive_end_billing_period: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusive_start_billing_period: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomLineItemChargeDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_item_filters": "LineItemFilters",
        "type_": "Type",
        "percentage": "Percentage",
        "flat": "Flat",
    }

    line_item_filters: Optional[list[LineItemFilter]] = None
    type_: Optional[Union[str, CustomLineItemType, Ref, GetAtt, Sub]] = None
    percentage: Optional[CustomLineItemPercentageChargeDetails] = None
    flat: Optional[CustomLineItemFlatChargeDetails] = None


@dataclass
class CustomLineItemFlatChargeDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "charge_value": "ChargeValue",
    }

    charge_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class CustomLineItemPercentageChargeDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "child_associated_resources": "ChildAssociatedResources",
        "percentage_value": "PercentageValue",
    }

    child_associated_resources: Optional[Union[list[str], Ref]] = None
    percentage_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LineItemFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_option": "MatchOption",
        "attribute": "Attribute",
        "attribute_values": "AttributeValues",
        "values": "Values",
    }

    match_option: Optional[Union[str, MatchOption, Ref, GetAtt, Sub]] = None
    attribute: Optional[Union[str, LineItemFilterAttributeName, Ref, GetAtt, Sub]] = None
    attribute_values: Optional[Union[list[str], Ref]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class PresentationDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service": "Service",
    }

    service: Optional[Union[str, Ref, GetAtt, Sub]] = None

