"""PropertyTypes for AWS::BillingConductor::CustomLineItem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AssociateResourceErrorReason:
    """AssociateResourceErrorReason enum values."""

    INVALID_ARN = "INVALID_ARN"
    SERVICE_LIMIT_EXCEEDED = "SERVICE_LIMIT_EXCEEDED"
    ILLEGAL_CUSTOMLINEITEM = "ILLEGAL_CUSTOMLINEITEM"
    INTERNAL_SERVER_EXCEPTION = "INTERNAL_SERVER_EXCEPTION"
    INVALID_BILLING_PERIOD_RANGE = "INVALID_BILLING_PERIOD_RANGE"


class BillingGroupStatus:
    """BillingGroupStatus enum values."""

    ACTIVE = "ACTIVE"
    PRIMARY_ACCOUNT_MISSING = "PRIMARY_ACCOUNT_MISSING"
    PENDING = "PENDING"


class BillingGroupType:
    """BillingGroupType enum values."""

    STANDARD = "STANDARD"
    TRANSFER_BILLING = "TRANSFER_BILLING"


class ComputationRuleEnum:
    """ComputationRuleEnum enum values."""

    ITEMIZED = "ITEMIZED"
    CONSOLIDATED = "CONSOLIDATED"


class ConflictExceptionReason:
    """ConflictExceptionReason enum values."""

    RESOURCE_NAME_CONFLICT = "RESOURCE_NAME_CONFLICT"
    PRICING_RULE_IN_PRICING_PLAN_CONFLICT = "PRICING_RULE_IN_PRICING_PLAN_CONFLICT"
    PRICING_PLAN_ATTACHED_TO_BILLING_GROUP_DELETE_CONFLICT = "PRICING_PLAN_ATTACHED_TO_BILLING_GROUP_DELETE_CONFLICT"
    PRICING_RULE_ATTACHED_TO_PRICING_PLAN_DELETE_CONFLICT = "PRICING_RULE_ATTACHED_TO_PRICING_PLAN_DELETE_CONFLICT"
    WRITE_CONFLICT_RETRY = "WRITE_CONFLICT_RETRY"


class CurrencyCode:
    """CurrencyCode enum values."""

    USD = "USD"
    CNY = "CNY"


class CustomLineItemRelationship:
    """CustomLineItemRelationship enum values."""

    PARENT = "PARENT"
    CHILD = "CHILD"


class CustomLineItemType:
    """CustomLineItemType enum values."""

    CREDIT = "CREDIT"
    FEE = "FEE"


class GroupByAttributeName:
    """GroupByAttributeName enum values."""

    PRODUCT_NAME = "PRODUCT_NAME"
    BILLING_PERIOD = "BILLING_PERIOD"


class LineItemFilterAttributeName:
    """LineItemFilterAttributeName enum values."""

    LINE_ITEM_TYPE = "LINE_ITEM_TYPE"
    SERVICE = "SERVICE"


class LineItemFilterValue:
    """LineItemFilterValue enum values."""

    SAVINGS_PLAN_NEGATION = "SAVINGS_PLAN_NEGATION"


class MatchOption:
    """MatchOption enum values."""

    NOT_EQUAL = "NOT_EQUAL"
    EQUAL = "EQUAL"


class PricingRuleScope:
    """PricingRuleScope enum values."""

    GLOBAL = "GLOBAL"
    SERVICE = "SERVICE"
    BILLING_ENTITY = "BILLING_ENTITY"
    SKU = "SKU"


class PricingRuleType:
    """PricingRuleType enum values."""

    MARKUP = "MARKUP"
    DISCOUNT = "DISCOUNT"
    TIERING = "TIERING"


class SearchOption:
    """SearchOption enum values."""

    STARTS_WITH = "STARTS_WITH"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"
    PRIMARY_NOT_ASSOCIATED = "PRIMARY_NOT_ASSOCIATED"
    PRIMARY_CANNOT_DISASSOCIATE = "PRIMARY_CANNOT_DISASSOCIATE"
    ACCOUNTS_NOT_ASSOCIATED = "ACCOUNTS_NOT_ASSOCIATED"
    ACCOUNTS_ALREADY_ASSOCIATED = "ACCOUNTS_ALREADY_ASSOCIATED"
    ILLEGAL_PRIMARY_ACCOUNT = "ILLEGAL_PRIMARY_ACCOUNT"
    ILLEGAL_ACCOUNTS = "ILLEGAL_ACCOUNTS"
    MISMATCHED_BILLINGGROUP_ARN = "MISMATCHED_BILLINGGROUP_ARN"
    MISSING_BILLINGGROUP = "MISSING_BILLINGGROUP"
    MISMATCHED_CUSTOMLINEITEM_ARN = "MISMATCHED_CUSTOMLINEITEM_ARN"
    ILLEGAL_BILLING_PERIOD = "ILLEGAL_BILLING_PERIOD"
    ILLEGAL_BILLING_PERIOD_RANGE = "ILLEGAL_BILLING_PERIOD_RANGE"
    TOO_MANY_ACCOUNTS_IN_REQUEST = "TOO_MANY_ACCOUNTS_IN_REQUEST"
    DUPLICATE_ACCOUNT = "DUPLICATE_ACCOUNT"
    INVALID_BILLING_GROUP_STATUS = "INVALID_BILLING_GROUP_STATUS"
    MISMATCHED_PRICINGPLAN_ARN = "MISMATCHED_PRICINGPLAN_ARN"
    MISSING_PRICINGPLAN = "MISSING_PRICINGPLAN"
    MISMATCHED_PRICINGRULE_ARN = "MISMATCHED_PRICINGRULE_ARN"
    DUPLICATE_PRICINGRULE_ARNS = "DUPLICATE_PRICINGRULE_ARNS"
    MISSING_COSTCATEGORY = "MISSING_COSTCATEGORY"
    ILLEGAL_EXPRESSION = "ILLEGAL_EXPRESSION"
    ILLEGAL_SCOPE = "ILLEGAL_SCOPE"
    ILLEGAL_SERVICE = "ILLEGAL_SERVICE"
    PRICINGRULES_NOT_EXIST = "PRICINGRULES_NOT_EXIST"
    PRICINGRULES_ALREADY_ASSOCIATED = "PRICINGRULES_ALREADY_ASSOCIATED"
    PRICINGRULES_NOT_ASSOCIATED = "PRICINGRULES_NOT_ASSOCIATED"
    INVALID_TIME_RANGE = "INVALID_TIME_RANGE"
    INVALID_BILLINGVIEW_ARN = "INVALID_BILLINGVIEW_ARN"
    MISMATCHED_BILLINGVIEW_ARN = "MISMATCHED_BILLINGVIEW_ARN"
    ILLEGAL_CUSTOMLINEITEM = "ILLEGAL_CUSTOMLINEITEM"
    MISSING_CUSTOMLINEITEM = "MISSING_CUSTOMLINEITEM"
    ILLEGAL_CUSTOMLINEITEM_UPDATE = "ILLEGAL_CUSTOMLINEITEM_UPDATE"
    TOO_MANY_CUSTOMLINEITEMS_IN_REQUEST = "TOO_MANY_CUSTOMLINEITEMS_IN_REQUEST"
    ILLEGAL_CHARGE_DETAILS = "ILLEGAL_CHARGE_DETAILS"
    ILLEGAL_UPDATE_CHARGE_DETAILS = "ILLEGAL_UPDATE_CHARGE_DETAILS"
    INVALID_ARN = "INVALID_ARN"
    ILLEGAL_RESOURCE_ARNS = "ILLEGAL_RESOURCE_ARNS"
    ILLEGAL_CUSTOMLINEITEM_MODIFICATION = "ILLEGAL_CUSTOMLINEITEM_MODIFICATION"
    MISSING_LINKED_ACCOUNT_IDS = "MISSING_LINKED_ACCOUNT_IDS"
    MULTIPLE_LINKED_ACCOUNT_IDS = "MULTIPLE_LINKED_ACCOUNT_IDS"
    MISSING_PRICING_PLAN_ARN = "MISSING_PRICING_PLAN_ARN"
    MULTIPLE_PRICING_PLAN_ARN = "MULTIPLE_PRICING_PLAN_ARN"
    ILLEGAL_CHILD_ASSOCIATE_RESOURCE = "ILLEGAL_CHILD_ASSOCIATE_RESOURCE"
    CUSTOM_LINE_ITEM_ASSOCIATION_EXISTS = "CUSTOM_LINE_ITEM_ASSOCIATION_EXISTS"
    INVALID_BILLING_GROUP = "INVALID_BILLING_GROUP"
    INVALID_BILLING_PERIOD_FOR_OPERATION = "INVALID_BILLING_PERIOD_FOR_OPERATION"
    ILLEGAL_BILLING_ENTITY = "ILLEGAL_BILLING_ENTITY"
    ILLEGAL_MODIFIER_PERCENTAGE = "ILLEGAL_MODIFIER_PERCENTAGE"
    ILLEGAL_TYPE = "ILLEGAL_TYPE"
    ILLEGAL_BILLING_GROUP_TYPE = "ILLEGAL_BILLING_GROUP_TYPE"
    ILLEGAL_BILLING_GROUP_PRICING_PLAN = "ILLEGAL_BILLING_GROUP_PRICING_PLAN"
    ILLEGAL_ENDED_BILLINGGROUP = "ILLEGAL_ENDED_BILLINGGROUP"
    ILLEGAL_TIERING_INPUT = "ILLEGAL_TIERING_INPUT"
    ILLEGAL_OPERATION = "ILLEGAL_OPERATION"
    ILLEGAL_USAGE_TYPE = "ILLEGAL_USAGE_TYPE"
    INVALID_SKU_COMBO = "INVALID_SKU_COMBO"
    INVALID_FILTER = "INVALID_FILTER"
    TOO_MANY_AUTO_ASSOCIATE_BILLING_GROUPS = "TOO_MANY_AUTO_ASSOCIATE_BILLING_GROUPS"
    CANNOT_DELETE_AUTO_ASSOCIATE_BILLING_GROUP = "CANNOT_DELETE_AUTO_ASSOCIATE_BILLING_GROUP"
    ILLEGAL_ACCOUNT_ID = "ILLEGAL_ACCOUNT_ID"
    BILLING_GROUP_ALREADY_EXIST_IN_CURRENT_BILLING_PERIOD = "BILLING_GROUP_ALREADY_EXIST_IN_CURRENT_BILLING_PERIOD"
    ILLEGAL_COMPUTATION_RULE = "ILLEGAL_COMPUTATION_RULE"
    ILLEGAL_LINE_ITEM_FILTER = "ILLEGAL_LINE_ITEM_FILTER"


@dataclass
class BillingPeriodRange(PropertyType):
    EXCLUSIVE_END_BILLING_PERIOD = "ExclusiveEndBillingPeriod"
    INCLUSIVE_START_BILLING_PERIOD = "InclusiveStartBillingPeriod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclusive_end_billing_period": "ExclusiveEndBillingPeriod",
        "inclusive_start_billing_period": "InclusiveStartBillingPeriod",
    }

    exclusive_end_billing_period: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusive_start_billing_period: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomLineItemChargeDetails(PropertyType):
    LINE_ITEM_FILTERS = "LineItemFilters"
    TYPE = "Type"
    PERCENTAGE = "Percentage"
    FLAT = "Flat"

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
    CHARGE_VALUE = "ChargeValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "charge_value": "ChargeValue",
    }

    charge_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class CustomLineItemPercentageChargeDetails(PropertyType):
    CHILD_ASSOCIATED_RESOURCES = "ChildAssociatedResources"
    PERCENTAGE_VALUE = "PercentageValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "child_associated_resources": "ChildAssociatedResources",
        "percentage_value": "PercentageValue",
    }

    child_associated_resources: Optional[Union[list[str], Ref]] = None
    percentage_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LineItemFilter(PropertyType):
    MATCH_OPTION = "MatchOption"
    ATTRIBUTE = "Attribute"
    ATTRIBUTE_VALUES = "AttributeValues"
    VALUES = "Values"

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
    SERVICE = "Service"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service": "Service",
    }

    service: Optional[Union[str, Ref, GetAtt, Sub]] = None

