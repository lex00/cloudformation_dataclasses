"""PropertyTypes for AWS::Glue::SchemaVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Schema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "registry_name": "RegistryName",
        "schema_arn": "SchemaArn",
        "schema_name": "SchemaName",
    }

    registry_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

