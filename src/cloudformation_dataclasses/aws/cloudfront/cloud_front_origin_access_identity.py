"""PropertyTypes for AWS::CloudFront::CloudFrontOriginAccessIdentity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudFrontOriginAccessIdentityConfig(PropertyType):
    COMMENT = "Comment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None

