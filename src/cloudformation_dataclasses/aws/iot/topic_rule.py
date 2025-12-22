"""PropertyTypes for AWS::IoT::TopicRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AbortAction:
    """AbortAction enum values."""

    CANCEL = "CANCEL"


class ActionType:
    """ActionType enum values."""

    PUBLISH = "PUBLISH"
    SUBSCRIBE = "SUBSCRIBE"
    RECEIVE = "RECEIVE"
    CONNECT = "CONNECT"


class AggregationTypeName:
    """AggregationTypeName enum values."""

    STATISTICS = "Statistics"
    PERCENTILES = "Percentiles"
    CARDINALITY = "Cardinality"


class AlertTargetType:
    """AlertTargetType enum values."""

    SNS = "SNS"


class ApplicationProtocol:
    """ApplicationProtocol enum values."""

    SECURE_MQTT = "SECURE_MQTT"
    MQTT_WSS = "MQTT_WSS"
    HTTPS = "HTTPS"
    DEFAULT = "DEFAULT"


class AuditCheckRunStatus:
    """AuditCheckRunStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    WAITING_FOR_DATA_COLLECTION = "WAITING_FOR_DATA_COLLECTION"
    CANCELED = "CANCELED"
    COMPLETED_COMPLIANT = "COMPLETED_COMPLIANT"
    COMPLETED_NON_COMPLIANT = "COMPLETED_NON_COMPLIANT"
    FAILED = "FAILED"


class AuditFindingSeverity:
    """AuditFindingSeverity enum values."""

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class AuditFrequency:
    """AuditFrequency enum values."""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"


class AuditMitigationActionsExecutionStatus:
    """AuditMitigationActionsExecutionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    SKIPPED = "SKIPPED"
    PENDING = "PENDING"


class AuditMitigationActionsTaskStatus:
    """AuditMitigationActionsTaskStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class AuditNotificationType:
    """AuditNotificationType enum values."""

    SNS = "SNS"


class AuditTaskStatus:
    """AuditTaskStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class AuditTaskType:
    """AuditTaskType enum values."""

    ON_DEMAND_AUDIT_TASK = "ON_DEMAND_AUDIT_TASK"
    SCHEDULED_AUDIT_TASK = "SCHEDULED_AUDIT_TASK"


class AuthDecision:
    """AuthDecision enum values."""

    ALLOWED = "ALLOWED"
    EXPLICIT_DENY = "EXPLICIT_DENY"
    IMPLICIT_DENY = "IMPLICIT_DENY"


class AuthenticationType:
    """AuthenticationType enum values."""

    CUSTOM_AUTH_X509 = "CUSTOM_AUTH_X509"
    CUSTOM_AUTH = "CUSTOM_AUTH"
    AWS_X509 = "AWS_X509"
    AWS_SIGV4 = "AWS_SIGV4"
    DEFAULT = "DEFAULT"


class AuthorizerStatus:
    """AuthorizerStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class AutoRegistrationStatus:
    """AutoRegistrationStatus enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class AwsJobAbortCriteriaAbortAction:
    """AwsJobAbortCriteriaAbortAction enum values."""

    CANCEL = "CANCEL"


class AwsJobAbortCriteriaFailureType:
    """AwsJobAbortCriteriaFailureType enum values."""

    FAILED = "FAILED"
    REJECTED = "REJECTED"
    TIMED_OUT = "TIMED_OUT"
    ALL = "ALL"


class BehaviorCriteriaType:
    """BehaviorCriteriaType enum values."""

    STATIC = "STATIC"
    STATISTICAL = "STATISTICAL"
    MACHINE_LEARNING = "MACHINE_LEARNING"


class CACertificateStatus:
    """CACertificateStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class CACertificateUpdateAction:
    """CACertificateUpdateAction enum values."""

    DEACTIVATE = "DEACTIVATE"


