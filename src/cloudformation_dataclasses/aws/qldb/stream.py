"""PropertyTypes for AWS::QLDB::Stream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class KinesisConfiguration(PropertyType):
    AGGREGATION_ENABLED = "AggregationEnabled"
    STREAM_ARN = "StreamArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_enabled": "AggregationEnabled",
        "stream_arn": "StreamArn",
    }

    aggregation_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

