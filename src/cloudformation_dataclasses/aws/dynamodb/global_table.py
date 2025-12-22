"""PropertyTypes for AWS::DynamoDB::GlobalTable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApproximateCreationDateTimePrecision:
    """ApproximateCreationDateTimePrecision enum values."""

    MILLISECOND = "MILLISECOND"
    MICROSECOND = "MICROSECOND"


class AttributeAction:
    """AttributeAction enum values."""

    ADD = "ADD"
    PUT = "PUT"
    DELETE = "DELETE"


class BackupStatus:
    """BackupStatus enum values."""

    CREATING = "CREATING"
    DELETED = "DELETED"
    AVAILABLE = "AVAILABLE"


class BackupType:
    """BackupType enum values."""

    USER = "USER"
    SYSTEM = "SYSTEM"
    AWS_BACKUP = "AWS_BACKUP"


class BackupTypeFilter:
    """BackupTypeFilter enum values."""

    USER = "USER"
    SYSTEM = "SYSTEM"
    AWS_BACKUP = "AWS_BACKUP"
    ALL = "ALL"


class BatchStatementErrorCodeEnum:
    """BatchStatementErrorCodeEnum enum values."""

    CONDITIONALCHECKFAILED = "ConditionalCheckFailed"
    ITEMCOLLECTIONSIZELIMITEXCEEDED = "ItemCollectionSizeLimitExceeded"
    REQUESTLIMITEXCEEDED = "RequestLimitExceeded"
    VALIDATIONERROR = "ValidationError"
    PROVISIONEDTHROUGHPUTEXCEEDED = "ProvisionedThroughputExceeded"
    TRANSACTIONCONFLICT = "TransactionConflict"
    THROTTLINGERROR = "ThrottlingError"
    INTERNALSERVERERROR = "InternalServerError"
    RESOURCENOTFOUND = "ResourceNotFound"
    ACCESSDENIED = "AccessDenied"
    DUPLICATEITEM = "DuplicateItem"


class BillingMode:
    """BillingMode enum values."""

    PROVISIONED = "PROVISIONED"
    PAY_PER_REQUEST = "PAY_PER_REQUEST"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    EQ = "EQ"
    NE = "NE"
    IN = "IN"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"
    BETWEEN = "BETWEEN"
    NOT_NULL = "NOT_NULL"
    NULL = "NULL"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    BEGINS_WITH = "BEGINS_WITH"


class ConditionalOperator:
    """ConditionalOperator enum values."""

    AND = "AND"
    OR = "OR"


class ContinuousBackupsStatus:
    """ContinuousBackupsStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ContributorInsightsAction:
    """ContributorInsightsAction enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class ContributorInsightsMode:
    """ContributorInsightsMode enum values."""

    ACCESSED_AND_THROTTLED_KEYS = "ACCESSED_AND_THROTTLED_KEYS"
    THROTTLED_KEYS = "THROTTLED_KEYS"


class ContributorInsightsStatus:
    """ContributorInsightsStatus enum values."""

    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    FAILED = "FAILED"


class DestinationStatus:
    """DestinationStatus enum values."""

    ENABLING = "ENABLING"
    ACTIVE = "ACTIVE"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    ENABLE_FAILED = "ENABLE_FAILED"
    UPDATING = "UPDATING"


class ExportFormat:
    """ExportFormat enum values."""

    DYNAMODB_JSON = "DYNAMODB_JSON"
    ION = "ION"


class ExportStatus:
    """ExportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ExportType:
    """ExportType enum values."""

    FULL_EXPORT = "FULL_EXPORT"
    INCREMENTAL_EXPORT = "INCREMENTAL_EXPORT"


class ExportViewType:
    """ExportViewType enum values."""

    NEW_IMAGE = "NEW_IMAGE"
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"


class GlobalTableStatus:
    """GlobalTableStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class ImportStatus:
    """ImportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class IndexStatus:
    """IndexStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


class InputCompressionType:
    """InputCompressionType enum values."""

    GZIP = "GZIP"
    ZSTD = "ZSTD"
    NONE = "NONE"


class InputFormat:
    """InputFormat enum values."""

    DYNAMODB_JSON = "DYNAMODB_JSON"
    ION = "ION"
    CSV = "CSV"


class KeyType:
    """KeyType enum values."""

    HASH = "HASH"
    RANGE = "RANGE"


class MultiRegionConsistency:
    """MultiRegionConsistency enum values."""

    EVENTUAL = "EVENTUAL"
    STRONG = "STRONG"


class PointInTimeRecoveryStatus:
    """PointInTimeRecoveryStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ProjectionType:
    """ProjectionType enum values."""

    ALL = "ALL"
    KEYS_ONLY = "KEYS_ONLY"
    INCLUDE = "INCLUDE"


