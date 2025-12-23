"""PropertyTypes for AWS::NotificationsContacts::EmailContact."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EmailContact(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "address": "Address",
        "creation_time": "CreationTime",
        "update_time": "UpdateTime",
        "arn": "Arn",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    update_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

