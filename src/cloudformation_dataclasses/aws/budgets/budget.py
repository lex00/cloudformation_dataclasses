"""PropertyTypes for AWS::Budgets::Budget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionStatus:
    """ActionStatus enum values."""

    STANDBY = "STANDBY"
    PENDING = "PENDING"
    EXECUTION_IN_PROGRESS = "EXECUTION_IN_PROGRESS"
    EXECUTION_SUCCESS = "EXECUTION_SUCCESS"
    EXECUTION_FAILURE = "EXECUTION_FAILURE"
    REVERSE_IN_PROGRESS = "REVERSE_IN_PROGRESS"
    REVERSE_SUCCESS = "REVERSE_SUCCESS"
    REVERSE_FAILURE = "REVERSE_FAILURE"
    RESET_IN_PROGRESS = "RESET_IN_PROGRESS"
    RESET_FAILURE = "RESET_FAILURE"


class ActionSubType:
    """ActionSubType enum values."""

    STOP_EC2_INSTANCES = "STOP_EC2_INSTANCES"
    STOP_RDS_INSTANCES = "STOP_RDS_INSTANCES"


class ActionType:
    """ActionType enum values."""

    APPLY_IAM_POLICY = "APPLY_IAM_POLICY"
    APPLY_SCP_POLICY = "APPLY_SCP_POLICY"
    RUN_SSM_DOCUMENTS = "RUN_SSM_DOCUMENTS"


class ApprovalModel:
    """ApprovalModel enum values."""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"


class AutoAdjustType:
    """AutoAdjustType enum values."""

    HISTORICAL = "HISTORICAL"
    FORECAST = "FORECAST"


class BudgetType:
    """BudgetType enum values."""

    USAGE = "USAGE"
    COST = "COST"
    RI_UTILIZATION = "RI_UTILIZATION"
    RI_COVERAGE = "RI_COVERAGE"
    SAVINGS_PLANS_UTILIZATION = "SAVINGS_PLANS_UTILIZATION"
    SAVINGS_PLANS_COVERAGE = "SAVINGS_PLANS_COVERAGE"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    EQUAL_TO = "EQUAL_TO"


class Dimension:
    """Dimension enum values."""

    AZ = "AZ"
    INSTANCE_TYPE = "INSTANCE_TYPE"
    LINKED_ACCOUNT = "LINKED_ACCOUNT"
    LINKED_ACCOUNT_NAME = "LINKED_ACCOUNT_NAME"
    OPERATION = "OPERATION"
    PURCHASE_TYPE = "PURCHASE_TYPE"
    REGION = "REGION"
    SERVICE = "SERVICE"
    SERVICE_CODE = "SERVICE_CODE"
    USAGE_TYPE = "USAGE_TYPE"
    USAGE_TYPE_GROUP = "USAGE_TYPE_GROUP"
    RECORD_TYPE = "RECORD_TYPE"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    TENANCY = "TENANCY"
    SCOPE = "SCOPE"
    PLATFORM = "PLATFORM"
    SUBSCRIPTION_ID = "SUBSCRIPTION_ID"
    LEGAL_ENTITY_NAME = "LEGAL_ENTITY_NAME"
    INVOICING_ENTITY = "INVOICING_ENTITY"
    DEPLOYMENT_OPTION = "DEPLOYMENT_OPTION"
    DATABASE_ENGINE = "DATABASE_ENGINE"
    CACHE_ENGINE = "CACHE_ENGINE"
    INSTANCE_TYPE_FAMILY = "INSTANCE_TYPE_FAMILY"
    BILLING_ENTITY = "BILLING_ENTITY"
    RESERVATION_ID = "RESERVATION_ID"
    RESOURCE_ID = "RESOURCE_ID"
    RIGHTSIZING_TYPE = "RIGHTSIZING_TYPE"
    SAVINGS_PLANS_TYPE = "SAVINGS_PLANS_TYPE"
    SAVINGS_PLAN_ARN = "SAVINGS_PLAN_ARN"
    PAYMENT_OPTION = "PAYMENT_OPTION"
    RESERVATION_MODIFIED = "RESERVATION_MODIFIED"
    TAG_KEY = "TAG_KEY"
    COST_CATEGORY_NAME = "COST_CATEGORY_NAME"


class EventType:
    """EventType enum values."""

    SYSTEM = "SYSTEM"
    CREATE_ACTION = "CREATE_ACTION"
    DELETE_ACTION = "DELETE_ACTION"
    UPDATE_ACTION = "UPDATE_ACTION"
    EXECUTE_ACTION = "EXECUTE_ACTION"


class ExecutionType:
    """ExecutionType enum values."""

    APPROVE_BUDGET_ACTION = "APPROVE_BUDGET_ACTION"
    RETRY_BUDGET_ACTION = "RETRY_BUDGET_ACTION"
    REVERSE_BUDGET_ACTION = "REVERSE_BUDGET_ACTION"
    RESET_BUDGET_ACTION = "RESET_BUDGET_ACTION"


class HealthStatusReason:
    """HealthStatusReason enum values."""

    BILLING_VIEW_NO_ACCESS = "BILLING_VIEW_NO_ACCESS"
    BILLING_VIEW_UNHEALTHY = "BILLING_VIEW_UNHEALTHY"
    FILTER_INVALID = "FILTER_INVALID"
    MULTI_YEAR_HISTORICAL_DATA_DISABLED = "MULTI_YEAR_HISTORICAL_DATA_DISABLED"


class HealthStatusValue:
    """HealthStatusValue enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class MatchOption:
    """MatchOption enum values."""

    EQUALS = "EQUALS"
    ABSENT = "ABSENT"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    CASE_SENSITIVE = "CASE_SENSITIVE"
    CASE_INSENSITIVE = "CASE_INSENSITIVE"


