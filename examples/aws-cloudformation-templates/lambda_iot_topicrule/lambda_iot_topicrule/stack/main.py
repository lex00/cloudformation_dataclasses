"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBCredentialGenerateSecretString:
    resource: secretsmanager.secret.GenerateSecretString
    password_length = 16
    exclude_characters = '"@/\\'
    require_each_included_type = True


@cloudformation_dataclass
class DBCredential:
    """AWS::SecretsManager::Secret resource."""

    resource: Secret
    generate_secret_string = DBCredentialGenerateSecretString


@cloudformation_dataclass
class myDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
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
