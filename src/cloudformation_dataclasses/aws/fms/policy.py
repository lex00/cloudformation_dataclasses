"""PropertyTypes for AWS::FMS::Policy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IEMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "account": "ACCOUNT",
        "orgunit": "ORGUNIT",
    }

    account: Optional[Union[list[str], Ref]] = None
    orgunit: Optional[Union[list[str], Ref]] = None


@dataclass
class IcmpTypeCode(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "code": "Code",
    }

    type_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkAclCommonPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "network_acl_entry_set": "NetworkAclEntrySet",
    }

    network_acl_entry_set: Optional[NetworkAclEntrySet] = None


@dataclass
class NetworkAclEntry(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "firewall_deployment_model": "FirewallDeploymentModel",
    }

    firewall_deployment_model: Optional[Union[str, FirewallDeploymentModel, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyOption(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
    }

    from_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecurityServicePolicyData(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "firewall_deployment_model": "FirewallDeploymentModel",
    }

    firewall_deployment_model: Optional[Union[str, FirewallDeploymentModel, Ref, GetAtt, Sub]] = None

