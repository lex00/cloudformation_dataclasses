"""PropertyTypes for AWS::Panorama::ApplicationInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ManifestOverridesPayload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "payload_data": "PayloadData",
    }

    payload_data: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManifestPayload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "payload_data": "PayloadData",
    }

    payload_data: Optional[Union[str, Ref, GetAtt, Sub]] = None

