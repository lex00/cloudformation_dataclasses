from __future__ import annotations

"""AuroraCluster - AWS::RDS::DBCluster resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AuroraCluster:
    """AWS::RDS::DBCluster resource."""

    resource: DBCluster
    database_name = 'dms_sample'
    backup_retention_period = 7
    db_subnet_group_name: Ref[AuroraDBSubnetGroup] = ref()
    engine = 'aurora-postgresql'
    snapshot_identifier = ref(SnapshotIdentifier)
    vpc_security_group_ids = [ref("AuroraSecurityGroup")]
    storage_encrypted = True
    deletion_policy = 'Retain'
