"""PropertyTypes for AWS::S3::StorageLens."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AnalyticsS3ExportFileFormat:
    """AnalyticsS3ExportFileFormat enum values."""

    CSV = "CSV"


class ArchiveStatus:
    """ArchiveStatus enum values."""

    ARCHIVE_ACCESS = "ARCHIVE_ACCESS"
    DEEP_ARCHIVE_ACCESS = "DEEP_ARCHIVE_ACCESS"


class BucketAbacStatus:
    """BucketAbacStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class BucketAccelerateStatus:
    """BucketAccelerateStatus enum values."""

    ENABLED = "Enabled"
    SUSPENDED = "Suspended"


class BucketCannedACL:
    """BucketCannedACL enum values."""

    PRIVATE = "private"
    PUBLIC_READ = "public-read"
    PUBLIC_READ_WRITE = "public-read-write"
    AUTHENTICATED_READ = "authenticated-read"


class BucketLocationConstraint:
    """BucketLocationConstraint enum values."""

    AF_SOUTH_1 = "af-south-1"
    AP_EAST_1 = "ap-east-1"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTH_2 = "ap-south-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_SOUTHEAST_4 = "ap-southeast-4"
    AP_SOUTHEAST_5 = "ap-southeast-5"
    CA_CENTRAL_1 = "ca-central-1"
    CN_NORTH_1 = "cn-north-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    EU = "EU"
    EU_CENTRAL_1 = "eu-central-1"
    EU_CENTRAL_2 = "eu-central-2"
    EU_NORTH_1 = "eu-north-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_SOUTH_2 = "eu-south-2"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    IL_CENTRAL_1 = "il-central-1"
    ME_CENTRAL_1 = "me-central-1"
    ME_SOUTH_1 = "me-south-1"
    SA_EAST_1 = "sa-east-1"
    US_EAST_2 = "us-east-2"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_GOV_WEST_1 = "us-gov-west-1"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"


class BucketLogsPermission:
    """BucketLogsPermission enum values."""

    FULL_CONTROL = "FULL_CONTROL"
    READ = "READ"
    WRITE = "WRITE"


class BucketType:
    """BucketType enum values."""

    DIRECTORY = "Directory"


class BucketVersioningStatus:
    """BucketVersioningStatus enum values."""

    ENABLED = "Enabled"
    SUSPENDED = "Suspended"


class ChecksumAlgorithm:
    """ChecksumAlgorithm enum values."""

    CRC32 = "CRC32"
    CRC32C = "CRC32C"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    CRC64NVME = "CRC64NVME"


class ChecksumMode:
    """ChecksumMode enum values."""

    ENABLED = "ENABLED"


class ChecksumType:
    """ChecksumType enum values."""

    COMPOSITE = "COMPOSITE"
    FULL_OBJECT = "FULL_OBJECT"


class CompressionType:
    """CompressionType enum values."""

    NONE = "NONE"
    GZIP = "GZIP"
    BZIP2 = "BZIP2"


class DataRedundancy:
    """DataRedundancy enum values."""

    SINGLEAVAILABILITYZONE = "SingleAvailabilityZone"
    SINGLELOCALZONE = "SingleLocalZone"


