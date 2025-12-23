"""PropertyTypes for AWS::PinpointEmail::Identity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MailFromAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mail_from_domain": "MailFromDomain",
        "behavior_on_mx_failure": "BehaviorOnMxFailure",
    }

    mail_from_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    behavior_on_mx_failure: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

