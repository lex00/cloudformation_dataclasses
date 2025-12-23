"""Compute resources: InboundHTTPPublicNetworkAclEntry, OutboundPublicNetworkAclEntry, PublicSubnetNetworkAclAssociation0, PublicSubnetNetworkAclAssociation1."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InboundHTTPPublicNetworkAclEntryPortRange:
    resource: ec2.network_insights_analysis.PortRange
    from_ = '0'
    to = '65535'


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


@cloudformation_dataclass
class OutboundPublicNetworkAclEntryPortRange:
    resource: ec2.network_insights_analysis.PortRange
    from_ = '0'
    to = '65535'


@cloudformation_dataclass
class OutboundPublicNetworkAclEntry:
    """AWS::EC2::NetworkAclEntry resource."""

    resource: NetworkAclEntry
    network_acl_id = ref(PublicNetworkAcl)
    rule_number = '100'
    protocol = '-1'
    rule_action = 'allow'
    egress = 'true'
    cidr_block = '0.0.0.0/0'
    port_range = OutboundPublicNetworkAclEntryPortRange


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation0:
    """AWS::EC2::SubnetNetworkAclAssociation resource."""

    resource: SubnetNetworkAclAssociation
    subnet_id = ref(PublicSubnet0)
    network_acl_id = ref(PublicNetworkAcl)


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation1:
    """AWS::EC2::SubnetNetworkAclAssociation resource."""

    resource: SubnetNetworkAclAssociation
    subnet_id = ref(PublicSubnet1)
    network_acl_id = ref(PublicNetworkAcl)
