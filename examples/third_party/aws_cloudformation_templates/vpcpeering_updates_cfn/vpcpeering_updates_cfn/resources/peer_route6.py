from __future__ import annotations

"""PeerRoute6 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerRoute6:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id = Select(5, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '6RouteTableCondition'
