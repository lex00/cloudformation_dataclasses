"""PropertyTypes for AWS::ACMPCA::Certificate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApiPassthrough(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "extensions": "Extensions",
        "subject": "Subject",
    }

    extensions: Optional[Extensions] = None
    subject: Optional[Subject] = None


@dataclass
class CustomAttribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "object_identifier": "ObjectIdentifier",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomExtension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "critical": "Critical",
        "object_identifier": "ObjectIdentifier",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    critical: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EdiPartyName(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "party_name": "PartyName",
        "name_assigner": "NameAssigner",
    }

    party_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name_assigner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExtendedKeyUsage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "extended_key_usage_type": "ExtendedKeyUsageType",
        "extended_key_usage_object_identifier": "ExtendedKeyUsageObjectIdentifier",
    }

    extended_key_usage_type: Optional[Union[str, ExtendedKeyUsageType, Ref, GetAtt, Sub]] = None
    extended_key_usage_object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Extensions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_extensions": "CustomExtensions",
        "certificate_policies": "CertificatePolicies",
        "key_usage": "KeyUsage",
        "subject_alternative_names": "SubjectAlternativeNames",
        "extended_key_usage": "ExtendedKeyUsage",
    }

    custom_extensions: Optional[list[CustomExtension]] = None
    certificate_policies: Optional[list[PolicyInformation]] = None
    key_usage: Optional[KeyUsage] = None
    subject_alternative_names: Optional[list[GeneralName]] = None
    extended_key_usage: Optional[list[ExtendedKeyUsage]] = None


@dataclass
class GeneralName(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uniform_resource_identifier": "UniformResourceIdentifier",
        "dns_name": "DnsName",
        "edi_party_name": "EdiPartyName",
        "registered_id": "RegisteredId",
        "rfc822_name": "Rfc822Name",
        "other_name": "OtherName",
        "ip_address": "IpAddress",
        "directory_name": "DirectoryName",
    }

    uniform_resource_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    edi_party_name: Optional[EdiPartyName] = None
    registered_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rfc822_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    other_name: Optional[OtherName] = None
    ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    directory_name: Optional[Subject] = None


@dataclass
class KeyUsage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_encipherment": "KeyEncipherment",
        "data_encipherment": "DataEncipherment",
        "digital_signature": "DigitalSignature",
        "key_cert_sign": "KeyCertSign",
        "decipher_only": "DecipherOnly",
        "key_agreement": "KeyAgreement",
        "non_repudiation": "NonRepudiation",
        "crl_sign": "CRLSign",
        "encipher_only": "EncipherOnly",
    }

    key_encipherment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_encipherment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    digital_signature: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key_cert_sign: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    decipher_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key_agreement: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    non_repudiation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    crl_sign: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    encipher_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OtherName(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_id": "TypeId",
        "value": "Value",
    }

    type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyInformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cert_policy_id": "CertPolicyId",
        "policy_qualifiers": "PolicyQualifiers",
    }

    cert_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_qualifiers: Optional[list[PolicyQualifierInfo]] = None


@dataclass
class PolicyQualifierInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "qualifier": "Qualifier",
        "policy_qualifier_id": "PolicyQualifierId",
    }

    qualifier: Optional[Qualifier] = None
    policy_qualifier_id: Optional[Union[str, PolicyQualifierId, Ref, GetAtt, Sub]] = None


@dataclass
class Qualifier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cps_uri": "CpsUri",
    }

    cps_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subject(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "organization": "Organization",
        "organizational_unit": "OrganizationalUnit",
        "locality": "Locality",
        "title": "Title",
        "given_name": "GivenName",
        "generation_qualifier": "GenerationQualifier",
        "initials": "Initials",
        "custom_attributes": "CustomAttributes",
        "serial_number": "SerialNumber",
        "state": "State",
        "country": "Country",
        "surname": "Surname",
        "distinguished_name_qualifier": "DistinguishedNameQualifier",
        "common_name": "CommonName",
        "pseudonym": "Pseudonym",
    }

    organization: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organizational_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    locality: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    given_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    generation_qualifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    initials: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_attributes: Optional[list[CustomAttribute]] = None
    serial_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    country: Optional[Union[str, Ref, GetAtt, Sub]] = None
    surname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    distinguished_name_qualifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    common_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pseudonym: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Validity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, ValidityPeriodType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None

