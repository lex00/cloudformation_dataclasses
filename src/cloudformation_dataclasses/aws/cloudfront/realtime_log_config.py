"""PropertyTypes for AWS::CloudFront::RealtimeLogConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EndPoint(PropertyType):
    KINESIS_STREAM_CONFIG = "KinesisStreamConfig"
    STREAM_TYPE = "StreamType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kinesis_stream_config": "KinesisStreamConfig",
        "stream_type": "StreamType",
    }

    kinesis_stream_config: Optional[KinesisStreamConfig] = None
    stream_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamConfig(PropertyType):
    STREAM_ARN = "StreamArn"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_arn": "StreamArn",
        "role_arn": "RoleArn",
    }

    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

