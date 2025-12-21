from __future__ import annotations

"""PublicSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(0, {
    'Fn::GetAZs': AWS_REGION,
})
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id: Ref[VPC] = ref()
