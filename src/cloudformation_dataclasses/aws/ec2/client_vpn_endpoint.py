"""PropertyTypes for AWS::EC2::ClientVpnEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CertificateAuthenticationRequest(PropertyType):
    CLIENT_ROOT_CERTIFICATE_CHAIN_ARN = "ClientRootCertificateChainArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_root_certificate_chain_arn": "ClientRootCertificateChainArn",
    }

    client_root_certificate_chain_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClientAuthenticationRequest(PropertyType):
    MUTUAL_AUTHENTICATION = "MutualAuthentication"
    TYPE = "Type"
    FEDERATED_AUTHENTICATION = "FederatedAuthentication"
    ACTIVE_DIRECTORY = "ActiveDirectory"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mutual_authentication": "MutualAuthentication",
        "type_": "Type",
        "federated_authentication": "FederatedAuthentication",
        "active_directory": "ActiveDirectory",
    }

    mutual_authentication: Optional[CertificateAuthenticationRequest] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    federated_authentication: Optional[FederatedAuthenticationRequest] = None
    active_directory: Optional[DirectoryServiceAuthenticationRequest] = None


@dataclass
class ClientConnectOptions(PropertyType):
    LAMBDA_FUNCTION_ARN = "LambdaFunctionArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_function_arn": "LambdaFunctionArn",
        "enabled": "Enabled",
    }

    lambda_function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ClientLoginBannerOptions(PropertyType):
    ENABLED = "Enabled"
    BANNER_TEXT = "BannerText"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "banner_text": "BannerText",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    banner_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClientRouteEnforcementOptions(PropertyType):
    ENFORCED = "Enforced"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enforced": "Enforced",
    }

    enforced: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionLogOptions(PropertyType):
    CLOUDWATCH_LOG_STREAM = "CloudwatchLogStream"
    ENABLED = "Enabled"
    CLOUDWATCH_LOG_GROUP = "CloudwatchLogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloudwatch_log_stream": "CloudwatchLogStream",
        "enabled": "Enabled",
        "cloudwatch_log_group": "CloudwatchLogGroup",
    }

    cloudwatch_log_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloudwatch_log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DirectoryServiceAuthenticationRequest(PropertyType):
    DIRECTORY_ID = "DirectoryId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "directory_id": "DirectoryId",
    }

    directory_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FederatedAuthenticationRequest(PropertyType):
    SELF_SERVICE_SAML_PROVIDER_ARN = "SelfServiceSAMLProviderArn"
    SAML_PROVIDER_ARN = "SAMLProviderArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "self_service_saml_provider_arn": "SelfServiceSAMLProviderArn",
        "saml_provider_arn": "SAMLProviderArn",
    }

    self_service_saml_provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    saml_provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagSpecification(PropertyType):
    RESOURCE_TYPE = "ResourceType"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None

