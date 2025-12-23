"""PropertyTypes for AWS::Connect::QuickConnect."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PhoneNumberQuickConnectConfig(PropertyType):
    PHONE_NUMBER = "PhoneNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "phone_number": "PhoneNumber",
    }

    phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueueQuickConnectConfig(PropertyType):
    CONTACT_FLOW_ARN = "ContactFlowArn"
    QUEUE_ARN = "QueueArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_flow_arn": "ContactFlowArn",
        "queue_arn": "QueueArn",
    }

    contact_flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuickConnectConfig(PropertyType):
    QUEUE_CONFIG = "QueueConfig"
    PHONE_CONFIG = "PhoneConfig"
    QUICK_CONNECT_TYPE = "QuickConnectType"
    USER_CONFIG = "UserConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "queue_config": "QueueConfig",
        "phone_config": "PhoneConfig",
        "quick_connect_type": "QuickConnectType",
        "user_config": "UserConfig",
    }

    queue_config: Optional[QueueQuickConnectConfig] = None
    phone_config: Optional[PhoneNumberQuickConnectConfig] = None
    quick_connect_type: Optional[Union[str, QuickConnectType, Ref, GetAtt, Sub]] = None
    user_config: Optional[UserQuickConnectConfig] = None


@dataclass
class UserQuickConnectConfig(PropertyType):
    USER_ARN = "UserArn"
    CONTACT_FLOW_ARN = "ContactFlowArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_arn": "UserArn",
        "contact_flow_arn": "ContactFlowArn",
    }

    user_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    contact_flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

