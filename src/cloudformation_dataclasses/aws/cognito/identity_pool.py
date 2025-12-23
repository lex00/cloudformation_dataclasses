"""PropertyTypes for AWS::Cognito::IdentityPool."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CognitoIdentityProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "server_side_token_check": "ServerSideTokenCheck",
        "provider_name": "ProviderName",
        "client_id": "ClientId",
    }

    server_side_token_check: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CognitoStreams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "streaming_status": "StreamingStatus",
        "stream_name": "StreamName",
        "role_arn": "RoleArn",
    }

    streaming_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PushSync(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_arns": "ApplicationArns",
        "role_arn": "RoleArn",
    }

    application_arns: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

