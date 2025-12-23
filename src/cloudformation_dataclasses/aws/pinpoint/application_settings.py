"""PropertyTypes for AWS::Pinpoint::ApplicationSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CampaignHook(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "web_url": "WebUrl",
        "lambda_function_name": "LambdaFunctionName",
    }

    mode: Optional[Union[str, Mode, Ref, GetAtt, Sub]] = None
    web_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_function_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Limits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "daily": "Daily",
        "maximum_duration": "MaximumDuration",
        "total": "Total",
        "messages_per_second": "MessagesPerSecond",
    }

    daily: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    total: Optional[Union[int, Ref, GetAtt, Sub]] = None
    messages_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QuietTime(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None

