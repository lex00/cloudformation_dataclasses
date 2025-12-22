"""PropertyTypes for AWS::AccessAnalyzer::Analyzer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessCheckPolicyType:
    """AccessCheckPolicyType enum values."""

    IDENTITY_POLICY = "IDENTITY_POLICY"
    RESOURCE_POLICY = "RESOURCE_POLICY"


class AccessCheckResourceType:
    """AccessCheckResourceType enum values."""

    AWS_DYNAMODB_TABLE = "AWS::DynamoDB::Table"
    AWS_DYNAMODB_STREAM = "AWS::DynamoDB::Stream"
    AWS_EFS_FILESYSTEM = "AWS::EFS::FileSystem"
    AWS_OPENSEARCHSERVICE_DOMAIN = "AWS::OpenSearchService::Domain"
    AWS_KINESIS_STREAM = "AWS::Kinesis::Stream"
    AWS_KINESIS_STREAMCONSUMER = "AWS::Kinesis::StreamConsumer"
    AWS_KMS_KEY = "AWS::KMS::Key"
    AWS_LAMBDA_FUNCTION = "AWS::Lambda::Function"
    AWS_S3_BUCKET = "AWS::S3::Bucket"
    AWS_S3_ACCESSPOINT = "AWS::S3::AccessPoint"
    AWS_S3EXPRESS_DIRECTORYBUCKET = "AWS::S3Express::DirectoryBucket"
    AWS_S3_GLACIER = "AWS::S3::Glacier"
    AWS_S3OUTPOSTS_BUCKET = "AWS::S3Outposts::Bucket"
    AWS_S3OUTPOSTS_ACCESSPOINT = "AWS::S3Outposts::AccessPoint"
    AWS_SECRETSMANAGER_SECRET = "AWS::SecretsManager::Secret"
    AWS_SNS_TOPIC = "AWS::SNS::Topic"
    AWS_SQS_QUEUE = "AWS::SQS::Queue"
    AWS_IAM_ASSUMEROLEPOLICYDOCUMENT = "AWS::IAM::AssumeRolePolicyDocument"
    AWS_S3TABLES_TABLEBUCKET = "AWS::S3Tables::TableBucket"
    AWS_APIGATEWAY_RESTAPI = "AWS::ApiGateway::RestApi"
    AWS_CODEARTIFACT_DOMAIN = "AWS::CodeArtifact::Domain"
    AWS_BACKUP_BACKUPVAULT = "AWS::Backup::BackupVault"
    AWS_CLOUDTRAIL_DASHBOARD = "AWS::CloudTrail::Dashboard"
    AWS_CLOUDTRAIL_EVENTDATASTORE = "AWS::CloudTrail::EventDataStore"
    AWS_S3TABLES_TABLE = "AWS::S3Tables::Table"
    AWS_S3EXPRESS_ACCESSPOINT = "AWS::S3Express::AccessPoint"


class AccessPreviewStatus:
    """AccessPreviewStatus enum values."""

    COMPLETED = "COMPLETED"
    CREATING = "CREATING"
    FAILED = "FAILED"


class AccessPreviewStatusReasonCode:
    """AccessPreviewStatusReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_CONFIGURATION = "INVALID_CONFIGURATION"


class AclPermission:
    """AclPermission enum values."""

    READ = "READ"
    WRITE = "WRITE"
    READ_ACP = "READ_ACP"
    WRITE_ACP = "WRITE_ACP"
    FULL_CONTROL = "FULL_CONTROL"


