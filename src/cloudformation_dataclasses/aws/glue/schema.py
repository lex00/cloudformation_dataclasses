"""PropertyTypes for AWS::Glue::Schema."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Registry(PropertyType):
    ARN = "Arn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
        "name": "Name",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaVersion(PropertyType):
    IS_LATEST = "IsLatest"
    VERSION_NUMBER = "VersionNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_latest": "IsLatest",
        "version_number": "VersionNumber",
    }

    is_latest: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    version_number: Optional[Union[int, Ref, GetAtt, Sub]] = None

