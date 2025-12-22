"""PropertyTypes for AWS::Glue::DataCatalogEncryptionSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AdditionalOptionKeys:
    """AdditionalOptionKeys enum values."""

    PERFORMANCETUNING_CACHING = "performanceTuning.caching"
    OBSERVATIONS_SCOPE = "observations.scope"
    COMPOSITERULEEVALUATION_METHOD = "compositeRuleEvaluation.method"


class AggFunction:
    """AggFunction enum values."""

    AVG = "avg"
    COUNTDISTINCT = "countDistinct"
    COUNT = "count"
    FIRST = "first"
    LAST = "last"
    KURTOSIS = "kurtosis"
    MAX = "max"
    MIN = "min"
    SKEWNESS = "skewness"
    STDDEV_SAMP = "stddev_samp"
    STDDEV_POP = "stddev_pop"
    SUM = "sum"
    SUMDISTINCT = "sumDistinct"
    VAR_SAMP = "var_samp"
    VAR_POP = "var_pop"


class AllowFullTableExternalDataAccessEnum:
    """AllowFullTableExternalDataAccessEnum enum values."""

    TRUE = "True"
    FALSE = "False"


class AuthenticationType:
    """AuthenticationType enum values."""

    BASIC = "BASIC"
    OAUTH2 = "OAUTH2"
    CUSTOM = "CUSTOM"
    IAM = "IAM"


class BackfillErrorCode:
    """BackfillErrorCode enum values."""

    ENCRYPTED_PARTITION_ERROR = "ENCRYPTED_PARTITION_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_PARTITION_TYPE_DATA_ERROR = "INVALID_PARTITION_TYPE_DATA_ERROR"
    MISSING_PARTITION_VALUE_ERROR = "MISSING_PARTITION_VALUE_ERROR"
    UNSUPPORTED_PARTITION_CHARACTER_ERROR = "UNSUPPORTED_PARTITION_CHARACTER_ERROR"


class BlueprintRunState:
    """BlueprintRunState enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    ROLLING_BACK = "ROLLING_BACK"


class BlueprintStatus:
    """BlueprintStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    FAILED = "FAILED"


class CatalogEncryptionMode:
    """CatalogEncryptionMode enum values."""

    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"
    SSE_KMS_WITH_SERVICE_ROLE = "SSE-KMS-WITH-SERVICE-ROLE"


class CloudWatchEncryptionMode:
    """CloudWatchEncryptionMode enum values."""

    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


class ColumnStatisticsState:
    """ColumnStatisticsState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class ColumnStatisticsType:
    """ColumnStatisticsType enum values."""

    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DOUBLE = "DOUBLE"
    LONG = "LONG"
    STRING = "STRING"
    BINARY = "BINARY"


class CompactionStrategy:
    """CompactionStrategy enum values."""

    BINPACK = "binpack"
    SORT = "sort"
    Z_ORDER = "z-order"


class Comparator:
    """Comparator enum values."""

    EQUALS = "EQUALS"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_EQUALS = "GREATER_THAN_EQUALS"
    LESS_THAN_EQUALS = "LESS_THAN_EQUALS"


class Compatibility:
    """Compatibility enum values."""

    NONE = "NONE"
    DISABLED = "DISABLED"
    BACKWARD = "BACKWARD"
    BACKWARD_ALL = "BACKWARD_ALL"
    FORWARD = "FORWARD"
    FORWARD_ALL = "FORWARD_ALL"
    FULL = "FULL"
    FULL_ALL = "FULL_ALL"


class CompressionType:
    """CompressionType enum values."""

    GZIP = "gzip"
    BZIP2 = "bzip2"


class ComputationType:
    """ComputationType enum values."""

    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"


class ComputeEnvironment:
    """ComputeEnvironment enum values."""

    SPARK = "SPARK"
    ATHENA = "ATHENA"
    PYTHON = "PYTHON"


class ConfigurationSource:
    """ConfigurationSource enum values."""

    CATALOG = "catalog"
    TABLE = "table"


