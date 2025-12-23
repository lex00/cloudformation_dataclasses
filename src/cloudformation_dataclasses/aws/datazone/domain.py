"""PropertyTypes for AWS::DataZone::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SingleSignOn(PropertyType):
    TYPE = "Type"
    USER_ASSIGNMENT = "UserAssignment"
    IDC_INSTANCE_ARN = "IdcInstanceArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "user_assignment": "UserAssignment",
        "idc_instance_arn": "IdcInstanceArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_assignment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    idc_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

