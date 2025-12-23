"""PropertyTypes for AWS::QuickSight::Topic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CellValueSynonym(PropertyType):
    SYNONYMS = "Synonyms"
    CELL_VALUE = "CellValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "synonyms": "Synonyms",
        "cell_value": "CellValue",
    }

    synonyms: Optional[Union[list[str], Ref]] = None
    cell_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CollectiveConstant(PropertyType):
    VALUE_LIST = "ValueList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_list": "ValueList",
    }

    value_list: Optional[Union[list[str], Ref]] = None


@dataclass
class ComparativeOrder(PropertyType):
    SPECIFED_ORDER = "SpecifedOrder"
    USE_ORDERING = "UseOrdering"
    TREAT_UNDEFINED_SPECIFIED_VALUES = "TreatUndefinedSpecifiedValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "specifed_order": "SpecifedOrder",
        "use_ordering": "UseOrdering",
        "treat_undefined_specified_values": "TreatUndefinedSpecifiedValues",
    }

    specifed_order: Optional[Union[list[str], Ref]] = None
    use_ordering: Optional[Union[str, ColumnOrderingType, Ref, GetAtt, Sub]] = None
    treat_undefined_specified_values: Optional[Union[str, UndefinedSpecifiedValueType, Ref, GetAtt, Sub]] = None


@dataclass
class CustomInstructions(PropertyType):
    CUSTOM_INSTRUCTIONS_STRING = "CustomInstructionsString"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_instructions_string": "CustomInstructionsString",
    }

    custom_instructions_string: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataAggregation(PropertyType):
    DATASET_ROW_DATE_GRANULARITY = "DatasetRowDateGranularity"
    DEFAULT_DATE_COLUMN_NAME = "DefaultDateColumnName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_row_date_granularity": "DatasetRowDateGranularity",
        "default_date_column_name": "DefaultDateColumnName",
    }

    dataset_row_date_granularity: Optional[Union[str, TopicTimeGranularity, Ref, GetAtt, Sub]] = None
    default_date_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetMetadata(PropertyType):
    DATASET_ARN = "DatasetArn"
    FILTERS = "Filters"
    NAMED_ENTITIES = "NamedEntities"
    DATASET_NAME = "DatasetName"
    CALCULATED_FIELDS = "CalculatedFields"
    COLUMNS = "Columns"
    DATA_AGGREGATION = "DataAggregation"
    DATASET_DESCRIPTION = "DatasetDescription"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_arn": "DatasetArn",
        "filters": "Filters",
        "named_entities": "NamedEntities",
        "dataset_name": "DatasetName",
        "calculated_fields": "CalculatedFields",
        "columns": "Columns",
        "data_aggregation": "DataAggregation",
        "dataset_description": "DatasetDescription",
    }

    dataset_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filters: Optional[list[TopicFilter]] = None
    named_entities: Optional[list[TopicNamedEntity]] = None
    dataset_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    calculated_fields: Optional[list[TopicCalculatedField]] = None
    columns: Optional[list[TopicColumn]] = None
    data_aggregation: Optional[DataAggregation] = None
    dataset_description: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultFormatting(PropertyType):
    DISPLAY_FORMAT_OPTIONS = "DisplayFormatOptions"
    DISPLAY_FORMAT = "DisplayFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "display_format_options": "DisplayFormatOptions",
        "display_format": "DisplayFormat",
    }

    display_format_options: Optional[DisplayFormatOptions] = None
    display_format: Optional[Union[str, DisplayFormat, Ref, GetAtt, Sub]] = None


@dataclass
class DisplayFormatOptions(PropertyType):
    DECIMAL_SEPARATOR = "DecimalSeparator"
    FRACTION_DIGITS = "FractionDigits"
    SUFFIX = "Suffix"
    DATE_FORMAT = "DateFormat"
    UNIT_SCALER = "UnitScaler"
    NEGATIVE_FORMAT = "NegativeFormat"
    USE_BLANK_CELL_FORMAT = "UseBlankCellFormat"
    PREFIX = "Prefix"
    BLANK_CELL_FORMAT = "BlankCellFormat"
    CURRENCY_SYMBOL = "CurrencySymbol"
    GROUPING_SEPARATOR = "GroupingSeparator"
    USE_GROUPING = "UseGrouping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "decimal_separator": "DecimalSeparator",
        "fraction_digits": "FractionDigits",
        "suffix": "Suffix",
        "date_format": "DateFormat",
        "unit_scaler": "UnitScaler",
        "negative_format": "NegativeFormat",
        "use_blank_cell_format": "UseBlankCellFormat",
        "prefix": "Prefix",
        "blank_cell_format": "BlankCellFormat",
        "currency_symbol": "CurrencySymbol",
        "grouping_separator": "GroupingSeparator",
        "use_grouping": "UseGrouping",
    }

    decimal_separator: Optional[Union[str, TopicNumericSeparatorSymbol, Ref, GetAtt, Sub]] = None
    fraction_digits: Optional[Union[float, Ref, GetAtt, Sub]] = None
    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    date_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit_scaler: Optional[Union[str, NumberScale, Ref, GetAtt, Sub]] = None
    negative_format: Optional[NegativeFormat] = None
    use_blank_cell_format: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    blank_cell_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    currency_symbol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    grouping_separator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_grouping: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class NamedEntityDefinition(PropertyType):
    PROPERTY_NAME = "PropertyName"
    PROPERTY_USAGE = "PropertyUsage"
    PROPERTY_ROLE = "PropertyRole"
    METRIC = "Metric"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "property_name": "PropertyName",
        "property_usage": "PropertyUsage",
        "property_role": "PropertyRole",
        "metric": "Metric",
        "field_name": "FieldName",
    }

    property_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_usage: Optional[Union[str, PropertyUsage, Ref, GetAtt, Sub]] = None
    property_role: Optional[Union[str, PropertyRole, Ref, GetAtt, Sub]] = None
    metric: Optional[NamedEntityDefinitionMetric] = None
    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NamedEntityDefinitionMetric(PropertyType):
    AGGREGATION = "Aggregation"
    AGGREGATION_FUNCTION_PARAMETERS = "AggregationFunctionParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation": "Aggregation",
        "aggregation_function_parameters": "AggregationFunctionParameters",
    }

    aggregation: Optional[Union[str, NamedEntityAggType, Ref, GetAtt, Sub]] = None
    aggregation_function_parameters: Optional[dict[str, str]] = None


@dataclass
class NegativeFormat(PropertyType):
    SUFFIX = "Suffix"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "suffix": "Suffix",
        "prefix": "Prefix",
    }

    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RangeConstant(PropertyType):
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
    }

    minimum: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticEntityType(PropertyType):
    TYPE_NAME = "TypeName"
    TYPE_PARAMETERS = "TypeParameters"
    SUB_TYPE_NAME = "SubTypeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_name": "TypeName",
        "type_parameters": "TypeParameters",
        "sub_type_name": "SubTypeName",
    }

    type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_parameters: Optional[dict[str, str]] = None
    sub_type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticType(PropertyType):
    TRUTHY_CELL_VALUE_SYNONYMS = "TruthyCellValueSynonyms"
    TYPE_NAME = "TypeName"
    TYPE_PARAMETERS = "TypeParameters"
    SUB_TYPE_NAME = "SubTypeName"
    TRUTHY_CELL_VALUE = "TruthyCellValue"
    FALSEY_CELL_VALUE = "FalseyCellValue"
    FALSEY_CELL_VALUE_SYNONYMS = "FalseyCellValueSynonyms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "truthy_cell_value_synonyms": "TruthyCellValueSynonyms",
        "type_name": "TypeName",
        "type_parameters": "TypeParameters",
        "sub_type_name": "SubTypeName",
        "truthy_cell_value": "TruthyCellValue",
        "falsey_cell_value": "FalseyCellValue",
        "falsey_cell_value_synonyms": "FalseyCellValueSynonyms",
    }

    truthy_cell_value_synonyms: Optional[Union[list[str], Ref]] = None
    type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_parameters: Optional[dict[str, str]] = None
    sub_type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    truthy_cell_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    falsey_cell_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    falsey_cell_value_synonyms: Optional[Union[list[str], Ref]] = None


@dataclass
class TopicCalculatedField(PropertyType):
    SEMANTIC_TYPE = "SemanticType"
    NOT_ALLOWED_AGGREGATIONS = "NotAllowedAggregations"
    DEFAULT_FORMATTING = "DefaultFormatting"
    ALLOWED_AGGREGATIONS = "AllowedAggregations"
    CALCULATED_FIELD_DESCRIPTION = "CalculatedFieldDescription"
    CALCULATED_FIELD_SYNONYMS = "CalculatedFieldSynonyms"
    IS_INCLUDED_IN_TOPIC = "IsIncludedInTopic"
    COLUMN_DATA_ROLE = "ColumnDataRole"
    AGGREGATION = "Aggregation"
    EXPRESSION = "Expression"
    NON_ADDITIVE = "NonAdditive"
    CALCULATED_FIELD_NAME = "CalculatedFieldName"
    NEVER_AGGREGATE_IN_FILTER = "NeverAggregateInFilter"
    TIME_GRANULARITY = "TimeGranularity"
    DISABLE_INDEXING = "DisableIndexing"
    COMPARATIVE_ORDER = "ComparativeOrder"
    CELL_VALUE_SYNONYMS = "CellValueSynonyms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "semantic_type": "SemanticType",
        "not_allowed_aggregations": "NotAllowedAggregations",
        "default_formatting": "DefaultFormatting",
        "allowed_aggregations": "AllowedAggregations",
        "calculated_field_description": "CalculatedFieldDescription",
        "calculated_field_synonyms": "CalculatedFieldSynonyms",
        "is_included_in_topic": "IsIncludedInTopic",
        "column_data_role": "ColumnDataRole",
        "aggregation": "Aggregation",
        "expression": "Expression",
        "non_additive": "NonAdditive",
        "calculated_field_name": "CalculatedFieldName",
        "never_aggregate_in_filter": "NeverAggregateInFilter",
        "time_granularity": "TimeGranularity",
        "disable_indexing": "DisableIndexing",
        "comparative_order": "ComparativeOrder",
        "cell_value_synonyms": "CellValueSynonyms",
    }

    semantic_type: Optional[SemanticType] = None
    not_allowed_aggregations: Optional[Union[list[str], Ref]] = None
    default_formatting: Optional[DefaultFormatting] = None
    allowed_aggregations: Optional[Union[list[str], Ref]] = None
    calculated_field_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    calculated_field_synonyms: Optional[Union[list[str], Ref]] = None
    is_included_in_topic: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    column_data_role: Optional[Union[str, ColumnDataRole, Ref, GetAtt, Sub]] = None
    aggregation: Optional[Union[str, DefaultAggregation, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    non_additive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    calculated_field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    never_aggregate_in_filter: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TopicTimeGranularity, Ref, GetAtt, Sub]] = None
    disable_indexing: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    comparative_order: Optional[ComparativeOrder] = None
    cell_value_synonyms: Optional[list[CellValueSynonym]] = None


@dataclass
class TopicCategoryFilter(PropertyType):
    CATEGORY_FILTER_TYPE = "CategoryFilterType"
    CATEGORY_FILTER_FUNCTION = "CategoryFilterFunction"
    CONSTANT = "Constant"
    INVERSE = "Inverse"

    _property_mappings: ClassVar[dict[str, str]] = {
        "category_filter_type": "CategoryFilterType",
        "category_filter_function": "CategoryFilterFunction",
        "constant": "Constant",
        "inverse": "Inverse",
    }

    category_filter_type: Optional[Union[str, CategoryFilterType, Ref, GetAtt, Sub]] = None
    category_filter_function: Optional[Union[str, CategoryFilterFunction, Ref, GetAtt, Sub]] = None
    constant: Optional[TopicCategoryFilterConstant] = None
    inverse: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TopicCategoryFilterConstant(PropertyType):
    SINGULAR_CONSTANT = "SingularConstant"
    CONSTANT_TYPE = "ConstantType"
    COLLECTIVE_CONSTANT = "CollectiveConstant"

    _property_mappings: ClassVar[dict[str, str]] = {
        "singular_constant": "SingularConstant",
        "constant_type": "ConstantType",
        "collective_constant": "CollectiveConstant",
    }

    singular_constant: Optional[Union[str, Ref, GetAtt, Sub]] = None
    constant_type: Optional[Union[str, ConstantType, Ref, GetAtt, Sub]] = None
    collective_constant: Optional[CollectiveConstant] = None


@dataclass
class TopicColumn(PropertyType):
    SEMANTIC_TYPE = "SemanticType"
    NOT_ALLOWED_AGGREGATIONS = "NotAllowedAggregations"
    ALLOWED_AGGREGATIONS = "AllowedAggregations"
    DEFAULT_FORMATTING = "DefaultFormatting"
    COLUMN_DESCRIPTION = "ColumnDescription"
    IS_INCLUDED_IN_TOPIC = "IsIncludedInTopic"
    COLUMN_DATA_ROLE = "ColumnDataRole"
    AGGREGATION = "Aggregation"
    COLUMN_NAME = "ColumnName"
    NON_ADDITIVE = "NonAdditive"
    COLUMN_SYNONYMS = "ColumnSynonyms"
    NEVER_AGGREGATE_IN_FILTER = "NeverAggregateInFilter"
    TIME_GRANULARITY = "TimeGranularity"
    COLUMN_FRIENDLY_NAME = "ColumnFriendlyName"
    DISABLE_INDEXING = "DisableIndexing"
    COMPARATIVE_ORDER = "ComparativeOrder"
    CELL_VALUE_SYNONYMS = "CellValueSynonyms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "semantic_type": "SemanticType",
        "not_allowed_aggregations": "NotAllowedAggregations",
        "allowed_aggregations": "AllowedAggregations",
        "default_formatting": "DefaultFormatting",
        "column_description": "ColumnDescription",
        "is_included_in_topic": "IsIncludedInTopic",
        "column_data_role": "ColumnDataRole",
        "aggregation": "Aggregation",
        "column_name": "ColumnName",
        "non_additive": "NonAdditive",
        "column_synonyms": "ColumnSynonyms",
        "never_aggregate_in_filter": "NeverAggregateInFilter",
        "time_granularity": "TimeGranularity",
        "column_friendly_name": "ColumnFriendlyName",
        "disable_indexing": "DisableIndexing",
        "comparative_order": "ComparativeOrder",
        "cell_value_synonyms": "CellValueSynonyms",
    }

    semantic_type: Optional[SemanticType] = None
    not_allowed_aggregations: Optional[Union[list[str], Ref]] = None
    allowed_aggregations: Optional[Union[list[str], Ref]] = None
    default_formatting: Optional[DefaultFormatting] = None
    column_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_included_in_topic: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    column_data_role: Optional[Union[str, ColumnDataRole, Ref, GetAtt, Sub]] = None
    aggregation: Optional[Union[str, DefaultAggregation, Ref, GetAtt, Sub]] = None
    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    non_additive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    column_synonyms: Optional[Union[list[str], Ref]] = None
    never_aggregate_in_filter: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TopicTimeGranularity, Ref, GetAtt, Sub]] = None
    column_friendly_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disable_indexing: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    comparative_order: Optional[ComparativeOrder] = None
    cell_value_synonyms: Optional[list[CellValueSynonym]] = None


@dataclass
class TopicConfigOptions(PropertyType):
    Q_BUSINESS_INSIGHTS_ENABLED = "QBusinessInsightsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "q_business_insights_enabled": "QBusinessInsightsEnabled",
    }

    q_business_insights_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TopicDateRangeFilter(PropertyType):
    INCLUSIVE = "Inclusive"
    CONSTANT = "Constant"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inclusive": "Inclusive",
        "constant": "Constant",
    }

    inclusive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    constant: Optional[TopicRangeFilterConstant] = None


@dataclass
class TopicFilter(PropertyType):
    FILTER_CLASS = "FilterClass"
    FILTER_SYNONYMS = "FilterSynonyms"
    FILTER_TYPE = "FilterType"
    RELATIVE_DATE_FILTER = "RelativeDateFilter"
    OPERAND_FIELD_NAME = "OperandFieldName"
    NUMERIC_EQUALITY_FILTER = "NumericEqualityFilter"
    FILTER_DESCRIPTION = "FilterDescription"
    NUMERIC_RANGE_FILTER = "NumericRangeFilter"
    DATE_RANGE_FILTER = "DateRangeFilter"
    FILTER_NAME = "FilterName"
    CATEGORY_FILTER = "CategoryFilter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_class": "FilterClass",
        "filter_synonyms": "FilterSynonyms",
        "filter_type": "FilterType",
        "relative_date_filter": "RelativeDateFilter",
        "operand_field_name": "OperandFieldName",
        "numeric_equality_filter": "NumericEqualityFilter",
        "filter_description": "FilterDescription",
        "numeric_range_filter": "NumericRangeFilter",
        "date_range_filter": "DateRangeFilter",
        "filter_name": "FilterName",
        "category_filter": "CategoryFilter",
    }

    filter_class: Optional[Union[str, FilterClass, Ref, GetAtt, Sub]] = None
    filter_synonyms: Optional[Union[list[str], Ref]] = None
    filter_type: Optional[Union[str, NamedFilterType, Ref, GetAtt, Sub]] = None
    relative_date_filter: Optional[TopicRelativeDateFilter] = None
    operand_field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    numeric_equality_filter: Optional[TopicNumericEqualityFilter] = None
    filter_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    numeric_range_filter: Optional[TopicNumericRangeFilter] = None
    date_range_filter: Optional[TopicDateRangeFilter] = None
    filter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category_filter: Optional[TopicCategoryFilter] = None


@dataclass
class TopicNamedEntity(PropertyType):
    ENTITY_SYNONYMS = "EntitySynonyms"
    ENTITY_NAME = "EntityName"
    SEMANTIC_ENTITY_TYPE = "SemanticEntityType"
    ENTITY_DESCRIPTION = "EntityDescription"
    DEFINITION = "Definition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_synonyms": "EntitySynonyms",
        "entity_name": "EntityName",
        "semantic_entity_type": "SemanticEntityType",
        "entity_description": "EntityDescription",
        "definition": "Definition",
    }

    entity_synonyms: Optional[Union[list[str], Ref]] = None
    entity_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    semantic_entity_type: Optional[SemanticEntityType] = None
    entity_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    definition: Optional[list[NamedEntityDefinition]] = None


@dataclass
class TopicNumericEqualityFilter(PropertyType):
    AGGREGATION = "Aggregation"
    CONSTANT = "Constant"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation": "Aggregation",
        "constant": "Constant",
    }

    aggregation: Optional[Union[str, NamedFilterAggType, Ref, GetAtt, Sub]] = None
    constant: Optional[TopicSingularFilterConstant] = None


@dataclass
class TopicNumericRangeFilter(PropertyType):
    AGGREGATION = "Aggregation"
    INCLUSIVE = "Inclusive"
    CONSTANT = "Constant"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation": "Aggregation",
        "inclusive": "Inclusive",
        "constant": "Constant",
    }

    aggregation: Optional[Union[str, NamedFilterAggType, Ref, GetAtt, Sub]] = None
    inclusive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    constant: Optional[TopicRangeFilterConstant] = None


@dataclass
class TopicRangeFilterConstant(PropertyType):
    CONSTANT_TYPE = "ConstantType"
    RANGE_CONSTANT = "RangeConstant"

    _property_mappings: ClassVar[dict[str, str]] = {
        "constant_type": "ConstantType",
        "range_constant": "RangeConstant",
    }

    constant_type: Optional[Union[str, ConstantType, Ref, GetAtt, Sub]] = None
    range_constant: Optional[RangeConstant] = None


@dataclass
class TopicRelativeDateFilter(PropertyType):
    RELATIVE_DATE_FILTER_FUNCTION = "RelativeDateFilterFunction"
    CONSTANT = "Constant"
    TIME_GRANULARITY = "TimeGranularity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "relative_date_filter_function": "RelativeDateFilterFunction",
        "constant": "Constant",
        "time_granularity": "TimeGranularity",
    }

    relative_date_filter_function: Optional[Union[str, TopicRelativeDateFilterFunction, Ref, GetAtt, Sub]] = None
    constant: Optional[TopicSingularFilterConstant] = None
    time_granularity: Optional[Union[str, TopicTimeGranularity, Ref, GetAtt, Sub]] = None


@dataclass
class TopicSingularFilterConstant(PropertyType):
    SINGULAR_CONSTANT = "SingularConstant"
    CONSTANT_TYPE = "ConstantType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "singular_constant": "SingularConstant",
        "constant_type": "ConstantType",
    }

    singular_constant: Optional[Union[str, Ref, GetAtt, Sub]] = None
    constant_type: Optional[Union[str, ConstantType, Ref, GetAtt, Sub]] = None