class ConnectionPropertyKey:
    """ConnectionPropertyKey enum values."""

    HOST = "HOST"
    PORT = "PORT"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    ENCRYPTED_PASSWORD = "ENCRYPTED_PASSWORD"
    JDBC_DRIVER_JAR_URI = "JDBC_DRIVER_JAR_URI"
    JDBC_DRIVER_CLASS_NAME = "JDBC_DRIVER_CLASS_NAME"
    JDBC_ENGINE = "JDBC_ENGINE"
    JDBC_ENGINE_VERSION = "JDBC_ENGINE_VERSION"
    CONFIG_FILES = "CONFIG_FILES"
    INSTANCE_ID = "INSTANCE_ID"
    JDBC_CONNECTION_URL = "JDBC_CONNECTION_URL"
    JDBC_ENFORCE_SSL = "JDBC_ENFORCE_SSL"
    CUSTOM_JDBC_CERT = "CUSTOM_JDBC_CERT"
    SKIP_CUSTOM_JDBC_CERT_VALIDATION = "SKIP_CUSTOM_JDBC_CERT_VALIDATION"
    CUSTOM_JDBC_CERT_STRING = "CUSTOM_JDBC_CERT_STRING"
    CONNECTION_URL = "CONNECTION_URL"
    KAFKA_BOOTSTRAP_SERVERS = "KAFKA_BOOTSTRAP_SERVERS"
    KAFKA_SSL_ENABLED = "KAFKA_SSL_ENABLED"
    KAFKA_CUSTOM_CERT = "KAFKA_CUSTOM_CERT"
    KAFKA_SKIP_CUSTOM_CERT_VALIDATION = "KAFKA_SKIP_CUSTOM_CERT_VALIDATION"
    KAFKA_CLIENT_KEYSTORE = "KAFKA_CLIENT_KEYSTORE"
    KAFKA_CLIENT_KEYSTORE_PASSWORD = "KAFKA_CLIENT_KEYSTORE_PASSWORD"
    KAFKA_CLIENT_KEY_PASSWORD = "KAFKA_CLIENT_KEY_PASSWORD"
    ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD = "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD"
    ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD = "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD"
    KAFKA_SASL_MECHANISM = "KAFKA_SASL_MECHANISM"
    KAFKA_SASL_PLAIN_USERNAME = "KAFKA_SASL_PLAIN_USERNAME"
    KAFKA_SASL_PLAIN_PASSWORD = "KAFKA_SASL_PLAIN_PASSWORD"
    ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD = "ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD"
    KAFKA_SASL_SCRAM_USERNAME = "KAFKA_SASL_SCRAM_USERNAME"
    KAFKA_SASL_SCRAM_PASSWORD = "KAFKA_SASL_SCRAM_PASSWORD"
    KAFKA_SASL_SCRAM_SECRETS_ARN = "KAFKA_SASL_SCRAM_SECRETS_ARN"
    ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD = "ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD"
    KAFKA_SASL_GSSAPI_KEYTAB = "KAFKA_SASL_GSSAPI_KEYTAB"
    KAFKA_SASL_GSSAPI_KRB5_CONF = "KAFKA_SASL_GSSAPI_KRB5_CONF"
    KAFKA_SASL_GSSAPI_SERVICE = "KAFKA_SASL_GSSAPI_SERVICE"
    KAFKA_SASL_GSSAPI_PRINCIPAL = "KAFKA_SASL_GSSAPI_PRINCIPAL"
    SECRET_ID = "SECRET_ID"
    CONNECTOR_URL = "CONNECTOR_URL"
    CONNECTOR_TYPE = "CONNECTOR_TYPE"
    CONNECTOR_CLASS_NAME = "CONNECTOR_CLASS_NAME"
    ENDPOINT = "ENDPOINT"
    ENDPOINT_TYPE = "ENDPOINT_TYPE"
    ROLE_ARN = "ROLE_ARN"
    REGION = "REGION"
    WORKGROUP_NAME = "WORKGROUP_NAME"
    CLUSTER_IDENTIFIER = "CLUSTER_IDENTIFIER"
    DATABASE = "DATABASE"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class ConnectionType:
    """ConnectionType enum values."""

    JDBC = "JDBC"
    SFTP = "SFTP"
    MONGODB = "MONGODB"
    KAFKA = "KAFKA"
    NETWORK = "NETWORK"
    MARKETPLACE = "MARKETPLACE"
    CUSTOM = "CUSTOM"
    SALESFORCE = "SALESFORCE"
    VIEW_VALIDATION_REDSHIFT = "VIEW_VALIDATION_REDSHIFT"
    VIEW_VALIDATION_ATHENA = "VIEW_VALIDATION_ATHENA"
    GOOGLEADS = "GOOGLEADS"
    GOOGLESHEETS = "GOOGLESHEETS"
    GOOGLEANALYTICS4 = "GOOGLEANALYTICS4"
    SERVICENOW = "SERVICENOW"
    MARKETO = "MARKETO"
    SAPODATA = "SAPODATA"
    ZENDESK = "ZENDESK"
    JIRACLOUD = "JIRACLOUD"
    NETSUITEERP = "NETSUITEERP"
    HUBSPOT = "HUBSPOT"
    FACEBOOKADS = "FACEBOOKADS"
    INSTAGRAMADS = "INSTAGRAMADS"
    ZOHOCRM = "ZOHOCRM"
    SALESFORCEPARDOT = "SALESFORCEPARDOT"
    SALESFORCEMARKETINGCLOUD = "SALESFORCEMARKETINGCLOUD"
    ADOBEANALYTICS = "ADOBEANALYTICS"
    SLACK = "SLACK"
    LINKEDIN = "LINKEDIN"
    MIXPANEL = "MIXPANEL"
    ASANA = "ASANA"
    STRIPE = "STRIPE"
    SMARTSHEET = "SMARTSHEET"
    DATADOG = "DATADOG"
    WOOCOMMERCE = "WOOCOMMERCE"
    INTERCOM = "INTERCOM"
    SNAPCHATADS = "SNAPCHATADS"
    PAYPAL = "PAYPAL"
    QUICKBOOKS = "QUICKBOOKS"
    FACEBOOKPAGEINSIGHTS = "FACEBOOKPAGEINSIGHTS"
    FRESHDESK = "FRESHDESK"
    TWILIO = "TWILIO"
    DOCUSIGNMONITOR = "DOCUSIGNMONITOR"
    FRESHSALES = "FRESHSALES"
    ZOOM = "ZOOM"
    GOOGLESEARCHCONSOLE = "GOOGLESEARCHCONSOLE"
    SALESFORCECOMMERCECLOUD = "SALESFORCECOMMERCECLOUD"
    SAPCONCUR = "SAPCONCUR"
    DYNATRACE = "DYNATRACE"
    MICROSOFTDYNAMIC365FINANCEANDOPS = "MICROSOFTDYNAMIC365FINANCEANDOPS"
    MICROSOFTTEAMS = "MICROSOFTTEAMS"
    BLACKBAUDRAISEREDGENXT = "BLACKBAUDRAISEREDGENXT"
    MAILCHIMP = "MAILCHIMP"
    GITLAB = "GITLAB"
    PENDO = "PENDO"
    PRODUCTBOARD = "PRODUCTBOARD"
    CIRCLECI = "CIRCLECI"
    PIPEDIVE = "PIPEDIVE"
    SENDGRID = "SENDGRID"
    AZURECOSMOS = "AZURECOSMOS"
    AZURESQL = "AZURESQL"
    BIGQUERY = "BIGQUERY"
    BLACKBAUD = "BLACKBAUD"
    CLOUDERAHIVE = "CLOUDERAHIVE"
    CLOUDERAIMPALA = "CLOUDERAIMPALA"
    CLOUDWATCH = "CLOUDWATCH"
    CLOUDWATCHMETRICS = "CLOUDWATCHMETRICS"
    CMDB = "CMDB"
    DATALAKEGEN2 = "DATALAKEGEN2"
    DB2 = "DB2"
    DB2AS400 = "DB2AS400"
    DOCUMENTDB = "DOCUMENTDB"
    DOMO = "DOMO"
    DYNAMODB = "DYNAMODB"
    GOOGLECLOUDSTORAGE = "GOOGLECLOUDSTORAGE"
    HBASE = "HBASE"
    KUSTOMER = "KUSTOMER"
    MICROSOFTDYNAMICS365CRM = "MICROSOFTDYNAMICS365CRM"
    MONDAY = "MONDAY"
    MYSQL = "MYSQL"
    OKTA = "OKTA"
    OPENSEARCH = "OPENSEARCH"
    ORACLE = "ORACLE"
    PIPEDRIVE = "PIPEDRIVE"
    POSTGRESQL = "POSTGRESQL"
    SAPHANA = "SAPHANA"
    SQLSERVER = "SQLSERVER"
    SYNAPSE = "SYNAPSE"
    TERADATA = "TERADATA"
    TERADATANOS = "TERADATANOS"
    TIMESTREAM = "TIMESTREAM"
    TPCDS = "TPCDS"
    VERTICA = "VERTICA"


