"""Database resources: MyDB."""

from . import *  # noqa: F403


@cloudformation_dataclass
class MyDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
    db_name = 'MyDatabase'
    allocated_storage = '5'
    db_instance_class = 'db.t3.small'
    backup_retention_period = 7
    engine = 'MySQL'
    master_username = 'myName'
    manage_master_user_password = True
    publicly_accessible = False
    storage_encrypted = True
    deletion_policy = 'Snapshot'
