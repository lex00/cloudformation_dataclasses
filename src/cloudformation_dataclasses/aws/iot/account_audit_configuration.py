"""PropertyTypes for AWS::IoT::AccountAuditConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuditCheckConfiguration(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AuditCheckConfigurations(PropertyType):
    IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK = "IotRoleAliasOverlyPermissiveCheck"
    DEVICE_CERTIFICATE_SHARED_CHECK = "DeviceCertificateSharedCheck"
    CONFLICTING_CLIENT_IDS_CHECK = "ConflictingClientIdsCheck"
    INTERMEDIATE_CA_REVOKED_FOR_ACTIVE_DEVICE_CERTIFICATES_CHECK = "IntermediateCaRevokedForActiveDeviceCertificatesCheck"
    IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK = "IotRoleAliasAllowsAccessToUnusedServicesCheck"
    REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK = "RevokedCaCertificateStillActiveCheck"
    LOGGING_DISABLED_CHECK = "LoggingDisabledCheck"
    UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK = "UnauthenticatedCognitoRoleOverlyPermissiveCheck"
    AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK = "AuthenticatedCognitoRoleOverlyPermissiveCheck"
    CA_CERTIFICATE_EXPIRING_CHECK = "CaCertificateExpiringCheck"
    DEVICE_CERTIFICATE_EXPIRING_CHECK = "DeviceCertificateExpiringCheck"
    IO_T_POLICY_POTENTIAL_MIS_CONFIGURATION_CHECK = "IoTPolicyPotentialMisConfigurationCheck"
    DEVICE_CERTIFICATE_AGE_CHECK = "DeviceCertificateAgeCheck"
    IOT_POLICY_OVERLY_PERMISSIVE_CHECK = "IotPolicyOverlyPermissiveCheck"
    REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK = "RevokedDeviceCertificateStillActiveCheck"
    DEVICE_CERTIFICATE_KEY_QUALITY_CHECK = "DeviceCertificateKeyQualityCheck"
    CA_CERTIFICATE_KEY_QUALITY_CHECK = "CaCertificateKeyQualityCheck"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iot_role_alias_overly_permissive_check": "IotRoleAliasOverlyPermissiveCheck",
        "device_certificate_shared_check": "DeviceCertificateSharedCheck",
        "conflicting_client_ids_check": "ConflictingClientIdsCheck",
        "intermediate_ca_revoked_for_active_device_certificates_check": "IntermediateCaRevokedForActiveDeviceCertificatesCheck",
        "iot_role_alias_allows_access_to_unused_services_check": "IotRoleAliasAllowsAccessToUnusedServicesCheck",
        "revoked_ca_certificate_still_active_check": "RevokedCaCertificateStillActiveCheck",
        "logging_disabled_check": "LoggingDisabledCheck",
        "unauthenticated_cognito_role_overly_permissive_check": "UnauthenticatedCognitoRoleOverlyPermissiveCheck",
        "authenticated_cognito_role_overly_permissive_check": "AuthenticatedCognitoRoleOverlyPermissiveCheck",
        "ca_certificate_expiring_check": "CaCertificateExpiringCheck",
        "device_certificate_expiring_check": "DeviceCertificateExpiringCheck",
        "io_t_policy_potential_mis_configuration_check": "IoTPolicyPotentialMisConfigurationCheck",
        "device_certificate_age_check": "DeviceCertificateAgeCheck",
        "iot_policy_overly_permissive_check": "IotPolicyOverlyPermissiveCheck",
        "revoked_device_certificate_still_active_check": "RevokedDeviceCertificateStillActiveCheck",
        "device_certificate_key_quality_check": "DeviceCertificateKeyQualityCheck",
        "ca_certificate_key_quality_check": "CaCertificateKeyQualityCheck",
    }

    iot_role_alias_overly_permissive_check: Optional[AuditCheckConfiguration] = None
    device_certificate_shared_check: Optional[AuditCheckConfiguration] = None
    conflicting_client_ids_check: Optional[AuditCheckConfiguration] = None
    intermediate_ca_revoked_for_active_device_certificates_check: Optional[AuditCheckConfiguration] = None
    iot_role_alias_allows_access_to_unused_services_check: Optional[AuditCheckConfiguration] = None
    revoked_ca_certificate_still_active_check: Optional[AuditCheckConfiguration] = None
    logging_disabled_check: Optional[AuditCheckConfiguration] = None
    unauthenticated_cognito_role_overly_permissive_check: Optional[AuditCheckConfiguration] = None
    authenticated_cognito_role_overly_permissive_check: Optional[AuditCheckConfiguration] = None
    ca_certificate_expiring_check: Optional[AuditCheckConfiguration] = None
    device_certificate_expiring_check: Optional[DeviceCertExpirationAuditCheckConfiguration] = None
    io_t_policy_potential_mis_configuration_check: Optional[AuditCheckConfiguration] = None
    device_certificate_age_check: Optional[DeviceCertAgeAuditCheckConfiguration] = None
    iot_policy_overly_permissive_check: Optional[AuditCheckConfiguration] = None
    revoked_device_certificate_still_active_check: Optional[AuditCheckConfiguration] = None
    device_certificate_key_quality_check: Optional[AuditCheckConfiguration] = None
    ca_certificate_key_quality_check: Optional[AuditCheckConfiguration] = None


@dataclass
class AuditNotificationTarget(PropertyType):
    TARGET_ARN = "TargetArn"
    ENABLED = "Enabled"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_arn": "TargetArn",
        "enabled": "Enabled",
        "role_arn": "RoleArn",
    }

    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuditNotificationTargetConfigurations(PropertyType):
    SNS = "Sns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns": "Sns",
    }

    sns: Optional[AuditNotificationTarget] = None


@dataclass
class CertAgeCheckCustomConfiguration(PropertyType):
    CERT_AGE_THRESHOLD_IN_DAYS = "CertAgeThresholdInDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cert_age_threshold_in_days": "CertAgeThresholdInDays",
    }

    cert_age_threshold_in_days: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CertExpirationCheckCustomConfiguration(PropertyType):
    CERT_EXPIRATION_THRESHOLD_IN_DAYS = "CertExpirationThresholdInDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cert_expiration_threshold_in_days": "CertExpirationThresholdInDays",
    }

    cert_expiration_threshold_in_days: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeviceCertAgeAuditCheckConfiguration(PropertyType):
    CONFIGURATION = "Configuration"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration": "Configuration",
        "enabled": "Enabled",
    }

    configuration: Optional[CertAgeCheckCustomConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeviceCertExpirationAuditCheckConfiguration(PropertyType):
    CONFIGURATION = "Configuration"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration": "Configuration",
        "enabled": "Enabled",
    }

    configuration: Optional[CertExpirationCheckCustomConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