class CrawlState:
    """CrawlState enum values."""

    RUNNING = "RUNNING"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    ERROR = "ERROR"


class CrawlerHistoryState:
    """CrawlerHistoryState enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class CrawlerLineageSettings:
    """CrawlerLineageSettings enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class CrawlerState:
    """CrawlerState enum values."""

    READY = "READY"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"


class CsvHeaderOption:
    """CsvHeaderOption enum values."""

    UNKNOWN = "UNKNOWN"
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"


class CsvSerdeOption:
    """CsvSerdeOption enum values."""

    OPENCSVSERDE = "OpenCSVSerDe"
    LAZYSIMPLESERDE = "LazySimpleSerDe"
    NONE = "None"


class DQCompositeRuleEvaluationMethod:
    """DQCompositeRuleEvaluationMethod enum values."""

    COLUMN = "COLUMN"
    ROW = "ROW"


class DQStopJobOnFailureTiming:
    """DQStopJobOnFailureTiming enum values."""

    IMMEDIATE = "Immediate"
    AFTERDATALOAD = "AfterDataLoad"


class DQTransformOutput:
    """DQTransformOutput enum values."""

    PRIMARYINPUT = "PrimaryInput"
    EVALUATIONRESULTS = "EvaluationResults"


class DataFormat:
    """DataFormat enum values."""

    AVRO = "AVRO"
    JSON = "JSON"
    PROTOBUF = "PROTOBUF"


