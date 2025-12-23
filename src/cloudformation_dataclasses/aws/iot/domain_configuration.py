"""PropertyTypes for AWS::IoT::DomainConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthorizerConfig(PropertyType):
    DEFAULT_AUTHORIZER_NAME = "DefaultAuthorizerName"
    ALLOW_AUTHORIZER_OVERRIDE = "AllowAuthorizerOverride"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_authorizer_name": "DefaultAuthorizerName",
        "allow_authorizer_override": "AllowAuthorizerOverride",
    }

    default_authorizer_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allow_authorizer_override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ClientCertificateConfig(PropertyType):
    CLIENT_CERTIFICATE_CALLBACK_ARN = "ClientCertificateCallbackArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_certificate_callback_arn": "ClientCertificateCallbackArn",
    }

    client_certificate_callback_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerCertificateConfig(PropertyType):
    ENABLE_OCSP_CHECK = "EnableOCSPCheck"
    OCSP_LAMBDA_ARN = "OcspLambdaArn"
    OCSP_AUTHORIZED_RESPONDER_ARN = "OcspAuthorizedResponderArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_ocsp_check": "EnableOCSPCheck",
        "ocsp_lambda_arn": "OcspLambdaArn",
        "ocsp_authorized_responder_arn": "OcspAuthorizedResponderArn",
    }

    enable_ocsp_check: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ocsp_lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ocsp_authorized_responder_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerCertificateSummary(PropertyType):
    SERVER_CERTIFICATE_STATUS_DETAIL = "ServerCertificateStatusDetail"
    SERVER_CERTIFICATE_ARN = "ServerCertificateArn"
    SERVER_CERTIFICATE_STATUS = "ServerCertificateStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_certificate_status_detail": "ServerCertificateStatusDetail",
        "server_certificate_arn": "ServerCertificateArn",
        "server_certificate_status": "ServerCertificateStatus",
    }

    server_certificate_status_detail: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    server_certificate_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TlsConfig(PropertyType):
    SECURITY_POLICY = "SecurityPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_policy": "SecurityPolicy",
    }

    security_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None