class AnalyzerStatus:
    """AnalyzerStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DISABLED = "DISABLED"
    FAILED = "FAILED"


class CheckAccessNotGrantedResult:
    """CheckAccessNotGrantedResult enum values."""

    PASS = "PASS"
    FAIL = "FAIL"


class CheckNoNewAccessResult:
    """CheckNoNewAccessResult enum values."""

    PASS = "PASS"
    FAIL = "FAIL"


class CheckNoPublicAccessResult:
    """CheckNoPublicAccessResult enum values."""

    PASS = "PASS"
    FAIL = "FAIL"


class FindingChangeType:
    """FindingChangeType enum values."""

    CHANGED = "CHANGED"
    NEW = "NEW"
    UNCHANGED = "UNCHANGED"


class FindingSourceType:
    """FindingSourceType enum values."""

    POLICY = "POLICY"
    BUCKET_ACL = "BUCKET_ACL"
    S3_ACCESS_POINT = "S3_ACCESS_POINT"
    S3_ACCESS_POINT_ACCOUNT = "S3_ACCESS_POINT_ACCOUNT"


class FindingStatus:
    """FindingStatus enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    RESOLVED = "RESOLVED"


class FindingStatusUpdate:
    """FindingStatusUpdate enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class FindingType:
    """FindingType enum values."""

    EXTERNALACCESS = "ExternalAccess"
    UNUSEDIAMROLE = "UnusedIAMRole"
    UNUSEDIAMUSERACCESSKEY = "UnusedIAMUserAccessKey"
    UNUSEDIAMUSERPASSWORD = "UnusedIAMUserPassword"
    UNUSEDPERMISSION = "UnusedPermission"
    INTERNALACCESS = "InternalAccess"


class InternalAccessType:
    """InternalAccessType enum values."""

    INTRA_ACCOUNT = "INTRA_ACCOUNT"
    INTRA_ORG = "INTRA_ORG"


class JobErrorCode:
    """JobErrorCode enum values."""

    AUTHORIZATION_ERROR = "AUTHORIZATION_ERROR"
    RESOURCE_NOT_FOUND_ERROR = "RESOURCE_NOT_FOUND_ERROR"
    SERVICE_QUOTA_EXCEEDED_ERROR = "SERVICE_QUOTA_EXCEEDED_ERROR"
    SERVICE_ERROR = "SERVICE_ERROR"


class JobStatus:
    """JobStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class KmsGrantOperation:
    """KmsGrantOperation enum values."""

    CREATEGRANT = "CreateGrant"
    DECRYPT = "Decrypt"
    DESCRIBEKEY = "DescribeKey"
    ENCRYPT = "Encrypt"
    GENERATEDATAKEY = "GenerateDataKey"
    GENERATEDATAKEYPAIR = "GenerateDataKeyPair"
    GENERATEDATAKEYPAIRWITHOUTPLAINTEXT = "GenerateDataKeyPairWithoutPlaintext"
    GENERATEDATAKEYWITHOUTPLAINTEXT = "GenerateDataKeyWithoutPlaintext"
    GETPUBLICKEY = "GetPublicKey"
    REENCRYPTFROM = "ReEncryptFrom"
    REENCRYPTTO = "ReEncryptTo"
    RETIREGRANT = "RetireGrant"
    SIGN = "Sign"
    VERIFY = "Verify"


class Locale:
    """Locale enum values."""

    DE = "DE"
    EN = "EN"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    JA = "JA"
    KO = "KO"
    PT_BR = "PT_BR"
    ZH_CN = "ZH_CN"
    ZH_TW = "ZH_TW"


class OrderBy:
    """OrderBy enum values."""

    ASC = "ASC"
    DESC = "DESC"


class PolicyType:
    """PolicyType enum values."""

    IDENTITY_POLICY = "IDENTITY_POLICY"
    RESOURCE_POLICY = "RESOURCE_POLICY"
    SERVICE_CONTROL_POLICY = "SERVICE_CONTROL_POLICY"
    RESOURCE_CONTROL_POLICY = "RESOURCE_CONTROL_POLICY"


class PrincipalType:
    """PrincipalType enum values."""

    IAM_ROLE = "IAM_ROLE"
    IAM_USER = "IAM_USER"


