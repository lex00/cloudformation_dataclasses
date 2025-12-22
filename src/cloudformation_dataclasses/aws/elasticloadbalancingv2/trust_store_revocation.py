"""PropertyTypes for AWS::ElasticLoadBalancingV2::TrustStoreRevocation."""

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
class RevocationContent(PropertyType):
    S3_OBJECT_VERSION = "S3ObjectVersion"
    S3_BUCKET = "S3Bucket"
    S3_KEY = "S3Key"
    REVOCATION_TYPE = "RevocationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_object_version": "S3ObjectVersion",
        "s3_bucket": "S3Bucket",
        "s3_key": "S3Key",
        "revocation_type": "RevocationType",
    }

    s3_object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revocation_type: Optional[Union[str, RevocationType, Ref, GetAtt, Sub]] = None


@dataclass
class TrustStoreRevocation(PropertyType):
    NUMBER_OF_REVOKED_ENTRIES = "NumberOfRevokedEntries"
    TRUST_STORE_ARN = "TrustStoreArn"
    REVOCATION_TYPE = "RevocationType"
    REVOCATION_ID = "RevocationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_revoked_entries": "NumberOfRevokedEntries",
        "trust_store_arn": "TrustStoreArn",
        "revocation_type": "RevocationType",
        "revocation_id": "RevocationId",
    }

    number_of_revoked_entries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    trust_store_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revocation_type: Optional[Union[str, RevocationType, Ref, GetAtt, Sub]] = None
    revocation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

