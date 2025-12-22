"""PropertyTypes for AWS::CleanRooms::PrivacyBudgetTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessBudgetType:
    """AccessBudgetType enum values."""

    CALENDAR_DAY = "CALENDAR_DAY"
    CALENDAR_MONTH = "CALENDAR_MONTH"
    CALENDAR_WEEK = "CALENDAR_WEEK"
    LIFETIME = "LIFETIME"


class AccessDeniedExceptionReason:
    """AccessDeniedExceptionReason enum values."""

    INSUFFICIENT_PERMISSIONS = "INSUFFICIENT_PERMISSIONS"


class AdditionalAnalyses:
    """AdditionalAnalyses enum values."""

    ALLOWED = "ALLOWED"
    REQUIRED = "REQUIRED"
    NOT_ALLOWED = "NOT_ALLOWED"


class AggregateFunctionName:
    """AggregateFunctionName enum values."""

    SUM = "SUM"
    SUM_DISTINCT = "SUM_DISTINCT"
    COUNT = "COUNT"
    COUNT_DISTINCT = "COUNT_DISTINCT"
    AVG = "AVG"


class AggregationType:
    """AggregationType enum values."""

    COUNT_DISTINCT = "COUNT_DISTINCT"


class AnalysisFormat:
    """AnalysisFormat enum values."""

    SQL = "SQL"
    PYSPARK_1_0 = "PYSPARK_1_0"


class AnalysisMethod:
    """AnalysisMethod enum values."""

    DIRECT_QUERY = "DIRECT_QUERY"
    DIRECT_JOB = "DIRECT_JOB"
    MULTIPLE = "MULTIPLE"


class AnalysisRuleType:
    """AnalysisRuleType enum values."""

    AGGREGATION = "AGGREGATION"
    LIST = "LIST"
    CUSTOM = "CUSTOM"
    ID_MAPPING_TABLE = "ID_MAPPING_TABLE"


class AnalysisTemplateValidationStatus:
    """AnalysisTemplateValidationStatus enum values."""

    VALID = "VALID"
    INVALID = "INVALID"
    UNABLE_TO_VALIDATE = "UNABLE_TO_VALIDATE"


class AnalysisTemplateValidationType:
    """AnalysisTemplateValidationType enum values."""

    DIFFERENTIAL_PRIVACY = "DIFFERENTIAL_PRIVACY"


class AnalysisType:
    """AnalysisType enum values."""

    DIRECT_ANALYSIS = "DIRECT_ANALYSIS"
    ADDITIONAL_ANALYSIS = "ADDITIONAL_ANALYSIS"


class AnalyticsEngine:
    """AnalyticsEngine enum values."""

    SPARK = "SPARK"
    CLEAN_ROOMS_SQL = "CLEAN_ROOMS_SQL"


class AutoApprovedChangeType:
    """AutoApprovedChangeType enum values."""

    ADD_MEMBER = "ADD_MEMBER"


class AutoRefreshMode:
    """AutoRefreshMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ChangeRequestStatus:
    """ChangeRequestStatus enum values."""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    DENIED = "DENIED"
    COMMITTED = "COMMITTED"


class ChangeSpecificationType:
    """ChangeSpecificationType enum values."""

    MEMBER = "MEMBER"


class ChangeType:
    """ChangeType enum values."""

    ADD_MEMBER = "ADD_MEMBER"


class CollaborationJobLogStatus:
    """CollaborationJobLogStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CollaborationQueryLogStatus:
    """CollaborationQueryLogStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CommercialRegion:
    """CommercialRegion enum values."""

    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    AF_SOUTH_1 = "af-south-1"
    AP_EAST_1 = "ap-east-1"
    AP_SOUTH_2 = "ap-south-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_SOUTHEAST_5 = "ap-southeast-5"
    AP_SOUTHEAST_4 = "ap-southeast-4"
    AP_SOUTHEAST_7 = "ap-southeast-7"
    AP_SOUTH_1 = "ap-south-1"
    AP_NORTHEAST_3 = "ap-northeast-3"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    CA_CENTRAL_1 = "ca-central-1"
    CA_WEST_1 = "ca-west-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_WEST_3 = "eu-west-3"
    EU_SOUTH_2 = "eu-south-2"
    EU_CENTRAL_2 = "eu-central-2"
    EU_CENTRAL_1 = "eu-central-1"
    EU_NORTH_1 = "eu-north-1"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    ME_SOUTH_1 = "me-south-1"
    ME_CENTRAL_1 = "me-central-1"
    IL_CENTRAL_1 = "il-central-1"
    SA_EAST_1 = "sa-east-1"
    MX_CENTRAL_1 = "mx-central-1"
    AP_EAST_2 = "ap-east-2"


