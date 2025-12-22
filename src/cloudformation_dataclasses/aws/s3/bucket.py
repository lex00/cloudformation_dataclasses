"""PropertyTypes for AWS::S3::Bucket."""

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
class AbortIncompleteMultipartUpload(PropertyType):
    DAYS_AFTER_INITIATION = "DaysAfterInitiation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "days_after_initiation": "DaysAfterInitiation",
    }

    days_after_initiation: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AccelerateConfiguration(PropertyType):
    ACCELERATION_STATUS = "AccelerationStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "acceleration_status": "AccelerationStatus",
    }

    acceleration_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AccessControlTranslation(PropertyType):
    OWNER = "Owner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
    }

    owner: Optional[Union[str, OwnerOverride, Ref, GetAtt, Sub]] = None


@dataclass
class AnalyticsConfiguration(PropertyType):
    STORAGE_CLASS_ANALYSIS = "StorageClassAnalysis"
    TAG_FILTERS = "TagFilters"
    ID = "Id"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class_analysis": "StorageClassAnalysis",
        "tag_filters": "TagFilters",
        "id": "Id",
        "prefix": "Prefix",
    }

    storage_class_analysis: Optional[StorageClassAnalysis] = None
    tag_filters: Optional[list[TagFilter]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BlockedEncryptionTypes(PropertyType):
    ENCRYPTION_TYPE = "EncryptionType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
    }

    encryption_type: Optional[Union[list[str], Ref]] = None


@dataclass
class BucketEncryption(PropertyType):
    SERVER_SIDE_ENCRYPTION_CONFIGURATION = "ServerSideEncryptionConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_side_encryption_configuration": "ServerSideEncryptionConfiguration",
    }

    server_side_encryption_configuration: Optional[list[ServerSideEncryptionRule]] = None


@dataclass
class CorsConfiguration(PropertyType):
    CORS_RULES = "CorsRules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cors_rules": "CorsRules",
    }

    cors_rules: Optional[list[CorsRule]] = None


@dataclass
class CorsRule(PropertyType):
    EXPOSED_HEADERS = "ExposedHeaders"
    ALLOWED_METHODS = "AllowedMethods"
    ALLOWED_ORIGINS = "AllowedOrigins"
    ALLOWED_HEADERS = "AllowedHeaders"
    MAX_AGE = "MaxAge"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exposed_headers": "ExposedHeaders",
        "allowed_methods": "AllowedMethods",
        "allowed_origins": "AllowedOrigins",
        "allowed_headers": "AllowedHeaders",
        "max_age": "MaxAge",
        "id": "Id",
    }

    exposed_headers: Optional[Union[list[str], Ref]] = None
    allowed_methods: Optional[Union[list[str], Ref]] = None
    allowed_origins: Optional[Union[list[str], Ref]] = None
    allowed_headers: Optional[Union[list[str], Ref]] = None
    max_age: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataExport(PropertyType):
    DESTINATION = "Destination"
    OUTPUT_SCHEMA_VERSION = "OutputSchemaVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "output_schema_version": "OutputSchemaVersion",
    }

    destination: Optional[Destination] = None
    output_schema_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultRetention(PropertyType):
    YEARS = "Years"
    DAYS = "Days"
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "years": "Years",
        "days": "Days",
        "mode": "Mode",
    }

    years: Optional[Union[int, Ref, GetAtt, Sub]] = None
    days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, ObjectLockRetentionMode, Ref, GetAtt, Sub]] = None


@dataclass
class DeleteMarkerReplication(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, DeleteMarkerReplicationStatus, Ref, GetAtt, Sub]] = None


@dataclass
class Destination(PropertyType):
    BUCKET_ARN = "BucketArn"
    FORMAT = "Format"
    BUCKET_ACCOUNT_ID = "BucketAccountId"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "format": "Format",
        "bucket_account_id": "BucketAccountId",
        "prefix": "Prefix",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    REPLICA_KMS_KEY_ID = "ReplicaKmsKeyID"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_kms_key_id": "ReplicaKmsKeyID",
    }

    replica_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeConfiguration(PropertyType):
    EVENT_BRIDGE_ENABLED = "EventBridgeEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bridge_enabled": "EventBridgeEnabled",
    }

    event_bridge_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FilterRule(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, FilterRuleName, Ref, GetAtt, Sub]] = None


