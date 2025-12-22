"""PropertyTypes for AWS::ElasticLoadBalancingV2::LoadBalancer."""

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
class LoadBalancerAttribute(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MinimumLoadBalancerCapacity(PropertyType):
    CAPACITY_UNITS = "CapacityUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_units": "CapacityUnits",
    }

    capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SubnetMapping(PropertyType):
    ALLOCATION_ID = "AllocationId"
    I_PV6_ADDRESS = "IPv6Address"
    SUBNET_ID = "SubnetId"
    SOURCE_NAT_IPV6_PREFIX = "SourceNatIpv6Prefix"
    PRIVATE_I_PV4_ADDRESS = "PrivateIPv4Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_id": "AllocationId",
        "i_pv6_address": "IPv6Address",
        "subnet_id": "SubnetId",
        "source_nat_ipv6_prefix": "SourceNatIpv6Prefix",
        "private_i_pv4_address": "PrivateIPv4Address",
    }

    allocation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    i_pv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_nat_ipv6_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_i_pv4_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

