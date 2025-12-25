"""RDS resources - PostgreSQL database with Secrets Manager."""

from .. import *  # noqa: F403, F401


# =============================================================================
# Security Group
# =============================================================================


@cloudformation_dataclass
class DbSecurityGroupIngress:
    """Allow PostgreSQL from within VPC."""

    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 5432
    to_port = 5432
    cidr_ip = ref(VpcCidrParam)


@cloudformation_dataclass
class DbSecurityGroup:
    """Security group for RDS PostgreSQL."""

    resource: ec2.SecurityGroup
    group_description = "Security group for RDS PostgreSQL"
    vpc_id = ref(VpcIdParam)
    security_group_ingress = [DbSecurityGroupIngress]


# =============================================================================
# Subnet Group
# =============================================================================


@cloudformation_dataclass
class DbSubnetGroup:
    """DB subnet group for RDS."""

    resource: rds.DBSubnetGroup
    db_subnet_group_description = "Subnet group for RDS PostgreSQL"
    subnet_ids = ref(PrivateSubnetIdsParam)


# =============================================================================
# Secrets Manager
# =============================================================================


@cloudformation_dataclass
class DbSecretGenerateString:
    """Password generation configuration."""

    resource: secret.GenerateSecretString
    secret_string_template = '{"username": "postgres"}'
    generate_string_key = "password"
    password_length = 32
    exclude_punctuation = True


@cloudformation_dataclass
class DbSecret:
    """Secrets Manager secret for RDS master password."""

    resource: secretsmanager.Secret
    description = "RDS PostgreSQL master user password"
    generate_secret_string = DbSecretGenerateString


# =============================================================================
# RDS Instance
# =============================================================================


@cloudformation_dataclass
class PostgresInstance:
    """RDS PostgreSQL instance."""

    resource: rds.DBInstance
    engine = "postgres"
    engine_version = "15.4"
    db_instance_class = "db.t3.micro"
    allocated_storage = "20"
    db_name = ref(DatabaseNameParam)
    master_username = Sub("{{resolve:secretsmanager:${DbSecret}:SecretString:username}}")
    master_user_password = Sub(
        "{{resolve:secretsmanager:${DbSecret}:SecretString:password}}"
    )
    db_subnet_group_name = ref(DbSubnetGroup)
    vpc_security_groups = [ref(DbSecurityGroup)]
    publicly_accessible = False
    storage_encrypted = True
    deletion_protection = False
    backup_retention_period = 7


# =============================================================================
# Secret Attachment
# =============================================================================


@cloudformation_dataclass
class SecretTargetAttachment:
    """Attach the secret to the RDS instance for rotation."""

    resource: secretsmanager.SecretTargetAttachment
    secret_id = ref(DbSecret)
    target_id = ref(PostgresInstance)
    target_type = "AWS::RDS::DBInstance"
