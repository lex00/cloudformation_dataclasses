"""PropertyTypes for AWS::Events::Connection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApiKeyAuthParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "api_key_value": "ApiKeyValue",
        "api_key_name": "ApiKeyName",
    }

    api_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "invocation_http_parameters": "InvocationHttpParameters",
        "connectivity_parameters": "ConnectivityParameters",
        "basic_auth_parameters": "BasicAuthParameters",
        "api_key_auth_parameters": "ApiKeyAuthParameters",
        "o_auth_parameters": "OAuthParameters",
    }

    invocation_http_parameters: Optional[ConnectionHttpParameters] = None
    connectivity_parameters: Optional[ConnectivityParameters] = None
    basic_auth_parameters: Optional[BasicAuthParameters] = None
    api_key_auth_parameters: Optional[ApiKeyAuthParameters] = None
    o_auth_parameters: Optional[OAuthParameters] = None


@dataclass
class BasicAuthParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClientParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "client_id": "ClientID",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionHttpParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header_parameters": "HeaderParameters",
        "query_string_parameters": "QueryStringParameters",
        "body_parameters": "BodyParameters",
    }

    header_parameters: Optional[list[Parameter]] = None
    query_string_parameters: Optional[list[Parameter]] = None
    body_parameters: Optional[list[Parameter]] = None


@dataclass
class ConnectivityParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_parameters": "ResourceParameters",
    }

    resource_parameters: Optional[ResourceParameters] = None


@dataclass
class InvocationConnectivityParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_parameters": "ResourceParameters",
    }

    resource_parameters: Optional[ResourceParameters] = None


@dataclass
class OAuthParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_parameters": "ClientParameters",
        "o_auth_http_parameters": "OAuthHttpParameters",
        "authorization_endpoint": "AuthorizationEndpoint",
        "http_method": "HttpMethod",
    }

    client_parameters: Optional[ClientParameters] = None
    o_auth_http_parameters: Optional[ConnectionHttpParameters] = None
    authorization_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_method: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Parameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "is_value_secret": "IsValueSecret",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_value_secret: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_association_arn": "ResourceAssociationArn",
        "resource_configuration_arn": "ResourceConfigurationArn",
    }

    resource_association_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

