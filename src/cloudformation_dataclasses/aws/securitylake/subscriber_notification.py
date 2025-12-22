"""PropertyTypes for AWS::SecurityLake::SubscriberNotification."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessType:
    """AccessType enum values."""

    LAKEFORMATION = "LAKEFORMATION"
    S3 = "S3"


class AwsLogSourceName:
    """AwsLogSourceName enum values."""

    ROUTE53 = "ROUTE53"
    VPC_FLOW = "VPC_FLOW"
    SH_FINDINGS = "SH_FINDINGS"
    CLOUD_TRAIL_MGMT = "CLOUD_TRAIL_MGMT"
    LAMBDA_EXECUTION = "LAMBDA_EXECUTION"
    S3_DATA = "S3_DATA"
    EKS_AUDIT = "EKS_AUDIT"
    WAF = "WAF"


class DataLakeStatus:
    """DataLakeStatus enum values."""

    INITIALIZED = "INITIALIZED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class HttpMethod:
    """HttpMethod enum values."""

    POST = "POST"
    PUT = "PUT"


class SourceCollectionStatus:
    """SourceCollectionStatus enum values."""

    COLLECTING = "COLLECTING"
    MISCONFIGURED = "MISCONFIGURED"
    NOT_COLLECTING = "NOT_COLLECTING"


class SubscriberStatus:
    """SubscriberStatus enum values."""

    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"
    PENDING = "PENDING"
    READY = "READY"


@dataclass
class HttpsNotificationConfiguration(PropertyType):
    ENDPOINT = "Endpoint"
    TARGET_ROLE_ARN = "TargetRoleArn"
    AUTHORIZATION_API_KEY_VALUE = "AuthorizationApiKeyValue"
    AUTHORIZATION_API_KEY_NAME = "AuthorizationApiKeyName"
    HTTP_METHOD = "HttpMethod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "target_role_arn": "TargetRoleArn",
        "authorization_api_key_value": "AuthorizationApiKeyValue",
        "authorization_api_key_name": "AuthorizationApiKeyName",
        "http_method": "HttpMethod",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_api_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_api_key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_method: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfiguration(PropertyType):
    HTTPS_NOTIFICATION_CONFIGURATION = "HttpsNotificationConfiguration"
    SQS_NOTIFICATION_CONFIGURATION = "SqsNotificationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "https_notification_configuration": "HttpsNotificationConfiguration",
        "sqs_notification_configuration": "SqsNotificationConfiguration",
    }

    https_notification_configuration: Optional[HttpsNotificationConfiguration] = None
    sqs_notification_configuration: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

