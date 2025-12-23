"""PropertyTypes for AWS::Route53Resolver::FirewallRuleGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FirewallRule(PropertyType):
    QTYPE = "Qtype"
    ACTION = "Action"
    PRIORITY = "Priority"
    BLOCK_OVERRIDE_DOMAIN = "BlockOverrideDomain"
    DNS_THREAT_PROTECTION = "DnsThreatProtection"
    FIREWALL_DOMAIN_LIST_ID = "FirewallDomainListId"
    FIREWALL_THREAT_PROTECTION_ID = "FirewallThreatProtectionId"
    CONFIDENCE_THRESHOLD = "ConfidenceThreshold"
    BLOCK_RESPONSE = "BlockResponse"
    BLOCK_OVERRIDE_TTL = "BlockOverrideTtl"
    BLOCK_OVERRIDE_DNS_TYPE = "BlockOverrideDnsType"
    FIREWALL_DOMAIN_REDIRECTION_ACTION = "FirewallDomainRedirectionAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "qtype": "Qtype",
        "action": "Action",
        "priority": "Priority",
        "block_override_domain": "BlockOverrideDomain",
        "dns_threat_protection": "DnsThreatProtection",
        "firewall_domain_list_id": "FirewallDomainListId",
        "firewall_threat_protection_id": "FirewallThreatProtectionId",
        "confidence_threshold": "ConfidenceThreshold",
        "block_response": "BlockResponse",
        "block_override_ttl": "BlockOverrideTtl",
        "block_override_dns_type": "BlockOverrideDnsType",
        "firewall_domain_redirection_action": "FirewallDomainRedirectionAction",
    }

    qtype: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    block_override_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_threat_protection: Optional[Union[str, DnsThreatProtection, Ref, GetAtt, Sub]] = None
    firewall_domain_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    firewall_threat_protection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    confidence_threshold: Optional[Union[str, ConfidenceThreshold, Ref, GetAtt, Sub]] = None
    block_response: Optional[Union[str, BlockResponse, Ref, GetAtt, Sub]] = None
    block_override_ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None
    block_override_dns_type: Optional[Union[str, BlockOverrideDnsType, Ref, GetAtt, Sub]] = None
    firewall_domain_redirection_action: Optional[Union[str, FirewallDomainRedirectionAction, Ref, GetAtt, Sub]] = None

