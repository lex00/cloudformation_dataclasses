"""PropertyTypes for AWS::AmazonMQ::ConfigurationAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigurationId(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "revision": "Revision",
        "id": "Id",
    }

    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

