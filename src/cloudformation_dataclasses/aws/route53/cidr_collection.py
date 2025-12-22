"""PropertyTypes for AWS::Route53::CidrCollection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratedRecoveryStatus:
    """AcceleratedRecoveryStatus enum values."""

    ENABLING = "ENABLING"
    ENABLE_FAILED = "ENABLE_FAILED"
    ENABLING_HOSTED_ZONE_LOCKED = "ENABLING_HOSTED_ZONE_LOCKED"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLE_FAILED = "DISABLE_FAILED"
    DISABLED = "DISABLED"
    DISABLING_HOSTED_ZONE_LOCKED = "DISABLING_HOSTED_ZONE_LOCKED"


class AccountLimitType:
    """AccountLimitType enum values."""

    MAX_HEALTH_CHECKS_BY_OWNER = "MAX_HEALTH_CHECKS_BY_OWNER"
    MAX_HOSTED_ZONES_BY_OWNER = "MAX_HOSTED_ZONES_BY_OWNER"
    MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER = "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER"
    MAX_REUSABLE_DELEGATION_SETS_BY_OWNER = "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER"
    MAX_TRAFFIC_POLICIES_BY_OWNER = "MAX_TRAFFIC_POLICIES_BY_OWNER"


class ChangeAction:
    """ChangeAction enum values."""

    CREATE = "CREATE"
    DELETE = "DELETE"
    UPSERT = "UPSERT"


class ChangeStatus:
    """ChangeStatus enum values."""

    PENDING = "PENDING"
    INSYNC = "INSYNC"


class CidrCollectionChangeAction:
    """CidrCollectionChangeAction enum values."""

    PUT = "PUT"
    DELETE_IF_EXISTS = "DELETE_IF_EXISTS"


class CloudWatchRegion:
    """CloudWatchRegion enum values."""

    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    CA_CENTRAL_1 = "ca-central-1"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    AP_EAST_1 = "ap-east-1"
    ME_SOUTH_1 = "me-south-1"
    ME_CENTRAL_1 = "me-central-1"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    CN_NORTH_1 = "cn-north-1"
    AF_SOUTH_1 = "af-south-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    US_GOV_WEST_1 = "us-gov-west-1"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_ISO_EAST_1 = "us-iso-east-1"
    US_ISO_WEST_1 = "us-iso-west-1"
    US_ISOB_EAST_1 = "us-isob-east-1"
    AP_SOUTHEAST_4 = "ap-southeast-4"
    IL_CENTRAL_1 = "il-central-1"
    CA_WEST_1 = "ca-west-1"
    AP_SOUTHEAST_5 = "ap-southeast-5"
    MX_CENTRAL_1 = "mx-central-1"
    US_ISOF_SOUTH_1 = "us-isof-south-1"
    US_ISOF_EAST_1 = "us-isof-east-1"
    AP_SOUTHEAST_7 = "ap-southeast-7"
    AP_EAST_2 = "ap-east-2"
    EU_ISOE_WEST_1 = "eu-isoe-west-1"
    AP_SOUTHEAST_6 = "ap-southeast-6"
    US_ISOB_WEST_1 = "us-isob-west-1"
    EUSC_DE_EAST_1 = "eusc-de-east-1"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"


class HealthCheckRegion:
    """HealthCheckRegion enum values."""

    US_EAST_1 = "us-east-1"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    EU_WEST_1 = "eu-west-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_NORTHEAST_1 = "ap-northeast-1"
    SA_EAST_1 = "sa-east-1"


class HealthCheckType:
    """HealthCheckType enum values."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"
    HTTP_STR_MATCH = "HTTP_STR_MATCH"
    HTTPS_STR_MATCH = "HTTPS_STR_MATCH"
    TCP = "TCP"
    CALCULATED = "CALCULATED"
    CLOUDWATCH_METRIC = "CLOUDWATCH_METRIC"
    RECOVERY_CONTROL = "RECOVERY_CONTROL"


class HostedZoneLimitType:
    """HostedZoneLimitType enum values."""

    MAX_RRSETS_BY_ZONE = "MAX_RRSETS_BY_ZONE"
    MAX_VPCS_ASSOCIATED_BY_ZONE = "MAX_VPCS_ASSOCIATED_BY_ZONE"


class HostedZoneType:
    """HostedZoneType enum values."""

    PRIVATEHOSTEDZONE = "PrivateHostedZone"


