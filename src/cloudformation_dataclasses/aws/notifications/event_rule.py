"""PropertyTypes for AWS::Notifications::EventRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessStatus:
    """AccessStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    PENDING = "PENDING"
    FAILED = "FAILED"


class AccountContactType:
    """AccountContactType enum values."""

    ACCOUNT_PRIMARY = "ACCOUNT_PRIMARY"
    ACCOUNT_ALTERNATE_BILLING = "ACCOUNT_ALTERNATE_BILLING"
    ACCOUNT_ALTERNATE_OPERATIONS = "ACCOUNT_ALTERNATE_OPERATIONS"
    ACCOUNT_ALTERNATE_SECURITY = "ACCOUNT_ALTERNATE_SECURITY"


class AggregationDuration:
    """AggregationDuration enum values."""

    LONG = "LONG"
    SHORT = "SHORT"
    NONE = "NONE"


class AggregationEventType:
    """AggregationEventType enum values."""

    AGGREGATE = "AGGREGATE"
    CHILD = "CHILD"
    NONE = "NONE"


class ChannelAssociationOverrideOption:
    """ChannelAssociationOverrideOption enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ChannelType:
    """ChannelType enum values."""

    MOBILE = "MOBILE"
    CHATBOT = "CHATBOT"
    EMAIL = "EMAIL"
    ACCOUNT_CONTACT = "ACCOUNT_CONTACT"


class EventRuleStatus:
    """EventRuleStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"


class EventStatus:
    """EventStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class LocaleCode:
    """LocaleCode enum values."""

    DE_DE = "de_DE"
    EN_CA = "en_CA"
    EN_US = "en_US"
    EN_UK = "en_UK"
    ES_ES = "es_ES"
    FR_CA = "fr_CA"
    FR_FR = "fr_FR"
    ID_ID = "id_ID"
    IT_IT = "it_IT"
    JA_JP = "ja_JP"
    KO_KR = "ko_KR"
    PT_BR = "pt_BR"
    TR_TR = "tr_TR"
    ZH_CN = "zh_CN"
    ZH_TW = "zh_TW"


class MediaElementType:
    """MediaElementType enum values."""

    IMAGE = "IMAGE"


class MemberAccountNotificationConfigurationStatus:
    """MemberAccountNotificationConfigurationStatus enum values."""

    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    INACTIVE = "INACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"


class NotificationConfigurationStatus:
    """NotificationConfigurationStatus enum values."""

    ACTIVE = "ACTIVE"
    PARTIALLY_ACTIVE = "PARTIALLY_ACTIVE"
    INACTIVE = "INACTIVE"
    DELETING = "DELETING"


class NotificationConfigurationSubtype:
    """NotificationConfigurationSubtype enum values."""

    ACCOUNT = "ACCOUNT"
    ADMIN_MANAGED = "ADMIN_MANAGED"


class NotificationHubStatus:
    """NotificationHubStatus enum values."""

    ACTIVE = "ACTIVE"
    REGISTERING = "REGISTERING"
    DEREGISTERING = "DEREGISTERING"
    INACTIVE = "INACTIVE"


class NotificationType:
    """NotificationType enum values."""

    ALERT = "ALERT"
    WARNING = "WARNING"
    ANNOUNCEMENT = "ANNOUNCEMENT"
    INFORMATIONAL = "INFORMATIONAL"


class SchemaVersion:
    """SchemaVersion enum values."""

    V1_0 = "v1.0"


class TextPartType:
    """TextPartType enum values."""

    LOCALIZED_TEXT = "LOCALIZED_TEXT"
    PLAIN_TEXT = "PLAIN_TEXT"
    URL = "URL"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


@dataclass
class EventRuleStatusSummary(PropertyType):
    STATUS = "Status"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "reason": "Reason",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None

