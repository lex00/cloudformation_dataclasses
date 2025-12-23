"""PropertyTypes for AWS::ApiGateway::DocumentationPart."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Location(PropertyType):
    PATH = "Path"
    TYPE = "Type"
    METHOD = "Method"
    STATUS_CODE = "StatusCode"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "type_": "Type",
        "method": "Method",
        "status_code": "StatusCode",
        "name": "Name",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

