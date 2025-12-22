"""PropertyTypes for AWS::DataZone::Connection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceptRuleBehavior:
    """AcceptRuleBehavior enum values."""

    ALL = "ALL"
    NONE = "NONE"


class AttributeEntityType:
    """AttributeEntityType enum values."""

    ASSET = "ASSET"
    LISTING = "LISTING"


class AuthType:
    """AuthType enum values."""

    IAM_IDC = "IAM_IDC"
    DISABLED = "DISABLED"


class AuthenticationType:
    """AuthenticationType enum values."""

    BASIC = "BASIC"
    OAUTH2 = "OAUTH2"
    CUSTOM = "CUSTOM"


class ChangeAction:
    """ChangeAction enum values."""

    PUBLISH = "PUBLISH"
    UNPUBLISH = "UNPUBLISH"


class ComputeEnvironments:
    """ComputeEnvironments enum values."""

    SPARK = "SPARK"
    ATHENA = "ATHENA"
    PYTHON = "PYTHON"


class ConfigurableActionTypeAuthorization:
    """ConfigurableActionTypeAuthorization enum values."""

    IAM = "IAM"
    HTTPS = "HTTPS"


class ConfigurationStatus:
    """ConfigurationStatus enum values."""

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ConnectionScope:
    """ConnectionScope enum values."""

    DOMAIN = "DOMAIN"
    PROJECT = "PROJECT"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    READY = "READY"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class ConnectionType:
    """ConnectionType enum values."""

    ATHENA = "ATHENA"
    BIGQUERY = "BIGQUERY"
    DATABRICKS = "DATABRICKS"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    HYPERPOD = "HYPERPOD"
    IAM = "IAM"
    MYSQL = "MYSQL"
    OPENSEARCH = "OPENSEARCH"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SAPHANA = "SAPHANA"
    SNOWFLAKE = "SNOWFLAKE"
    SPARK = "SPARK"
    SQLSERVER = "SQLSERVER"
    TERADATA = "TERADATA"
    VERTICA = "VERTICA"
    WORKFLOWS_MWAA = "WORKFLOWS_MWAA"
    AMAZON_Q = "AMAZON_Q"
    MLFLOW = "MLFLOW"


class DataAssetActivityStatus:
    """DataAssetActivityStatus enum values."""

    FAILED = "FAILED"
    PUBLISHING_FAILED = "PUBLISHING_FAILED"
    SUCCEEDED_CREATED = "SUCCEEDED_CREATED"
    SUCCEEDED_UPDATED = "SUCCEEDED_UPDATED"
    SKIPPED_ALREADY_IMPORTED = "SKIPPED_ALREADY_IMPORTED"
    SKIPPED_ARCHIVED = "SKIPPED_ARCHIVED"
    SKIPPED_NO_ACCESS = "SKIPPED_NO_ACCESS"
    UNCHANGED = "UNCHANGED"


class DataProductItemType:
    """DataProductItemType enum values."""

    ASSET = "ASSET"


class DataProductStatus:
    """DataProductStatus enum values."""

    CREATED = "CREATED"
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"


class DataSourceErrorType:
    """DataSourceErrorType enum values."""

    ACCESS_DENIED_EXCEPTION = "ACCESS_DENIED_EXCEPTION"
    CONFLICT_EXCEPTION = "CONFLICT_EXCEPTION"
    INTERNAL_SERVER_EXCEPTION = "INTERNAL_SERVER_EXCEPTION"
    RESOURCE_NOT_FOUND_EXCEPTION = "RESOURCE_NOT_FOUND_EXCEPTION"
    SERVICE_QUOTA_EXCEEDED_EXCEPTION = "SERVICE_QUOTA_EXCEEDED_EXCEPTION"
    THROTTLING_EXCEPTION = "THROTTLING_EXCEPTION"
    VALIDATION_EXCEPTION = "VALIDATION_EXCEPTION"


class DataSourceRunStatus:
    """DataSourceRunStatus enum values."""

    REQUESTED = "REQUESTED"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"
    SUCCESS = "SUCCESS"


class DataSourceRunType:
    """DataSourceRunType enum values."""

    PRIORITIZED = "PRIORITIZED"
    SCHEDULED = "SCHEDULED"


class DataSourceStatus:
    """DataSourceStatus enum values."""

    CREATING = "CREATING"
    FAILED_CREATION = "FAILED_CREATION"
    READY = "READY"
    UPDATING = "UPDATING"
    FAILED_UPDATE = "FAILED_UPDATE"
    RUNNING = "RUNNING"
    DELETING = "DELETING"
    FAILED_DELETION = "FAILED_DELETION"


class DataZoneEntityType:
    """DataZoneEntityType enum values."""

    DOMAIN_UNIT = "DOMAIN_UNIT"


class DeploymentMode:
    """DeploymentMode enum values."""

    ON_CREATE = "ON_CREATE"
    ON_DEMAND = "ON_DEMAND"


class DeploymentStatus:
    """DeploymentStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    PENDING_DEPLOYMENT = "PENDING_DEPLOYMENT"


