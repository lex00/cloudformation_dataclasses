"""PropertyTypes for AWS::Route53Resolver::ResolverEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Action:
    """Action enum values."""

    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    ALERT = "ALERT"


class AutodefinedReverseFlag:
    """AutodefinedReverseFlag enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    USE_LOCAL_RESOURCE_SETTING = "USE_LOCAL_RESOURCE_SETTING"


class BlockOverrideDnsType:
    """BlockOverrideDnsType enum values."""

    CNAME = "CNAME"


class BlockResponse:
    """BlockResponse enum values."""

    NODATA = "NODATA"
    NXDOMAIN = "NXDOMAIN"
    OVERRIDE = "OVERRIDE"


class ConfidenceThreshold:
    """ConfidenceThreshold enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class DnsThreatProtection:
    """DnsThreatProtection enum values."""

    DGA = "DGA"
    DNS_TUNNELING = "DNS_TUNNELING"
    DICTIONARY_DGA = "DICTIONARY_DGA"


class FirewallDomainImportOperation:
    """FirewallDomainImportOperation enum values."""

    REPLACE = "REPLACE"


class FirewallDomainListStatus:
    """FirewallDomainListStatus enum values."""

    COMPLETE = "COMPLETE"
    COMPLETE_IMPORT_FAILED = "COMPLETE_IMPORT_FAILED"
    IMPORTING = "IMPORTING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class FirewallDomainRedirectionAction:
    """FirewallDomainRedirectionAction enum values."""

    INSPECT_REDIRECTION_DOMAIN = "INSPECT_REDIRECTION_DOMAIN"
    TRUST_REDIRECTION_DOMAIN = "TRUST_REDIRECTION_DOMAIN"


class FirewallDomainUpdateOperation:
    """FirewallDomainUpdateOperation enum values."""

    ADD = "ADD"
    REMOVE = "REMOVE"
    REPLACE = "REPLACE"


class FirewallFailOpenStatus:
    """FirewallFailOpenStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    USE_LOCAL_RESOURCE_SETTING = "USE_LOCAL_RESOURCE_SETTING"


class FirewallRuleGroupAssociationStatus:
    """FirewallRuleGroupAssociationStatus enum values."""

    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class FirewallRuleGroupStatus:
    """FirewallRuleGroupStatus enum values."""

    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class IpAddressStatus:
    """IpAddressStatus enum values."""

    CREATING = "CREATING"
    FAILED_CREATION = "FAILED_CREATION"
    ATTACHING = "ATTACHING"
    ATTACHED = "ATTACHED"
    REMAP_DETACHING = "REMAP_DETACHING"
    REMAP_ATTACHING = "REMAP_ATTACHING"
    DETACHING = "DETACHING"
    FAILED_RESOURCE_GONE = "FAILED_RESOURCE_GONE"
    DELETING = "DELETING"
    DELETE_FAILED_FAS_EXPIRED = "DELETE_FAILED_FAS_EXPIRED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    ISOLATED = "ISOLATED"


class MutationProtectionStatus:
    """MutationProtectionStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OutpostResolverStatus:
    """OutpostResolverStatus enum values."""

    CREATING = "CREATING"
    OPERATIONAL = "OPERATIONAL"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTION_NEEDED = "ACTION_NEEDED"
    FAILED_CREATION = "FAILED_CREATION"
    FAILED_DELETION = "FAILED_DELETION"


class Protocol:
    """Protocol enum values."""

    DOH = "DoH"
    DO53 = "Do53"
    DOH_FIPS = "DoH-FIPS"


class ResolverAutodefinedReverseStatus:
    """ResolverAutodefinedReverseStatus enum values."""

    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    UPDATING_TO_USE_LOCAL_RESOURCE_SETTING = "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING"
    USE_LOCAL_RESOURCE_SETTING = "USE_LOCAL_RESOURCE_SETTING"


class ResolverDNSSECValidationStatus:
    """ResolverDNSSECValidationStatus enum values."""

    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    UPDATING_TO_USE_LOCAL_RESOURCE_SETTING = "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING"
    USE_LOCAL_RESOURCE_SETTING = "USE_LOCAL_RESOURCE_SETTING"


class ResolverEndpointDirection:
    """ResolverEndpointDirection enum values."""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    INBOUND_DELEGATION = "INBOUND_DELEGATION"


class ResolverEndpointStatus:
    """ResolverEndpointStatus enum values."""

    CREATING = "CREATING"
    OPERATIONAL = "OPERATIONAL"
    UPDATING = "UPDATING"
    AUTO_RECOVERING = "AUTO_RECOVERING"
    ACTION_NEEDED = "ACTION_NEEDED"
    DELETING = "DELETING"


class ResolverEndpointType:
    """ResolverEndpointType enum values."""

    IPV6 = "IPV6"
    IPV4 = "IPV4"
    DUALSTACK = "DUALSTACK"


class ResolverQueryLogConfigAssociationError:
    """ResolverQueryLogConfigAssociationError enum values."""

    NONE = "NONE"
    DESTINATION_NOT_FOUND = "DESTINATION_NOT_FOUND"
    ACCESS_DENIED = "ACCESS_DENIED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"


class ResolverQueryLogConfigAssociationStatus:
    """ResolverQueryLogConfigAssociationStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    ACTION_NEEDED = "ACTION_NEEDED"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ResolverQueryLogConfigStatus:
    """ResolverQueryLogConfigStatus enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ResolverRuleAssociationStatus:
    """ResolverRuleAssociationStatus enum values."""

    CREATING = "CREATING"
    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    OVERRIDDEN = "OVERRIDDEN"


class ResolverRuleStatus:
    """ResolverRuleStatus enum values."""

    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    FAILED = "FAILED"


class RuleTypeOption:
    """RuleTypeOption enum values."""

    FORWARD = "FORWARD"
    SYSTEM = "SYSTEM"
    RECURSIVE = "RECURSIVE"
    DELEGATE = "DELEGATE"


class ShareStatus:
    """ShareStatus enum values."""

    NOT_SHARED = "NOT_SHARED"
    SHARED_WITH_ME = "SHARED_WITH_ME"
    SHARED_BY_ME = "SHARED_BY_ME"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Validation:
    """Validation enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    USE_LOCAL_RESOURCE_SETTING = "USE_LOCAL_RESOURCE_SETTING"


@dataclass
class IpAddressRequest(PropertyType):
    IPV6 = "Ipv6"
    IP = "Ip"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6": "Ipv6",
        "ip": "Ip",
        "subnet_id": "SubnetId",
    }

    ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

