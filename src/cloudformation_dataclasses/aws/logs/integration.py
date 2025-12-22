"""PropertyTypes for AWS::Logs::Integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionStatus:
    """ActionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CLIENT_ERROR = "CLIENT_ERROR"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"


class AnomalyDetectorStatus:
    """AnomalyDetectorStatus enum values."""

    INITIALIZING = "INITIALIZING"
    TRAINING = "TRAINING"
    ANALYZING = "ANALYZING"
    FAILED = "FAILED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class DataProtectionStatus:
    """DataProtectionStatus enum values."""

    ACTIVATED = "ACTIVATED"
    DELETED = "DELETED"
    ARCHIVED = "ARCHIVED"
    DISABLED = "DISABLED"


class DeliveryDestinationType:
    """DeliveryDestinationType enum values."""

    S3 = "S3"
    CWL = "CWL"
    FH = "FH"
    XRAY = "XRAY"


class Distribution:
    """Distribution enum values."""

    RANDOM = "Random"
    BYLOGSTREAM = "ByLogStream"


class EntityRejectionErrorType:
    """EntityRejectionErrorType enum values."""

    INVALIDENTITY = "InvalidEntity"
    INVALIDTYPEVALUE = "InvalidTypeValue"
    INVALIDKEYATTRIBUTES = "InvalidKeyAttributes"
    INVALIDATTRIBUTES = "InvalidAttributes"
    ENTITYSIZETOOLARGE = "EntitySizeTooLarge"
    UNSUPPORTEDLOGGROUPTYPE = "UnsupportedLogGroupType"
    MISSINGREQUIREDFIELDS = "MissingRequiredFields"


class EvaluationFrequency:
    """EvaluationFrequency enum values."""

    ONE_MIN = "ONE_MIN"
    FIVE_MIN = "FIVE_MIN"
    TEN_MIN = "TEN_MIN"
    FIFTEEN_MIN = "FIFTEEN_MIN"
    THIRTY_MIN = "THIRTY_MIN"
    ONE_HOUR = "ONE_HOUR"


class EventSource:
    """EventSource enum values."""

    CLOUDTRAIL = "CloudTrail"
    ROUTE53RESOLVER = "Route53Resolver"
    VPCFLOW = "VPCFlow"
    EKSAUDIT = "EKSAudit"
    AWSWAF = "AWSWAF"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    RUNNING = "Running"
    INVALIDQUERY = "InvalidQuery"
    COMPLETE = "Complete"
    FAILED = "Failed"
    TIMEOUT = "Timeout"


class ExportTaskStatusCode:
    """ExportTaskStatusCode enum values."""

    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PENDING_CANCEL = "PENDING_CANCEL"
    RUNNING = "RUNNING"


class FlattenedElement:
    """FlattenedElement enum values."""

    FIRST = "first"
    LAST = "last"


