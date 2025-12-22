"""PropertyTypes for AWS::DMS::Endpoint."""

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
    DOCS_TO_INVESTIGATE = "DocsToInvestigate"
    EXTRACT_DOC_ID = "ExtractDocId"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    NESTING_LEVEL = "NestingLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "docs_to_investigate": "DocsToInvestigate",
        "extract_doc_id": "ExtractDocId",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "nesting_level": "NestingLevel",
    }

    docs_to_investigate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    extract_doc_id: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nesting_level: Optional[Union[str, NestingLevelValue, Ref, GetAtt, Sub]] = None


@dataclass
class DynamoDbSettings(PropertyType):
    SERVICE_ACCESS_ROLE_ARN = "ServiceAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_access_role_arn": "ServiceAccessRoleArn",
    }

    service_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticsearchSettings(PropertyType):
    ENDPOINT_URI = "EndpointUri"
    FULL_LOAD_ERROR_PERCENTAGE = "FullLoadErrorPercentage"
    ERROR_RETRY_DURATION = "ErrorRetryDuration"
    SERVICE_ACCESS_ROLE_ARN = "ServiceAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_uri": "EndpointUri",
        "full_load_error_percentage": "FullLoadErrorPercentage",
        "error_retry_duration": "ErrorRetryDuration",
        "service_access_role_arn": "ServiceAccessRoleArn",
    }

    endpoint_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    full_load_error_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    error_retry_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    service_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GcpMySQLSettings(PropertyType):
    AFTER_CONNECT_SCRIPT = "AfterConnectScript"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    CLEAN_SOURCE_METADATA_ON_MISMATCH = "CleanSourceMetadataOnMismatch"
    SERVER_TIMEZONE = "ServerTimezone"
    EVENTS_POLL_INTERVAL = "EventsPollInterval"
    PARALLEL_LOAD_THREADS = "ParallelLoadThreads"
    USERNAME = "Username"
    MAX_FILE_SIZE = "MaxFileSize"
    SERVER_NAME = "ServerName"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "after_connect_script": "AfterConnectScript",
        "port": "Port",
        "database_name": "DatabaseName",
        "clean_source_metadata_on_mismatch": "CleanSourceMetadataOnMismatch",
        "server_timezone": "ServerTimezone",
        "events_poll_interval": "EventsPollInterval",
        "parallel_load_threads": "ParallelLoadThreads",
        "username": "Username",
        "max_file_size": "MaxFileSize",
        "server_name": "ServerName",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "password": "Password",
    }

    after_connect_script: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    clean_source_metadata_on_mismatch: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    server_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    events_poll_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    parallel_load_threads: Optional[Union[int, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IbmDb2Settings(PropertyType):
    LOAD_TIMEOUT = "LoadTimeout"
    SET_DATA_CAPTURE_CHANGES = "SetDataCaptureChanges"
    MAX_FILE_SIZE = "MaxFileSize"
    KEEP_CSV_FILES = "KeepCsvFiles"
    CURRENT_LSN = "CurrentLsn"
    MAX_K_BYTES_PER_READ = "MaxKBytesPerRead"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    WRITE_BUFFER_SIZE = "WriteBufferSize"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "load_timeout": "LoadTimeout",
        "set_data_capture_changes": "SetDataCaptureChanges",
        "max_file_size": "MaxFileSize",
        "keep_csv_files": "KeepCsvFiles",
        "current_lsn": "CurrentLsn",
        "max_k_bytes_per_read": "MaxKBytesPerRead",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "write_buffer_size": "WriteBufferSize",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
    }

    load_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    set_data_capture_changes: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    keep_csv_files: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    current_lsn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_k_bytes_per_read: Optional[Union[int, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    write_buffer_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KafkaSettings(PropertyType):
    BROKER = "Broker"
    SASL_PASSWORD = "SaslPassword"
    MESSAGE_FORMAT = "MessageFormat"
    SSL_CLIENT_CERTIFICATE_ARN = "SslClientCertificateArn"
    INCLUDE_TRANSACTION_DETAILS = "IncludeTransactionDetails"
    SECURITY_PROTOCOL = "SecurityProtocol"
    INCLUDE_TABLE_ALTER_OPERATIONS = "IncludeTableAlterOperations"
    SSL_CA_CERTIFICATE_ARN = "SslCaCertificateArn"
    INCLUDE_CONTROL_DETAILS = "IncludeControlDetails"
    INCLUDE_PARTITION_VALUE = "IncludePartitionValue"
    NO_HEX_PREFIX = "NoHexPrefix"
    SSL_CLIENT_KEY_ARN = "SslClientKeyArn"
    SSL_CLIENT_KEY_PASSWORD = "SslClientKeyPassword"
    SASL_USER_NAME = "SaslUserName"
    MESSAGE_MAX_BYTES = "MessageMaxBytes"
    TOPIC = "Topic"
    PARTITION_INCLUDE_SCHEMA_TABLE = "PartitionIncludeSchemaTable"
    INCLUDE_NULL_AND_EMPTY = "IncludeNullAndEmpty"

    _property_mappings: ClassVar[dict[str, str]] = {
        "broker": "Broker",
        "sasl_password": "SaslPassword",
        "message_format": "MessageFormat",
        "ssl_client_certificate_arn": "SslClientCertificateArn",
        "include_transaction_details": "IncludeTransactionDetails",
        "security_protocol": "SecurityProtocol",
        "include_table_alter_operations": "IncludeTableAlterOperations",
        "ssl_ca_certificate_arn": "SslCaCertificateArn",
        "include_control_details": "IncludeControlDetails",
        "include_partition_value": "IncludePartitionValue",
        "no_hex_prefix": "NoHexPrefix",
        "ssl_client_key_arn": "SslClientKeyArn",
        "ssl_client_key_password": "SslClientKeyPassword",
        "sasl_user_name": "SaslUserName",
        "message_max_bytes": "MessageMaxBytes",
        "topic": "Topic",
        "partition_include_schema_table": "PartitionIncludeSchemaTable",
        "include_null_and_empty": "IncludeNullAndEmpty",
    }

    broker: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sasl_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_format: Optional[Union[str, MessageFormatValue, Ref, GetAtt, Sub]] = None
    ssl_client_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_transaction_details: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_protocol: Optional[Union[str, KafkaSecurityProtocol, Ref, GetAtt, Sub]] = None
    include_table_alter_operations: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ssl_ca_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_control_details: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_partition_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    no_hex_prefix: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ssl_client_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssl_client_key_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sasl_user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_max_bytes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    partition_include_schema_table: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_null_and_empty: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisSettings(PropertyType):
    MESSAGE_FORMAT = "MessageFormat"
    INCLUDE_TRANSACTION_DETAILS = "IncludeTransactionDetails"
    INCLUDE_TABLE_ALTER_OPERATIONS = "IncludeTableAlterOperations"
    INCLUDE_CONTROL_DETAILS = "IncludeControlDetails"
    INCLUDE_PARTITION_VALUE = "IncludePartitionValue"
    STREAM_ARN = "StreamArn"
    SERVICE_ACCESS_ROLE_ARN = "ServiceAccessRoleArn"
    NO_HEX_PREFIX = "NoHexPrefix"
    PARTITION_INCLUDE_SCHEMA_TABLE = "PartitionIncludeSchemaTable"
    INCLUDE_NULL_AND_EMPTY = "IncludeNullAndEmpty"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_format": "MessageFormat",
        "include_transaction_details": "IncludeTransactionDetails",
        "include_table_alter_operations": "IncludeTableAlterOperations",
        "include_control_details": "IncludeControlDetails",
        "include_partition_value": "IncludePartitionValue",
        "stream_arn": "StreamArn",
        "service_access_role_arn": "ServiceAccessRoleArn",
        "no_hex_prefix": "NoHexPrefix",
        "partition_include_schema_table": "PartitionIncludeSchemaTable",
        "include_null_and_empty": "IncludeNullAndEmpty",
    }

    message_format: Optional[Union[str, MessageFormatValue, Ref, GetAtt, Sub]] = None
    include_transaction_details: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_table_alter_operations: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_control_details: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_partition_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    no_hex_prefix: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    partition_include_schema_table: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_null_and_empty: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MicrosoftSqlServerSettings(PropertyType):
    READ_BACKUP_ONLY = "ReadBackupOnly"
    TLOG_ACCESS_MODE = "TlogAccessMode"
    BCP_PACKET_SIZE = "BcpPacketSize"
    PORT = "Port"
    SAFEGUARD_POLICY = "SafeguardPolicy"
    USE_THIRD_PARTY_BACKUP_DEVICE = "UseThirdPartyBackupDevice"
    DATABASE_NAME = "DatabaseName"
    USE_BCP_FULL_LOAD = "UseBcpFullLoad"
    USERNAME = "Username"
    QUERY_SINGLE_ALWAYS_ON_NODE = "QuerySingleAlwaysOnNode"
    SERVER_NAME = "ServerName"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    CONTROL_TABLES_FILE_GROUP = "ControlTablesFileGroup"
    FORCE_LOB_LOOKUP = "ForceLobLookup"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    TRIM_SPACE_IN_CHAR = "TrimSpaceInChar"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_backup_only": "ReadBackupOnly",
        "tlog_access_mode": "TlogAccessMode",
        "bcp_packet_size": "BcpPacketSize",
        "port": "Port",
        "safeguard_policy": "SafeguardPolicy",
        "use_third_party_backup_device": "UseThirdPartyBackupDevice",
        "database_name": "DatabaseName",
        "use_bcp_full_load": "UseBcpFullLoad",
        "username": "Username",
        "query_single_always_on_node": "QuerySingleAlwaysOnNode",
        "server_name": "ServerName",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "control_tables_file_group": "ControlTablesFileGroup",
        "force_lob_lookup": "ForceLobLookup",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "trim_space_in_char": "TrimSpaceInChar",
        "password": "Password",
    }

    read_backup_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tlog_access_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bcp_packet_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    safeguard_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_third_party_backup_device: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_bcp_full_load: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_single_always_on_node: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    control_tables_file_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    force_lob_lookup: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trim_space_in_char: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MongoDbSettings(PropertyType):
    PORT = "Port"
    EXTRACT_DOC_ID = "ExtractDocId"
    DATABASE_NAME = "DatabaseName"
    AUTH_SOURCE = "AuthSource"
    AUTH_MECHANISM = "AuthMechanism"
    USERNAME = "Username"
    DOCS_TO_INVESTIGATE = "DocsToInvestigate"
    SERVER_NAME = "ServerName"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    AUTH_TYPE = "AuthType"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    PASSWORD = "Password"
    NESTING_LEVEL = "NestingLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "extract_doc_id": "ExtractDocId",
        "database_name": "DatabaseName",
        "auth_source": "AuthSource",
        "auth_mechanism": "AuthMechanism",
        "username": "Username",
        "docs_to_investigate": "DocsToInvestigate",
        "server_name": "ServerName",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "auth_type": "AuthType",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "password": "Password",
        "nesting_level": "NestingLevel",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    extract_doc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_mechanism: Optional[Union[str, AuthMechanismValue, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    docs_to_investigate: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, AuthTypeValue, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nesting_level: Optional[Union[str, NestingLevelValue, Ref, GetAtt, Sub]] = None


@dataclass
class MySqlSettings(PropertyType):
    SERVER_TIMEZONE = "ServerTimezone"
    EVENTS_POLL_INTERVAL = "EventsPollInterval"
    PARALLEL_LOAD_THREADS = "ParallelLoadThreads"
    AFTER_CONNECT_SCRIPT = "AfterConnectScript"
    MAX_FILE_SIZE = "MaxFileSize"
    TARGET_DB_TYPE = "TargetDbType"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    CLEAN_SOURCE_METADATA_ON_MISMATCH = "CleanSourceMetadataOnMismatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_timezone": "ServerTimezone",
        "events_poll_interval": "EventsPollInterval",
        "parallel_load_threads": "ParallelLoadThreads",
        "after_connect_script": "AfterConnectScript",
        "max_file_size": "MaxFileSize",
        "target_db_type": "TargetDbType",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "clean_source_metadata_on_mismatch": "CleanSourceMetadataOnMismatch",
    }

    server_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    events_poll_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    parallel_load_threads: Optional[Union[int, Ref, GetAtt, Sub]] = None
    after_connect_script: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_db_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    clean_source_metadata_on_mismatch: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class NeptuneSettings(PropertyType):
    MAX_RETRY_COUNT = "MaxRetryCount"
    MAX_FILE_SIZE = "MaxFileSize"
    S3_BUCKET_FOLDER = "S3BucketFolder"
    ERROR_RETRY_DURATION = "ErrorRetryDuration"
    IAM_AUTH_ENABLED = "IamAuthEnabled"
    S3_BUCKET_NAME = "S3BucketName"
    SERVICE_ACCESS_ROLE_ARN = "ServiceAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_retry_count": "MaxRetryCount",
        "max_file_size": "MaxFileSize",
        "s3_bucket_folder": "S3BucketFolder",
        "error_retry_duration": "ErrorRetryDuration",
        "iam_auth_enabled": "IamAuthEnabled",
        "s3_bucket_name": "S3BucketName",
        "service_access_role_arn": "ServiceAccessRoleArn",
    }

    max_retry_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    s3_bucket_folder: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_retry_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iam_auth_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OracleSettings(PropertyType):
    ASM_PASSWORD = "AsmPassword"
    DIRECT_PATH_PARALLEL_LOAD = "DirectPathParallelLoad"
    ADDITIONAL_ARCHIVED_LOG_DEST_ID = "AdditionalArchivedLogDestId"
    SPATIAL_DATA_OPTION_TO_GEO_JSON_FUNCTION_NAME = "SpatialDataOptionToGeoJsonFunctionName"
    REPLACE_PATH_PREFIX = "ReplacePathPrefix"
    FAIL_TASKS_ON_LOB_TRUNCATION = "FailTasksOnLobTruncation"
    ASM_SERVER = "AsmServer"
    SECRETS_MANAGER_ORACLE_ASM_ACCESS_ROLE_ARN = "SecretsManagerOracleAsmAccessRoleArn"
    ORACLE_PATH_PREFIX = "OraclePathPrefix"
    READ_AHEAD_BLOCKS = "ReadAheadBlocks"
    STANDBY_DELAY_TIME = "StandbyDelayTime"
    ALLOW_SELECT_NESTED_TABLES = "AllowSelectNestedTables"
    ADD_SUPPLEMENTAL_LOGGING = "AddSupplementalLogging"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    USE_B_FILE = "UseBFile"
    ENABLE_HOMOGENOUS_TABLESPACE = "EnableHomogenousTablespace"
    ASM_USER = "AsmUser"
    USE_DIRECT_PATH_FULL_LOAD = "UseDirectPathFullLoad"
    SECURITY_DB_ENCRYPTION = "SecurityDbEncryption"
    PARALLEL_ASM_READ_THREADS = "ParallelAsmReadThreads"
    ARCHIVED_LOG_DEST_ID = "ArchivedLogDestId"
    USE_PATH_PREFIX = "UsePathPrefix"
    USE_LOGMINER_READER = "UseLogminerReader"
    SECURITY_DB_ENCRYPTION_NAME = "SecurityDbEncryptionName"
    DIRECT_PATH_NO_LOG = "DirectPathNoLog"
    SECRETS_MANAGER_ORACLE_ASM_SECRET_ID = "SecretsManagerOracleAsmSecretId"
    CHAR_LENGTH_SEMANTICS = "CharLengthSemantics"
    NUMBER_DATATYPE_SCALE = "NumberDatatypeScale"
    READ_TABLE_SPACE_NAME = "ReadTableSpaceName"
    ACCESS_ALTERNATE_DIRECTLY = "AccessAlternateDirectly"
    USE_ALTERNATE_FOLDER_FOR_ONLINE = "UseAlternateFolderForOnline"
    ARCHIVED_LOGS_ONLY = "ArchivedLogsOnly"
    EXTRA_ARCHIVED_LOG_DEST_IDS = "ExtraArchivedLogDestIds"
    RETRY_INTERVAL = "RetryInterval"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "asm_password": "AsmPassword",
        "direct_path_parallel_load": "DirectPathParallelLoad",
        "additional_archived_log_dest_id": "AdditionalArchivedLogDestId",
        "spatial_data_option_to_geo_json_function_name": "SpatialDataOptionToGeoJsonFunctionName",
        "replace_path_prefix": "ReplacePathPrefix",
        "fail_tasks_on_lob_truncation": "FailTasksOnLobTruncation",
        "asm_server": "AsmServer",
        "secrets_manager_oracle_asm_access_role_arn": "SecretsManagerOracleAsmAccessRoleArn",
        "oracle_path_prefix": "OraclePathPrefix",
        "read_ahead_blocks": "ReadAheadBlocks",
        "standby_delay_time": "StandbyDelayTime",
        "allow_select_nested_tables": "AllowSelectNestedTables",
        "add_supplemental_logging": "AddSupplementalLogging",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "use_b_file": "UseBFile",
        "enable_homogenous_tablespace": "EnableHomogenousTablespace",
        "asm_user": "AsmUser",
        "use_direct_path_full_load": "UseDirectPathFullLoad",
        "security_db_encryption": "SecurityDbEncryption",
        "parallel_asm_read_threads": "ParallelAsmReadThreads",
        "archived_log_dest_id": "ArchivedLogDestId",
        "use_path_prefix": "UsePathPrefix",
        "use_logminer_reader": "UseLogminerReader",
        "security_db_encryption_name": "SecurityDbEncryptionName",
        "direct_path_no_log": "DirectPathNoLog",
        "secrets_manager_oracle_asm_secret_id": "SecretsManagerOracleAsmSecretId",
        "char_length_semantics": "CharLengthSemantics",
        "number_datatype_scale": "NumberDatatypeScale",
        "read_table_space_name": "ReadTableSpaceName",
        "access_alternate_directly": "AccessAlternateDirectly",
        "use_alternate_folder_for_online": "UseAlternateFolderForOnline",
        "archived_logs_only": "ArchivedLogsOnly",
        "extra_archived_log_dest_ids": "ExtraArchivedLogDestIds",
        "retry_interval": "RetryInterval",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
    }

    asm_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    direct_path_parallel_load: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    additional_archived_log_dest_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    spatial_data_option_to_geo_json_function_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replace_path_prefix: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    fail_tasks_on_lob_truncation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    asm_server: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_oracle_asm_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    oracle_path_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    read_ahead_blocks: Optional[Union[int, Ref, GetAtt, Sub]] = None
    standby_delay_time: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allow_select_nested_tables: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    add_supplemental_logging: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_b_file: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enable_homogenous_tablespace: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    asm_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_direct_path_full_load: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_db_encryption: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parallel_asm_read_threads: Optional[Union[int, Ref, GetAtt, Sub]] = None
    archived_log_dest_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    use_path_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_logminer_reader: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_db_encryption_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    direct_path_no_log: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    secrets_manager_oracle_asm_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    char_length_semantics: Optional[Union[str, CharLengthSemantics, Ref, GetAtt, Sub]] = None
    number_datatype_scale: Optional[Union[int, Ref, GetAtt, Sub]] = None
    read_table_space_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    access_alternate_directly: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_alternate_folder_for_online: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    archived_logs_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    extra_archived_log_dest_ids: Optional[Union[list[int], Ref]] = None
    retry_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PostgreSqlSettings(PropertyType):
    PLUGIN_NAME = "PluginName"
    MAP_BOOLEAN_AS_BOOLEAN = "MapBooleanAsBoolean"
    AFTER_CONNECT_SCRIPT = "AfterConnectScript"
    EXECUTE_TIMEOUT = "ExecuteTimeout"
    DDL_ARTIFACTS_SCHEMA = "DdlArtifactsSchema"
    FAIL_TASKS_ON_LOB_TRUNCATION = "FailTasksOnLobTruncation"
    HEARTBEAT_ENABLE = "HeartbeatEnable"
    BABELFISH_DATABASE_NAME = "BabelfishDatabaseName"
    DATABASE_MODE = "DatabaseMode"
    CAPTURE_DDLS = "CaptureDdls"
    MAX_FILE_SIZE = "MaxFileSize"
    HEARTBEAT_FREQUENCY = "HeartbeatFrequency"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    HEARTBEAT_SCHEMA = "HeartbeatSchema"
    SLOT_NAME = "SlotName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "plugin_name": "PluginName",
        "map_boolean_as_boolean": "MapBooleanAsBoolean",
        "after_connect_script": "AfterConnectScript",
        "execute_timeout": "ExecuteTimeout",
        "ddl_artifacts_schema": "DdlArtifactsSchema",
        "fail_tasks_on_lob_truncation": "FailTasksOnLobTruncation",
        "heartbeat_enable": "HeartbeatEnable",
        "babelfish_database_name": "BabelfishDatabaseName",
        "database_mode": "DatabaseMode",
        "capture_ddls": "CaptureDdls",
        "max_file_size": "MaxFileSize",
        "heartbeat_frequency": "HeartbeatFrequency",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "heartbeat_schema": "HeartbeatSchema",
        "slot_name": "SlotName",
    }

    plugin_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    map_boolean_as_boolean: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    after_connect_script: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execute_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ddl_artifacts_schema: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fail_tasks_on_lob_truncation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    heartbeat_enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    babelfish_database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capture_ddls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    heartbeat_frequency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    heartbeat_schema: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedisSettings(PropertyType):
    SSL_SECURITY_PROTOCOL = "SslSecurityProtocol"
    AUTH_USER_NAME = "AuthUserName"
    SERVER_NAME = "ServerName"
    PORT = "Port"
    SSL_CA_CERTIFICATE_ARN = "SslCaCertificateArn"
    AUTH_PASSWORD = "AuthPassword"
    AUTH_TYPE = "AuthType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_security_protocol": "SslSecurityProtocol",
        "auth_user_name": "AuthUserName",
        "server_name": "ServerName",
        "port": "Port",
        "ssl_ca_certificate_arn": "SslCaCertificateArn",
        "auth_password": "AuthPassword",
        "auth_type": "AuthType",
    }

    ssl_security_protocol: Optional[Union[str, SslSecurityProtocolValue, Ref, GetAtt, Sub]] = None
    auth_user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ssl_ca_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, RedisAuthTypeValue, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftSettings(PropertyType):
    CONNECTION_TIMEOUT = "ConnectionTimeout"
    MAP_BOOLEAN_AS_BOOLEAN = "MapBooleanAsBoolean"
    AFTER_CONNECT_SCRIPT = "AfterConnectScript"
    FILE_TRANSFER_UPLOAD_STREAMS = "FileTransferUploadStreams"
    BUCKET_NAME = "BucketName"
    SERVER_SIDE_ENCRYPTION_KMS_KEY_ID = "ServerSideEncryptionKmsKeyId"
    EXPLICIT_IDS = "ExplicitIds"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    TRUNCATE_COLUMNS = "TruncateColumns"
    SERVICE_ACCESS_ROLE_ARN = "ServiceAccessRoleArn"
    REPLACE_CHARS = "ReplaceChars"
    TIME_FORMAT = "TimeFormat"
    BUCKET_FOLDER = "BucketFolder"
    REPLACE_INVALID_CHARS = "ReplaceInvalidChars"
    REMOVE_QUOTES = "RemoveQuotes"
    LOAD_TIMEOUT = "LoadTimeout"
    MAX_FILE_SIZE = "MaxFileSize"
    TRIM_BLANKS = "TrimBlanks"
    DATE_FORMAT = "DateFormat"
    COMP_UPDATE = "CompUpdate"
    ACCEPT_ANY_DATE = "AcceptAnyDate"
    WRITE_BUFFER_SIZE = "WriteBufferSize"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    CASE_SENSITIVE_NAMES = "CaseSensitiveNames"
    EMPTY_AS_NULL = "EmptyAsNull"
    ENCRYPTION_MODE = "EncryptionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_timeout": "ConnectionTimeout",
        "map_boolean_as_boolean": "MapBooleanAsBoolean",
        "after_connect_script": "AfterConnectScript",
        "file_transfer_upload_streams": "FileTransferUploadStreams",
        "bucket_name": "BucketName",
        "server_side_encryption_kms_key_id": "ServerSideEncryptionKmsKeyId",
        "explicit_ids": "ExplicitIds",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "truncate_columns": "TruncateColumns",
        "service_access_role_arn": "ServiceAccessRoleArn",
        "replace_chars": "ReplaceChars",
        "time_format": "TimeFormat",
        "bucket_folder": "BucketFolder",
        "replace_invalid_chars": "ReplaceInvalidChars",
        "remove_quotes": "RemoveQuotes",
        "load_timeout": "LoadTimeout",
        "max_file_size": "MaxFileSize",
        "trim_blanks": "TrimBlanks",
        "date_format": "DateFormat",
        "comp_update": "CompUpdate",
        "accept_any_date": "AcceptAnyDate",
        "write_buffer_size": "WriteBufferSize",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "case_sensitive_names": "CaseSensitiveNames",
        "empty_as_null": "EmptyAsNull",
        "encryption_mode": "EncryptionMode",
    }

    connection_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    map_boolean_as_boolean: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    after_connect_script: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_transfer_upload_streams: Optional[Union[int, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_side_encryption_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    explicit_ids: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    truncate_columns: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    service_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replace_chars: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_folder: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replace_invalid_chars: Optional[Union[str, Ref, GetAtt, Sub]] = None
    remove_quotes: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    load_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    trim_blanks: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    date_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    comp_update: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    accept_any_date: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    write_buffer_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    case_sensitive_names: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    empty_as_null: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    encryption_mode: Optional[Union[str, EncryptionModeValue, Ref, GetAtt, Sub]] = None


@dataclass
class S3Settings(PropertyType):
    TIMESTAMP_COLUMN_NAME = "TimestampColumnName"
    ENABLE_STATISTICS = "EnableStatistics"
    DATE_PARTITION_SEQUENCE = "DatePartitionSequence"
    CSV_NULL_VALUE = "CsvNullValue"
    INCLUDE_OP_FOR_FULL_LOAD = "IncludeOpForFullLoad"
    CDC_INSERTS_AND_UPDATES = "CdcInsertsAndUpdates"
    BUCKET_NAME = "BucketName"
    SERVER_SIDE_ENCRYPTION_KMS_KEY_ID = "ServerSideEncryptionKmsKeyId"
    USE_TASK_START_TIME_FOR_FULL_LOAD_TIMESTAMP = "UseTaskStartTimeForFullLoadTimestamp"
    GLUE_CATALOG_GENERATION = "GlueCatalogGeneration"
    DATA_FORMAT = "DataFormat"
    CSV_DELIMITER = "CsvDelimiter"
    ADD_TRAILING_PADDING_CHARACTER = "AddTrailingPaddingCharacter"
    IGNORE_HEADER_ROWS = "IgnoreHeaderRows"
    CANNED_ACL_FOR_OBJECTS = "CannedAclForObjects"
    RFC4180 = "Rfc4180"
    SERVICE_ACCESS_ROLE_ARN = "ServiceAccessRoleArn"
    PARQUET_TIMESTAMP_IN_MILLISECOND = "ParquetTimestampInMillisecond"
    PRESERVE_TRANSACTIONS = "PreserveTransactions"
    BUCKET_FOLDER = "BucketFolder"
    DATE_PARTITION_DELIMITER = "DatePartitionDelimiter"
    ENCODING_TYPE = "EncodingType"
    ADD_COLUMN_NAME = "AddColumnName"
    CDC_MIN_FILE_SIZE = "CdcMinFileSize"
    PARQUET_VERSION = "ParquetVersion"
    EXTERNAL_TABLE_DEFINITION = "ExternalTableDefinition"
    USE_CSV_NO_SUP_VALUE = "UseCsvNoSupValue"
    MAX_FILE_SIZE = "MaxFileSize"
    CDC_PATH = "CdcPath"
    CSV_NO_SUP_VALUE = "CsvNoSupValue"
    CDC_MAX_BATCH_INTERVAL = "CdcMaxBatchInterval"
    CSV_ROW_DELIMITER = "CsvRowDelimiter"
    ROW_GROUP_LENGTH = "RowGroupLength"
    DATA_PAGE_SIZE = "DataPageSize"
    DATE_PARTITION_ENABLED = "DatePartitionEnabled"
    DICT_PAGE_SIZE_LIMIT = "DictPageSizeLimit"
    COMPRESSION_TYPE = "CompressionType"
    DATE_PARTITION_TIMEZONE = "DatePartitionTimezone"
    CDC_INSERTS_ONLY = "CdcInsertsOnly"
    EXPECTED_BUCKET_OWNER = "ExpectedBucketOwner"
    ENCRYPTION_MODE = "EncryptionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timestamp_column_name": "TimestampColumnName",
        "enable_statistics": "EnableStatistics",
        "date_partition_sequence": "DatePartitionSequence",
        "csv_null_value": "CsvNullValue",
        "include_op_for_full_load": "IncludeOpForFullLoad",
        "cdc_inserts_and_updates": "CdcInsertsAndUpdates",
        "bucket_name": "BucketName",
        "server_side_encryption_kms_key_id": "ServerSideEncryptionKmsKeyId",
        "use_task_start_time_for_full_load_timestamp": "UseTaskStartTimeForFullLoadTimestamp",
        "glue_catalog_generation": "GlueCatalogGeneration",
        "data_format": "DataFormat",
        "csv_delimiter": "CsvDelimiter",
        "add_trailing_padding_character": "AddTrailingPaddingCharacter",
        "ignore_header_rows": "IgnoreHeaderRows",
        "canned_acl_for_objects": "CannedAclForObjects",
        "rfc4180": "Rfc4180",
        "service_access_role_arn": "ServiceAccessRoleArn",
        "parquet_timestamp_in_millisecond": "ParquetTimestampInMillisecond",
        "preserve_transactions": "PreserveTransactions",
        "bucket_folder": "BucketFolder",
        "date_partition_delimiter": "DatePartitionDelimiter",
        "encoding_type": "EncodingType",
        "add_column_name": "AddColumnName",
        "cdc_min_file_size": "CdcMinFileSize",
        "parquet_version": "ParquetVersion",
        "external_table_definition": "ExternalTableDefinition",
        "use_csv_no_sup_value": "UseCsvNoSupValue",
        "max_file_size": "MaxFileSize",
        "cdc_path": "CdcPath",
        "csv_no_sup_value": "CsvNoSupValue",
        "cdc_max_batch_interval": "CdcMaxBatchInterval",
        "csv_row_delimiter": "CsvRowDelimiter",
        "row_group_length": "RowGroupLength",
        "data_page_size": "DataPageSize",
        "date_partition_enabled": "DatePartitionEnabled",
        "dict_page_size_limit": "DictPageSizeLimit",
        "compression_type": "CompressionType",
        "date_partition_timezone": "DatePartitionTimezone",
        "cdc_inserts_only": "CdcInsertsOnly",
        "expected_bucket_owner": "ExpectedBucketOwner",
        "encryption_mode": "EncryptionMode",
    }

    timestamp_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_statistics: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    date_partition_sequence: Optional[Union[str, DatePartitionSequenceValue, Ref, GetAtt, Sub]] = None
    csv_null_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_op_for_full_load: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cdc_inserts_and_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_side_encryption_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_task_start_time_for_full_load_timestamp: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    glue_catalog_generation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_format: Optional[Union[str, DataFormatValue, Ref, GetAtt, Sub]] = None
    csv_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    add_trailing_padding_character: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ignore_header_rows: Optional[Union[int, Ref, GetAtt, Sub]] = None
    canned_acl_for_objects: Optional[Union[str, CannedAclForObjectsValue, Ref, GetAtt, Sub]] = None
    rfc4180: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    service_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parquet_timestamp_in_millisecond: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    preserve_transactions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bucket_folder: Optional[Union[str, Ref, GetAtt, Sub]] = None
    date_partition_delimiter: Optional[Union[str, DatePartitionDelimiterValue, Ref, GetAtt, Sub]] = None
    encoding_type: Optional[Union[str, EncodingTypeValue, Ref, GetAtt, Sub]] = None
    add_column_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cdc_min_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    parquet_version: Optional[Union[str, ParquetVersionValue, Ref, GetAtt, Sub]] = None
    external_table_definition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_csv_no_sup_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cdc_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    csv_no_sup_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdc_max_batch_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    csv_row_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    row_group_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    data_page_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    date_partition_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dict_page_size_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    compression_type: Optional[Union[str, CompressionTypeValue, Ref, GetAtt, Sub]] = None
    date_partition_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdc_inserts_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expected_bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_mode: Optional[Union[str, EncryptionModeValue, Ref, GetAtt, Sub]] = None


@dataclass
class SybaseSettings(PropertyType):
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
    }

    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

