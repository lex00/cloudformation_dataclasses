"""PropertyTypes for AWS::IoTEvents::DetectorModel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iot_events": "IotEvents",
        "firehose": "Firehose",
        "dynamo_db": "DynamoDB",
        "iot_topic_publish": "IotTopicPublish",
        "dynamo_d_bv2": "DynamoDBv2",
        "iot_site_wise": "IotSiteWise",
        "reset_timer": "ResetTimer",
        "sqs": "Sqs",
        "set_timer": "SetTimer",
        "sns": "Sns",
        "clear_timer": "ClearTimer",
        "lambda_": "Lambda",
        "set_variable": "SetVariable",
    }

    iot_events: Optional[IotEvents] = None
    firehose: Optional[Firehose] = None
    dynamo_db: Optional[DynamoDB] = None
    iot_topic_publish: Optional[IotTopicPublish] = None
    dynamo_d_bv2: Optional[DynamoDBv2] = None
    iot_site_wise: Optional[IotSiteWise] = None
    reset_timer: Optional[ResetTimer] = None
    sqs: Optional[Sqs] = None
    set_timer: Optional[SetTimer] = None
    sns: Optional[Sns] = None
    clear_timer: Optional[ClearTimer] = None
    lambda_: Optional[Lambda] = None
    set_variable: Optional[SetVariable] = None


@dataclass
class AssetPropertyTimestamp(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time_in_seconds": "TimeInSeconds",
        "offset_in_nanos": "OffsetInNanos",
    }

    time_in_seconds: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset_in_nanos: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetPropertyValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "quality": "Quality",
        "value": "Value",
        "timestamp": "Timestamp",
    }

    quality: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[AssetPropertyVariant] = None
    timestamp: Optional[AssetPropertyTimestamp] = None


@dataclass
class AssetPropertyVariant(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "double_value": "DoubleValue",
        "boolean_value": "BooleanValue",
        "integer_value": "IntegerValue",
        "string_value": "StringValue",
    }

    double_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    boolean_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    integer_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClearTimer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timer_name": "TimerName",
    }

    timer_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DetectorModelDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "states": "States",
        "initial_state_name": "InitialStateName",
    }

    states: Optional[list[State]] = None
    initial_state_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynamoDB(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "payload_field": "PayloadField",
        "range_key_field": "RangeKeyField",
        "hash_key_field": "HashKeyField",
        "range_key_value": "RangeKeyValue",
        "range_key_type": "RangeKeyType",
        "hash_key_type": "HashKeyType",
        "hash_key_value": "HashKeyValue",
        "payload": "Payload",
        "operation": "Operation",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hash_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_key_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hash_key_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hash_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None
    operation: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynamoDBv2(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "payload": "Payload",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Event(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "actions": "Actions",
        "event_name": "EventName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    actions: Optional[list[Action]] = None
    event_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Firehose(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_name": "DeliveryStreamName",
        "payload": "Payload",
        "separator": "Separator",
    }

    delivery_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None
    separator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IotEvents(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_name": "InputName",
        "payload": "Payload",
    }

    input_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class IotSiteWise(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entry_id": "EntryId",
        "property_alias": "PropertyAlias",
        "property_value": "PropertyValue",
        "asset_id": "AssetId",
        "property_id": "PropertyId",
    }

    entry_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_value: Optional[AssetPropertyValue] = None
    asset_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IotTopicPublish(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mqtt_topic": "MqttTopic",
        "payload": "Payload",
    }

    mqtt_topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Lambda(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionArn",
        "payload": "Payload",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class OnEnter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
    }

    events: Optional[list[Event]] = None


@dataclass
class OnExit(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
    }

    events: Optional[list[Event]] = None


@dataclass
class OnInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
        "transition_events": "TransitionEvents",
    }

    events: Optional[list[Event]] = None
    transition_events: Optional[list[TransitionEvent]] = None


@dataclass
class Payload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_expression": "ContentExpression",
        "type_": "Type",
    }

    content_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResetTimer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timer_name": "TimerName",
    }

    timer_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SetTimer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "seconds": "Seconds",
        "timer_name": "TimerName",
        "duration_expression": "DurationExpression",
    }

    seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timer_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    duration_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SetVariable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "variable_name": "VariableName",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variable_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Sns(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_arn": "TargetArn",
        "payload": "Payload",
    }

    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Sqs(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "use_base64": "UseBase64",
        "payload": "Payload",
        "queue_url": "QueueUrl",
    }

    use_base64: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None
    queue_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class State(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "on_input": "OnInput",
        "on_exit": "OnExit",
        "state_name": "StateName",
        "on_enter": "OnEnter",
    }

    on_input: Optional[OnInput] = None
    on_exit: Optional[OnExit] = None
    state_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_enter: Optional[OnEnter] = None


@dataclass
class TransitionEvent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "actions": "Actions",
        "next_state": "NextState",
        "event_name": "EventName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    actions: Optional[list[Action]] = None
    next_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

