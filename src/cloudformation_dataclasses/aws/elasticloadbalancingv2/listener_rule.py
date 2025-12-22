"""PropertyTypes for AWS::ElasticLoadBalancingV2::ListenerRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionTypeEnum:
    """ActionTypeEnum enum values."""

    FORWARD = "forward"
    AUTHENTICATE_OIDC = "authenticate-oidc"
    AUTHENTICATE_COGNITO = "authenticate-cognito"
    REDIRECT = "redirect"
    FIXED_RESPONSE = "fixed-response"
    JWT_VALIDATION = "jwt-validation"


class AdvertiseTrustStoreCaNamesEnum:
    """AdvertiseTrustStoreCaNamesEnum enum values."""

    ON = "on"
    OFF = "off"


class AnomalyResultEnum:
    """AnomalyResultEnum enum values."""

    ANOMALOUS = "anomalous"
    NORMAL = "normal"


class AuthenticateCognitoActionConditionalBehaviorEnum:
    """AuthenticateCognitoActionConditionalBehaviorEnum enum values."""

    DENY = "deny"
    ALLOW = "allow"
    AUTHENTICATE = "authenticate"


class AuthenticateOidcActionConditionalBehaviorEnum:
    """AuthenticateOidcActionConditionalBehaviorEnum enum values."""

    DENY = "deny"
    ALLOW = "allow"
    AUTHENTICATE = "authenticate"


class CapacityReservationStateEnum:
    """CapacityReservationStateEnum enum values."""

    PROVISIONED = "provisioned"
    PENDING = "pending"
    REBALANCING = "rebalancing"
    FAILED = "failed"


class DescribeTargetHealthInputIncludeEnum:
    """DescribeTargetHealthInputIncludeEnum enum values."""

    ANOMALYDETECTION = "AnomalyDetection"
    ALL = "All"


class EnablePrefixForIpv6SourceNatEnum:
    """EnablePrefixForIpv6SourceNatEnum enum values."""

    ON = "on"
    OFF = "off"


class EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum:
    """EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnum enum values."""

    ON = "on"
    OFF = "off"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"
    DUALSTACK_WITHOUT_PUBLIC_IPV4 = "dualstack-without-public-ipv4"


class JwtValidationActionAdditionalClaimFormatEnum:
    """JwtValidationActionAdditionalClaimFormatEnum enum values."""

    SINGLE_STRING = "single-string"
    STRING_ARRAY = "string-array"
    SPACE_SEPARATED_VALUES = "space-separated-values"


class LoadBalancerSchemeEnum:
    """LoadBalancerSchemeEnum enum values."""

    INTERNET_FACING = "internet-facing"
    INTERNAL = "internal"


class LoadBalancerStateEnum:
    """LoadBalancerStateEnum enum values."""

    ACTIVE = "active"
    PROVISIONING = "provisioning"
    ACTIVE_IMPAIRED = "active_impaired"
    FAILED = "failed"


class LoadBalancerTypeEnum:
    """LoadBalancerTypeEnum enum values."""

    APPLICATION = "application"
    NETWORK = "network"
    GATEWAY = "gateway"


class MitigationInEffectEnum:
    """MitigationInEffectEnum enum values."""

    YES = "yes"
    NO = "no"


class ProtocolEnum:
    """ProtocolEnum enum values."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"
    TLS = "TLS"
    UDP = "UDP"
    TCP_UDP = "TCP_UDP"
    GENEVE = "GENEVE"
    QUIC = "QUIC"
    TCP_QUIC = "TCP_QUIC"


class RedirectActionStatusCodeEnum:
    """RedirectActionStatusCodeEnum enum values."""

    HTTP_301 = "HTTP_301"
    HTTP_302 = "HTTP_302"


class RemoveIpamPoolEnum:
    """RemoveIpamPoolEnum enum values."""

    IPV4 = "ipv4"


class RevocationType:
    """RevocationType enum values."""

    CRL = "CRL"


class TargetAdministrativeOverrideReasonEnum:
    """TargetAdministrativeOverrideReasonEnum enum values."""

    ADMINISTRATIVEOVERRIDE_UNKNOWN = "AdministrativeOverride.Unknown"
    ADMINISTRATIVEOVERRIDE_NOOVERRIDE = "AdministrativeOverride.NoOverride"
    ADMINISTRATIVEOVERRIDE_ZONALSHIFTACTIVE = "AdministrativeOverride.ZonalShiftActive"
    ADMINISTRATIVEOVERRIDE_ZONALSHIFTDELEGATEDTODNS = "AdministrativeOverride.ZonalShiftDelegatedToDns"


class TargetAdministrativeOverrideStateEnum:
    """TargetAdministrativeOverrideStateEnum enum values."""

    UNKNOWN = "unknown"
    NO_OVERRIDE = "no_override"
    ZONAL_SHIFT_ACTIVE = "zonal_shift_active"
    ZONAL_SHIFT_DELEGATED_TO_DNS = "zonal_shift_delegated_to_dns"


