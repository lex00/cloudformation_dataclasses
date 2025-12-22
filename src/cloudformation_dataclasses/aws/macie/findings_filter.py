"""PropertyTypes for AWS::Macie::FindingsFilter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AdminStatus:
    """AdminStatus enum values."""

    ENABLED = "ENABLED"
    DISABLING_IN_PROGRESS = "DISABLING_IN_PROGRESS"


class AllowListStatusCode:
    """AllowListStatusCode enum values."""

    OK = "OK"
    S3_OBJECT_NOT_FOUND = "S3_OBJECT_NOT_FOUND"
    S3_USER_ACCESS_DENIED = "S3_USER_ACCESS_DENIED"
    S3_OBJECT_ACCESS_DENIED = "S3_OBJECT_ACCESS_DENIED"
    S3_THROTTLED = "S3_THROTTLED"
    S3_OBJECT_OVERSIZE = "S3_OBJECT_OVERSIZE"
    S3_OBJECT_EMPTY = "S3_OBJECT_EMPTY"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"


class AllowsUnencryptedObjectUploads:
    """AllowsUnencryptedObjectUploads enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"
    UNKNOWN = "UNKNOWN"


class AutoEnableMode:
    """AutoEnableMode enum values."""

    ALL = "ALL"
    NEW = "NEW"
    NONE = "NONE"


class AutomatedDiscoveryAccountStatus:
    """AutomatedDiscoveryAccountStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AutomatedDiscoveryAccountUpdateErrorCode:
    """AutomatedDiscoveryAccountUpdateErrorCode enum values."""

    ACCOUNT_PAUSED = "ACCOUNT_PAUSED"
    ACCOUNT_NOT_FOUND = "ACCOUNT_NOT_FOUND"


class AutomatedDiscoveryMonitoringStatus:
    """AutomatedDiscoveryMonitoringStatus enum values."""

    MONITORED = "MONITORED"
    NOT_MONITORED = "NOT_MONITORED"


class AutomatedDiscoveryStatus:
    """AutomatedDiscoveryStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AvailabilityCode:
    """AvailabilityCode enum values."""

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class BucketMetadataErrorCode:
    """BucketMetadataErrorCode enum values."""

    ACCESS_DENIED = "ACCESS_DENIED"
    BUCKET_COUNT_EXCEEDS_QUOTA = "BUCKET_COUNT_EXCEEDS_QUOTA"


class ClassificationScopeUpdateOperation:
    """ClassificationScopeUpdateOperation enum values."""

    ADD = "ADD"
    REPLACE = "REPLACE"
    REMOVE = "REMOVE"


class Currency:
    """Currency enum values."""

    USD = "USD"


