"""DMSReplicationInstance - AWS::DMS::ReplicationInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DMSReplicationInstance:
    """AWS::DMS::ReplicationInstance resource."""

    resource: dms.ReplicationInstance
    availability_zone = get_att(DBSubnet1, "AvailabilityZone")
    publicly_accessible = False
    replication_instance_class = 'dms.t3.medium'
    replication_instance_identifier = 'aurora-s3-repinstance-sampledb'
    replication_subnet_group_identifier = ref(DMSReplicationSubnetGroup)
    vpc_security_group_ids = [ref(DMSSecurityGroup)]
    depends_on = ["DMSReplicationSubnetGroup", "DMSSecurityGroup"]
