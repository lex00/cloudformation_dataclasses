"""PropertyTypes for AWS::DMS::DataProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AssessmentReportType:
    """AssessmentReportType enum values."""

    PDF = "pdf"
    CSV = "csv"


class AuthMechanismValue:
    """AuthMechanismValue enum values."""

    DEFAULT = "default"
    MONGODB_CR = "mongodb_cr"
    SCRAM_SHA_1 = "scram_sha_1"


class AuthTypeValue:
    """AuthTypeValue enum values."""

    NO = "no"
    PASSWORD = "password"


class CannedAclForObjectsValue:
    """CannedAclForObjectsValue enum values."""

    NONE = "none"
    PRIVATE = "private"
    PUBLIC_READ = "public-read"
    PUBLIC_READ_WRITE = "public-read-write"
    AUTHENTICATED_READ = "authenticated-read"
    AWS_EXEC_READ = "aws-exec-read"
    BUCKET_OWNER_READ = "bucket-owner-read"
    BUCKET_OWNER_FULL_CONTROL = "bucket-owner-full-control"


class CharLengthSemantics:
    """CharLengthSemantics enum values."""

    DEFAULT = "default"
    CHAR = "char"
    BYTE = "byte"


class CollectorStatus:
    """CollectorStatus enum values."""

    UNREGISTERED = "UNREGISTERED"
    ACTIVE = "ACTIVE"


class CompressionTypeValue:
    """CompressionTypeValue enum values."""

    NONE = "none"
    GZIP = "gzip"


class DataFormatValue:
    """DataFormatValue enum values."""

    CSV = "csv"
    PARQUET = "parquet"


class DatabaseMode:
    """DatabaseMode enum values."""

    DEFAULT = "default"
    BABELFISH = "babelfish"


class DatePartitionDelimiterValue:
    """DatePartitionDelimiterValue enum values."""

    SLASH = "SLASH"
    UNDERSCORE = "UNDERSCORE"
    DASH = "DASH"
    NONE = "NONE"


class DatePartitionSequenceValue:
    """DatePartitionSequenceValue enum values."""

    YYYYMMDD = "YYYYMMDD"
    YYYYMMDDHH = "YYYYMMDDHH"
    YYYYMM = "YYYYMM"
    MMYYYYDD = "MMYYYYDD"
    DDMMYYYY = "DDMMYYYY"


class DmsSslModeValue:
    """DmsSslModeValue enum values."""

    NONE = "none"
    REQUIRE = "require"
    VERIFY_CA = "verify-ca"
    VERIFY_FULL = "verify-full"


class EncodingTypeValue:
    """EncodingTypeValue enum values."""

    PLAIN = "plain"
    PLAIN_DICTIONARY = "plain-dictionary"
    RLE_DICTIONARY = "rle-dictionary"


class EncryptionModeValue:
    """EncryptionModeValue enum values."""

    SSE_S3 = "sse-s3"
    SSE_KMS = "sse-kms"


class EndpointSettingTypeValue:
    """EndpointSettingTypeValue enum values."""

    STRING = "string"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    ENUM = "enum"


class KafkaSaslMechanism:
    """KafkaSaslMechanism enum values."""

    SCRAM_SHA_512 = "scram-sha-512"
    PLAIN = "plain"


class KafkaSecurityProtocol:
    """KafkaSecurityProtocol enum values."""

    PLAINTEXT = "plaintext"
    SSL_AUTHENTICATION = "ssl-authentication"
    SSL_ENCRYPTION = "ssl-encryption"
    SASL_SSL = "sasl-ssl"


class KafkaSslEndpointIdentificationAlgorithm:
    """KafkaSslEndpointIdentificationAlgorithm enum values."""

    NONE = "none"
    HTTPS = "https"


class LongVarcharMappingType:
    """LongVarcharMappingType enum values."""

    WSTRING = "wstring"
    CLOB = "clob"
    NCLOB = "nclob"


class MessageFormatValue:
    """MessageFormatValue enum values."""

    JSON = "json"
    JSON_UNFORMATTED = "json-unformatted"


class MigrationTypeValue:
    """MigrationTypeValue enum values."""

    FULL_LOAD = "full-load"
    CDC = "cdc"
    FULL_LOAD_AND_CDC = "full-load-and-cdc"


class MySQLAuthenticationMethod:
    """MySQLAuthenticationMethod enum values."""

    PASSWORD = "password"
    IAM = "iam"


class NestingLevelValue:
    """NestingLevelValue enum values."""

    NONE = "none"
    ONE = "one"


class OracleAuthenticationMethod:
    """OracleAuthenticationMethod enum values."""

    PASSWORD = "password"
    KERBEROS = "kerberos"


class OriginTypeValue:
    """OriginTypeValue enum values."""

    SOURCE = "SOURCE"
    TARGET = "TARGET"


class ParquetVersionValue:
    """ParquetVersionValue enum values."""

    PARQUET_1_0 = "parquet-1-0"
    PARQUET_2_0 = "parquet-2-0"


class PluginNameValue:
    """PluginNameValue enum values."""

    NO_PREFERENCE = "no-preference"
    TEST_DECODING = "test-decoding"
    PGLOGICAL = "pglogical"


class PostgreSQLAuthenticationMethod:
    """PostgreSQLAuthenticationMethod enum values."""

    PASSWORD = "password"
    IAM = "iam"


class RedisAuthTypeValue:
    """RedisAuthTypeValue enum values."""

    NONE = "none"
    AUTH_ROLE = "auth-role"
    AUTH_TOKEN = "auth-token"


class RefreshSchemasStatusTypeValue:
    """RefreshSchemasStatusTypeValue enum values."""

    SUCCESSFUL = "successful"
    FAILED = "failed"
    REFRESHING = "refreshing"


class ReleaseStatusValues:
    """ReleaseStatusValues enum values."""

    BETA = "beta"
    PROD = "prod"


class ReloadOptionValue:
    """ReloadOptionValue enum values."""

    DATA_RELOAD = "data-reload"
    VALIDATE_ONLY = "validate-only"


class ReplicationEndpointTypeValue:
    """ReplicationEndpointTypeValue enum values."""

    SOURCE = "source"
    TARGET = "target"


class SafeguardPolicy:
    """SafeguardPolicy enum values."""

    RELY_ON_SQL_SERVER_REPLICATION_AGENT = "rely-on-sql-server-replication-agent"
    EXCLUSIVE_AUTOMATIC_TRUNCATION = "exclusive-automatic-truncation"
    SHARED_AUTOMATIC_TRUNCATION = "shared-automatic-truncation"


class SourceType:
    """SourceType enum values."""

    REPLICATION_INSTANCE = "replication-instance"


class SqlServerAuthenticationMethod:
    """SqlServerAuthenticationMethod enum values."""

    PASSWORD = "password"
    KERBEROS = "kerberos"


class SslSecurityProtocolValue:
    """SslSecurityProtocolValue enum values."""

    PLAINTEXT = "plaintext"
    SSL_ENCRYPTION = "ssl-encryption"


class StartReplicationMigrationTypeValue:
    """StartReplicationMigrationTypeValue enum values."""

    RELOAD_TARGET = "reload-target"
    RESUME_PROCESSING = "resume-processing"
    START_REPLICATION = "start-replication"


class StartReplicationTaskTypeValue:
    """StartReplicationTaskTypeValue enum values."""

    START_REPLICATION = "start-replication"
    RESUME_PROCESSING = "resume-processing"
    RELOAD_TARGET = "reload-target"


class TablePreparationMode:
    """TablePreparationMode enum values."""

    DROP_TABLES_ON_TARGET = "drop-tables-on-target"
    TRUNCATE = "truncate"
    DO_NOTHING = "do-nothing"


class TargetDbType:
    """TargetDbType enum values."""

    SPECIFIC_DATABASE = "specific-database"
    MULTIPLE_DATABASES = "multiple-databases"


class TlogAccessMode:
    """TlogAccessMode enum values."""

    BACKUPONLY = "BackupOnly"
    PREFERBACKUP = "PreferBackup"
    PREFERTLOG = "PreferTlog"
    TLOGONLY = "TlogOnly"


class VersionStatus:
    """VersionStatus enum values."""

    UP_TO_DATE = "UP_TO_DATE"
    OUTDATED = "OUTDATED"
    UNSUPPORTED = "UNSUPPORTED"


@dataclass
class DocDbSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IbmDb2LuwSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IbmDb2zOsSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MariaDbSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MicrosoftSqlServerSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MongoDbSettings(PropertyType):
    AUTH_SOURCE = "AuthSource"
    AUTH_MECHANISM = "AuthMechanism"
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    AUTH_TYPE = "AuthType"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_source": "AuthSource",
        "auth_mechanism": "AuthMechanism",
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "auth_type": "AuthType",
        "certificate_arn": "CertificateArn",
    }

    auth_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_mechanism: Optional[Union[str, AuthMechanismValue, Ref, GetAtt, Sub]] = None
    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, AuthTypeValue, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MySqlSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OracleSettings(PropertyType):
    SECRETS_MANAGER_ORACLE_ASM_ACCESS_ROLE_ARN = "SecretsManagerOracleAsmAccessRoleArn"
    SECRETS_MANAGER_ORACLE_ASM_SECRET_ID = "SecretsManagerOracleAsmSecretId"
    SSL_MODE = "SslMode"
    SECRETS_MANAGER_SECURITY_DB_ENCRYPTION_SECRET_ID = "SecretsManagerSecurityDbEncryptionSecretId"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    ASM_SERVER = "AsmServer"
    CERTIFICATE_ARN = "CertificateArn"
    SECRETS_MANAGER_SECURITY_DB_ENCRYPTION_ACCESS_ROLE_ARN = "SecretsManagerSecurityDbEncryptionAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager_oracle_asm_access_role_arn": "SecretsManagerOracleAsmAccessRoleArn",
        "secrets_manager_oracle_asm_secret_id": "SecretsManagerOracleAsmSecretId",
        "ssl_mode": "SslMode",
        "secrets_manager_security_db_encryption_secret_id": "SecretsManagerSecurityDbEncryptionSecretId",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "asm_server": "AsmServer",
        "certificate_arn": "CertificateArn",
        "secrets_manager_security_db_encryption_access_role_arn": "SecretsManagerSecurityDbEncryptionAccessRoleArn",
    }

    secrets_manager_oracle_asm_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_oracle_asm_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_security_db_encryption_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    asm_server: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_security_db_encryption_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PostgreSqlSettings(PropertyType):
    SSL_MODE = "SslMode"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_mode": "SslMode",
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
        "certificate_arn": "CertificateArn",
    }

    ssl_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftSettings(PropertyType):
    SERVER_NAME = "ServerName"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_name": "ServerName",
        "port": "Port",
        "database_name": "DatabaseName",
    }

    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Settings(PropertyType):
    MARIA_DB_SETTINGS = "MariaDbSettings"
    ORACLE_SETTINGS = "OracleSettings"
    MICROSOFT_SQL_SERVER_SETTINGS = "MicrosoftSqlServerSettings"
    REDSHIFT_SETTINGS = "RedshiftSettings"
    IBM_DB2Z_OS_SETTINGS = "IbmDb2zOsSettings"
    MY_SQL_SETTINGS = "MySqlSettings"
    IBM_DB2_LUW_SETTINGS = "IbmDb2LuwSettings"
    DOC_DB_SETTINGS = "DocDbSettings"
    POSTGRE_SQL_SETTINGS = "PostgreSqlSettings"
    MONGO_DB_SETTINGS = "MongoDbSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maria_db_settings": "MariaDbSettings",
        "oracle_settings": "OracleSettings",
        "microsoft_sql_server_settings": "MicrosoftSqlServerSettings",
        "redshift_settings": "RedshiftSettings",
        "ibm_db2z_os_settings": "IbmDb2zOsSettings",
        "my_sql_settings": "MySqlSettings",
        "ibm_db2_luw_settings": "IbmDb2LuwSettings",
        "doc_db_settings": "DocDbSettings",
        "postgre_sql_settings": "PostgreSqlSettings",
        "mongo_db_settings": "MongoDbSettings",
    }

    maria_db_settings: Optional[MariaDbSettings] = None
    oracle_settings: Optional[OracleSettings] = None
    microsoft_sql_server_settings: Optional[MicrosoftSqlServerSettings] = None
    redshift_settings: Optional[RedshiftSettings] = None
    ibm_db2z_os_settings: Optional[IbmDb2zOsSettings] = None
    my_sql_settings: Optional[MySqlSettings] = None
    ibm_db2_luw_settings: Optional[IbmDb2LuwSettings] = None
    doc_db_settings: Optional[DocDbSettings] = None
    postgre_sql_settings: Optional[PostgreSqlSettings] = None
    mongo_db_settings: Optional[MongoDbSettings] = None

