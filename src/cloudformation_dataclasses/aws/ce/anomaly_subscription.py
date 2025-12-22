"""PropertyTypes for AWS::CE::AnomalySubscription."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountScope:
    """AccountScope enum values."""

    PAYER = "PAYER"
    LINKED = "LINKED"


class AnalysisStatus:
    """AnalysisStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class AnalysisType:
    """AnalysisType enum values."""

    MAX_SAVINGS = "MAX_SAVINGS"
    CUSTOM_COMMITMENT = "CUSTOM_COMMITMENT"


class AnomalyFeedbackType:
    """AnomalyFeedbackType enum values."""

    YES = "YES"
    NO = "NO"
    PLANNED_ACTIVITY = "PLANNED_ACTIVITY"


class AnomalySubscriptionFrequency:
    """AnomalySubscriptionFrequency enum values."""

    DAILY = "DAILY"
    IMMEDIATE = "IMMEDIATE"
    WEEKLY = "WEEKLY"


class ApproximationDimension:
    """ApproximationDimension enum values."""

    SERVICE = "SERVICE"
    RESOURCE = "RESOURCE"


class Context:
    """Context enum values."""

    COST_AND_USAGE = "COST_AND_USAGE"
    RESERVATIONS = "RESERVATIONS"
    SAVINGS_PLANS = "SAVINGS_PLANS"


class CostAllocationTagBackfillStatus:
    """CostAllocationTagBackfillStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class CostAllocationTagStatus:
    """CostAllocationTagStatus enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class CostAllocationTagType:
    """CostAllocationTagType enum values."""

    AWSGENERATED = "AWSGenerated"
    USERDEFINED = "UserDefined"


class CostCategoryInheritedValueDimensionName:
    """CostCategoryInheritedValueDimensionName enum values."""

    LINKED_ACCOUNT_NAME = "LINKED_ACCOUNT_NAME"
    TAG = "TAG"


class CostCategoryRuleType:
    """CostCategoryRuleType enum values."""

    REGULAR = "REGULAR"
    INHERITED_VALUE = "INHERITED_VALUE"


class CostCategoryRuleVersion:
    """CostCategoryRuleVersion enum values."""

    COSTCATEGORYEXPRESSION_V1 = "CostCategoryExpression.v1"


class CostCategorySplitChargeMethod:
    """CostCategorySplitChargeMethod enum values."""

    FIXED = "FIXED"
    PROPORTIONAL = "PROPORTIONAL"
    EVEN = "EVEN"


class CostCategorySplitChargeRuleParameterType:
    """CostCategorySplitChargeRuleParameterType enum values."""

    ALLOCATION_PERCENTAGES = "ALLOCATION_PERCENTAGES"


class CostCategoryStatus:
    """CostCategoryStatus enum values."""

    PROCESSING = "PROCESSING"
    APPLIED = "APPLIED"


class CostCategoryStatusComponent:
    """CostCategoryStatusComponent enum values."""

    COST_EXPLORER = "COST_EXPLORER"


class Dimension:
    """Dimension enum values."""

    AZ = "AZ"
    INSTANCE_TYPE = "INSTANCE_TYPE"
    LINKED_ACCOUNT = "LINKED_ACCOUNT"
    PAYER_ACCOUNT = "PAYER_ACCOUNT"
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
    AGREEMENT_END_DATE_TIME_AFTER = "AGREEMENT_END_DATE_TIME_AFTER"
    AGREEMENT_END_DATE_TIME_BEFORE = "AGREEMENT_END_DATE_TIME_BEFORE"
    INVOICING_ENTITY = "INVOICING_ENTITY"
    ANOMALY_TOTAL_IMPACT_ABSOLUTE = "ANOMALY_TOTAL_IMPACT_ABSOLUTE"
    ANOMALY_TOTAL_IMPACT_PERCENTAGE = "ANOMALY_TOTAL_IMPACT_PERCENTAGE"


class ErrorCode:
    """ErrorCode enum values."""

    NO_USAGE_FOUND = "NO_USAGE_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    INVALID_SAVINGS_PLANS_TO_ADD = "INVALID_SAVINGS_PLANS_TO_ADD"
    INVALID_SAVINGS_PLANS_TO_EXCLUDE = "INVALID_SAVINGS_PLANS_TO_EXCLUDE"
    INVALID_ACCOUNT_ID = "INVALID_ACCOUNT_ID"


class FindingReasonCode:
    """FindingReasonCode enum values."""

    CPU_OVER_PROVISIONED = "CPU_OVER_PROVISIONED"
    CPU_UNDER_PROVISIONED = "CPU_UNDER_PROVISIONED"
    MEMORY_OVER_PROVISIONED = "MEMORY_OVER_PROVISIONED"
    MEMORY_UNDER_PROVISIONED = "MEMORY_UNDER_PROVISIONED"
    EBS_THROUGHPUT_OVER_PROVISIONED = "EBS_THROUGHPUT_OVER_PROVISIONED"
    EBS_THROUGHPUT_UNDER_PROVISIONED = "EBS_THROUGHPUT_UNDER_PROVISIONED"
    EBS_IOPS_OVER_PROVISIONED = "EBS_IOPS_OVER_PROVISIONED"
    EBS_IOPS_UNDER_PROVISIONED = "EBS_IOPS_UNDER_PROVISIONED"
    NETWORK_BANDWIDTH_OVER_PROVISIONED = "NETWORK_BANDWIDTH_OVER_PROVISIONED"
    NETWORK_BANDWIDTH_UNDER_PROVISIONED = "NETWORK_BANDWIDTH_UNDER_PROVISIONED"
    NETWORK_PPS_OVER_PROVISIONED = "NETWORK_PPS_OVER_PROVISIONED"
    NETWORK_PPS_UNDER_PROVISIONED = "NETWORK_PPS_UNDER_PROVISIONED"
    DISK_IOPS_OVER_PROVISIONED = "DISK_IOPS_OVER_PROVISIONED"
    DISK_IOPS_UNDER_PROVISIONED = "DISK_IOPS_UNDER_PROVISIONED"
    DISK_THROUGHPUT_OVER_PROVISIONED = "DISK_THROUGHPUT_OVER_PROVISIONED"
    DISK_THROUGHPUT_UNDER_PROVISIONED = "DISK_THROUGHPUT_UNDER_PROVISIONED"


