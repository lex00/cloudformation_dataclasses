"""ReplicaDB - AWS::RDS::DBInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ReplicaDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
    source_db_instance_identifier = ref(MainDB)
    publicly_accessible = False
    db_instance_class = ref(DBInstanceClass)
    tags = [{
        'Key': 'Name',
        'Value': 'Read Replica Database',
    }]
    condition = 'EnableReadReplica'
    deletion_policy = 'Retain'
