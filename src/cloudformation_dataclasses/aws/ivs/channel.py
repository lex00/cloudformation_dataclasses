"""PropertyTypes for AWS::IVS::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MultitrackInputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_resolution": "MaximumResolution",
        "policy": "Policy",
        "enabled": "Enabled",
    }

    maximum_resolution: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

