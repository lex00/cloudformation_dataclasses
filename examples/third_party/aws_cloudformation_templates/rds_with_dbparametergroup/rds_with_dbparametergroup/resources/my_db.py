"""MyDB - AWS::RDS::DBInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
    db_name = ref(DBName)
    allocated_storage = '5'
    db_instance_class = 'db.t3.small'
    backup_retention_period = 7
    engine = 'MySQL'
    engine_version = '8.0.36'
    master_username = ref(DBUser)
    manage_master_user_password = True
    db_parameter_group_name = ref(MyRDSParamGroup)
    publicly_accessible = False
    storage_encrypted = True
    deletion_policy = 'Snapshot'
