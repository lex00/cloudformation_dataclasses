"""myDB - AWS::RDS::DBInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myDB:
    """AWS::RDS::DBInstance resource."""

    resource: DBInstance
    allocated_storage = '100'
    db_instance_class = 'db.t3.small'
    backup_retention_period = 7
    engine = 'MySQL'
    iops = '1000'
    master_username = ref(DBUser)
    master_user_password = Sub('{{resolve:secretsmanager:${DBCredential}}}')
    publicly_accessible = False
    storage_encrypted = True
    depends_on = ["DBCredential"]
