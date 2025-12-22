"""PropertyTypes for AWS::Lambda::EventSourceMapping."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationLogLevel:
    """ApplicationLogLevel enum values."""

    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Architecture:
    """Architecture enum values."""

    X86_64 = "x86_64"
    ARM64 = "arm64"


class CapacityProviderPredefinedMetricType:
    """CapacityProviderPredefinedMetricType enum values."""

    LAMBDACAPACITYPROVIDERAVERAGECPUUTILIZATION = "LambdaCapacityProviderAverageCPUUtilization"


class CapacityProviderScalingMode:
    """CapacityProviderScalingMode enum values."""

    AUTO = "Auto"
    MANUAL = "Manual"


class CapacityProviderState:
    """CapacityProviderState enum values."""

    PENDING = "Pending"
    ACTIVE = "Active"
    FAILED = "Failed"
    DELETING = "Deleting"


class CodeSigningPolicy:
    """CodeSigningPolicy enum values."""

    WARN = "Warn"
    ENFORCE = "Enforce"


class EndPointType:
    """EndPointType enum values."""

    KAFKA_BOOTSTRAP_SERVERS = "KAFKA_BOOTSTRAP_SERVERS"


class EventSourceMappingMetric:
    """EventSourceMappingMetric enum values."""

    EVENTCOUNT = "EventCount"


class EventSourcePosition:
    """EventSourcePosition enum values."""

    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


class EventType:
    """EventType enum values."""

    EXECUTIONSTARTED = "ExecutionStarted"
    EXECUTIONSUCCEEDED = "ExecutionSucceeded"
    EXECUTIONFAILED = "ExecutionFailed"
    EXECUTIONTIMEDOUT = "ExecutionTimedOut"
    EXECUTIONSTOPPED = "ExecutionStopped"
    CONTEXTSTARTED = "ContextStarted"
    CONTEXTSUCCEEDED = "ContextSucceeded"
    CONTEXTFAILED = "ContextFailed"
    WAITSTARTED = "WaitStarted"
    WAITSUCCEEDED = "WaitSucceeded"
    WAITCANCELLED = "WaitCancelled"
    STEPSTARTED = "StepStarted"
    STEPSUCCEEDED = "StepSucceeded"
    STEPFAILED = "StepFailed"
    CHAINEDINVOKESTARTED = "ChainedInvokeStarted"
    CHAINEDINVOKESUCCEEDED = "ChainedInvokeSucceeded"
    CHAINEDINVOKEFAILED = "ChainedInvokeFailed"
    CHAINEDINVOKETIMEDOUT = "ChainedInvokeTimedOut"
    CHAINEDINVOKESTOPPED = "ChainedInvokeStopped"
    CALLBACKSTARTED = "CallbackStarted"
    CALLBACKSUCCEEDED = "CallbackSucceeded"
    CALLBACKFAILED = "CallbackFailed"
    CALLBACKTIMEDOUT = "CallbackTimedOut"
    INVOCATIONCOMPLETED = "InvocationCompleted"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    STOPPED = "STOPPED"


class FullDocument:
    """FullDocument enum values."""

    UPDATELOOKUP = "UpdateLookup"
    DEFAULT = "Default"


class FunctionResponseType:
    """FunctionResponseType enum values."""

    REPORTBATCHITEMFAILURES = "ReportBatchItemFailures"


class FunctionUrlAuthType:
    """FunctionUrlAuthType enum values."""

    NONE = "NONE"
    AWS_IAM = "AWS_IAM"


class FunctionVersion:
    """FunctionVersion enum values."""

    ALL = "ALL"


class FunctionVersionLatestPublished:
    """FunctionVersionLatestPublished enum values."""

    LATEST_PUBLISHED = "LATEST_PUBLISHED"


class InvocationType:
    """InvocationType enum values."""

    EVENT = "Event"
    REQUESTRESPONSE = "RequestResponse"
    DRYRUN = "DryRun"


class InvokeMode:
    """InvokeMode enum values."""

    BUFFERED = "BUFFERED"
    RESPONSE_STREAM = "RESPONSE_STREAM"


class KafkaSchemaRegistryAuthType:
    """KafkaSchemaRegistryAuthType enum values."""

    BASIC_AUTH = "BASIC_AUTH"
    CLIENT_CERTIFICATE_TLS_AUTH = "CLIENT_CERTIFICATE_TLS_AUTH"
    SERVER_ROOT_CA_CERTIFICATE = "SERVER_ROOT_CA_CERTIFICATE"


class KafkaSchemaValidationAttribute:
    """KafkaSchemaValidationAttribute enum values."""

    KEY = "KEY"
    VALUE = "VALUE"


class LastUpdateStatus:
    """LastUpdateStatus enum values."""

    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    INPROGRESS = "InProgress"


class LastUpdateStatusReasonCode:
    """LastUpdateStatusReasonCode enum values."""

    ENILIMITEXCEEDED = "EniLimitExceeded"
    INSUFFICIENTROLEPERMISSIONS = "InsufficientRolePermissions"
    INVALIDCONFIGURATION = "InvalidConfiguration"
    INTERNALERROR = "InternalError"
    SUBNETOUTOFIPADDRESSES = "SubnetOutOfIPAddresses"
    INVALIDSUBNET = "InvalidSubnet"
    INVALIDSECURITYGROUP = "InvalidSecurityGroup"
    IMAGEDELETED = "ImageDeleted"
    IMAGEACCESSDENIED = "ImageAccessDenied"
    INVALIDIMAGE = "InvalidImage"
    KMSKEYACCESSDENIED = "KMSKeyAccessDenied"
    KMSKEYNOTFOUND = "KMSKeyNotFound"
    INVALIDSTATEKMSKEY = "InvalidStateKMSKey"
    DISABLEDKMSKEY = "DisabledKMSKey"
    EFSIOERROR = "EFSIOError"
    EFSMOUNTCONNECTIVITYERROR = "EFSMountConnectivityError"
    EFSMOUNTFAILURE = "EFSMountFailure"
    EFSMOUNTTIMEOUT = "EFSMountTimeout"
    INVALIDRUNTIME = "InvalidRuntime"
    INVALIDZIPFILEEXCEPTION = "InvalidZipFileException"
    FUNCTIONERROR = "FunctionError"
    VCPULIMITEXCEEDED = "VcpuLimitExceeded"
    CAPACITYPROVIDERSCALINGLIMITEXCEEDED = "CapacityProviderScalingLimitExceeded"
    INSUFFICIENTCAPACITY = "InsufficientCapacity"
    EC2REQUESTLIMITEXCEEDED = "EC2RequestLimitExceeded"
    FUNCTIONERROR_INITTIMEOUT = "FunctionError.InitTimeout"
    FUNCTIONERROR_RUNTIMEINITERROR = "FunctionError.RuntimeInitError"
    FUNCTIONERROR_EXTENSIONINITERROR = "FunctionError.ExtensionInitError"
    FUNCTIONERROR_INVALIDENTRYPOINT = "FunctionError.InvalidEntryPoint"
    FUNCTIONERROR_INVALIDWORKINGDIRECTORY = "FunctionError.InvalidWorkingDirectory"
    FUNCTIONERROR_PERMISSIONDENIED = "FunctionError.PermissionDenied"
    FUNCTIONERROR_TOOMANYEXTENSIONS = "FunctionError.TooManyExtensions"
    FUNCTIONERROR_INITRESOURCEEXHAUSTED = "FunctionError.InitResourceExhausted"
    DISALLOWEDBYVPCENCRYPTIONCONTROL = "DisallowedByVpcEncryptionControl"


class LogFormat:
    """LogFormat enum values."""

    JSON = "JSON"
    TEXT = "Text"


class LogType:
    """LogType enum values."""

    NONE = "None"
    TAIL = "Tail"


class OperationAction:
    """OperationAction enum values."""

    START = "START"
    SUCCEED = "SUCCEED"
    FAIL = "FAIL"
    RETRY = "RETRY"
    CANCEL = "CANCEL"


class OperationStatus:
    """OperationStatus enum values."""

    STARTED = "STARTED"
    PENDING = "PENDING"
    READY = "READY"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    TIMED_OUT = "TIMED_OUT"
    STOPPED = "STOPPED"


class OperationType:
    """OperationType enum values."""

    EXECUTION = "EXECUTION"
    CONTEXT = "CONTEXT"
    STEP = "STEP"
    WAIT = "WAIT"
    CALLBACK = "CALLBACK"
    CHAINED_INVOKE = "CHAINED_INVOKE"


class PackageType:
    """PackageType enum values."""

    ZIP = "Zip"
    IMAGE = "Image"


class ProvisionedConcurrencyStatusEnum:
    """ProvisionedConcurrencyStatusEnum enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    READY = "READY"
    FAILED = "FAILED"


