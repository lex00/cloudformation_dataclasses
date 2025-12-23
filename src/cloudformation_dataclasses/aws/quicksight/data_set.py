"""PropertyTypes for AWS::QuickSight::DataSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AggregateOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_by_column_names": "GroupByColumnNames",
        "alias": "Alias",
        "aggregations": "Aggregations",
        "source": "Source",
    }

    group_by_column_names: Optional[Union[list[str], Ref]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aggregations: Optional[list[Aggregation]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class Aggregation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "new_column_name": "NewColumnName",
        "new_column_id": "NewColumnId",
    }

    aggregation_function: Optional[DataPrepAggregationFunction] = None
    new_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AppendOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "appended_columns": "AppendedColumns",
        "second_source": "SecondSource",
        "alias": "Alias",
        "first_source": "FirstSource",
    }

    appended_columns: Optional[list[AppendedColumn]] = None
    second_source: Optional[TransformOperationSource] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_source: Optional[TransformOperationSource] = None


@dataclass
class AppendedColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "new_column_id": "NewColumnId",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CalculatedColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_id": "ColumnId",
        "column_name": "ColumnName",
        "expression": "Expression",
    }

    column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CastColumnTypeOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "sub_type": "SubType",
        "format": "Format",
        "new_column_type": "NewColumnType",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, ColumnDataSubType, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_type: Optional[Union[str, ColumnDataType, Ref, GetAtt, Sub]] = None


@dataclass
class CastColumnTypesOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cast_column_type_operations": "CastColumnTypeOperations",
        "alias": "Alias",
        "source": "Source",
    }

    cast_column_type_operations: Optional[list[CastColumnTypeOperation]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class ColumnGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "geo_spatial_column_group": "GeoSpatialColumnGroup",
    }

    geo_spatial_column_group: Optional[GeoSpatialColumnGroup] = None


@dataclass
class ColumnLevelPermissionRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_names": "ColumnNames",
        "principals": "Principals",
    }

    column_names: Optional[Union[list[str], Ref]] = None
    principals: Optional[Union[list[str], Ref]] = None


@dataclass
class ColumnToUnpivot(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "new_value": "NewValue",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CreateColumnsOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "columns": "Columns",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[CalculatedColumn]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class CustomSql(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "sql_query": "SqlQuery",
        "columns": "Columns",
        "name": "Name",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql_query: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[InputColumn]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrepAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "percentile_aggregation": "PercentileAggregation",
        "simple_aggregation": "SimpleAggregation",
        "list_aggregation": "ListAggregation",
    }

    percentile_aggregation: Optional[DataPrepPercentileAggregationFunction] = None
    simple_aggregation: Optional[DataPrepSimpleAggregationFunction] = None
    list_aggregation: Optional[DataPrepListAggregationFunction] = None


@dataclass
class DataPrepConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_table_map": "DestinationTableMap",
        "transform_step_map": "TransformStepMap",
        "source_table_map": "SourceTableMap",
    }

    destination_table_map: Optional[dict[str, Any]] = None
    transform_step_map: Optional[dict[str, Any]] = None
    source_table_map: Optional[dict[str, Any]] = None


@dataclass
class DataPrepListAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "distinct": "Distinct",
        "input_column_name": "InputColumnName",
        "separator": "Separator",
    }

    distinct: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    separator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrepPercentileAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_column_name": "InputColumnName",
        "percentile_value": "PercentileValue",
    }

    input_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    percentile_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrepSimpleAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_type": "FunctionType",
        "input_column_name": "InputColumnName",
    }

    function_type: Optional[Union[str, DataPrepSimpleAggregationFunctionType, Ref, GetAtt, Sub]] = None
    input_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetColumnIdMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_column_id": "SourceColumnId",
        "target_column_id": "TargetColumnId",
    }

    source_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetDateComparisonFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, DataSetDateComparisonFilterOperator, Ref, GetAtt, Sub]] = None
    value: Optional[DataSetDateFilterValue] = None


@dataclass
class DataSetDateFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "range_filter_condition": "RangeFilterCondition",
        "comparison_filter_condition": "ComparisonFilterCondition",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_filter_condition: Optional[DataSetDateRangeFilterCondition] = None
    comparison_filter_condition: Optional[DataSetDateComparisonFilterCondition] = None


@dataclass
class DataSetDateFilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
    }

    static_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetDateRangeFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_maximum": "IncludeMaximum",
        "range_minimum": "RangeMinimum",
        "range_maximum": "RangeMaximum",
        "include_minimum": "IncludeMinimum",
    }

    include_maximum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    range_minimum: Optional[DataSetDateFilterValue] = None
    range_maximum: Optional[DataSetDateFilterValue] = None
    include_minimum: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetNumericComparisonFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, DataSetNumericComparisonFilterOperator, Ref, GetAtt, Sub]] = None
    value: Optional[DataSetNumericFilterValue] = None


@dataclass
class DataSetNumericFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "range_filter_condition": "RangeFilterCondition",
        "comparison_filter_condition": "ComparisonFilterCondition",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_filter_condition: Optional[DataSetNumericRangeFilterCondition] = None
    comparison_filter_condition: Optional[DataSetNumericComparisonFilterCondition] = None


@dataclass
class DataSetNumericFilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
    }

    static_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetNumericRangeFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_maximum": "IncludeMaximum",
        "range_minimum": "RangeMinimum",
        "range_maximum": "RangeMaximum",
        "include_minimum": "IncludeMinimum",
    }

    include_maximum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    range_minimum: Optional[DataSetNumericFilterValue] = None
    range_maximum: Optional[DataSetNumericFilterValue] = None
    include_minimum: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetRefreshProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_configuration": "RefreshConfiguration",
        "failure_configuration": "FailureConfiguration",
    }

    refresh_configuration: Optional[RefreshConfiguration] = None
    failure_configuration: Optional[RefreshFailureConfiguration] = None


@dataclass
class DataSetStringComparisonFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, DataSetStringComparisonFilterOperator, Ref, GetAtt, Sub]] = None
    value: Optional[DataSetStringFilterValue] = None


@dataclass
class DataSetStringFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "comparison_filter_condition": "ComparisonFilterCondition",
        "list_filter_condition": "ListFilterCondition",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    comparison_filter_condition: Optional[DataSetStringComparisonFilterCondition] = None
    list_filter_condition: Optional[DataSetStringListFilterCondition] = None


@dataclass
class DataSetStringFilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
    }

    static_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetStringListFilterCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "values": "Values",
    }

    operator: Optional[Union[str, DataSetStringListFilterOperator, Ref, GetAtt, Sub]] = None
    values: Optional[DataSetStringListFilterValue] = None


@dataclass
class DataSetStringListFilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class DataSetUsageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "disable_use_as_imported_source": "DisableUseAsImportedSource",
        "disable_use_as_direct_query_source": "DisableUseAsDirectQuerySource",
    }

    disable_use_as_imported_source: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    disable_use_as_direct_query_source: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "integer_dataset_parameter": "IntegerDatasetParameter",
        "date_time_dataset_parameter": "DateTimeDatasetParameter",
        "decimal_dataset_parameter": "DecimalDatasetParameter",
        "string_dataset_parameter": "StringDatasetParameter",
    }

    integer_dataset_parameter: Optional[IntegerDatasetParameter] = None
    date_time_dataset_parameter: Optional[DateTimeDatasetParameter] = None
    decimal_dataset_parameter: Optional[DecimalDatasetParameter] = None
    string_dataset_parameter: Optional[StringDatasetParameter] = None


@dataclass
class DateTimeDatasetParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "time_granularity": "TimeGranularity",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    default_values: Optional[DateTimeDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeDatasetParameterDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class DecimalDatasetParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    default_values: Optional[DecimalDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecimalDatasetParameterDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[float], Ref]] = None


@dataclass
class DestinationTable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[DestinationTableSource] = None


@dataclass
class DestinationTableSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transform_operation_id": "TransformOperationId",
    }

    transform_operation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FieldFolder(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "columns": "Columns",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[Union[list[str], Ref]] = None


@dataclass
class FilterOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "date_filter_condition": "DateFilterCondition",
        "string_filter_condition": "StringFilterCondition",
        "condition_expression": "ConditionExpression",
        "numeric_filter_condition": "NumericFilterCondition",
    }

    date_filter_condition: Optional[DataSetDateFilterCondition] = None
    string_filter_condition: Optional[DataSetStringFilterCondition] = None
    condition_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    numeric_filter_condition: Optional[DataSetNumericFilterCondition] = None


@dataclass
class FiltersOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_operations": "FilterOperations",
        "alias": "Alias",
        "source": "Source",
    }

    filter_operations: Optional[list[FilterOperation]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class GeoSpatialColumnGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "columns": "Columns",
        "country_code": "CountryCode",
        "name": "Name",
    }

    columns: Optional[Union[list[str], Ref]] = None
    country_code: Optional[Union[str, GeoSpatialCountryCode, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImportTableOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[ImportTableOperationSource] = None


@dataclass
class ImportTableOperationSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_table_id": "SourceTableId",
        "column_id_mappings": "ColumnIdMappings",
    }

    source_table_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_id_mappings: Optional[list[DataSetColumnIdMapping]] = None


@dataclass
class IncrementalRefresh(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lookback_window": "LookbackWindow",
    }

    lookback_window: Optional[LookbackWindow] = None


@dataclass
class IngestionWaitPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "wait_for_spice_ingestion": "WaitForSpiceIngestion",
        "ingestion_wait_time_in_hours": "IngestionWaitTimeInHours",
    }

    wait_for_spice_ingestion: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ingestion_wait_time_in_hours: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class InputColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "sub_type": "SubType",
        "id": "Id",
        "name": "Name",
    }

    type_: Optional[Union[str, InputColumnDataType, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, ColumnDataSubType, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerDatasetParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    default_values: Optional[IntegerDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerDatasetParameterDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[int], Ref]] = None


@dataclass
class JoinOperandProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_column_name_overrides": "OutputColumnNameOverrides",
    }

    output_column_name_overrides: Optional[list[OutputColumnNameOverride]] = None


@dataclass
class JoinOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "on_clause": "OnClause",
        "type_": "Type",
        "right_operand_properties": "RightOperandProperties",
        "left_operand_properties": "LeftOperandProperties",
        "alias": "Alias",
        "left_operand": "LeftOperand",
        "right_operand": "RightOperand",
    }

    on_clause: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, JoinOperationType, Ref, GetAtt, Sub]] = None
    right_operand_properties: Optional[JoinOperandProperties] = None
    left_operand_properties: Optional[JoinOperandProperties] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    left_operand: Optional[TransformOperationSource] = None
    right_operand: Optional[TransformOperationSource] = None


@dataclass
class LookbackWindow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "size_unit": "SizeUnit",
        "size": "Size",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_unit: Optional[Union[str, LookbackWindowSizeUnit, Ref, GetAtt, Sub]] = None
    size: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OutputColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "sub_type": "SubType",
        "id": "Id",
        "name": "Name",
    }

    type_: Optional[Union[str, ColumnDataType, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, ColumnDataSubType, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputColumnNameOverride(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_column_name": "OutputColumnName",
        "source_column_name": "SourceColumnName",
    }

    output_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParentDataSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_columns": "InputColumns",
        "data_set_arn": "DataSetArn",
    }

    input_columns: Optional[list[InputColumn]] = None
    data_set_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PerformanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unique_keys": "UniqueKeys",
    }

    unique_keys: Optional[list[UniqueKey]] = None


@dataclass
class PhysicalTable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "saa_s_table": "SaaSTable",
        "relational_table": "RelationalTable",
        "custom_sql": "CustomSql",
        "s3_source": "S3Source",
    }

    saa_s_table: Optional[SaaSTable] = None
    relational_table: Optional[RelationalTable] = None
    custom_sql: Optional[CustomSql] = None
    s3_source: Optional[S3Source] = None


@dataclass
class PivotConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "label_column_name": "LabelColumnName",
        "pivoted_labels": "PivotedLabels",
    }

    label_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pivoted_labels: Optional[list[PivotedLabel]] = None


@dataclass
class PivotOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pivot_configuration": "PivotConfiguration",
        "group_by_column_names": "GroupByColumnNames",
        "alias": "Alias",
        "value_column_configuration": "ValueColumnConfiguration",
        "source": "Source",
    }

    pivot_configuration: Optional[PivotConfiguration] = None
    group_by_column_names: Optional[Union[list[str], Ref]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_column_configuration: Optional[ValueColumnConfiguration] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class PivotedLabel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "new_column_name": "NewColumnName",
        "new_column_id": "NewColumnId",
        "label_name": "LabelName",
    }

    new_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "projected_columns": "ProjectedColumns",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    projected_columns: Optional[Union[list[str], Ref]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class RefreshConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "incremental_refresh": "IncrementalRefresh",
    }

    incremental_refresh: Optional[IncrementalRefresh] = None


@dataclass
class RefreshFailureConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "email_alert": "EmailAlert",
    }

    email_alert: Optional[RefreshFailureEmailAlert] = None


@dataclass
class RefreshFailureEmailAlert(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alert_status": "AlertStatus",
    }

    alert_status: Optional[Union[str, RefreshFailureAlertStatus, Ref, GetAtt, Sub]] = None


@dataclass
class RelationalTable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "input_columns": "InputColumns",
        "schema": "Schema",
        "catalog": "Catalog",
        "name": "Name",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_columns: Optional[list[InputColumn]] = None
    schema: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenameColumnOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "new_column_name": "NewColumnName",
        "column_name": "ColumnName",
    }

    new_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenameColumnsOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "rename_column_operations": "RenameColumnOperations",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rename_column_operations: Optional[list[RenameColumnOperation]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class ResourcePermission(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "principal": "Principal",
    }

    actions: Optional[Union[list[str], Ref]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RowLevelPermissionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_configuration": "TagConfiguration",
        "row_level_permission_data_set": "RowLevelPermissionDataSet",
    }

    tag_configuration: Optional[RowLevelPermissionTagConfiguration] = None
    row_level_permission_data_set: Optional[RowLevelPermissionDataSet] = None


@dataclass
class RowLevelPermissionDataSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "format_version": "FormatVersion",
        "arn": "Arn",
        "namespace": "Namespace",
        "permission_policy": "PermissionPolicy",
    }

    status: Optional[Union[str, Status, Ref, GetAtt, Sub]] = None
    format_version: Optional[Union[str, RowLevelPermissionFormatVersion, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    permission_policy: Optional[Union[str, RowLevelPermissionPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class RowLevelPermissionTagConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "tag_rules": "TagRules",
        "tag_rule_configurations": "TagRuleConfigurations",
    }

    status: Optional[Union[str, Status, Ref, GetAtt, Sub]] = None
    tag_rules: Optional[list[RowLevelPermissionTagRule]] = None
    tag_rule_configurations: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class RowLevelPermissionTagRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "tag_key": "TagKey",
        "match_all_value": "MatchAllValue",
        "tag_multi_value_delimiter": "TagMultiValueDelimiter",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_all_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_multi_value_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "input_columns": "InputColumns",
        "upload_settings": "UploadSettings",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_columns: Optional[list[InputColumn]] = None
    upload_settings: Optional[UploadSettings] = None


@dataclass
class SaaSTable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "input_columns": "InputColumns",
        "table_path": "TablePath",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_columns: Optional[list[InputColumn]] = None
    table_path: Optional[list[TablePathElement]] = None


@dataclass
class SemanticModelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_map": "TableMap",
    }

    table_map: Optional[dict[str, Any]] = None


@dataclass
class SemanticTable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "destination_table_id": "DestinationTableId",
        "row_level_permission_configuration": "RowLevelPermissionConfiguration",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_table_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    row_level_permission_configuration: Optional[RowLevelPermissionConfiguration] = None


@dataclass
class SourceTable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "physical_table_id": "PhysicalTableId",
        "data_set": "DataSet",
    }

    physical_table_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set: Optional[ParentDataSet] = None


@dataclass
class StringDatasetParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    default_values: Optional[StringDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StringDatasetParameterDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class TablePathElement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
        "name": "Name",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TransformOperationSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transform_operation_id": "TransformOperationId",
        "column_id_mappings": "ColumnIdMappings",
    }

    transform_operation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_id_mappings: Optional[list[DataSetColumnIdMapping]] = None


@dataclass
class TransformStep(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_step": "ProjectStep",
        "create_columns_step": "CreateColumnsStep",
        "rename_columns_step": "RenameColumnsStep",
        "cast_column_types_step": "CastColumnTypesStep",
        "import_table_step": "ImportTableStep",
        "unpivot_step": "UnpivotStep",
        "join_step": "JoinStep",
        "append_step": "AppendStep",
        "filters_step": "FiltersStep",
        "aggregate_step": "AggregateStep",
        "pivot_step": "PivotStep",
    }

    project_step: Optional[ProjectOperation] = None
    create_columns_step: Optional[CreateColumnsOperation] = None
    rename_columns_step: Optional[RenameColumnsOperation] = None
    cast_column_types_step: Optional[CastColumnTypesOperation] = None
    import_table_step: Optional[ImportTableOperation] = None
    unpivot_step: Optional[UnpivotOperation] = None
    join_step: Optional[JoinOperation] = None
    append_step: Optional[AppendOperation] = None
    filters_step: Optional[FiltersOperation] = None
    aggregate_step: Optional[AggregateOperation] = None
    pivot_step: Optional[PivotOperation] = None


@dataclass
class UniqueKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_names": "ColumnNames",
    }

    column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class UnpivotOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unpivoted_label_column_name": "UnpivotedLabelColumnName",
        "columns_to_unpivot": "ColumnsToUnpivot",
        "unpivoted_label_column_id": "UnpivotedLabelColumnId",
        "alias": "Alias",
        "unpivoted_value_column_id": "UnpivotedValueColumnId",
        "unpivoted_value_column_name": "UnpivotedValueColumnName",
        "source": "Source",
    }

    unpivoted_label_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns_to_unpivot: Optional[list[ColumnToUnpivot]] = None
    unpivoted_label_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unpivoted_value_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unpivoted_value_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class UploadSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "contains_header": "ContainsHeader",
        "text_qualifier": "TextQualifier",
        "format": "Format",
        "start_from_row": "StartFromRow",
        "delimiter": "Delimiter",
    }

    contains_header: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    text_qualifier: Optional[Union[str, TextQualifier, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, FileFormat, Ref, GetAtt, Sub]] = None
    start_from_row: Optional[Union[float, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValueColumnConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
    }

    aggregation_function: Optional[DataPrepAggregationFunction] = None

