"""PropertyTypes for AWS::QBusiness::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttachmentsConfiguration(PropertyType):
    ATTACHMENTS_CONTROL_MODE = "AttachmentsControlMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attachments_control_mode": "AttachmentsControlMode",
    }

    attachments_control_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AutoSubscriptionConfiguration(PropertyType):
    DEFAULT_SUBSCRIPTION_TYPE = "DefaultSubscriptionType"
    AUTO_SUBSCRIBE = "AutoSubscribe"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_subscription_type": "DefaultSubscriptionType",
        "auto_subscribe": "AutoSubscribe",
    }

    default_subscription_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_subscribe: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PersonalizationConfiguration(PropertyType):
    PERSONALIZATION_CONTROL_MODE = "PersonalizationControlMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "personalization_control_mode": "PersonalizationControlMode",
    }

    personalization_control_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QAppsConfiguration(PropertyType):
    Q_APPS_CONTROL_MODE = "QAppsControlMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "q_apps_control_mode": "QAppsControlMode",
    }

    q_apps_control_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuickSightConfiguration(PropertyType):
    CLIENT_NAMESPACE = "ClientNamespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_namespace": "ClientNamespace",
    }

    client_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None

