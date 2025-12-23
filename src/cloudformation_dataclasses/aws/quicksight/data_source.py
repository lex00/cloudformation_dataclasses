"""PropertyTypes for AWS::QuickSight::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmazonElasticsearchParameters(PropertyType):
    DOMAIN = "Domain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain": "Domain",
    }

    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AmazonOpenSearchParameters(PropertyType):
    DOMAIN = "Domain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain": "Domain",
    }

    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AthenaParameters(PropertyType):
    WORK_GROUP = "WorkGroup"
    IDENTITY_CENTER_CONFIGURATION = "IdentityCenterConfiguration"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "work_group": "WorkGroup",
        "identity_center_configuration": "IdentityCenterConfiguration",
        "role_arn": "RoleArn",
    }

    work_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identity_center_configuration: Optional[IdentityCenterConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuroraParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuroraPostgreSqlParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CredentialPair(PropertyType):
    ALTERNATE_DATA_SOURCE_PARAMETERS = "AlternateDataSourceParameters"
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alternate_data_source_parameters": "AlternateDataSourceParameters",
        "username": "Username",
        "password": "Password",
    }

    alternate_data_source_parameters: Optional[list[DataSourceParameters]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSourceCredentials(PropertyType):
    SECRET_ARN = "SecretArn"
    COPY_SOURCE_ARN = "CopySourceArn"
    CREDENTIAL_PAIR = "CredentialPair"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "copy_source_arn": "CopySourceArn",
        "credential_pair": "CredentialPair",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_pair: Optional[CredentialPair] = None


@dataclass
class DataSourceErrorInfo(PropertyType):
    TYPE = "Type"
    MESSAGE = "Message"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "message": "Message",
    }

    type_: Optional[Union[str, DataSourceErrorInfoType, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSourceParameters(PropertyType):
    AURORA_POSTGRE_SQL_PARAMETERS = "AuroraPostgreSqlParameters"
    TERADATA_PARAMETERS = "TeradataParameters"
    RDS_PARAMETERS = "RdsParameters"
    ATHENA_PARAMETERS = "AthenaParameters"
    SPARK_PARAMETERS = "SparkParameters"
    MARIA_DB_PARAMETERS = "MariaDbParameters"
    ORACLE_PARAMETERS = "OracleParameters"
    PRESTO_PARAMETERS = "PrestoParameters"
    STARBURST_PARAMETERS = "StarburstParameters"
    REDSHIFT_PARAMETERS = "RedshiftParameters"
    MY_SQL_PARAMETERS = "MySqlParameters"
    SQL_SERVER_PARAMETERS = "SqlServerParameters"
    SNOWFLAKE_PARAMETERS = "SnowflakeParameters"
    AMAZON_ELASTICSEARCH_PARAMETERS = "AmazonElasticsearchParameters"
    AMAZON_OPEN_SEARCH_PARAMETERS = "AmazonOpenSearchParameters"
    POSTGRE_SQL_PARAMETERS = "PostgreSqlParameters"
    AURORA_PARAMETERS = "AuroraParameters"
    S3_PARAMETERS = "S3Parameters"
    TRINO_PARAMETERS = "TrinoParameters"
    DATABRICKS_PARAMETERS = "DatabricksParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aurora_postgre_sql_parameters": "AuroraPostgreSqlParameters",
        "teradata_parameters": "TeradataParameters",
        "rds_parameters": "RdsParameters",
        "athena_parameters": "AthenaParameters",
        "spark_parameters": "SparkParameters",
        "maria_db_parameters": "MariaDbParameters",
        "oracle_parameters": "OracleParameters",
        "presto_parameters": "PrestoParameters",
        "starburst_parameters": "StarburstParameters",
        "redshift_parameters": "RedshiftParameters",
        "my_sql_parameters": "MySqlParameters",
        "sql_server_parameters": "SqlServerParameters",
        "snowflake_parameters": "SnowflakeParameters",
        "amazon_elasticsearch_parameters": "AmazonElasticsearchParameters",
        "amazon_open_search_parameters": "AmazonOpenSearchParameters",
        "postgre_sql_parameters": "PostgreSqlParameters",
        "aurora_parameters": "AuroraParameters",
        "s3_parameters": "S3Parameters",
        "trino_parameters": "TrinoParameters",
        "databricks_parameters": "DatabricksParameters",
    }

    aurora_postgre_sql_parameters: Optional[AuroraPostgreSqlParameters] = None
    teradata_parameters: Optional[TeradataParameters] = None
    rds_parameters: Optional[RdsParameters] = None
    athena_parameters: Optional[AthenaParameters] = None
    spark_parameters: Optional[SparkParameters] = None
    maria_db_parameters: Optional[MariaDbParameters] = None
    oracle_parameters: Optional[OracleParameters] = None
    presto_parameters: Optional[PrestoParameters] = None
    starburst_parameters: Optional[StarburstParameters] = None
    redshift_parameters: Optional[RedshiftParameters] = None
    my_sql_parameters: Optional[MySqlParameters] = None
    sql_server_parameters: Optional[SqlServerParameters] = None
    snowflake_parameters: Optional[SnowflakeParameters] = None
    amazon_elasticsearch_parameters: Optional[AmazonElasticsearchParameters] = None
    amazon_open_search_parameters: Optional[AmazonOpenSearchParameters] = None
    postgre_sql_parameters: Optional[PostgreSqlParameters] = None
    aurora_parameters: Optional[AuroraParameters] = None
    s3_parameters: Optional[S3Parameters] = None
    trino_parameters: Optional[TrinoParameters] = None
    databricks_parameters: Optional[DatabricksParameters] = None


@dataclass
class DatabricksParameters(PropertyType):
    PORT = "Port"
    HOST = "Host"
    SQL_ENDPOINT_PATH = "SqlEndpointPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "host": "Host",
        "sql_endpoint_path": "SqlEndpointPath",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql_endpoint_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdentityCenterConfiguration(PropertyType):
    ENABLE_IDENTITY_PROPAGATION = "EnableIdentityPropagation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_identity_propagation": "EnableIdentityPropagation",
    }

    enable_identity_propagation: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ManifestFileLocation(PropertyType):
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MariaDbParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MySqlParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuthParameters(PropertyType):
    TOKEN_PROVIDER_URL = "TokenProviderUrl"
    O_AUTH_SCOPE = "OAuthScope"
    IDENTITY_PROVIDER_VPC_CONNECTION_PROPERTIES = "IdentityProviderVpcConnectionProperties"
    IDENTITY_PROVIDER_RESOURCE_URI = "IdentityProviderResourceUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "token_provider_url": "TokenProviderUrl",
        "o_auth_scope": "OAuthScope",
        "identity_provider_vpc_connection_properties": "IdentityProviderVpcConnectionProperties",
        "identity_provider_resource_uri": "IdentityProviderResourceUri",
    }

    token_provider_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identity_provider_vpc_connection_properties: Optional[VpcConnectionProperties] = None
    identity_provider_resource_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OracleParameters(PropertyType):
    USE_SERVICE_NAME = "UseServiceName"
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "use_service_name": "UseServiceName",
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    use_service_name: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PostgreSqlParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrestoParameters(PropertyType):
    PORT = "Port"
    HOST = "Host"
    CATALOG = "Catalog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "host": "Host",
        "catalog": "Catalog",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsParameters(PropertyType):
    INSTANCE_ID = "InstanceId"
    DATABASE = "Database"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_id": "InstanceId",
        "database": "Database",
    }

    instance_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftIAMParameters(PropertyType):
    AUTO_CREATE_DATABASE_USER = "AutoCreateDatabaseUser"
    DATABASE_USER = "DatabaseUser"
    ROLE_ARN = "RoleArn"
    DATABASE_GROUPS = "DatabaseGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_create_database_user": "AutoCreateDatabaseUser",
        "database_user": "DatabaseUser",
        "role_arn": "RoleArn",
        "database_groups": "DatabaseGroups",
    }

    auto_create_database_user: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    database_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_groups: Optional[Union[list[str], Ref]] = None


@dataclass
class RedshiftParameters(PropertyType):
    IAM_PARAMETERS = "IAMParameters"
    CLUSTER_ID = "ClusterId"
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"
    IDENTITY_CENTER_CONFIGURATION = "IdentityCenterConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_parameters": "IAMParameters",
        "cluster_id": "ClusterId",
        "port": "Port",
        "database": "Database",
        "host": "Host",
        "identity_center_configuration": "IdentityCenterConfiguration",
    }

    iam_parameters: Optional[RedshiftIAMParameters] = None
    cluster_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identity_center_configuration: Optional[IdentityCenterConfiguration] = None


@dataclass
class ResourcePermission(PropertyType):
    ACTIONS = "Actions"
    RESOURCE = "Resource"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "resource": "Resource",
        "principal": "Principal",
    }

    actions: Optional[Union[list[str], Ref]] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Parameters(PropertyType):
    MANIFEST_FILE_LOCATION = "ManifestFileLocation"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "manifest_file_location": "ManifestFileLocation",
        "role_arn": "RoleArn",
    }

    manifest_file_location: Optional[ManifestFileLocation] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeParameters(PropertyType):
    WAREHOUSE = "Warehouse"
    DATABASE_ACCESS_CONTROL_ROLE = "DatabaseAccessControlRole"
    DATABASE = "Database"
    O_AUTH_PARAMETERS = "OAuthParameters"
    HOST = "Host"
    AUTHENTICATION_TYPE = "AuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "warehouse": "Warehouse",
        "database_access_control_role": "DatabaseAccessControlRole",
        "database": "Database",
        "o_auth_parameters": "OAuthParameters",
        "host": "Host",
        "authentication_type": "AuthenticationType",
    }

    warehouse: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_access_control_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth_parameters: Optional[OAuthParameters] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authentication_type: Optional[Union[str, AuthenticationType, Ref, GetAtt, Sub]] = None


@dataclass
class SparkParameters(PropertyType):
    PORT = "Port"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SqlServerParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SslProperties(PropertyType):
    DISABLE_SSL = "DisableSsl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disable_ssl": "DisableSsl",
    }

    disable_ssl: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class StarburstParameters(PropertyType):
    PORT = "Port"
    DATABASE_ACCESS_CONTROL_ROLE = "DatabaseAccessControlRole"
    PRODUCT_TYPE = "ProductType"
    O_AUTH_PARAMETERS = "OAuthParameters"
    HOST = "Host"
    CATALOG = "Catalog"
    AUTHENTICATION_TYPE = "AuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database_access_control_role": "DatabaseAccessControlRole",
        "product_type": "ProductType",
        "o_auth_parameters": "OAuthParameters",
        "host": "Host",
        "catalog": "Catalog",
        "authentication_type": "AuthenticationType",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database_access_control_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    product_type: Optional[Union[str, StarburstProductType, Ref, GetAtt, Sub]] = None
    o_auth_parameters: Optional[OAuthParameters] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authentication_type: Optional[Union[str, AuthenticationType, Ref, GetAtt, Sub]] = None


@dataclass
class TeradataParameters(PropertyType):
    PORT = "Port"
    DATABASE = "Database"
    HOST = "Host"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "database": "Database",
        "host": "Host",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrinoParameters(PropertyType):
    PORT = "Port"
    HOST = "Host"
    CATALOG = "Catalog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "host": "Host",
        "catalog": "Catalog",
    }

    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectionProperties(PropertyType):
    VPC_CONNECTION_ARN = "VpcConnectionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_connection_arn": "VpcConnectionArn",
    }

    vpc_connection_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

