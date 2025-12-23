"""PropertyTypes for AWS::CloudFront::KeyValueStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ImportSource(PropertyType):
    SOURCE_ARN = "SourceArn"
    SOURCE_TYPE = "SourceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_arn": "SourceArn",
        "source_type": "SourceType",
    }

    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_type: Optional[Union[str, ImportSourceType, Ref, GetAtt, Sub]] = None