class DataIdentifierSeverity:
    """DataIdentifierSeverity enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class DataIdentifierType:
    """DataIdentifierType enum values."""

    CUSTOM = "CUSTOM"
    MANAGED = "MANAGED"


class DayOfWeek:
    """DayOfWeek enum values."""

    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class EffectivePermission:
    """EffectivePermission enum values."""

    PUBLIC = "PUBLIC"
    NOT_PUBLIC = "NOT_PUBLIC"
    UNKNOWN = "UNKNOWN"


class EncryptionType:
    """EncryptionType enum values."""

    NONE = "NONE"
    AES256 = "AES256"
    AWS_KMS = "aws:kms"
    UNKNOWN = "UNKNOWN"
    AWS_KMS_DSSE = "aws:kms:dsse"


class ErrorCode:
    """ErrorCode enum values."""

    CLIENTERROR = "ClientError"
    INTERNALERROR = "InternalError"


class FindingActionType:
    """FindingActionType enum values."""

    AWS_API_CALL = "AWS_API_CALL"


class FindingCategory:
    """FindingCategory enum values."""

    CLASSIFICATION = "CLASSIFICATION"
    POLICY = "POLICY"


class FindingPublishingFrequency:
    """FindingPublishingFrequency enum values."""

    FIFTEEN_MINUTES = "FIFTEEN_MINUTES"
    ONE_HOUR = "ONE_HOUR"
    SIX_HOURS = "SIX_HOURS"


class FindingStatisticsSortAttributeName:
    """FindingStatisticsSortAttributeName enum values."""

    GROUPKEY = "groupKey"
    COUNT = "count"


class FindingType:
    """FindingType enum values."""

    SENSITIVEDATA_S3OBJECT_MULTIPLE = "SensitiveData:S3Object/Multiple"
    SENSITIVEDATA_S3OBJECT_FINANCIAL = "SensitiveData:S3Object/Financial"
    SENSITIVEDATA_S3OBJECT_PERSONAL = "SensitiveData:S3Object/Personal"
    SENSITIVEDATA_S3OBJECT_CREDENTIALS = "SensitiveData:S3Object/Credentials"
    SENSITIVEDATA_S3OBJECT_CUSTOMIDENTIFIER = "SensitiveData:S3Object/CustomIdentifier"
    POLICY_IAMUSER_S3BUCKETPUBLIC = "Policy:IAMUser/S3BucketPublic"
    POLICY_IAMUSER_S3BUCKETSHAREDEXTERNALLY = "Policy:IAMUser/S3BucketSharedExternally"
    POLICY_IAMUSER_S3BUCKETREPLICATEDEXTERNALLY = "Policy:IAMUser/S3BucketReplicatedExternally"
    POLICY_IAMUSER_S3BUCKETENCRYPTIONDISABLED = "Policy:IAMUser/S3BucketEncryptionDisabled"
    POLICY_IAMUSER_S3BLOCKPUBLICACCESSDISABLED = "Policy:IAMUser/S3BlockPublicAccessDisabled"
    POLICY_IAMUSER_S3BUCKETSHAREDWITHCLOUDFRONT = "Policy:IAMUser/S3BucketSharedWithCloudFront"


class FindingsFilterAction:
    """FindingsFilterAction enum values."""

    ARCHIVE = "ARCHIVE"
    NOOP = "NOOP"


class GroupBy:
    """GroupBy enum values."""

    RESOURCESAFFECTED_S3BUCKET_NAME = "resourcesAffected.s3Bucket.name"
    TYPE = "type"
    CLASSIFICATIONDETAILS_JOBID = "classificationDetails.jobId"
    SEVERITY_DESCRIPTION = "severity.description"


class IsDefinedInJob:
    """IsDefinedInJob enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"
    UNKNOWN = "UNKNOWN"


class IsMonitoredByJob:
    """IsMonitoredByJob enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"
    UNKNOWN = "UNKNOWN"


class JobComparator:
    """JobComparator enum values."""

    EQ = "EQ"
    GT = "GT"
    GTE = "GTE"
    LT = "LT"
    LTE = "LTE"
    NE = "NE"
    CONTAINS = "CONTAINS"
    STARTS_WITH = "STARTS_WITH"


class JobStatus:
    """JobStatus enum values."""

    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
    IDLE = "IDLE"
    USER_PAUSED = "USER_PAUSED"


class JobType:
    """JobType enum values."""

    ONE_TIME = "ONE_TIME"
    SCHEDULED = "SCHEDULED"


class LastRunErrorStatusCode:
    """LastRunErrorStatusCode enum values."""

    NONE = "NONE"
    ERROR = "ERROR"


class ListJobsFilterKey:
    """ListJobsFilterKey enum values."""

    JOBTYPE = "jobType"
    JOBSTATUS = "jobStatus"
    CREATEDAT = "createdAt"
    NAME = "name"


class ListJobsSortAttributeName:
    """ListJobsSortAttributeName enum values."""

    CREATEDAT = "createdAt"
    JOBSTATUS = "jobStatus"
    NAME = "name"
    JOBTYPE = "jobType"


class MacieStatus:
    """MacieStatus enum values."""

    PAUSED = "PAUSED"
    ENABLED = "ENABLED"


class ManagedDataIdentifierSelector:
    """ManagedDataIdentifierSelector enum values."""

    ALL = "ALL"
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"
    NONE = "NONE"
    RECOMMENDED = "RECOMMENDED"


class OrderBy:
    """OrderBy enum values."""

    ASC = "ASC"
    DESC = "DESC"


class OriginType:
    """OriginType enum values."""

    SENSITIVE_DATA_DISCOVERY_JOB = "SENSITIVE_DATA_DISCOVERY_JOB"
    AUTOMATED_SENSITIVE_DATA_DISCOVERY = "AUTOMATED_SENSITIVE_DATA_DISCOVERY"


class RelationshipStatus:
    """RelationshipStatus enum values."""

    ENABLED = "Enabled"
    PAUSED = "Paused"
    INVITED = "Invited"
    CREATED = "Created"
    REMOVED = "Removed"
    RESIGNED = "Resigned"
    EMAILVERIFICATIONINPROGRESS = "EmailVerificationInProgress"
    EMAILVERIFICATIONFAILED = "EmailVerificationFailed"
    REGIONDISABLED = "RegionDisabled"
    ACCOUNTSUSPENDED = "AccountSuspended"


class RetrievalMode:
    """RetrievalMode enum values."""

    CALLER_CREDENTIALS = "CALLER_CREDENTIALS"
    ASSUME_ROLE = "ASSUME_ROLE"


class RevealRequestStatus:
    """RevealRequestStatus enum values."""

    SUCCESS = "SUCCESS"
    PROCESSING = "PROCESSING"
    ERROR = "ERROR"


class RevealStatus:
    """RevealStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ScopeFilterKey:
    """ScopeFilterKey enum values."""

    OBJECT_EXTENSION = "OBJECT_EXTENSION"
    OBJECT_LAST_MODIFIED_DATE = "OBJECT_LAST_MODIFIED_DATE"
    OBJECT_SIZE = "OBJECT_SIZE"
    OBJECT_KEY = "OBJECT_KEY"