@dataclass
class IntelligentTieringConfiguration(PropertyType):
    STATUS = "Status"
    TIERINGS = "Tierings"
    TAG_FILTERS = "TagFilters"
    ID = "Id"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "tierings": "Tierings",
        "tag_filters": "TagFilters",
        "id": "Id",
        "prefix": "Prefix",
    }

    status: Optional[Union[str, IntelligentTieringStatus, Ref, GetAtt, Sub]] = None
    tierings: Optional[list[Tiering]] = None
    tag_filters: Optional[list[TagFilter]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InventoryConfiguration(PropertyType):
    DESTINATION = "Destination"
    OPTIONAL_FIELDS = "OptionalFields"
    INCLUDED_OBJECT_VERSIONS = "IncludedObjectVersions"
    ENABLED = "Enabled"
    ID = "Id"
    PREFIX = "Prefix"
    SCHEDULE_FREQUENCY = "ScheduleFrequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "optional_fields": "OptionalFields",
        "included_object_versions": "IncludedObjectVersions",
        "enabled": "Enabled",
        "id": "Id",
        "prefix": "Prefix",
        "schedule_frequency": "ScheduleFrequency",
    }

    destination: Optional[Destination] = None
    optional_fields: Optional[Union[list[str], Ref]] = None
    included_object_versions: Optional[Union[str, InventoryIncludedObjectVersions, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InventoryTableConfiguration(PropertyType):
    TABLE_NAME = "TableName"
    CONFIGURATION_STATE = "ConfigurationState"
    TABLE_ARN = "TableArn"
    ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "configuration_state": "ConfigurationState",
        "table_arn": "TableArn",
        "encryption_configuration": "EncryptionConfiguration",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_state: Optional[Union[str, InventoryConfigurationState, Ref, GetAtt, Sub]] = None
    table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[MetadataTableEncryptionConfiguration] = None


@dataclass
class JournalTableConfiguration(PropertyType):
    TABLE_NAME = "TableName"
    TABLE_ARN = "TableArn"
    ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    RECORD_EXPIRATION = "RecordExpiration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "table_arn": "TableArn",
        "encryption_configuration": "EncryptionConfiguration",
        "record_expiration": "RecordExpiration",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[MetadataTableEncryptionConfiguration] = None
    record_expiration: Optional[RecordExpiration] = None


@dataclass
class LambdaConfiguration(PropertyType):
    FUNCTION = "Function"
    FILTER = "Filter"
    EVENT = "Event"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "filter": "Filter",
        "event": "Event",
    }

    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter: Optional[NotificationFilter] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    TRANSITION_DEFAULT_MINIMUM_OBJECT_SIZE = "TransitionDefaultMinimumObjectSize"
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_default_minimum_object_size": "TransitionDefaultMinimumObjectSize",
        "rules": "Rules",
    }

    transition_default_minimum_object_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[Rule]] = None


@dataclass
class LoggingConfiguration(PropertyType):
    TARGET_OBJECT_KEY_FORMAT = "TargetObjectKeyFormat"
    LOG_FILE_PREFIX = "LogFilePrefix"
    DESTINATION_BUCKET_NAME = "DestinationBucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_object_key_format": "TargetObjectKeyFormat",
        "log_file_prefix": "LogFilePrefix",
        "destination_bucket_name": "DestinationBucketName",
    }

    target_object_key_format: Optional[TargetObjectKeyFormat] = None
    log_file_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataConfiguration(PropertyType):
    DESTINATION = "Destination"
    JOURNAL_TABLE_CONFIGURATION = "JournalTableConfiguration"
    INVENTORY_TABLE_CONFIGURATION = "InventoryTableConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "journal_table_configuration": "JournalTableConfiguration",
        "inventory_table_configuration": "InventoryTableConfiguration",
    }

    destination: Optional[MetadataDestination] = None
    journal_table_configuration: Optional[JournalTableConfiguration] = None
    inventory_table_configuration: Optional[InventoryTableConfiguration] = None


@dataclass
class MetadataDestination(PropertyType):
    TABLE_BUCKET_ARN = "TableBucketArn"
    TABLE_BUCKET_TYPE = "TableBucketType"
    TABLE_NAMESPACE = "TableNamespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_bucket_arn": "TableBucketArn",
        "table_bucket_type": "TableBucketType",
        "table_namespace": "TableNamespace",
    }

    table_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_bucket_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataTableConfiguration(PropertyType):
    S3_TABLES_DESTINATION = "S3TablesDestination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_tables_destination": "S3TablesDestination",
    }

    s3_tables_destination: Optional[S3TablesDestination] = None