class DeploymentType:
    """DeploymentType enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class DomainStatus:
    """DomainStatus enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATION_FAILED = "CREATION_FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETION_FAILED = "DELETION_FAILED"


class DomainUnitDesignation:
    """DomainUnitDesignation enum values."""

    OWNER = "OWNER"


class DomainVersion:
    """DomainVersion enum values."""

    V1 = "V1"
    V2 = "V2"


class EdgeDirection:
    """EdgeDirection enum values."""

    UPSTREAM = "UPSTREAM"
    DOWNSTREAM = "DOWNSTREAM"


class EnableSetting:
    """EnableSetting enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EntityType:
    """EntityType enum values."""

    ASSET = "ASSET"
    DATA_PRODUCT = "DATA_PRODUCT"


class EnvironmentStatus:
    """EnvironmentStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    VALIDATION_FAILED = "VALIDATION_FAILED"
    SUSPENDED = "SUSPENDED"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"
    DELETED = "DELETED"
    INACCESSIBLE = "INACCESSIBLE"


class FilterExpressionType:
    """FilterExpressionType enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class FilterStatus:
    """FilterStatus enum values."""

    VALID = "VALID"
    INVALID = "INVALID"


class FormTypeStatus:
    """FormTypeStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GlossaryStatus:
    """GlossaryStatus enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class GlossaryTermStatus:
    """GlossaryTermStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GlossaryUsageRestriction:
    """GlossaryUsageRestriction enum values."""

    ASSET_GOVERNED_TERMS = "ASSET_GOVERNED_TERMS"


class GlueConnectionType:
    """GlueConnectionType enum values."""

    SNOWFLAKE = "SNOWFLAKE"
    BIGQUERY = "BIGQUERY"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    MYSQL = "MYSQL"
    OPENSEARCH = "OPENSEARCH"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    REDSHIFT = "REDSHIFT"
    SAPHANA = "SAPHANA"
    SQLSERVER = "SQLSERVER"
    TERADATA = "TERADATA"
    VERTICA = "VERTICA"


class GovernanceType:
    """GovernanceType enum values."""

    AWS_MANAGED = "AWS_MANAGED"
    USER_MANAGED = "USER_MANAGED"


class GovernedEntityType:
    """GovernedEntityType enum values."""

    ASSET = "ASSET"


class GroupProfileStatus:
    """GroupProfileStatus enum values."""

    ASSIGNED = "ASSIGNED"
    NOT_ASSIGNED = "NOT_ASSIGNED"


class GroupSearchType:
    """GroupSearchType enum values."""

    SSO_GROUP = "SSO_GROUP"
    DATAZONE_SSO_GROUP = "DATAZONE_SSO_GROUP"


class HyperPodOrchestrator:
    """HyperPodOrchestrator enum values."""

    EKS = "EKS"
    SLURM = "SLURM"


class InventorySearchScope:
    """InventorySearchScope enum values."""

    ASSET = "ASSET"
    GLOSSARY = "GLOSSARY"
    GLOSSARY_TERM = "GLOSSARY_TERM"
    DATA_PRODUCT = "DATA_PRODUCT"


class JobRunMode:
    """JobRunMode enum values."""

    SCHEDULED = "SCHEDULED"
    ON_DEMAND = "ON_DEMAND"


class JobRunStatus:
    """JobRunStatus enum values."""

    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"
    FAILED = "FAILED"
    ABORTED = "ABORTED"
    TIMED_OUT = "TIMED_OUT"
    CANCELED = "CANCELED"


class JobType:
    """JobType enum values."""

    LINEAGE = "LINEAGE"


