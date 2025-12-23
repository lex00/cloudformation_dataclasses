"""PropertyTypes for AWS::AppSync::ChannelNamespace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthMode(PropertyType):
    AUTH_TYPE = "AuthType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_type": "AuthType",
    }

    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HandlerConfig(PropertyType):
    INTEGRATION = "Integration"
    BEHAVIOR = "Behavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "integration": "Integration",
        "behavior": "Behavior",
    }

    integration: Optional[Integration] = None
    behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HandlerConfigs(PropertyType):
    ON_PUBLISH = "OnPublish"
    ON_SUBSCRIBE = "OnSubscribe"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_publish": "OnPublish",
        "on_subscribe": "OnSubscribe",
    }

    on_publish: Optional[HandlerConfig] = None
    on_subscribe: Optional[HandlerConfig] = None


@dataclass
class Integration(PropertyType):
    DATA_SOURCE_NAME = "DataSourceName"
    LAMBDA_CONFIG = "LambdaConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_name": "DataSourceName",
        "lambda_config": "LambdaConfig",
    }

    data_source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_config: Optional[LambdaConfig] = None


@dataclass
class LambdaConfig(PropertyType):
    INVOKE_TYPE = "InvokeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invoke_type": "InvokeType",
    }

    invoke_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

