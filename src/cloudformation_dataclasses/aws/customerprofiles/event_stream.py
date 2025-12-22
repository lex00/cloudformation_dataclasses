"""PropertyTypes for AWS::CustomerProfiles::EventStream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DestinationDetails(PropertyType):
    STATUS = "Status"
    URI = "Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "uri": "Uri",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None

