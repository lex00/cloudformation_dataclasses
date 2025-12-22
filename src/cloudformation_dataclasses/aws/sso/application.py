"""PropertyTypes for AWS::SSO::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessDeniedExceptionReason:
    """AccessDeniedExceptionReason enum values."""

    KMS_ACCESSDENIEDEXCEPTION = "KMS_AccessDeniedException"


class ApplicationStatus:
    """ApplicationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ApplicationVisibility:
    """ApplicationVisibility enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AuthenticationMethodType:
    """AuthenticationMethodType enum values."""

    IAM = "IAM"


class FederationProtocol:
    """FederationProtocol enum values."""

    SAML = "SAML"
    OAUTH = "OAUTH"


class GrantType:
    """GrantType enum values."""

    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"


class InstanceAccessControlAttributeConfigurationStatus:
    """InstanceAccessControlAttributeConfigurationStatus enum values."""

    ENABLED = "ENABLED"
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_FAILED = "CREATION_FAILED"


class InstanceStatus:
    """InstanceStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    ACTIVE = "ACTIVE"


class JwksRetrievalOption:
    """JwksRetrievalOption enum values."""

    OPEN_ID_DISCOVERY = "OPEN_ID_DISCOVERY"


class KmsKeyStatus:
    """KmsKeyStatus enum values."""

    UPDATING = "UPDATING"
    ENABLED = "ENABLED"
    UPDATE_FAILED = "UPDATE_FAILED"


class KmsKeyType:
    """KmsKeyType enum values."""

    AWS_OWNED_KMS_KEY = "AWS_OWNED_KMS_KEY"
    CUSTOMER_MANAGED_KEY = "CUSTOMER_MANAGED_KEY"


class PrincipalType:
    """PrincipalType enum values."""

    USER = "USER"
    GROUP = "GROUP"


class ProvisionTargetType:
    """ProvisionTargetType enum values."""

    AWS_ACCOUNT = "AWS_ACCOUNT"
    ALL_PROVISIONED_ACCOUNTS = "ALL_PROVISIONED_ACCOUNTS"


class ProvisioningStatus:
    """ProvisioningStatus enum values."""

    LATEST_PERMISSION_SET_PROVISIONED = "LATEST_PERMISSION_SET_PROVISIONED"
    LATEST_PERMISSION_SET_NOT_PROVISIONED = "LATEST_PERMISSION_SET_NOT_PROVISIONED"


class ResourceNotFoundExceptionReason:
    """ResourceNotFoundExceptionReason enum values."""

    KMS_NOTFOUNDEXCEPTION = "KMS_NotFoundException"


class SignInOrigin:
    """SignInOrigin enum values."""

    IDENTITY_CENTER = "IDENTITY_CENTER"
    APPLICATION = "APPLICATION"


class StatusValues:
    """StatusValues enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class TargetType:
    """TargetType enum values."""

    AWS_ACCOUNT = "AWS_ACCOUNT"


class ThrottlingExceptionReason:
    """ThrottlingExceptionReason enum values."""

    KMS_THROTTLINGEXCEPTION = "KMS_ThrottlingException"


class TrustedTokenIssuerType:
    """TrustedTokenIssuerType enum values."""

    OIDC_JWT = "OIDC_JWT"


class UserBackgroundSessionApplicationStatus:
    """UserBackgroundSessionApplicationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    KMS_INVALIDKEYUSAGEEXCEPTION = "KMS_InvalidKeyUsageException"
    KMS_INVALIDSTATEEXCEPTION = "KMS_InvalidStateException"
    KMS_DISABLEDEXCEPTION = "KMS_DisabledException"


@dataclass
class PortalOptionsConfiguration(PropertyType):
    SIGN_IN_OPTIONS = "SignInOptions"
    VISIBILITY = "Visibility"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sign_in_options": "SignInOptions",
        "visibility": "Visibility",
    }

    sign_in_options: Optional[SignInOptions] = None
    visibility: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SignInOptions(PropertyType):
    ORIGIN = "Origin"
    APPLICATION_URL = "ApplicationUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "origin": "Origin",
        "application_url": "ApplicationUrl",
    }

    origin: Optional[Union[str, SignInOrigin, Ref, GetAtt, Sub]] = None
    application_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