class ReasonCode:
    """ReasonCode enum values."""

    AWS_SERVICE_ACCESS_DISABLED = "AWS_SERVICE_ACCESS_DISABLED"
    DELEGATED_ADMINISTRATOR_DEREGISTERED = "DELEGATED_ADMINISTRATOR_DEREGISTERED"
    ORGANIZATION_DELETED = "ORGANIZATION_DELETED"
    SERVICE_LINKED_ROLE_CREATION_FAILED = "SERVICE_LINKED_ROLE_CREATION_FAILED"


class RecommendationType:
    """RecommendationType enum values."""

    UNUSEDPERMISSIONRECOMMENDATION = "UnusedPermissionRecommendation"


class RecommendedRemediationAction:
    """RecommendedRemediationAction enum values."""

    CREATE_POLICY = "CREATE_POLICY"
    DETACH_POLICY = "DETACH_POLICY"


class ResourceControlPolicyRestriction:
    """ResourceControlPolicyRestriction enum values."""

    APPLICABLE = "APPLICABLE"
    FAILED_TO_EVALUATE_RCP = "FAILED_TO_EVALUATE_RCP"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    APPLIED = "APPLIED"


class ResourceType:
    """ResourceType enum values."""

    AWS_S3_BUCKET = "AWS::S3::Bucket"
    AWS_IAM_ROLE = "AWS::IAM::Role"
    AWS_SQS_QUEUE = "AWS::SQS::Queue"
    AWS_LAMBDA_FUNCTION = "AWS::Lambda::Function"
    AWS_LAMBDA_LAYERVERSION = "AWS::Lambda::LayerVersion"
    AWS_KMS_KEY = "AWS::KMS::Key"
    AWS_SECRETSMANAGER_SECRET = "AWS::SecretsManager::Secret"
    AWS_EFS_FILESYSTEM = "AWS::EFS::FileSystem"
    AWS_EC2_SNAPSHOT = "AWS::EC2::Snapshot"
    AWS_ECR_REPOSITORY = "AWS::ECR::Repository"
    AWS_RDS_DBSNAPSHOT = "AWS::RDS::DBSnapshot"
    AWS_RDS_DBCLUSTERSNAPSHOT = "AWS::RDS::DBClusterSnapshot"
    AWS_SNS_TOPIC = "AWS::SNS::Topic"
    AWS_S3EXPRESS_DIRECTORYBUCKET = "AWS::S3Express::DirectoryBucket"
    AWS_DYNAMODB_TABLE = "AWS::DynamoDB::Table"
    AWS_DYNAMODB_STREAM = "AWS::DynamoDB::Stream"
    AWS_IAM_USER = "AWS::IAM::User"


class ServiceControlPolicyRestriction:
    """ServiceControlPolicyRestriction enum values."""

    APPLICABLE = "APPLICABLE"
    FAILED_TO_EVALUATE_SCP = "FAILED_TO_EVALUATE_SCP"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    APPLIED = "APPLIED"


