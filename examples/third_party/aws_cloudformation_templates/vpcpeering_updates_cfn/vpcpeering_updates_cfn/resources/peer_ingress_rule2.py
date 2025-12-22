"""PeerIngressRule2 - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerIngressRule2:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer CIDR, ${PeerName}')
    group_id = Select(1, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '2SecurityGroupCondition'