class ConfiguredTableAnalysisRuleType:
    """ConfiguredTableAnalysisRuleType enum values."""

    AGGREGATION = "AGGREGATION"
    LIST = "LIST"
    CUSTOM = "CUSTOM"


class ConfiguredTableAssociationAnalysisRuleType:
    """ConfiguredTableAssociationAnalysisRuleType enum values."""

    AGGREGATION = "AGGREGATION"
    LIST = "LIST"
    CUSTOM = "CUSTOM"


class ConflictExceptionReason:
    """ConflictExceptionReason enum values."""

    ALREADY_EXISTS = "ALREADY_EXISTS"
    SUBRESOURCES_EXIST = "SUBRESOURCES_EXIST"
    INVALID_STATE = "INVALID_STATE"


class CustomMLMemberAbility:
    """CustomMLMemberAbility enum values."""

    CAN_RECEIVE_MODEL_OUTPUT = "CAN_RECEIVE_MODEL_OUTPUT"
    CAN_RECEIVE_INFERENCE_OUTPUT = "CAN_RECEIVE_INFERENCE_OUTPUT"


class DifferentialPrivacyAggregationType:
    """DifferentialPrivacyAggregationType enum values."""

    AVG = "AVG"
    COUNT = "COUNT"
    COUNT_DISTINCT = "COUNT_DISTINCT"
    SUM = "SUM"
    STDDEV = "STDDEV"


class ErrorMessageType:
    """ErrorMessageType enum values."""

    DETAILED = "DETAILED"


class FilterableMemberStatus:
    """FilterableMemberStatus enum values."""

    INVITED = "INVITED"
    ACTIVE = "ACTIVE"


class IdNamespaceType:
    """IdNamespaceType enum values."""

    SOURCE = "SOURCE"
    TARGET = "TARGET"


class JobType:
    """JobType enum values."""

    BATCH = "BATCH"
    INCREMENTAL = "INCREMENTAL"
    DELETE_ONLY = "DELETE_ONLY"


class JoinOperator:
    """JoinOperator enum values."""

    OR = "OR"
    AND = "AND"


class JoinRequiredOption:
    """JoinRequiredOption enum values."""

    QUERY_RUNNER = "QUERY_RUNNER"


class MemberAbility:
    """MemberAbility enum values."""

    CAN_QUERY = "CAN_QUERY"
    CAN_RECEIVE_RESULTS = "CAN_RECEIVE_RESULTS"
    CAN_RUN_JOB = "CAN_RUN_JOB"


class MemberStatus:
    """MemberStatus enum values."""

    INVITED = "INVITED"
    ACTIVE = "ACTIVE"
    LEFT = "LEFT"
    REMOVED = "REMOVED"


class MembershipJobLogStatus:
    """MembershipJobLogStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MembershipQueryLogStatus:
    """MembershipQueryLogStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MembershipStatus:
    """MembershipStatus enum values."""

    ACTIVE = "ACTIVE"
    REMOVED = "REMOVED"
    COLLABORATION_DELETED = "COLLABORATION_DELETED"


class ParameterType:
    """ParameterType enum values."""

    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    DECIMAL = "DECIMAL"
    REAL = "REAL"
    DOUBLE_PRECISION = "DOUBLE_PRECISION"
    BOOLEAN = "BOOLEAN"
    CHAR = "CHAR"
    VARCHAR = "VARCHAR"
    DATE = "DATE"
    TIMESTAMP = "TIMESTAMP"
    TIMESTAMPTZ = "TIMESTAMPTZ"
    TIME = "TIME"
    TIMETZ = "TIMETZ"
    VARBYTE = "VARBYTE"
    BINARY = "BINARY"
    BYTE = "BYTE"
    CHARACTER = "CHARACTER"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INT = "INT"
    LONG = "LONG"
    NUMERIC = "NUMERIC"
    SHORT = "SHORT"
    STRING = "STRING"
    TIMESTAMP_LTZ = "TIMESTAMP_LTZ"
    TIMESTAMP_NTZ = "TIMESTAMP_NTZ"
    TINYINT = "TINYINT"


