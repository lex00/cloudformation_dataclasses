from __future__ import annotations

"""InboundHTTPPublicNetworkAclEntry - AWS::EC2::NetworkAclEntry resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InboundHTTPPublicNetworkAclEntryPortRange:
    resource: PortRange
    # Unknown CF key: From = '0'
    # Unknown CF key: To = '65535'


@cloudformation_dataclass
class InboundHTTPPublicNetworkAclEntry:
    """AWS::EC2::NetworkAclEntry resource."""

    resource: NetworkAclEntry
    network_acl_id = ref(PublicNetworkAcl)
    rule_number = '100'
    protocol = '-1'
    rule_action = 'allow'
    egress = 'false'
    cidr_block = '0.0.0.0/0'
    port_range = InboundHTTPPublicNetworkAclEntryPortRange
