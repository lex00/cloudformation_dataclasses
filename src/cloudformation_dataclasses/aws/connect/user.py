"""PropertyTypes for AWS::Connect::User."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class UserIdentityInfo(PropertyType):
    EMAIL = "Email"
    FIRST_NAME = "FirstName"
    SECONDARY_EMAIL = "SecondaryEmail"
    LAST_NAME = "LastName"
    MOBILE = "Mobile"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email": "Email",
        "first_name": "FirstName",
        "secondary_email": "SecondaryEmail",
        "last_name": "LastName",
        "mobile": "Mobile",
    }

    email: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_email: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mobile: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserPhoneConfig(PropertyType):
    AUTO_ACCEPT = "AutoAccept"
    PHONE_TYPE = "PhoneType"
    PERSISTENT_CONNECTION = "PersistentConnection"
    DESK_PHONE_NUMBER = "DeskPhoneNumber"
    AFTER_CONTACT_WORK_TIME_LIMIT = "AfterContactWorkTimeLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_accept": "AutoAccept",
        "phone_type": "PhoneType",
        "persistent_connection": "PersistentConnection",
        "desk_phone_number": "DeskPhoneNumber",
        "after_contact_work_time_limit": "AfterContactWorkTimeLimit",
    }

    auto_accept: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    phone_type: Optional[Union[str, PhoneType, Ref, GetAtt, Sub]] = None
    persistent_connection: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    desk_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    after_contact_work_time_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class UserProficiency(PropertyType):
    ATTRIBUTE_VALUE = "AttributeValue"
    ATTRIBUTE_NAME = "AttributeName"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_value": "AttributeValue",
        "attribute_name": "AttributeName",
        "level": "Level",
    }

    attribute_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    level: Optional[Union[float, Ref, GetAtt, Sub]] = None