class CannedAccessControlList:
    """CannedAccessControlList enum values."""

    PRIVATE = "private"
    PUBLIC_READ = "public-read"
    PUBLIC_READ_WRITE = "public-read-write"
    AWS_EXEC_READ = "aws-exec-read"
    AUTHENTICATED_READ = "authenticated-read"
    BUCKET_OWNER_READ = "bucket-owner-read"
    BUCKET_OWNER_FULL_CONTROL = "bucket-owner-full-control"
    LOG_DELIVERY_WRITE = "log-delivery-write"


class CertificateMode:
    """CertificateMode enum values."""

    DEFAULT = "DEFAULT"
    SNI_ONLY = "SNI_ONLY"


class CertificateProviderOperation:
    """CertificateProviderOperation enum values."""

    CREATECERTIFICATEFROMCSR = "CreateCertificateFromCsr"


class CertificateStatus:
    """CertificateStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    REVOKED = "REVOKED"
    PENDING_TRANSFER = "PENDING_TRANSFER"
    REGISTER_INACTIVE = "REGISTER_INACTIVE"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"


class CommandExecutionStatus:
    """CommandExecutionStatus enum values."""

    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    TIMED_OUT = "TIMED_OUT"


class CommandNamespace:
    """CommandNamespace enum values."""

    AWS_IOT = "AWS-IoT"
    AWS_IOT_FLEETWISE = "AWS-IoT-FleetWise"


class CommandParameterType:
    """CommandParameterType enum values."""

    STRING = "STRING"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    LONG = "LONG"
    UNSIGNEDLONG = "UNSIGNEDLONG"
    BOOLEAN = "BOOLEAN"
    BINARY = "BINARY"


class CommandParameterValueComparisonOperator:
    """CommandParameterValueComparisonOperator enum values."""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_EQUALS = "LESS_THAN_EQUALS"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_EQUALS = "GREATER_THAN_EQUALS"
    IN_SET = "IN_SET"
    NOT_IN_SET = "NOT_IN_SET"
    IN_RANGE = "IN_RANGE"
    NOT_IN_RANGE = "NOT_IN_RANGE"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    LESS_THAN = "less-than"
    LESS_THAN_EQUALS = "less-than-equals"
    GREATER_THAN = "greater-than"
    GREATER_THAN_EQUALS = "greater-than-equals"
    IN_CIDR_SET = "in-cidr-set"
    NOT_IN_CIDR_SET = "not-in-cidr-set"
    IN_PORT_SET = "in-port-set"
    NOT_IN_PORT_SET = "not-in-port-set"
    IN_SET = "in-set"
    NOT_IN_SET = "not-in-set"


class ConfidenceLevel:
    """ConfidenceLevel enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class ConfigName:
    """ConfigName enum values."""

    CERT_AGE_THRESHOLD_IN_DAYS = "CERT_AGE_THRESHOLD_IN_DAYS"
    CERT_EXPIRATION_THRESHOLD_IN_DAYS = "CERT_EXPIRATION_THRESHOLD_IN_DAYS"


