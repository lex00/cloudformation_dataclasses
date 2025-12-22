"""PropertyTypes for AWS::SNS::Topic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class LanguageCodeString:
    """LanguageCodeString enum values."""

    EN_US = "en-US"
    EN_GB = "en-GB"
    ES_419 = "es-419"
    ES_ES = "es-ES"
    DE_DE = "de-DE"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    PT_BR = "pt-BR"
    KR_KR = "kr-KR"
    ZH_CN = "zh-CN"
    ZH_TW = "zh-TW"


class NumberCapability:
    """NumberCapability enum values."""

    SMS = "SMS"
    MMS = "MMS"
    VOICE = "VOICE"


class RouteType:
    """RouteType enum values."""

    TRANSACTIONAL = "Transactional"
    PROMOTIONAL = "Promotional"
    PREMIUM = "Premium"


class SMSSandboxPhoneNumberVerificationStatus:
    """SMSSandboxPhoneNumberVerificationStatus enum values."""

    PENDING = "Pending"
    VERIFIED = "Verified"


@dataclass
class LoggingConfig(PropertyType):
    FAILURE_FEEDBACK_ROLE_ARN = "FailureFeedbackRoleArn"
    SUCCESS_FEEDBACK_SAMPLE_RATE = "SuccessFeedbackSampleRate"
    SUCCESS_FEEDBACK_ROLE_ARN = "SuccessFeedbackRoleArn"
    PROTOCOL = "Protocol"

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
    ENDPOINT = "Endpoint"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "protocol": "Protocol",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None