class Status:
    """Status enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class Type:
    """Type enum values."""

    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"
    ACCOUNT_UNUSED_ACCESS = "ACCOUNT_UNUSED_ACCESS"
    ORGANIZATION_UNUSED_ACCESS = "ORGANIZATION_UNUSED_ACCESS"
    ACCOUNT_INTERNAL_ACCESS = "ACCOUNT_INTERNAL_ACCESS"
    ORGANIZATION_INTERNAL_ACCESS = "ORGANIZATION_INTERNAL_ACCESS"


class ValidatePolicyFindingType:
    """ValidatePolicyFindingType enum values."""

    ERROR = "ERROR"
    SECURITY_WARNING = "SECURITY_WARNING"
    SUGGESTION = "SUGGESTION"
    WARNING = "WARNING"


class ValidatePolicyResourceType:
    """ValidatePolicyResourceType enum values."""

    AWS_S3_BUCKET = "AWS::S3::Bucket"
    AWS_S3_ACCESSPOINT = "AWS::S3::AccessPoint"
    AWS_S3_MULTIREGIONACCESSPOINT = "AWS::S3::MultiRegionAccessPoint"
    AWS_S3OBJECTLAMBDA_ACCESSPOINT = "AWS::S3ObjectLambda::AccessPoint"
    AWS_IAM_ASSUMEROLEPOLICYDOCUMENT = "AWS::IAM::AssumeRolePolicyDocument"
    AWS_DYNAMODB_TABLE = "AWS::DynamoDB::Table"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"
    NOTSUPPORTED = "notSupported"


@dataclass
class AnalysisRule(PropertyType):
    EXCLUSIONS = "Exclusions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclusions": "Exclusions",
    }

    exclusions: Optional[list[AnalysisRuleCriteria]] = None


@dataclass
class AnalysisRuleCriteria(PropertyType):
    ACCOUNT_IDS = "AccountIds"
    RESOURCE_TAGS = "ResourceTags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_ids": "AccountIds",
        "resource_tags": "ResourceTags",
    }

    account_ids: Optional[Union[list[str], Ref]] = None
    resource_tags: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class AnalyzerConfiguration(PropertyType):
    INTERNAL_ACCESS_CONFIGURATION = "InternalAccessConfiguration"
    UNUSED_ACCESS_CONFIGURATION = "UnusedAccessConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "internal_access_configuration": "InternalAccessConfiguration",
        "unused_access_configuration": "UnusedAccessConfiguration",
    }

    internal_access_configuration: Optional[InternalAccessConfiguration] = None
    unused_access_configuration: Optional[UnusedAccessConfiguration] = None


@dataclass
class ArchiveRule(PropertyType):
    FILTER = "Filter"
    RULE_NAME = "RuleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "rule_name": "RuleName",
    }

    filter: Optional[list[Filter]] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Filter(PropertyType):
    EXISTS = "Exists"
    CONTAINS = "Contains"
    NEQ = "Neq"
    EQ = "Eq"
    PROPERTY = "Property"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exists": "Exists",
        "contains": "Contains",
        "neq": "Neq",
        "eq": "Eq",
        "property": "Property",
    }

    exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    contains: Optional[Union[list[str], Ref]] = None
    neq: Optional[Union[list[str], Ref]] = None
    eq: Optional[Union[list[str], Ref]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InternalAccessAnalysisRule(PropertyType):
    INCLUSIONS = "Inclusions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inclusions": "Inclusions",
    }

    inclusions: Optional[list[InternalAccessAnalysisRuleCriteria]] = None


@dataclass
class InternalAccessAnalysisRuleCriteria(PropertyType):
    RESOURCE_TYPES = "ResourceTypes"
    ACCOUNT_IDS = "AccountIds"
    RESOURCE_ARNS = "ResourceArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_types": "ResourceTypes",
        "account_ids": "AccountIds",
        "resource_arns": "ResourceArns",
    }

    resource_types: Optional[Union[list[str], Ref]] = None
    account_ids: Optional[Union[list[str], Ref]] = None
    resource_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class InternalAccessConfiguration(PropertyType):
    INTERNAL_ACCESS_ANALYSIS_RULE = "InternalAccessAnalysisRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "internal_access_analysis_rule": "InternalAccessAnalysisRule",
    }

    internal_access_analysis_rule: Optional[InternalAccessAnalysisRule] = None


@dataclass
class UnusedAccessConfiguration(PropertyType):
    UNUSED_ACCESS_AGE = "UnusedAccessAge"
    ANALYSIS_RULE = "AnalysisRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unused_access_age": "UnusedAccessAge",
        "analysis_rule": "AnalysisRule",
    }

    unused_access_age: Optional[Union[int, Ref, GetAtt, Sub]] = None
    analysis_rule: Optional[AnalysisRule] = None

