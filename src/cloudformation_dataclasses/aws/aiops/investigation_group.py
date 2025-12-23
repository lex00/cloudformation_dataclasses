"""PropertyTypes for AWS::AIOps::InvestigationGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ChatbotNotificationChannel(PropertyType):
    SNS_TOPIC_ARN = "SNSTopicArn"
    CHAT_CONFIGURATION_ARNS = "ChatConfigurationArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_topic_arn": "SNSTopicArn",
        "chat_configuration_arns": "ChatConfigurationArns",
    }

    sns_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chat_configuration_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class CrossAccountConfiguration(PropertyType):
    SOURCE_ROLE_ARN = "SourceRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_role_arn": "SourceRoleArn",
    }

    source_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfigMap(PropertyType):
    ENCRYPTION_CONFIGURATION_TYPE = "EncryptionConfigurationType"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_configuration_type": "EncryptionConfigurationType",
        "kms_key_id": "KmsKeyId",
    }

    encryption_configuration_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