class GenerationStatus:
    """GenerationStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class Granularity:
    """Granularity enum values."""

    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    HOURLY = "HOURLY"


class GroupDefinitionType:
    """GroupDefinitionType enum values."""

    DIMENSION = "DIMENSION"
    TAG = "TAG"
    COST_CATEGORY = "COST_CATEGORY"


class LookbackPeriodInDays:
    """LookbackPeriodInDays enum values."""

    SEVEN_DAYS = "SEVEN_DAYS"
    THIRTY_DAYS = "THIRTY_DAYS"
    SIXTY_DAYS = "SIXTY_DAYS"


class MatchOption:
    """MatchOption enum values."""

    EQUALS = "EQUALS"
    ABSENT = "ABSENT"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CASE_SENSITIVE = "CASE_SENSITIVE"
    CASE_INSENSITIVE = "CASE_INSENSITIVE"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"


class Metric:
    """Metric enum values."""

    BLENDED_COST = "BLENDED_COST"
    UNBLENDED_COST = "UNBLENDED_COST"
    AMORTIZED_COST = "AMORTIZED_COST"
    NET_UNBLENDED_COST = "NET_UNBLENDED_COST"
    NET_AMORTIZED_COST = "NET_AMORTIZED_COST"
    USAGE_QUANTITY = "USAGE_QUANTITY"
    NORMALIZED_USAGE_AMOUNT = "NORMALIZED_USAGE_AMOUNT"


class MonitorDimension:
    """MonitorDimension enum values."""

    SERVICE = "SERVICE"
    LINKED_ACCOUNT = "LINKED_ACCOUNT"
    TAG = "TAG"
    COST_CATEGORY = "COST_CATEGORY"


class MonitorType:
    """MonitorType enum values."""

    DIMENSIONAL = "DIMENSIONAL"
    CUSTOM = "CUSTOM"


class NumericOperator:
    """NumericOperator enum values."""

    EQUAL = "EQUAL"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    BETWEEN = "BETWEEN"


class OfferingClass:
    """OfferingClass enum values."""

    STANDARD = "STANDARD"
    CONVERTIBLE = "CONVERTIBLE"


class PaymentOption:
    """PaymentOption enum values."""

    NO_UPFRONT = "NO_UPFRONT"
    PARTIAL_UPFRONT = "PARTIAL_UPFRONT"
    ALL_UPFRONT = "ALL_UPFRONT"
    LIGHT_UTILIZATION = "LIGHT_UTILIZATION"
    MEDIUM_UTILIZATION = "MEDIUM_UTILIZATION"
    HEAVY_UTILIZATION = "HEAVY_UTILIZATION"


class PlatformDifference:
    """PlatformDifference enum values."""

    HYPERVISOR = "HYPERVISOR"
    NETWORK_INTERFACE = "NETWORK_INTERFACE"
    STORAGE_INTERFACE = "STORAGE_INTERFACE"
    INSTANCE_STORE_AVAILABILITY = "INSTANCE_STORE_AVAILABILITY"
    VIRTUALIZATION_TYPE = "VIRTUALIZATION_TYPE"


class RecommendationTarget:
    """RecommendationTarget enum values."""

    SAME_INSTANCE_FAMILY = "SAME_INSTANCE_FAMILY"
    CROSS_INSTANCE_FAMILY = "CROSS_INSTANCE_FAMILY"


class RightsizingType:
    """RightsizingType enum values."""

    TERMINATE = "TERMINATE"
    MODIFY = "MODIFY"


class SavingsPlansDataType:
    """SavingsPlansDataType enum values."""

    ATTRIBUTES = "ATTRIBUTES"
    UTILIZATION = "UTILIZATION"
    AMORTIZED_COMMITMENT = "AMORTIZED_COMMITMENT"
    SAVINGS = "SAVINGS"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SubscriberStatus:
    """SubscriberStatus enum values."""

    CONFIRMED = "CONFIRMED"
    DECLINED = "DECLINED"


class SubscriberType:
    """SubscriberType enum values."""

    EMAIL = "EMAIL"
    SNS = "SNS"


class SupportedSavingsPlansType:
    """SupportedSavingsPlansType enum values."""

    COMPUTE_SP = "COMPUTE_SP"
    EC2_INSTANCE_SP = "EC2_INSTANCE_SP"
    SAGEMAKER_SP = "SAGEMAKER_SP"
    DATABASE_SP = "DATABASE_SP"


class TermInYears:
    """TermInYears enum values."""

    ONE_YEAR = "ONE_YEAR"
    THREE_YEARS = "THREE_YEARS"


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
class Subscriber(PropertyType):
    STATUS = "Status"
    TYPE = "Type"
    ADDRESS = "Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "type_": "Type",
        "address": "Address",
    }

    status: Optional[Union[str, SubscriberStatus, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SubscriberType, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None