class ReplicaStatus:
    """ReplicaStatus enum values."""

    CREATING = "CREATING"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    REGION_DISABLED = "REGION_DISABLED"
    INACCESSIBLE_ENCRYPTION_CREDENTIALS = "INACCESSIBLE_ENCRYPTION_CREDENTIALS"
    ARCHIVING = "ARCHIVING"
    ARCHIVED = "ARCHIVED"
    REPLICATION_NOT_AUTHORIZED = "REPLICATION_NOT_AUTHORIZED"


class ReturnConsumedCapacity:
    """ReturnConsumedCapacity enum values."""

    INDEXES = "INDEXES"
    TOTAL = "TOTAL"
    NONE = "NONE"


class ReturnItemCollectionMetrics:
    """ReturnItemCollectionMetrics enum values."""

    SIZE = "SIZE"
    NONE = "NONE"


class ReturnValue:
    """ReturnValue enum values."""

    NONE = "NONE"
    ALL_OLD = "ALL_OLD"
    UPDATED_OLD = "UPDATED_OLD"
    ALL_NEW = "ALL_NEW"
    UPDATED_NEW = "UPDATED_NEW"


class ReturnValuesOnConditionCheckFailure:
    """ReturnValuesOnConditionCheckFailure enum values."""

    ALL_OLD = "ALL_OLD"
    NONE = "NONE"


class S3SseAlgorithm:
    """S3SseAlgorithm enum values."""

    AES256 = "AES256"
    KMS = "KMS"


class SSEStatus:
    """SSEStatus enum values."""

    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    UPDATING = "UPDATING"


class SSEType:
    """SSEType enum values."""

    AES256 = "AES256"
    KMS = "KMS"


class ScalarAttributeType:
    """ScalarAttributeType enum values."""

    S = "S"
    N = "N"
    B = "B"


class Select:
    """Select enum values."""

    ALL_ATTRIBUTES = "ALL_ATTRIBUTES"
    ALL_PROJECTED_ATTRIBUTES = "ALL_PROJECTED_ATTRIBUTES"
    SPECIFIC_ATTRIBUTES = "SPECIFIC_ATTRIBUTES"
    COUNT = "COUNT"


class StreamViewType:
    """StreamViewType enum values."""

    NEW_IMAGE = "NEW_IMAGE"
    OLD_IMAGE = "OLD_IMAGE"
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"
    KEYS_ONLY = "KEYS_ONLY"


class TableClass:
    """TableClass enum values."""

    STANDARD = "STANDARD"
    STANDARD_INFREQUENT_ACCESS = "STANDARD_INFREQUENT_ACCESS"


class TableStatus:
    """TableStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    INACCESSIBLE_ENCRYPTION_CREDENTIALS = "INACCESSIBLE_ENCRYPTION_CREDENTIALS"
    ARCHIVING = "ARCHIVING"
    ARCHIVED = "ARCHIVED"
    REPLICATION_NOT_AUTHORIZED = "REPLICATION_NOT_AUTHORIZED"


class TimeToLiveStatus:
    """TimeToLiveStatus enum values."""

    ENABLING = "ENABLING"
    DISABLING = "DISABLING"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class WitnessStatus:
    """WitnessStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