class ImportStatus:
    """ImportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class IndexSource:
    """IndexSource enum values."""

    ACCOUNT = "ACCOUNT"
    LOG_GROUP = "LOG_GROUP"


class IndexType:
    """IndexType enum values."""

    FACET = "FACET"
    FIELD_INDEX = "FIELD_INDEX"


class InheritedProperty:
    """InheritedProperty enum values."""

    ACCOUNT_DATA_PROTECTION = "ACCOUNT_DATA_PROTECTION"


class IntegrationStatus:
    """IntegrationStatus enum values."""

    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class IntegrationType:
    """IntegrationType enum values."""

    OPENSEARCH = "OPENSEARCH"


class ListAggregateLogGroupSummariesGroupBy:
    """ListAggregateLogGroupSummariesGroupBy enum values."""

    DATA_SOURCE_NAME_TYPE_AND_FORMAT = "DATA_SOURCE_NAME_TYPE_AND_FORMAT"
    DATA_SOURCE_NAME_AND_TYPE = "DATA_SOURCE_NAME_AND_TYPE"


class LogGroupClass:
    """LogGroupClass enum values."""

    STANDARD = "STANDARD"
    INFREQUENT_ACCESS = "INFREQUENT_ACCESS"
    DELIVERY = "DELIVERY"


class OCSFVersion:
    """OCSFVersion enum values."""

    V1_1 = "V1.1"
    V1_5 = "V1.5"


class OpenSearchResourceStatusType:
    """OpenSearchResourceStatusType enum values."""

    ACTIVE = "ACTIVE"
    NOT_FOUND = "NOT_FOUND"
    ERROR = "ERROR"


class OrderBy:
    """OrderBy enum values."""

    LOGSTREAMNAME = "LogStreamName"
    LASTEVENTTIME = "LastEventTime"


class OutputFormat:
    """OutputFormat enum values."""

    JSON = "json"
    PLAIN = "plain"
    W3C = "w3c"
    RAW = "raw"
    PARQUET = "parquet"


class PolicyScope:
    """PolicyScope enum values."""

    ACCOUNT = "ACCOUNT"
    RESOURCE = "RESOURCE"


class PolicyType:
    """PolicyType enum values."""

    DATA_PROTECTION_POLICY = "DATA_PROTECTION_POLICY"
    SUBSCRIPTION_FILTER_POLICY = "SUBSCRIPTION_FILTER_POLICY"
    FIELD_INDEX_POLICY = "FIELD_INDEX_POLICY"
    TRANSFORMER_POLICY = "TRANSFORMER_POLICY"
    METRIC_EXTRACTION_POLICY = "METRIC_EXTRACTION_POLICY"


class QueryLanguage:
    """QueryLanguage enum values."""

    CWLI = "CWLI"
    SQL = "SQL"
    PPL = "PPL"


class QueryStatus:
    """QueryStatus enum values."""

    SCHEDULED = "Scheduled"
    RUNNING = "Running"
    COMPLETE = "Complete"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    TIMEOUT = "Timeout"
    UNKNOWN = "Unknown"


class S3TableIntegrationSourceStatus:
    """S3TableIntegrationSourceStatus enum values."""

    ACTIVE = "ACTIVE"
    UNHEALTHY = "UNHEALTHY"
    FAILED = "FAILED"
    DATA_SOURCE_DELETE_IN_PROGRESS = "DATA_SOURCE_DELETE_IN_PROGRESS"


class ScheduledQueryDestinationType:
    """ScheduledQueryDestinationType enum values."""

    S3 = "S3"


class ScheduledQueryState:
    """ScheduledQueryState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Scope:
    """Scope enum values."""

    ALL = "ALL"


class StandardUnit:
    """StandardUnit enum values."""

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


class State:
    """State enum values."""

    ACTIVE = "Active"
    SUPPRESSED = "Suppressed"
    BASELINE = "Baseline"


class SuppressionState:
    """SuppressionState enum values."""

    SUPPRESSED = "SUPPRESSED"
    UNSUPPRESSED = "UNSUPPRESSED"


class SuppressionType:
    """SuppressionType enum values."""

    LIMITED = "LIMITED"
    INFINITE = "INFINITE"


class SuppressionUnit:
    """SuppressionUnit enum values."""

    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"


class Type:
    """Type enum values."""

    BOOLEAN = "boolean"
    INTEGER = "integer"
    DOUBLE = "double"
    STRING = "string"


@dataclass
class OpenSearchResourceConfig(PropertyType):
    DASHBOARD_VIEWER_PRINCIPALS = "DashboardViewerPrincipals"
    APPLICATION_ARN = "ApplicationARN"
    KMS_KEY_ARN = "KmsKeyArn"
    RETENTION_DAYS = "RetentionDays"
    DATA_SOURCE_ROLE_ARN = "DataSourceRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dashboard_viewer_principals": "DashboardViewerPrincipals",
        "application_arn": "ApplicationARN",
        "kms_key_arn": "KmsKeyArn",
        "retention_days": "RetentionDays",
        "data_source_role_arn": "DataSourceRoleArn",
    }

    dashboard_viewer_principals: Optional[Union[list[str], Ref]] = None
    application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    data_source_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceConfig(PropertyType):
    OPEN_SEARCH_RESOURCE_CONFIG = "OpenSearchResourceConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "open_search_resource_config": "OpenSearchResourceConfig",
    }

    open_search_resource_config: Optional[OpenSearchResourceConfig] = None

