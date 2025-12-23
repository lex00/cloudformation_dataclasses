"""PropertyTypes for AWS::Glue::Connection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthenticationConfigurationInput(PropertyType):
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
    o_auth2_properties: Optional[OAuth2PropertiesInput] = None
    custom_authentication_credentials: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    basic_authentication_credentials: Optional[BasicAuthenticationCredentials] = None
    authentication_type: Optional[Union[str, AuthenticationType, Ref, GetAtt, Sub]] = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_code": "AuthorizationCode",
        "redirect_uri": "RedirectUri",
    }

    authorization_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_configuration": "AuthenticationConfiguration",
        "python_properties": "PythonProperties",
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

    authentication_configuration: Optional[AuthenticationConfigurationInput] = None
    python_properties: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    spark_properties: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_type: Optional[Union[str, ConnectionType, Ref, GetAtt, Sub]] = None
    match_criteria: Optional[Union[list[str], Ref]] = None
    physical_connection_requirements: Optional[PhysicalConnectionRequirements] = None
    connection_properties: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    athena_properties: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    validate_for_compute_environments: Optional[Union[list[str], Ref]] = None
    validate_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2ClientApplication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
        "user_managed_client_application_client_id": "UserManagedClientApplicationClientId",
    }

    aws_managed_client_application_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_managed_client_application_client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Credentials(PropertyType):
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
class OAuth2PropertiesInput(PropertyType):
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
    o_auth2_credentials: Optional[OAuth2Credentials] = None
    o_auth2_grant_type: Optional[Union[str, OAuth2GrantType, Ref, GetAtt, Sub]] = None
    token_url_parameters_map: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone": "AvailabilityZone",
        "security_group_id_list": "SecurityGroupIdList",
        "subnet_id": "SubnetId",
    }

    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_id_list: Optional[Union[list[str], Ref]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