class ConfigurationStatus:
    """ConfigurationStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class CustomMetricType:
    """CustomMetricType enum values."""

    STRING_LIST = "string-list"
    IP_ADDRESS_LIST = "ip-address-list"
    NUMBER_LIST = "number-list"
    NUMBER = "number"


class DayOfWeek:
    """DayOfWeek enum values."""

    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"


class DetectMitigationActionExecutionStatus:
    """DetectMitigationActionExecutionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class DetectMitigationActionsTaskStatus:
    """DetectMitigationActionsTaskStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class DeviceCertificateUpdateAction:
    """DeviceCertificateUpdateAction enum values."""

    DEACTIVATE = "DEACTIVATE"


class DeviceDefenderIndexingMode:
    """DeviceDefenderIndexingMode enum values."""

    OFF = "OFF"
    VIOLATIONS = "VIOLATIONS"


class DimensionType:
    """DimensionType enum values."""

    TOPIC_FILTER = "TOPIC_FILTER"


class DimensionValueOperator:
    """DimensionValueOperator enum values."""

    IN = "IN"
    NOT_IN = "NOT_IN"


class DisconnectReasonValue:
    """DisconnectReasonValue enum values."""

    AUTH_ERROR = "AUTH_ERROR"
    CLIENT_INITIATED_DISCONNECT = "CLIENT_INITIATED_DISCONNECT"
    CLIENT_ERROR = "CLIENT_ERROR"
    CONNECTION_LOST = "CONNECTION_LOST"
    DUPLICATE_CLIENTID = "DUPLICATE_CLIENTID"
    FORBIDDEN_ACCESS = "FORBIDDEN_ACCESS"
    MQTT_KEEP_ALIVE_TIMEOUT = "MQTT_KEEP_ALIVE_TIMEOUT"
    SERVER_ERROR = "SERVER_ERROR"
    SERVER_INITIATED_DISCONNECT = "SERVER_INITIATED_DISCONNECT"
    THROTTLED = "THROTTLED"
    WEBSOCKET_TTL_EXPIRATION = "WEBSOCKET_TTL_EXPIRATION"
    CUSTOMAUTH_TTL_EXPIRATION = "CUSTOMAUTH_TTL_EXPIRATION"
    UNKNOWN = "UNKNOWN"
    NONE = "NONE"


class DomainConfigurationStatus:
    """DomainConfigurationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DomainType:
    """DomainType enum values."""

    ENDPOINT = "ENDPOINT"
    AWS_MANAGED = "AWS_MANAGED"
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"


class DynamicGroupStatus:
    """DynamicGroupStatus enum values."""

    ACTIVE = "ACTIVE"
    BUILDING = "BUILDING"
    REBUILDING = "REBUILDING"


class DynamoKeyType:
    """DynamoKeyType enum values."""

    STRING = "STRING"
    NUMBER = "NUMBER"


class EncryptionType:
    """EncryptionType enum values."""

    CUSTOMER_MANAGED_KMS_KEY = "CUSTOMER_MANAGED_KMS_KEY"
    AWS_OWNED_KMS_KEY = "AWS_OWNED_KMS_KEY"


class EventType:
    """EventType enum values."""

    THING = "THING"
    THING_GROUP = "THING_GROUP"
    THING_TYPE = "THING_TYPE"
    THING_GROUP_MEMBERSHIP = "THING_GROUP_MEMBERSHIP"
    THING_GROUP_HIERARCHY = "THING_GROUP_HIERARCHY"
    THING_TYPE_ASSOCIATION = "THING_TYPE_ASSOCIATION"
    JOB = "JOB"
    JOB_EXECUTION = "JOB_EXECUTION"
    POLICY = "POLICY"
    CERTIFICATE = "CERTIFICATE"
    CA_CERTIFICATE = "CA_CERTIFICATE"


class FieldType:
    """FieldType enum values."""

    NUMBER = "Number"
    STRING = "String"
    BOOLEAN = "Boolean"


class FleetMetricUnit:
    """FleetMetricUnit enum values."""

    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


class IndexStatus:
    """IndexStatus enum values."""

    ACTIVE = "ACTIVE"
    BUILDING = "BUILDING"
    REBUILDING = "REBUILDING"


class JobEndBehavior:
    """JobEndBehavior enum values."""

    STOP_ROLLOUT = "STOP_ROLLOUT"
    CANCEL = "CANCEL"
    FORCE_CANCEL = "FORCE_CANCEL"


class JobExecutionFailureType:
    """JobExecutionFailureType enum values."""

    FAILED = "FAILED"
    REJECTED = "REJECTED"
    TIMED_OUT = "TIMED_OUT"
    ALL = "ALL"


class JobExecutionStatus:
    """JobExecutionStatus enum values."""

    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    REJECTED = "REJECTED"
    REMOVED = "REMOVED"
    CANCELED = "CANCELED"


class JobStatus:
    """JobStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    SCHEDULED = "SCHEDULED"


class LogLevel:
    """LogLevel enum values."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"
    DISABLED = "DISABLED"


