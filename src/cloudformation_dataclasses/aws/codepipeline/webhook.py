"""PropertyTypes for AWS::CodePipeline::Webhook."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class WebhookAuthConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_ip_range": "AllowedIPRange",
        "secret_token": "SecretToken",
    }

    allowed_ip_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebhookFilterRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "json_path": "JsonPath",
        "match_equals": "MatchEquals",
    }

    json_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_equals: Optional[Union[str, Ref, GetAtt, Sub]] = None