class Metric:
    """Metric enum values."""

    BLENDEDCOST = "BlendedCost"
    UNBLENDEDCOST = "UnblendedCost"
    AMORTIZEDCOST = "AmortizedCost"
    NETUNBLENDEDCOST = "NetUnblendedCost"
    NETAMORTIZEDCOST = "NetAmortizedCost"
    USAGEQUANTITY = "UsageQuantity"
    NORMALIZEDUSAGEAMOUNT = "NormalizedUsageAmount"
    HOURS = "Hours"


class NotificationState:
    """NotificationState enum values."""

    OK = "OK"
    ALARM = "ALARM"


class NotificationType:
    """NotificationType enum values."""

    ACTUAL = "ACTUAL"
    FORECASTED = "FORECASTED"


class SubscriptionType:
    """SubscriptionType enum values."""

    SNS = "SNS"
    EMAIL = "EMAIL"


class ThresholdType:
    """ThresholdType enum values."""

    PERCENTAGE = "PERCENTAGE"
    ABSOLUTE_VALUE = "ABSOLUTE_VALUE"


class TimeUnit:
    """TimeUnit enum values."""

    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    ANNUALLY = "ANNUALLY"
    CUSTOM = "CUSTOM"


@dataclass
class AutoAdjustData(PropertyType):
    AUTO_ADJUST_TYPE = "AutoAdjustType"
    HISTORICAL_OPTIONS = "HistoricalOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_adjust_type": "AutoAdjustType",
        "historical_options": "HistoricalOptions",
    }

    auto_adjust_type: Optional[Union[str, AutoAdjustType, Ref, GetAtt, Sub]] = None
    historical_options: Optional[HistoricalOptions] = None


@dataclass
class BudgetData(PropertyType):
    METRICS = "Metrics"
    BUDGET_LIMIT = "BudgetLimit"
    TIME_PERIOD = "TimePeriod"
    BILLING_VIEW_ARN = "BillingViewArn"
    AUTO_ADJUST_DATA = "AutoAdjustData"
    TIME_UNIT = "TimeUnit"
    PLANNED_BUDGET_LIMITS = "PlannedBudgetLimits"
    COST_FILTERS = "CostFilters"
    FILTER_EXPRESSION = "FilterExpression"
    BUDGET_NAME = "BudgetName"
    COST_TYPES = "CostTypes"
    BUDGET_TYPE = "BudgetType"

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
    MATCH_OPTIONS = "MatchOptions"
    VALUES = "Values"
    KEY = "Key"

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
    INCLUDE_SUPPORT = "IncludeSupport"
    INCLUDE_OTHER_SUBSCRIPTION = "IncludeOtherSubscription"
    INCLUDE_TAX = "IncludeTax"
    INCLUDE_SUBSCRIPTION = "IncludeSubscription"
    USE_BLENDED = "UseBlended"
    INCLUDE_UPFRONT = "IncludeUpfront"
    INCLUDE_DISCOUNT = "IncludeDiscount"
    INCLUDE_CREDIT = "IncludeCredit"
    INCLUDE_RECURRING = "IncludeRecurring"
    USE_AMORTIZED = "UseAmortized"
    INCLUDE_REFUND = "IncludeRefund"

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
    NOT = "Not"
    OR = "Or"
    AND = "And"
    DIMENSIONS = "Dimensions"
    COST_CATEGORIES = "CostCategories"
    TAGS = "Tags"

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
    MATCH_OPTIONS = "MatchOptions"
    VALUES = "Values"
    KEY = "Key"

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
    BUDGET_ADJUSTMENT_PERIOD = "BudgetAdjustmentPeriod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "budget_adjustment_period": "BudgetAdjustmentPeriod",
    }

    budget_adjustment_period: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Notification(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    NOTIFICATION_TYPE = "NotificationType"
    THRESHOLD = "Threshold"
    THRESHOLD_TYPE = "ThresholdType"

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
    SUBSCRIBERS = "Subscribers"
    NOTIFICATION = "Notification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subscribers": "Subscribers",
        "notification": "Notification",
    }

    subscribers: Optional[list[Subscriber]] = None
    notification: Optional[Notification] = None


@dataclass
class ResourceTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Spend(PropertyType):
    AMOUNT = "Amount"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amount": "Amount",
        "unit": "Unit",
    }

    amount: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subscriber(PropertyType):
    SUBSCRIPTION_TYPE = "SubscriptionType"
    ADDRESS = "Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subscription_type": "SubscriptionType",
        "address": "Address",
    }

    subscription_type: Optional[Union[str, SubscriptionType, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagValues(PropertyType):
    MATCH_OPTIONS = "MatchOptions"
    VALUES = "Values"
    KEY = "Key"

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
    START = "Start"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None

