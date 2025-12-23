"""PropertyTypes for AWS::IAM::SAMLProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SAMLPrivateKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_id": "KeyId",
        "timestamp": "Timestamp",
    }

    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp: Optional[Union[str, Ref, GetAtt, Sub]] = None