class DeleteMarkerReplicationStatus:
    """DeleteMarkerReplicationStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EncodingType:
    """EncodingType enum values."""

    URL = "url"


class EncryptionType:
    """EncryptionType enum values."""

    NONE = "NONE"
    SSE_C = "SSE-C"


class Event:
    """Event enum values."""

    S3_REDUCEDREDUNDANCYLOSTOBJECT = "s3:ReducedRedundancyLostObject"
    S3_OBJECTCREATED_STAR = "s3:ObjectCreated:*"
    S3_OBJECTCREATED_PUT = "s3:ObjectCreated:Put"
    S3_OBJECTCREATED_POST = "s3:ObjectCreated:Post"
    S3_OBJECTCREATED_COPY = "s3:ObjectCreated:Copy"
    S3_OBJECTCREATED_COMPLETEMULTIPARTUPLOAD = "s3:ObjectCreated:CompleteMultipartUpload"
    S3_OBJECTREMOVED_STAR = "s3:ObjectRemoved:*"
    S3_OBJECTREMOVED_DELETE = "s3:ObjectRemoved:Delete"
    S3_OBJECTREMOVED_DELETEMARKERCREATED = "s3:ObjectRemoved:DeleteMarkerCreated"
    S3_OBJECTRESTORE_STAR = "s3:ObjectRestore:*"
    S3_OBJECTRESTORE_POST = "s3:ObjectRestore:Post"
    S3_OBJECTRESTORE_COMPLETED = "s3:ObjectRestore:Completed"
    S3_REPLICATION_STAR = "s3:Replication:*"
    S3_REPLICATION_OPERATIONFAILEDREPLICATION = "s3:Replication:OperationFailedReplication"
    S3_REPLICATION_OPERATIONNOTTRACKED = "s3:Replication:OperationNotTracked"
    S3_REPLICATION_OPERATIONMISSEDTHRESHOLD = "s3:Replication:OperationMissedThreshold"
    S3_REPLICATION_OPERATIONREPLICATEDAFTERTHRESHOLD = "s3:Replication:OperationReplicatedAfterThreshold"
    S3_OBJECTRESTORE_DELETE = "s3:ObjectRestore:Delete"
    S3_LIFECYCLETRANSITION = "s3:LifecycleTransition"
    S3_INTELLIGENTTIERING = "s3:IntelligentTiering"
    S3_OBJECTACL_PUT = "s3:ObjectAcl:Put"
    S3_LIFECYCLEEXPIRATION_STAR = "s3:LifecycleExpiration:*"
    S3_LIFECYCLEEXPIRATION_DELETE = "s3:LifecycleExpiration:Delete"
    S3_LIFECYCLEEXPIRATION_DELETEMARKERCREATED = "s3:LifecycleExpiration:DeleteMarkerCreated"
    S3_OBJECTTAGGING_STAR = "s3:ObjectTagging:*"
    S3_OBJECTTAGGING_PUT = "s3:ObjectTagging:Put"
    S3_OBJECTTAGGING_DELETE = "s3:ObjectTagging:Delete"


class ExistingObjectReplicationStatus:
    """ExistingObjectReplicationStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpirationState:
    """ExpirationState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ExpirationStatus:
    """ExpirationStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpressionType:
    """ExpressionType enum values."""

    SQL = "SQL"


class FileHeaderInfo:
    """FileHeaderInfo enum values."""

    USE = "USE"
    IGNORE = "IGNORE"
    NONE = "NONE"


class FilterRuleName:
    """FilterRuleName enum values."""

    PREFIX = "prefix"
    SUFFIX = "suffix"


class IntelligentTieringAccessTier:
    """IntelligentTieringAccessTier enum values."""

    ARCHIVE_ACCESS = "ARCHIVE_ACCESS"
    DEEP_ARCHIVE_ACCESS = "DEEP_ARCHIVE_ACCESS"


class IntelligentTieringStatus:
    """IntelligentTieringStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class InventoryConfigurationState:
    """InventoryConfigurationState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InventoryFormat:
    """InventoryFormat enum values."""

    CSV = "CSV"
    ORC = "ORC"
    PARQUET = "Parquet"


class InventoryFrequency:
    """InventoryFrequency enum values."""

    DAILY = "Daily"
    WEEKLY = "Weekly"


class InventoryIncludedObjectVersions:
    """InventoryIncludedObjectVersions enum values."""

    ALL = "All"
    CURRENT = "Current"