@dataclass
class MetadataTableEncryptionConfiguration(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    SSE_ALGORITHM = "SseAlgorithm"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "sse_algorithm": "SseAlgorithm",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_algorithm: Optional[Union[str, TableSseAlgorithm, Ref, GetAtt, Sub]] = None


@dataclass
class Metrics(PropertyType):
    STATUS = "Status"
    EVENT_THRESHOLD = "EventThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "event_threshold": "EventThreshold",
    }

    status: Optional[Union[str, MetricsStatus, Ref, GetAtt, Sub]] = None
    event_threshold: Optional[ReplicationTimeValue] = None


@dataclass
class MetricsConfiguration(PropertyType):
    ACCESS_POINT_ARN = "AccessPointArn"
    TAG_FILTERS = "TagFilters"
    ID = "Id"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_point_arn": "AccessPointArn",
        "tag_filters": "TagFilters",
        "id": "Id",
        "prefix": "Prefix",
    }

    access_point_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_filters: Optional[list[TagFilter]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NoncurrentVersionExpiration(PropertyType):
    NONCURRENT_DAYS = "NoncurrentDays"
    NEWER_NONCURRENT_VERSIONS = "NewerNoncurrentVersions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "noncurrent_days": "NoncurrentDays",
        "newer_noncurrent_versions": "NewerNoncurrentVersions",
    }

    noncurrent_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    newer_noncurrent_versions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NoncurrentVersionTransition(PropertyType):
    STORAGE_CLASS = "StorageClass"
    TRANSITION_IN_DAYS = "TransitionInDays"
    NEWER_NONCURRENT_VERSIONS = "NewerNoncurrentVersions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
        "transition_in_days": "TransitionInDays",
        "newer_noncurrent_versions": "NewerNoncurrentVersions",
    }

    storage_class: Optional[Union[str, TransitionStorageClass, Ref, GetAtt, Sub]] = None
    transition_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    newer_noncurrent_versions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfiguration(PropertyType):
    TOPIC_CONFIGURATIONS = "TopicConfigurations"
    QUEUE_CONFIGURATIONS = "QueueConfigurations"
    LAMBDA_CONFIGURATIONS = "LambdaConfigurations"
    EVENT_BRIDGE_CONFIGURATION = "EventBridgeConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_configurations": "TopicConfigurations",
        "queue_configurations": "QueueConfigurations",
        "lambda_configurations": "LambdaConfigurations",
        "event_bridge_configuration": "EventBridgeConfiguration",
    }

    topic_configurations: Optional[list[TopicConfiguration]] = None
    queue_configurations: Optional[list[QueueConfiguration]] = None
    lambda_configurations: Optional[list[LambdaConfiguration]] = None
    event_bridge_configuration: Optional[EventBridgeConfiguration] = None


@dataclass
class NotificationFilter(PropertyType):
    S3_KEY = "S3Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_key": "S3Key",
    }

    s3_key: Optional[S3KeyFilter] = None


@dataclass
class ObjectLockConfiguration(PropertyType):
    OBJECT_LOCK_ENABLED = "ObjectLockEnabled"
    RULE = "Rule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_lock_enabled": "ObjectLockEnabled",
        "rule": "Rule",
    }

    object_lock_enabled: Optional[Union[str, ObjectLockEnabled, Ref, GetAtt, Sub]] = None
    rule: Optional[ObjectLockRule] = None


@dataclass
class ObjectLockRule(PropertyType):
    DEFAULT_RETENTION = "DefaultRetention"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_retention": "DefaultRetention",
    }

    default_retention: Optional[DefaultRetention] = None


@dataclass
class OwnershipControls(PropertyType):
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[OwnershipControlsRule]] = None


@dataclass
class OwnershipControlsRule(PropertyType):
    OBJECT_OWNERSHIP = "ObjectOwnership"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_ownership": "ObjectOwnership",
    }

    object_ownership: Optional[Union[str, ObjectOwnership, Ref, GetAtt, Sub]] = None


