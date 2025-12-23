"""PropertyTypes for AWS::SES::ContactList."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Topic(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "display_name": "DisplayName",
        "default_subscription_status": "DefaultSubscriptionStatus",
        "topic_name": "TopicName",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_subscription_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