class LogTargetType:
    """LogTargetType enum values."""

    DEFAULT = "DEFAULT"
    THING_GROUP = "THING_GROUP"
    CLIENT_ID = "CLIENT_ID"
    SOURCE_IP = "SOURCE_IP"
    PRINCIPAL_ID = "PRINCIPAL_ID"


class MessageFormat:
    """MessageFormat enum values."""

    RAW = "RAW"
    JSON = "JSON"


class MitigationActionType:
    """MitigationActionType enum values."""

    UPDATE_DEVICE_CERTIFICATE = "UPDATE_DEVICE_CERTIFICATE"
    UPDATE_CA_CERTIFICATE = "UPDATE_CA_CERTIFICATE"
    ADD_THINGS_TO_THING_GROUP = "ADD_THINGS_TO_THING_GROUP"
    REPLACE_DEFAULT_POLICY_VERSION = "REPLACE_DEFAULT_POLICY_VERSION"
    ENABLE_IOT_LOGGING = "ENABLE_IOT_LOGGING"
    PUBLISH_FINDING_TO_SNS = "PUBLISH_FINDING_TO_SNS"


class ModelStatus:
    """ModelStatus enum values."""

    PENDING_BUILD = "PENDING_BUILD"
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"


class NamedShadowIndexingMode:
    """NamedShadowIndexingMode enum values."""

    OFF = "OFF"
    ON = "ON"


class OTAUpdateStatus:
    """OTAUpdateStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class OutputFormat:
    """OutputFormat enum values."""

    JSON = "JSON"
    CBOR = "CBOR"


class PackageVersionAction:
    """PackageVersionAction enum values."""

    PUBLISH = "PUBLISH"
    DEPRECATE = "DEPRECATE"


class PackageVersionStatus:
    """PackageVersionStatus enum values."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DEPRECATED = "DEPRECATED"


class PolicyTemplateName:
    """PolicyTemplateName enum values."""

    BLANK_POLICY = "BLANK_POLICY"


class Protocol:
    """Protocol enum values."""

    MQTT = "MQTT"
    HTTP = "HTTP"


class ReportType:
    """ReportType enum values."""

    ERRORS = "ERRORS"
    RESULTS = "RESULTS"


class ResourceType:
    """ResourceType enum values."""

    DEVICE_CERTIFICATE = "DEVICE_CERTIFICATE"
    CA_CERTIFICATE = "CA_CERTIFICATE"
    IOT_POLICY = "IOT_POLICY"
    COGNITO_IDENTITY_POOL = "COGNITO_IDENTITY_POOL"
    CLIENT_ID = "CLIENT_ID"
    ACCOUNT_SETTINGS = "ACCOUNT_SETTINGS"
    ROLE_ALIAS = "ROLE_ALIAS"
    IAM_ROLE = "IAM_ROLE"
    ISSUER_CERTIFICATE = "ISSUER_CERTIFICATE"


class RetryableFailureType:
    """RetryableFailureType enum values."""

    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    ALL = "ALL"


class SbomValidationErrorCode:
    """SbomValidationErrorCode enum values."""

    INCOMPATIBLE_FORMAT = "INCOMPATIBLE_FORMAT"
    FILE_SIZE_LIMIT_EXCEEDED = "FILE_SIZE_LIMIT_EXCEEDED"


class SbomValidationResult:
    """SbomValidationResult enum values."""

    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class SbomValidationStatus:
    """SbomValidationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class ServerCertificateStatus:
    """ServerCertificateStatus enum values."""

    INVALID = "INVALID"
    VALID = "VALID"


class ServiceType:
    """ServiceType enum values."""

    DATA = "DATA"
    CREDENTIAL_PROVIDER = "CREDENTIAL_PROVIDER"
    JOBS = "JOBS"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Status:
    """Status enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"


class TargetFieldOrder:
    """TargetFieldOrder enum values."""

    LATLON = "LatLon"
    LONLAT = "LonLat"


