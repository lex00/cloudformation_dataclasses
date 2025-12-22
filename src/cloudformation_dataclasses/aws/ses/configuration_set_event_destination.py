"""PropertyTypes for AWS::SES::ConfigurationSetEventDestination."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BehaviorOnMXFailure:
    """BehaviorOnMXFailure enum values."""

    USEDEFAULTVALUE = "UseDefaultValue"
    REJECTMESSAGE = "RejectMessage"


class BounceType:
    """BounceType enum values."""

    DOESNOTEXIST = "DoesNotExist"
    MESSAGETOOLARGE = "MessageTooLarge"
    EXCEEDEDQUOTA = "ExceededQuota"
    CONTENTREJECTED = "ContentRejected"
    UNDEFINED = "Undefined"
    TEMPORARYFAILURE = "TemporaryFailure"


class BulkEmailStatus:
    """BulkEmailStatus enum values."""

    SUCCESS = "Success"
    MESSAGEREJECTED = "MessageRejected"
    MAILFROMDOMAINNOTVERIFIED = "MailFromDomainNotVerified"
    CONFIGURATIONSETDOESNOTEXIST = "ConfigurationSetDoesNotExist"
    TEMPLATEDOESNOTEXIST = "TemplateDoesNotExist"
    ACCOUNTSUSPENDED = "AccountSuspended"
    ACCOUNTTHROTTLED = "AccountThrottled"
    ACCOUNTDAILYQUOTAEXCEEDED = "AccountDailyQuotaExceeded"
    INVALIDSENDINGPOOLNAME = "InvalidSendingPoolName"
    ACCOUNTSENDINGPAUSED = "AccountSendingPaused"
    CONFIGURATIONSETSENDINGPAUSED = "ConfigurationSetSendingPaused"
    INVALIDPARAMETERVALUE = "InvalidParameterValue"
    TRANSIENTFAILURE = "TransientFailure"
    FAILED = "Failed"


class ConfigurationSetAttribute:
    """ConfigurationSetAttribute enum values."""

    EVENTDESTINATIONS = "eventDestinations"
    TRACKINGOPTIONS = "trackingOptions"
    DELIVERYOPTIONS = "deliveryOptions"
    REPUTATIONOPTIONS = "reputationOptions"


class CustomMailFromStatus:
    """CustomMailFromStatus enum values."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"
    TEMPORARYFAILURE = "TemporaryFailure"


class DimensionValueSource:
    """DimensionValueSource enum values."""

    MESSAGETAG = "messageTag"
    EMAILHEADER = "emailHeader"
    LINKTAG = "linkTag"


class DsnAction:
    """DsnAction enum values."""

    FAILED = "failed"
    DELAYED = "delayed"
    DELIVERED = "delivered"
    RELAYED = "relayed"
    EXPANDED = "expanded"


class EventType:
    """EventType enum values."""

    SEND = "send"
    REJECT = "reject"
    BOUNCE = "bounce"
    COMPLAINT = "complaint"
    DELIVERY = "delivery"
    OPEN = "open"
    CLICK = "click"
    RENDERINGFAILURE = "renderingFailure"


class IdentityType:
    """IdentityType enum values."""

    EMAILADDRESS = "EmailAddress"
    DOMAIN = "Domain"


class InvocationType:
    """InvocationType enum values."""

    EVENT = "Event"
    REQUESTRESPONSE = "RequestResponse"


class NotificationType:
    """NotificationType enum values."""

    BOUNCE = "Bounce"
    COMPLAINT = "Complaint"
    DELIVERY = "Delivery"


class ReceiptFilterPolicy:
    """ReceiptFilterPolicy enum values."""

    BLOCK = "Block"
    ALLOW = "Allow"


class SNSActionEncoding:
    """SNSActionEncoding enum values."""

    UTF_8 = "UTF-8"
    BASE64 = "Base64"


class StopScope:
    """StopScope enum values."""

    RULESET = "RuleSet"


class TlsPolicy:
    """TlsPolicy enum values."""

    REQUIRE = "Require"
    OPTIONAL = "Optional"


class VerificationStatus:
    """VerificationStatus enum values."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"
    TEMPORARYFAILURE = "TemporaryFailure"
    NOTSTARTED = "NotStarted"


@dataclass
class CloudWatchDestination(PropertyType):
    DIMENSION_CONFIGURATIONS = "DimensionConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_configurations": "DimensionConfigurations",
    }

    dimension_configurations: Optional[list[DimensionConfiguration]] = None


@dataclass
class DimensionConfiguration(PropertyType):
    DIMENSION_VALUE_SOURCE = "DimensionValueSource"
    DEFAULT_DIMENSION_VALUE = "DefaultDimensionValue"
    DIMENSION_NAME = "DimensionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_value_source": "DimensionValueSource",
        "default_dimension_value": "DefaultDimensionValue",
        "dimension_name": "DimensionName",
    }

    dimension_value_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_dimension_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeDestination(PropertyType):
    EVENT_BUS_ARN = "EventBusArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bus_arn": "EventBusArn",
    }

    event_bus_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventDestination(PropertyType):
    SNS_DESTINATION = "SnsDestination"
    CLOUD_WATCH_DESTINATION = "CloudWatchDestination"
    ENABLED = "Enabled"
    MATCHING_EVENT_TYPES = "MatchingEventTypes"
    EVENT_BRIDGE_DESTINATION = "EventBridgeDestination"
    NAME = "Name"
    KINESIS_FIREHOSE_DESTINATION = "KinesisFirehoseDestination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_destination": "SnsDestination",
        "cloud_watch_destination": "CloudWatchDestination",
        "enabled": "Enabled",
        "matching_event_types": "MatchingEventTypes",
        "event_bridge_destination": "EventBridgeDestination",
        "name": "Name",
        "kinesis_firehose_destination": "KinesisFirehoseDestination",
    }

    sns_destination: Optional[SnsDestination] = None
    cloud_watch_destination: Optional[CloudWatchDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    matching_event_types: Optional[Union[list[str], Ref]] = None
    event_bridge_destination: Optional[EventBridgeDestination] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kinesis_firehose_destination: Optional[KinesisFirehoseDestination] = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    IAM_ROLE_ARN = "IAMRoleARN"
    DELIVERY_STREAM_ARN = "DeliveryStreamARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_role_arn": "IAMRoleARN",
        "delivery_stream_arn": "DeliveryStreamARN",
    }

    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delivery_stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnsDestination(PropertyType):
    TOPIC_ARN = "TopicARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicARN",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

