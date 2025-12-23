"""PropertyTypes for AWS::CE::AnomalySubscription."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourceTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subscriber(PropertyType):
    STATUS = "Status"
    TYPE = "Type"
    ADDRESS = "Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "type_": "Type",
        "address": "Address",
    }

    status: Optional[Union[str, SubscriberStatus, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SubscriberType, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None

