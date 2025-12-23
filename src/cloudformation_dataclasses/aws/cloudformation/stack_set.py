"""PropertyTypes for AWS::CloudFormation::StackSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoDeployment(PropertyType):
    DEPENDS_ON = "DependsOn"
    ENABLED = "Enabled"
    RETAIN_STACKS_ON_ACCOUNT_REMOVAL = "RetainStacksOnAccountRemoval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "depends_on": "DependsOn",
        "enabled": "Enabled",
        "retain_stacks_on_account_removal": "RetainStacksOnAccountRemoval",
    }

    depends_on: Optional[Union[list[str], Ref]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    retain_stacks_on_account_removal: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentTargets(PropertyType):
    ACCOUNT_FILTER_TYPE = "AccountFilterType"
    ACCOUNTS = "Accounts"
    ACCOUNTS_URL = "AccountsUrl"
    ORGANIZATIONAL_UNIT_IDS = "OrganizationalUnitIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_filter_type": "AccountFilterType",
        "accounts": "Accounts",
        "accounts_url": "AccountsUrl",
        "organizational_unit_ids": "OrganizationalUnitIds",
    }

    account_filter_type: Optional[Union[str, AccountFilterType, Ref, GetAtt, Sub]] = None
    accounts: Optional[Union[list[str], Ref]] = None
    accounts_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organizational_unit_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ManagedExecution(PropertyType):
    ACTIVE = "Active"

    _property_mappings: ClassVar[dict[str, str]] = {
        "active": "Active",
    }

    active: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OperationPreferences(PropertyType):
    MAX_CONCURRENT_PERCENTAGE = "MaxConcurrentPercentage"
    REGION_CONCURRENCY_TYPE = "RegionConcurrencyType"
    MAX_CONCURRENT_COUNT = "MaxConcurrentCount"
    FAILURE_TOLERANCE_PERCENTAGE = "FailureTolerancePercentage"
    CONCURRENCY_MODE = "ConcurrencyMode"
    FAILURE_TOLERANCE_COUNT = "FailureToleranceCount"
    REGION_ORDER = "RegionOrder"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_concurrent_percentage": "MaxConcurrentPercentage",
        "region_concurrency_type": "RegionConcurrencyType",
        "max_concurrent_count": "MaxConcurrentCount",
        "failure_tolerance_percentage": "FailureTolerancePercentage",
        "concurrency_mode": "ConcurrencyMode",
        "failure_tolerance_count": "FailureToleranceCount",
        "region_order": "RegionOrder",
    }

    max_concurrent_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    region_concurrency_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_concurrent_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    failure_tolerance_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    concurrency_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    failure_tolerance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    region_order: Optional[Union[list[str], Ref]] = None


@dataclass
class Parameter(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_KEY = "ParameterKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_key": "ParameterKey",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StackInstances(PropertyType):
    PARAMETER_OVERRIDES = "ParameterOverrides"
    DEPLOYMENT_TARGETS = "DeploymentTargets"
    REGIONS = "Regions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_overrides": "ParameterOverrides",
        "deployment_targets": "DeploymentTargets",
        "regions": "Regions",
    }

    parameter_overrides: Optional[list[Parameter]] = None
    deployment_targets: Optional[DeploymentTargets] = None
    regions: Optional[Union[list[str], Ref]] = None

