"""Compute resources: PeerIngressRule1, PeerIngressRule2, PeerIngressRule3, PeerIngressRule4, PeerIngressRule5, PeerIngressRule6."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerIngressRule1:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(0, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)


@cloudformation_dataclass
class PeerIngressRule2:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer CIDR, ${PeerName}')
    group_id = Select(1, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '2SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule3:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(2, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '3SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule4:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(3, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '4SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule5:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(4, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '5SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule6:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(5, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '6SecurityGroupCondition'