class PrivacyBudgetTemplateAutoRefresh:
    """PrivacyBudgetTemplateAutoRefresh enum values."""

    CALENDAR_MONTH = "CALENDAR_MONTH"
    NONE = "NONE"


class PrivacyBudgetType:
    """PrivacyBudgetType enum values."""

    DIFFERENTIAL_PRIVACY = "DIFFERENTIAL_PRIVACY"
    ACCESS_BUDGET = "ACCESS_BUDGET"


class ProtectedJobAnalysisType:
    """ProtectedJobAnalysisType enum values."""

    DIRECT_ANALYSIS = "DIRECT_ANALYSIS"


class ProtectedJobStatus:
    """ProtectedJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    STARTED = "STARTED"
    CANCELLED = "CANCELLED"
    CANCELLING = "CANCELLING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class ProtectedJobType:
    """ProtectedJobType enum values."""

    PYSPARK = "PYSPARK"


class ProtectedJobWorkerComputeType:
    """ProtectedJobWorkerComputeType enum values."""

    CR_1X = "CR.1X"
    CR_4X = "CR.4X"


class ProtectedQueryStatus:
    """ProtectedQueryStatus enum values."""

    SUBMITTED = "SUBMITTED"
    STARTED = "STARTED"
    CANCELLED = "CANCELLED"
    CANCELLING = "CANCELLING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    TIMED_OUT = "TIMED_OUT"


class ProtectedQueryType:
    """ProtectedQueryType enum values."""

    SQL = "SQL"


class ResourceType:
    """ResourceType enum values."""

    CONFIGURED_TABLE = "CONFIGURED_TABLE"
    COLLABORATION = "COLLABORATION"
    MEMBERSHIP = "MEMBERSHIP"
    CONFIGURED_TABLE_ASSOCIATION = "CONFIGURED_TABLE_ASSOCIATION"


class ResultFormat:
    """ResultFormat enum values."""

    CSV = "CSV"
    PARQUET = "PARQUET"


class ScalarFunctions:
    """ScalarFunctions enum values."""

    ABS = "ABS"
    CAST = "CAST"
    CEILING = "CEILING"
    COALESCE = "COALESCE"
    CONVERT = "CONVERT"
    CURRENT_DATE = "CURRENT_DATE"
    DATEADD = "DATEADD"
    EXTRACT = "EXTRACT"
    FLOOR = "FLOOR"
    GETDATE = "GETDATE"
    LN = "LN"
    LOG = "LOG"
    LOWER = "LOWER"
    ROUND = "ROUND"
    RTRIM = "RTRIM"
    SQRT = "SQRT"
    SUBSTRING = "SUBSTRING"
    TO_CHAR = "TO_CHAR"
    TO_DATE = "TO_DATE"
    TO_NUMBER = "TO_NUMBER"
    TO_TIMESTAMP = "TO_TIMESTAMP"
    TRIM = "TRIM"
    TRUNC = "TRUNC"
    UPPER = "UPPER"


class SchemaConfiguration:
    """SchemaConfiguration enum values."""

    DIFFERENTIAL_PRIVACY = "DIFFERENTIAL_PRIVACY"


class SchemaStatus:
    """SchemaStatus enum values."""

    READY = "READY"
    NOT_READY = "NOT_READY"


class SchemaStatusReasonCode:
    """SchemaStatusReasonCode enum values."""

    ANALYSIS_RULE_MISSING = "ANALYSIS_RULE_MISSING"
    ANALYSIS_TEMPLATES_NOT_CONFIGURED = "ANALYSIS_TEMPLATES_NOT_CONFIGURED"
    ANALYSIS_PROVIDERS_NOT_CONFIGURED = "ANALYSIS_PROVIDERS_NOT_CONFIGURED"
    DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED = "DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED"
    ID_MAPPING_TABLE_NOT_POPULATED = "ID_MAPPING_TABLE_NOT_POPULATED"
    COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED = "COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED"
    ADDITIONAL_ANALYSES_NOT_CONFIGURED = "ADDITIONAL_ANALYSES_NOT_CONFIGURED"
    RESULT_RECEIVERS_NOT_CONFIGURED = "RESULT_RECEIVERS_NOT_CONFIGURED"
    ADDITIONAL_ANALYSES_NOT_ALLOWED = "ADDITIONAL_ANALYSES_NOT_ALLOWED"
    RESULT_RECEIVERS_NOT_ALLOWED = "RESULT_RECEIVERS_NOT_ALLOWED"
    ANALYSIS_RULE_TYPES_NOT_COMPATIBLE = "ANALYSIS_RULE_TYPES_NOT_COMPATIBLE"


class SchemaType:
    """SchemaType enum values."""

    TABLE = "TABLE"
    ID_MAPPING_TABLE = "ID_MAPPING_TABLE"


class SelectedAnalysisMethod:
    """SelectedAnalysisMethod enum values."""

    DIRECT_QUERY = "DIRECT_QUERY"
    DIRECT_JOB = "DIRECT_JOB"


class SupportedS3Region:
    """SupportedS3Region enum values."""

    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    AF_SOUTH_1 = "af-south-1"
    AP_EAST_1 = "ap-east-1"
    AP_EAST_2 = "ap-east-2"
    AP_SOUTH_2 = "ap-south-2"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_SOUTHEAST_3 = "ap-southeast-3"
    AP_SOUTHEAST_5 = "ap-southeast-5"
    AP_SOUTHEAST_4 = "ap-southeast-4"
    AP_SOUTHEAST_7 = "ap-southeast-7"
    AP_SOUTH_1 = "ap-south-1"
    AP_NORTHEAST_3 = "ap-northeast-3"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    CA_CENTRAL_1 = "ca-central-1"
    CA_WEST_1 = "ca-west-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_WEST_3 = "eu-west-3"
    EU_SOUTH_2 = "eu-south-2"
    EU_CENTRAL_2 = "eu-central-2"
    EU_CENTRAL_1 = "eu-central-1"
    EU_NORTH_1 = "eu-north-1"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    ME_SOUTH_1 = "me-south-1"
    ME_CENTRAL_1 = "me-central-1"
    IL_CENTRAL_1 = "il-central-1"
    SA_EAST_1 = "sa-east-1"
    MX_CENTRAL_1 = "mx-central-1"


class SyntheticDataColumnType:
    """SyntheticDataColumnType enum values."""

    CATEGORICAL = "CATEGORICAL"
    NUMERICAL = "NUMERICAL"


class TargetProtectedJobStatus:
    """TargetProtectedJobStatus enum values."""

    CANCELLED = "CANCELLED"


class TargetProtectedQueryStatus:
    """TargetProtectedQueryStatus enum values."""

    CANCELLED = "CANCELLED"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    INVALID_CONFIGURATION = "INVALID_CONFIGURATION"
    INVALID_QUERY = "INVALID_QUERY"
    IAM_SYNCHRONIZATION_DELAY = "IAM_SYNCHRONIZATION_DELAY"


class WorkerComputeType:
    """WorkerComputeType enum values."""

    CR_1X = "CR.1X"
    CR_4X = "CR.4X"


@dataclass
class BudgetParameter(PropertyType):
    TYPE = "Type"
    BUDGET = "Budget"
    AUTO_REFRESH = "AutoRefresh"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "budget": "Budget",
        "auto_refresh": "AutoRefresh",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    budget: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_refresh: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Parameters(PropertyType):
    RESOURCE_ARN = "ResourceArn"
    BUDGET_PARAMETERS = "BudgetParameters"
    EPSILON = "Epsilon"
    USERS_NOISE_PER_QUERY = "UsersNoisePerQuery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "budget_parameters": "BudgetParameters",
        "epsilon": "Epsilon",
        "users_noise_per_query": "UsersNoisePerQuery",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    budget_parameters: Optional[list[BudgetParameter]] = None
    epsilon: Optional[Union[int, Ref, GetAtt, Sub]] = None
    users_noise_per_query: Optional[Union[int, Ref, GetAtt, Sub]] = None

