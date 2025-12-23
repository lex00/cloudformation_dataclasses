"""PropertyTypes for AWS::Wisdom::MessageTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AgentAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "first_name": "FirstName",
        "last_name": "LastName",
    }

    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Content(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "email_message_template_content": "EmailMessageTemplateContent",
        "sms_message_template_content": "SmsMessageTemplateContent",
    }

    email_message_template_content: Optional[EmailMessageTemplateContent] = None
    sms_message_template_content: Optional[SmsMessageTemplateContent] = None


@dataclass
class CustomerProfileAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "profile_id": "ProfileId",
        "billing_city": "BillingCity",
        "gender": "Gender",
        "profile_arn": "ProfileARN",
        "billing_province": "BillingProvince",
        "billing_postal_code": "BillingPostalCode",
        "shipping_address1": "ShippingAddress1",
        "business_name": "BusinessName",
        "shipping_address4": "ShippingAddress4",
        "shipping_address3": "ShippingAddress3",
        "shipping_address2": "ShippingAddress2",
        "mailing_city": "MailingCity",
        "business_phone_number": "BusinessPhoneNumber",
        "city": "City",
        "email_address": "EmailAddress",
        "province": "Province",
        "state": "State",
        "shipping_postal_code": "ShippingPostalCode",
        "country": "Country",
        "shipping_state": "ShippingState",
        "last_name": "LastName",
        "billing_county": "BillingCounty",
        "billing_state": "BillingState",
        "birth_date": "BirthDate",
        "business_email_address": "BusinessEmailAddress",
        "mailing_country": "MailingCountry",
        "postal_code": "PostalCode",
        "shipping_province": "ShippingProvince",
        "mailing_county": "MailingCounty",
        "mobile_phone_number": "MobilePhoneNumber",
        "county": "County",
        "mailing_state": "MailingState",
        "home_phone_number": "HomePhoneNumber",
        "address4": "Address4",
        "mailing_postal_code": "MailingPostalCode",
        "mailing_address3": "MailingAddress3",
        "shipping_country": "ShippingCountry",
        "mailing_address4": "MailingAddress4",
        "shipping_city": "ShippingCity",
        "mailing_address1": "MailingAddress1",
        "mailing_address2": "MailingAddress2",
        "party_type": "PartyType",
        "additional_information": "AdditionalInformation",
        "mailing_province": "MailingProvince",
        "billing_address1": "BillingAddress1",
        "billing_address2": "BillingAddress2",
        "first_name": "FirstName",
        "billing_address3": "BillingAddress3",
        "billing_address4": "BillingAddress4",
        "address2": "Address2",
        "address3": "Address3",
        "custom": "Custom",
        "address1": "Address1",
        "middle_name": "MiddleName",
        "account_number": "AccountNumber",
        "shipping_county": "ShippingCounty",
        "billing_country": "BillingCountry",
        "phone_number": "PhoneNumber",
    }

    profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_city: Optional[Union[str, Ref, GetAtt, Sub]] = None
    gender: Optional[Union[str, Ref, GetAtt, Sub]] = None
    profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_province: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_postal_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_address1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    business_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_address4: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_address3: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_address2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_city: Optional[Union[str, Ref, GetAtt, Sub]] = None
    business_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    city: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    province: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_postal_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    country: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_county: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    birth_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    business_email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_country: Optional[Union[str, Ref, GetAtt, Sub]] = None
    postal_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_province: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_county: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mobile_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    county: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    home_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address4: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_postal_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_address3: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_country: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_address4: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_city: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_address1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_address2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    party_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_information: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mailing_province: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_address1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_address2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_address3: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_address4: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address3: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom: Optional[dict[str, str]] = None
    address1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    middle_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shipping_county: Optional[Union[str, Ref, GetAtt, Sub]] = None
    billing_country: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmailMessageTemplateContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "headers": "Headers",
        "body": "Body",
        "subject": "Subject",
    }

    headers: Optional[list[EmailMessageTemplateHeader]] = None
    body: Optional[EmailMessageTemplateContentBody] = None
    subject: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmailMessageTemplateContentBody(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "plain_text": "PlainText",
        "html": "Html",
    }

    plain_text: Optional[MessageTemplateBodyContentProvider] = None
    html: Optional[MessageTemplateBodyContentProvider] = None


@dataclass
class EmailMessageTemplateHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GroupingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "criteria": "Criteria",
    }

    values: Optional[Union[list[str], Ref]] = None
    criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MessageTemplateAttachment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attachment_name": "AttachmentName",
        "s3_presigned_url": "S3PresignedUrl",
        "attachment_id": "AttachmentId",
    }

    attachment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_presigned_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attachment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MessageTemplateAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "system_attributes": "SystemAttributes",
        "custom_attributes": "CustomAttributes",
        "agent_attributes": "AgentAttributes",
        "customer_profile_attributes": "CustomerProfileAttributes",
    }

    system_attributes: Optional[SystemAttributes] = None
    custom_attributes: Optional[dict[str, str]] = None
    agent_attributes: Optional[AgentAttributes] = None
    customer_profile_attributes: Optional[CustomerProfileAttributes] = None


@dataclass
class MessageTemplateBodyContentProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
    }

    content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SmsMessageTemplateContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "body": "Body",
    }

    body: Optional[SmsMessageTemplateContentBody] = None


@dataclass
class SmsMessageTemplateContentBody(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "plain_text": "PlainText",
    }

    plain_text: Optional[MessageTemplateBodyContentProvider] = None


@dataclass
class SystemAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_endpoint": "CustomerEndpoint",
        "system_endpoint": "SystemEndpoint",
        "name": "Name",
    }

    customer_endpoint: Optional[SystemEndpointAttributes] = None
    system_endpoint: Optional[SystemEndpointAttributes] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SystemEndpointAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None

