"""PropertyTypes for AWS::MediaTailor::VodSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HttpPackageConfiguration(PropertyType):
    PATH = "Path"
    TYPE = "Type"
    SOURCE_GROUP = "SourceGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "type_": "Type",
        "source_group": "SourceGroup",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Type, Ref, GetAtt, Sub]] = None
    source_group: Optional[Union[str, Ref, GetAtt, Sub]] = None