class TargetSelection:
    """TargetSelection enum values."""

    CONTINUOUS = "CONTINUOUS"
    SNAPSHOT = "SNAPSHOT"


class TemplateType:
    """TemplateType enum values."""

    FLEET_PROVISIONING = "FLEET_PROVISIONING"
    JITP = "JITP"


class ThingConnectivityIndexingMode:
    """ThingConnectivityIndexingMode enum values."""

    OFF = "OFF"
    STATUS = "STATUS"


class ThingGroupIndexingMode:
    """ThingGroupIndexingMode enum values."""

    OFF = "OFF"
    ON = "ON"


class ThingIndexingMode:
    """ThingIndexingMode enum values."""

    OFF = "OFF"
    REGISTRY = "REGISTRY"
    REGISTRY_AND_SHADOW = "REGISTRY_AND_SHADOW"


class ThingPrincipalType:
    """ThingPrincipalType enum values."""

    EXCLUSIVE_THING = "EXCLUSIVE_THING"
    NON_EXCLUSIVE_THING = "NON_EXCLUSIVE_THING"


class TopicRuleDestinationStatus:
    """TopicRuleDestinationStatus enum values."""

    ENABLED = "ENABLED"
    IN_PROGRESS = "IN_PROGRESS"
    DISABLED = "DISABLED"
    ERROR = "ERROR"
    DELETING = "DELETING"


class VerificationState:
    """VerificationState enum values."""

    FALSE_POSITIVE = "FALSE_POSITIVE"
    BENIGN_POSITIVE = "BENIGN_POSITIVE"
    TRUE_POSITIVE = "TRUE_POSITIVE"
    UNKNOWN = "UNKNOWN"


class ViolationEventType:
    """ViolationEventType enum values."""

    IN_ALARM = "in-alarm"
    ALARM_CLEARED = "alarm-cleared"
    ALARM_INVALIDATED = "alarm-invalidated"