class RecursiveLoop:
    """RecursiveLoop enum values."""

    ALLOW = "Allow"
    TERMINATE = "Terminate"


class ResponseStreamingInvocationType:
    """ResponseStreamingInvocationType enum values."""

    REQUESTRESPONSE = "RequestResponse"
    DRYRUN = "DryRun"


class Runtime:
    """Runtime enum values."""

    NODEJS = "nodejs"
    NODEJS4_3 = "nodejs4.3"
    NODEJS6_10 = "nodejs6.10"
    NODEJS8_10 = "nodejs8.10"
    NODEJS10_X = "nodejs10.x"
    NODEJS12_X = "nodejs12.x"
    NODEJS14_X = "nodejs14.x"
    NODEJS16_X = "nodejs16.x"
    JAVA8 = "java8"
    JAVA8_AL2 = "java8.al2"
    JAVA11 = "java11"
    PYTHON2_7 = "python2.7"
    PYTHON3_6 = "python3.6"
    PYTHON3_7 = "python3.7"
    PYTHON3_8 = "python3.8"
    PYTHON3_9 = "python3.9"
    DOTNETCORE1_0 = "dotnetcore1.0"
    DOTNETCORE2_0 = "dotnetcore2.0"
    DOTNETCORE2_1 = "dotnetcore2.1"
    DOTNETCORE3_1 = "dotnetcore3.1"
    DOTNET6 = "dotnet6"
    DOTNET8 = "dotnet8"
    NODEJS4_3_EDGE = "nodejs4.3-edge"
    GO1_X = "go1.x"
    RUBY2_5 = "ruby2.5"
    RUBY2_7 = "ruby2.7"
    PROVIDED = "provided"
    PROVIDED_AL2 = "provided.al2"
    NODEJS18_X = "nodejs18.x"
    PYTHON3_10 = "python3.10"
    JAVA17 = "java17"
    RUBY3_2 = "ruby3.2"
    RUBY3_3 = "ruby3.3"
    RUBY3_4 = "ruby3.4"
    PYTHON3_11 = "python3.11"
    NODEJS20_X = "nodejs20.x"
    PROVIDED_AL2023 = "provided.al2023"
    PYTHON3_12 = "python3.12"
    JAVA21 = "java21"
    PYTHON3_13 = "python3.13"
    NODEJS22_X = "nodejs22.x"
    NODEJS24_X = "nodejs24.x"
    PYTHON3_14 = "python3.14"
    JAVA25 = "java25"
    DOTNET10 = "dotnet10"


