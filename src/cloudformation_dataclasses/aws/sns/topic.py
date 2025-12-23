"""PropertyTypes for AWS::SNS::Topic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoggingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "failure_feedback_role_arn": "FailureFeedbackRoleArn",
        "success_feedback_sample_rate": "SuccessFeedbackSampleRate",
        "success_feedback_role_arn": "SuccessFeedbackRoleArn",
        "protocol": "Protocol",
    }

    failure_feedback_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    success_feedback_sample_rate: Optional[Union[str, Ref, GetAtt, Sub]] = None
    success_feedback_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subscription(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "protocol": "Protocol",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None

