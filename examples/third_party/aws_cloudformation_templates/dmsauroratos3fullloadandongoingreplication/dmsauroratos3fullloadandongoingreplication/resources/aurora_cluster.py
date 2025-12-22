"""AuroraCluster - AWS::RDS::DBCluster resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AuroraCluster:
    """AWS::RDS::DBCluster resource."""

    resource: rds.DBCluster
    database_name = 'dms_sample'
    backup_retention_period = 7
    db_subnet_group_name = ref(AuroraDBSubnetGroup)
    engine = 'aurora-postgresql'
    snapshot_identifier = ref(SnapshotIdentifier)
    vpc_security_group_ids = [ref(AuroraSecurityGroup)]
    storage_encrypted = True
    deletion_policy = 'Retain'