@dataclass
class AttributeDefinition(PropertyType):
    ATTRIBUTE_TYPE = "AttributeType"
    ATTRIBUTE_NAME = "AttributeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_type": "AttributeType",
        "attribute_name": "AttributeName",
    }

    attribute_type: Optional[Union[str, AttributeType, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityAutoScalingSettings(PropertyType):
    MIN_CAPACITY = "MinCapacity"
    SEED_CAPACITY = "SeedCapacity"
    TARGET_TRACKING_SCALING_POLICY_CONFIGURATION = "TargetTrackingScalingPolicyConfiguration"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_capacity": "MinCapacity",
        "seed_capacity": "SeedCapacity",
        "target_tracking_scaling_policy_configuration": "TargetTrackingScalingPolicyConfiguration",
        "max_capacity": "MaxCapacity",
    }

    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    seed_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_tracking_scaling_policy_configuration: Optional[TargetTrackingScalingPolicyConfiguration] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ContributorInsightsSpecification(PropertyType):
    MODE = "Mode"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "enabled": "Enabled",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GlobalSecondaryIndex(PropertyType):
    INDEX_NAME = "IndexName"
    PROJECTION = "Projection"
    KEY_SCHEMA = "KeySchema"
    WARM_THROUGHPUT = "WarmThroughput"
    WRITE_PROVISIONED_THROUGHPUT_SETTINGS = "WriteProvisionedThroughputSettings"
    WRITE_ON_DEMAND_THROUGHPUT_SETTINGS = "WriteOnDemandThroughputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "projection": "Projection",
        "key_schema": "KeySchema",
        "warm_throughput": "WarmThroughput",
        "write_provisioned_throughput_settings": "WriteProvisionedThroughputSettings",
        "write_on_demand_throughput_settings": "WriteOnDemandThroughputSettings",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    projection: Optional[Projection] = None
    key_schema: Optional[list[KeySchema]] = None
    warm_throughput: Optional[WarmThroughput] = None
    write_provisioned_throughput_settings: Optional[WriteProvisionedThroughputSettings] = None
    write_on_demand_throughput_settings: Optional[WriteOnDemandThroughputSettings] = None


@dataclass
class GlobalTableWitness(PropertyType):
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
    }

    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeySchema(PropertyType):
    KEY_TYPE = "KeyType"
    ATTRIBUTE_NAME = "AttributeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_type": "KeyType",
        "attribute_name": "AttributeName",
    }

    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamSpecification(PropertyType):
    APPROXIMATE_CREATION_DATE_TIME_PRECISION = "ApproximateCreationDateTimePrecision"
    STREAM_ARN = "StreamArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "approximate_creation_date_time_precision": "ApproximateCreationDateTimePrecision",
        "stream_arn": "StreamArn",
    }

    approximate_creation_date_time_precision: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LocalSecondaryIndex(PropertyType):
    INDEX_NAME = "IndexName"
    PROJECTION = "Projection"
    KEY_SCHEMA = "KeySchema"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "projection": "Projection",
        "key_schema": "KeySchema",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    projection: Optional[Projection] = None
    key_schema: Optional[list[KeySchema]] = None


@dataclass
class PointInTimeRecoverySpecification(PropertyType):
    POINT_IN_TIME_RECOVERY_ENABLED = "PointInTimeRecoveryEnabled"
    RECOVERY_PERIOD_IN_DAYS = "RecoveryPeriodInDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "point_in_time_recovery_enabled": "PointInTimeRecoveryEnabled",
        "recovery_period_in_days": "RecoveryPeriodInDays",
    }

    point_in_time_recovery_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    recovery_period_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Projection(PropertyType):
    PROJECTION_TYPE = "ProjectionType"
    NON_KEY_ATTRIBUTES = "NonKeyAttributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "projection_type": "ProjectionType",
        "non_key_attributes": "NonKeyAttributes",
    }

    projection_type: Optional[Union[str, ProjectionType, Ref, GetAtt, Sub]] = None
    non_key_attributes: Optional[Union[list[str], Ref]] = None


@dataclass
class ReadOnDemandThroughputSettings(PropertyType):
    MAX_READ_REQUEST_UNITS = "MaxReadRequestUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_read_request_units": "MaxReadRequestUnits",
    }

    max_read_request_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ReadProvisionedThroughputSettings(PropertyType):
    READ_CAPACITY_UNITS = "ReadCapacityUnits"
    READ_CAPACITY_AUTO_SCALING_SETTINGS = "ReadCapacityAutoScalingSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_capacity_units": "ReadCapacityUnits",
        "read_capacity_auto_scaling_settings": "ReadCapacityAutoScalingSettings",
    }

    read_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    read_capacity_auto_scaling_settings: Optional[CapacityAutoScalingSettings] = None


@dataclass
class ReplicaGlobalSecondaryIndexSpecification(PropertyType):
    INDEX_NAME = "IndexName"
    CONTRIBUTOR_INSIGHTS_SPECIFICATION = "ContributorInsightsSpecification"
    READ_PROVISIONED_THROUGHPUT_SETTINGS = "ReadProvisionedThroughputSettings"
    READ_ON_DEMAND_THROUGHPUT_SETTINGS = "ReadOnDemandThroughputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "contributor_insights_specification": "ContributorInsightsSpecification",
        "read_provisioned_throughput_settings": "ReadProvisionedThroughputSettings",
        "read_on_demand_throughput_settings": "ReadOnDemandThroughputSettings",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    contributor_insights_specification: Optional[ContributorInsightsSpecification] = None
    read_provisioned_throughput_settings: Optional[ReadProvisionedThroughputSettings] = None
    read_on_demand_throughput_settings: Optional[ReadOnDemandThroughputSettings] = None


