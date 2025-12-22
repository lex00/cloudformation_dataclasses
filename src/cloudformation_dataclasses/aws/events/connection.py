"""PropertyTypes for AWS::Events::Connection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApiDestinationHttpMethod:
    """ApiDestinationHttpMethod enum values."""

    POST = "POST"
    GET = "GET"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ApiDestinationState:
    """ApiDestinationState enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ArchiveState:
    """ArchiveState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"


class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ConnectionAuthorizationType:
    """ConnectionAuthorizationType enum values."""

    BASIC = "BASIC"
    OAUTH_CLIENT_CREDENTIALS = "OAUTH_CLIENT_CREDENTIALS"
    API_KEY = "API_KEY"


class ConnectionOAuthHttpMethod:
    """ConnectionOAuthHttpMethod enum values."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class ConnectionState:
    """ConnectionState enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    AUTHORIZED = "AUTHORIZED"
    DEAUTHORIZED = "DEAUTHORIZED"
    AUTHORIZING = "AUTHORIZING"
    DEAUTHORIZING = "DEAUTHORIZING"
    ACTIVE = "ACTIVE"
    FAILED_CONNECTIVITY = "FAILED_CONNECTIVITY"


class EndpointState:
    """EndpointState enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


class EventSourceState:
    """EventSourceState enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class IncludeDetail:
    """IncludeDetail enum values."""

    NONE = "NONE"
    FULL = "FULL"


class LaunchType:
    """LaunchType enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class Level:
    """Level enum values."""

    OFF = "OFF"
    ERROR = "ERROR"
    INFO = "INFO"
    TRACE = "TRACE"


class PlacementConstraintType:
    """PlacementConstraintType enum values."""

    DISTINCTINSTANCE = "distinctInstance"
    MEMBEROF = "memberOf"


class PlacementStrategyType:
    """PlacementStrategyType enum values."""

    RANDOM = "random"
    SPREAD = "spread"
    BINPACK = "binpack"


class PropagateTags:
    """PropagateTags enum values."""

    TASK_DEFINITION = "TASK_DEFINITION"


class ReplayState:
    """ReplayState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    CANCELLING = "CANCELLING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class ReplicationState:
    """ReplicationState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RuleState:
    """RuleState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS = "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS"


@dataclass
class ApiKeyAuthParameters(PropertyType):
    API_KEY_VALUE = "ApiKeyValue"
    API_KEY_NAME = "ApiKeyName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "api_key_value": "ApiKeyValue",
        "api_key_name": "ApiKeyName",
    }

    api_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthParameters(PropertyType):
    INVOCATION_HTTP_PARAMETERS = "InvocationHttpParameters"
    CONNECTIVITY_PARAMETERS = "ConnectivityParameters"
    BASIC_AUTH_PARAMETERS = "BasicAuthParameters"
    API_KEY_AUTH_PARAMETERS = "ApiKeyAuthParameters"
    O_AUTH_PARAMETERS = "OAuthParameters"

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
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClientParameters(PropertyType):
    CLIENT_SECRET = "ClientSecret"
    CLIENT_ID = "ClientID"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "client_id": "ClientID",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionHttpParameters(PropertyType):
    HEADER_PARAMETERS = "HeaderParameters"
    QUERY_STRING_PARAMETERS = "QueryStringParameters"
    BODY_PARAMETERS = "BodyParameters"

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
    RESOURCE_PARAMETERS = "ResourceParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_parameters": "ResourceParameters",
    }

    resource_parameters: Optional[ResourceParameters] = None


@dataclass
class InvocationConnectivityParameters(PropertyType):
    RESOURCE_PARAMETERS = "ResourceParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_parameters": "ResourceParameters",
    }

    resource_parameters: Optional[ResourceParameters] = None


@dataclass
class OAuthParameters(PropertyType):
    CLIENT_PARAMETERS = "ClientParameters"
    O_AUTH_HTTP_PARAMETERS = "OAuthHttpParameters"
    AUTHORIZATION_ENDPOINT = "AuthorizationEndpoint"
    HTTP_METHOD = "HttpMethod"

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
    VALUE = "Value"
    IS_VALUE_SECRET = "IsValueSecret"
    KEY = "Key"

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
    RESOURCE_ASSOCIATION_ARN = "ResourceAssociationArn"
    RESOURCE_CONFIGURATION_ARN = "ResourceConfigurationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_association_arn": "ResourceAssociationArn",
        "resource_configuration_arn": "ResourceConfigurationArn",
    }

    resource_association_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

