"""PropertyTypes for AWS::CertificateManager::Account."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ExpiryEventsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days_before_expiry": "DaysBeforeExpiry",
    }

    days_before_expiry: Optional[Union[int, Ref, GetAtt, Sub]] = None