class DataOperation:
    """DataOperation enum values."""

    READ = "READ"
    WRITE = "WRITE"


class DataQualityEncryptionMode:
    """DataQualityEncryptionMode enum values."""

    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


class DataQualityModelStatus:
    """DataQualityModelStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class DataQualityRuleResultStatus:
    """DataQualityRuleResultStatus enum values."""

    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"


class DatabaseAttributes:
    """DatabaseAttributes enum values."""

    NAME = "NAME"
    TARGET_DATABASE = "TARGET_DATABASE"


class DdbExportType:
    """DdbExportType enum values."""

    DDB = "ddb"
    S3 = "s3"


class DeleteBehavior:
    """DeleteBehavior enum values."""

    LOG = "LOG"
    DELETE_FROM_DATABASE = "DELETE_FROM_DATABASE"
    DEPRECATE_IN_DATABASE = "DEPRECATE_IN_DATABASE"


class DeltaTargetCompressionType:
    """DeltaTargetCompressionType enum values."""

    UNCOMPRESSED = "uncompressed"
    SNAPPY = "snappy"


class EnableHybridValues:
    """EnableHybridValues enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"


class ExecutionClass:
    """ExecutionClass enum values."""

    FLEX = "FLEX"
    STANDARD = "STANDARD"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    FAILED = "FAILED"
    STARTED = "STARTED"


class ExistCondition:
    """ExistCondition enum values."""

    MUST_EXIST = "MUST_EXIST"
    NOT_EXIST = "NOT_EXIST"
    NONE = "NONE"


class FederationSourceErrorCode:
    """FederationSourceErrorCode enum values."""

    ACCESSDENIEDEXCEPTION = "AccessDeniedException"
    ENTITYNOTFOUNDEXCEPTION = "EntityNotFoundException"
    INVALIDCREDENTIALSEXCEPTION = "InvalidCredentialsException"
    INVALIDINPUTEXCEPTION = "InvalidInputException"
    INVALIDRESPONSEEXCEPTION = "InvalidResponseException"
    OPERATIONTIMEOUTEXCEPTION = "OperationTimeoutException"
    OPERATIONNOTSUPPORTEDEXCEPTION = "OperationNotSupportedException"
    INTERNALSERVICEEXCEPTION = "InternalServiceException"
    PARTIALFAILUREEXCEPTION = "PartialFailureException"
    THROTTLINGEXCEPTION = "ThrottlingException"


class FieldDataType:
    """FieldDataType enum values."""

    INT = "INT"
    SMALLINT = "SMALLINT"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    LONG = "LONG"
    DATE = "DATE"
    BOOLEAN = "BOOLEAN"
    MAP = "MAP"
    ARRAY = "ARRAY"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    DECIMAL = "DECIMAL"
    BYTE = "BYTE"
    SHORT = "SHORT"
    DOUBLE = "DOUBLE"
    STRUCT = "STRUCT"


class FieldFilterOperator:
    """FieldFilterOperator enum values."""

    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    CONTAINS = "CONTAINS"
    ORDER_BY = "ORDER_BY"


class FieldName:
    """FieldName enum values."""

    CRAWL_ID = "CRAWL_ID"
    STATE = "STATE"
    START_TIME = "START_TIME"
    END_TIME = "END_TIME"
    DPU_HOUR = "DPU_HOUR"


class FilterLogicalOperator:
    """FilterLogicalOperator enum values."""

    AND = "AND"
    OR = "OR"


class FilterOperation:
    """FilterOperation enum values."""

    EQ = "EQ"
    LT = "LT"
    GT = "GT"
    LTE = "LTE"
    GTE = "GTE"
    REGEX = "REGEX"
    ISNULL = "ISNULL"


