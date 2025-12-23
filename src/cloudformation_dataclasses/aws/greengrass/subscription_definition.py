"""PropertyTypes for AWS::Greengrass::SubscriptionDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Subscription(PropertyType):
    TARGET = "Target"
    ID = "Id"
    SOURCE = "Source"
    SUBJECT = "Subject"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "id": "Id",
        "source": "Source",
        "subject": "Subject",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubscriptionDefinitionVersion(PropertyType):
    SUBSCRIPTIONS = "Subscriptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subscriptions": "Subscriptions",
    }

    subscriptions: Optional[list[Subscription]] = None