@dataclass
class Action(PropertyType):
    S3 = "S3"
    CLOUDWATCH_ALARM = "CloudwatchAlarm"
    IOT_EVENTS = "IotEvents"
    FIREHOSE = "Firehose"
    REPUBLISH = "Republish"
    KAFKA = "Kafka"
    STEP_FUNCTIONS = "StepFunctions"
    DYNAMO_DB = "DynamoDB"
    HTTP = "Http"
    OPEN_SEARCH = "OpenSearch"
    DYNAMO_D_BV2 = "DynamoDBv2"
    CLOUDWATCH_METRIC = "CloudwatchMetric"
    IOT_SITE_WISE = "IotSiteWise"
    ELASTICSEARCH = "Elasticsearch"
    SQS = "Sqs"
    KINESIS = "Kinesis"
    CLOUDWATCH_LOGS = "CloudwatchLogs"
    TIMESTREAM = "Timestream"
    IOT_ANALYTICS = "IotAnalytics"
    SNS = "Sns"
    LAMBDA = "Lambda"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "cloudwatch_alarm": "CloudwatchAlarm",
        "iot_events": "IotEvents",
        "firehose": "Firehose",
        "republish": "Republish",
        "kafka": "Kafka",
        "step_functions": "StepFunctions",
        "dynamo_db": "DynamoDB",
        "http": "Http",
        "open_search": "OpenSearch",
        "dynamo_d_bv2": "DynamoDBv2",
        "cloudwatch_metric": "CloudwatchMetric",
        "iot_site_wise": "IotSiteWise",
        "elasticsearch": "Elasticsearch",
        "sqs": "Sqs",
        "kinesis": "Kinesis",
        "cloudwatch_logs": "CloudwatchLogs",
        "timestream": "Timestream",
        "iot_analytics": "IotAnalytics",
        "sns": "Sns",
        "lambda_": "Lambda",
        "location": "Location",
    }

    s3: Optional[S3Action] = None
    cloudwatch_alarm: Optional[CloudwatchAlarmAction] = None
    iot_events: Optional[IotEventsAction] = None
    firehose: Optional[FirehoseAction] = None
    republish: Optional[RepublishAction] = None
    kafka: Optional[KafkaAction] = None
    step_functions: Optional[StepFunctionsAction] = None
    dynamo_db: Optional[DynamoDBAction] = None
    http: Optional[HttpAction] = None
    open_search: Optional[OpenSearchAction] = None
    dynamo_d_bv2: Optional[DynamoDBv2Action] = None
    cloudwatch_metric: Optional[CloudwatchMetricAction] = None
    iot_site_wise: Optional[IotSiteWiseAction] = None
    elasticsearch: Optional[ElasticsearchAction] = None
    sqs: Optional[SqsAction] = None
    kinesis: Optional[KinesisAction] = None
    cloudwatch_logs: Optional[CloudwatchLogsAction] = None
    timestream: Optional[TimestreamAction] = None
    iot_analytics: Optional[IotAnalyticsAction] = None
    sns: Optional[SnsAction] = None
    lambda_: Optional[LambdaAction] = None
    location: Optional[LocationAction] = None


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
class CloudwatchAlarmAction(PropertyType):
    ALARM_NAME = "AlarmName"
    STATE_REASON = "StateReason"
    STATE_VALUE = "StateValue"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_name": "AlarmName",
        "state_reason": "StateReason",
        "state_value": "StateValue",
        "role_arn": "RoleArn",
    }

    alarm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudwatchLogsAction(PropertyType):
    BATCH_MODE = "BatchMode"
    LOG_GROUP_NAME = "LogGroupName"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_mode": "BatchMode",
        "log_group_name": "LogGroupName",
        "role_arn": "RoleArn",
    }

    batch_mode: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudwatchMetricAction(PropertyType):
    METRIC_NAME = "MetricName"
    METRIC_VALUE = "MetricValue"
    METRIC_NAMESPACE = "MetricNamespace"
    METRIC_UNIT = "MetricUnit"
    ROLE_ARN = "RoleArn"
    METRIC_TIMESTAMP = "MetricTimestamp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "metric_value": "MetricValue",
        "metric_namespace": "MetricNamespace",
        "metric_unit": "MetricUnit",
        "role_arn": "RoleArn",
        "metric_timestamp": "MetricTimestamp",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_timestamp: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynamoDBAction(PropertyType):
    TABLE_NAME = "TableName"
    PAYLOAD_FIELD = "PayloadField"
    RANGE_KEY_FIELD = "RangeKeyField"
    HASH_KEY_FIELD = "HashKeyField"
    RANGE_KEY_VALUE = "RangeKeyValue"
    RANGE_KEY_TYPE = "RangeKeyType"
    HASH_KEY_TYPE = "HashKeyType"
    HASH_KEY_VALUE = "HashKeyValue"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "payload_field": "PayloadField",
        "range_key_field": "RangeKeyField",
        "hash_key_field": "HashKeyField",
        "range_key_value": "RangeKeyValue",
        "range_key_type": "RangeKeyType",
        "hash_key_type": "HashKeyType",
        "hash_key_value": "HashKeyValue",
        "role_arn": "RoleArn",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hash_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_key_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hash_key_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hash_key_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynamoDBv2Action(PropertyType):
    PUT_ITEM = "PutItem"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "put_item": "PutItem",
        "role_arn": "RoleArn",
    }

    put_item: Optional[PutItemInput] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticsearchAction(PropertyType):
    TYPE = "Type"
    ENDPOINT = "Endpoint"
    INDEX = "Index"
    ID = "Id"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "endpoint": "Endpoint",
        "index": "Index",
        "id": "Id",
        "role_arn": "RoleArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FirehoseAction(PropertyType):
    DELIVERY_STREAM_NAME = "DeliveryStreamName"
    BATCH_MODE = "BatchMode"
    ROLE_ARN = "RoleArn"
    SEPARATOR = "Separator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_name": "DeliveryStreamName",
        "batch_mode": "BatchMode",
        "role_arn": "RoleArn",
        "separator": "Separator",
    }

    delivery_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    batch_mode: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    separator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpAction(PropertyType):
    HEADERS = "Headers"
    AUTH = "Auth"
    CONFIRMATION_URL = "ConfirmationUrl"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "headers": "Headers",
        "auth": "Auth",
        "confirmation_url": "ConfirmationUrl",
        "url": "Url",
    }

    headers: Optional[list[HttpActionHeader]] = None
    auth: Optional[HttpAuthorization] = None
    confirmation_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpActionHeader(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpAuthorization(PropertyType):
    SIGV4 = "Sigv4"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sigv4": "Sigv4",
    }

    sigv4: Optional[SigV4Authorization] = None