class FilterOperator:
    """FilterOperator enum values."""

    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"
    EQ = "EQ"
    NE = "NE"


class FilterValueType:
    """FilterValueType enum values."""

    COLUMNEXTRACTED = "COLUMNEXTRACTED"
    CONSTANT = "CONSTANT"


class FunctionType:
    """FunctionType enum values."""

    REGULAR_FUNCTION = "REGULAR_FUNCTION"
    AGGREGATE_FUNCTION = "AGGREGATE_FUNCTION"
    STORED_PROCEDURE = "STORED_PROCEDURE"


class GlueRecordType:
    """GlueRecordType enum values."""

    DATE = "DATE"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    INT = "INT"
    FLOAT = "FLOAT"
    LONG = "LONG"
    BIGDECIMAL = "BIGDECIMAL"
    BYTE = "BYTE"
    SHORT = "SHORT"
    DOUBLE = "DOUBLE"


class HudiTargetCompressionType:
    """HudiTargetCompressionType enum values."""

    GZIP = "gzip"
    LZO = "lzo"
    UNCOMPRESSED = "uncompressed"
    SNAPPY = "snappy"


class HyperTargetCompressionType:
    """HyperTargetCompressionType enum values."""

    UNCOMPRESSED = "uncompressed"


class IcebergNullOrder:
    """IcebergNullOrder enum values."""

    NULLS_FIRST = "nulls-first"
    NULLS_LAST = "nulls-last"


class IcebergSortDirection:
    """IcebergSortDirection enum values."""

    ASC = "asc"
    DESC = "desc"


class IcebergStructTypeEnum:
    """IcebergStructTypeEnum enum values."""

    STRUCT = "struct"


class IcebergTargetCompressionType:
    """IcebergTargetCompressionType enum values."""

    GZIP = "gzip"
    LZO = "lzo"
    UNCOMPRESSED = "uncompressed"
    SNAPPY = "snappy"


class IcebergUpdateAction:
    """IcebergUpdateAction enum values."""

    ADD_SCHEMA = "add-schema"
    SET_CURRENT_SCHEMA = "set-current-schema"
    ADD_SPEC = "add-spec"
    SET_DEFAULT_SPEC = "set-default-spec"
    ADD_SORT_ORDER = "add-sort-order"
    SET_DEFAULT_SORT_ORDER = "set-default-sort-order"
    SET_LOCATION = "set-location"
    SET_PROPERTIES = "set-properties"
    REMOVE_PROPERTIES = "remove-properties"
    ADD_ENCRYPTION_KEY = "add-encryption-key"
    REMOVE_ENCRYPTION_KEY = "remove-encryption-key"


class InclusionAnnotationValue:
    """InclusionAnnotationValue enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class IntegrationStatus:
    """IntegrationStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    MODIFYING = "MODIFYING"
    FAILED = "FAILED"
    DELETING = "DELETING"
    SYNCING = "SYNCING"
    NEEDS_ATTENTION = "NEEDS_ATTENTION"


class JDBCConnectionType:
    """JDBCConnectionType enum values."""

    SQLSERVER = "sqlserver"
    MYSQL = "mysql"
    ORACLE = "oracle"
    POSTGRESQL = "postgresql"
    REDSHIFT = "redshift"


class JDBCDataType:
    """JDBCDataType enum values."""

    ARRAY = "ARRAY"
    BIGINT = "BIGINT"
    BINARY = "BINARY"
    BIT = "BIT"
    BLOB = "BLOB"
    BOOLEAN = "BOOLEAN"
    CHAR = "CHAR"
    CLOB = "CLOB"
    DATALINK = "DATALINK"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DISTINCT = "DISTINCT"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    JAVA_OBJECT = "JAVA_OBJECT"
    LONGNVARCHAR = "LONGNVARCHAR"
    LONGVARBINARY = "LONGVARBINARY"
    LONGVARCHAR = "LONGVARCHAR"
    NCHAR = "NCHAR"
    NCLOB = "NCLOB"
    NULL = "NULL"
    NUMERIC = "NUMERIC"
    NVARCHAR = "NVARCHAR"
    OTHER = "OTHER"
    REAL = "REAL"
    REF = "REF"
    REF_CURSOR = "REF_CURSOR"
    ROWID = "ROWID"
    SMALLINT = "SMALLINT"
    SQLXML = "SQLXML"
    STRUCT = "STRUCT"
    TIME = "TIME"
    TIME_WITH_TIMEZONE = "TIME_WITH_TIMEZONE"
    TIMESTAMP = "TIMESTAMP"
    TIMESTAMP_WITH_TIMEZONE = "TIMESTAMP_WITH_TIMEZONE"
    TINYINT = "TINYINT"
    VARBINARY = "VARBINARY"
    VARCHAR = "VARCHAR"


