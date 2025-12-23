"""PropertyTypes for AWS::ElasticLoadBalancingV2::Listener."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    ORDER = "Order"
    TARGET_GROUP_ARN = "TargetGroupArn"
    FIXED_RESPONSE_CONFIG = "FixedResponseConfig"
    AUTHENTICATE_COGNITO_CONFIG = "AuthenticateCognitoConfig"
    TYPE = "Type"
    REDIRECT_CONFIG = "RedirectConfig"
    JWT_VALIDATION_CONFIG = "JwtValidationConfig"
    FORWARD_CONFIG = "ForwardConfig"
    AUTHENTICATE_OIDC_CONFIG = "AuthenticateOidcConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "order": "Order",
        "target_group_arn": "TargetGroupArn",
        "fixed_response_config": "FixedResponseConfig",
        "authenticate_cognito_config": "AuthenticateCognitoConfig",
        "type_": "Type",
        "redirect_config": "RedirectConfig",
        "jwt_validation_config": "JwtValidationConfig",
        "forward_config": "ForwardConfig",
        "authenticate_oidc_config": "AuthenticateOidcConfig",
    }

    order: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fixed_response_config: Optional[FixedResponseConfig] = None
    authenticate_cognito_config: Optional[AuthenticateCognitoConfig] = None
    type_: Optional[Union[str, ActionTypeEnum, Ref, GetAtt, Sub]] = None
    redirect_config: Optional[RedirectConfig] = None
    jwt_validation_config: Optional[JwtValidationConfig] = None
    forward_config: Optional[ForwardConfig] = None
    authenticate_oidc_config: Optional[AuthenticateOidcConfig] = None


@dataclass
class AuthenticateCognitoConfig(PropertyType):
    ON_UNAUTHENTICATED_REQUEST = "OnUnauthenticatedRequest"
    USER_POOL_CLIENT_ID = "UserPoolClientId"
    USER_POOL_DOMAIN = "UserPoolDomain"
    SESSION_TIMEOUT = "SessionTimeout"
    SCOPE = "Scope"
    SESSION_COOKIE_NAME = "SessionCookieName"
    USER_POOL_ARN = "UserPoolArn"
    AUTHENTICATION_REQUEST_EXTRA_PARAMS = "AuthenticationRequestExtraParams"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_unauthenticated_request": "OnUnauthenticatedRequest",
        "user_pool_client_id": "UserPoolClientId",
        "user_pool_domain": "UserPoolDomain",
        "session_timeout": "SessionTimeout",
        "scope": "Scope",
        "session_cookie_name": "SessionCookieName",
        "user_pool_arn": "UserPoolArn",
        "authentication_request_extra_params": "AuthenticationRequestExtraParams",
    }

    on_unauthenticated_request: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    session_timeout: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    session_cookie_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authentication_request_extra_params: Optional[dict[str, str]] = None


@dataclass
class AuthenticateOidcConfig(PropertyType):
    ON_UNAUTHENTICATED_REQUEST = "OnUnauthenticatedRequest"
    TOKEN_ENDPOINT = "TokenEndpoint"
    USE_EXISTING_CLIENT_SECRET = "UseExistingClientSecret"
    SESSION_TIMEOUT = "SessionTimeout"
    SCOPE = "Scope"
    ISSUER = "Issuer"
    CLIENT_SECRET = "ClientSecret"
    USER_INFO_ENDPOINT = "UserInfoEndpoint"
    CLIENT_ID = "ClientId"
    AUTHORIZATION_ENDPOINT = "AuthorizationEndpoint"
    SESSION_COOKIE_NAME = "SessionCookieName"
    AUTHENTICATION_REQUEST_EXTRA_PARAMS = "AuthenticationRequestExtraParams"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_unauthenticated_request": "OnUnauthenticatedRequest",
        "token_endpoint": "TokenEndpoint",
        "use_existing_client_secret": "UseExistingClientSecret",
        "session_timeout": "SessionTimeout",
        "scope": "Scope",
        "issuer": "Issuer",
        "client_secret": "ClientSecret",
        "user_info_endpoint": "UserInfoEndpoint",
        "client_id": "ClientId",
        "authorization_endpoint": "AuthorizationEndpoint",
        "session_cookie_name": "SessionCookieName",
        "authentication_request_extra_params": "AuthenticationRequestExtraParams",
    }

    on_unauthenticated_request: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_existing_client_secret: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    session_timeout: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_info_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    session_cookie_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authentication_request_extra_params: Optional[dict[str, str]] = None


@dataclass
class Certificate(PropertyType):
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_arn": "CertificateArn",
    }

    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FixedResponseConfig(PropertyType):
    CONTENT_TYPE = "ContentType"
    STATUS_CODE = "StatusCode"
    MESSAGE_BODY = "MessageBody"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_type": "ContentType",
        "status_code": "StatusCode",
        "message_body": "MessageBody",
    }

    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_body: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ForwardConfig(PropertyType):
    TARGET_GROUP_STICKINESS_CONFIG = "TargetGroupStickinessConfig"
    TARGET_GROUPS = "TargetGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_stickiness_config": "TargetGroupStickinessConfig",
        "target_groups": "TargetGroups",
    }

    target_group_stickiness_config: Optional[TargetGroupStickinessConfig] = None
    target_groups: Optional[list[TargetGroupTuple]] = None


@dataclass
class JwtValidationActionAdditionalClaim(PropertyType):
    FORMAT = "Format"
    VALUES = "Values"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "values": "Values",
        "name": "Name",
    }

    format: Optional[Union[str, JwtValidationActionAdditionalClaimFormatEnum, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JwtValidationConfig(PropertyType):
    JWKS_ENDPOINT = "JwksEndpoint"
    ISSUER = "Issuer"
    ADDITIONAL_CLAIMS = "AdditionalClaims"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jwks_endpoint": "JwksEndpoint",
        "issuer": "Issuer",
        "additional_claims": "AdditionalClaims",
    }

    jwks_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_claims: Optional[list[JwtValidationActionAdditionalClaim]] = None


@dataclass
class ListenerAttribute(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MutualAuthentication(PropertyType):
    IGNORE_CLIENT_CERTIFICATE_EXPIRY = "IgnoreClientCertificateExpiry"
    MODE = "Mode"
    TRUST_STORE_ARN = "TrustStoreArn"
    ADVERTISE_TRUST_STORE_CA_NAMES = "AdvertiseTrustStoreCaNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ignore_client_certificate_expiry": "IgnoreClientCertificateExpiry",
        "mode": "Mode",
        "trust_store_arn": "TrustStoreArn",
        "advertise_trust_store_ca_names": "AdvertiseTrustStoreCaNames",
    }

    ignore_client_certificate_expiry: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trust_store_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    advertise_trust_store_ca_names: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedirectConfig(PropertyType):
    PATH = "Path"
    QUERY = "Query"
    PORT = "Port"
    HOST = "Host"
    PROTOCOL = "Protocol"
    STATUS_CODE = "StatusCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "query": "Query",
        "port": "Port",
        "host": "Host",
        "protocol": "Protocol",
        "status_code": "StatusCode",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupStickinessConfig(PropertyType):
    ENABLED = "Enabled"
    DURATION_SECONDS = "DurationSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "duration_seconds": "DurationSeconds",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    duration_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupTuple(PropertyType):
    TARGET_GROUP_ARN = "TargetGroupArn"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_arn": "TargetGroupArn",
        "weight": "Weight",
    }

    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

