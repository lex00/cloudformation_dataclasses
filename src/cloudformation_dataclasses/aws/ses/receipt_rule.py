"""PropertyTypes for AWS::SES::ReceiptRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connect_action": "ConnectAction",
        "bounce_action": "BounceAction",
        "s3_action": "S3Action",
        "stop_action": "StopAction",
        "sns_action": "SNSAction",
        "workmail_action": "WorkmailAction",
        "add_header_action": "AddHeaderAction",
        "lambda_action": "LambdaAction",
    }

    connect_action: Optional[ConnectAction] = None
    bounce_action: Optional[BounceAction] = None
    s3_action: Optional[S3Action] = None
    stop_action: Optional[StopAction] = None
    sns_action: Optional[SNSAction] = None
    workmail_action: Optional[WorkmailAction] = None
    add_header_action: Optional[AddHeaderAction] = None
    lambda_action: Optional[LambdaAction] = None


@dataclass
class AddHeaderAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header_value": "HeaderValue",
        "header_name": "HeaderName",
    }

    header_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BounceAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sender": "Sender",
        "smtp_reply_code": "SmtpReplyCode",
        "message": "Message",
        "topic_arn": "TopicArn",
        "status_code": "StatusCode",
    }

    sender: Optional[Union[str, Ref, GetAtt, Sub]] = None
    smtp_reply_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_arn": "InstanceARN",
        "iam_role_arn": "IAMRoleARN",
    }

    instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionArn",
        "topic_arn": "TopicArn",
        "invocation_type": "InvocationType",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invocation_type: Optional[Union[str, InvocationType, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scan_enabled": "ScanEnabled",
        "recipients": "Recipients",
        "actions": "Actions",
        "enabled": "Enabled",
        "name": "Name",
        "tls_policy": "TlsPolicy",
    }

    scan_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    recipients: Optional[Union[list[str], Ref]] = None
    actions: Optional[list[Action]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tls_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "kms_key_arn": "KmsKeyArn",
        "topic_arn": "TopicArn",
        "object_key_prefix": "ObjectKeyPrefix",
        "iam_role_arn": "IamRoleArn",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SNSAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
        "encoding": "Encoding",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encoding: Optional[Union[str, SNSActionEncoding, Ref, GetAtt, Sub]] = None


@dataclass
class StopAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "topic_arn": "TopicArn",
    }

    scope: Optional[Union[str, StopScope, Ref, GetAtt, Sub]] = None
    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkmailAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
        "organization_arn": "OrganizationArn",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organization_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

