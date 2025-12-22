"""PropertyTypes for AWS::IoTSiteWise::Portal."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AggregateType:
    """AggregateType enum values."""

    AVERAGE = "AVERAGE"
    COUNT = "COUNT"
    MAXIMUM = "MAXIMUM"
    MINIMUM = "MINIMUM"
    SUM = "SUM"
    STANDARD_DEVIATION = "STANDARD_DEVIATION"


class AssetErrorCode:
    """AssetErrorCode enum values."""

    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class AssetModelState:
    """AssetModelState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    PROPAGATING = "PROPAGATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class AssetModelType:
    """AssetModelType enum values."""

    ASSET_MODEL = "ASSET_MODEL"
    COMPONENT_MODEL = "COMPONENT_MODEL"
    INTERFACE = "INTERFACE"


class AssetModelVersionType:
    """AssetModelVersionType enum values."""

    LATEST = "LATEST"
    ACTIVE = "ACTIVE"


class AssetRelationshipType:
    """AssetRelationshipType enum values."""

    HIERARCHY = "HIERARCHY"


class AssetState:
    """AssetState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class AuthMode:
    """AuthMode enum values."""

    IAM = "IAM"
    SSO = "SSO"


class BatchEntryCompletionStatus:
    """BatchEntryCompletionStatus enum values."""

    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class BatchGetAssetPropertyAggregatesErrorCode:
    """BatchGetAssetPropertyAggregatesErrorCode enum values."""

    RESOURCENOTFOUNDEXCEPTION = "ResourceNotFoundException"
    INVALIDREQUESTEXCEPTION = "InvalidRequestException"
    ACCESSDENIEDEXCEPTION = "AccessDeniedException"


class BatchGetAssetPropertyValueErrorCode:
    """BatchGetAssetPropertyValueErrorCode enum values."""

    RESOURCENOTFOUNDEXCEPTION = "ResourceNotFoundException"
    INVALIDREQUESTEXCEPTION = "InvalidRequestException"
    ACCESSDENIEDEXCEPTION = "AccessDeniedException"


class BatchGetAssetPropertyValueHistoryErrorCode:
    """BatchGetAssetPropertyValueHistoryErrorCode enum values."""

    RESOURCENOTFOUNDEXCEPTION = "ResourceNotFoundException"
    INVALIDREQUESTEXCEPTION = "InvalidRequestException"
    ACCESSDENIEDEXCEPTION = "AccessDeniedException"


class BatchPutAssetPropertyValueErrorCode:
    """BatchPutAssetPropertyValueErrorCode enum values."""

    RESOURCENOTFOUNDEXCEPTION = "ResourceNotFoundException"
    INVALIDREQUESTEXCEPTION = "InvalidRequestException"
    INTERNALFAILUREEXCEPTION = "InternalFailureException"
    SERVICEUNAVAILABLEEXCEPTION = "ServiceUnavailableException"
    THROTTLINGEXCEPTION = "ThrottlingException"
    LIMITEXCEEDEDEXCEPTION = "LimitExceededException"
    CONFLICTINGOPERATIONEXCEPTION = "ConflictingOperationException"
    TIMESTAMPOUTOFRANGEEXCEPTION = "TimestampOutOfRangeException"
    ACCESSDENIEDEXCEPTION = "AccessDeniedException"


class CapabilitySyncStatus:
    """CapabilitySyncStatus enum values."""

    IN_SYNC = "IN_SYNC"
    OUT_OF_SYNC = "OUT_OF_SYNC"
    SYNC_FAILED = "SYNC_FAILED"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class ColumnName:
    """ColumnName enum values."""

    ALIAS = "ALIAS"
    ASSET_ID = "ASSET_ID"
    PROPERTY_ID = "PROPERTY_ID"
    DATA_TYPE = "DATA_TYPE"
    TIMESTAMP_SECONDS = "TIMESTAMP_SECONDS"
    TIMESTAMP_NANO_OFFSET = "TIMESTAMP_NANO_OFFSET"
    QUALITY = "QUALITY"
    VALUE = "VALUE"


class ComputationModelState:
    """ComputationModelState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ComputationModelType:
    """ComputationModelType enum values."""

    ANOMALY_DETECTION = "ANOMALY_DETECTION"


class ComputeLocation:
    """ComputeLocation enum values."""

    EDGE = "EDGE"
    CLOUD = "CLOUD"


class ConfigurationState:
    """ConfigurationState enum values."""

    ACTIVE = "ACTIVE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class CoreDeviceOperatingSystem:
    """CoreDeviceOperatingSystem enum values."""

    LINUX_AARCH64 = "LINUX_AARCH64"
    LINUX_AMD64 = "LINUX_AMD64"
    WINDOWS_AMD64 = "WINDOWS_AMD64"


class DatasetSourceFormat:
    """DatasetSourceFormat enum values."""

    KNOWLEDGE_BASE = "KNOWLEDGE_BASE"


class DatasetSourceType:
    """DatasetSourceType enum values."""

    KENDRA = "KENDRA"