class JdbcMetadataEntry:
    """JdbcMetadataEntry enum values."""

    COMMENTS = "COMMENTS"
    RAWTYPES = "RAWTYPES"


class JobBookmarksEncryptionMode:
    """JobBookmarksEncryptionMode enum values."""

    DISABLED = "DISABLED"
    CSE_KMS = "CSE-KMS"


class JobMode:
    """JobMode enum values."""

    SCRIPT = "SCRIPT"
    VISUAL = "VISUAL"
    NOTEBOOK = "NOTEBOOK"


class JobRunState:
    """JobRunState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    ERROR = "ERROR"
    WAITING = "WAITING"
    EXPIRED = "EXPIRED"


class JoinType:
    """JoinType enum values."""

    EQUIJOIN = "equijoin"
    LEFT = "left"
    RIGHT = "right"
    OUTER = "outer"
    LEFTSEMI = "leftsemi"
    LEFTANTI = "leftanti"


class Language:
    """Language enum values."""

    PYTHON = "PYTHON"
    SCALA = "SCALA"


class LastCrawlStatus:
    """LastCrawlStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class LastRefreshType:
    """LastRefreshType enum values."""

    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"


class Logical:
    """Logical enum values."""

    AND = "AND"
    ANY = "ANY"


class LogicalOperator:
    """LogicalOperator enum values."""

    EQUALS = "EQUALS"


class MLUserDataEncryptionModeString:
    """MLUserDataEncryptionModeString enum values."""

    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


class MetadataOperation:
    """MetadataOperation enum values."""

    CREATE = "CREATE"


class NodeType:
    """NodeType enum values."""

    CRAWLER = "CRAWLER"
    JOB = "JOB"
    TRIGGER = "TRIGGER"


class OAuth2GrantType:
    """OAuth2GrantType enum values."""

    AUTHORIZATION_CODE = "AUTHORIZATION_CODE"
    CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"
    JWT_BEARER = "JWT_BEARER"


class ParamType:
    """ParamType enum values."""

    STR = "str"
    INT = "int"
    FLOAT = "float"
    COMPLEX = "complex"
    BOOL = "bool"
    LIST = "list"
    NULL = "null"


class ParquetCompressionType:
    """ParquetCompressionType enum values."""

    SNAPPY = "snappy"
    LZO = "lzo"
    GZIP = "gzip"
    BROTLI = "brotli"
    LZ4 = "lz4"
    UNCOMPRESSED = "uncompressed"
    NONE = "none"


class PartitionIndexStatus:
    """PartitionIndexStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"


class Permission:
    """Permission enum values."""

    ALL = "ALL"
    SELECT = "SELECT"
    ALTER = "ALTER"
    DROP = "DROP"
    DELETE = "DELETE"
    INSERT = "INSERT"
    CREATE_DATABASE = "CREATE_DATABASE"
    CREATE_TABLE = "CREATE_TABLE"
    DATA_LOCATION_ACCESS = "DATA_LOCATION_ACCESS"


class PermissionType:
    """PermissionType enum values."""

    COLUMN_PERMISSION = "COLUMN_PERMISSION"
    CELL_FILTER_PERMISSION = "CELL_FILTER_PERMISSION"
    NESTED_PERMISSION = "NESTED_PERMISSION"
    NESTED_CELL_PERMISSION = "NESTED_CELL_PERMISSION"


class PiiType:
    """PiiType enum values."""

    ROWAUDIT = "RowAudit"
    ROWHASHING = "RowHashing"
    ROWMASKING = "RowMasking"
    ROWPARTIALMASKING = "RowPartialMasking"
    COLUMNAUDIT = "ColumnAudit"
    COLUMNHASHING = "ColumnHashing"
    COLUMNMASKING = "ColumnMasking"


class PrincipalType:
    """PrincipalType enum values."""

    USER = "USER"
    ROLE = "ROLE"
    GROUP = "GROUP"


class PropertyType:
    """PropertyType enum values."""

    USER_INPUT = "USER_INPUT"
    SECRET = "SECRET"
    READ_ONLY = "READ_ONLY"
    UNUSED = "UNUSED"
    SECRET_OR_USER_INPUT = "SECRET_OR_USER_INPUT"


class QuoteChar:
    """QuoteChar enum values."""

    QUOTE = "quote"
    QUILLEMET = "quillemet"
    SINGLE_QUOTE = "single_quote"
    DISABLED = "disabled"


class RecrawlBehavior:
    """RecrawlBehavior enum values."""

    CRAWL_EVERYTHING = "CRAWL_EVERYTHING"
    CRAWL_NEW_FOLDERS_ONLY = "CRAWL_NEW_FOLDERS_ONLY"
    CRAWL_EVENT_MODE = "CRAWL_EVENT_MODE"


class RegistryStatus:
    """RegistryStatus enum values."""

    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"


class ResourceAction:
    """ResourceAction enum values."""

    UPDATE = "UPDATE"
    CREATE = "CREATE"


class ResourceShareType:
    """ResourceShareType enum values."""

    FOREIGN = "FOREIGN"
    ALL = "ALL"
    FEDERATED = "FEDERATED"


class ResourceState:
    """ResourceState enum values."""

    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


class ResourceType:
    """ResourceType enum values."""

    JAR = "JAR"
    FILE = "FILE"
    ARCHIVE = "ARCHIVE"


class S3EncryptionMode:
    """S3EncryptionMode enum values."""

    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"
    SSE_S3 = "SSE-S3"


class ScheduleState:
    """ScheduleState enum values."""

    SCHEDULED = "SCHEDULED"
    NOT_SCHEDULED = "NOT_SCHEDULED"
    TRANSITIONING = "TRANSITIONING"


class ScheduleType:
    """ScheduleType enum values."""

    CRON = "CRON"
    AUTO = "AUTO"


class SchemaDiffType:
    """SchemaDiffType enum values."""

    SYNTAX_DIFF = "SYNTAX_DIFF"


class SchemaStatus:
    """SchemaStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    DELETING = "DELETING"


