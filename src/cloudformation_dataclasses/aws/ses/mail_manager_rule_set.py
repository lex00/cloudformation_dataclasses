"""PropertyTypes for AWS::SES::MailManagerRuleSet."""

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
class AddHeaderAction(PropertyType):
    HEADER_VALUE = "HeaderValue"
    HEADER_NAME = "HeaderName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "header_value": "HeaderValue",
        "header_name": "HeaderName",
    }

    header_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Analysis(PropertyType):
    ANALYZER = "Analyzer"
    RESULT_FIELD = "ResultField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "analyzer": "Analyzer",
        "result_field": "ResultField",
    }

    analyzer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    result_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArchiveAction(PropertyType):
    TARGET_ARCHIVE = "TargetArchive"
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_archive": "TargetArchive",
        "action_failure_policy": "ActionFailurePolicy",
    }

    target_archive: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeliverToMailboxAction(PropertyType):
    MAILBOX_ARN = "MailboxArn"
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mailbox_arn": "MailboxArn",
        "action_failure_policy": "ActionFailurePolicy",
        "role_arn": "RoleArn",
    }

    mailbox_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeliverToQBusinessAction(PropertyType):
    INDEX_ID = "IndexId"
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"
    APPLICATION_ID = "ApplicationId"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_id": "IndexId",
        "action_failure_policy": "ActionFailurePolicy",
        "application_id": "ApplicationId",
        "role_arn": "RoleArn",
    }

    index_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RelayAction(PropertyType):
    RELAY = "Relay"
    MAIL_FROM = "MailFrom"
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "relay": "Relay",
        "mail_from": "MailFrom",
        "action_failure_policy": "ActionFailurePolicy",
    }

    relay: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mail_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplaceRecipientAction(PropertyType):
    REPLACE_WITH = "ReplaceWith"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replace_with": "ReplaceWith",
    }

    replace_with: Optional[Union[list[str], Ref]] = None


@dataclass
class Rule(PropertyType):
    ACTIONS = "Actions"
    CONDITIONS = "Conditions"
    UNLESS = "Unless"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "conditions": "Conditions",
        "unless": "Unless",
        "name": "Name",
    }

    actions: Optional[list[RuleAction]] = None
    conditions: Optional[list[RuleCondition]] = None
    unless: Optional[list[RuleCondition]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleAction(PropertyType):
    ADD_HEADER = "AddHeader"
    RELAY = "Relay"
    DELIVER_TO_MAILBOX = "DeliverToMailbox"
    ARCHIVE = "Archive"
    REPLACE_RECIPIENT = "ReplaceRecipient"
    WRITE_TO_S3 = "WriteToS3"
    PUBLISH_TO_SNS = "PublishToSns"
    DELIVER_TO_Q_BUSINESS = "DeliverToQBusiness"
    DROP = "Drop"
    SEND = "Send"

    _property_mappings: ClassVar[dict[str, str]] = {
        "add_header": "AddHeader",
        "relay": "Relay",
        "deliver_to_mailbox": "DeliverToMailbox",
        "archive": "Archive",
        "replace_recipient": "ReplaceRecipient",
        "write_to_s3": "WriteToS3",
        "publish_to_sns": "PublishToSns",
        "deliver_to_q_business": "DeliverToQBusiness",
        "drop": "Drop",
        "send": "Send",
    }

    add_header: Optional[AddHeaderAction] = None
    relay: Optional[RelayAction] = None
    deliver_to_mailbox: Optional[DeliverToMailboxAction] = None
    archive: Optional[ArchiveAction] = None
    replace_recipient: Optional[ReplaceRecipientAction] = None
    write_to_s3: Optional[S3Action] = None
    publish_to_sns: Optional[SnsAction] = None
    deliver_to_q_business: Optional[DeliverToQBusinessAction] = None
    drop: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    send: Optional[SendAction] = None


@dataclass
class RuleBooleanExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[RuleBooleanToEvaluate] = None


@dataclass
class RuleBooleanToEvaluate(PropertyType):
    IS_IN_ADDRESS_LIST = "IsInAddressList"
    ATTRIBUTE = "Attribute"
    ANALYSIS = "Analysis"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_in_address_list": "IsInAddressList",
        "attribute": "Attribute",
        "analysis": "Analysis",
    }

    is_in_address_list: Optional[RuleIsInAddressList] = None
    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    analysis: Optional[Analysis] = None


