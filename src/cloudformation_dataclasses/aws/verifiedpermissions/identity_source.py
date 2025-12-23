"""PropertyTypes for AWS::VerifiedPermissions::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CognitoGroupConfiguration(PropertyType):
    GROUP_ENTITY_TYPE = "GroupEntityType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_entity_type": "GroupEntityType",
    }

    group_entity_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CognitoUserPoolConfiguration(PropertyType):
    USER_POOL_ARN = "UserPoolArn"
    GROUP_CONFIGURATION = "GroupConfiguration"
    CLIENT_IDS = "ClientIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_pool_arn": "UserPoolArn",
        "group_configuration": "GroupConfiguration",
        "client_ids": "ClientIds",
    }

    user_pool_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_configuration: Optional[CognitoGroupConfiguration] = None
    client_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class IdentitySourceConfiguration(PropertyType):
    COGNITO_USER_POOL_CONFIGURATION = "CognitoUserPoolConfiguration"
    OPEN_ID_CONNECT_CONFIGURATION = "OpenIdConnectConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cognito_user_pool_configuration": "CognitoUserPoolConfiguration",
        "open_id_connect_configuration": "OpenIdConnectConfiguration",
    }

    cognito_user_pool_configuration: Optional[CognitoUserPoolConfiguration] = None
    open_id_connect_configuration: Optional[OpenIdConnectConfiguration] = None


@dataclass
class OpenIdConnectAccessTokenConfiguration(PropertyType):
    AUDIENCES = "Audiences"
    PRINCIPAL_ID_CLAIM = "PrincipalIdClaim"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audiences": "Audiences",
        "principal_id_claim": "PrincipalIdClaim",
    }

    audiences: Optional[Union[list[str], Ref]] = None
    principal_id_claim: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenIdConnectConfiguration(PropertyType):
    ISSUER = "Issuer"
    TOKEN_SELECTION = "TokenSelection"
    GROUP_CONFIGURATION = "GroupConfiguration"
    ENTITY_ID_PREFIX = "EntityIdPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "issuer": "Issuer",
        "token_selection": "TokenSelection",
        "group_configuration": "GroupConfiguration",
        "entity_id_prefix": "EntityIdPrefix",
    }

    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_selection: Optional[OpenIdConnectTokenSelection] = None
    group_configuration: Optional[OpenIdConnectGroupConfiguration] = None
    entity_id_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenIdConnectGroupConfiguration(PropertyType):
    GROUP_ENTITY_TYPE = "GroupEntityType"
    GROUP_CLAIM = "GroupClaim"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_entity_type": "GroupEntityType",
        "group_claim": "GroupClaim",
    }

    group_entity_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_claim: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenIdConnectIdentityTokenConfiguration(PropertyType):
    CLIENT_IDS = "ClientIds"
    PRINCIPAL_ID_CLAIM = "PrincipalIdClaim"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_ids": "ClientIds",
        "principal_id_claim": "PrincipalIdClaim",
    }

    client_ids: Optional[Union[list[str], Ref]] = None
    principal_id_claim: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenIdConnectTokenSelection(PropertyType):
    ACCESS_TOKEN_ONLY = "AccessTokenOnly"
    IDENTITY_TOKEN_ONLY = "IdentityTokenOnly"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_token_only": "AccessTokenOnly",
        "identity_token_only": "IdentityTokenOnly",
    }

    access_token_only: Optional[OpenIdConnectAccessTokenConfiguration] = None
    identity_token_only: Optional[OpenIdConnectIdentityTokenConfiguration] = None