@dataclass
class PartitionedPrefix(PropertyType):
    PARTITION_DATE_SOURCE = "PartitionDateSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partition_date_source": "PartitionDateSource",
    }

    partition_date_source: Optional[Union[str, PartitionDateSource, Ref, GetAtt, Sub]] = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    RESTRICT_PUBLIC_BUCKETS = "RestrictPublicBuckets"
    BLOCK_PUBLIC_POLICY = "BlockPublicPolicy"
    BLOCK_PUBLIC_ACLS = "BlockPublicAcls"
    IGNORE_PUBLIC_ACLS = "IgnorePublicAcls"

    _property_mappings: ClassVar[dict[str, str]] = {
        "restrict_public_buckets": "RestrictPublicBuckets",
        "block_public_policy": "BlockPublicPolicy",
        "block_public_acls": "BlockPublicAcls",
        "ignore_public_acls": "IgnorePublicAcls",
    }

    restrict_public_buckets: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    block_public_policy: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    block_public_acls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ignore_public_acls: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class QueueConfiguration(PropertyType):
    FILTER = "Filter"
    EVENT = "Event"
    QUEUE = "Queue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "event": "Event",
        "queue": "Queue",
    }

    filter: Optional[NotificationFilter] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    queue: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecordExpiration(PropertyType):
    DAYS = "Days"
    EXPIRATION = "Expiration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "days": "Days",
        "expiration": "Expiration",
    }

    days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    expiration: Optional[Union[str, ExpirationState, Ref, GetAtt, Sub]] = None


@dataclass
class RedirectAllRequestsTo(PropertyType):
    PROTOCOL = "Protocol"
    HOST_NAME = "HostName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol": "Protocol",
        "host_name": "HostName",
    }

    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None
    host_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedirectRule(PropertyType):
    REPLACE_KEY_WITH = "ReplaceKeyWith"
    HTTP_REDIRECT_CODE = "HttpRedirectCode"
    PROTOCOL = "Protocol"
    HOST_NAME = "HostName"
    REPLACE_KEY_PREFIX_WITH = "ReplaceKeyPrefixWith"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replace_key_with": "ReplaceKeyWith",
        "http_redirect_code": "HttpRedirectCode",
        "protocol": "Protocol",
        "host_name": "HostName",
        "replace_key_prefix_with": "ReplaceKeyPrefixWith",
    }

    replace_key_with: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_redirect_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replace_key_prefix_with: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicaModifications(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, ReplicaModificationsStatus, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationConfiguration(PropertyType):
    ROLE = "Role"
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "rules": "Rules",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[ReplicationRule]] = None


@dataclass
class ReplicationDestination(PropertyType):
    ACCESS_CONTROL_TRANSLATION = "AccessControlTranslation"
    ACCOUNT = "Account"
    METRICS = "Metrics"
    BUCKET = "Bucket"
    ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    STORAGE_CLASS = "StorageClass"
    REPLICATION_TIME = "ReplicationTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_control_translation": "AccessControlTranslation",
        "account": "Account",
        "metrics": "Metrics",
        "bucket": "Bucket",
        "encryption_configuration": "EncryptionConfiguration",
        "storage_class": "StorageClass",
        "replication_time": "ReplicationTime",
    }

    access_control_translation: Optional[AccessControlTranslation] = None
    account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metrics: Optional[Metrics] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[EncryptionConfiguration] = None
    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replication_time: Optional[ReplicationTime] = None


@dataclass
class ReplicationRule(PropertyType):
    STATUS = "Status"
    DESTINATION = "Destination"
    FILTER = "Filter"
    PRIORITY = "Priority"
    SOURCE_SELECTION_CRITERIA = "SourceSelectionCriteria"
    ID = "Id"
    PREFIX = "Prefix"
    DELETE_MARKER_REPLICATION = "DeleteMarkerReplication"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "destination": "Destination",
        "filter": "Filter",
        "priority": "Priority",
        "source_selection_criteria": "SourceSelectionCriteria",
        "id": "Id",
        "prefix": "Prefix",
        "delete_marker_replication": "DeleteMarkerReplication",
    }

    status: Optional[Union[str, ReplicationRuleStatus, Ref, GetAtt, Sub]] = None
    destination: Optional[ReplicationDestination] = None
    filter: Optional[ReplicationRuleFilter] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source_selection_criteria: Optional[SourceSelectionCriteria] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delete_marker_replication: Optional[DeleteMarkerReplication] = None


