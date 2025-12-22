from __future__ import annotations

"""MainDB - AWS::RDS::DBInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MainDBTagFormat:
    resource: TagFormat
    key = 'Name'
    value = 'Master Database'


@cloudformation_dataclass
class MainDB:
    """AWS::RDS::DBInstance resource."""

    resource: DBInstance
    db_name = ref(DBName)
    allocated_storage = ref(DBAllocatedStorage)
    backup_retention_period = 7
    db_instance_class = ref(DBInstanceClass)
    engine = 'MySQL'
    master_username = ref(DBUser)
    master_user_password = Sub('{{resolve:secretsmanager:${DBCredential}}}')
    multi_az = ref(MultiAZ)
    publicly_accessible = False
    storage_encrypted = True
    tags = [MainDBTagFormat]
    vpc_security_groups = If("IsEC2VPC", [get_att(DBEC2SecurityGroup, "GroupId")], AWS_NO_VALUE)
    depends_on = ["DBCredential"]
    deletion_policy = 'Snapshot'
