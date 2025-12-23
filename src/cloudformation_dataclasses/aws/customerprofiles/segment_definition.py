"""PropertyTypes for AWS::CustomerProfiles::SegmentDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AddressDimension(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class CalculatedAttributeDimension(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "range": "Range",
    }

    range: Optional[RangeOverride] = None


@dataclass
class DateDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Dimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "calculated_attributes": "CalculatedAttributes",
        "profile_attributes": "ProfileAttributes",
    }

    calculated_attributes: Optional[dict[str, Any]] = None
    profile_attributes: Optional[ProfileAttributes] = None


@dataclass
class ExtraLengthValueProfileDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Group(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class ProfileTypeDimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class RangeOverride(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "groups": "Groups",
        "include": "Include",
    }

    groups: Optional[list[Group]] = None
    include: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceSegment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_definition_name": "SegmentDefinitionName",
    }

    segment_definition_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

