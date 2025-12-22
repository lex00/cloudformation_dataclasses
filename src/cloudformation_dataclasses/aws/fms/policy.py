"""PropertyTypes for AWS::FMS::Policy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountRoleStatus:
    """AccountRoleStatus enum values."""

    READY = "READY"
    CREATING = "CREATING"
    PENDING_DELETION = "PENDING_DELETION"
    DELETING = "DELETING"
    DELETED = "DELETED"


class CustomerPolicyScopeIdType:
    """CustomerPolicyScopeIdType enum values."""

    ACCOUNT = "ACCOUNT"
    ORG_UNIT = "ORG_UNIT"


class CustomerPolicyStatus:
    """CustomerPolicyStatus enum values."""

    ACTIVE = "ACTIVE"
    OUT_OF_ADMIN_SCOPE = "OUT_OF_ADMIN_SCOPE"


class DependentServiceName:
    """DependentServiceName enum values."""

    AWSCONFIG = "AWSCONFIG"
    AWSWAF = "AWSWAF"
    AWSSHIELD_ADVANCED = "AWSSHIELD_ADVANCED"
    AWSVPC = "AWSVPC"


class DestinationType:
    """DestinationType enum values."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"
    PREFIX_LIST = "PREFIX_LIST"


class EntryType:
    """EntryType enum values."""

    FMS_MANAGED_FIRST_ENTRY = "FMS_MANAGED_FIRST_ENTRY"
    FMS_MANAGED_LAST_ENTRY = "FMS_MANAGED_LAST_ENTRY"
    CUSTOM_ENTRY = "CUSTOM_ENTRY"


class EntryViolationReason:
    """EntryViolationReason enum values."""

    MISSING_EXPECTED_ENTRY = "MISSING_EXPECTED_ENTRY"
    INCORRECT_ENTRY_ORDER = "INCORRECT_ENTRY_ORDER"
    ENTRY_CONFLICT = "ENTRY_CONFLICT"


class FailedItemReason:
    """FailedItemReason enum values."""

    NOT_VALID_ARN = "NOT_VALID_ARN"
    NOT_VALID_PARTITION = "NOT_VALID_PARTITION"
    NOT_VALID_REGION = "NOT_VALID_REGION"
    NOT_VALID_SERVICE = "NOT_VALID_SERVICE"
    NOT_VALID_RESOURCE_TYPE = "NOT_VALID_RESOURCE_TYPE"
    NOT_VALID_ACCOUNT_ID = "NOT_VALID_ACCOUNT_ID"


class FirewallDeploymentModel:
    """FirewallDeploymentModel enum values."""

    CENTRALIZED = "CENTRALIZED"
    DISTRIBUTED = "DISTRIBUTED"


class MarketplaceSubscriptionOnboardingStatus:
    """MarketplaceSubscriptionOnboardingStatus enum values."""

    NO_SUBSCRIPTION = "NO_SUBSCRIPTION"
    NOT_COMPLETE = "NOT_COMPLETE"
    COMPLETE = "COMPLETE"


class NetworkAclRuleAction:
    """NetworkAclRuleAction enum values."""

    ALLOW = "allow"
    DENY = "deny"


class NetworkFirewallOverrideAction:
    """NetworkFirewallOverrideAction enum values."""

    DROP_TO_ALERT = "DROP_TO_ALERT"


class OrganizationStatus:
    """OrganizationStatus enum values."""

    ONBOARDING = "ONBOARDING"
    ONBOARDING_COMPLETE = "ONBOARDING_COMPLETE"
    OFFBOARDING = "OFFBOARDING"
    OFFBOARDING_COMPLETE = "OFFBOARDING_COMPLETE"


class PolicyComplianceStatusType:
    """PolicyComplianceStatusType enum values."""

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"


class RemediationActionType:
    """RemediationActionType enum values."""

    REMOVE = "REMOVE"
    MODIFY = "MODIFY"


class ResourceSetStatus:
    """ResourceSetStatus enum values."""

    ACTIVE = "ACTIVE"
    OUT_OF_ADMIN_SCOPE = "OUT_OF_ADMIN_SCOPE"


class ResourceTagLogicalOperator:
    """ResourceTagLogicalOperator enum values."""

    AND = "AND"
    OR = "OR"


class RuleOrder:
    """RuleOrder enum values."""

    STRICT_ORDER = "STRICT_ORDER"
    DEFAULT_ACTION_ORDER = "DEFAULT_ACTION_ORDER"


