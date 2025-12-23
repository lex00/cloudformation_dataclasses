"""PropertyTypes for AWS::SSMContacts::Plan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ChannelTargetInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_interval_in_minutes": "RetryIntervalInMinutes",
        "channel_id": "ChannelId",
    }

    retry_interval_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    channel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContactTargetInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_id": "ContactId",
        "is_essential": "IsEssential",
    }

    contact_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_essential: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Stage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_minutes": "DurationInMinutes",
        "targets": "Targets",
    }

    duration_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    targets: Optional[list[Targets]] = None


@dataclass
class Targets(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_target_info": "ChannelTargetInfo",
        "contact_target_info": "ContactTargetInfo",
    }

    channel_target_info: Optional[ChannelTargetInfo] = None
    contact_target_info: Optional[ContactTargetInfo] = None

