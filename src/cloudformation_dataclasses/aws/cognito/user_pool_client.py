"""PropertyTypes for AWS::Cognito::UserPoolClient."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnalyticsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_arn": "ApplicationArn",
        "user_data_shared": "UserDataShared",
        "external_id": "ExternalId",
        "application_id": "ApplicationId",
        "role_arn": "RoleArn",
    }

    application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_data_shared: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RefreshTokenRotation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_grace_period_seconds": "RetryGracePeriodSeconds",
        "feature": "Feature",
    }

    retry_grace_period_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    feature: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TokenValidityUnits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id_token": "IdToken",
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
    }

    id_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None

