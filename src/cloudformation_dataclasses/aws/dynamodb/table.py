"""PropertyTypes for AWS::DynamoDB::Table."""

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
class Csv(PropertyType):
    DELIMITER = "Delimiter"
    HEADER_LIST = "HeaderList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "header_list": "HeaderList",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_list: Optional[Union[list[str], Ref]] = None


@dataclass
class GlobalSecondaryIndex(PropertyType):
    INDEX_NAME = "IndexName"
    ON_DEMAND_THROUGHPUT = "OnDemandThroughput"
    CONTRIBUTOR_INSIGHTS_SPECIFICATION = "ContributorInsightsSpecification"
    PROJECTION = "Projection"
    PROVISIONED_THROUGHPUT = "ProvisionedThroughput"
    KEY_SCHEMA = "KeySchema"
    WARM_THROUGHPUT = "WarmThroughput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "on_demand_throughput": "OnDemandThroughput",
        "contributor_insights_specification": "ContributorInsightsSpecification",
        "projection": "Projection",
        "provisioned_throughput": "ProvisionedThroughput",
        "key_schema": "KeySchema",
        "warm_throughput": "WarmThroughput",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    on_demand_throughput: Optional[OnDemandThroughput] = None
    contributor_insights_specification: Optional[ContributorInsightsSpecification] = None
    projection: Optional[Projection] = None
    provisioned_throughput: Optional[ProvisionedThroughput] = None
    key_schema: Optional[list[KeySchema]] = None
    warm_throughput: Optional[WarmThroughput] = None


@dataclass
class ImportSourceSpecification(PropertyType):
    S3_BUCKET_SOURCE = "S3BucketSource"
    INPUT_FORMAT = "InputFormat"
    INPUT_FORMAT_OPTIONS = "InputFormatOptions"
    INPUT_COMPRESSION_TYPE = "InputCompressionType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_source": "S3BucketSource",
        "input_format": "InputFormat",
        "input_format_options": "InputFormatOptions",
        "input_compression_type": "InputCompressionType",
    }

    s3_bucket_source: Optional[S3BucketSource] = None
    input_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_format_options: Optional[InputFormatOptions] = None
    input_compression_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputFormatOptions(PropertyType):
    CSV = "Csv"

    _property_mappings: ClassVar[dict[str, str]] = {
        "csv": "Csv",
    }

    csv: Optional[Csv] = None


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
class OnDemandThroughput(PropertyType):
    MAX_READ_REQUEST_UNITS = "MaxReadRequestUnits"
    MAX_WRITE_REQUEST_UNITS = "MaxWriteRequestUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_read_request_units": "MaxReadRequestUnits",
        "max_write_request_units": "MaxWriteRequestUnits",
    }

    max_read_request_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_write_request_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
    NON_KEY_ATTRIBUTES = "NonKeyAttributes"
    PROJECTION_TYPE = "ProjectionType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "non_key_attributes": "NonKeyAttributes",
        "projection_type": "ProjectionType",
    }

    non_key_attributes: Optional[Union[list[str], Ref]] = None
    projection_type: Optional[Union[str, ProjectionType, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisionedThroughput(PropertyType):
    WRITE_CAPACITY_UNITS = "WriteCapacityUnits"
    READ_CAPACITY_UNITS = "ReadCapacityUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "write_capacity_units": "WriteCapacityUnits",
        "read_capacity_units": "ReadCapacityUnits",
    }

    write_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    read_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ResourcePolicy(PropertyType):
    POLICY_DOCUMENT = "PolicyDocument"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_document": "PolicyDocument",
    }

    policy_document: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class S3BucketSource(PropertyType):
    S3_BUCKET = "S3Bucket"
    S3_KEY_PREFIX = "S3KeyPrefix"
    S3_BUCKET_OWNER = "S3BucketOwner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "s3_key_prefix": "S3KeyPrefix",
        "s3_bucket_owner": "S3BucketOwner",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SSESpecification(PropertyType):
    SSE_ENABLED = "SSEEnabled"
    SSE_TYPE = "SSEType"
    KMS_MASTER_KEY_ID = "KMSMasterKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
        "kms_master_key_id": "KMSMasterKeyId",
    }

    sse_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sse_type: Optional[Union[str, SSEType, Ref, GetAtt, Sub]] = None
    kms_master_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamSpecification(PropertyType):
    STREAM_VIEW_TYPE = "StreamViewType"
    RESOURCE_POLICY = "ResourcePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_view_type": "StreamViewType",
        "resource_policy": "ResourcePolicy",
    }

    stream_view_type: Optional[Union[str, StreamViewType, Ref, GetAtt, Sub]] = None
    resource_policy: Optional[ResourcePolicy] = None


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

