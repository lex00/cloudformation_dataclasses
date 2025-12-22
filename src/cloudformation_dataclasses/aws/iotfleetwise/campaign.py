"""PropertyTypes for AWS::IoTFleetWise::Campaign."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CampaignStatus:
    """CampaignStatus enum values."""

    CREATING = "CREATING"
    WAITING_FOR_APPROVAL = "WAITING_FOR_APPROVAL"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"


class Compression:
    """Compression enum values."""

    OFF = "OFF"
    SNAPPY = "SNAPPY"


class DataFormat:
    """DataFormat enum values."""

    JSON = "JSON"
    PARQUET = "PARQUET"


class DefaultForUnmappedSignalsType:
    """DefaultForUnmappedSignalsType enum values."""

    CUSTOM_DECODING = "CUSTOM_DECODING"


class DiagnosticsMode:
    """DiagnosticsMode enum values."""

    OFF = "OFF"
    SEND_ACTIVE_DTCS = "SEND_ACTIVE_DTCS"


class EncryptionStatus:
    """EncryptionStatus enum values."""

    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class EncryptionType:
    """EncryptionType enum values."""

    KMS_BASED_ENCRYPTION = "KMS_BASED_ENCRYPTION"
    FLEETWISE_DEFAULT_ENCRYPTION = "FLEETWISE_DEFAULT_ENCRYPTION"


class ListResponseScope:
    """ListResponseScope enum values."""

    METADATA_ONLY = "METADATA_ONLY"


class LogType:
    """LogType enum values."""

    OFF = "OFF"
    ERROR = "ERROR"


class ManifestStatus:
    """ManifestStatus enum values."""

    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    INVALID = "INVALID"
    VALIDATING = "VALIDATING"


class NetworkInterfaceFailureReason:
    """NetworkInterfaceFailureReason enum values."""

    DUPLICATE_NETWORK_INTERFACE = "DUPLICATE_NETWORK_INTERFACE"
    CONFLICTING_NETWORK_INTERFACE = "CONFLICTING_NETWORK_INTERFACE"
    NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS = "NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS"
    CAN_NETWORK_INTERFACE_INFO_IS_NULL = "CAN_NETWORK_INTERFACE_INFO_IS_NULL"
    OBD_NETWORK_INTERFACE_INFO_IS_NULL = "OBD_NETWORK_INTERFACE_INFO_IS_NULL"
    NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS = "NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS"
    VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL = "VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL"
    CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL = "CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL"


class NetworkInterfaceType:
    """NetworkInterfaceType enum values."""

    CAN_INTERFACE = "CAN_INTERFACE"
    OBD_INTERFACE = "OBD_INTERFACE"
    VEHICLE_MIDDLEWARE = "VEHICLE_MIDDLEWARE"
    CUSTOM_DECODING_INTERFACE = "CUSTOM_DECODING_INTERFACE"


class NodeDataEncoding:
    """NodeDataEncoding enum values."""

    BINARY = "BINARY"
    TYPED = "TYPED"


class NodeDataType:
    """NodeDataType enum values."""

    INT8 = "INT8"
    UINT8 = "UINT8"
    INT16 = "INT16"
    UINT16 = "UINT16"
    INT32 = "INT32"
    UINT32 = "UINT32"
    INT64 = "INT64"
    UINT64 = "UINT64"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    UNIX_TIMESTAMP = "UNIX_TIMESTAMP"
    INT8_ARRAY = "INT8_ARRAY"
    UINT8_ARRAY = "UINT8_ARRAY"
    INT16_ARRAY = "INT16_ARRAY"
    UINT16_ARRAY = "UINT16_ARRAY"
    INT32_ARRAY = "INT32_ARRAY"
    UINT32_ARRAY = "UINT32_ARRAY"
    INT64_ARRAY = "INT64_ARRAY"
    UINT64_ARRAY = "UINT64_ARRAY"
    BOOLEAN_ARRAY = "BOOLEAN_ARRAY"
    FLOAT_ARRAY = "FLOAT_ARRAY"
    DOUBLE_ARRAY = "DOUBLE_ARRAY"
    STRING_ARRAY = "STRING_ARRAY"
    UNIX_TIMESTAMP_ARRAY = "UNIX_TIMESTAMP_ARRAY"
    UNKNOWN = "UNKNOWN"
    STRUCT = "STRUCT"
    STRUCT_ARRAY = "STRUCT_ARRAY"


class ROS2PrimitiveType:
    """ROS2PrimitiveType enum values."""

    BOOL = "BOOL"
    BYTE = "BYTE"
    CHAR = "CHAR"
    FLOAT32 = "FLOAT32"
    FLOAT64 = "FLOAT64"
    INT8 = "INT8"
    UINT8 = "UINT8"
    INT16 = "INT16"
    UINT16 = "UINT16"
    INT32 = "INT32"
    UINT32 = "UINT32"
    INT64 = "INT64"
    UINT64 = "UINT64"
    STRING = "STRING"
    WSTRING = "WSTRING"


class RegistrationStatus:
    """RegistrationStatus enum values."""

    REGISTRATION_PENDING = "REGISTRATION_PENDING"
    REGISTRATION_SUCCESS = "REGISTRATION_SUCCESS"
    REGISTRATION_FAILURE = "REGISTRATION_FAILURE"


class SignalDecoderFailureReason:
    """SignalDecoderFailureReason enum values."""

    DUPLICATE_SIGNAL = "DUPLICATE_SIGNAL"
    CONFLICTING_SIGNAL = "CONFLICTING_SIGNAL"
    SIGNAL_TO_ADD_ALREADY_EXISTS = "SIGNAL_TO_ADD_ALREADY_EXISTS"
    SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE = "SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE"
    NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE = "NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE"
    SIGNAL_NOT_IN_MODEL = "SIGNAL_NOT_IN_MODEL"
    CAN_SIGNAL_INFO_IS_NULL = "CAN_SIGNAL_INFO_IS_NULL"
    OBD_SIGNAL_INFO_IS_NULL = "OBD_SIGNAL_INFO_IS_NULL"
    NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL = "NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL"
    MESSAGE_SIGNAL_INFO_IS_NULL = "MESSAGE_SIGNAL_INFO_IS_NULL"
    SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE = "SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE"
    STRUCT_SIZE_MISMATCH = "STRUCT_SIZE_MISMATCH"
    NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL = "NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL"
    SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG = "SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG"
    EMPTY_MESSAGE_SIGNAL = "EMPTY_MESSAGE_SIGNAL"
    CUSTOM_DECODING_SIGNAL_INFO_IS_NULL = "CUSTOM_DECODING_SIGNAL_INFO_IS_NULL"


class SignalDecoderType:
    """SignalDecoderType enum values."""

    CAN_SIGNAL = "CAN_SIGNAL"
    OBD_SIGNAL = "OBD_SIGNAL"
    MESSAGE_SIGNAL = "MESSAGE_SIGNAL"
    CUSTOM_DECODING_SIGNAL = "CUSTOM_DECODING_SIGNAL"


class SignalNodeType:
    """SignalNodeType enum values."""

    SENSOR = "SENSOR"
    ACTUATOR = "ACTUATOR"
    ATTRIBUTE = "ATTRIBUTE"
    BRANCH = "BRANCH"
    CUSTOM_STRUCT = "CUSTOM_STRUCT"
    CUSTOM_PROPERTY = "CUSTOM_PROPERTY"


class SignalValueType:
    """SignalValueType enum values."""

    INTEGER = "INTEGER"
    FLOATING_POINT = "FLOATING_POINT"


class SpoolingMode:
    """SpoolingMode enum values."""

    OFF = "OFF"
    TO_DISK = "TO_DISK"


class StorageCompressionFormat:
    """StorageCompressionFormat enum values."""

    NONE = "NONE"
    GZIP = "GZIP"


class StorageMaximumSizeUnit:
    """StorageMaximumSizeUnit enum values."""

    MB = "MB"
    GB = "GB"
    TB = "TB"


class StorageMinimumTimeToLiveUnit:
    """StorageMinimumTimeToLiveUnit enum values."""

    HOURS = "HOURS"
    DAYS = "DAYS"
    WEEKS = "WEEKS"


class StructuredMessageListType:
    """StructuredMessageListType enum values."""

    FIXED_CAPACITY = "FIXED_CAPACITY"
    DYNAMIC_UNBOUNDED_CAPACITY = "DYNAMIC_UNBOUNDED_CAPACITY"
    DYNAMIC_BOUNDED_CAPACITY = "DYNAMIC_BOUNDED_CAPACITY"


class TimeUnit:
    """TimeUnit enum values."""

    MILLISECOND = "MILLISECOND"
    SECOND = "SECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"


class TriggerMode:
    """TriggerMode enum values."""

    ALWAYS = "ALWAYS"
    RISING_EDGE = "RISING_EDGE"


class UpdateCampaignAction:
    """UpdateCampaignAction enum values."""

    APPROVE = "APPROVE"
    SUSPEND = "SUSPEND"
    RESUME = "RESUME"
    UPDATE = "UPDATE"


class UpdateMode:
    """UpdateMode enum values."""

    OVERWRITE = "Overwrite"
    MERGE = "Merge"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


class VehicleAssociationBehavior:
    """VehicleAssociationBehavior enum values."""

    CREATEIOTTHING = "CreateIotThing"
    VALIDATEIOTTHINGEXISTS = "ValidateIotThingExists"


class VehicleMiddlewareProtocol:
    """VehicleMiddlewareProtocol enum values."""

    ROS_2 = "ROS_2"


class VehicleState:
    """VehicleState enum values."""

    CREATED = "CREATED"
    READY = "READY"
    HEALTHY = "HEALTHY"
    SUSPENDED = "SUSPENDED"
    DELETING = "DELETING"
    READY_FOR_CHECKIN = "READY_FOR_CHECKIN"


@dataclass
class CollectionScheme(PropertyType):
    TIME_BASED_COLLECTION_SCHEME = "TimeBasedCollectionScheme"
    CONDITION_BASED_COLLECTION_SCHEME = "ConditionBasedCollectionScheme"

    _property_mappings: ClassVar[dict[str, str]] = {
        "time_based_collection_scheme": "TimeBasedCollectionScheme",
        "condition_based_collection_scheme": "ConditionBasedCollectionScheme",
    }

    time_based_collection_scheme: Optional[TimeBasedCollectionScheme] = None
    condition_based_collection_scheme: Optional[ConditionBasedCollectionScheme] = None


@dataclass
class ConditionBasedCollectionScheme(PropertyType):
    MINIMUM_TRIGGER_INTERVAL_MS = "MinimumTriggerIntervalMs"
    EXPRESSION = "Expression"
    TRIGGER_MODE = "TriggerMode"
    CONDITION_LANGUAGE_VERSION = "ConditionLanguageVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_trigger_interval_ms": "MinimumTriggerIntervalMs",
        "expression": "Expression",
        "trigger_mode": "TriggerMode",
        "condition_language_version": "ConditionLanguageVersion",
    }

    minimum_trigger_interval_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_language_version: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionBasedSignalFetchConfig(PropertyType):
    CONDITION_EXPRESSION = "ConditionExpression"
    TRIGGER_MODE = "TriggerMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_expression": "ConditionExpression",
        "trigger_mode": "TriggerMode",
    }

    condition_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataDestinationConfig(PropertyType):
    S3_CONFIG = "S3Config"
    MQTT_TOPIC_CONFIG = "MqttTopicConfig"
    TIMESTREAM_CONFIG = "TimestreamConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_config": "S3Config",
        "mqtt_topic_config": "MqttTopicConfig",
        "timestream_config": "TimestreamConfig",
    }

    s3_config: Optional[S3Config] = None
    mqtt_topic_config: Optional[MqttTopicConfig] = None
    timestream_config: Optional[TimestreamConfig] = None


@dataclass
class DataPartition(PropertyType):
    UPLOAD_OPTIONS = "UploadOptions"
    STORAGE_OPTIONS = "StorageOptions"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "upload_options": "UploadOptions",
        "storage_options": "StorageOptions",
        "id": "Id",
    }

    upload_options: Optional[DataPartitionUploadOptions] = None
    storage_options: Optional[DataPartitionStorageOptions] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPartitionStorageOptions(PropertyType):
    MAXIMUM_SIZE = "MaximumSize"
    STORAGE_LOCATION = "StorageLocation"
    MINIMUM_TIME_TO_LIVE = "MinimumTimeToLive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_size": "MaximumSize",
        "storage_location": "StorageLocation",
        "minimum_time_to_live": "MinimumTimeToLive",
    }

    maximum_size: Optional[StorageMaximumSize] = None
    storage_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_time_to_live: Optional[StorageMinimumTimeToLive] = None


@dataclass
class DataPartitionUploadOptions(PropertyType):
    EXPRESSION = "Expression"
    CONDITION_LANGUAGE_VERSION = "ConditionLanguageVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "condition_language_version": "ConditionLanguageVersion",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_language_version: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MqttTopicConfig(PropertyType):
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    MQTT_TOPIC_ARN = "MqttTopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role_arn": "ExecutionRoleArn",
        "mqtt_topic_arn": "MqttTopicArn",
    }

    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mqtt_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Config(PropertyType):
    BUCKET_ARN = "BucketArn"
    DATA_FORMAT = "DataFormat"
    STORAGE_COMPRESSION_FORMAT = "StorageCompressionFormat"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "data_format": "DataFormat",
        "storage_compression_format": "StorageCompressionFormat",
        "prefix": "Prefix",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_compression_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SignalFetchConfig(PropertyType):
    CONDITION_BASED = "ConditionBased"
    TIME_BASED = "TimeBased"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_based": "ConditionBased",
        "time_based": "TimeBased",
    }

    condition_based: Optional[ConditionBasedSignalFetchConfig] = None
    time_based: Optional[TimeBasedSignalFetchConfig] = None


@dataclass
class SignalFetchInformation(PropertyType):
    ACTIONS = "Actions"
    FULLY_QUALIFIED_NAME = "FullyQualifiedName"
    SIGNAL_FETCH_CONFIG = "SignalFetchConfig"
    CONDITION_LANGUAGE_VERSION = "ConditionLanguageVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "fully_qualified_name": "FullyQualifiedName",
        "signal_fetch_config": "SignalFetchConfig",
        "condition_language_version": "ConditionLanguageVersion",
    }

    actions: Optional[Union[list[str], Ref]] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signal_fetch_config: Optional[SignalFetchConfig] = None
    condition_language_version: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class SignalInformation(PropertyType):
    MAX_SAMPLE_COUNT = "MaxSampleCount"
    DATA_PARTITION_ID = "DataPartitionId"
    MINIMUM_SAMPLING_INTERVAL_MS = "MinimumSamplingIntervalMs"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_sample_count": "MaxSampleCount",
        "data_partition_id": "DataPartitionId",
        "minimum_sampling_interval_ms": "MinimumSamplingIntervalMs",
        "name": "Name",
    }

    max_sample_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    data_partition_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_sampling_interval_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageMaximumSize(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageMinimumTimeToLive(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedCollectionScheme(PropertyType):
    PERIOD_MS = "PeriodMs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "period_ms": "PeriodMs",
    }

    period_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedSignalFetchConfig(PropertyType):
    EXECUTION_FREQUENCY_MS = "ExecutionFrequencyMs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_frequency_ms": "ExecutionFrequencyMs",
    }

    execution_frequency_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TimestreamConfig(PropertyType):
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    TIMESTREAM_TABLE_ARN = "TimestreamTableArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role_arn": "ExecutionRoleArn",
        "timestream_table_arn": "TimestreamTableArn",
    }

    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestream_table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

