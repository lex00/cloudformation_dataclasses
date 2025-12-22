from __future__ import annotations

"""RouteTablePublic - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteTablePublic:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[VPC] = ref()
