"""PropertyTypes for AWS::LicenseManager::License."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActivationOverrideBehavior:
    """ActivationOverrideBehavior enum values."""

    DISTRIBUTED_GRANTS_ONLY = "DISTRIBUTED_GRANTS_ONLY"
    ALL_GRANTS_PERMITTED_BY_ISSUER = "ALL_GRANTS_PERMITTED_BY_ISSUER"


class AllowedOperation:
    """AllowedOperation enum values."""

    CREATEGRANT = "CreateGrant"
    CHECKOUTLICENSE = "CheckoutLicense"
    CHECKOUTBORROWLICENSE = "CheckoutBorrowLicense"
    CHECKINLICENSE = "CheckInLicense"
    EXTENDCONSUMPTIONLICENSE = "ExtendConsumptionLicense"
    LISTPURCHASEDLICENSES = "ListPurchasedLicenses"
    CREATETOKEN = "CreateToken"


class CheckoutType:
    """CheckoutType enum values."""

    PROVISIONAL = "PROVISIONAL"
    PERPETUAL = "PERPETUAL"


class DigitalSignatureMethod:
    """DigitalSignatureMethod enum values."""

    JWT_PS384 = "JWT_PS384"


class EntitlementDataUnit:
    """EntitlementDataUnit enum values."""

    COUNT = "Count"
    NONE = "None"
    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"


class EntitlementUnit:
    """EntitlementUnit enum values."""

    COUNT = "Count"
    NONE = "None"
    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"


class GrantStatus:
    """GrantStatus enum values."""

    PENDING_WORKFLOW = "PENDING_WORKFLOW"
    PENDING_ACCEPT = "PENDING_ACCEPT"
    REJECTED = "REJECTED"
    ACTIVE = "ACTIVE"
    FAILED_WORKFLOW = "FAILED_WORKFLOW"
    DELETED = "DELETED"
    PENDING_DELETE = "PENDING_DELETE"
    DISABLED = "DISABLED"
    WORKFLOW_COMPLETED = "WORKFLOW_COMPLETED"


class InventoryFilterCondition:
    """InventoryFilterCondition enum values."""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    BEGINS_WITH = "BEGINS_WITH"
    CONTAINS = "CONTAINS"


class LicenseAssetGroupStatus:
    """LicenseAssetGroupStatus enum values."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    DELETED = "DELETED"


class LicenseConfigurationStatus:
    """LicenseConfigurationStatus enum values."""

    AVAILABLE = "AVAILABLE"
    DISABLED = "DISABLED"


class LicenseConversionTaskStatus:
    """LicenseConversionTaskStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class LicenseCountingType:
    """LicenseCountingType enum values."""

    VCPU = "vCPU"
    INSTANCE = "Instance"
    CORE = "Core"
    SOCKET = "Socket"


class LicenseDeletionStatus:
    """LicenseDeletionStatus enum values."""

    PENDING_DELETE = "PENDING_DELETE"
    DELETED = "DELETED"


class LicenseStatus:
    """LicenseStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING_AVAILABLE = "PENDING_AVAILABLE"
    DEACTIVATED = "DEACTIVATED"
    SUSPENDED = "SUSPENDED"
    EXPIRED = "EXPIRED"
    PENDING_DELETE = "PENDING_DELETE"
    DELETED = "DELETED"


class ProductCodeType:
    """ProductCodeType enum values."""

    MARKETPLACE = "marketplace"


class ReceivedStatus:
    """ReceivedStatus enum values."""

    PENDING_WORKFLOW = "PENDING_WORKFLOW"
    PENDING_ACCEPT = "PENDING_ACCEPT"
    REJECTED = "REJECTED"
    ACTIVE = "ACTIVE"
    FAILED_WORKFLOW = "FAILED_WORKFLOW"
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    WORKFLOW_COMPLETED = "WORKFLOW_COMPLETED"


class RenewType:
    """RenewType enum values."""

    NONE = "None"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"


class ReportFrequencyType:
    """ReportFrequencyType enum values."""

    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    ONE_TIME = "ONE_TIME"


class ReportType:
    """ReportType enum values."""

    LICENSECONFIGURATIONSUMMARYREPORT = "LicenseConfigurationSummaryReport"
    LICENSECONFIGURATIONUSAGEREPORT = "LicenseConfigurationUsageReport"
    LICENSEASSETGROUPUSAGEREPORT = "LicenseAssetGroupUsageReport"


class ResourceType:
    """ResourceType enum values."""

    EC2_INSTANCE = "EC2_INSTANCE"
    EC2_HOST = "EC2_HOST"
    EC2_AMI = "EC2_AMI"
    RDS = "RDS"
    SYSTEMS_MANAGER_MANAGED_INSTANCE = "SYSTEMS_MANAGER_MANAGED_INSTANCE"


class TokenType:
    """TokenType enum values."""

    REFRESH_TOKEN = "REFRESH_TOKEN"


@dataclass
class BorrowConfiguration(PropertyType):
    ALLOW_EARLY_CHECK_IN = "AllowEarlyCheckIn"
    MAX_TIME_TO_LIVE_IN_MINUTES = "MaxTimeToLiveInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_early_check_in": "AllowEarlyCheckIn",
        "max_time_to_live_in_minutes": "MaxTimeToLiveInMinutes",
    }

    allow_early_check_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_time_to_live_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ConsumptionConfiguration(PropertyType):
    BORROW_CONFIGURATION = "BorrowConfiguration"
    RENEW_TYPE = "RenewType"
    PROVISIONAL_CONFIGURATION = "ProvisionalConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "borrow_configuration": "BorrowConfiguration",
        "renew_type": "RenewType",
        "provisional_configuration": "ProvisionalConfiguration",
    }

    borrow_configuration: Optional[BorrowConfiguration] = None
    renew_type: Optional[Union[str, RenewType, Ref, GetAtt, Sub]] = None
    provisional_configuration: Optional[ProvisionalConfiguration] = None


@dataclass
class Entitlement(PropertyType):
    ALLOW_CHECK_IN = "AllowCheckIn"
    OVERAGE = "Overage"
    VALUE = "Value"
    MAX_COUNT = "MaxCount"
    UNIT = "Unit"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_check_in": "AllowCheckIn",
        "overage": "Overage",
        "value": "Value",
        "max_count": "MaxCount",
        "unit": "Unit",
        "name": "Name",
    }

    allow_check_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    overage: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, EntitlementUnit, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IssuerData(PropertyType):
    SIGN_KEY = "SignKey"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sign_key": "SignKey",
        "name": "Name",
    }

    sign_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Metadata(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisionalConfiguration(PropertyType):
    MAX_TIME_TO_LIVE_IN_MINUTES = "MaxTimeToLiveInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_time_to_live_in_minutes": "MaxTimeToLiveInMinutes",
    }

    max_time_to_live_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ValidityDateFormat(PropertyType):
    BEGIN = "Begin"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "begin": "Begin",
        "end": "End",
    }

    begin: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None

