"""PropertyTypes for AWS::Rbin::Rule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourceTag(PropertyType):
    RESOURCE_TAG_VALUE = "ResourceTagValue"
    RESOURCE_TAG_KEY = "ResourceTagKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_tag_value": "ResourceTagValue",
        "resource_tag_key": "ResourceTagKey",
    }

    resource_tag_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionPeriod(PropertyType):
    RETENTION_PERIOD_UNIT = "RetentionPeriodUnit"
    RETENTION_PERIOD_VALUE = "RetentionPeriodValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retention_period_unit": "RetentionPeriodUnit",
        "retention_period_value": "RetentionPeriodValue",
    }

    retention_period_unit: Optional[Union[str, RetentionPeriodUnit, Ref, GetAtt, Sub]] = None
    retention_period_value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class UnlockDelay(PropertyType):
    UNLOCK_DELAY_VALUE = "UnlockDelayValue"
    UNLOCK_DELAY_UNIT = "UnlockDelayUnit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unlock_delay_value": "UnlockDelayValue",
        "unlock_delay_unit": "UnlockDelayUnit",
    }

    unlock_delay_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlock_delay_unit: Optional[Union[str, UnlockDelayUnit, Ref, GetAtt, Sub]] = None

