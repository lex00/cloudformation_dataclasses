"""ReplicaDB - AWS::RDS::DBInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ReplicaDBTagFormat:
    resource: TagFormat
    key = 'Name'
    value = 'Read Replica Database'


@cloudformation_dataclass
class ReplicaDB:
    """AWS::RDS::DBInstance resource."""

    resource: DBInstance
    source_db_instance_identifier = ref(MainDB)
    publicly_accessible = False
    db_instance_class = ref(DBInstanceClass)
    tags = [ReplicaDBTagFormat]
    condition = 'EnableReadReplica'
    deletion_policy = 'Retain'