@dataclass
class RuleCondition(PropertyType):
    BOOLEAN_EXPRESSION = "BooleanExpression"
    VERDICT_EXPRESSION = "VerdictExpression"
    STRING_EXPRESSION = "StringExpression"
    DMARC_EXPRESSION = "DmarcExpression"
    NUMBER_EXPRESSION = "NumberExpression"
    IP_EXPRESSION = "IpExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "boolean_expression": "BooleanExpression",
        "verdict_expression": "VerdictExpression",
        "string_expression": "StringExpression",
        "dmarc_expression": "DmarcExpression",
        "number_expression": "NumberExpression",
        "ip_expression": "IpExpression",
    }

    boolean_expression: Optional[RuleBooleanExpression] = None
    verdict_expression: Optional[RuleVerdictExpression] = None
    string_expression: Optional[RuleStringExpression] = None
    dmarc_expression: Optional[RuleDmarcExpression] = None
    number_expression: Optional[RuleNumberExpression] = None
    ip_expression: Optional[RuleIpExpression] = None


@dataclass
class RuleDmarcExpression(PropertyType):
    OPERATOR = "Operator"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class RuleIpExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[RuleIpToEvaluate] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class RuleIpToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleIsInAddressList(PropertyType):
    ATTRIBUTE = "Attribute"
    ADDRESS_LISTS = "AddressLists"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "address_lists": "AddressLists",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address_lists: Optional[Union[list[str], Ref]] = None


@dataclass
class RuleNumberExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "value": "Value",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[RuleNumberToEvaluate] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class RuleNumberToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleStringExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[RuleStringToEvaluate] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class RuleStringToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"
    MIME_HEADER_ATTRIBUTE = "MimeHeaderAttribute"
    ANALYSIS = "Analysis"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "mime_header_attribute": "MimeHeaderAttribute",
        "analysis": "Analysis",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mime_header_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    analysis: Optional[Analysis] = None


@dataclass
class RuleVerdictExpression(PropertyType):
    OPERATOR = "Operator"
    EVALUATE = "Evaluate"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "evaluate": "Evaluate",
        "values": "Values",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate: Optional[RuleVerdictToEvaluate] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class RuleVerdictToEvaluate(PropertyType):
    ATTRIBUTE = "Attribute"
    ANALYSIS = "Analysis"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "analysis": "Analysis",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    analysis: Optional[Analysis] = None


@dataclass
class S3Action(PropertyType):
    S3_SSE_KMS_KEY_ID = "S3SseKmsKeyId"
    S3_BUCKET = "S3Bucket"
    S3_PREFIX = "S3Prefix"
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_sse_kms_key_id": "S3SseKmsKeyId",
        "s3_bucket": "S3Bucket",
        "s3_prefix": "S3Prefix",
        "action_failure_policy": "ActionFailurePolicy",
        "role_arn": "RoleArn",
    }

    s3_sse_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SendAction(PropertyType):
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action_failure_policy": "ActionFailurePolicy",
        "role_arn": "RoleArn",
    }

    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnsAction(PropertyType):
    TOPIC_ARN = "TopicArn"
    ENCODING = "Encoding"
    ACTION_FAILURE_POLICY = "ActionFailurePolicy"
    ROLE_ARN = "RoleArn"
    PAYLOAD_TYPE = "PayloadType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
        "encoding": "Encoding",
        "action_failure_policy": "ActionFailurePolicy",
        "role_arn": "RoleArn",
        "payload_type": "PayloadType",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encoding: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_failure_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

