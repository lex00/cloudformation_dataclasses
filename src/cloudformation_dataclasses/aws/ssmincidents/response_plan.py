"""PropertyTypes for AWS::SSMIncidents::ResponsePlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    SSM_AUTOMATION = "SsmAutomation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssm_automation": "SsmAutomation",
    }

    ssm_automation: Optional[SsmAutomation] = None


@dataclass
class ChatChannel(PropertyType):
    CHATBOT_SNS = "ChatbotSns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "chatbot_sns": "ChatbotSns",
    }

    chatbot_sns: Optional[Union[list[str], Ref]] = None


@dataclass
class DynamicSsmParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[DynamicSsmParameterValue] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynamicSsmParameterValue(PropertyType):
    VARIABLE = "Variable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variable": "Variable",
    }

    variable: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IncidentTemplate(PropertyType):
    IMPACT = "Impact"
    INCIDENT_TAGS = "IncidentTags"
    SUMMARY = "Summary"
    TITLE = "Title"
    NOTIFICATION_TARGETS = "NotificationTargets"
    DEDUPE_STRING = "DedupeString"

    _property_mappings: ClassVar[dict[str, str]] = {
        "impact": "Impact",
        "incident_tags": "IncidentTags",
        "summary": "Summary",
        "title": "Title",
        "notification_targets": "NotificationTargets",
        "dedupe_string": "DedupeString",
    }

    impact: Optional[Union[int, Ref, GetAtt, Sub]] = None
    incident_tags: Optional[list[Tag]] = None
    summary: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_targets: Optional[list[NotificationTargetItem]] = None
    dedupe_string: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Integration(PropertyType):
    PAGER_DUTY_CONFIGURATION = "PagerDutyConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pager_duty_configuration": "PagerDutyConfiguration",
    }

    pager_duty_configuration: Optional[PagerDutyConfiguration] = None


@dataclass
class NotificationTargetItem(PropertyType):
    SNS_TOPIC_ARN = "SnsTopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_topic_arn": "SnsTopicArn",
    }

    sns_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PagerDutyConfiguration(PropertyType):
    SECRET_ID = "SecretId"
    PAGER_DUTY_INCIDENT_CONFIGURATION = "PagerDutyIncidentConfiguration"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_id": "SecretId",
        "pager_duty_incident_configuration": "PagerDutyIncidentConfiguration",
        "name": "Name",
    }

    secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pager_duty_incident_configuration: Optional[PagerDutyIncidentConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PagerDutyIncidentConfiguration(PropertyType):
    SERVICE_ID = "ServiceId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_id": "ServiceId",
    }

    service_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SsmAutomation(PropertyType):
    PARAMETERS = "Parameters"
    TARGET_ACCOUNT = "TargetAccount"
    DYNAMIC_PARAMETERS = "DynamicParameters"
    DOCUMENT_VERSION = "DocumentVersion"
    ROLE_ARN = "RoleArn"
    DOCUMENT_NAME = "DocumentName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "target_account": "TargetAccount",
        "dynamic_parameters": "DynamicParameters",
        "document_version": "DocumentVersion",
        "role_arn": "RoleArn",
        "document_name": "DocumentName",
    }

    parameters: Optional[list[SsmParameter]] = None
    target_account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dynamic_parameters: Optional[list[DynamicSsmParameter]] = None
    document_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    document_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SsmParameter(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