@dataclass
class ReplicationRuleAndOperator(PropertyType):
    TAG_FILTERS = "TagFilters"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_filters": "TagFilters",
        "prefix": "Prefix",
    }

    tag_filters: Optional[list[TagFilter]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationRuleFilter(PropertyType):
    AND = "And"
    TAG_FILTER = "TagFilter"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "and_": "And",
        "tag_filter": "TagFilter",
        "prefix": "Prefix",
    }

    and_: Optional[ReplicationRuleAndOperator] = None
    tag_filter: Optional[TagFilter] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationTime(PropertyType):
    STATUS = "Status"
    TIME = "Time"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "time": "Time",
    }

    status: Optional[Union[str, ReplicationTimeStatus, Ref, GetAtt, Sub]] = None
    time: Optional[ReplicationTimeValue] = None


@dataclass
class ReplicationTimeValue(PropertyType):
    MINUTES = "Minutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minutes": "Minutes",
    }

    minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingRule(PropertyType):
    REDIRECT_RULE = "RedirectRule"
    ROUTING_RULE_CONDITION = "RoutingRuleCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "redirect_rule": "RedirectRule",
        "routing_rule_condition": "RoutingRuleCondition",
    }

    redirect_rule: Optional[RedirectRule] = None
    routing_rule_condition: Optional[RoutingRuleCondition] = None


@dataclass
class RoutingRuleCondition(PropertyType):
    KEY_PREFIX_EQUALS = "KeyPrefixEquals"
    HTTP_ERROR_CODE_RETURNED_EQUALS = "HttpErrorCodeReturnedEquals"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_prefix_equals": "KeyPrefixEquals",
        "http_error_code_returned_equals": "HttpErrorCodeReturnedEquals",
    }

    key_prefix_equals: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_error_code_returned_equals: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    STATUS = "Status"
    EXPIRED_OBJECT_DELETE_MARKER = "ExpiredObjectDeleteMarker"
    NONCURRENT_VERSION_EXPIRATION_IN_DAYS = "NoncurrentVersionExpirationInDays"
    TRANSITIONS = "Transitions"
    OBJECT_SIZE_GREATER_THAN = "ObjectSizeGreaterThan"
    TAG_FILTERS = "TagFilters"
    NONCURRENT_VERSION_TRANSITIONS = "NoncurrentVersionTransitions"
    PREFIX = "Prefix"
    OBJECT_SIZE_LESS_THAN = "ObjectSizeLessThan"
    NONCURRENT_VERSION_TRANSITION = "NoncurrentVersionTransition"
    EXPIRATION_DATE = "ExpirationDate"
    NONCURRENT_VERSION_EXPIRATION = "NoncurrentVersionExpiration"
    EXPIRATION_IN_DAYS = "ExpirationInDays"
    TRANSITION = "Transition"
    ID = "Id"
    ABORT_INCOMPLETE_MULTIPART_UPLOAD = "AbortIncompleteMultipartUpload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "expired_object_delete_marker": "ExpiredObjectDeleteMarker",
        "noncurrent_version_expiration_in_days": "NoncurrentVersionExpirationInDays",
        "transitions": "Transitions",
        "object_size_greater_than": "ObjectSizeGreaterThan",
        "tag_filters": "TagFilters",
        "noncurrent_version_transitions": "NoncurrentVersionTransitions",
        "prefix": "Prefix",
        "object_size_less_than": "ObjectSizeLessThan",
        "noncurrent_version_transition": "NoncurrentVersionTransition",
        "expiration_date": "ExpirationDate",
        "noncurrent_version_expiration": "NoncurrentVersionExpiration",
        "expiration_in_days": "ExpirationInDays",
        "transition": "Transition",
        "id": "Id",
        "abort_incomplete_multipart_upload": "AbortIncompleteMultipartUpload",
    }

    status: Optional[Union[str, ExpirationStatus, Ref, GetAtt, Sub]] = None
    expired_object_delete_marker: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    noncurrent_version_expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transitions: Optional[list[Transition]] = None
    object_size_greater_than: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_filters: Optional[list[TagFilter]] = None
    noncurrent_version_transitions: Optional[list[NoncurrentVersionTransition]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_size_less_than: Optional[Union[str, Ref, GetAtt, Sub]] = None
    noncurrent_version_transition: Optional[NoncurrentVersionTransition] = None
    expiration_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = None
    expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transition: Optional[Transition] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = None


@dataclass
class S3KeyFilter(PropertyType):
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[FilterRule]] = None


