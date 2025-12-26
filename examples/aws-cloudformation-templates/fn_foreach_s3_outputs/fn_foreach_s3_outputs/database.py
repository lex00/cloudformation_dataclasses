"""Database resources: AuroraDBSubnetGroup, AuroraCluster, AuroraDB."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AuroraDBSubnetGroup:
    """AWS::RDS::DBSubnetGroup resource."""

    resource: rds.DBSubnetGroup
    db_subnet_group_description = 'Subnets available for the Aurora SampleDB DB Instance'
    subnet_ids = [ref(DBSubnet1), ref(DBSubnet2)]


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


@cloudformation_dataclass
class AuroraDBTagFormat:
    resource: rds.db_proxy.TagFormat
    key = 'Application'
    value = AWS_STACK_ID


@cloudformation_dataclass
class AuroraDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
    db_cluster_identifier = ref(AuroraCluster)
    db_instance_class = 'db.t3.medium'
    db_instance_identifier = 'dms-sample'
    db_subnet_group_name = ref(AuroraDBSubnetGroup)
    engine = 'aurora-postgresql'
    multi_az = False
    publicly_accessible = False
    tags = [AuroraDBTagFormat]
    depends_on = ["AuroraCluster"]
    deletion_policy = 'Retain'
