"""PeerRoute5 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerRoute5:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(4, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '5RouteTableCondition'
