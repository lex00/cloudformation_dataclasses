"""PropertyTypes for AWS::PCAConnectorAD::TemplateGroupAccessControlEntry."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessRights(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enroll": "Enroll",
        "auto_enroll": "AutoEnroll",
    }

    enroll: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_enroll: Optional[Union[str, Ref, GetAtt, Sub]] = None

