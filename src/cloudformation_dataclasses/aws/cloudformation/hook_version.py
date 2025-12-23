"""PropertyTypes for AWS::CloudFormation::HookVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoggingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_name": "LogGroupName",
        "log_role_arn": "LogRoleArn",
    }

    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

