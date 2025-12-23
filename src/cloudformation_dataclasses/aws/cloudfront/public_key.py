"""PropertyTypes for AWS::CloudFront::PublicKey."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PublicKeyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "caller_reference": "CallerReference",
        "encoded_key": "EncodedKey",
        "name": "Name",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    caller_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encoded_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