class LineageEventProcessingStatus:
    """LineageEventProcessingStatus enum values."""

    REQUESTED = "REQUESTED"
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class LineageImportStatus:
    """LineageImportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"


class ListingStatus:
    """ListingStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ManagedPolicyType:
    """ManagedPolicyType enum values."""

    CREATE_DOMAIN_UNIT = "CREATE_DOMAIN_UNIT"
    OVERRIDE_DOMAIN_UNIT_OWNERS = "OVERRIDE_DOMAIN_UNIT_OWNERS"
    ADD_TO_PROJECT_MEMBER_POOL = "ADD_TO_PROJECT_MEMBER_POOL"
    OVERRIDE_PROJECT_OWNERS = "OVERRIDE_PROJECT_OWNERS"
    CREATE_GLOSSARY = "CREATE_GLOSSARY"
    CREATE_FORM_TYPE = "CREATE_FORM_TYPE"
    CREATE_ASSET_TYPE = "CREATE_ASSET_TYPE"
    CREATE_PROJECT = "CREATE_PROJECT"
    CREATE_ENVIRONMENT_PROFILE = "CREATE_ENVIRONMENT_PROFILE"
    DELEGATE_CREATE_ENVIRONMENT_PROFILE = "DELEGATE_CREATE_ENVIRONMENT_PROFILE"
    CREATE_ENVIRONMENT = "CREATE_ENVIRONMENT"
    CREATE_ENVIRONMENT_FROM_BLUEPRINT = "CREATE_ENVIRONMENT_FROM_BLUEPRINT"
    CREATE_PROJECT_FROM_PROJECT_PROFILE = "CREATE_PROJECT_FROM_PROJECT_PROFILE"
    USE_ASSET_TYPE = "USE_ASSET_TYPE"


class MetadataGenerationRunStatus:
    """MetadataGenerationRunStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELED = "CANCELED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"


class MetadataGenerationRunType:
    """MetadataGenerationRunType enum values."""

    BUSINESS_DESCRIPTIONS = "BUSINESS_DESCRIPTIONS"
    BUSINESS_NAMES = "BUSINESS_NAMES"
    BUSINESS_GLOSSARY_ASSOCIATIONS = "BUSINESS_GLOSSARY_ASSOCIATIONS"


class MetadataGenerationTargetType:
    """MetadataGenerationTargetType enum values."""

    ASSET = "ASSET"


class NotificationResourceType:
    """NotificationResourceType enum values."""

    PROJECT = "PROJECT"


class NotificationRole:
    """NotificationRole enum values."""

    PROJECT_OWNER = "PROJECT_OWNER"
    PROJECT_CONTRIBUTOR = "PROJECT_CONTRIBUTOR"
    PROJECT_VIEWER = "PROJECT_VIEWER"
    DOMAIN_OWNER = "DOMAIN_OWNER"
    PROJECT_SUBSCRIBER = "PROJECT_SUBSCRIBER"


class NotificationType:
    """NotificationType enum values."""

    TASK = "TASK"
    EVENT = "EVENT"


class OAuth2GrantType:
    """OAuth2GrantType enum values."""

    AUTHORIZATION_CODE = "AUTHORIZATION_CODE"
    CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"
    JWT_BEARER = "JWT_BEARER"


class OpenLineageRunState:
    """OpenLineageRunState enum values."""

    START = "START"
    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"
    ABORT = "ABORT"
    FAIL = "FAIL"
    OTHER = "OTHER"


class OverallDeploymentStatus:
    """OverallDeploymentStatus enum values."""

    PENDING_DEPLOYMENT = "PENDING_DEPLOYMENT"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED_VALIDATION = "FAILED_VALIDATION"
    FAILED_DEPLOYMENT = "FAILED_DEPLOYMENT"


class ProjectDesignation:
    """ProjectDesignation enum values."""

    OWNER = "OWNER"
    CONTRIBUTOR = "CONTRIBUTOR"
    PROJECT_CATALOG_STEWARD = "PROJECT_CATALOG_STEWARD"


class ProjectStatus:
    """ProjectStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    MOVING = "MOVING"


class Protocol:
    """Protocol enum values."""

    ATHENA = "ATHENA"
    GLUE_INTERACTIVE_SESSION = "GLUE_INTERACTIVE_SESSION"
    HTTPS = "HTTPS"
    JDBC = "JDBC"
    LIVY = "LIVY"
    ODBC = "ODBC"
    PRISM = "PRISM"


class RejectRuleBehavior:
    """RejectRuleBehavior enum values."""

    ALL = "ALL"
    NONE = "NONE"


class ResolutionStrategy:
    """ResolutionStrategy enum values."""

    MANUAL = "MANUAL"


class ResourceTagSource:
    """ResourceTagSource enum values."""

    PROJECT = "PROJECT"
    PROJECT_PROFILE = "PROJECT_PROFILE"


class RuleAction:
    """RuleAction enum values."""

    CREATE_LISTING_CHANGE_SET = "CREATE_LISTING_CHANGE_SET"
    CREATE_SUBSCRIPTION_REQUEST = "CREATE_SUBSCRIPTION_REQUEST"


class RuleScopeSelectionMode:
    """RuleScopeSelectionMode enum values."""

    ALL = "ALL"
    SPECIFIC = "SPECIFIC"


class RuleTargetType:
    """RuleTargetType enum values."""

    DOMAIN_UNIT = "DOMAIN_UNIT"


