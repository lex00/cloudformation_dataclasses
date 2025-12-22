"""DMSReplicationSubnetGroup - AWS::DMS::ReplicationSubnetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DMSReplicationSubnetGroup:
    """AWS::DMS::ReplicationSubnetGroup resource."""

    resource: ReplicationSubnetGroup
    replication_subnet_group_description = 'Subnets available for DMS'
    subnet_ids = [ref(DBSubnet1), ref(DBSubnet2)]
