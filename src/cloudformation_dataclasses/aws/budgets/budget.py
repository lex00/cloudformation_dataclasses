"""PropertyTypes for AWS::Budgets::Budget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoAdjustData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_adjust_type": "AutoAdjustType",
        "historical_options": "HistoricalOptions",
    }

    auto_adjust_type: Optional[Union[str, AutoAdjustType, Ref, GetAtt, Sub]] = None
    historical_options: Optional[HistoricalOptions] = None


@dataclass
class BudgetData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metrics": "Metrics",
        "budget_limit": "BudgetLimit",
        "time_period": "TimePeriod",
        "billing_view_arn": "BillingViewArn",
        "auto_adjust_data": "AutoAdjustData",
        "time_unit": "TimeUnit",
        "planned_budget_limits": "PlannedBudgetLimits",
        "cost_filters": "CostFilters",
        "filter_expression": "FilterExpression",
        "budget_name": "BudgetName",
        "cost_types": "CostTypes",
        "budget_type": "BudgetType",
    }

    metrics: Optional[Union[list[str], Ref]] = None
    budget_limit: Optional[Spend] = None
    time_period: Optional[TimePeriod] = None
    billing_view_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_adjust_data: Optional[AutoAdjustData] = None
    time_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    planned_budget_limits: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    cost_filters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    filter_expression: Optional[Expression] = None
    budget_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cost_types: Optional[CostTypes] = None
    budget_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CostCategoryValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_options": "MatchOptions",
        "values": "Values",
        "key": "Key",
    }

    match_options: Optional[Union[list[str], Ref]] = None
    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CostTypes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_support": "IncludeSupport",
        "include_other_subscription": "IncludeOtherSubscription",
        "include_tax": "IncludeTax",
        "include_subscription": "IncludeSubscription",
        "use_blended": "UseBlended",
        "include_upfront": "IncludeUpfront",
        "include_discount": "IncludeDiscount",
        "include_credit": "IncludeCredit",
        "include_recurring": "IncludeRecurring",
        "use_amortized": "UseAmortized",
        "include_refund": "IncludeRefund",
    }

    include_support: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_other_subscription: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_tax: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_subscription: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_blended: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_upfront: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_discount: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_credit: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_recurring: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_amortized: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_refund: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Expression(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "not_": "Not",
        "or_": "Or",
        "and_": "And",
        "dimensions": "Dimensions",
        "cost_categories": "CostCategories",
        "tags": "Tags",
    }

    not_: Optional[Expression] = None
    or_: Optional[list[Expression]] = None
    and_: Optional[list[Expression]] = None
    dimensions: Optional[ExpressionDimensionValues] = None
    cost_categories: Optional[CostCategoryValues] = None
    tags: Optional[TagValues] = None


@dataclass
class ExpressionDimensionValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_options": "MatchOptions",
        "values": "Values",
        "key": "Key",
    }

    match_options: Optional[Union[list[str], Ref]] = None
    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Dimension, Ref, GetAtt, Sub]] = None


@dataclass
class HistoricalOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "budget_adjustment_period": "BudgetAdjustmentPeriod",
    }

    budget_adjustment_period: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Notification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "notification_type": "NotificationType",
        "threshold": "Threshold",
        "threshold_type": "ThresholdType",
    }

    comparison_operator: Optional[Union[str, ComparisonOperator, Ref, GetAtt, Sub]] = None
    notification_type: Optional[Union[str, NotificationType, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    threshold_type: Optional[Union[str, ThresholdType, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationWithSubscribers(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subscribers": "Subscribers",
        "notification": "Notification",
    }

    subscribers: Optional[list[Subscriber]] = None
    notification: Optional[Notification] = None


@dataclass
class ResourceTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Spend(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "amount": "Amount",
        "unit": "Unit",
    }

    amount: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subscriber(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subscription_type": "SubscriptionType",
        "address": "Address",
    }

    subscription_type: Optional[Union[str, SubscriptionType, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_options": "MatchOptions",
        "values": "Values",
        "key": "Key",
    }

    match_options: Optional[Union[list[str], Ref]] = None
    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimePeriod(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None