class RuleType:
    """RuleType enum values."""

    METADATA_FORM_ENFORCEMENT = "METADATA_FORM_ENFORCEMENT"
    GLOSSARY_TERM_ENFORCEMENT = "GLOSSARY_TERM_ENFORCEMENT"


class S3Permission:
    """S3Permission enum values."""

    READ = "READ"
    WRITE = "WRITE"


class SearchOutputAdditionalAttribute:
    """SearchOutputAdditionalAttribute enum values."""

    FORMS = "FORMS"
    TIME_SERIES_DATA_POINT_FORMS = "TIME_SERIES_DATA_POINT_FORMS"
    TEXT_MATCH_RATIONALE = "TEXT_MATCH_RATIONALE"


class SelfGrantStatus:
    """SelfGrantStatus enum values."""

    GRANT_PENDING = "GRANT_PENDING"
    REVOKE_PENDING = "REVOKE_PENDING"
    GRANT_IN_PROGRESS = "GRANT_IN_PROGRESS"
    REVOKE_IN_PROGRESS = "REVOKE_IN_PROGRESS"
    GRANTED = "GRANTED"
    GRANT_FAILED = "GRANT_FAILED"
    REVOKE_FAILED = "REVOKE_FAILED"


class SortFieldAccountPool:
    """SortFieldAccountPool enum values."""

    NAME = "NAME"


class SortFieldConnection:
    """SortFieldConnection enum values."""

    NAME = "NAME"


class SortFieldProject:
    """SortFieldProject enum values."""

    NAME = "NAME"


class SortKey:
    """SortKey enum values."""

    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Status:
    """Status enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SubscriptionGrantOverallStatus:
    """SubscriptionGrantOverallStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    GRANT_FAILED = "GRANT_FAILED"
    REVOKE_FAILED = "REVOKE_FAILED"
    GRANT_AND_REVOKE_FAILED = "GRANT_AND_REVOKE_FAILED"
    COMPLETED = "COMPLETED"
    INACCESSIBLE = "INACCESSIBLE"


class SubscriptionGrantStatus:
    """SubscriptionGrantStatus enum values."""

    GRANT_PENDING = "GRANT_PENDING"
    REVOKE_PENDING = "REVOKE_PENDING"
    GRANT_IN_PROGRESS = "GRANT_IN_PROGRESS"
    REVOKE_IN_PROGRESS = "REVOKE_IN_PROGRESS"
    GRANTED = "GRANTED"
    REVOKED = "REVOKED"
    GRANT_FAILED = "GRANT_FAILED"
    REVOKE_FAILED = "REVOKE_FAILED"


class SubscriptionRequestStatus:
    """SubscriptionRequestStatus enum values."""

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


class SubscriptionStatus:
    """SubscriptionStatus enum values."""

    APPROVED = "APPROVED"
    REVOKED = "REVOKED"
    CANCELLED = "CANCELLED"


class TargetEntityType:
    """TargetEntityType enum values."""

    DOMAIN_UNIT = "DOMAIN_UNIT"
    ENVIRONMENT_BLUEPRINT_CONFIGURATION = "ENVIRONMENT_BLUEPRINT_CONFIGURATION"
    ENVIRONMENT_PROFILE = "ENVIRONMENT_PROFILE"
    ASSET_TYPE = "ASSET_TYPE"


