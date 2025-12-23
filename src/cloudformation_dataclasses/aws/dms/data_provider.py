"""PropertyTypes for AWS::DMS::DataProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

