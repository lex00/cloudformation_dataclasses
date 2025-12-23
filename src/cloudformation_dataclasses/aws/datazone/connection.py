"""PropertyTypes for AWS::DataZone::Connection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmazonQPropertiesInput(PropertyType):
    IS_ENABLED = "IsEnabled"
    PROFILE_ARN = "ProfileArn"
    AUTH_MODE = "AuthMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
        "profile_arn": "ProfileArn",
        "auth_mode": "AuthMode",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AthenaPropertiesInput(PropertyType):
    WORKGROUP_NAME = "WorkgroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_name": "WorkgroupName",
    }

    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthenticationConfigurationInput(PropertyType):
    SECRET_ARN = "SecretArn"
    KMS_KEY_ARN = "KmsKeyArn"
    O_AUTH2_PROPERTIES = "OAuth2Properties"
    CUSTOM_AUTHENTICATION_CREDENTIALS = "CustomAuthenticationCredentials"
    BASIC_AUTHENTICATION_CREDENTIALS = "BasicAuthenticationCredentials"
    AUTHENTICATION_TYPE = "AuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "kms_key_arn": "KmsKeyArn",
        "o_auth2_properties": "OAuth2Properties",
        "custom_authentication_credentials": "CustomAuthenticationCredentials",
        "basic_authentication_credentials": "BasicAuthenticationCredentials",
        "authentication_type": "AuthenticationType",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_properties: Optional[OAuth2Properties] = None
    custom_authentication_credentials: Optional[dict[str, str]] = None
    basic_authentication_credentials: Optional[BasicAuthenticationCredentials] = None
    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    AUTHORIZATION_CODE = "AuthorizationCode"
    REDIRECT_URI = "RedirectUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_code": "AuthorizationCode",
        "redirect_uri": "RedirectUri",
    }

    authorization_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsLocation(PropertyType):
    AWS_REGION = "AwsRegion"
    ACCESS_ROLE = "AccessRole"
    AWS_ACCOUNT_ID = "AwsAccountId"
    IAM_CONNECTION_ID = "IamConnectionId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AwsRegion",
        "access_role": "AccessRole",
        "aws_account_id": "AwsAccountId",
        "iam_connection_id": "IamConnectionId",
    }

    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_connection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    USER_NAME = "UserName"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_name": "UserName",
        "password": "Password",
    }

    user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionPropertiesInput(PropertyType):
    AMAZON_Q_PROPERTIES = "AmazonQProperties"
    IAM_PROPERTIES = "IamProperties"
    S3_PROPERTIES = "S3Properties"
    SPARK_EMR_PROPERTIES = "SparkEmrProperties"
    HYPER_POD_PROPERTIES = "HyperPodProperties"
    SPARK_GLUE_PROPERTIES = "SparkGlueProperties"
    MLFLOW_PROPERTIES = "MlflowProperties"
    ATHENA_PROPERTIES = "AthenaProperties"
    GLUE_PROPERTIES = "GlueProperties"
    REDSHIFT_PROPERTIES = "RedshiftProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amazon_q_properties": "AmazonQProperties",
        "iam_properties": "IamProperties",
        "s3_properties": "S3Properties",
        "spark_emr_properties": "SparkEmrProperties",
        "hyper_pod_properties": "HyperPodProperties",
        "spark_glue_properties": "SparkGlueProperties",
        "mlflow_properties": "MlflowProperties",
        "athena_properties": "AthenaProperties",
        "glue_properties": "GlueProperties",
        "redshift_properties": "RedshiftProperties",
    }

    amazon_q_properties: Optional[AmazonQPropertiesInput] = None
    iam_properties: Optional[IamPropertiesInput] = None
    s3_properties: Optional[S3PropertiesInput] = None
    spark_emr_properties: Optional[SparkEmrPropertiesInput] = None
    hyper_pod_properties: Optional[HyperPodPropertiesInput] = None
    spark_glue_properties: Optional[SparkGluePropertiesInput] = None
    mlflow_properties: Optional[MlflowPropertiesInput] = None
    athena_properties: Optional[AthenaPropertiesInput] = None
    glue_properties: Optional[GluePropertiesInput] = None
    redshift_properties: Optional[RedshiftPropertiesInput] = None


@dataclass
class GlueConnectionInput(PropertyType):
    PYTHON_PROPERTIES = "PythonProperties"
    AUTHENTICATION_CONFIGURATION = "AuthenticationConfiguration"
    SPARK_PROPERTIES = "SparkProperties"
    DESCRIPTION = "Description"
    CONNECTION_TYPE = "ConnectionType"
    MATCH_CRITERIA = "MatchCriteria"
    PHYSICAL_CONNECTION_REQUIREMENTS = "PhysicalConnectionRequirements"
    CONNECTION_PROPERTIES = "ConnectionProperties"
    ATHENA_PROPERTIES = "AthenaProperties"
    VALIDATE_FOR_COMPUTE_ENVIRONMENTS = "ValidateForComputeEnvironments"
    VALIDATE_CREDENTIALS = "ValidateCredentials"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "python_properties": "PythonProperties",
        "authentication_configuration": "AuthenticationConfiguration",
        "spark_properties": "SparkProperties",
        "description": "Description",
        "connection_type": "ConnectionType",
        "match_criteria": "MatchCriteria",
        "physical_connection_requirements": "PhysicalConnectionRequirements",
        "connection_properties": "ConnectionProperties",
        "athena_properties": "AthenaProperties",
        "validate_for_compute_environments": "ValidateForComputeEnvironments",
        "validate_credentials": "ValidateCredentials",
        "name": "Name",
    }

    python_properties: Optional[dict[str, str]] = None
    authentication_configuration: Optional[AuthenticationConfigurationInput] = None
    spark_properties: Optional[dict[str, str]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None
    physical_connection_requirements: Optional[PhysicalConnectionRequirements] = None
    connection_properties: Optional[dict[str, str]] = None
    athena_properties: Optional[dict[str, str]] = None
    validate_for_compute_environments: Optional[Union[list[str], Ref]] = None
    validate_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GlueOAuth2Credentials(PropertyType):
    USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET = "UserManagedClientApplicationClientSecret"
    JWT_TOKEN = "JwtToken"
    REFRESH_TOKEN = "RefreshToken"
    ACCESS_TOKEN = "AccessToken"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_managed_client_application_client_secret": "UserManagedClientApplicationClientSecret",
        "jwt_token": "JwtToken",
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
    }

    user_managed_client_application_client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    jwt_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GluePropertiesInput(PropertyType):
    GLUE_CONNECTION_INPUT = "GlueConnectionInput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_connection_input": "GlueConnectionInput",
    }

    glue_connection_input: Optional[GlueConnectionInput] = None


@dataclass
class HyperPodPropertiesInput(PropertyType):
    CLUSTER_NAME = "ClusterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_name": "ClusterName",
    }

    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamPropertiesInput(PropertyType):
    GLUE_LINEAGE_SYNC_ENABLED = "GlueLineageSyncEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_lineage_sync_enabled": "GlueLineageSyncEnabled",
    }

    glue_lineage_sync_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LineageSyncSchedule(PropertyType):
    SCHEDULE = "Schedule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule": "Schedule",
    }

    schedule: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MlflowPropertiesInput(PropertyType):
    TRACKING_SERVER_ARN = "TrackingServerArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tracking_server_arn": "TrackingServerArn",
    }

    tracking_server_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2ClientApplication(PropertyType):
    AWS_MANAGED_CLIENT_APPLICATION_REFERENCE = "AWSManagedClientApplicationReference"
    USER_MANAGED_CLIENT_APPLICATION_CLIENT_ID = "UserManagedClientApplicationClientId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
        "user_managed_client_application_client_id": "UserManagedClientApplicationClientId",
    }

    aws_managed_client_application_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_managed_client_application_client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Properties(PropertyType):
    AUTHORIZATION_CODE_PROPERTIES = "AuthorizationCodeProperties"
    O_AUTH2_CLIENT_APPLICATION = "OAuth2ClientApplication"
    TOKEN_URL = "TokenUrl"
    O_AUTH2_CREDENTIALS = "OAuth2Credentials"
    O_AUTH2_GRANT_TYPE = "OAuth2GrantType"
    TOKEN_URL_PARAMETERS_MAP = "TokenUrlParametersMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_code_properties": "AuthorizationCodeProperties",
        "o_auth2_client_application": "OAuth2ClientApplication",
        "token_url": "TokenUrl",
        "o_auth2_credentials": "OAuth2Credentials",
        "o_auth2_grant_type": "OAuth2GrantType",
        "token_url_parameters_map": "TokenUrlParametersMap",
    }

    authorization_code_properties: Optional[AuthorizationCodeProperties] = None
    o_auth2_client_application: Optional[OAuth2ClientApplication] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_credentials: Optional[GlueOAuth2Credentials] = None
    o_auth2_grant_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_url_parameters_map: Optional[dict[str, str]] = None


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    SUBNET_ID_LIST = "SubnetIdList"
    AVAILABILITY_ZONE = "AvailabilityZone"
    SECURITY_GROUP_ID_LIST = "SecurityGroupIdList"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_id_list": "SubnetIdList",
        "availability_zone": "AvailabilityZone",
        "security_group_id_list": "SecurityGroupIdList",
        "subnet_id": "SubnetId",
    }

    subnet_id_list: Optional[Union[list[str], Ref]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_id_list: Optional[Union[list[str], Ref]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftCredentials(PropertyType):
    SECRET_ARN = "SecretArn"
    USERNAME_PASSWORD = "UsernamePassword"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "username_password": "UsernamePassword",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password: Optional[UsernamePassword] = None


@dataclass
class RedshiftLineageSyncConfigurationInput(PropertyType):
    SCHEDULE = "Schedule"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule": "Schedule",
        "enabled": "Enabled",
    }

    schedule: Optional[LineageSyncSchedule] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftPropertiesInput(PropertyType):
    STORAGE = "Storage"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    HOST = "Host"
    CREDENTIALS = "Credentials"
    LINEAGE_SYNC = "LineageSync"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage": "Storage",
        "port": "Port",
        "database_name": "DatabaseName",
        "host": "Host",
        "credentials": "Credentials",
        "lineage_sync": "LineageSync",
    }

    storage: Optional[RedshiftStorageProperties] = None
    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials: Optional[RedshiftCredentials] = None
    lineage_sync: Optional[RedshiftLineageSyncConfigurationInput] = None


@dataclass
class RedshiftStorageProperties(PropertyType):
    CLUSTER_NAME = "ClusterName"
    WORKGROUP_NAME = "WorkgroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_name": "ClusterName",
        "workgroup_name": "WorkgroupName",
    }

    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3PropertiesInput(PropertyType):
    S3_URI = "S3Uri"
    S3_ACCESS_GRANT_LOCATION_ID = "S3AccessGrantLocationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "s3_access_grant_location_id": "S3AccessGrantLocationId",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_access_grant_location_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SparkEmrPropertiesInput(PropertyType):
    COMPUTE_ARN = "ComputeArn"
    TRUSTED_CERTIFICATES_S3_URI = "TrustedCertificatesS3Uri"
    LOG_URI = "LogUri"
    JAVA_VIRTUAL_ENV = "JavaVirtualEnv"
    PYTHON_VIRTUAL_ENV = "PythonVirtualEnv"
    RUNTIME_ROLE = "RuntimeRole"
    INSTANCE_PROFILE_ARN = "InstanceProfileArn"
    MANAGED_ENDPOINT_ARN = "ManagedEndpointArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_arn": "ComputeArn",
        "trusted_certificates_s3_uri": "TrustedCertificatesS3Uri",
        "log_uri": "LogUri",
        "java_virtual_env": "JavaVirtualEnv",
        "python_virtual_env": "PythonVirtualEnv",
        "runtime_role": "RuntimeRole",
        "instance_profile_arn": "InstanceProfileArn",
        "managed_endpoint_arn": "ManagedEndpointArn",
    }

    compute_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trusted_certificates_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    java_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    python_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_endpoint_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SparkGlueArgs(PropertyType):
    CONNECTION = "Connection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection": "Connection",
    }

    connection: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SparkGluePropertiesInput(PropertyType):
    WORKER_TYPE = "WorkerType"
    ADDITIONAL_ARGS = "AdditionalArgs"
    JAVA_VIRTUAL_ENV = "JavaVirtualEnv"
    GLUE_VERSION = "GlueVersion"
    PYTHON_VIRTUAL_ENV = "PythonVirtualEnv"
    IDLE_TIMEOUT = "IdleTimeout"
    GLUE_CONNECTION_NAME = "GlueConnectionName"
    NUMBER_OF_WORKERS = "NumberOfWorkers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "worker_type": "WorkerType",
        "additional_args": "AdditionalArgs",
        "java_virtual_env": "JavaVirtualEnv",
        "glue_version": "GlueVersion",
        "python_virtual_env": "PythonVirtualEnv",
        "idle_timeout": "IdleTimeout",
        "glue_connection_name": "GlueConnectionName",
        "number_of_workers": "NumberOfWorkers",
    }

    worker_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_args: Optional[SparkGlueArgs] = None
    java_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    glue_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    python_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    idle_timeout: Optional[Union[float, Ref, GetAtt, Sub]] = None
    glue_connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    number_of_workers: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class UsernamePassword(PropertyType):
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None

