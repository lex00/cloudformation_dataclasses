"""PropertyTypes for AWS::PCAConnectorAD::Template."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationPolicies(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policies": "Policies",
        "critical": "Critical",
    }

    policies: Optional[list[ApplicationPolicy]] = None
    critical: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_type": "PolicyType",
        "policy_object_identifier": "PolicyObjectIdentifier",
    }

    policy_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_object_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CertificateValidity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validity_period": "ValidityPeriod",
        "renewal_period": "RenewalPeriod",
    }

    validity_period: Optional[ValidityPeriod] = None
    renewal_period: Optional[ValidityPeriod] = None


@dataclass
class EnrollmentFlagsV2(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_policies": "ApplicationPolicies",
        "key_usage": "KeyUsage",
    }

    application_policies: Optional[ApplicationPolicies] = None
    key_usage: Optional[KeyUsage] = None


@dataclass
class ExtensionsV3(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_policies": "ApplicationPolicies",
        "key_usage": "KeyUsage",
    }

    application_policies: Optional[ApplicationPolicies] = None
    key_usage: Optional[KeyUsage] = None


@dataclass
class ExtensionsV4(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_policies": "ApplicationPolicies",
        "key_usage": "KeyUsage",
    }

    application_policies: Optional[ApplicationPolicies] = None
    key_usage: Optional[KeyUsage] = None


@dataclass
class GeneralFlagsV2(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_enrollment": "AutoEnrollment",
        "machine_type": "MachineType",
    }

    auto_enrollment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GeneralFlagsV3(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_enrollment": "AutoEnrollment",
        "machine_type": "MachineType",
    }

    auto_enrollment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GeneralFlagsV4(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_enrollment": "AutoEnrollment",
        "machine_type": "MachineType",
    }

    auto_enrollment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    machine_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KeyUsage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "critical": "Critical",
        "usage_flags": "UsageFlags",
    }

    critical: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    usage_flags: Optional[KeyUsageFlags] = None


@dataclass
class KeyUsageFlags(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "property_flags": "PropertyFlags",
        "property_type": "PropertyType",
    }

    property_flags: Optional[KeyUsagePropertyFlags] = None
    property_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyUsagePropertyFlags(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "period_type": "PeriodType",
        "period": "Period",
    }

    period_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    period: Optional[Union[float, Ref, GetAtt, Sub]] = None

