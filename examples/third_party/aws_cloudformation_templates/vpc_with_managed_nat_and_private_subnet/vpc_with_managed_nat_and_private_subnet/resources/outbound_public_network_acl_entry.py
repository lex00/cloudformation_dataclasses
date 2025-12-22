"""OutboundPublicNetworkAclEntry - AWS::EC2::NetworkAclEntry resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OutboundPublicNetworkAclEntryPortRange:
    resource: ec2.PortRange
    # Unknown CF key: From = '0'
    # Unknown CF key: To = '65535'


@cloudformation_dataclass
class OutboundPublicNetworkAclEntry:
    """AWS::EC2::NetworkAclEntry resource."""

    resource: ec2.NetworkAclEntry
    network_acl_id = ref(PublicNetworkAcl)
    rule_number = '100'
    protocol = '-1'
    rule_action = 'allow'
    egress = 'true'
    cidr_block = '0.0.0.0/0'
    port_range = OutboundPublicNetworkAclEntryPortRange
