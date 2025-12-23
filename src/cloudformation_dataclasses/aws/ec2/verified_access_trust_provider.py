"""PropertyTypes for AWS::EC2::VerifiedAccessTrustProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeviceOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tenant_id": "TenantId",
        "public_signing_key_url": "PublicSigningKeyUrl",
    }

    tenant_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    public_signing_key_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NativeApplicationOidcOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "token_endpoint": "TokenEndpoint",
        "scope": "Scope",
        "issuer": "Issuer",
        "client_secret": "ClientSecret",
        "user_info_endpoint": "UserInfoEndpoint",
        "client_id": "ClientId",
        "authorization_endpoint": "AuthorizationEndpoint",
        "public_signing_key_endpoint": "PublicSigningKeyEndpoint",
    }

    token_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_info_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    public_signing_key_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OidcOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "token_endpoint": "TokenEndpoint",
        "scope": "Scope",
        "issuer": "Issuer",
        "client_secret": "ClientSecret",
        "user_info_endpoint": "UserInfoEndpoint",
        "client_id": "ClientId",
        "authorization_endpoint": "AuthorizationEndpoint",
    }

    token_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_info_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SseSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_key_enabled": "CustomerManagedKeyEnabled",
        "kms_key_arn": "KmsKeyArn",
    }

    customer_managed_key_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

