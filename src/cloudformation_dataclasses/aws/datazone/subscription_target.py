"""PropertyTypes for AWS::DataZone::SubscriptionTarget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SubscriptionTargetForm(PropertyType):
    CONTENT = "Content"
    FORM_NAME = "FormName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
        "form_name": "FormName",
    }

    content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    form_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

