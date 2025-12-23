"""PropertyTypes for AWS::Glue::Integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IntegrationConfig(PropertyType):
    CONTINUOUS_SYNC = "ContinuousSync"
    REFRESH_INTERVAL = "RefreshInterval"
    SOURCE_PROPERTIES = "SourceProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "continuous_sync": "ContinuousSync",
        "refresh_interval": "RefreshInterval",
        "source_properties": "SourceProperties",
    }

    continuous_sync: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    refresh_interval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_properties: Optional[dict[str, str]] = None

