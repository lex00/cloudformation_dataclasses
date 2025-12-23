"""PropertyTypes for AWS::CleanRooms::ConfiguredTable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

