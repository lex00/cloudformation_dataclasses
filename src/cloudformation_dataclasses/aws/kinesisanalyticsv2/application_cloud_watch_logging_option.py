"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLoggingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_arn": "LogStreamARN",
    }

    log_stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

