"""PropertyTypes for AWS::SES::MailManagerArchive."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ArchiveRetention(PropertyType):
    RETENTION_PERIOD = "RetentionPeriod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retention_period": "RetentionPeriod",
    }

    retention_period: Optional[Union[str, Ref, GetAtt, Sub]] = None

