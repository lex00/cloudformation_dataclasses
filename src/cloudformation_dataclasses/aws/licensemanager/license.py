"""PropertyTypes for AWS::LicenseManager::License."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

