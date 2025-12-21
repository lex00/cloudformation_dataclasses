from __future__ import annotations

"""PeerIngressRule1 - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerIngressRule1:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(0, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
