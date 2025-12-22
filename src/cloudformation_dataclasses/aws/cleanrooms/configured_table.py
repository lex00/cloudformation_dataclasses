"""PropertyTypes for AWS::CleanRooms::ConfiguredTable."""

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
class AggregateColumn(PropertyType):
    FUNCTION = "Function"
    COLUMN_NAMES = "ColumnNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "column_names": "ColumnNames",
    }

    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class AggregationConstraint(PropertyType):
    COLUMN_NAME = "ColumnName"
    MINIMUM = "Minimum"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "minimum": "Minimum",
        "type_": "Type",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum: Optional[Union[float, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisRule(PropertyType):
    POLICY = "Policy"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
        "type_": "Type",
    }

    policy: Optional[ConfiguredTableAnalysisRulePolicy] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisRuleAggregation(PropertyType):
    ALLOWED_JOIN_OPERATORS = "AllowedJoinOperators"
    SCALAR_FUNCTIONS = "ScalarFunctions"
    ADDITIONAL_ANALYSES = "AdditionalAnalyses"
    OUTPUT_CONSTRAINTS = "OutputConstraints"
    DIMENSION_COLUMNS = "DimensionColumns"
    JOIN_COLUMNS = "JoinColumns"
    JOIN_REQUIRED = "JoinRequired"
    AGGREGATE_COLUMNS = "AggregateColumns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_join_operators": "AllowedJoinOperators",
        "scalar_functions": "ScalarFunctions",
        "additional_analyses": "AdditionalAnalyses",
        "output_constraints": "OutputConstraints",
        "dimension_columns": "DimensionColumns",
        "join_columns": "JoinColumns",
        "join_required": "JoinRequired",
        "aggregate_columns": "AggregateColumns",
    }

    allowed_join_operators: Optional[Union[list[str], Ref]] = None
    scalar_functions: Optional[Union[list[str], Ref]] = None
    additional_analyses: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_constraints: Optional[list[AggregationConstraint]] = None
    dimension_columns: Optional[Union[list[str], Ref]] = None
    join_columns: Optional[Union[list[str], Ref]] = None
    join_required: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aggregate_columns: Optional[list[AggregateColumn]] = None


@dataclass
class AnalysisRuleCustom(PropertyType):
    ADDITIONAL_ANALYSES = "AdditionalAnalyses"
    ALLOWED_ANALYSIS_PROVIDERS = "AllowedAnalysisProviders"
    DIFFERENTIAL_PRIVACY = "DifferentialPrivacy"
    ALLOWED_ANALYSES = "AllowedAnalyses"
    DISALLOWED_OUTPUT_COLUMNS = "DisallowedOutputColumns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_analyses": "AdditionalAnalyses",
        "allowed_analysis_providers": "AllowedAnalysisProviders",
        "differential_privacy": "DifferentialPrivacy",
        "allowed_analyses": "AllowedAnalyses",
        "disallowed_output_columns": "DisallowedOutputColumns",
    }

    additional_analyses: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_analysis_providers: Optional[Union[list[str], Ref]] = None
    differential_privacy: Optional[DifferentialPrivacy] = None
    allowed_analyses: Optional[Union[list[str], Ref]] = None
    disallowed_output_columns: Optional[Union[list[str], Ref]] = None


@dataclass
class AnalysisRuleList(PropertyType):
    ALLOWED_JOIN_OPERATORS = "AllowedJoinOperators"
    LIST_COLUMNS = "ListColumns"
    ADDITIONAL_ANALYSES = "AdditionalAnalyses"
    JOIN_COLUMNS = "JoinColumns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_join_operators": "AllowedJoinOperators",
        "list_columns": "ListColumns",
        "additional_analyses": "AdditionalAnalyses",
        "join_columns": "JoinColumns",
    }

    allowed_join_operators: Optional[Union[list[str], Ref]] = None
    list_columns: Optional[Union[list[str], Ref]] = None
    additional_analyses: Optional[Union[str, Ref, GetAtt, Sub]] = None
    join_columns: Optional[Union[list[str], Ref]] = None


@dataclass
class AthenaTableReference(PropertyType):
    WORK_GROUP = "WorkGroup"
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    REGION = "Region"
    OUTPUT_LOCATION = "OutputLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "work_group": "WorkGroup",
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "region": "Region",
        "output_location": "OutputLocation",
    }

    work_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConfiguredTableAnalysisRulePolicy(PropertyType):
    V1 = "V1"

    _property_mappings: ClassVar[dict[str, str]] = {
        "v1": "V1",
    }

    v1: Optional[ConfiguredTableAnalysisRulePolicyV1] = None


@dataclass
class ConfiguredTableAnalysisRulePolicyV1(PropertyType):
    AGGREGATION = "Aggregation"
    LIST = "List"
    CUSTOM = "Custom"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation": "Aggregation",
        "list": "List",
        "custom": "Custom",
    }

    aggregation: Optional[AnalysisRuleAggregation] = None
    list: Optional[AnalysisRuleList] = None
    custom: Optional[AnalysisRuleCustom] = None


@dataclass
class DifferentialPrivacy(PropertyType):
    COLUMNS = "Columns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "columns": "Columns",
    }

    columns: Optional[list[DifferentialPrivacyColumn]] = None


@dataclass
class DifferentialPrivacyColumn(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GlueTableReference(PropertyType):
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "region": "Region",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeTableReference(PropertyType):
    SECRET_ARN = "SecretArn"
    TABLE_NAME = "TableName"
    TABLE_SCHEMA = "TableSchema"
    ACCOUNT_IDENTIFIER = "AccountIdentifier"
    DATABASE_NAME = "DatabaseName"
    SCHEMA_NAME = "SchemaName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "table_name": "TableName",
        "table_schema": "TableSchema",
        "account_identifier": "AccountIdentifier",
        "database_name": "DatabaseName",
        "schema_name": "SchemaName",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_schema: Optional[SnowflakeTableSchema] = None
    account_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeTableSchema(PropertyType):
    V1 = "V1"

    _property_mappings: ClassVar[dict[str, str]] = {
        "v1": "V1",
    }

    v1: Optional[list[SnowflakeTableSchemaV1]] = None


@dataclass
class SnowflakeTableSchemaV1(PropertyType):
    COLUMN_NAME = "ColumnName"
    COLUMN_TYPE = "ColumnType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "column_type": "ColumnType",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableReference(PropertyType):
    GLUE = "Glue"
    SNOWFLAKE = "Snowflake"
    ATHENA = "Athena"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue": "Glue",
        "snowflake": "Snowflake",
        "athena": "Athena",
    }

    glue: Optional[GlueTableReference] = None
    snowflake: Optional[SnowflakeTableReference] = None
    athena: Optional[AthenaTableReference] = None