class SearchResourcesComparator:
    """SearchResourcesComparator enum values."""

    EQ = "EQ"
    NE = "NE"


class SearchResourcesSimpleCriterionKey:
    """SearchResourcesSimpleCriterionKey enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    S3_BUCKET_NAME = "S3_BUCKET_NAME"
    S3_BUCKET_EFFECTIVE_PERMISSION = "S3_BUCKET_EFFECTIVE_PERMISSION"
    S3_BUCKET_SHARED_ACCESS = "S3_BUCKET_SHARED_ACCESS"
    AUTOMATED_DISCOVERY_MONITORING_STATUS = "AUTOMATED_DISCOVERY_MONITORING_STATUS"


class SearchResourcesSortAttributeName:
    """SearchResourcesSortAttributeName enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    RESOURCE_NAME = "RESOURCE_NAME"
    S3_CLASSIFIABLE_OBJECT_COUNT = "S3_CLASSIFIABLE_OBJECT_COUNT"
    S3_CLASSIFIABLE_SIZE_IN_BYTES = "S3_CLASSIFIABLE_SIZE_IN_BYTES"


class SensitiveDataItemCategory:
    """SensitiveDataItemCategory enum values."""

    FINANCIAL_INFORMATION = "FINANCIAL_INFORMATION"
    PERSONAL_INFORMATION = "PERSONAL_INFORMATION"
    CREDENTIALS = "CREDENTIALS"
    CUSTOM_IDENTIFIER = "CUSTOM_IDENTIFIER"


class SeverityDescription:
    """SeverityDescription enum values."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class SharedAccess:
    """SharedAccess enum values."""

    EXTERNAL = "EXTERNAL"
    INTERNAL = "INTERNAL"
    NOT_SHARED = "NOT_SHARED"
    UNKNOWN = "UNKNOWN"


class SimpleCriterionKeyForJob:
    """SimpleCriterionKeyForJob enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    S3_BUCKET_NAME = "S3_BUCKET_NAME"
    S3_BUCKET_EFFECTIVE_PERMISSION = "S3_BUCKET_EFFECTIVE_PERMISSION"
    S3_BUCKET_SHARED_ACCESS = "S3_BUCKET_SHARED_ACCESS"


class StorageClass:
    """StorageClass enum values."""

    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    ONEZONE_IA = "ONEZONE_IA"
    GLACIER = "GLACIER"
    GLACIER_IR = "GLACIER_IR"
    OUTPOSTS = "OUTPOSTS"


class TagTarget:
    """TagTarget enum values."""

    S3_OBJECT = "S3_OBJECT"


