"""PropertyTypes for AWS::AppConfig::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Monitor(PropertyType):
    ALARM_ARN = "AlarmArn"
    ALARM_ROLE_ARN = "AlarmRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_arn": "AlarmArn",
        "alarm_role_arn": "AlarmRoleArn",
    }

    alarm_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alarm_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

