"""PropertyTypes for AWS::MediaTailor::SourceLocation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessConfiguration(PropertyType):
    SECRETS_MANAGER_ACCESS_TOKEN_CONFIGURATION = "SecretsManagerAccessTokenConfiguration"
    ACCESS_TYPE = "AccessType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager_access_token_configuration": "SecretsManagerAccessTokenConfiguration",
        "access_type": "AccessType",
    }

    secrets_manager_access_token_configuration: Optional[SecretsManagerAccessTokenConfiguration] = None
    access_type: Optional[Union[str, AccessType, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultSegmentDeliveryConfiguration(PropertyType):
    BASE_URL = "BaseUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "base_url": "BaseUrl",
    }

    base_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpConfiguration(PropertyType):
    BASE_URL = "BaseUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "base_url": "BaseUrl",
    }

    base_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecretsManagerAccessTokenConfiguration(PropertyType):
    SECRET_ARN = "SecretArn"
    HEADER_NAME = "HeaderName"
    SECRET_STRING_KEY = "SecretStringKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "header_name": "HeaderName",
        "secret_string_key": "SecretStringKey",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_string_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SegmentDeliveryConfiguration(PropertyType):
    BASE_URL = "BaseUrl"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "base_url": "BaseUrl",
        "name": "Name",
    }

    base_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

