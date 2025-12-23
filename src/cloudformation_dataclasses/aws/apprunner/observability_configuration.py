"""PropertyTypes for AWS::AppRunner::ObservabilityConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TraceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vendor": "Vendor",
    }

    vendor: Optional[Union[str, TracingVendor, Ref, GetAtt, Sub]] = None

