"""PropertyTypes for AWS::PCAConnectorAD::Template."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationPolicies(PropertyType):
    POLICIES = "Policies"
    CRITICAL = "Critical"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policies": "Policies",
        "critical": "Critical",
    }

    policies: Optional[list[ApplicationPolicy]] = None
    critical: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationPolicy(PropertyType):
    POLICY_TYPE = "PolicyType"
    POLICY_OBJECT_IDENTIFIER = "PolicyObjectIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_type": "PolicyType",
        "policy_object_identifier": "PolicyObjectIdentifier",
    }

    policy_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CertificateValidity(PropertyType):
    VALIDITY_PERIOD = "ValidityPeriod"
    RENEWAL_PERIOD = "RenewalPeriod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "validity_period": "ValidityPeriod",
        "renewal_period": "RenewalPeriod",
    }

    validity_period: Optional[ValidityPeriod] = None
    renewal_period: Optional[ValidityPeriod] = None


@dataclass
class EnrollmentFlagsV2(PropertyType):
    NO_SECURITY_EXTENSION = "NoSecurityExtension"
    INCLUDE_SYMMETRIC_ALGORITHMS = "IncludeSymmetricAlgorithms"
    USER_INTERACTION_REQUIRED = "UserInteractionRequired"
    ENABLE_KEY_REUSE_ON_NT_TOKEN_KEYSET_STORAGE_FULL = "EnableKeyReuseOnNtTokenKeysetStorageFull"
    REMOVE_INVALID_CERTIFICATE_FROM_PERSONAL_STORE = "RemoveInvalidCertificateFromPersonalStore"

    _property_mappings: ClassVar[dict[str, str]] = {
        "no_security_extension": "NoSecurityExtension",
        "include_symmetric_algorithms": "IncludeSymmetricAlgorithms",
        "user_interaction_required": "UserInteractionRequired",
        "enable_key_reuse_on_nt_token_keyset_storage_full": "EnableKeyReuseOnNtTokenKeysetStorageFull",
        "remove_invalid_certificate_from_personal_store": "RemoveInvalidCertificateFromPersonalStore",
    }

    no_security_extension: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_symmetric_algorithms: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    user_interaction_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_key_reuse_on_nt_token_keyset_storage_full: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    remove_invalid_certificate_from_personal_store: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnrollmentFlagsV3(PropertyType):
    NO_SECURITY_EXTENSION = "NoSecurityExtension"
    INCLUDE_SYMMETRIC_ALGORITHMS = "IncludeSymmetricAlgorithms"
    USER_INTERACTION_REQUIRED = "UserInteractionRequired"
    ENABLE_KEY_REUSE_ON_NT_TOKEN_KEYSET_STORAGE_FULL = "EnableKeyReuseOnNtTokenKeysetStorageFull"
    REMOVE_INVALID_CERTIFICATE_FROM_PERSONAL_STORE = "RemoveInvalidCertificateFromPersonalStore"

    _property_mappings: ClassVar[dict[str, str]] = {
        "no_security_extension": "NoSecurityExtension",
        "include_symmetric_algorithms": "IncludeSymmetricAlgorithms",
        "user_interaction_required": "UserInteractionRequired",
        "enable_key_reuse_on_nt_token_keyset_storage_full": "EnableKeyReuseOnNtTokenKeysetStorageFull",
        "remove_invalid_certificate_from_personal_store": "RemoveInvalidCertificateFromPersonalStore",
    }

    no_security_extension: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_symmetric_algorithms: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    user_interaction_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_key_reuse_on_nt_token_keyset_storage_full: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    remove_invalid_certificate_from_personal_store: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnrollmentFlagsV4(PropertyType):
    NO_SECURITY_EXTENSION = "NoSecurityExtension"
    INCLUDE_SYMMETRIC_ALGORITHMS = "IncludeSymmetricAlgorithms"
    USER_INTERACTION_REQUIRED = "UserInteractionRequired"
    ENABLE_KEY_REUSE_ON_NT_TOKEN_KEYSET_STORAGE_FULL = "EnableKeyReuseOnNtTokenKeysetStorageFull"
    REMOVE_INVALID_CERTIFICATE_FROM_PERSONAL_STORE = "RemoveInvalidCertificateFromPersonalStore"

    _property_mappings: ClassVar[dict[str, str]] = {
        "no_security_extension": "NoSecurityExtension",
        "include_symmetric_algorithms": "IncludeSymmetricAlgorithms",
        "user_interaction_required": "UserInteractionRequired",
        "enable_key_reuse_on_nt_token_keyset_storage_full": "EnableKeyReuseOnNtTokenKeysetStorageFull",
        "remove_invalid_certificate_from_personal_store": "RemoveInvalidCertificateFromPersonalStore",
    }

    no_security_extension: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_symmetric_algorithms: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    user_interaction_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_key_reuse_on_nt_token_keyset_storage_full: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    remove_invalid_certificate_from_personal_store: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ExtensionsV2(PropertyType):
    APPLICATION_POLICIES = "ApplicationPolicies"
    KEY_USAGE = "KeyUsage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_policies": "ApplicationPolicies",
        "key_usage": "KeyUsage",
    }

    application_policies: Optional[ApplicationPolicies] = None
    key_usage: Optional[KeyUsage] = None


@dataclass
class ExtensionsV3(PropertyType):
    APPLICATION_POLICIES = "ApplicationPolicies"
    KEY_USAGE = "KeyUsage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_policies": "ApplicationPolicies",
        "key_usage": "KeyUsage",
    }

    application_policies: Optional[ApplicationPolicies] = None
    key_usage: Optional[KeyUsage] = None


@dataclass
class ExtensionsV4(PropertyType):
    APPLICATION_POLICIES = "ApplicationPolicies"
    KEY_USAGE = "KeyUsage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_policies": "ApplicationPolicies",
        "key_usage": "KeyUsage",
    }

    application_policies: Optional[ApplicationPolicies] = None
    key_usage: Optional[KeyUsage] = None


@dataclass
class GeneralFlagsV2(PropertyType):
    AUTO_ENROLLMENT = "AutoEnrollment"
    MACHINE_TYPE = "MachineType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_enrollment": "AutoEnrollment",
        "machine_type": "MachineType",
    }

    auto_enrollment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GeneralFlagsV3(PropertyType):
    AUTO_ENROLLMENT = "AutoEnrollment"
    MACHINE_TYPE = "MachineType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_enrollment": "AutoEnrollment",
        "machine_type": "MachineType",
    }

    auto_enrollment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GeneralFlagsV4(PropertyType):
    AUTO_ENROLLMENT = "AutoEnrollment"
    MACHINE_TYPE = "MachineType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_enrollment": "AutoEnrollment",
        "machine_type": "MachineType",
    }

    auto_enrollment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KeyUsage(PropertyType):
    CRITICAL = "Critical"
    USAGE_FLAGS = "UsageFlags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "critical": "Critical",
        "usage_flags": "UsageFlags",
    }

    critical: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    usage_flags: Optional[KeyUsageFlags] = None


@dataclass
class KeyUsageFlags(PropertyType):
    KEY_ENCIPHERMENT = "KeyEncipherment"
    DATA_ENCIPHERMENT = "DataEncipherment"
    DIGITAL_SIGNATURE = "DigitalSignature"
    KEY_AGREEMENT = "KeyAgreement"
    NON_REPUDIATION = "NonRepudiation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_encipherment": "KeyEncipherment",
        "data_encipherment": "DataEncipherment",
        "digital_signature": "DigitalSignature",
        "key_agreement": "KeyAgreement",
        "non_repudiation": "NonRepudiation",
    }

    key_encipherment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_encipherment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    digital_signature: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key_agreement: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    non_repudiation: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KeyUsageProperty(PropertyType):
    PROPERTY_FLAGS = "PropertyFlags"
    PROPERTY_TYPE = "PropertyType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "property_flags": "PropertyFlags",
        "property_type": "PropertyType",
    }

    property_flags: Optional[KeyUsagePropertyFlags] = None
    property_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyUsagePropertyFlags(PropertyType):
    DECRYPT = "Decrypt"
    SIGN = "Sign"
    KEY_AGREEMENT = "KeyAgreement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "decrypt": "Decrypt",
        "sign": "Sign",
        "key_agreement": "KeyAgreement",
    }

    decrypt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sign: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key_agreement: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateKeyAttributesV2(PropertyType):
    MINIMAL_KEY_LENGTH = "MinimalKeyLength"
    KEY_SPEC = "KeySpec"
    CRYPTO_PROVIDERS = "CryptoProviders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimal_key_length": "MinimalKeyLength",
        "key_spec": "KeySpec",
        "crypto_providers": "CryptoProviders",
    }

    minimal_key_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    key_spec: Optional[Union[str, Ref, GetAtt, Sub]] = None
    crypto_providers: Optional[Union[list[str], Ref]] = None


@dataclass
class PrivateKeyAttributesV3(PropertyType):
    MINIMAL_KEY_LENGTH = "MinimalKeyLength"
    KEY_SPEC = "KeySpec"
    KEY_USAGE_PROPERTY = "KeyUsageProperty"
    ALGORITHM = "Algorithm"
    CRYPTO_PROVIDERS = "CryptoProviders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimal_key_length": "MinimalKeyLength",
        "key_spec": "KeySpec",
        "key_usage_property": "KeyUsageProperty",
        "algorithm": "Algorithm",
        "crypto_providers": "CryptoProviders",
    }

    minimal_key_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    key_spec: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_usage_property: Optional[KeyUsageProperty] = None
    algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None
    crypto_providers: Optional[Union[list[str], Ref]] = None


@dataclass
class PrivateKeyAttributesV4(PropertyType):
    MINIMAL_KEY_LENGTH = "MinimalKeyLength"
    KEY_SPEC = "KeySpec"
    KEY_USAGE_PROPERTY = "KeyUsageProperty"
    ALGORITHM = "Algorithm"
    CRYPTO_PROVIDERS = "CryptoProviders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimal_key_length": "MinimalKeyLength",
        "key_spec": "KeySpec",
        "key_usage_property": "KeyUsageProperty",
        "algorithm": "Algorithm",
        "crypto_providers": "CryptoProviders",
    }

    minimal_key_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    key_spec: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_usage_property: Optional[KeyUsageProperty] = None
    algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None
    crypto_providers: Optional[Union[list[str], Ref]] = None


@dataclass
class PrivateKeyFlagsV2(PropertyType):
    EXPORTABLE_KEY = "ExportableKey"
    STRONG_KEY_PROTECTION_REQUIRED = "StrongKeyProtectionRequired"
    CLIENT_VERSION = "ClientVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exportable_key": "ExportableKey",
        "strong_key_protection_required": "StrongKeyProtectionRequired",
        "client_version": "ClientVersion",
    }

    exportable_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    strong_key_protection_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    client_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateKeyFlagsV3(PropertyType):
    REQUIRE_ALTERNATE_SIGNATURE_ALGORITHM = "RequireAlternateSignatureAlgorithm"
    EXPORTABLE_KEY = "ExportableKey"
    STRONG_KEY_PROTECTION_REQUIRED = "StrongKeyProtectionRequired"
    CLIENT_VERSION = "ClientVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "require_alternate_signature_algorithm": "RequireAlternateSignatureAlgorithm",
        "exportable_key": "ExportableKey",
        "strong_key_protection_required": "StrongKeyProtectionRequired",
        "client_version": "ClientVersion",
    }

    require_alternate_signature_algorithm: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exportable_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    strong_key_protection_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    client_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateKeyFlagsV4(PropertyType):
    REQUIRE_ALTERNATE_SIGNATURE_ALGORITHM = "RequireAlternateSignatureAlgorithm"
    EXPORTABLE_KEY = "ExportableKey"
    USE_LEGACY_PROVIDER = "UseLegacyProvider"
    STRONG_KEY_PROTECTION_REQUIRED = "StrongKeyProtectionRequired"
    REQUIRE_SAME_KEY_RENEWAL = "RequireSameKeyRenewal"
    CLIENT_VERSION = "ClientVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "require_alternate_signature_algorithm": "RequireAlternateSignatureAlgorithm",
        "exportable_key": "ExportableKey",
        "use_legacy_provider": "UseLegacyProvider",
        "strong_key_protection_required": "StrongKeyProtectionRequired",
        "require_same_key_renewal": "RequireSameKeyRenewal",
        "client_version": "ClientVersion",
    }

    require_alternate_signature_algorithm: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exportable_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_legacy_provider: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    strong_key_protection_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_same_key_renewal: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    client_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubjectNameFlagsV2(PropertyType):
    SAN_REQUIRE_EMAIL = "SanRequireEmail"
    SAN_REQUIRE_DNS = "SanRequireDns"
    REQUIRE_COMMON_NAME = "RequireCommonName"
    SAN_REQUIRE_UPN = "SanRequireUpn"
    SAN_REQUIRE_DOMAIN_DNS = "SanRequireDomainDns"
    SAN_REQUIRE_SPN = "SanRequireSpn"
    REQUIRE_EMAIL = "RequireEmail"
    REQUIRE_DIRECTORY_PATH = "RequireDirectoryPath"
    SAN_REQUIRE_DIRECTORY_GUID = "SanRequireDirectoryGuid"
    REQUIRE_DNS_AS_CN = "RequireDnsAsCn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "san_require_email": "SanRequireEmail",
        "san_require_dns": "SanRequireDns",
        "require_common_name": "RequireCommonName",
        "san_require_upn": "SanRequireUpn",
        "san_require_domain_dns": "SanRequireDomainDns",
        "san_require_spn": "SanRequireSpn",
        "require_email": "RequireEmail",
        "require_directory_path": "RequireDirectoryPath",
        "san_require_directory_guid": "SanRequireDirectoryGuid",
        "require_dns_as_cn": "RequireDnsAsCn",
    }

    san_require_email: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_dns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_common_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_upn: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_domain_dns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_spn: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_email: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_directory_path: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_directory_guid: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_dns_as_cn: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SubjectNameFlagsV3(PropertyType):
    SAN_REQUIRE_EMAIL = "SanRequireEmail"
    SAN_REQUIRE_DNS = "SanRequireDns"
    REQUIRE_COMMON_NAME = "RequireCommonName"
    SAN_REQUIRE_UPN = "SanRequireUpn"
    SAN_REQUIRE_DOMAIN_DNS = "SanRequireDomainDns"
    SAN_REQUIRE_SPN = "SanRequireSpn"
    REQUIRE_EMAIL = "RequireEmail"
    REQUIRE_DIRECTORY_PATH = "RequireDirectoryPath"
    SAN_REQUIRE_DIRECTORY_GUID = "SanRequireDirectoryGuid"
    REQUIRE_DNS_AS_CN = "RequireDnsAsCn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "san_require_email": "SanRequireEmail",
        "san_require_dns": "SanRequireDns",
        "require_common_name": "RequireCommonName",
        "san_require_upn": "SanRequireUpn",
        "san_require_domain_dns": "SanRequireDomainDns",
        "san_require_spn": "SanRequireSpn",
        "require_email": "RequireEmail",
        "require_directory_path": "RequireDirectoryPath",
        "san_require_directory_guid": "SanRequireDirectoryGuid",
        "require_dns_as_cn": "RequireDnsAsCn",
    }

    san_require_email: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_dns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_common_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_upn: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_domain_dns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_spn: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_email: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_directory_path: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_directory_guid: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_dns_as_cn: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SubjectNameFlagsV4(PropertyType):
    SAN_REQUIRE_EMAIL = "SanRequireEmail"
    SAN_REQUIRE_DNS = "SanRequireDns"
    REQUIRE_COMMON_NAME = "RequireCommonName"
    SAN_REQUIRE_UPN = "SanRequireUpn"
    SAN_REQUIRE_DOMAIN_DNS = "SanRequireDomainDns"
    SAN_REQUIRE_SPN = "SanRequireSpn"
    REQUIRE_EMAIL = "RequireEmail"
    REQUIRE_DIRECTORY_PATH = "RequireDirectoryPath"
    SAN_REQUIRE_DIRECTORY_GUID = "SanRequireDirectoryGuid"
    REQUIRE_DNS_AS_CN = "RequireDnsAsCn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "san_require_email": "SanRequireEmail",
        "san_require_dns": "SanRequireDns",
        "require_common_name": "RequireCommonName",
        "san_require_upn": "SanRequireUpn",
        "san_require_domain_dns": "SanRequireDomainDns",
        "san_require_spn": "SanRequireSpn",
        "require_email": "RequireEmail",
        "require_directory_path": "RequireDirectoryPath",
        "san_require_directory_guid": "SanRequireDirectoryGuid",
        "require_dns_as_cn": "RequireDnsAsCn",
    }

    san_require_email: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_dns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_common_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_upn: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_domain_dns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_spn: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_email: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_directory_path: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    san_require_directory_guid: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_dns_as_cn: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateDefinition(PropertyType):
    TEMPLATE_V4 = "TemplateV4"
    TEMPLATE_V3 = "TemplateV3"
    TEMPLATE_V2 = "TemplateV2"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template_v4": "TemplateV4",
        "template_v3": "TemplateV3",
        "template_v2": "TemplateV2",
    }

    template_v4: Optional[TemplateV4] = None
    template_v3: Optional[TemplateV3] = None
    template_v2: Optional[TemplateV2] = None


@dataclass
class TemplateV2(PropertyType):
    SUBJECT_NAME_FLAGS = "SubjectNameFlags"
    SUPERSEDED_TEMPLATES = "SupersededTemplates"
    PRIVATE_KEY_FLAGS = "PrivateKeyFlags"
    PRIVATE_KEY_ATTRIBUTES = "PrivateKeyAttributes"
    GENERAL_FLAGS = "GeneralFlags"
    CERTIFICATE_VALIDITY = "CertificateValidity"
    EXTENSIONS = "Extensions"
    ENROLLMENT_FLAGS = "EnrollmentFlags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_name_flags": "SubjectNameFlags",
        "superseded_templates": "SupersededTemplates",
        "private_key_flags": "PrivateKeyFlags",
        "private_key_attributes": "PrivateKeyAttributes",
        "general_flags": "GeneralFlags",
        "certificate_validity": "CertificateValidity",
        "extensions": "Extensions",
        "enrollment_flags": "EnrollmentFlags",
    }

    subject_name_flags: Optional[SubjectNameFlagsV2] = None
    superseded_templates: Optional[Union[list[str], Ref]] = None
    private_key_flags: Optional[PrivateKeyFlagsV2] = None
    private_key_attributes: Optional[PrivateKeyAttributesV2] = None
    general_flags: Optional[GeneralFlagsV2] = None
    certificate_validity: Optional[CertificateValidity] = None
    extensions: Optional[ExtensionsV2] = None
    enrollment_flags: Optional[EnrollmentFlagsV2] = None


@dataclass
class TemplateV3(PropertyType):
    SUBJECT_NAME_FLAGS = "SubjectNameFlags"
    SUPERSEDED_TEMPLATES = "SupersededTemplates"
    PRIVATE_KEY_FLAGS = "PrivateKeyFlags"
    PRIVATE_KEY_ATTRIBUTES = "PrivateKeyAttributes"
    GENERAL_FLAGS = "GeneralFlags"
    CERTIFICATE_VALIDITY = "CertificateValidity"
    EXTENSIONS = "Extensions"
    ENROLLMENT_FLAGS = "EnrollmentFlags"
    HASH_ALGORITHM = "HashAlgorithm"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_name_flags": "SubjectNameFlags",
        "superseded_templates": "SupersededTemplates",
        "private_key_flags": "PrivateKeyFlags",
        "private_key_attributes": "PrivateKeyAttributes",
        "general_flags": "GeneralFlags",
        "certificate_validity": "CertificateValidity",
        "extensions": "Extensions",
        "enrollment_flags": "EnrollmentFlags",
        "hash_algorithm": "HashAlgorithm",
    }

    subject_name_flags: Optional[SubjectNameFlagsV3] = None
    superseded_templates: Optional[Union[list[str], Ref]] = None
    private_key_flags: Optional[PrivateKeyFlagsV3] = None
    private_key_attributes: Optional[PrivateKeyAttributesV3] = None
    general_flags: Optional[GeneralFlagsV3] = None
    certificate_validity: Optional[CertificateValidity] = None
    extensions: Optional[ExtensionsV3] = None
    enrollment_flags: Optional[EnrollmentFlagsV3] = None
    hash_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateV4(PropertyType):
    SUBJECT_NAME_FLAGS = "SubjectNameFlags"
    SUPERSEDED_TEMPLATES = "SupersededTemplates"
    PRIVATE_KEY_FLAGS = "PrivateKeyFlags"
    PRIVATE_KEY_ATTRIBUTES = "PrivateKeyAttributes"
    GENERAL_FLAGS = "GeneralFlags"
    CERTIFICATE_VALIDITY = "CertificateValidity"
    EXTENSIONS = "Extensions"
    ENROLLMENT_FLAGS = "EnrollmentFlags"
    HASH_ALGORITHM = "HashAlgorithm"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_name_flags": "SubjectNameFlags",
        "superseded_templates": "SupersededTemplates",
        "private_key_flags": "PrivateKeyFlags",
        "private_key_attributes": "PrivateKeyAttributes",
        "general_flags": "GeneralFlags",
        "certificate_validity": "CertificateValidity",
        "extensions": "Extensions",
        "enrollment_flags": "EnrollmentFlags",
        "hash_algorithm": "HashAlgorithm",
    }

    subject_name_flags: Optional[SubjectNameFlagsV4] = None
    superseded_templates: Optional[Union[list[str], Ref]] = None
    private_key_flags: Optional[PrivateKeyFlagsV4] = None
    private_key_attributes: Optional[PrivateKeyAttributesV4] = None
    general_flags: Optional[GeneralFlagsV4] = None
    certificate_validity: Optional[CertificateValidity] = None
    extensions: Optional[ExtensionsV4] = None
    enrollment_flags: Optional[EnrollmentFlagsV4] = None
    hash_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValidityPeriod(PropertyType):
    PERIOD_TYPE = "PeriodType"
    PERIOD = "Period"

    _property_mappings: ClassVar[dict[str, str]] = {
        "period_type": "PeriodType",
        "period": "Period",
    }

    period_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[float, Ref, GetAtt, Sub]] = None

