"""PropertyTypes for AWS::ODB::CloudExadataInfrastructure."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Access:
    """Access enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ComputeModel:
    """ComputeModel enum values."""

    ECPU = "ECPU"
    OCPU = "OCPU"


class DayOfWeekName:
    """DayOfWeekName enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DbNodeMaintenanceType:
    """DbNodeMaintenanceType enum values."""

    VMDB_REBOOT_MIGRATION = "VMDB_REBOOT_MIGRATION"


class DbNodeResourceStatus:
    """DbNodeResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    STARTING = "STARTING"


class DbServerPatchingStatus:
    """DbServerPatchingStatus enum values."""

    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"
    SCHEDULED = "SCHEDULED"


class DiskRedundancy:
    """DiskRedundancy enum values."""

    HIGH = "HIGH"
    NORMAL = "NORMAL"


class IamRoleStatus:
    """IamRoleStatus enum values."""

    ASSOCIATING = "ASSOCIATING"
    DISASSOCIATING = "DISASSOCIATING"
    FAILED = "FAILED"
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    PARTIALLY_CONNECTED = "PARTIALLY_CONNECTED"
    UNKNOWN = "UNKNOWN"


class IormLifecycleState:
    """IormLifecycleState enum values."""

    BOOTSTRAPPING = "BOOTSTRAPPING"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    FAILED = "FAILED"
    UPDATING = "UPDATING"


class LicenseModel:
    """LicenseModel enum values."""

    BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"
    LICENSE_INCLUDED = "LICENSE_INCLUDED"


class ManagedResourceStatus:
    """ManagedResourceStatus enum values."""

    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DISABLED = "DISABLED"
    DISABLING = "DISABLING"


class MonthName:
    """MonthName enum values."""

    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"


class Objective:
    """Objective enum values."""

    AUTO = "AUTO"
    BALANCED = "BALANCED"
    BASIC = "BASIC"
    HIGH_THROUGHPUT = "HIGH_THROUGHPUT"
    LOW_LATENCY = "LOW_LATENCY"


class OciOnboardingStatus:
    """OciOnboardingStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    PENDING_LINK_GENERATION = "PENDING_LINK_GENERATION"
    PENDING_CUSTOMER_ACTION = "PENDING_CUSTOMER_ACTION"
    PENDING_INITIALIZATION = "PENDING_INITIALIZATION"
    ACTIVATING = "ACTIVATING"
    ACTIVE_IN_HOME_REGION = "ACTIVE_IN_HOME_REGION"
    ACTIVE = "ACTIVE"
    ACTIVE_LIMITED = "ACTIVE_LIMITED"
    FAILED = "FAILED"
    PUBLIC_OFFER_UNSUPPORTED = "PUBLIC_OFFER_UNSUPPORTED"
    SUSPENDED = "SUSPENDED"
    CANCELED = "CANCELED"


class PatchingModeType:
    """PatchingModeType enum values."""

    ROLLING = "ROLLING"
    NONROLLING = "NONROLLING"


class PreferenceType:
    """PreferenceType enum values."""

    NO_PREFERENCE = "NO_PREFERENCE"
    CUSTOM_PREFERENCE = "CUSTOM_PREFERENCE"


class ResourceStatus:
    """ResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"
    MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"


class ShapeType:
    """ShapeType enum values."""

    AMD = "AMD"
    INTEL = "INTEL"
    INTEL_FLEX_X9 = "INTEL_FLEX_X9"
    AMPERE_FLEX_A1 = "AMPERE_FLEX_A1"


class SupportedAwsIntegration:
    """SupportedAwsIntegration enum values."""

    KMSTDE = "KmsTde"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


class VpcEndpointType:
    """VpcEndpointType enum values."""

    SERVICENETWORK = "SERVICENETWORK"


@dataclass
class CustomerContact(PropertyType):
    EMAIL = "Email"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email": "Email",
    }

    email: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindow(PropertyType):
    CUSTOM_ACTION_TIMEOUT_IN_MINS = "CustomActionTimeoutInMins"
    DAYS_OF_WEEK = "DaysOfWeek"
    PREFERENCE = "Preference"
    LEAD_TIME_IN_WEEKS = "LeadTimeInWeeks"
    MONTHS = "Months"
    PATCHING_MODE = "PatchingMode"
    WEEKS_OF_MONTH = "WeeksOfMonth"
    IS_CUSTOM_ACTION_TIMEOUT_ENABLED = "IsCustomActionTimeoutEnabled"
    HOURS_OF_DAY = "HoursOfDay"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_action_timeout_in_mins": "CustomActionTimeoutInMins",
        "days_of_week": "DaysOfWeek",
        "preference": "Preference",
        "lead_time_in_weeks": "LeadTimeInWeeks",
        "months": "Months",
        "patching_mode": "PatchingMode",
        "weeks_of_month": "WeeksOfMonth",
        "is_custom_action_timeout_enabled": "IsCustomActionTimeoutEnabled",
        "hours_of_day": "HoursOfDay",
    }

    custom_action_timeout_in_mins: Optional[Union[int, Ref, GetAtt, Sub]] = None
    days_of_week: Optional[Union[list[str], Ref]] = None
    preference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lead_time_in_weeks: Optional[Union[int, Ref, GetAtt, Sub]] = None
    months: Optional[Union[list[str], Ref]] = None
    patching_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weeks_of_month: Optional[Union[list[int], Ref]] = None
    is_custom_action_timeout_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hours_of_day: Optional[Union[list[int], Ref]] = None