class SchemaRegistryEventRecordFormat:
    """SchemaRegistryEventRecordFormat enum values."""

    JSON = "JSON"
    SOURCE = "SOURCE"


class SnapStartApplyOn:
    """SnapStartApplyOn enum values."""

    PUBLISHEDVERSIONS = "PublishedVersions"
    NONE = "None"


class SnapStartOptimizationStatus:
    """SnapStartOptimizationStatus enum values."""

    ON = "On"
    OFF = "Off"


class SourceAccessType:
    """SourceAccessType enum values."""

    BASIC_AUTH = "BASIC_AUTH"
    VPC_SUBNET = "VPC_SUBNET"
    VPC_SECURITY_GROUP = "VPC_SECURITY_GROUP"
    SASL_SCRAM_512_AUTH = "SASL_SCRAM_512_AUTH"
    SASL_SCRAM_256_AUTH = "SASL_SCRAM_256_AUTH"
    VIRTUAL_HOST = "VIRTUAL_HOST"
    CLIENT_CERTIFICATE_TLS_AUTH = "CLIENT_CERTIFICATE_TLS_AUTH"
    SERVER_ROOT_CA_CERTIFICATE = "SERVER_ROOT_CA_CERTIFICATE"


class State:
    """State enum values."""

    PENDING = "Pending"
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    FAILED = "Failed"
    DEACTIVATING = "Deactivating"
    DEACTIVATED = "Deactivated"
    ACTIVENONINVOCABLE = "ActiveNonInvocable"
    DELETING = "Deleting"


