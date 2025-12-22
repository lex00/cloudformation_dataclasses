"""PropertyTypes for AWS::DMS::MigrationProject."""

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
class DataProviderDescriptor(PropertyType):
    DATA_PROVIDER_NAME = "DataProviderName"
    DATA_PROVIDER_ARN = "DataProviderArn"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    DATA_PROVIDER_IDENTIFIER = "DataProviderIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_provider_name": "DataProviderName",
        "data_provider_arn": "DataProviderArn",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "data_provider_identifier": "DataProviderIdentifier",
    }

    data_provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_provider_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaConversionApplicationAttributes(PropertyType):
    S3_BUCKET_PATH = "S3BucketPath"
    S3_BUCKET_ROLE_ARN = "S3BucketRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_path": "S3BucketPath",
        "s3_bucket_role_arn": "S3BucketRoleArn",
    }

    s3_bucket_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

