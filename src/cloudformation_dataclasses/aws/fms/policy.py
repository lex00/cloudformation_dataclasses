"""PropertyTypes for AWS::FMS::Policy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

