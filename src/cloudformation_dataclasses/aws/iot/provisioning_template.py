"""PropertyTypes for AWS::IoT::ProvisioningTemplate."""

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
class ProvisioningHook(PropertyType):
    TARGET_ARN = "TargetArn"
    PAYLOAD_VERSION = "PayloadVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_arn": "TargetArn",
        "payload_version": "PayloadVersion",
    }

    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