class InventoryOptionalField:
    """InventoryOptionalField enum values."""

    SIZE = "Size"
    LASTMODIFIEDDATE = "LastModifiedDate"
    STORAGECLASS = "StorageClass"
    ETAG = "ETag"
    ISMULTIPARTUPLOADED = "IsMultipartUploaded"
    REPLICATIONSTATUS = "ReplicationStatus"
    ENCRYPTIONSTATUS = "EncryptionStatus"
    OBJECTLOCKRETAINUNTILDATE = "ObjectLockRetainUntilDate"
    OBJECTLOCKMODE = "ObjectLockMode"
    OBJECTLOCKLEGALHOLDSTATUS = "ObjectLockLegalHoldStatus"
    INTELLIGENTTIERINGACCESSTIER = "IntelligentTieringAccessTier"
    BUCKETKEYSTATUS = "BucketKeyStatus"
    CHECKSUMALGORITHM = "ChecksumAlgorithm"
    OBJECTACCESSCONTROLLIST = "ObjectAccessControlList"
    OBJECTOWNER = "ObjectOwner"
    LIFECYCLEEXPIRATIONDATE = "LifecycleExpirationDate"


class JSONType:
    """JSONType enum values."""

    DOCUMENT = "DOCUMENT"
    LINES = "LINES"


class LocationType:
    """LocationType enum values."""

    AVAILABILITYZONE = "AvailabilityZone"
    LOCALZONE = "LocalZone"


class MFADelete:
    """MFADelete enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MFADeleteStatus:
    """MFADeleteStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MetadataDirective:
    """MetadataDirective enum values."""

    COPY = "COPY"
    REPLACE = "REPLACE"


class MetricsStatus:
    """MetricsStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ObjectAttributes:
    """ObjectAttributes enum values."""

    ETAG = "ETag"
    CHECKSUM = "Checksum"
    OBJECTPARTS = "ObjectParts"
    STORAGECLASS = "StorageClass"
    OBJECTSIZE = "ObjectSize"


class ObjectCannedACL:
    """ObjectCannedACL enum values."""

    PRIVATE = "private"
    PUBLIC_READ = "public-read"
    PUBLIC_READ_WRITE = "public-read-write"
    AUTHENTICATED_READ = "authenticated-read"
    AWS_EXEC_READ = "aws-exec-read"
    BUCKET_OWNER_READ = "bucket-owner-read"
    BUCKET_OWNER_FULL_CONTROL = "bucket-owner-full-control"


class ObjectLockEnabled:
    """ObjectLockEnabled enum values."""

    ENABLED = "Enabled"


class ObjectLockLegalHoldStatus:
    """ObjectLockLegalHoldStatus enum values."""

    ON = "ON"
    OFF = "OFF"


class ObjectLockMode:
    """ObjectLockMode enum values."""

    GOVERNANCE = "GOVERNANCE"
    COMPLIANCE = "COMPLIANCE"


class ObjectLockRetentionMode:
    """ObjectLockRetentionMode enum values."""

    GOVERNANCE = "GOVERNANCE"
    COMPLIANCE = "COMPLIANCE"


class ObjectOwnership:
    """ObjectOwnership enum values."""

    BUCKETOWNERPREFERRED = "BucketOwnerPreferred"
    OBJECTWRITER = "ObjectWriter"
    BUCKETOWNERENFORCED = "BucketOwnerEnforced"


class ObjectStorageClass:
    """ObjectStorageClass enum values."""

    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    GLACIER = "GLACIER"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    OUTPOSTS = "OUTPOSTS"
    GLACIER_IR = "GLACIER_IR"
    SNOW = "SNOW"
    EXPRESS_ONEZONE = "EXPRESS_ONEZONE"
    FSX_OPENZFS = "FSX_OPENZFS"
    FSX_ONTAP = "FSX_ONTAP"


class ObjectVersionStorageClass:
    """ObjectVersionStorageClass enum values."""

    STANDARD = "STANDARD"


class OptionalObjectAttributes:
    """OptionalObjectAttributes enum values."""

    RESTORESTATUS = "RestoreStatus"


class OwnerOverride:
    """OwnerOverride enum values."""

    DESTINATION = "Destination"


class PartitionDateSource:
    """PartitionDateSource enum values."""

    EVENTTIME = "EventTime"
    DELIVERYTIME = "DeliveryTime"


class Payer:
    """Payer enum values."""

    REQUESTER = "Requester"
    BUCKETOWNER = "BucketOwner"


class Permission:
    """Permission enum values."""

    FULL_CONTROL = "FULL_CONTROL"
    WRITE = "WRITE"
    WRITE_ACP = "WRITE_ACP"
    READ = "READ"
    READ_ACP = "READ_ACP"


class Protocol:
    """Protocol enum values."""

    HTTP = "http"
    HTTPS = "https"


class QuoteFields:
    """QuoteFields enum values."""

    ALWAYS = "ALWAYS"
    ASNEEDED = "ASNEEDED"


class ReplicaModificationsStatus:
    """ReplicaModificationsStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ReplicationRuleStatus:
    """ReplicationRuleStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ReplicationStatus:
    """ReplicationStatus enum values."""

    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    FAILED = "FAILED"
    REPLICA = "REPLICA"
    COMPLETED = "COMPLETED"


class ReplicationTimeStatus:
    """ReplicationTimeStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RequestCharged:
    """RequestCharged enum values."""

    REQUESTER = "requester"