@dataclass
class IotAnalyticsAction(PropertyType):
    CHANNEL_NAME = "ChannelName"
    BATCH_MODE = "BatchMode"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_name": "ChannelName",
        "batch_mode": "BatchMode",
        "role_arn": "RoleArn",
    }

    channel_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    batch_mode: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IotEventsAction(PropertyType):
    INPUT_NAME = "InputName"
    BATCH_MODE = "BatchMode"
    ROLE_ARN = "RoleArn"
    MESSAGE_ID = "MessageId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_name": "InputName",
        "batch_mode": "BatchMode",
        "role_arn": "RoleArn",
        "message_id": "MessageId",
    }

    input_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    batch_mode: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IotSiteWiseAction(PropertyType):
    PUT_ASSET_PROPERTY_VALUE_ENTRIES = "PutAssetPropertyValueEntries"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "put_asset_property_value_entries": "PutAssetPropertyValueEntries",
        "role_arn": "RoleArn",
    }

    put_asset_property_value_entries: Optional[list[PutAssetPropertyValueEntry]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KafkaAction(PropertyType):
    PARTITION = "Partition"
    CLIENT_PROPERTIES = "ClientProperties"
    HEADERS = "Headers"
    TOPIC = "Topic"
    DESTINATION_ARN = "DestinationArn"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partition": "Partition",
        "client_properties": "ClientProperties",
        "headers": "Headers",
        "topic": "Topic",
        "destination_arn": "DestinationArn",
        "key": "Key",
    }

    partition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_properties: Optional[dict[str, str]] = None
    headers: Optional[list[KafkaActionHeader]] = None
    topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KafkaActionHeader(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisAction(PropertyType):
    STREAM_NAME = "StreamName"
    PARTITION_KEY = "PartitionKey"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_name": "StreamName",
        "partition_key": "PartitionKey",
        "role_arn": "RoleArn",
    }

    stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    partition_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaAction(PropertyType):
    FUNCTION_ARN = "FunctionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionArn",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LocationAction(PropertyType):
    TRACKER_NAME = "TrackerName"
    DEVICE_ID = "DeviceId"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"
    TIMESTAMP = "Timestamp"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tracker_name": "TrackerName",
        "device_id": "DeviceId",
        "latitude": "Latitude",
        "longitude": "Longitude",
        "timestamp": "Timestamp",
        "role_arn": "RoleArn",
    }

    tracker_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    latitude: Optional[Union[str, Ref, GetAtt, Sub]] = None
    longitude: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp: Optional[Timestamp] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchAction(PropertyType):
    TYPE = "Type"
    ENDPOINT = "Endpoint"
    INDEX = "Index"
    ID = "Id"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "endpoint": "Endpoint",
        "index": "Index",
        "id": "Id",
        "role_arn": "RoleArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PutAssetPropertyValueEntry(PropertyType):
    PROPERTY_VALUES = "PropertyValues"
    ENTRY_ID = "EntryId"
    PROPERTY_ALIAS = "PropertyAlias"
    ASSET_ID = "AssetId"
    PROPERTY_ID = "PropertyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "property_values": "PropertyValues",
        "entry_id": "EntryId",
        "property_alias": "PropertyAlias",
        "asset_id": "AssetId",
        "property_id": "PropertyId",
    }

    property_values: Optional[list[AssetPropertyValue]] = None
    entry_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    asset_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PutItemInput(PropertyType):
    TABLE_NAME = "TableName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RepublishAction(PropertyType):
    QOS = "Qos"
    HEADERS = "Headers"
    TOPIC = "Topic"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "qos": "Qos",
        "headers": "Headers",
        "topic": "Topic",
        "role_arn": "RoleArn",
    }

    qos: Optional[Union[int, Ref, GetAtt, Sub]] = None
    headers: Optional[RepublishActionHeaders] = None
    topic: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RepublishActionHeaders(PropertyType):
    CORRELATION_DATA = "CorrelationData"
    USER_PROPERTIES = "UserProperties"
    PAYLOAD_FORMAT_INDICATOR = "PayloadFormatIndicator"
    CONTENT_TYPE = "ContentType"
    MESSAGE_EXPIRY = "MessageExpiry"
    RESPONSE_TOPIC = "ResponseTopic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "correlation_data": "CorrelationData",
        "user_properties": "UserProperties",
        "payload_format_indicator": "PayloadFormatIndicator",
        "content_type": "ContentType",
        "message_expiry": "MessageExpiry",
        "response_topic": "ResponseTopic",
    }

    correlation_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_properties: Optional[list[UserProperty]] = None
    payload_format_indicator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_expiry: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_topic: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Action(PropertyType):
    BUCKET_NAME = "BucketName"
    CANNED_ACL = "CannedAcl"
    KEY = "Key"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "canned_acl": "CannedAcl",
        "key": "Key",
        "role_arn": "RoleArn",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    canned_acl: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SigV4Authorization(PropertyType):
    SERVICE_NAME = "ServiceName"
    SIGNING_REGION = "SigningRegion"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_name": "ServiceName",
        "signing_region": "SigningRegion",
        "role_arn": "RoleArn",
    }

    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signing_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnsAction(PropertyType):
    MESSAGE_FORMAT = "MessageFormat"
    TARGET_ARN = "TargetArn"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message_format": "MessageFormat",
        "target_arn": "TargetArn",
        "role_arn": "RoleArn",
    }

    message_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SqsAction(PropertyType):
    USE_BASE64 = "UseBase64"
    ROLE_ARN = "RoleArn"
    QUEUE_URL = "QueueUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "use_base64": "UseBase64",
        "role_arn": "RoleArn",
        "queue_url": "QueueUrl",
    }

    use_base64: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    queue_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StepFunctionsAction(PropertyType):
    EXECUTION_NAME_PREFIX = "ExecutionNamePrefix"
    STATE_MACHINE_NAME = "StateMachineName"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_name_prefix": "ExecutionNamePrefix",
        "state_machine_name": "StateMachineName",
        "role_arn": "RoleArn",
    }

    execution_name_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state_machine_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Timestamp(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimestreamAction(PropertyType):
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    DIMENSIONS = "Dimensions"
    TIMESTAMP = "Timestamp"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "dimensions": "Dimensions",
        "timestamp": "Timestamp",
        "role_arn": "RoleArn",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[TimestreamDimension]] = None
    timestamp: Optional[TimestreamTimestamp] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimestreamDimension(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimestreamTimestamp(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TopicRulePayload(PropertyType):
    RULE_DISABLED = "RuleDisabled"
    ERROR_ACTION = "ErrorAction"
    DESCRIPTION = "Description"
    AWS_IOT_SQL_VERSION = "AwsIotSqlVersion"
    ACTIONS = "Actions"
    SQL = "Sql"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_disabled": "RuleDisabled",
        "error_action": "ErrorAction",
        "description": "Description",
        "aws_iot_sql_version": "AwsIotSqlVersion",
        "actions": "Actions",
        "sql": "Sql",
    }

    rule_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    error_action: Optional[Action] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_iot_sql_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    actions: Optional[list[Action]] = None
    sql: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserProperty(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

