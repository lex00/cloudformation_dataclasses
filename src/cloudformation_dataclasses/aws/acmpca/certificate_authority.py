"""PropertyTypes for AWS::ACMPCA::CertificateAuthority."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessDescription(PropertyType):
    ACCESS_METHOD = "AccessMethod"
    ACCESS_LOCATION = "AccessLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_method": "AccessMethod",
        "access_location": "AccessLocation",
    }

    access_method: Optional[AccessMethod] = None
    access_location: Optional[GeneralName] = None


@dataclass
class AccessMethod(PropertyType):
    CUSTOM_OBJECT_IDENTIFIER = "CustomObjectIdentifier"
    ACCESS_METHOD_TYPE = "AccessMethodType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_object_identifier": "CustomObjectIdentifier",
        "access_method_type": "AccessMethodType",
    }

    custom_object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_method_type: Optional[Union[str, AccessMethodType, Ref, GetAtt, Sub]] = None


@dataclass
class CrlConfiguration(PropertyType):
    CRL_DISTRIBUTION_POINT_EXTENSION_CONFIGURATION = "CrlDistributionPointExtensionConfiguration"
    CUSTOM_CNAME = "CustomCname"
    S3_OBJECT_ACL = "S3ObjectAcl"
    CRL_TYPE = "CrlType"
    EXPIRATION_IN_DAYS = "ExpirationInDays"
    ENABLED = "Enabled"
    S3_BUCKET_NAME = "S3BucketName"
    CUSTOM_PATH = "CustomPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "crl_distribution_point_extension_configuration": "CrlDistributionPointExtensionConfiguration",
        "custom_cname": "CustomCname",
        "s3_object_acl": "S3ObjectAcl",
        "crl_type": "CrlType",
        "expiration_in_days": "ExpirationInDays",
        "enabled": "Enabled",
        "s3_bucket_name": "S3BucketName",
        "custom_path": "CustomPath",
    }

    crl_distribution_point_extension_configuration: Optional[CrlDistributionPointExtensionConfiguration] = None
    custom_cname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_acl: Optional[Union[str, S3ObjectAcl, Ref, GetAtt, Sub]] = None
    crl_type: Optional[Union[str, CrlType, Ref, GetAtt, Sub]] = None
    expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CrlDistributionPointExtensionConfiguration(PropertyType):
    OMIT_EXTENSION = "OmitExtension"

    _property_mappings: ClassVar[dict[str, str]] = {
        "omit_extension": "OmitExtension",
    }

    omit_extension: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CsrExtensions(PropertyType):
    KEY_USAGE = "KeyUsage"
    SUBJECT_INFORMATION_ACCESS = "SubjectInformationAccess"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_usage": "KeyUsage",
        "subject_information_access": "SubjectInformationAccess",
    }

    key_usage: Optional[KeyUsage] = None
    subject_information_access: Optional[list[AccessDescription]] = None


@dataclass
class CustomAttribute(PropertyType):
    VALUE = "Value"
    OBJECT_IDENTIFIER = "ObjectIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "object_identifier": "ObjectIdentifier",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EdiPartyName(PropertyType):
    PARTY_NAME = "PartyName"
    NAME_ASSIGNER = "NameAssigner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "party_name": "PartyName",
        "name_assigner": "NameAssigner",
    }

    party_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name_assigner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeneralName(PropertyType):
    UNIFORM_RESOURCE_IDENTIFIER = "UniformResourceIdentifier"
    DNS_NAME = "DnsName"
    EDI_PARTY_NAME = "EdiPartyName"
    REGISTERED_ID = "RegisteredId"
    RFC822_NAME = "Rfc822Name"
    OTHER_NAME = "OtherName"
    IP_ADDRESS = "IpAddress"
    DIRECTORY_NAME = "DirectoryName"

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
    KEY_ENCIPHERMENT = "KeyEncipherment"
    DATA_ENCIPHERMENT = "DataEncipherment"
    DIGITAL_SIGNATURE = "DigitalSignature"
    KEY_CERT_SIGN = "KeyCertSign"
    DECIPHER_ONLY = "DecipherOnly"
    KEY_AGREEMENT = "KeyAgreement"
    NON_REPUDIATION = "NonRepudiation"
    CRL_SIGN = "CRLSign"
    ENCIPHER_ONLY = "EncipherOnly"

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
class OcspConfiguration(PropertyType):
    OCSP_CUSTOM_CNAME = "OcspCustomCname"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ocsp_custom_cname": "OcspCustomCname",
        "enabled": "Enabled",
    }

    ocsp_custom_cname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OtherName(PropertyType):
    TYPE_ID = "TypeId"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_id": "TypeId",
        "value": "Value",
    }

    type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RevocationConfiguration(PropertyType):
    OCSP_CONFIGURATION = "OcspConfiguration"
    CRL_CONFIGURATION = "CrlConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ocsp_configuration": "OcspConfiguration",
        "crl_configuration": "CrlConfiguration",
    }

    ocsp_configuration: Optional[OcspConfiguration] = None
    crl_configuration: Optional[CrlConfiguration] = None


@dataclass
class Subject(PropertyType):
    ORGANIZATION = "Organization"
    ORGANIZATIONAL_UNIT = "OrganizationalUnit"
    LOCALITY = "Locality"
    TITLE = "Title"
    GIVEN_NAME = "GivenName"
    GENERATION_QUALIFIER = "GenerationQualifier"
    INITIALS = "Initials"
    CUSTOM_ATTRIBUTES = "CustomAttributes"
    SERIAL_NUMBER = "SerialNumber"
    STATE = "State"
    COUNTRY = "Country"
    SURNAME = "Surname"
    DISTINGUISHED_NAME_QUALIFIER = "DistinguishedNameQualifier"
    COMMON_NAME = "CommonName"
    PSEUDONYM = "Pseudonym"

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