@dataclass
class S3TablesDestination(PropertyType):
    TABLE_BUCKET_ARN = "TableBucketArn"
    TABLE_NAME = "TableName"
    TABLE_ARN = "TableArn"
    TABLE_NAMESPACE = "TableNamespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_bucket_arn": "TableBucketArn",
        "table_name": "TableName",
        "table_arn": "TableArn",
        "table_namespace": "TableNamespace",
    }

    table_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    SSE_ALGORITHM = "SSEAlgorithm"
    KMS_MASTER_KEY_ID = "KMSMasterKeyID"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_algorithm": "SSEAlgorithm",
        "kms_master_key_id": "KMSMasterKeyID",
    }

    sse_algorithm: Optional[Union[str, ServerSideEncryption, Ref, GetAtt, Sub]] = None
    kms_master_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    BUCKET_KEY_ENABLED = "BucketKeyEnabled"
    BLOCKED_ENCRYPTION_TYPES = "BlockedEncryptionTypes"
    SERVER_SIDE_ENCRYPTION_BY_DEFAULT = "ServerSideEncryptionByDefault"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_key_enabled": "BucketKeyEnabled",
        "blocked_encryption_types": "BlockedEncryptionTypes",
        "server_side_encryption_by_default": "ServerSideEncryptionByDefault",
    }

    bucket_key_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    blocked_encryption_types: Optional[BlockedEncryptionTypes] = None
    server_side_encryption_by_default: Optional[ServerSideEncryptionByDefault] = None


@dataclass
class SourceSelectionCriteria(PropertyType):
    REPLICA_MODIFICATIONS = "ReplicaModifications"
    SSE_KMS_ENCRYPTED_OBJECTS = "SseKmsEncryptedObjects"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_modifications": "ReplicaModifications",
        "sse_kms_encrypted_objects": "SseKmsEncryptedObjects",
    }

    replica_modifications: Optional[ReplicaModifications] = None
    sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = None


@dataclass
class SseKmsEncryptedObjects(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, SseKmsEncryptedObjectsStatus, Ref, GetAtt, Sub]] = None


@dataclass
class StorageClassAnalysis(PropertyType):
    DATA_EXPORT = "DataExport"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_export": "DataExport",
    }

    data_export: Optional[DataExport] = None


@dataclass
class TagFilter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetObjectKeyFormat(PropertyType):
    PARTITIONED_PREFIX = "PartitionedPrefix"
    SIMPLE_PREFIX = "SimplePrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partitioned_prefix": "PartitionedPrefix",
        "simple_prefix": "SimplePrefix",
    }

    partitioned_prefix: Optional[PartitionedPrefix] = None
    simple_prefix: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class Tiering(PropertyType):
    ACCESS_TIER = "AccessTier"
    DAYS = "Days"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_tier": "AccessTier",
        "days": "Days",
    }

    access_tier: Optional[Union[str, IntelligentTieringAccessTier, Ref, GetAtt, Sub]] = None
    days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TopicConfiguration(PropertyType):
    FILTER = "Filter"
    EVENT = "Event"
    TOPIC = "Topic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "event": "Event",
        "topic": "Topic",
    }

    filter: Optional[NotificationFilter] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transition(PropertyType):
    TRANSITION_DATE = "TransitionDate"
    STORAGE_CLASS = "StorageClass"
    TRANSITION_IN_DAYS = "TransitionInDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_date": "TransitionDate",
        "storage_class": "StorageClass",
        "transition_in_days": "TransitionInDays",
    }

    transition_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_class: Optional[Union[str, TransitionStorageClass, Ref, GetAtt, Sub]] = None
    transition_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VersioningConfiguration(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, BucketVersioningStatus, Ref, GetAtt, Sub]] = None


@dataclass
class WebsiteConfiguration(PropertyType):
    INDEX_DOCUMENT = "IndexDocument"
    REDIRECT_ALL_REQUESTS_TO = "RedirectAllRequestsTo"
    ROUTING_RULES = "RoutingRules"
    ERROR_DOCUMENT = "ErrorDocument"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_document": "IndexDocument",
        "redirect_all_requests_to": "RedirectAllRequestsTo",
        "routing_rules": "RoutingRules",
        "error_document": "ErrorDocument",
    }

    index_document: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_all_requests_to: Optional[RedirectAllRequestsTo] = None
    routing_rules: Optional[list[RoutingRule]] = None
    error_document: Optional[Union[str, Ref, GetAtt, Sub]] = None

