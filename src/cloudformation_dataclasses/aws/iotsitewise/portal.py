"""PropertyTypes for AWS::IoTSiteWise::Portal."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Alarms(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_lambda_arn": "NotificationLambdaArn",
        "alarm_role_arn": "AlarmRoleArn",
    }

    notification_lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alarm_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortalTypeEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "portal_tools": "PortalTools",
    }

    portal_tools: Optional[Union[list[str], Ref]] = None