class StateReasonCode:
    """StateReasonCode enum values."""

    IDLE = "Idle"
    CREATING = "Creating"
    RESTORING = "Restoring"
    ENILIMITEXCEEDED = "EniLimitExceeded"
    INSUFFICIENTROLEPERMISSIONS = "InsufficientRolePermissions"
    INVALIDCONFIGURATION = "InvalidConfiguration"
    INTERNALERROR = "InternalError"
    SUBNETOUTOFIPADDRESSES = "SubnetOutOfIPAddresses"
    INVALIDSUBNET = "InvalidSubnet"
    INVALIDSECURITYGROUP = "InvalidSecurityGroup"
    IMAGEDELETED = "ImageDeleted"
    IMAGEACCESSDENIED = "ImageAccessDenied"
    INVALIDIMAGE = "InvalidImage"
    KMSKEYACCESSDENIED = "KMSKeyAccessDenied"
    KMSKEYNOTFOUND = "KMSKeyNotFound"
    INVALIDSTATEKMSKEY = "InvalidStateKMSKey"
    DISABLEDKMSKEY = "DisabledKMSKey"
    EFSIOERROR = "EFSIOError"
    EFSMOUNTCONNECTIVITYERROR = "EFSMountConnectivityError"
    EFSMOUNTFAILURE = "EFSMountFailure"
    EFSMOUNTTIMEOUT = "EFSMountTimeout"
    INVALIDRUNTIME = "InvalidRuntime"
    INVALIDZIPFILEEXCEPTION = "InvalidZipFileException"
    FUNCTIONERROR = "FunctionError"
    DRAININGDURABLEEXECUTIONS = "DrainingDurableExecutions"
    VCPULIMITEXCEEDED = "VcpuLimitExceeded"
    CAPACITYPROVIDERSCALINGLIMITEXCEEDED = "CapacityProviderScalingLimitExceeded"
    INSUFFICIENTCAPACITY = "InsufficientCapacity"
    EC2REQUESTLIMITEXCEEDED = "EC2RequestLimitExceeded"
    FUNCTIONERROR_INITTIMEOUT = "FunctionError.InitTimeout"
    FUNCTIONERROR_RUNTIMEINITERROR = "FunctionError.RuntimeInitError"
    FUNCTIONERROR_EXTENSIONINITERROR = "FunctionError.ExtensionInitError"
    FUNCTIONERROR_INVALIDENTRYPOINT = "FunctionError.InvalidEntryPoint"
    FUNCTIONERROR_INVALIDWORKINGDIRECTORY = "FunctionError.InvalidWorkingDirectory"
    FUNCTIONERROR_PERMISSIONDENIED = "FunctionError.PermissionDenied"
    FUNCTIONERROR_TOOMANYEXTENSIONS = "FunctionError.TooManyExtensions"
    FUNCTIONERROR_INITRESOURCEEXHAUSTED = "FunctionError.InitResourceExhausted"
    DISALLOWEDBYVPCENCRYPTIONCONTROL = "DisallowedByVpcEncryptionControl"


