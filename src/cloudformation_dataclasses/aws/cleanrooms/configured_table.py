"""PropertyTypes for AWS::CleanRooms::ConfiguredTable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AggregateColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "column_names": "ColumnNames",
    }

    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class AggregationConstraint(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
        "type_": "Type",
    }

    policy: Optional[ConfiguredTableAnalysisRulePolicy] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisRuleAggregation(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "v1": "V1",
    }

    v1: Optional[ConfiguredTableAnalysisRulePolicyV1] = None


@dataclass
class ConfiguredTableAnalysisRulePolicyV1(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "columns": "Columns",
    }

    columns: Optional[list[DifferentialPrivacyColumn]] = None


@dataclass
class DifferentialPrivacyColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GlueTableReference(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "v1": "V1",
    }

    v1: Optional[list[SnowflakeTableSchemaV1]] = None


@dataclass
class SnowflakeTableSchemaV1(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "column_type": "ColumnType",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "glue": "Glue",
        "snowflake": "Snowflake",
        "athena": "Athena",
    }

    glue: Optional[GlueTableReference] = None
    snowflake: Optional[SnowflakeTableReference] = None
    athena: Optional[AthenaTableReference] = None