class SchemaVersionStatus:
    """SchemaVersionStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    FAILURE = "FAILURE"
    DELETING = "DELETING"


class Separator:
    """Separator enum values."""

    COMMA = "comma"
    CTRLA = "ctrla"
    PIPE = "pipe"
    SEMICOLON = "semicolon"
    TAB = "tab"


class SessionStatus:
    """SessionStatus enum values."""

    PROVISIONING = "PROVISIONING"
    READY = "READY"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class SettingSource:
    """SettingSource enum values."""

    CATALOG = "CATALOG"
    TABLE = "TABLE"


class Sort:
    """Sort enum values."""

    ASC = "ASC"
    DESC = "DESC"


class SortDirectionType:
    """SortDirectionType enum values."""

    DESCENDING = "DESCENDING"
    ASCENDING = "ASCENDING"


class SourceControlAuthStrategy:
    """SourceControlAuthStrategy enum values."""

    PERSONAL_ACCESS_TOKEN = "PERSONAL_ACCESS_TOKEN"
    AWS_SECRETS_MANAGER = "AWS_SECRETS_MANAGER"


class SourceControlProvider:
    """SourceControlProvider enum values."""

    GITHUB = "GITHUB"
    GITLAB = "GITLAB"
    BITBUCKET = "BITBUCKET"
    AWS_CODE_COMMIT = "AWS_CODE_COMMIT"


class StartingPosition:
    """StartingPosition enum values."""

    LATEST = "latest"
    TRIM_HORIZON = "trim_horizon"
    EARLIEST = "earliest"
    TIMESTAMP = "timestamp"


class StatementState:
    """StatementState enum values."""

    WAITING = "WAITING"
    RUNNING = "RUNNING"
    AVAILABLE = "AVAILABLE"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    ERROR = "ERROR"


class StatisticEvaluationLevel:
    """StatisticEvaluationLevel enum values."""

    DATASET = "Dataset"
    COLUMN = "Column"
    MULTICOLUMN = "Multicolumn"


class TableAttributes:
    """TableAttributes enum values."""

    NAME = "NAME"
    TABLE_TYPE = "TABLE_TYPE"


class TableOptimizerEventType:
    """TableOptimizerEventType enum values."""

    STARTING = "starting"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"


class TableOptimizerType:
    """TableOptimizerType enum values."""

    COMPACTION = "compaction"
    RETENTION = "retention"
    ORPHAN_FILE_DELETION = "orphan_file_deletion"


class TargetFormat:
    """TargetFormat enum values."""

    JSON = "json"
    CSV = "csv"
    AVRO = "avro"
    ORC = "orc"
    PARQUET = "parquet"
    HUDI = "hudi"
    DELTA = "delta"
    ICEBERG = "iceberg"
    HYPER = "hyper"
    XML = "xml"


class TaskRunSortColumnType:
    """TaskRunSortColumnType enum values."""

    TASK_RUN_TYPE = "TASK_RUN_TYPE"
    STATUS = "STATUS"
    STARTED = "STARTED"


class TaskStatusType:
    """TaskStatusType enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"