class SystemLogLevel:
    """SystemLogLevel enum values."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"


class TenantIsolationMode:
    """TenantIsolationMode enum values."""

    PER_TENANT = "PER_TENANT"


class ThrottleReason:
    """ThrottleReason enum values."""

    CONCURRENTINVOCATIONLIMITEXCEEDED = "ConcurrentInvocationLimitExceeded"
    FUNCTIONINVOCATIONRATELIMITEXCEEDED = "FunctionInvocationRateLimitExceeded"
    RESERVEDFUNCTIONCONCURRENTINVOCATIONLIMITEXCEEDED = "ReservedFunctionConcurrentInvocationLimitExceeded"
    RESERVEDFUNCTIONINVOCATIONRATELIMITEXCEEDED = "ReservedFunctionInvocationRateLimitExceeded"
    CALLERRATELIMITEXCEEDED = "CallerRateLimitExceeded"
    CONCURRENTSNAPSHOTCREATELIMITEXCEEDED = "ConcurrentSnapshotCreateLimitExceeded"


class TracingMode:
    """TracingMode enum values."""

    ACTIVE = "Active"
    PASSTHROUGH = "PassThrough"


class UpdateRuntimeOn:
    """UpdateRuntimeOn enum values."""

    AUTO = "Auto"
    MANUAL = "Manual"
    FUNCTIONUPDATE = "FunctionUpdate"


@dataclass
class AmazonManagedKafkaEventSourceConfig(PropertyType):
    CONSUMER_GROUP_ID = "ConsumerGroupId"
    SCHEMA_REGISTRY_CONFIG = "SchemaRegistryConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupId",
        "schema_registry_config": "SchemaRegistryConfig",
    }

    consumer_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_registry_config: Optional[SchemaRegistryConfig] = None


@dataclass
class DestinationConfig(PropertyType):
    ON_FAILURE = "OnFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_failure": "OnFailure",
    }

    on_failure: Optional[OnFailure] = None


@dataclass
class DocumentDBEventSourceConfig(PropertyType):
    FULL_DOCUMENT = "FullDocument"
    COLLECTION_NAME = "CollectionName"
    DATABASE_NAME = "DatabaseName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "full_document": "FullDocument",
        "collection_name": "CollectionName",
        "database_name": "DatabaseName",
    }

    full_document: Optional[Union[str, FullDocument, Ref, GetAtt, Sub]] = None
    collection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoints(PropertyType):
    KAFKA_BOOTSTRAP_SERVERS = "KafkaBootstrapServers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kafka_bootstrap_servers": "KafkaBootstrapServers",
    }

    kafka_bootstrap_servers: Optional[Union[list[str], Ref]] = None


@dataclass
class Filter(PropertyType):
    PATTERN = "Pattern"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterCriteria(PropertyType):
    FILTERS = "Filters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
    }

    filters: Optional[list[Filter]] = None


@dataclass
class LoggingConfig(PropertyType):
    SYSTEM_LOG_LEVEL = "SystemLogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "system_log_level": "SystemLogLevel",
    }

    system_log_level: Optional[Union[str, SystemLogLevel, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsConfig(PropertyType):
    METRICS = "Metrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metrics": "Metrics",
    }

    metrics: Optional[Union[list[str], Ref]] = None


@dataclass
class OnFailure(PropertyType):
    DESTINATION = "Destination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisionedPollerConfig(PropertyType):
    POLLER_GROUP_NAME = "PollerGroupName"
    MINIMUM_POLLERS = "MinimumPollers"
    MAXIMUM_POLLERS = "MaximumPollers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "poller_group_name": "PollerGroupName",
        "minimum_pollers": "MinimumPollers",
        "maximum_pollers": "MaximumPollers",
    }

    poller_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_pollers: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_pollers: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingConfig(PropertyType):
    MAXIMUM_CONCURRENCY = "MaximumConcurrency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_concurrency": "MaximumConcurrency",
    }

    maximum_concurrency: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaRegistryAccessConfig(PropertyType):
    TYPE = "Type"
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "uri": "URI",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaRegistryConfig(PropertyType):
    SCHEMA_VALIDATION_CONFIGS = "SchemaValidationConfigs"
    SCHEMA_REGISTRY_URI = "SchemaRegistryURI"
    EVENT_RECORD_FORMAT = "EventRecordFormat"
    ACCESS_CONFIGS = "AccessConfigs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_validation_configs": "SchemaValidationConfigs",
        "schema_registry_uri": "SchemaRegistryURI",
        "event_record_format": "EventRecordFormat",
        "access_configs": "AccessConfigs",
    }

    schema_validation_configs: Optional[list[SchemaValidationConfig]] = None
    schema_registry_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_record_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_configs: Optional[list[SchemaRegistryAccessConfig]] = None


@dataclass
class SchemaValidationConfig(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelfManagedEventSource(PropertyType):
    ENDPOINTS = "Endpoints"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoints": "Endpoints",
    }

    endpoints: Optional[Endpoints] = None


@dataclass
class SelfManagedKafkaEventSourceConfig(PropertyType):
    CONSUMER_GROUP_ID = "ConsumerGroupId"
    SCHEMA_REGISTRY_CONFIG = "SchemaRegistryConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupId",
        "schema_registry_config": "SchemaRegistryConfig",
    }

    consumer_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_registry_config: Optional[SchemaRegistryConfig] = None


@dataclass
class SourceAccessConfiguration(PropertyType):
    TYPE = "Type"
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "uri": "URI",
    }

    type_: Optional[Union[str, SourceAccessType, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None

