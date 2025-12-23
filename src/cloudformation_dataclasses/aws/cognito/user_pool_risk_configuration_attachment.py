"""PropertyTypes for AWS::Cognito::UserPoolRiskConfigurationAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccountTakeoverActionType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notify": "Notify",
        "event_action": "EventAction",
    }

    notify: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    event_action: Optional[Union[str, AccountTakeoverEventActionType, Ref, GetAtt, Sub]] = None


@dataclass
class AccountTakeoverActionsType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "high_action": "HighAction",
        "low_action": "LowAction",
        "medium_action": "MediumAction",
    }

    high_action: Optional[AccountTakeoverActionType] = None
    low_action: Optional[AccountTakeoverActionType] = None
    medium_action: Optional[AccountTakeoverActionType] = None


@dataclass
class AccountTakeoverRiskConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "notify_configuration": "NotifyConfiguration",
    }

    actions: Optional[AccountTakeoverActionsType] = None
    notify_configuration: Optional[NotifyConfigurationType] = None


@dataclass
class CompromisedCredentialsActionsType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_action": "EventAction",
    }

    event_action: Optional[Union[str, CompromisedCredentialsEventActionType, Ref, GetAtt, Sub]] = None


@dataclass
class CompromisedCredentialsRiskConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "event_filter": "EventFilter",
    }

    actions: Optional[CompromisedCredentialsActionsType] = None
    event_filter: Optional[Union[list[str], Ref]] = None


@dataclass
class NotifyConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "block_email": "BlockEmail",
        "reply_to": "ReplyTo",
        "source_arn": "SourceArn",
        "no_action_email": "NoActionEmail",
        "from_": "From",
        "mfa_email": "MfaEmail",
    }

    block_email: Optional[NotifyEmailType] = None
    reply_to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    no_action_email: Optional[NotifyEmailType] = None
    from_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mfa_email: Optional[NotifyEmailType] = None


@dataclass
class NotifyEmailType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_body": "TextBody",
        "html_body": "HtmlBody",
        "subject": "Subject",
    }

    text_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    html_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RiskExceptionConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "blocked_ip_range_list": "BlockedIPRangeList",
        "skipped_ip_range_list": "SkippedIPRangeList",
    }

    blocked_ip_range_list: Optional[Union[list[str], Ref]] = None
    skipped_ip_range_list: Optional[Union[list[str], Ref]] = None

