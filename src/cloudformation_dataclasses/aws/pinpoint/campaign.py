"""PropertyTypes for AWS::Pinpoint::Campaign."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeDimension(PropertyType):
    ATTRIBUTE_TYPE = "AttributeType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_type": "AttributeType",
        "values": "Values",
    }

    attribute_type: Optional[Union[str, AttributeType, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class CampaignCustomMessage(PropertyType):
    DATA = "Data"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data": "Data",
    }

    data: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CampaignEmailMessage(PropertyType):
    FROM_ADDRESS = "FromAddress"
    HTML_BODY = "HtmlBody"
    TITLE = "Title"
    BODY = "Body"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_address": "FromAddress",
        "html_body": "HtmlBody",
        "title": "Title",
        "body": "Body",
    }

    from_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    html_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CampaignEventFilter(PropertyType):
    FILTER_TYPE = "FilterType"
    DIMENSIONS = "Dimensions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_type": "FilterType",
        "dimensions": "Dimensions",
    }

    filter_type: Optional[Union[str, FilterType, Ref, GetAtt, Sub]] = None
    dimensions: Optional[EventDimensions] = None


@dataclass
class CampaignHook(PropertyType):
    MODE = "Mode"
    WEB_URL = "WebUrl"
    LAMBDA_FUNCTION_NAME = "LambdaFunctionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "web_url": "WebUrl",
        "lambda_function_name": "LambdaFunctionName",
    }

    mode: Optional[Union[str, Mode, Ref, GetAtt, Sub]] = None
    web_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_function_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CampaignInAppMessage(PropertyType):
    CUSTOM_CONFIG = "CustomConfig"
    LAYOUT = "Layout"
    CONTENT = "Content"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_config": "CustomConfig",
        "layout": "Layout",
        "content": "Content",
    }

    custom_config: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    layout: Optional[Union[str, Layout, Ref, GetAtt, Sub]] = None
    content: Optional[list[InAppMessageContent]] = None


@dataclass
class CampaignSmsMessage(PropertyType):
    ENTITY_ID = "EntityId"
    ORIGINATION_NUMBER = "OriginationNumber"
    SENDER_ID = "SenderId"
    BODY = "Body"
    MESSAGE_TYPE = "MessageType"
    TEMPLATE_ID = "TemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id": "EntityId",
        "origination_number": "OriginationNumber",
        "sender_id": "SenderId",
        "body": "Body",
        "message_type": "MessageType",
        "template_id": "TemplateId",
    }

    entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origination_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sender_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_type: Optional[Union[str, MessageType, Ref, GetAtt, Sub]] = None
    template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomDeliveryConfiguration(PropertyType):
    DELIVERY_URI = "DeliveryUri"
    ENDPOINT_TYPES = "EndpointTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_uri": "DeliveryUri",
        "endpoint_types": "EndpointTypes",
    }

    delivery_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_types: Optional[Union[list[str], Ref]] = None


@dataclass
class DefaultButtonConfiguration(PropertyType):
    BUTTON_ACTION = "ButtonAction"
    BORDER_RADIUS = "BorderRadius"
    TEXT = "Text"
    TEXT_COLOR = "TextColor"
    LINK = "Link"
    BACKGROUND_COLOR = "BackgroundColor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "button_action": "ButtonAction",
        "border_radius": "BorderRadius",
        "text": "Text",
        "text_color": "TextColor",
        "link": "Link",
        "background_color": "BackgroundColor",
    }

    button_action: Optional[Union[str, ButtonAction, Ref, GetAtt, Sub]] = None
    border_radius: Optional[Union[int, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    link: Optional[Union[str, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventDimensions(PropertyType):
    METRICS = "Metrics"
    EVENT_TYPE = "EventType"
    ATTRIBUTES = "Attributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metrics": "Metrics",
        "event_type": "EventType",
        "attributes": "Attributes",
    }

    metrics: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    event_type: Optional[SetDimension] = None
    attributes: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class InAppMessageBodyConfig(PropertyType):
    ALIGNMENT = "Alignment"
    TEXT_COLOR = "TextColor"
    BODY = "Body"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alignment": "Alignment",
        "text_color": "TextColor",
        "body": "Body",
    }

    alignment: Optional[Union[str, Alignment, Ref, GetAtt, Sub]] = None
    text_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InAppMessageButton(PropertyType):
    WEB = "Web"
    DEFAULT_CONFIG = "DefaultConfig"
    IOS = "IOS"
    ANDROID = "Android"

    _property_mappings: ClassVar[dict[str, str]] = {
        "web": "Web",
        "default_config": "DefaultConfig",
        "ios": "IOS",
        "android": "Android",
    }

    web: Optional[OverrideButtonConfiguration] = None
    default_config: Optional[DefaultButtonConfiguration] = None
    ios: Optional[OverrideButtonConfiguration] = None
    android: Optional[OverrideButtonConfiguration] = None


@dataclass
class InAppMessageContent(PropertyType):
    BODY_CONFIG = "BodyConfig"
    SECONDARY_BTN = "SecondaryBtn"
    IMAGE_URL = "ImageUrl"
    PRIMARY_BTN = "PrimaryBtn"
    HEADER_CONFIG = "HeaderConfig"
    BACKGROUND_COLOR = "BackgroundColor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "body_config": "BodyConfig",
        "secondary_btn": "SecondaryBtn",
        "image_url": "ImageUrl",
        "primary_btn": "PrimaryBtn",
        "header_config": "HeaderConfig",
        "background_color": "BackgroundColor",
    }

    body_config: Optional[InAppMessageBodyConfig] = None
    secondary_btn: Optional[InAppMessageButton] = None
    image_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_btn: Optional[InAppMessageButton] = None
    header_config: Optional[InAppMessageHeaderConfig] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InAppMessageHeaderConfig(PropertyType):
    ALIGNMENT = "Alignment"
    HEADER = "Header"
    TEXT_COLOR = "TextColor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alignment": "Alignment",
        "header": "Header",
        "text_color": "TextColor",
    }

    alignment: Optional[Union[str, Alignment, Ref, GetAtt, Sub]] = None
    header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Limits(PropertyType):
    DAILY = "Daily"
    MAXIMUM_DURATION = "MaximumDuration"
    TOTAL = "Total"
    MESSAGES_PER_SECOND = "MessagesPerSecond"
    SESSION = "Session"

    _property_mappings: ClassVar[dict[str, str]] = {
        "daily": "Daily",
        "maximum_duration": "MaximumDuration",
        "total": "Total",
        "messages_per_second": "MessagesPerSecond",
        "session": "Session",
    }

    daily: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None
    total: Optional[Union[int, Ref, GetAtt, Sub]] = None
    messages_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    session: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Message(PropertyType):
    JSON_BODY = "JsonBody"
    ACTION = "Action"
    MEDIA_URL = "MediaUrl"
    TIME_TO_LIVE = "TimeToLive"
    IMAGE_SMALL_ICON_URL = "ImageSmallIconUrl"
    IMAGE_URL = "ImageUrl"
    TITLE = "Title"
    IMAGE_ICON_URL = "ImageIconUrl"
    SILENT_PUSH = "SilentPush"
    BODY = "Body"
    RAW_CONTENT = "RawContent"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json_body": "JsonBody",
        "action": "Action",
        "media_url": "MediaUrl",
        "time_to_live": "TimeToLive",
        "image_small_icon_url": "ImageSmallIconUrl",
        "image_url": "ImageUrl",
        "title": "Title",
        "image_icon_url": "ImageIconUrl",
        "silent_push": "SilentPush",
        "body": "Body",
        "raw_content": "RawContent",
        "url": "Url",
    }

    json_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    media_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_to_live: Optional[Union[int, Ref, GetAtt, Sub]] = None
    image_small_icon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_icon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    silent_push: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    raw_content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MessageConfiguration(PropertyType):
    APNS_MESSAGE = "APNSMessage"
    BAIDU_MESSAGE = "BaiduMessage"
    DEFAULT_MESSAGE = "DefaultMessage"
    IN_APP_MESSAGE = "InAppMessage"
    EMAIL_MESSAGE = "EmailMessage"
    GCM_MESSAGE = "GCMMessage"
    SMS_MESSAGE = "SMSMessage"
    CUSTOM_MESSAGE = "CustomMessage"
    ADM_MESSAGE = "ADMMessage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "apns_message": "APNSMessage",
        "baidu_message": "BaiduMessage",
        "default_message": "DefaultMessage",
        "in_app_message": "InAppMessage",
        "email_message": "EmailMessage",
        "gcm_message": "GCMMessage",
        "sms_message": "SMSMessage",
        "custom_message": "CustomMessage",
        "adm_message": "ADMMessage",
    }

    apns_message: Optional[Message] = None
    baidu_message: Optional[Message] = None
    default_message: Optional[Message] = None
    in_app_message: Optional[CampaignInAppMessage] = None
    email_message: Optional[CampaignEmailMessage] = None
    gcm_message: Optional[Message] = None
    sms_message: Optional[CampaignSmsMessage] = None
    custom_message: Optional[CampaignCustomMessage] = None
    adm_message: Optional[Message] = None


@dataclass
class MetricDimension(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "value": "Value",
    }

    comparison_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OverrideButtonConfiguration(PropertyType):
    BUTTON_ACTION = "ButtonAction"
    LINK = "Link"

    _property_mappings: ClassVar[dict[str, str]] = {
        "button_action": "ButtonAction",
        "link": "Link",
    }

    button_action: Optional[Union[str, ButtonAction, Ref, GetAtt, Sub]] = None
    link: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuietTime(PropertyType):
    START = "Start"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    TIME_ZONE = "TimeZone"
    QUIET_TIME = "QuietTime"
    END_TIME = "EndTime"
    START_TIME = "StartTime"
    FREQUENCY = "Frequency"
    EVENT_FILTER = "EventFilter"
    IS_LOCAL_TIME = "IsLocalTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "time_zone": "TimeZone",
        "quiet_time": "QuietTime",
        "end_time": "EndTime",
        "start_time": "StartTime",
        "frequency": "Frequency",
        "event_filter": "EventFilter",
        "is_local_time": "IsLocalTime",
    }

    time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    quiet_time: Optional[QuietTime] = None
    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    frequency: Optional[Union[str, Frequency, Ref, GetAtt, Sub]] = None
    event_filter: Optional[CampaignEventFilter] = None
    is_local_time: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SetDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, DimensionType, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Template(PropertyType):
    VERSION = "Version"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "name": "Name",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateConfiguration(PropertyType):
    SMS_TEMPLATE = "SMSTemplate"
    EMAIL_TEMPLATE = "EmailTemplate"
    PUSH_TEMPLATE = "PushTemplate"
    VOICE_TEMPLATE = "VoiceTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sms_template": "SMSTemplate",
        "email_template": "EmailTemplate",
        "push_template": "PushTemplate",
        "voice_template": "VoiceTemplate",
    }

    sms_template: Optional[Template] = None
    email_template: Optional[Template] = None
    push_template: Optional[Template] = None
    voice_template: Optional[Template] = None


@dataclass
class WriteTreatmentResource(PropertyType):
    TREATMENT_DESCRIPTION = "TreatmentDescription"
    MESSAGE_CONFIGURATION = "MessageConfiguration"
    SCHEDULE = "Schedule"
    TEMPLATE_CONFIGURATION = "TemplateConfiguration"
    CUSTOM_DELIVERY_CONFIGURATION = "CustomDeliveryConfiguration"
    SIZE_PERCENT = "SizePercent"
    TREATMENT_NAME = "TreatmentName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "treatment_description": "TreatmentDescription",
        "message_configuration": "MessageConfiguration",
        "schedule": "Schedule",
        "template_configuration": "TemplateConfiguration",
        "custom_delivery_configuration": "CustomDeliveryConfiguration",
        "size_percent": "SizePercent",
        "treatment_name": "TreatmentName",
    }

    treatment_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_configuration: Optional[MessageConfiguration] = None
    schedule: Optional[Schedule] = None
    template_configuration: Optional[TemplateConfiguration] = None
    custom_delivery_configuration: Optional[CustomDeliveryConfiguration] = None
    size_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    treatment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