class TimeRange:
    """TimeRange enum values."""

    MONTH_TO_DATE = "MONTH_TO_DATE"
    PAST_30_DAYS = "PAST_30_DAYS"


class Type:
    """Type enum values."""

    NONE = "NONE"
    AES256 = "AES256"
    AWS_KMS = "aws:kms"
    AWS_KMS_DSSE = "aws:kms:dsse"


class UnavailabilityReasonCode:
    """UnavailabilityReasonCode enum values."""

    OBJECT_EXCEEDS_SIZE_QUOTA = "OBJECT_EXCEEDS_SIZE_QUOTA"
    UNSUPPORTED_OBJECT_TYPE = "UNSUPPORTED_OBJECT_TYPE"
    UNSUPPORTED_FINDING_TYPE = "UNSUPPORTED_FINDING_TYPE"
    INVALID_CLASSIFICATION_RESULT = "INVALID_CLASSIFICATION_RESULT"
    OBJECT_UNAVAILABLE = "OBJECT_UNAVAILABLE"
    ACCOUNT_NOT_IN_ORGANIZATION = "ACCOUNT_NOT_IN_ORGANIZATION"
    MISSING_GET_MEMBER_PERMISSION = "MISSING_GET_MEMBER_PERMISSION"
    ROLE_TOO_PERMISSIVE = "ROLE_TOO_PERMISSIVE"
    MEMBER_ROLE_TOO_PERMISSIVE = "MEMBER_ROLE_TOO_PERMISSIVE"
    INVALID_RESULT_SIGNATURE = "INVALID_RESULT_SIGNATURE"
    RESULT_NOT_SIGNED = "RESULT_NOT_SIGNED"


class Unit:
    """Unit enum values."""

    TERABYTES = "TERABYTES"


class UsageStatisticsFilterComparator:
    """UsageStatisticsFilterComparator enum values."""

    GT = "GT"
    GTE = "GTE"
    LT = "LT"
    LTE = "LTE"
    EQ = "EQ"
    NE = "NE"
    CONTAINS = "CONTAINS"


class UsageStatisticsFilterKey:
    """UsageStatisticsFilterKey enum values."""

    ACCOUNTID = "accountId"
    SERVICELIMIT = "serviceLimit"
    FREETRIALSTARTDATE = "freeTrialStartDate"
    TOTAL = "total"


class UsageStatisticsSortKey:
    """UsageStatisticsSortKey enum values."""

    ACCOUNTID = "accountId"
    TOTAL = "total"
    SERVICELIMITVALUE = "serviceLimitValue"
    FREETRIALSTARTDATE = "freeTrialStartDate"


class UsageType:
    """UsageType enum values."""

    DATA_INVENTORY_EVALUATION = "DATA_INVENTORY_EVALUATION"
    SENSITIVE_DATA_DISCOVERY = "SENSITIVE_DATA_DISCOVERY"
    AUTOMATED_SENSITIVE_DATA_DISCOVERY = "AUTOMATED_SENSITIVE_DATA_DISCOVERY"
    AUTOMATED_OBJECT_MONITORING = "AUTOMATED_OBJECT_MONITORING"


class UserIdentityType:
    """UserIdentityType enum values."""

    ASSUMEDROLE = "AssumedRole"
    IAMUSER = "IAMUser"
    FEDERATEDUSER = "FederatedUser"
    ROOT = "Root"
    AWSACCOUNT = "AWSAccount"
    AWSSERVICE = "AWSService"


@dataclass
class CriterionAdditionalProperties(PropertyType):
    LT = "lt"
    GTE = "gte"
    NEQ = "neq"
    LTE = "lte"
    EQ = "eq"
    GT = "gt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lt": "lt",
        "gte": "gte",
        "neq": "neq",
        "lte": "lte",
        "eq": "eq",
        "gt": "gt",
    }

    lt: Optional[Union[int, Ref, GetAtt, Sub]] = None
    gte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    neq: Optional[Union[list[str], Ref]] = None
    lte: Optional[Union[int, Ref, GetAtt, Sub]] = None
    eq: Optional[Union[list[str], Ref]] = None
    gt: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FindingCriteria(PropertyType):
    CRITERION = "Criterion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "criterion": "Criterion",
    }

    criterion: Optional[dict[str, Any]] = None

