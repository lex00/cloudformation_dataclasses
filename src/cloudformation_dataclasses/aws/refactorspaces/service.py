"""PropertyTypes for AWS::RefactorSpaces::Service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LambdaEndpointInput(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UrlEndpointInput(PropertyType):
    HEALTH_URL = "HealthUrl"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "health_url": "HealthUrl",
        "url": "Url",
    }

    health_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None