class TaskType:
    """TaskType enum values."""

    EVALUATION = "EVALUATION"
    LABELING_SET_GENERATION = "LABELING_SET_GENERATION"
    IMPORT_LABELS = "IMPORT_LABELS"
    EXPORT_LABELS = "EXPORT_LABELS"
    FIND_MATCHES = "FIND_MATCHES"


class TransformSortColumnType:
    """TransformSortColumnType enum values."""

    NAME = "NAME"
    TRANSFORM_TYPE = "TRANSFORM_TYPE"
    STATUS = "STATUS"
    CREATED = "CREATED"
    LAST_MODIFIED = "LAST_MODIFIED"


class TransformStatusType:
    """TransformStatusType enum values."""

    NOT_READY = "NOT_READY"
    READY = "READY"
    DELETING = "DELETING"


class TransformType:
    """TransformType enum values."""

    FIND_MATCHES = "FIND_MATCHES"


class TriggerState:
    """TriggerState enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    ACTIVATING = "ACTIVATING"
    ACTIVATED = "ACTIVATED"
    DEACTIVATING = "DEACTIVATING"
    DEACTIVATED = "DEACTIVATED"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class TriggerType:
    """TriggerType enum values."""

    SCHEDULED = "SCHEDULED"
    CONDITIONAL = "CONDITIONAL"
    ON_DEMAND = "ON_DEMAND"
    EVENT = "EVENT"


class UnionType:
    """UnionType enum values."""

    ALL = "ALL"
    DISTINCT = "DISTINCT"


class UnnestSpec:
    """UnnestSpec enum values."""

    TOPLEVEL = "TOPLEVEL"
    FULL = "FULL"
    NOUNNEST = "NOUNNEST"


class UpdateBehavior:
    """UpdateBehavior enum values."""

    LOG = "LOG"
    UPDATE_IN_DATABASE = "UPDATE_IN_DATABASE"


class UpdateCatalogBehavior:
    """UpdateCatalogBehavior enum values."""

    UPDATE_IN_DATABASE = "UPDATE_IN_DATABASE"
    LOG = "LOG"


class ViewDialect:
    """ViewDialect enum values."""

    REDSHIFT = "REDSHIFT"
    ATHENA = "ATHENA"
    SPARK = "SPARK"


class ViewUpdateAction:
    """ViewUpdateAction enum values."""

    ADD = "ADD"
    REPLACE = "REPLACE"
    ADD_OR_REPLACE = "ADD_OR_REPLACE"
    DROP = "DROP"


class WorkerType:
    """WorkerType enum values."""

    STANDARD = "Standard"
    G_1X = "G.1X"
    G_2X = "G.2X"
    G_025X = "G.025X"
    G_4X = "G.4X"
    G_8X = "G.8X"
    Z_2X = "Z.2X"


class WorkflowRunStatus:
    """WorkflowRunStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


@dataclass
class ConnectionPasswordEncryption(PropertyType):
    RETURN_CONNECTION_PASSWORD_ENCRYPTED = "ReturnConnectionPasswordEncrypted"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "return_connection_password_encrypted": "ReturnConnectionPasswordEncrypted",
        "kms_key_id": "KmsKeyId",
    }

    return_connection_password_encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataCatalogEncryptionSettings(PropertyType):
    CONNECTION_PASSWORD_ENCRYPTION = "ConnectionPasswordEncryption"
    ENCRYPTION_AT_REST = "EncryptionAtRest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_password_encryption": "ConnectionPasswordEncryption",
        "encryption_at_rest": "EncryptionAtRest",
    }

    connection_password_encryption: Optional[ConnectionPasswordEncryption] = None
    encryption_at_rest: Optional[EncryptionAtRest] = None


@dataclass
class EncryptionAtRest(PropertyType):
    CATALOG_ENCRYPTION_MODE = "CatalogEncryptionMode"
    CATALOG_ENCRYPTION_SERVICE_ROLE = "CatalogEncryptionServiceRole"
    SSE_AWS_KMS_KEY_ID = "SseAwsKmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_encryption_mode": "CatalogEncryptionMode",
        "catalog_encryption_service_role": "CatalogEncryptionServiceRole",
        "sse_aws_kms_key_id": "SseAwsKmsKeyId",
    }

    catalog_encryption_mode: Optional[Union[str, CatalogEncryptionMode, Ref, GetAtt, Sub]] = None
    catalog_encryption_service_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_aws_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

