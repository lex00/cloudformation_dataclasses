"""PropertyTypes for AWS::Budgets::BudgetsAction."""

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
class ActionThreshold(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Definition(PropertyType):
    SSM_ACTION_DEFINITION = "SsmActionDefinition"
    IAM_ACTION_DEFINITION = "IamActionDefinition"
    SCP_ACTION_DEFINITION = "ScpActionDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssm_action_definition": "SsmActionDefinition",
        "iam_action_definition": "IamActionDefinition",
        "scp_action_definition": "ScpActionDefinition",
    }

    ssm_action_definition: Optional[SsmActionDefinition] = None
    iam_action_definition: Optional[IamActionDefinition] = None
    scp_action_definition: Optional[ScpActionDefinition] = None


@dataclass
class IamActionDefinition(PropertyType):
    POLICY_ARN = "PolicyArn"
    GROUPS = "Groups"
    ROLES = "Roles"
    USERS = "Users"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_arn": "PolicyArn",
        "groups": "Groups",
        "roles": "Roles",
        "users": "Users",
    }

    policy_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[list[str], Ref]] = None
    roles: Optional[Union[list[str], Ref]] = None
    users: Optional[Union[list[str], Ref]] = None


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
class ScpActionDefinition(PropertyType):
    TARGET_IDS = "TargetIds"
    POLICY_ID = "PolicyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_ids": "TargetIds",
        "policy_id": "PolicyId",
    }

    target_ids: Optional[Union[list[str], Ref]] = None
    policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SsmActionDefinition(PropertyType):
    REGION = "Region"
    INSTANCE_IDS = "InstanceIds"
    SUBTYPE = "Subtype"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
        "instance_ids": "InstanceIds",
        "subtype": "Subtype",
    }

    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_ids: Optional[Union[list[str], Ref]] = None
    subtype: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subscriber(PropertyType):
    TYPE = "Type"
    ADDRESS = "Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "address": "Address",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None