class RequestPayer:
    """RequestPayer enum values."""

    REQUESTER = "requester"


class RestoreRequestType:
    """RestoreRequestType enum values."""

    SELECT = "SELECT"


class S3TablesBucketType:
    """S3TablesBucketType enum values."""

    AWS = "aws"
    CUSTOMER = "customer"


class ServerSideEncryption:
    """ServerSideEncryption enum values."""

    AES256 = "AES256"
    AWS_FSX = "aws:fsx"
    AWS_KMS = "aws:kms"
    AWS_KMS_DSSE = "aws:kms:dsse"


class SessionMode:
    """SessionMode enum values."""

    READONLY = "ReadOnly"
    READWRITE = "ReadWrite"


class SseKmsEncryptedObjectsStatus:
    """SseKmsEncryptedObjectsStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class StorageClass:
    """StorageClass enum values."""

    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    GLACIER = "GLACIER"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    OUTPOSTS = "OUTPOSTS"
    GLACIER_IR = "GLACIER_IR"
    SNOW = "SNOW"
    EXPRESS_ONEZONE = "EXPRESS_ONEZONE"
    FSX_OPENZFS = "FSX_OPENZFS"
    FSX_ONTAP = "FSX_ONTAP"


class StorageClassAnalysisSchemaVersion:
    """StorageClassAnalysisSchemaVersion enum values."""

    V_1 = "V_1"


class TableSseAlgorithm:
    """TableSseAlgorithm enum values."""

    AWS_KMS = "aws:kms"
    AES256 = "AES256"


class TaggingDirective:
    """TaggingDirective enum values."""

    COPY = "COPY"
    REPLACE = "REPLACE"


class Tier:
    """Tier enum values."""

    STANDARD = "Standard"
    BULK = "Bulk"
    EXPEDITED = "Expedited"


class TransitionDefaultMinimumObjectSize:
    """TransitionDefaultMinimumObjectSize enum values."""

    VARIES_BY_STORAGE_CLASS = "varies_by_storage_class"
    ALL_STORAGE_CLASSES_128K = "all_storage_classes_128K"


class TransitionStorageClass:
    """TransitionStorageClass enum values."""

    GLACIER = "GLACIER"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    GLACIER_IR = "GLACIER_IR"


class Type:
    """Type enum values."""

    CANONICALUSER = "CanonicalUser"
    AMAZONCUSTOMERBYEMAIL = "AmazonCustomerByEmail"
    GROUP = "Group"


@dataclass
class AccountLevel(PropertyType):
    ADVANCED_DATA_PROTECTION_METRICS = "AdvancedDataProtectionMetrics"
    STORAGE_LENS_GROUP_LEVEL = "StorageLensGroupLevel"
    ACTIVITY_METRICS = "ActivityMetrics"
    ADVANCED_PERFORMANCE_METRICS = "AdvancedPerformanceMetrics"
    BUCKET_LEVEL = "BucketLevel"
    ADVANCED_COST_OPTIMIZATION_METRICS = "AdvancedCostOptimizationMetrics"
    DETAILED_STATUS_CODES_METRICS = "DetailedStatusCodesMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_data_protection_metrics": "AdvancedDataProtectionMetrics",
        "storage_lens_group_level": "StorageLensGroupLevel",
        "activity_metrics": "ActivityMetrics",
        "advanced_performance_metrics": "AdvancedPerformanceMetrics",
        "bucket_level": "BucketLevel",
        "advanced_cost_optimization_metrics": "AdvancedCostOptimizationMetrics",
        "detailed_status_codes_metrics": "DetailedStatusCodesMetrics",
    }

    advanced_data_protection_metrics: Optional[AdvancedDataProtectionMetrics] = None
    storage_lens_group_level: Optional[StorageLensGroupLevel] = None
    activity_metrics: Optional[ActivityMetrics] = None
    advanced_performance_metrics: Optional[AdvancedPerformanceMetrics] = None
    bucket_level: Optional[BucketLevel] = None
    advanced_cost_optimization_metrics: Optional[AdvancedCostOptimizationMetrics] = None
    detailed_status_codes_metrics: Optional[DetailedStatusCodesMetrics] = None


@dataclass
class ActivityMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedCostOptimizationMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedDataProtectionMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedPerformanceMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AwsOrg(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BucketLevel(PropertyType):
    ADVANCED_DATA_PROTECTION_METRICS = "AdvancedDataProtectionMetrics"
    PREFIX_LEVEL = "PrefixLevel"
    ACTIVITY_METRICS = "ActivityMetrics"
    ADVANCED_PERFORMANCE_METRICS = "AdvancedPerformanceMetrics"
    ADVANCED_COST_OPTIMIZATION_METRICS = "AdvancedCostOptimizationMetrics"
    DETAILED_STATUS_CODES_METRICS = "DetailedStatusCodesMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_data_protection_metrics": "AdvancedDataProtectionMetrics",
        "prefix_level": "PrefixLevel",
        "activity_metrics": "ActivityMetrics",
        "advanced_performance_metrics": "AdvancedPerformanceMetrics",
        "advanced_cost_optimization_metrics": "AdvancedCostOptimizationMetrics",
        "detailed_status_codes_metrics": "DetailedStatusCodesMetrics",
    }

    advanced_data_protection_metrics: Optional[AdvancedDataProtectionMetrics] = None
    prefix_level: Optional[PrefixLevel] = None
    activity_metrics: Optional[ActivityMetrics] = None
    advanced_performance_metrics: Optional[AdvancedPerformanceMetrics] = None
    advanced_cost_optimization_metrics: Optional[AdvancedCostOptimizationMetrics] = None
    detailed_status_codes_metrics: Optional[DetailedStatusCodesMetrics] = None


@dataclass
class BucketsAndRegions(PropertyType):
    REGIONS = "Regions"
    BUCKETS = "Buckets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regions": "Regions",
        "buckets": "Buckets",
    }

    regions: Optional[Union[list[str], Ref]] = None
    buckets: Optional[Union[list[str], Ref]] = None


@dataclass
class CloudWatchMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataExport(PropertyType):
    STORAGE_LENS_TABLE_DESTINATION = "StorageLensTableDestination"
    S3_BUCKET_DESTINATION = "S3BucketDestination"
    CLOUD_WATCH_METRICS = "CloudWatchMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_lens_table_destination": "StorageLensTableDestination",
        "s3_bucket_destination": "S3BucketDestination",
        "cloud_watch_metrics": "CloudWatchMetrics",
    }

    storage_lens_table_destination: Optional[StorageLensTableDestination] = None
    s3_bucket_destination: Optional[S3BucketDestination] = None
    cloud_watch_metrics: Optional[CloudWatchMetrics] = None


@dataclass
class DetailedStatusCodesMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Encryption(PropertyType):
    SSEKMS = "SSEKMS"
    SSES3 = "SSES3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssekms": "SSEKMS",
        "sses3": "SSES3",
    }

    ssekms: Optional[SSEKMS] = None
    sses3: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class PrefixLevel(PropertyType):
    STORAGE_METRICS = "StorageMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_metrics": "StorageMetrics",
    }

    storage_metrics: Optional[PrefixLevelStorageMetrics] = None


@dataclass
class PrefixLevelStorageMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"
    SELECTION_CRITERIA = "SelectionCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
        "selection_criteria": "SelectionCriteria",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    selection_criteria: Optional[SelectionCriteria] = None


@dataclass
class S3BucketDestination(PropertyType):
    OUTPUT_SCHEMA_VERSION = "OutputSchemaVersion"
    FORMAT = "Format"
    ACCOUNT_ID = "AccountId"
    PREFIX = "Prefix"
    ENCRYPTION = "Encryption"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_schema_version": "OutputSchemaVersion",
        "format": "Format",
        "account_id": "AccountId",
        "prefix": "Prefix",
        "encryption": "Encryption",
        "arn": "Arn",
    }

    output_schema_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption: Optional[Encryption] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SSEKMS(PropertyType):
    KEY_ID = "KeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_id": "KeyId",
    }

    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelectionCriteria(PropertyType):
    DELIMITER = "Delimiter"
    MAX_DEPTH = "MaxDepth"
    MIN_STORAGE_BYTES_PERCENTAGE = "MinStorageBytesPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "max_depth": "MaxDepth",
        "min_storage_bytes_percentage": "MinStorageBytesPercentage",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_depth: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_storage_bytes_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StorageLensConfiguration(PropertyType):
    ACCOUNT_LEVEL = "AccountLevel"
    EXCLUDE = "Exclude"
    IS_ENABLED = "IsEnabled"
    INCLUDE = "Include"
    PREFIX_DELIMITER = "PrefixDelimiter"
    AWS_ORG = "AwsOrg"
    ID = "Id"
    STORAGE_LENS_ARN = "StorageLensArn"
    DATA_EXPORT = "DataExport"
    EXPANDED_PREFIXES_DATA_EXPORT = "ExpandedPrefixesDataExport"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_level": "AccountLevel",
        "exclude": "Exclude",
        "is_enabled": "IsEnabled",
        "include": "Include",
        "prefix_delimiter": "PrefixDelimiter",
        "aws_org": "AwsOrg",
        "id": "Id",
        "storage_lens_arn": "StorageLensArn",
        "data_export": "DataExport",
        "expanded_prefixes_data_export": "ExpandedPrefixesDataExport",
    }

    account_level: Optional[AccountLevel] = None
    exclude: Optional[BucketsAndRegions] = None
    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include: Optional[BucketsAndRegions] = None
    prefix_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_org: Optional[AwsOrg] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_lens_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_export: Optional[DataExport] = None
    expanded_prefixes_data_export: Optional[StorageLensExpandedPrefixesDataExport] = None


@dataclass
class StorageLensExpandedPrefixesDataExport(PropertyType):
    STORAGE_LENS_TABLE_DESTINATION = "StorageLensTableDestination"
    S3_BUCKET_DESTINATION = "S3BucketDestination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_lens_table_destination": "StorageLensTableDestination",
        "s3_bucket_destination": "S3BucketDestination",
    }

    storage_lens_table_destination: Optional[StorageLensTableDestination] = None
    s3_bucket_destination: Optional[S3BucketDestination] = None


@dataclass
class StorageLensGroupLevel(PropertyType):
    STORAGE_LENS_GROUP_SELECTION_CRITERIA = "StorageLensGroupSelectionCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_lens_group_selection_criteria": "StorageLensGroupSelectionCriteria",
    }

    storage_lens_group_selection_criteria: Optional[StorageLensGroupSelectionCriteria] = None


@dataclass
class StorageLensGroupSelectionCriteria(PropertyType):
    EXCLUDE = "Exclude"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class StorageLensTableDestination(PropertyType):
    IS_ENABLED = "IsEnabled"
    ENCRYPTION = "Encryption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
        "encryption": "Encryption",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    encryption: Optional[Encryption] = None

