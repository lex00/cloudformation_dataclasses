"""PropertyTypes for AWS::ConnectCampaignsV2::Campaign."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AgentAction:
    """AgentAction enum values."""

    DISCARD = "DISCARD"


class CampaignDeletionPolicy:
    """CampaignDeletionPolicy enum values."""

    RETAIN_ALL = "RETAIN_ALL"
    DELETE_ALL = "DELETE_ALL"


class CampaignState:
    """CampaignState enum values."""

    INITIALIZED = "Initialized"
    RUNNING = "Running"
    PAUSED = "Paused"
    STOPPED = "Stopped"
    FAILED = "Failed"
    COMPLETED = "Completed"


class ChannelSubtype:
    """ChannelSubtype enum values."""

    TELEPHONY = "TELEPHONY"
    SMS = "SMS"
    EMAIL = "EMAIL"
    WHATSAPP = "WHATSAPP"


class CommunicationLimitTimeUnit:
    """CommunicationLimitTimeUnit enum values."""

    DAY = "DAY"


class CommunicationLimitsConfigType:
    """CommunicationLimitsConfigType enum values."""

    ALL_CHANNEL_SUBTYPES = "ALL_CHANNEL_SUBTYPES"


class CommunicationTimeConfigType:
    """CommunicationTimeConfigType enum values."""

    TELEPHONY = "TELEPHONY"
    SMS = "SMS"
    EMAIL = "EMAIL"
    WHATSAPP = "WHATSAPP"


class DayOfWeek:
    """DayOfWeek enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class EncryptionType:
    """EncryptionType enum values."""

    KMS = "KMS"


class EventType:
    """EventType enum values."""

    CAMPAIGN_EMAIL = "Campaign-Email"
    CAMPAIGN_SMS = "Campaign-SMS"
    CAMPAIGN_TELEPHONY = "Campaign-Telephony"
    CAMPAIGN_ORCHESTRATION = "Campaign-Orchestration"


class ExternalCampaignType:
    """ExternalCampaignType enum values."""

    MANAGED = "MANAGED"
    JOURNEY = "JOURNEY"


class FailureCode:
    """FailureCode enum values."""

    INVALIDINPUT = "InvalidInput"
    REQUESTTHROTTLED = "RequestThrottled"
    UNKNOWNERROR = "UnknownError"
    BUFFERLIMITEXCEEDED = "BufferLimitExceeded"


class GetCampaignStateBatchFailureCode:
    """GetCampaignStateBatchFailureCode enum values."""

    RESOURCENOTFOUND = "ResourceNotFound"
    UNKNOWNERROR = "UnknownError"


class InstanceIdFilterOperator:
    """InstanceIdFilterOperator enum values."""

    EQ = "Eq"


class InstanceLimitsHandling:
    """InstanceLimitsHandling enum values."""

    OPT_IN = "OPT_IN"
    OPT_OUT = "OPT_OUT"


