from __future__ import annotations

"""AuroraDBSubnetGroup - AWS::RDS::DBSubnetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AuroraDBSubnetGroup:
    """AWS::RDS::DBSubnetGroup resource."""

    resource: DBSubnetGroup
    db_subnet_group_description = 'Subnets available for the Aurora SampleDB DB Instance'
    subnet_ids = [ref("DBSubnet1"), ref("DBSubnet2")]
