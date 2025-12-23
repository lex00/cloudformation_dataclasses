"""PropertyTypes for AWS::SageMaker::Workteam."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CognitoMemberDefinition(PropertyType):
    COGNITO_USER_POOL = "CognitoUserPool"
    COGNITO_CLIENT_ID = "CognitoClientId"
    COGNITO_USER_GROUP = "CognitoUserGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cognito_user_pool": "CognitoUserPool",
        "cognito_client_id": "CognitoClientId",
        "cognito_user_group": "CognitoUserGroup",
    }

    cognito_user_pool: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cognito_client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cognito_user_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemberDefinition(PropertyType):
    OIDC_MEMBER_DEFINITION = "OidcMemberDefinition"
    COGNITO_MEMBER_DEFINITION = "CognitoMemberDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "oidc_member_definition": "OidcMemberDefinition",
        "cognito_member_definition": "CognitoMemberDefinition",
    }

    oidc_member_definition: Optional[OidcMemberDefinition] = None
    cognito_member_definition: Optional[CognitoMemberDefinition] = None


@dataclass
class NotificationConfiguration(PropertyType):
    NOTIFICATION_TOPIC_ARN = "NotificationTopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_topic_arn": "NotificationTopicArn",
    }

    notification_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OidcMemberDefinition(PropertyType):
    OIDC_GROUPS = "OidcGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "oidc_groups": "OidcGroups",
    }

    oidc_groups: Optional[Union[list[str], Ref]] = None

