"""PropertyTypes for AWS::IoTEvents::AlarmModel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AlarmModelVersionStatus:
    """AlarmModelVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    ACTIVATING = "ACTIVATING"
    INACTIVE = "INACTIVE"
    FAILED = "FAILED"


class AnalysisResultLevel:
    """AnalysisResultLevel enum values."""

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class AnalysisStatus:
    """AnalysisStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"


class DetectorModelVersionStatus:
    """DetectorModelVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    ACTIVATING = "ACTIVATING"
    INACTIVE = "INACTIVE"
    DEPRECATED = "DEPRECATED"
    DRAFT = "DRAFT"
    PAUSED = "PAUSED"
    FAILED = "FAILED"


class EvaluationMethod:
    """EvaluationMethod enum values."""

    BATCH = "BATCH"
    SERIAL = "SERIAL"


class InputStatus:
    """InputStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class LoggingLevel:
    """LoggingLevel enum values."""

    ERROR = "ERROR"
    INFO = "INFO"
    DEBUG = "DEBUG"


class PayloadType:
    """PayloadType enum values."""

    STRING = "STRING"
    JSON = "JSON"


@dataclass
class AcknowledgeFlow(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AlarmAction(PropertyType):
    DYNAMO_D_BV2 = "DynamoDBv2"
    IOT_EVENTS = "IotEvents"
    IOT_SITE_WISE = "IotSiteWise"
    SQS = "Sqs"
    FIREHOSE = "Firehose"
    DYNAMO_DB = "DynamoDB"
    IOT_TOPIC_PUBLISH = "IotTopicPublish"
    SNS = "Sns"
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_d_bv2": "DynamoDBv2",
        "iot_events": "IotEvents",
        "iot_site_wise": "IotSiteWise",
        "sqs": "Sqs",
        "firehose": "Firehose",
        "dynamo_db": "DynamoDB",
        "iot_topic_publish": "IotTopicPublish",
        "sns": "Sns",
        "lambda_": "Lambda",
    }

    dynamo_d_bv2: Optional[DynamoDBv2] = None
    iot_events: Optional[IotEvents] = None
    iot_site_wise: Optional[IotSiteWise] = None
    sqs: Optional[Sqs] = None
    firehose: Optional[Firehose] = None
    dynamo_db: Optional[DynamoDB] = None
    iot_topic_publish: Optional[IotTopicPublish] = None
    sns: Optional[Sns] = None
    lambda_: Optional[Lambda] = None


@dataclass
class AlarmCapabilities(PropertyType):
    ACKNOWLEDGE_FLOW = "AcknowledgeFlow"
    INITIALIZATION_CONFIGURATION = "InitializationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "acknowledge_flow": "AcknowledgeFlow",
        "initialization_configuration": "InitializationConfiguration",
    }

    acknowledge_flow: Optional[AcknowledgeFlow] = None
    initialization_configuration: Optional[InitializationConfiguration] = None


@dataclass
class AlarmEventActions(PropertyType):
    ALARM_ACTIONS = "AlarmActions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_actions": "AlarmActions",
    }

    alarm_actions: Optional[list[AlarmAction]] = None


@dataclass
class AlarmRule(PropertyType):
    SIMPLE_RULE = "SimpleRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "simple_rule": "SimpleRule",
    }

    simple_rule: Optional[SimpleRule] = None


@dataclass
class AssetPropertyTimestamp(PropertyType):
    TIME_IN_SECONDS = "TimeInSeconds"
    OFFSET_IN_NANOS = "OffsetInNanos"

    _property_mappings: ClassVar[dict[str, str]] = {
        "time_in_seconds": "TimeInSeconds",
        "offset_in_nanos": "OffsetInNanos",
    }

    time_in_seconds: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset_in_nanos: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetPropertyValue(PropertyType):
    QUALITY = "Quality"
    VALUE = "Value"
    TIMESTAMP = "Timestamp"

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
    DOUBLE_VALUE = "DoubleValue"
    BOOLEAN_VALUE = "BooleanValue"
    INTEGER_VALUE = "IntegerValue"
    STRING_VALUE = "StringValue"

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
class DynamoDB(PropertyType):
    TABLE_NAME = "TableName"
    PAYLOAD_FIELD = "PayloadField"
    RANGE_KEY_FIELD = "RangeKeyField"
    HASH_KEY_FIELD = "HashKeyField"
    RANGE_KEY_VALUE = "RangeKeyValue"
    RANGE_KEY_TYPE = "RangeKeyType"
    HASH_KEY_TYPE = "HashKeyType"
    HASH_KEY_VALUE = "HashKeyValue"
    PAYLOAD = "Payload"
    OPERATION = "Operation"

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
    TABLE_NAME = "TableName"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "payload": "Payload",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Firehose(PropertyType):
    DELIVERY_STREAM_NAME = "DeliveryStreamName"
    PAYLOAD = "Payload"
    SEPARATOR = "Separator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_name": "DeliveryStreamName",
        "payload": "Payload",
        "separator": "Separator",
    }

    delivery_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None
    separator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InitializationConfiguration(PropertyType):
    DISABLED_ON_INITIALIZATION = "DisabledOnInitialization"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disabled_on_initialization": "DisabledOnInitialization",
    }

    disabled_on_initialization: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IotEvents(PropertyType):
    INPUT_NAME = "InputName"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_name": "InputName",
        "payload": "Payload",
    }

    input_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class IotSiteWise(PropertyType):
    ENTRY_ID = "EntryId"
    PROPERTY_ALIAS = "PropertyAlias"
    PROPERTY_VALUE = "PropertyValue"
    ASSET_ID = "AssetId"
    PROPERTY_ID = "PropertyId"

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
    MQTT_TOPIC = "MqttTopic"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mqtt_topic": "MqttTopic",
        "payload": "Payload",
    }

    mqtt_topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Lambda(PropertyType):
    FUNCTION_ARN = "FunctionArn"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionArn",
        "payload": "Payload",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Payload(PropertyType):
    CONTENT_EXPRESSION = "ContentExpression"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_expression": "ContentExpression",
        "type_": "Type",
    }

    content_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SimpleRule(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    INPUT_PROPERTY = "InputProperty"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "input_property": "InputProperty",
        "threshold": "Threshold",
    }

    comparison_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_property: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Sns(PropertyType):
    TARGET_ARN = "TargetArn"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_arn": "TargetArn",
        "payload": "Payload",
    }

    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None


@dataclass
class Sqs(PropertyType):
    USE_BASE64 = "UseBase64"
    PAYLOAD = "Payload"
    QUEUE_URL = "QueueUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "use_base64": "UseBase64",
        "payload": "Payload",
        "queue_url": "QueueUrl",
    }

    use_base64: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    payload: Optional[Payload] = None
    queue_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