class SecurityServiceType:
    """SecurityServiceType enum values."""

    WAF = "WAF"
    WAFV2 = "WAFV2"
    SHIELD_ADVANCED = "SHIELD_ADVANCED"
    SECURITY_GROUPS_COMMON = "SECURITY_GROUPS_COMMON"
    SECURITY_GROUPS_CONTENT_AUDIT = "SECURITY_GROUPS_CONTENT_AUDIT"
    SECURITY_GROUPS_USAGE_AUDIT = "SECURITY_GROUPS_USAGE_AUDIT"
    NETWORK_FIREWALL = "NETWORK_FIREWALL"
    DNS_FIREWALL = "DNS_FIREWALL"
    THIRD_PARTY_FIREWALL = "THIRD_PARTY_FIREWALL"
    IMPORT_NETWORK_FIREWALL = "IMPORT_NETWORK_FIREWALL"
    NETWORK_ACL_COMMON = "NETWORK_ACL_COMMON"


class StreamExceptionPolicy:
    """StreamExceptionPolicy enum values."""

    DROP = "DROP"
    CONTINUE = "CONTINUE"
    REJECT = "REJECT"
    FMS_IGNORE = "FMS_IGNORE"


class TargetType:
    """TargetType enum values."""

    GATEWAY = "GATEWAY"
    CARRIER_GATEWAY = "CARRIER_GATEWAY"
    INSTANCE = "INSTANCE"
    LOCAL_GATEWAY = "LOCAL_GATEWAY"
    NAT_GATEWAY = "NAT_GATEWAY"
    NETWORK_INTERFACE = "NETWORK_INTERFACE"
    VPC_ENDPOINT = "VPC_ENDPOINT"
    VPC_PEERING_CONNECTION = "VPC_PEERING_CONNECTION"
    EGRESS_ONLY_INTERNET_GATEWAY = "EGRESS_ONLY_INTERNET_GATEWAY"
    TRANSIT_GATEWAY = "TRANSIT_GATEWAY"


class ThirdPartyFirewall:
    """ThirdPartyFirewall enum values."""

    PALO_ALTO_NETWORKS_CLOUD_NGFW = "PALO_ALTO_NETWORKS_CLOUD_NGFW"
    FORTIGATE_CLOUD_NATIVE_FIREWALL = "FORTIGATE_CLOUD_NATIVE_FIREWALL"


class ThirdPartyFirewallAssociationStatus:
    """ThirdPartyFirewallAssociationStatus enum values."""

    ONBOARDING = "ONBOARDING"
    ONBOARD_COMPLETE = "ONBOARD_COMPLETE"
    OFFBOARDING = "OFFBOARDING"
    OFFBOARD_COMPLETE = "OFFBOARD_COMPLETE"
    NOT_EXIST = "NOT_EXIST"


class ViolationReason:
    """ViolationReason enum values."""

    WEB_ACL_MISSING_RULE_GROUP = "WEB_ACL_MISSING_RULE_GROUP"
    RESOURCE_MISSING_WEB_ACL = "RESOURCE_MISSING_WEB_ACL"
    RESOURCE_INCORRECT_WEB_ACL = "RESOURCE_INCORRECT_WEB_ACL"
    RESOURCE_MISSING_SHIELD_PROTECTION = "RESOURCE_MISSING_SHIELD_PROTECTION"
    RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION = "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION"
    RESOURCE_MISSING_SECURITY_GROUP = "RESOURCE_MISSING_SECURITY_GROUP"
    RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP = "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP"
    SECURITY_GROUP_UNUSED = "SECURITY_GROUP_UNUSED"
    SECURITY_GROUP_REDUNDANT = "SECURITY_GROUP_REDUNDANT"
    FMS_CREATED_SECURITY_GROUP_EDITED = "FMS_CREATED_SECURITY_GROUP_EDITED"
    MISSING_FIREWALL = "MISSING_FIREWALL"
    MISSING_FIREWALL_SUBNET_IN_AZ = "MISSING_FIREWALL_SUBNET_IN_AZ"
    MISSING_EXPECTED_ROUTE_TABLE = "MISSING_EXPECTED_ROUTE_TABLE"
    NETWORK_FIREWALL_POLICY_MODIFIED = "NETWORK_FIREWALL_POLICY_MODIFIED"
    FIREWALL_SUBNET_IS_OUT_OF_SCOPE = "FIREWALL_SUBNET_IS_OUT_OF_SCOPE"
    INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE = "INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE"
    FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE = "FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE"
    UNEXPECTED_FIREWALL_ROUTES = "UNEXPECTED_FIREWALL_ROUTES"
    UNEXPECTED_TARGET_GATEWAY_ROUTES = "UNEXPECTED_TARGET_GATEWAY_ROUTES"
    TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY = "TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY"
    INVALID_ROUTE_CONFIGURATION = "INVALID_ROUTE_CONFIGURATION"
    MISSING_TARGET_GATEWAY = "MISSING_TARGET_GATEWAY"
    INTERNET_TRAFFIC_NOT_INSPECTED = "INTERNET_TRAFFIC_NOT_INSPECTED"
    BLACK_HOLE_ROUTE_DETECTED = "BLACK_HOLE_ROUTE_DETECTED"
    BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET = "BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET"
    RESOURCE_MISSING_DNS_FIREWALL = "RESOURCE_MISSING_DNS_FIREWALL"
    ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT = "ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT"
    FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT = "FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT"
    INVALID_NETWORK_ACL_ENTRY = "INVALID_NETWORK_ACL_ENTRY"
    WEB_ACL_CONFIGURATION_OR_SCOPE_OF_USE = "WEB_ACL_CONFIGURATION_OR_SCOPE_OF_USE"