class DatasetState:
    """DatasetState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class DetailedErrorCode:
    """DetailedErrorCode enum values."""

    INCOMPATIBLE_COMPUTE_LOCATION = "INCOMPATIBLE_COMPUTE_LOCATION"
    INCOMPATIBLE_FORWARDING_CONFIGURATION = "INCOMPATIBLE_FORWARDING_CONFIGURATION"


class DisassociatedDataStorageState:
    """DisassociatedDataStorageState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EncryptionType:
    """EncryptionType enum values."""

    SITEWISE_DEFAULT_ENCRYPTION = "SITEWISE_DEFAULT_ENCRYPTION"
    KMS_BASED_ENCRYPTION = "KMS_BASED_ENCRYPTION"


class ErrorCode:
    """ErrorCode enum values."""

    VALIDATION_ERROR = "VALIDATION_ERROR"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class ExecutionState:
    """ExecutionState enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ForwardingConfigState:
    """ForwardingConfigState enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class IdentityType:
    """IdentityType enum values."""

    USER = "USER"
    GROUP = "GROUP"
    IAM = "IAM"


class ImageFileType:
    """ImageFileType enum values."""

    PNG = "PNG"


class JobStatus:
    """JobStatus enum values."""

    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"


class ListAssetModelPropertiesFilter:
    """ListAssetModelPropertiesFilter enum values."""

    ALL = "ALL"
    BASE = "BASE"


class ListAssetPropertiesFilter:
    """ListAssetPropertiesFilter enum values."""

    ALL = "ALL"
    BASE = "BASE"


class ListAssetsFilter:
    """ListAssetsFilter enum values."""

    ALL = "ALL"
    TOP_LEVEL = "TOP_LEVEL"


class ListBulkImportJobsFilter:
    """ListBulkImportJobsFilter enum values."""

    ALL = "ALL"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"
    COMPLETED = "COMPLETED"


class ListTimeSeriesType:
    """ListTimeSeriesType enum values."""

    ASSOCIATED = "ASSOCIATED"
    DISASSOCIATED = "DISASSOCIATED"


class LoggingLevel:
    """LoggingLevel enum values."""

    ERROR = "ERROR"
    INFO = "INFO"
    OFF = "OFF"


class MonitorErrorCode:
    """MonitorErrorCode enum values."""

    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"


class Permission:
    """Permission enum values."""

    ADMINISTRATOR = "ADMINISTRATOR"
    VIEWER = "VIEWER"


class PortalState:
    """PortalState enum values."""

    CREATING = "CREATING"
    PENDING = "PENDING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class PortalType:
    """PortalType enum values."""

    SITEWISE_PORTAL_V1 = "SITEWISE_PORTAL_V1"
    SITEWISE_PORTAL_V2 = "SITEWISE_PORTAL_V2"


class PropertyDataType:
    """PropertyDataType enum values."""

    STRING = "STRING"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"
    STRUCT = "STRUCT"


class PropertyNotificationState:
    """PropertyNotificationState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Quality:
    """Quality enum values."""

    GOOD = "GOOD"
    BAD = "BAD"
    UNCERTAIN = "UNCERTAIN"


class RawValueType:
    """RawValueType enum values."""

    D = "D"
    B = "B"
    S = "S"
    I = "I"
    U = "U"


class ResolveToResourceType:
    """ResolveToResourceType enum values."""

    ASSET = "ASSET"


class ResourceType:
    """ResourceType enum values."""

    PORTAL = "PORTAL"
    PROJECT = "PROJECT"


class ScalarType:
    """ScalarType enum values."""

    BOOLEAN = "BOOLEAN"
    INT = "INT"
    DOUBLE = "DOUBLE"
    TIMESTAMP = "TIMESTAMP"
    STRING = "STRING"


class StorageType:
    """StorageType enum values."""

    SITEWISE_DEFAULT_STORAGE = "SITEWISE_DEFAULT_STORAGE"
    MULTI_LAYER_STORAGE = "MULTI_LAYER_STORAGE"


class TargetResourceType:
    """TargetResourceType enum values."""

    ASSET = "ASSET"
    COMPUTATION_MODEL = "COMPUTATION_MODEL"


class TimeOrdering:
    """TimeOrdering enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class TraversalDirection:
    """TraversalDirection enum values."""

    PARENT = "PARENT"
    CHILD = "CHILD"


class TraversalType:
    """TraversalType enum values."""

    PATH_TO_ROOT = "PATH_TO_ROOT"


class WarmTierState:
    """WarmTierState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclass
class Alarms(PropertyType):
    NOTIFICATION_LAMBDA_ARN = "NotificationLambdaArn"
    ALARM_ROLE_ARN = "AlarmRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_lambda_arn": "NotificationLambdaArn",
        "alarm_role_arn": "AlarmRoleArn",
    }

    notification_lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alarm_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortalTypeEntry(PropertyType):
    PORTAL_TOOLS = "PortalTools"

    _property_mappings: ClassVar[dict[str, str]] = {
        "portal_tools": "PortalTools",
    }

    portal_tools: Optional[Union[list[str], Ref]] = None

