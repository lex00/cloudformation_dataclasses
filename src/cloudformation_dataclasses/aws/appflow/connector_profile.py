"""PropertyTypes for AWS::AppFlow::ConnectorProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmplitudeConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_key": "SecretKey",
        "api_key": "ApiKey",
    }

    secret_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApiKeyCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "api_secret_key": "ApiSecretKey",
        "api_key": "ApiKey",
    }

    api_secret_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorOAuthRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_code": "AuthCode",
        "redirect_uri": "RedirectUri",
    }

    auth_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorProfileConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_profile_credentials": "ConnectorProfileCredentials",
        "connector_profile_properties": "ConnectorProfileProperties",
    }

    connector_profile_credentials: Optional[ConnectorProfileCredentials] = None
    connector_profile_properties: Optional[ConnectorProfileProperties] = None


@dataclass
class ConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "amplitude": "Amplitude",
        "google_analytics": "GoogleAnalytics",
        "service_now": "ServiceNow",
        "custom_connector": "CustomConnector",
        "sapo_data": "SAPOData",
        "pardot": "Pardot",
        "veeva": "Veeva",
        "trendmicro": "Trendmicro",
        "datadog": "Datadog",
        "marketo": "Marketo",
        "redshift": "Redshift",
        "singular": "Singular",
        "slack": "Slack",
        "snowflake": "Snowflake",
        "dynatrace": "Dynatrace",
        "zendesk": "Zendesk",
        "infor_nexus": "InforNexus",
        "salesforce": "Salesforce",
    }

    amplitude: Optional[AmplitudeConnectorProfileCredentials] = None
    google_analytics: Optional[GoogleAnalyticsConnectorProfileCredentials] = None
    service_now: Optional[ServiceNowConnectorProfileCredentials] = None
    custom_connector: Optional[CustomConnectorProfileCredentials] = None
    sapo_data: Optional[SAPODataConnectorProfileCredentials] = None
    pardot: Optional[PardotConnectorProfileCredentials] = None
    veeva: Optional[VeevaConnectorProfileCredentials] = None
    trendmicro: Optional[TrendmicroConnectorProfileCredentials] = None
    datadog: Optional[DatadogConnectorProfileCredentials] = None
    marketo: Optional[MarketoConnectorProfileCredentials] = None
    redshift: Optional[RedshiftConnectorProfileCredentials] = None
    singular: Optional[SingularConnectorProfileCredentials] = None
    slack: Optional[SlackConnectorProfileCredentials] = None
    snowflake: Optional[SnowflakeConnectorProfileCredentials] = None
    dynatrace: Optional[DynatraceConnectorProfileCredentials] = None
    zendesk: Optional[ZendeskConnectorProfileCredentials] = None
    infor_nexus: Optional[InforNexusConnectorProfileCredentials] = None
    salesforce: Optional[SalesforceConnectorProfileCredentials] = None


@dataclass
class ConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_now": "ServiceNow",
        "custom_connector": "CustomConnector",
        "sapo_data": "SAPOData",
        "pardot": "Pardot",
        "veeva": "Veeva",
        "datadog": "Datadog",
        "marketo": "Marketo",
        "redshift": "Redshift",
        "slack": "Slack",
        "snowflake": "Snowflake",
        "dynatrace": "Dynatrace",
        "zendesk": "Zendesk",
        "infor_nexus": "InforNexus",
        "salesforce": "Salesforce",
    }

    service_now: Optional[ServiceNowConnectorProfileProperties] = None
    custom_connector: Optional[CustomConnectorProfileProperties] = None
    sapo_data: Optional[SAPODataConnectorProfileProperties] = None
    pardot: Optional[PardotConnectorProfileProperties] = None
    veeva: Optional[VeevaConnectorProfileProperties] = None
    datadog: Optional[DatadogConnectorProfileProperties] = None
    marketo: Optional[MarketoConnectorProfileProperties] = None
    redshift: Optional[RedshiftConnectorProfileProperties] = None
    slack: Optional[SlackConnectorProfileProperties] = None
    snowflake: Optional[SnowflakeConnectorProfileProperties] = None
    dynatrace: Optional[DynatraceConnectorProfileProperties] = None
    zendesk: Optional[ZendeskConnectorProfileProperties] = None
    infor_nexus: Optional[InforNexusConnectorProfileProperties] = None
    salesforce: Optional[SalesforceConnectorProfileProperties] = None


@dataclass
class CustomAuthCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "credentials_map": "CredentialsMap",
        "custom_authentication_type": "CustomAuthenticationType",
    }

    credentials_map: Optional[dict[str, str]] = None
    custom_authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "basic": "Basic",
        "api_key": "ApiKey",
        "oauth2": "Oauth2",
        "custom": "Custom",
        "authentication_type": "AuthenticationType",
    }

    basic: Optional[BasicAuthCredentials] = None
    api_key: Optional[ApiKeyCredentials] = None
    oauth2: Optional[OAuth2Credentials] = None
    custom: Optional[CustomAuthCredentials] = None
    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "o_auth2_properties": "OAuth2Properties",
        "profile_properties": "ProfileProperties",
    }

    o_auth2_properties: Optional[OAuth2Properties] = None
    profile_properties: Optional[dict[str, str]] = None


@dataclass
class DatadogConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_key": "ApplicationKey",
        "api_key": "ApiKey",
    }

    application_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatadogConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynatraceConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "api_token": "ApiToken",
    }

    api_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynatraceConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GoogleAnalyticsConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_token": "RefreshToken",
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class InforNexusConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_key_id": "AccessKeyId",
        "user_id": "UserId",
        "secret_access_key": "SecretAccessKey",
        "datakey": "Datakey",
    }

    access_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_access_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    datakey: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InforNexusConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MarketoConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class MarketoConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Credentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "o_auth_request": "OAuthRequest",
        "refresh_token": "RefreshToken",
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
    }

    o_auth_request: Optional[ConnectorOAuthRequest] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Properties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "token_url_custom_properties": "TokenUrlCustomProperties",
        "token_url": "TokenUrl",
        "o_auth2_grant_type": "OAuth2GrantType",
    }

    token_url_custom_properties: Optional[dict[str, str]] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_grant_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuthCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
        "client_secret": "ClientSecret",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class OAuthProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_code_url": "AuthCodeUrl",
        "token_url": "TokenUrl",
        "o_auth_scopes": "OAuthScopes",
    }

    auth_code_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth_scopes: Optional[Union[list[str], Ref]] = None


@dataclass
class PardotConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
        "client_credentials_arn": "ClientCredentialsArn",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_credentials_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class PardotConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
        "is_sandbox_environment": "IsSandboxEnvironment",
        "business_unit_id": "BusinessUnitId",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_sandbox_environment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    business_unit_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_url": "DatabaseUrl",
        "bucket_name": "BucketName",
        "is_redshift_serverless": "IsRedshiftServerless",
        "data_api_role_arn": "DataApiRoleArn",
        "database_name": "DatabaseName",
        "workgroup_name": "WorkgroupName",
        "bucket_prefix": "BucketPrefix",
        "cluster_identifier": "ClusterIdentifier",
        "role_arn": "RoleArn",
    }

    database_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_redshift_serverless: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_api_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SAPODataConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "basic_auth_credentials": "BasicAuthCredentials",
        "o_auth_credentials": "OAuthCredentials",
    }

    basic_auth_credentials: Optional[BasicAuthCredentials] = None
    o_auth_credentials: Optional[OAuthCredentials] = None


@dataclass
class SAPODataConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_service_path": "ApplicationServicePath",
        "application_host_url": "ApplicationHostUrl",
        "o_auth_properties": "OAuthProperties",
        "disable_sso": "DisableSSO",
        "logon_language": "LogonLanguage",
        "private_link_service_name": "PrivateLinkServiceName",
        "port_number": "PortNumber",
        "client_number": "ClientNumber",
    }

    application_service_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_host_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth_properties: Optional[OAuthProperties] = None
    disable_sso: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    logon_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_link_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    client_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jwt_token": "JwtToken",
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
        "client_credentials_arn": "ClientCredentialsArn",
        "connector_o_auth_request": "ConnectorOAuthRequest",
        "o_auth2_grant_type": "OAuth2GrantType",
    }

    jwt_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_credentials_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None
    o_auth2_grant_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
        "is_sandbox_environment": "isSandboxEnvironment",
        "use_private_link_for_metadata_and_authorization": "usePrivateLinkForMetadataAndAuthorization",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_sandbox_environment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_private_link_for_metadata_and_authorization: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNowConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "o_auth2_credentials": "OAuth2Credentials",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_credentials: Optional[OAuth2Credentials] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNowConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingularConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "api_key": "ApiKey",
    }

    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlackConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class SlackConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "warehouse": "Warehouse",
        "bucket_name": "BucketName",
        "private_link_service_name": "PrivateLinkServiceName",
        "stage": "Stage",
        "region": "Region",
        "bucket_prefix": "BucketPrefix",
        "account_name": "AccountName",
    }

    warehouse: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_link_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrendmicroConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "api_secret_key": "ApiSecretKey",
    }

    api_secret_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VeevaConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VeevaConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ZendeskConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class ZendeskConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