@dataclass
class IEMap(PropertyType):
    ACCOUNT = "ACCOUNT"
    ORGUNIT = "ORGUNIT"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account": "ACCOUNT",
        "orgunit": "ORGUNIT",
    }

    account: Optional[Union[list[str], Ref]] = None
    orgunit: Optional[Union[list[str], Ref]] = None


@dataclass
class IcmpTypeCode(PropertyType):
    TYPE = "Type"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "code": "Code",
    }

    type_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkAclCommonPolicy(PropertyType):
    NETWORK_ACL_ENTRY_SET = "NetworkAclEntrySet"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_acl_entry_set": "NetworkAclEntrySet",
    }

    network_acl_entry_set: Optional[NetworkAclEntrySet] = None


@dataclass
class NetworkAclEntry(PropertyType):
    PORT_RANGE = "PortRange"
    ICMP_TYPE_CODE = "IcmpTypeCode"
    RULE_ACTION = "RuleAction"
    CIDR_BLOCK = "CidrBlock"
    EGRESS = "Egress"
    IPV6_CIDR_BLOCK = "Ipv6CidrBlock"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port_range": "PortRange",
        "icmp_type_code": "IcmpTypeCode",
        "rule_action": "RuleAction",
        "cidr_block": "CidrBlock",
        "egress": "Egress",
        "ipv6_cidr_block": "Ipv6CidrBlock",
        "protocol": "Protocol",
    }

    port_range: Optional[PortRange] = None
    icmp_type_code: Optional[IcmpTypeCode] = None
    rule_action: Optional[Union[str, NetworkAclRuleAction, Ref, GetAtt, Sub]] = None
    cidr_block: Optional[Union[str, Ref, GetAtt, Sub]] = None
    egress: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ipv6_cidr_block: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkAclEntrySet(PropertyType):
    LAST_ENTRIES = "LastEntries"
    FORCE_REMEDIATE_FOR_FIRST_ENTRIES = "ForceRemediateForFirstEntries"
    FIRST_ENTRIES = "FirstEntries"
    FORCE_REMEDIATE_FOR_LAST_ENTRIES = "ForceRemediateForLastEntries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "last_entries": "LastEntries",
        "force_remediate_for_first_entries": "ForceRemediateForFirstEntries",
        "first_entries": "FirstEntries",
        "force_remediate_for_last_entries": "ForceRemediateForLastEntries",
    }

    last_entries: Optional[list[NetworkAclEntry]] = None
    force_remediate_for_first_entries: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    first_entries: Optional[list[NetworkAclEntry]] = None
    force_remediate_for_last_entries: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkFirewallPolicy(PropertyType):
    FIREWALL_DEPLOYMENT_MODEL = "FirewallDeploymentModel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "firewall_deployment_model": "FirewallDeploymentModel",
    }

    firewall_deployment_model: Optional[Union[str, FirewallDeploymentModel, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyOption(PropertyType):
    NETWORK_FIREWALL_POLICY = "NetworkFirewallPolicy"
    NETWORK_ACL_COMMON_POLICY = "NetworkAclCommonPolicy"
    THIRD_PARTY_FIREWALL_POLICY = "ThirdPartyFirewallPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_firewall_policy": "NetworkFirewallPolicy",
        "network_acl_common_policy": "NetworkAclCommonPolicy",
        "third_party_firewall_policy": "ThirdPartyFirewallPolicy",
    }

    network_firewall_policy: Optional[NetworkFirewallPolicy] = None
    network_acl_common_policy: Optional[NetworkAclCommonPolicy] = None
    third_party_firewall_policy: Optional[ThirdPartyFirewallPolicy] = None


@dataclass
class PolicyTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortRange(PropertyType):
    FROM = "From"
    TO = "To"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
    }

    from_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecurityServicePolicyData(PropertyType):
    MANAGED_SERVICE_DATA = "ManagedServiceData"
    TYPE = "Type"
    POLICY_OPTION = "PolicyOption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_service_data": "ManagedServiceData",
        "type_": "Type",
        "policy_option": "PolicyOption",
    }

    managed_service_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SecurityServiceType, Ref, GetAtt, Sub]] = None
    policy_option: Optional[PolicyOption] = None


@dataclass
class ThirdPartyFirewallPolicy(PropertyType):
    FIREWALL_DEPLOYMENT_MODEL = "FirewallDeploymentModel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "firewall_deployment_model": "FirewallDeploymentModel",
    }

    firewall_deployment_model: Optional[Union[str, FirewallDeploymentModel, Ref, GetAtt, Sub]] = None