class TargetGroupIpAddressTypeEnum:
    """TargetGroupIpAddressTypeEnum enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class TargetHealthReasonEnum:
    """TargetHealthReasonEnum enum values."""

    ELB_REGISTRATIONINPROGRESS = "Elb.RegistrationInProgress"
    ELB_INITIALHEALTHCHECKING = "Elb.InitialHealthChecking"
    TARGET_RESPONSECODEMISMATCH = "Target.ResponseCodeMismatch"
    TARGET_TIMEOUT = "Target.Timeout"
    TARGET_FAILEDHEALTHCHECKS = "Target.FailedHealthChecks"
    TARGET_NOTREGISTERED = "Target.NotRegistered"
    TARGET_NOTINUSE = "Target.NotInUse"
    TARGET_DEREGISTRATIONINPROGRESS = "Target.DeregistrationInProgress"
    TARGET_INVALIDSTATE = "Target.InvalidState"
    TARGET_IPUNUSABLE = "Target.IpUnusable"
    TARGET_HEALTHCHECKDISABLED = "Target.HealthCheckDisabled"
    ELB_INTERNALERROR = "Elb.InternalError"


class TargetHealthStateEnum:
    """TargetHealthStateEnum enum values."""

    INITIAL = "initial"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNHEALTHY_DRAINING = "unhealthy.draining"
    UNUSED = "unused"
    DRAINING = "draining"
    UNAVAILABLE = "unavailable"


class TargetTypeEnum:
    """TargetTypeEnum enum values."""

    INSTANCE = "instance"
    IP = "ip"
    LAMBDA = "lambda"
    ALB = "alb"


class TransformTypeEnum:
    """TransformTypeEnum enum values."""

    HOST_HEADER_REWRITE = "host-header-rewrite"
    URL_REWRITE = "url-rewrite"


class TrustStoreAssociationStatusEnum:
    """TrustStoreAssociationStatusEnum enum values."""

    ACTIVE = "active"
    REMOVED = "removed"


class TrustStoreStatus:
    """TrustStoreStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"


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
    session_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
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
    session_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_info_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    session_cookie_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authentication_request_extra_params: Optional[dict[str, str]] = None


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
class HostHeaderConfig(PropertyType):
    VALUES = "Values"
    REGEX_VALUES = "RegexValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "regex_values": "RegexValues",
    }

    values: Optional[Union[list[str], Ref]] = None
    regex_values: Optional[Union[list[str], Ref]] = None


@dataclass
class HttpHeaderConfig(PropertyType):
    VALUES = "Values"
    REGEX_VALUES = "RegexValues"
    HTTP_HEADER_NAME = "HttpHeaderName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "regex_values": "RegexValues",
        "http_header_name": "HttpHeaderName",
    }

    values: Optional[Union[list[str], Ref]] = None
    regex_values: Optional[Union[list[str], Ref]] = None
    http_header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpRequestMethodConfig(PropertyType):
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[Union[list[str], Ref]] = None


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
class PathPatternConfig(PropertyType):
    VALUES = "Values"
    REGEX_VALUES = "RegexValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "regex_values": "RegexValues",
    }

    values: Optional[Union[list[str], Ref]] = None
    regex_values: Optional[Union[list[str], Ref]] = None


@dataclass
class QueryStringConfig(PropertyType):
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[list[QueryStringKeyValue]] = None


@dataclass
class QueryStringKeyValue(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class RewriteConfig(PropertyType):
    REPLACE = "Replace"
    REGEX = "Regex"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replace": "Replace",
        "regex": "Regex",
    }

    replace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RewriteConfigObject(PropertyType):
    REWRITES = "Rewrites"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rewrites": "Rewrites",
    }

    rewrites: Optional[list[RewriteConfig]] = None


@dataclass
class RuleCondition(PropertyType):
    FIELD = "Field"
    HTTP_HEADER_CONFIG = "HttpHeaderConfig"
    VALUES = "Values"
    QUERY_STRING_CONFIG = "QueryStringConfig"
    REGEX_VALUES = "RegexValues"
    HOST_HEADER_CONFIG = "HostHeaderConfig"
    HTTP_REQUEST_METHOD_CONFIG = "HttpRequestMethodConfig"
    PATH_PATTERN_CONFIG = "PathPatternConfig"
    SOURCE_IP_CONFIG = "SourceIpConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "http_header_config": "HttpHeaderConfig",
        "values": "Values",
        "query_string_config": "QueryStringConfig",
        "regex_values": "RegexValues",
        "host_header_config": "HostHeaderConfig",
        "http_request_method_config": "HttpRequestMethodConfig",
        "path_pattern_config": "PathPatternConfig",
        "source_ip_config": "SourceIpConfig",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_header_config: Optional[HttpHeaderConfig] = None
    values: Optional[Union[list[str], Ref]] = None
    query_string_config: Optional[QueryStringConfig] = None
    regex_values: Optional[Union[list[str], Ref]] = None
    host_header_config: Optional[HostHeaderConfig] = None
    http_request_method_config: Optional[HttpRequestMethodConfig] = None
    path_pattern_config: Optional[PathPatternConfig] = None
    source_ip_config: Optional[SourceIpConfig] = None


@dataclass
class SourceIpConfig(PropertyType):
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[Union[list[str], Ref]] = None


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


@dataclass
class Transform(PropertyType):
    TYPE = "Type"
    URL_REWRITE_CONFIG = "UrlRewriteConfig"
    HOST_HEADER_REWRITE_CONFIG = "HostHeaderRewriteConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "url_rewrite_config": "UrlRewriteConfig",
        "host_header_rewrite_config": "HostHeaderRewriteConfig",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url_rewrite_config: Optional[RewriteConfigObject] = None
    host_header_rewrite_config: Optional[RewriteConfigObject] = None