class InsufficientDataHealthStatus:
    """InsufficientDataHealthStatus enum values."""

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    LASTKNOWNSTATUS = "LastKnownStatus"


class RRType:
    """RRType enum values."""

    SOA = "SOA"
    A = "A"
    TXT = "TXT"
    NS = "NS"
    CNAME = "CNAME"
    MX = "MX"
    NAPTR = "NAPTR"
    PTR = "PTR"
    SRV = "SRV"
    SPF = "SPF"
    AAAA = "AAAA"
    CAA = "CAA"
    DS = "DS"
    TLSA = "TLSA"
    SSHFP = "SSHFP"
    SVCB = "SVCB"
    HTTPS = "HTTPS"


class ResettableElementName:
    """ResettableElementName enum values."""

    FULLYQUALIFIEDDOMAINNAME = "FullyQualifiedDomainName"
    REGIONS = "Regions"
    RESOURCEPATH = "ResourcePath"
    CHILDHEALTHCHECKS = "ChildHealthChecks"


class ResourceRecordSetFailover:
    """ResourceRecordSetFailover enum values."""

    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"


class ResourceRecordSetRegion:
    """ResourceRecordSetRegion enum values."""

    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    CA_CENTRAL_1 = "ca-central-1"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    CN_NORTH_1 = "cn-north-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    AP_EAST_1 = "ap-east-1"
    ME_SOUTH_1 = "me-south-1"
    ME_CENTRAL_1 = "me-central-1"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AF_SOUTH_1 = "af-south-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    AP_SOUTHEAST_4 = "ap-southeast-4"
    IL_CENTRAL_1 = "il-central-1"
    CA_WEST_1 = "ca-west-1"
    AP_SOUTHEAST_5 = "ap-southeast-5"
    MX_CENTRAL_1 = "mx-central-1"
    AP_SOUTHEAST_7 = "ap-southeast-7"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_GOV_WEST_1 = "us-gov-west-1"
    AP_EAST_2 = "ap-east-2"
    AP_SOUTHEAST_6 = "ap-southeast-6"
    EUSC_DE_EAST_1 = "eusc-de-east-1"


class ReusableDelegationSetLimitType:
    """ReusableDelegationSetLimitType enum values."""

    MAX_ZONES_BY_REUSABLE_DELEGATION_SET = "MAX_ZONES_BY_REUSABLE_DELEGATION_SET"


class Statistic:
    """Statistic enum values."""

    AVERAGE = "Average"
    SUM = "Sum"
    SAMPLECOUNT = "SampleCount"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"


class TagResourceType:
    """TagResourceType enum values."""

    HEALTHCHECK = "healthcheck"
    HOSTEDZONE = "hostedzone"


class VPCRegion:
    """VPCRegion enum values."""

    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    AP_EAST_1 = "ap-east-1"
    ME_SOUTH_1 = "me-south-1"
    US_GOV_WEST_1 = "us-gov-west-1"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_ISO_EAST_1 = "us-iso-east-1"
    US_ISO_WEST_1 = "us-iso-west-1"
    US_ISOB_EAST_1 = "us-isob-east-1"
    ME_CENTRAL_1 = "me-central-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    CA_CENTRAL_1 = "ca-central-1"
    CN_NORTH_1 = "cn-north-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    AF_SOUTH_1 = "af-south-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    AP_SOUTHEAST_4 = "ap-southeast-4"
    IL_CENTRAL_1 = "il-central-1"
    CA_WEST_1 = "ca-west-1"
    AP_SOUTHEAST_5 = "ap-southeast-5"
    MX_CENTRAL_1 = "mx-central-1"
    US_ISOF_SOUTH_1 = "us-isof-south-1"
    US_ISOF_EAST_1 = "us-isof-east-1"
    AP_SOUTHEAST_7 = "ap-southeast-7"
    AP_EAST_2 = "ap-east-2"
    EU_ISOE_WEST_1 = "eu-isoe-west-1"
    AP_SOUTHEAST_6 = "ap-southeast-6"
    US_ISOB_WEST_1 = "us-isob-west-1"
    EUSC_DE_EAST_1 = "eusc-de-east-1"


@dataclass
class Location(PropertyType):
    CIDR_LIST = "CidrList"
    LOCATION_NAME = "LocationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr_list": "CidrList",
        "location_name": "LocationName",
    }

    cidr_list: Optional[Union[list[str], Ref]] = None
    location_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

