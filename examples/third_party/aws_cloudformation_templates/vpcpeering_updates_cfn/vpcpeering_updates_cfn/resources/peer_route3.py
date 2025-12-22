"""PeerRoute3 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerRoute3:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id = Select(2, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '3RouteTableCondition'
