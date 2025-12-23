"""PropertyTypes for AWS::VerifiedPermissions::PolicyStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeletionProtection(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaDefinition(PropertyType):
    CEDAR_JSON = "CedarJson"
    CEDAR_FORMAT = "CedarFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cedar_json": "CedarJson",
        "cedar_format": "CedarFormat",
    }

    cedar_json: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cedar_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValidationSettings(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None