@dataclass
class ReplicaSSESpecification(PropertyType):
    KMS_MASTER_KEY_ID = "KMSMasterKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyId",
    }

    kms_master_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicaSpecification(PropertyType):
    SSE_SPECIFICATION = "SSESpecification"
    KINESIS_STREAM_SPECIFICATION = "KinesisStreamSpecification"
    CONTRIBUTOR_INSIGHTS_SPECIFICATION = "ContributorInsightsSpecification"
    POINT_IN_TIME_RECOVERY_SPECIFICATION = "PointInTimeRecoverySpecification"
    REPLICA_STREAM_SPECIFICATION = "ReplicaStreamSpecification"
    GLOBAL_SECONDARY_INDEXES = "GlobalSecondaryIndexes"
    REGION = "Region"
    RESOURCE_POLICY = "ResourcePolicy"
    READ_PROVISIONED_THROUGHPUT_SETTINGS = "ReadProvisionedThroughputSettings"
    TABLE_CLASS = "TableClass"
    DELETION_PROTECTION_ENABLED = "DeletionProtectionEnabled"
    TAGS = "Tags"
    READ_ON_DEMAND_THROUGHPUT_SETTINGS = "ReadOnDemandThroughputSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_specification": "SSESpecification",
        "kinesis_stream_specification": "KinesisStreamSpecification",
        "contributor_insights_specification": "ContributorInsightsSpecification",
        "point_in_time_recovery_specification": "PointInTimeRecoverySpecification",
        "replica_stream_specification": "ReplicaStreamSpecification",
        "global_secondary_indexes": "GlobalSecondaryIndexes",
        "region": "Region",
        "resource_policy": "ResourcePolicy",
        "read_provisioned_throughput_settings": "ReadProvisionedThroughputSettings",
        "table_class": "TableClass",
        "deletion_protection_enabled": "DeletionProtectionEnabled",
        "tags": "Tags",
        "read_on_demand_throughput_settings": "ReadOnDemandThroughputSettings",
    }

    sse_specification: Optional[ReplicaSSESpecification] = None
    kinesis_stream_specification: Optional[KinesisStreamSpecification] = None
    contributor_insights_specification: Optional[ContributorInsightsSpecification] = None
    point_in_time_recovery_specification: Optional[PointInTimeRecoverySpecification] = None
    replica_stream_specification: Optional[ReplicaStreamSpecification] = None
    global_secondary_indexes: Optional[list[ReplicaGlobalSecondaryIndexSpecification]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_policy: Optional[ResourcePolicy] = None
    read_provisioned_throughput_settings: Optional[ReadProvisionedThroughputSettings] = None
    table_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deletion_protection_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    read_on_demand_throughput_settings: Optional[ReadOnDemandThroughputSettings] = None


@dataclass
class ReplicaStreamSpecification(PropertyType):
    RESOURCE_POLICY = "ResourcePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_policy": "ResourcePolicy",
    }

    resource_policy: Optional[ResourcePolicy] = None


@dataclass
class ResourcePolicy(PropertyType):
    POLICY_DOCUMENT = "PolicyDocument"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_document": "PolicyDocument",
    }

    policy_document: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class SSESpecification(PropertyType):
    SSE_ENABLED = "SSEEnabled"
    SSE_TYPE = "SSEType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
    }

    sse_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sse_type: Optional[Union[str, SSEType, Ref, GetAtt, Sub]] = None


@dataclass
class StreamSpecification(PropertyType):
    STREAM_VIEW_TYPE = "StreamViewType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_view_type": "StreamViewType",
    }

    stream_view_type: Optional[Union[str, StreamViewType, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    SCALE_OUT_COOLDOWN = "ScaleOutCooldown"
    TARGET_VALUE = "TargetValue"
    DISABLE_SCALE_IN = "DisableScaleIn"
    SCALE_IN_COOLDOWN = "ScaleInCooldown"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_out_cooldown": "ScaleOutCooldown",
        "target_value": "TargetValue",
        "disable_scale_in": "DisableScaleIn",
        "scale_in_cooldown": "ScaleInCooldown",
    }

    scale_out_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    disable_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scale_in_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeToLiveSpecification(PropertyType):
    ENABLED = "Enabled"
    ATTRIBUTE_NAME = "AttributeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "attribute_name": "AttributeName",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WarmThroughput(PropertyType):
    READ_UNITS_PER_SECOND = "ReadUnitsPerSecond"
    WRITE_UNITS_PER_SECOND = "WriteUnitsPerSecond"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_units_per_second": "ReadUnitsPerSecond",
        "write_units_per_second": "WriteUnitsPerSecond",
    }

    read_units_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    write_units_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WriteOnDemandThroughputSettings(PropertyType):
    MAX_WRITE_REQUEST_UNITS = "MaxWriteRequestUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_write_request_units": "MaxWriteRequestUnits",
    }

    max_write_request_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WriteProvisionedThroughputSettings(PropertyType):
    WRITE_CAPACITY_AUTO_SCALING_SETTINGS = "WriteCapacityAutoScalingSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "write_capacity_auto_scaling_settings": "WriteCapacityAutoScalingSettings",
    }

    write_capacity_auto_scaling_settings: Optional[CapacityAutoScalingSettings] = None