class InstanceOnboardingJobFailureCode:
    """InstanceOnboardingJobFailureCode enum values."""

    EVENT_BRIDGE_ACCESS_DENIED = "EVENT_BRIDGE_ACCESS_DENIED"
    EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED = "EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED"
    IAM_ACCESS_DENIED = "IAM_ACCESS_DENIED"
    KMS_ACCESS_DENIED = "KMS_ACCESS_DENIED"
    KMS_KEY_NOT_FOUND = "KMS_KEY_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class InstanceOnboardingJobStatusCode:
    """InstanceOnboardingJobStatusCode enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class LocalTimeZoneDetectionType:
    """LocalTimeZoneDetectionType enum values."""

    ZIP_CODE = "ZIP_CODE"
    AREA_CODE = "AREA_CODE"


class ProfileOutboundRequestFailureCode:
    """ProfileOutboundRequestFailureCode enum values."""

    UNKNOWNERROR = "UnknownError"
    RESOURCENOTFOUND = "ResourceNotFound"
    CONFLICT = "Conflict"
    REQUESTTHROTTLED = "RequestThrottled"
    INVALIDINPUT = "InvalidInput"


@dataclass
class AnswerMachineDetectionConfig(PropertyType):
    ENABLE_ANSWER_MACHINE_DETECTION = "EnableAnswerMachineDetection"
    AWAIT_ANSWER_MACHINE_PROMPT = "AwaitAnswerMachinePrompt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_answer_machine_detection": "EnableAnswerMachineDetection",
        "await_answer_machine_prompt": "AwaitAnswerMachinePrompt",
    }

    enable_answer_machine_detection: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    await_answer_machine_prompt: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ChannelSubtypeConfig(PropertyType):
    EMAIL = "Email"
    TELEPHONY = "Telephony"
    SMS = "Sms"
    WHATS_APP = "WhatsApp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email": "Email",
        "telephony": "Telephony",
        "sms": "Sms",
        "whats_app": "WhatsApp",
    }

    email: Optional[EmailChannelSubtypeConfig] = None
    telephony: Optional[TelephonyChannelSubtypeConfig] = None
    sms: Optional[SmsChannelSubtypeConfig] = None
    whats_app: Optional[WhatsAppChannelSubtypeConfig] = None


@dataclass
class CommunicationLimit(PropertyType):
    FREQUENCY = "Frequency"
    MAX_COUNT_PER_RECIPIENT = "MaxCountPerRecipient"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "frequency": "Frequency",
        "max_count_per_recipient": "MaxCountPerRecipient",
        "unit": "Unit",
    }

    frequency: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_count_per_recipient: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CommunicationLimits(PropertyType):
    COMMUNICATION_LIMIT_LIST = "CommunicationLimitList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "communication_limit_list": "CommunicationLimitList",
    }

    communication_limit_list: Optional[list[CommunicationLimit]] = None


@dataclass
class CommunicationLimitsConfig(PropertyType):
    ALL_CHANNELS_SUBTYPES = "AllChannelsSubtypes"
    INSTANCE_LIMITS_HANDLING = "InstanceLimitsHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_channels_subtypes": "AllChannelsSubtypes",
        "instance_limits_handling": "InstanceLimitsHandling",
    }

    all_channels_subtypes: Optional[CommunicationLimits] = None
    instance_limits_handling: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CommunicationTimeConfig(PropertyType):
    LOCAL_TIME_ZONE_CONFIG = "LocalTimeZoneConfig"
    EMAIL = "Email"
    TELEPHONY = "Telephony"
    SMS = "Sms"
    WHATS_APP = "WhatsApp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "local_time_zone_config": "LocalTimeZoneConfig",
        "email": "Email",
        "telephony": "Telephony",
        "sms": "Sms",
        "whats_app": "WhatsApp",
    }

    local_time_zone_config: Optional[LocalTimeZoneConfig] = None
    email: Optional[TimeWindow] = None
    telephony: Optional[TimeWindow] = None
    sms: Optional[TimeWindow] = None
    whats_app: Optional[TimeWindow] = None


@dataclass
class DailyHour(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[list[TimeRange]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmailChannelSubtypeConfig(PropertyType):
    OUTBOUND_MODE = "OutboundMode"
    CAPACITY = "Capacity"
    DEFAULT_OUTBOUND_CONFIG = "DefaultOutboundConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outbound_mode": "OutboundMode",
        "capacity": "Capacity",
        "default_outbound_config": "DefaultOutboundConfig",
    }

    outbound_mode: Optional[EmailOutboundMode] = None
    capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    default_outbound_config: Optional[EmailOutboundConfig] = None


@dataclass
class EmailOutboundConfig(PropertyType):
    CONNECT_SOURCE_EMAIL_ADDRESS = "ConnectSourceEmailAddress"
    SOURCE_EMAIL_ADDRESS_DISPLAY_NAME = "SourceEmailAddressDisplayName"
    WISDOM_TEMPLATE_ARN = "WisdomTemplateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connect_source_email_address": "ConnectSourceEmailAddress",
        "source_email_address_display_name": "SourceEmailAddressDisplayName",
        "wisdom_template_arn": "WisdomTemplateArn",
    }

    connect_source_email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_email_address_display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    wisdom_template_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmailOutboundMode(PropertyType):
    AGENTLESS_CONFIG = "AgentlessConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agentless_config": "AgentlessConfig",
    }

    agentless_config: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class EventTrigger(PropertyType):
    CUSTOMER_PROFILES_DOMAIN_ARN = "CustomerProfilesDomainArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_profiles_domain_arn": "CustomerProfilesDomainArn",
    }

    customer_profiles_domain_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LocalTimeZoneConfig(PropertyType):
    DEFAULT_TIME_ZONE = "DefaultTimeZone"
    LOCAL_TIME_ZONE_DETECTION = "LocalTimeZoneDetection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_time_zone": "DefaultTimeZone",
        "local_time_zone_detection": "LocalTimeZoneDetection",
    }

    default_time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_time_zone_detection: Optional[Union[list[str], Ref]] = None


@dataclass
class OpenHours(PropertyType):
    DAILY_HOURS = "DailyHours"

    _property_mappings: ClassVar[dict[str, str]] = {
        "daily_hours": "DailyHours",
    }

    daily_hours: Optional[list[DailyHour]] = None


@dataclass
class PredictiveConfig(PropertyType):
    BANDWIDTH_ALLOCATION = "BandwidthAllocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bandwidth_allocation": "BandwidthAllocation",
    }

    bandwidth_allocation: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PreviewConfig(PropertyType):
    TIMEOUT_CONFIG = "TimeoutConfig"
    AGENT_ACTIONS = "AgentActions"
    BANDWIDTH_ALLOCATION = "BandwidthAllocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_config": "TimeoutConfig",
        "agent_actions": "AgentActions",
        "bandwidth_allocation": "BandwidthAllocation",
    }

    timeout_config: Optional[TimeoutConfig] = None
    agent_actions: Optional[Union[list[str], Ref]] = None
    bandwidth_allocation: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ProgressiveConfig(PropertyType):
    BANDWIDTH_ALLOCATION = "BandwidthAllocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bandwidth_allocation": "BandwidthAllocation",
    }

    bandwidth_allocation: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class RestrictedPeriod(PropertyType):
    START_DATE = "StartDate"
    END_DATE = "EndDate"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start_date": "StartDate",
        "end_date": "EndDate",
        "name": "Name",
    }

    start_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RestrictedPeriods(PropertyType):
    RESTRICTED_PERIOD_LIST = "RestrictedPeriodList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "restricted_period_list": "RestrictedPeriodList",
    }

    restricted_period_list: Optional[list[RestrictedPeriod]] = None


@dataclass
class Schedule(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"
    REFRESH_FREQUENCY = "RefreshFrequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
        "refresh_frequency": "RefreshFrequency",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SmsChannelSubtypeConfig(PropertyType):
    OUTBOUND_MODE = "OutboundMode"
    CAPACITY = "Capacity"
    DEFAULT_OUTBOUND_CONFIG = "DefaultOutboundConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outbound_mode": "OutboundMode",
        "capacity": "Capacity",
        "default_outbound_config": "DefaultOutboundConfig",
    }

    outbound_mode: Optional[SmsOutboundMode] = None
    capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    default_outbound_config: Optional[SmsOutboundConfig] = None


@dataclass
class SmsOutboundConfig(PropertyType):
    CONNECT_SOURCE_PHONE_NUMBER_ARN = "ConnectSourcePhoneNumberArn"
    WISDOM_TEMPLATE_ARN = "WisdomTemplateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connect_source_phone_number_arn": "ConnectSourcePhoneNumberArn",
        "wisdom_template_arn": "WisdomTemplateArn",
    }

    connect_source_phone_number_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    wisdom_template_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SmsOutboundMode(PropertyType):
    AGENTLESS_CONFIG = "AgentlessConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agentless_config": "AgentlessConfig",
    }

    agentless_config: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    CUSTOMER_PROFILES_SEGMENT_ARN = "CustomerProfilesSegmentArn"
    EVENT_TRIGGER = "EventTrigger"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_profiles_segment_arn": "CustomerProfilesSegmentArn",
        "event_trigger": "EventTrigger",
    }

    customer_profiles_segment_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_trigger: Optional[EventTrigger] = None


@dataclass
class TelephonyChannelSubtypeConfig(PropertyType):
    OUTBOUND_MODE = "OutboundMode"
    CAPACITY = "Capacity"
    CONNECT_QUEUE_ID = "ConnectQueueId"
    DEFAULT_OUTBOUND_CONFIG = "DefaultOutboundConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outbound_mode": "OutboundMode",
        "capacity": "Capacity",
        "connect_queue_id": "ConnectQueueId",
        "default_outbound_config": "DefaultOutboundConfig",
    }

    outbound_mode: Optional[TelephonyOutboundMode] = None
    capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    connect_queue_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_outbound_config: Optional[TelephonyOutboundConfig] = None


@dataclass
class TelephonyOutboundConfig(PropertyType):
    CONNECT_CONTACT_FLOW_ID = "ConnectContactFlowId"
    RING_TIMEOUT = "RingTimeout"
    ANSWER_MACHINE_DETECTION_CONFIG = "AnswerMachineDetectionConfig"
    CONNECT_SOURCE_PHONE_NUMBER = "ConnectSourcePhoneNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connect_contact_flow_id": "ConnectContactFlowId",
        "ring_timeout": "RingTimeout",
        "answer_machine_detection_config": "AnswerMachineDetectionConfig",
        "connect_source_phone_number": "ConnectSourcePhoneNumber",
    }

    connect_contact_flow_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ring_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    answer_machine_detection_config: Optional[AnswerMachineDetectionConfig] = None
    connect_source_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TelephonyOutboundMode(PropertyType):
    PROGRESSIVE_CONFIG = "ProgressiveConfig"
    PREDICTIVE_CONFIG = "PredictiveConfig"
    AGENTLESS_CONFIG = "AgentlessConfig"
    PREVIEW_CONFIG = "PreviewConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "progressive_config": "ProgressiveConfig",
        "predictive_config": "PredictiveConfig",
        "agentless_config": "AgentlessConfig",
        "preview_config": "PreviewConfig",
    }

    progressive_config: Optional[ProgressiveConfig] = None
    predictive_config: Optional[PredictiveConfig] = None
    agentless_config: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    preview_config: Optional[PreviewConfig] = None


@dataclass
class TimeRange(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeWindow(PropertyType):
    OPEN_HOURS = "OpenHours"
    RESTRICTED_PERIODS = "RestrictedPeriods"

    _property_mappings: ClassVar[dict[str, str]] = {
        "open_hours": "OpenHours",
        "restricted_periods": "RestrictedPeriods",
    }

    open_hours: Optional[OpenHours] = None
    restricted_periods: Optional[RestrictedPeriods] = None


@dataclass
class TimeoutConfig(PropertyType):
    DURATION_IN_SECONDS = "DurationInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
    }

    duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WhatsAppChannelSubtypeConfig(PropertyType):
    OUTBOUND_MODE = "OutboundMode"
    CAPACITY = "Capacity"
    DEFAULT_OUTBOUND_CONFIG = "DefaultOutboundConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outbound_mode": "OutboundMode",
        "capacity": "Capacity",
        "default_outbound_config": "DefaultOutboundConfig",
    }

    outbound_mode: Optional[WhatsAppOutboundMode] = None
    capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    default_outbound_config: Optional[WhatsAppOutboundConfig] = None


@dataclass
class WhatsAppOutboundConfig(PropertyType):
    CONNECT_SOURCE_PHONE_NUMBER_ARN = "ConnectSourcePhoneNumberArn"
    WISDOM_TEMPLATE_ARN = "WisdomTemplateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connect_source_phone_number_arn": "ConnectSourcePhoneNumberArn",
        "wisdom_template_arn": "WisdomTemplateArn",
    }

    connect_source_phone_number_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    wisdom_template_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WhatsAppOutboundMode(PropertyType):
    AGENTLESS_CONFIG = "AgentlessConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agentless_config": "AgentlessConfig",
    }

    agentless_config: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