class TaskStatus:
    """TaskStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TimeSeriesEntityType:
    """TimeSeriesEntityType enum values."""

    ASSET = "ASSET"
    LISTING = "LISTING"


class Timezone:
    """Timezone enum values."""

    UTC = "UTC"
    AFRICA_JOHANNESBURG = "AFRICA_JOHANNESBURG"
    AMERICA_MONTREAL = "AMERICA_MONTREAL"
    AMERICA_SAO_PAULO = "AMERICA_SAO_PAULO"
    ASIA_BAHRAIN = "ASIA_BAHRAIN"
    ASIA_BANGKOK = "ASIA_BANGKOK"
    ASIA_CALCUTTA = "ASIA_CALCUTTA"
    ASIA_DUBAI = "ASIA_DUBAI"
    ASIA_HONG_KONG = "ASIA_HONG_KONG"
    ASIA_JAKARTA = "ASIA_JAKARTA"
    ASIA_KUALA_LUMPUR = "ASIA_KUALA_LUMPUR"
    ASIA_SEOUL = "ASIA_SEOUL"
    ASIA_SHANGHAI = "ASIA_SHANGHAI"
    ASIA_SINGAPORE = "ASIA_SINGAPORE"
    ASIA_TAIPEI = "ASIA_TAIPEI"
    ASIA_TOKYO = "ASIA_TOKYO"
    AUSTRALIA_MELBOURNE = "AUSTRALIA_MELBOURNE"
    AUSTRALIA_SYDNEY = "AUSTRALIA_SYDNEY"
    CANADA_CENTRAL = "CANADA_CENTRAL"
    CET = "CET"
    CST6CDT = "CST6CDT"
    ETC_GMT = "ETC_GMT"
    ETC_GMT0 = "ETC_GMT0"
    ETC_GMT_ADD_0 = "ETC_GMT_ADD_0"
    ETC_GMT_ADD_1 = "ETC_GMT_ADD_1"
    ETC_GMT_ADD_10 = "ETC_GMT_ADD_10"
    ETC_GMT_ADD_11 = "ETC_GMT_ADD_11"
    ETC_GMT_ADD_12 = "ETC_GMT_ADD_12"
    ETC_GMT_ADD_2 = "ETC_GMT_ADD_2"
    ETC_GMT_ADD_3 = "ETC_GMT_ADD_3"
    ETC_GMT_ADD_4 = "ETC_GMT_ADD_4"
    ETC_GMT_ADD_5 = "ETC_GMT_ADD_5"
    ETC_GMT_ADD_6 = "ETC_GMT_ADD_6"
    ETC_GMT_ADD_7 = "ETC_GMT_ADD_7"
    ETC_GMT_ADD_8 = "ETC_GMT_ADD_8"
    ETC_GMT_ADD_9 = "ETC_GMT_ADD_9"
    ETC_GMT_NEG_0 = "ETC_GMT_NEG_0"
    ETC_GMT_NEG_1 = "ETC_GMT_NEG_1"
    ETC_GMT_NEG_10 = "ETC_GMT_NEG_10"
    ETC_GMT_NEG_11 = "ETC_GMT_NEG_11"
    ETC_GMT_NEG_12 = "ETC_GMT_NEG_12"
    ETC_GMT_NEG_13 = "ETC_GMT_NEG_13"
    ETC_GMT_NEG_14 = "ETC_GMT_NEG_14"
    ETC_GMT_NEG_2 = "ETC_GMT_NEG_2"
    ETC_GMT_NEG_3 = "ETC_GMT_NEG_3"
    ETC_GMT_NEG_4 = "ETC_GMT_NEG_4"
    ETC_GMT_NEG_5 = "ETC_GMT_NEG_5"
    ETC_GMT_NEG_6 = "ETC_GMT_NEG_6"
    ETC_GMT_NEG_7 = "ETC_GMT_NEG_7"
    ETC_GMT_NEG_8 = "ETC_GMT_NEG_8"
    ETC_GMT_NEG_9 = "ETC_GMT_NEG_9"
    EUROPE_DUBLIN = "EUROPE_DUBLIN"
    EUROPE_LONDON = "EUROPE_LONDON"
    EUROPE_PARIS = "EUROPE_PARIS"
    EUROPE_STOCKHOLM = "EUROPE_STOCKHOLM"
    EUROPE_ZURICH = "EUROPE_ZURICH"
    ISRAEL = "ISRAEL"
    MEXICO_GENERAL = "MEXICO_GENERAL"
    MST7MDT = "MST7MDT"
    PACIFIC_AUCKLAND = "PACIFIC_AUCKLAND"
    US_CENTRAL = "US_CENTRAL"
    US_EASTERN = "US_EASTERN"
    US_MOUNTAIN = "US_MOUNTAIN"
    US_PACIFIC = "US_PACIFIC"


class TypesSearchScope:
    """TypesSearchScope enum values."""

    ASSET_TYPE = "ASSET_TYPE"
    FORM_TYPE = "FORM_TYPE"
    LINEAGE_NODE_TYPE = "LINEAGE_NODE_TYPE"


class UserAssignment:
    """UserAssignment enum values."""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"


class UserDesignation:
    """UserDesignation enum values."""

    PROJECT_OWNER = "PROJECT_OWNER"
    PROJECT_CONTRIBUTOR = "PROJECT_CONTRIBUTOR"
    PROJECT_CATALOG_VIEWER = "PROJECT_CATALOG_VIEWER"
    PROJECT_CATALOG_CONSUMER = "PROJECT_CATALOG_CONSUMER"
    PROJECT_CATALOG_STEWARD = "PROJECT_CATALOG_STEWARD"


class UserProfileStatus:
    """UserProfileStatus enum values."""

    ASSIGNED = "ASSIGNED"
    NOT_ASSIGNED = "NOT_ASSIGNED"
    ACTIVATED = "ACTIVATED"
    DEACTIVATED = "DEACTIVATED"


class UserProfileType:
    """UserProfileType enum values."""

    IAM = "IAM"
    SSO = "SSO"


class UserSearchType:
    """UserSearchType enum values."""

    SSO_USER = "SSO_USER"
    DATAZONE_USER = "DATAZONE_USER"
    DATAZONE_SSO_USER = "DATAZONE_SSO_USER"
    DATAZONE_IAM_USER = "DATAZONE_IAM_USER"


class UserType:
    """UserType enum values."""

    IAM_USER = "IAM_USER"
    IAM_ROLE = "IAM_ROLE"
    SSO_USER = "SSO_USER"


@dataclass
class AmazonQPropertiesInput(PropertyType):
    IS_ENABLED = "IsEnabled"
    PROFILE_ARN = "ProfileArn"
    AUTH_MODE = "AuthMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
        "profile_arn": "ProfileArn",
        "auth_mode": "AuthMode",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AthenaPropertiesInput(PropertyType):
    WORKGROUP_NAME = "WorkgroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_name": "WorkgroupName",
    }

    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthenticationConfigurationInput(PropertyType):
    SECRET_ARN = "SecretArn"
    KMS_KEY_ARN = "KmsKeyArn"
    O_AUTH2_PROPERTIES = "OAuth2Properties"
    CUSTOM_AUTHENTICATION_CREDENTIALS = "CustomAuthenticationCredentials"
    BASIC_AUTHENTICATION_CREDENTIALS = "BasicAuthenticationCredentials"
    AUTHENTICATION_TYPE = "AuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "kms_key_arn": "KmsKeyArn",
        "o_auth2_properties": "OAuth2Properties",
        "custom_authentication_credentials": "CustomAuthenticationCredentials",
        "basic_authentication_credentials": "BasicAuthenticationCredentials",
        "authentication_type": "AuthenticationType",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_properties: Optional[OAuth2Properties] = None
    custom_authentication_credentials: Optional[dict[str, str]] = None
    basic_authentication_credentials: Optional[BasicAuthenticationCredentials] = None
    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    AUTHORIZATION_CODE = "AuthorizationCode"
    REDIRECT_URI = "RedirectUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_code": "AuthorizationCode",
        "redirect_uri": "RedirectUri",
    }

    authorization_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsLocation(PropertyType):
    AWS_REGION = "AwsRegion"
    ACCESS_ROLE = "AccessRole"
    AWS_ACCOUNT_ID = "AwsAccountId"
    IAM_CONNECTION_ID = "IamConnectionId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AwsRegion",
        "access_role": "AccessRole",
        "aws_account_id": "AwsAccountId",
        "iam_connection_id": "IamConnectionId",
    }

    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_connection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    USER_NAME = "UserName"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_name": "UserName",
        "password": "Password",
    }

    user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionPropertiesInput(PropertyType):
    AMAZON_Q_PROPERTIES = "AmazonQProperties"
    IAM_PROPERTIES = "IamProperties"
    S3_PROPERTIES = "S3Properties"
    SPARK_EMR_PROPERTIES = "SparkEmrProperties"
    HYPER_POD_PROPERTIES = "HyperPodProperties"
    SPARK_GLUE_PROPERTIES = "SparkGlueProperties"
    MLFLOW_PROPERTIES = "MlflowProperties"
    ATHENA_PROPERTIES = "AthenaProperties"
    GLUE_PROPERTIES = "GlueProperties"
    REDSHIFT_PROPERTIES = "RedshiftProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amazon_q_properties": "AmazonQProperties",
        "iam_properties": "IamProperties",
        "s3_properties": "S3Properties",
        "spark_emr_properties": "SparkEmrProperties",
        "hyper_pod_properties": "HyperPodProperties",
        "spark_glue_properties": "SparkGlueProperties",
        "mlflow_properties": "MlflowProperties",
        "athena_properties": "AthenaProperties",
        "glue_properties": "GlueProperties",
        "redshift_properties": "RedshiftProperties",
    }

    amazon_q_properties: Optional[AmazonQPropertiesInput] = None
    iam_properties: Optional[IamPropertiesInput] = None
    s3_properties: Optional[S3PropertiesInput] = None
    spark_emr_properties: Optional[SparkEmrPropertiesInput] = None
    hyper_pod_properties: Optional[HyperPodPropertiesInput] = None
    spark_glue_properties: Optional[SparkGluePropertiesInput] = None
    mlflow_properties: Optional[MlflowPropertiesInput] = None
    athena_properties: Optional[AthenaPropertiesInput] = None
    glue_properties: Optional[GluePropertiesInput] = None
    redshift_properties: Optional[RedshiftPropertiesInput] = None


@dataclass
class GlueConnectionInput(PropertyType):
    PYTHON_PROPERTIES = "PythonProperties"
    AUTHENTICATION_CONFIGURATION = "AuthenticationConfiguration"
    SPARK_PROPERTIES = "SparkProperties"
    DESCRIPTION = "Description"
    CONNECTION_TYPE = "ConnectionType"
    MATCH_CRITERIA = "MatchCriteria"
    PHYSICAL_CONNECTION_REQUIREMENTS = "PhysicalConnectionRequirements"
    CONNECTION_PROPERTIES = "ConnectionProperties"
    ATHENA_PROPERTIES = "AthenaProperties"
    VALIDATE_FOR_COMPUTE_ENVIRONMENTS = "ValidateForComputeEnvironments"
    VALIDATE_CREDENTIALS = "ValidateCredentials"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "python_properties": "PythonProperties",
        "authentication_configuration": "AuthenticationConfiguration",
        "spark_properties": "SparkProperties",
        "description": "Description",
        "connection_type": "ConnectionType",
        "match_criteria": "MatchCriteria",
        "physical_connection_requirements": "PhysicalConnectionRequirements",
        "connection_properties": "ConnectionProperties",
        "athena_properties": "AthenaProperties",
        "validate_for_compute_environments": "ValidateForComputeEnvironments",
        "validate_credentials": "ValidateCredentials",
        "name": "Name",
    }

    python_properties: Optional[dict[str, str]] = None
    authentication_configuration: Optional[AuthenticationConfigurationInput] = None
    spark_properties: Optional[dict[str, str]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None
    physical_connection_requirements: Optional[PhysicalConnectionRequirements] = None
    connection_properties: Optional[dict[str, str]] = None
    athena_properties: Optional[dict[str, str]] = None
    validate_for_compute_environments: Optional[Union[list[str], Ref]] = None
    validate_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GlueOAuth2Credentials(PropertyType):
    USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET = "UserManagedClientApplicationClientSecret"
    JWT_TOKEN = "JwtToken"
    REFRESH_TOKEN = "RefreshToken"
    ACCESS_TOKEN = "AccessToken"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_managed_client_application_client_secret": "UserManagedClientApplicationClientSecret",
        "jwt_token": "JwtToken",
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
    }

    user_managed_client_application_client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    jwt_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GluePropertiesInput(PropertyType):
    GLUE_CONNECTION_INPUT = "GlueConnectionInput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_connection_input": "GlueConnectionInput",
    }

    glue_connection_input: Optional[GlueConnectionInput] = None


@dataclass
class HyperPodPropertiesInput(PropertyType):
    CLUSTER_NAME = "ClusterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_name": "ClusterName",
    }

    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamPropertiesInput(PropertyType):
    GLUE_LINEAGE_SYNC_ENABLED = "GlueLineageSyncEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_lineage_sync_enabled": "GlueLineageSyncEnabled",
    }

    glue_lineage_sync_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LineageSyncSchedule(PropertyType):
    SCHEDULE = "Schedule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule": "Schedule",
    }

    schedule: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MlflowPropertiesInput(PropertyType):
    TRACKING_SERVER_ARN = "TrackingServerArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tracking_server_arn": "TrackingServerArn",
    }

    tracking_server_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2ClientApplication(PropertyType):
    AWS_MANAGED_CLIENT_APPLICATION_REFERENCE = "AWSManagedClientApplicationReference"
    USER_MANAGED_CLIENT_APPLICATION_CLIENT_ID = "UserManagedClientApplicationClientId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
        "user_managed_client_application_client_id": "UserManagedClientApplicationClientId",
    }

    aws_managed_client_application_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_managed_client_application_client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Properties(PropertyType):
    AUTHORIZATION_CODE_PROPERTIES = "AuthorizationCodeProperties"
    O_AUTH2_CLIENT_APPLICATION = "OAuth2ClientApplication"
    TOKEN_URL = "TokenUrl"
    O_AUTH2_CREDENTIALS = "OAuth2Credentials"
    O_AUTH2_GRANT_TYPE = "OAuth2GrantType"
    TOKEN_URL_PARAMETERS_MAP = "TokenUrlParametersMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_code_properties": "AuthorizationCodeProperties",
        "o_auth2_client_application": "OAuth2ClientApplication",
        "token_url": "TokenUrl",
        "o_auth2_credentials": "OAuth2Credentials",
        "o_auth2_grant_type": "OAuth2GrantType",
        "token_url_parameters_map": "TokenUrlParametersMap",
    }

    authorization_code_properties: Optional[AuthorizationCodeProperties] = None
    o_auth2_client_application: Optional[OAuth2ClientApplication] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_credentials: Optional[GlueOAuth2Credentials] = None
    o_auth2_grant_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_url_parameters_map: Optional[dict[str, str]] = None


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    SUBNET_ID_LIST = "SubnetIdList"
    AVAILABILITY_ZONE = "AvailabilityZone"
    SECURITY_GROUP_ID_LIST = "SecurityGroupIdList"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_id_list": "SubnetIdList",
        "availability_zone": "AvailabilityZone",
        "security_group_id_list": "SecurityGroupIdList",
        "subnet_id": "SubnetId",
    }

    subnet_id_list: Optional[Union[list[str], Ref]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_id_list: Optional[Union[list[str], Ref]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftCredentials(PropertyType):
    SECRET_ARN = "SecretArn"
    USERNAME_PASSWORD = "UsernamePassword"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "username_password": "UsernamePassword",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password: Optional[UsernamePassword] = None


@dataclass
class RedshiftLineageSyncConfigurationInput(PropertyType):
    SCHEDULE = "Schedule"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule": "Schedule",
        "enabled": "Enabled",
    }

    schedule: Optional[LineageSyncSchedule] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftPropertiesInput(PropertyType):
    STORAGE = "Storage"
    PORT = "Port"
    DATABASE_NAME = "DatabaseName"
    HOST = "Host"
    CREDENTIALS = "Credentials"
    LINEAGE_SYNC = "LineageSync"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage": "Storage",
        "port": "Port",
        "database_name": "DatabaseName",
        "host": "Host",
        "credentials": "Credentials",
        "lineage_sync": "LineageSync",
    }

    storage: Optional[RedshiftStorageProperties] = None
    port: Optional[Union[float, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials: Optional[RedshiftCredentials] = None
    lineage_sync: Optional[RedshiftLineageSyncConfigurationInput] = None


@dataclass
class RedshiftStorageProperties(PropertyType):
    CLUSTER_NAME = "ClusterName"
    WORKGROUP_NAME = "WorkgroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_name": "ClusterName",
        "workgroup_name": "WorkgroupName",
    }

    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3PropertiesInput(PropertyType):
    S3_URI = "S3Uri"
    S3_ACCESS_GRANT_LOCATION_ID = "S3AccessGrantLocationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "s3_access_grant_location_id": "S3AccessGrantLocationId",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_access_grant_location_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SparkEmrPropertiesInput(PropertyType):
    COMPUTE_ARN = "ComputeArn"
    TRUSTED_CERTIFICATES_S3_URI = "TrustedCertificatesS3Uri"
    LOG_URI = "LogUri"
    JAVA_VIRTUAL_ENV = "JavaVirtualEnv"
    PYTHON_VIRTUAL_ENV = "PythonVirtualEnv"
    RUNTIME_ROLE = "RuntimeRole"
    INSTANCE_PROFILE_ARN = "InstanceProfileArn"
    MANAGED_ENDPOINT_ARN = "ManagedEndpointArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_arn": "ComputeArn",
        "trusted_certificates_s3_uri": "TrustedCertificatesS3Uri",
        "log_uri": "LogUri",
        "java_virtual_env": "JavaVirtualEnv",
        "python_virtual_env": "PythonVirtualEnv",
        "runtime_role": "RuntimeRole",
        "instance_profile_arn": "InstanceProfileArn",
        "managed_endpoint_arn": "ManagedEndpointArn",
    }

    compute_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trusted_certificates_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    java_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    python_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_endpoint_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SparkGlueArgs(PropertyType):
    CONNECTION = "Connection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection": "Connection",
    }

    connection: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SparkGluePropertiesInput(PropertyType):
    WORKER_TYPE = "WorkerType"
    ADDITIONAL_ARGS = "AdditionalArgs"
    JAVA_VIRTUAL_ENV = "JavaVirtualEnv"
    GLUE_VERSION = "GlueVersion"
    PYTHON_VIRTUAL_ENV = "PythonVirtualEnv"
    IDLE_TIMEOUT = "IdleTimeout"
    GLUE_CONNECTION_NAME = "GlueConnectionName"
    NUMBER_OF_WORKERS = "NumberOfWorkers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "worker_type": "WorkerType",
        "additional_args": "AdditionalArgs",
        "java_virtual_env": "JavaVirtualEnv",
        "glue_version": "GlueVersion",
        "python_virtual_env": "PythonVirtualEnv",
        "idle_timeout": "IdleTimeout",
        "glue_connection_name": "GlueConnectionName",
        "number_of_workers": "NumberOfWorkers",
    }

    worker_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_args: Optional[SparkGlueArgs] = None
    java_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    glue_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    python_virtual_env: Optional[Union[str, Ref, GetAtt, Sub]] = None
    idle_timeout: Optional[Union[float, Ref, GetAtt, Sub]] = None
    glue_connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    number_of_workers: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class UsernamePassword(PropertyType):
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None

