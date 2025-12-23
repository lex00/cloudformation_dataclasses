"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBEC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Open database for access'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '3306',
        'ToPort': '3306',
        'SourceSecurityGroupName': ref(EC2SecurityGroup),
    }]
    condition = 'IsEC2VPC'


@cloudformation_dataclass
class DBCredentialGenerateSecretString:
    resource: secretsmanager.secret.GenerateSecretString
    password_length = 16
    exclude_characters = '"@/\\'
    require_each_included_type = True


@cloudformation_dataclass
class DBCredential:
    """AWS::SecretsManager::Secret resource."""

    resource: secretsmanager.Secret
    generate_secret_string = DBCredentialGenerateSecretString


@cloudformation_dataclass
class MainDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
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
    tags = [{
        'Key': 'Name',
        'Value': 'Master Database',
    }]
    vpc_security_groups = If("IsEC2VPC", [get_att(DBEC2SecurityGroup, "GroupId")], AWS_NO_VALUE)
    depends_on = ["DBCredential"]
    deletion_policy = 'Snapshot'


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
