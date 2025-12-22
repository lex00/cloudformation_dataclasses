"""PropertyTypes for AWS::SMSVOICE::PhoneNumber."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MandatoryKeyword(PropertyType):
    MESSAGE = "Message"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MandatoryKeywords(PropertyType):
    HELP = "HELP"
    STOP = "STOP"

    _property_mappings: ClassVar[dict[str, str]] = {
        "help": "HELP",
        "stop": "STOP",
    }

    help: Optional[MandatoryKeyword] = None
    stop: Optional[MandatoryKeyword] = None


@dataclass
class OptionalKeyword(PropertyType):
    ACTION = "Action"
    KEYWORD = "Keyword"
    MESSAGE = "Message"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "keyword": "Keyword",
        "message": "Message",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    keyword: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TwoWay(PropertyType):
    CHANNEL_ARN = "ChannelArn"
    CHANNEL_ROLE = "ChannelRole"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_arn": "ChannelArn",
        "channel_role": "ChannelRole",
        "enabled": "Enabled",
    }

    channel_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

