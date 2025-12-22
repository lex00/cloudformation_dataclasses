"""PropertyTypes for AWS::CustomerProfiles::SegmentDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AddressDimension(PropertyType):
    STATE = "State"
    COUNTRY = "Country"
    POSTAL_CODE = "PostalCode"
    CITY = "City"
    COUNTY = "County"
    PROVINCE = "Province"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "country": "Country",
        "postal_code": "PostalCode",
        "city": "City",
        "county": "County",
        "province": "Province",
    }

    state: Optional[ProfileDimension] = None
    country: Optional[ProfileDimension] = None
    postal_code: Optional[ProfileDimension] = None
    city: Optional[ProfileDimension] = None
    county: Optional[ProfileDimension] = None
    province: Optional[ProfileDimension] = None


@dataclass
class AttributeDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class CalculatedAttributeDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"
    CONDITION_OVERRIDES = "ConditionOverrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
        "condition_overrides": "ConditionOverrides",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None
    condition_overrides: Optional[ConditionOverrides] = None


@dataclass
class ConditionOverrides(PropertyType):
    RANGE = "Range"

    _property_mappings: ClassVar[dict[str, str]] = {
        "range": "Range",
    }

    range: Optional[RangeOverride] = None


@dataclass
class DateDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Dimension(PropertyType):
    CALCULATED_ATTRIBUTES = "CalculatedAttributes"
    PROFILE_ATTRIBUTES = "ProfileAttributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "calculated_attributes": "CalculatedAttributes",
        "profile_attributes": "ProfileAttributes",
    }

    calculated_attributes: Optional[dict[str, Any]] = None
    profile_attributes: Optional[ProfileAttributes] = None


@dataclass
class ExtraLengthValueProfileDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Group(PropertyType):
    TYPE = "Type"
    SOURCE_TYPE = "SourceType"
    DIMENSIONS = "Dimensions"
    SOURCE_SEGMENTS = "SourceSegments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "source_type": "SourceType",
        "dimensions": "Dimensions",
        "source_segments": "SourceSegments",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[Dimension]] = None
    source_segments: Optional[list[SourceSegment]] = None


@dataclass
class ProfileAttributes(PropertyType):
    ADDITIONAL_INFORMATION = "AdditionalInformation"
    PROFILE_TYPE = "ProfileType"
    BUSINESS_NAME = "BusinessName"
    ADDRESS = "Address"
    FIRST_NAME = "FirstName"
    PERSONAL_EMAIL_ADDRESS = "PersonalEmailAddress"
    BUSINESS_EMAIL_ADDRESS = "BusinessEmailAddress"
    ATTRIBUTES = "Attributes"
    MAILING_ADDRESS = "MailingAddress"
    BUSINESS_PHONE_NUMBER = "BusinessPhoneNumber"
    MIDDLE_NAME = "MiddleName"
    MOBILE_PHONE_NUMBER = "MobilePhoneNumber"
    EMAIL_ADDRESS = "EmailAddress"
    ACCOUNT_NUMBER = "AccountNumber"
    BILLING_ADDRESS = "BillingAddress"
    GENDER_STRING = "GenderString"
    HOME_PHONE_NUMBER = "HomePhoneNumber"
    SHIPPING_ADDRESS = "ShippingAddress"
    PHONE_NUMBER = "PhoneNumber"
    LAST_NAME = "LastName"
    PARTY_TYPE_STRING = "PartyTypeString"
    BIRTH_DATE = "BirthDate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_information": "AdditionalInformation",
        "profile_type": "ProfileType",
        "business_name": "BusinessName",
        "address": "Address",
        "first_name": "FirstName",
        "personal_email_address": "PersonalEmailAddress",
        "business_email_address": "BusinessEmailAddress",
        "attributes": "Attributes",
        "mailing_address": "MailingAddress",
        "business_phone_number": "BusinessPhoneNumber",
        "middle_name": "MiddleName",
        "mobile_phone_number": "MobilePhoneNumber",
        "email_address": "EmailAddress",
        "account_number": "AccountNumber",
        "billing_address": "BillingAddress",
        "gender_string": "GenderString",
        "home_phone_number": "HomePhoneNumber",
        "shipping_address": "ShippingAddress",
        "phone_number": "PhoneNumber",
        "last_name": "LastName",
        "party_type_string": "PartyTypeString",
        "birth_date": "BirthDate",
    }

    additional_information: Optional[ExtraLengthValueProfileDimension] = None
    profile_type: Optional[ProfileTypeDimension] = None
    business_name: Optional[ProfileDimension] = None
    address: Optional[AddressDimension] = None
    first_name: Optional[ProfileDimension] = None
    personal_email_address: Optional[ProfileDimension] = None
    business_email_address: Optional[ProfileDimension] = None
    attributes: Optional[dict[str, Any]] = None
    mailing_address: Optional[AddressDimension] = None
    business_phone_number: Optional[ProfileDimension] = None
    middle_name: Optional[ProfileDimension] = None
    mobile_phone_number: Optional[ProfileDimension] = None
    email_address: Optional[ProfileDimension] = None
    account_number: Optional[ProfileDimension] = None
    billing_address: Optional[AddressDimension] = None
    gender_string: Optional[ProfileDimension] = None
    home_phone_number: Optional[ProfileDimension] = None
    shipping_address: Optional[AddressDimension] = None
    phone_number: Optional[ProfileDimension] = None
    last_name: Optional[ProfileDimension] = None
    party_type_string: Optional[ProfileDimension] = None
    birth_date: Optional[DateDimension] = None


@dataclass
class ProfileDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class ProfileTypeDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class RangeOverride(PropertyType):
    START = "Start"
    END = "End"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
        "unit": "Unit",
    }

    start: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SegmentGroup(PropertyType):
    GROUPS = "Groups"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "groups": "Groups",
        "include": "Include",
    }

    groups: Optional[list[Group]] = None
    include: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceSegment(PropertyType):
    SEGMENT_DEFINITION_NAME = "SegmentDefinitionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_definition_name": "SegmentDefinitionName",
    }

    segment_definition_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

