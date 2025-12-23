"""AuroraDB - AWS::RDS::DBInstance resource."""

from .. import *  # noqa: F403


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
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]
    depends_on = ["AuroraCluster"]
    deletion_policy = 'Retain'
