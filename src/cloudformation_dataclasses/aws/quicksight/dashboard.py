"""PropertyTypes for AWS::QuickSight::Dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdHocFilteringOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class AggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_aggregation_function": "AttributeAggregationFunction",
        "date_aggregation_function": "DateAggregationFunction",
        "numerical_aggregation_function": "NumericalAggregationFunction",
        "categorical_aggregation_function": "CategoricalAggregationFunction",
    }

    attribute_aggregation_function: Optional[AttributeAggregationFunction] = None
    date_aggregation_function: Optional[Union[str, DateAggregationFunction, Ref, GetAtt, Sub]] = None
    numerical_aggregation_function: Optional[NumericalAggregationFunction] = None
    categorical_aggregation_function: Optional[Union[str, CategoricalAggregationFunction, Ref, GetAtt, Sub]] = None


@dataclass
class AggregationSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "sort_direction": "SortDirection",
        "column": "Column",
    }

    aggregation_function: Optional[AggregationFunction] = None
    sort_direction: Optional[Union[str, SortDirection, Ref, GetAtt, Sub]] = None
    column: Optional[ColumnIdentifier] = None


@dataclass
class AnalysisDefaults(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_new_sheet_configuration": "DefaultNewSheetConfiguration",
    }

    default_new_sheet_configuration: Optional[DefaultNewSheetConfiguration] = None


@dataclass
class AnchorDateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "anchor_option": "AnchorOption",
        "parameter_name": "ParameterName",
    }

    anchor_option: Optional[Union[str, AnchorOption, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArcAxisConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "range": "Range",
        "reserve_range": "ReserveRange",
    }

    range: Optional[ArcAxisDisplayRange] = None
    reserve_range: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ArcAxisDisplayRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ArcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arc_angle": "ArcAngle",
        "arc_thickness": "ArcThickness",
    }

    arc_angle: Optional[Union[float, Ref, GetAtt, Sub]] = None
    arc_thickness: Optional[Union[str, ArcThicknessOptions, Ref, GetAtt, Sub]] = None


@dataclass
class ArcOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arc_thickness": "ArcThickness",
    }

    arc_thickness: Optional[Union[str, ArcThickness, Ref, GetAtt, Sub]] = None


@dataclass
class AssetOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timezone": "Timezone",
        "week_start": "WeekStart",
        "q_business_insights_status": "QBusinessInsightsStatus",
        "excluded_data_set_arns": "ExcludedDataSetArns",
    }

    timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    week_start: Optional[Union[str, DayOfTheWeek, Ref, GetAtt, Sub]] = None
    q_business_insights_status: Optional[Union[str, QBusinessInsightsStatus, Ref, GetAtt, Sub]] = None
    excluded_data_set_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class AttributeAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "simple_attribute_aggregation": "SimpleAttributeAggregation",
        "value_for_multiple_values": "ValueForMultipleValues",
    }

    simple_attribute_aggregation: Optional[Union[str, SimpleAttributeAggregationFunction, Ref, GetAtt, Sub]] = None
    value_for_multiple_values: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AxisDataOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "date_axis_options": "DateAxisOptions",
        "numeric_axis_options": "NumericAxisOptions",
    }

    date_axis_options: Optional[DateAxisOptions] = None
    numeric_axis_options: Optional[NumericAxisOptions] = None


@dataclass
class AxisDisplayMinMaxRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
    }

    minimum: Optional[Union[float, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class AxisDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_options": "DataOptions",
        "tick_label_options": "TickLabelOptions",
        "axis_offset": "AxisOffset",
        "axis_line_visibility": "AxisLineVisibility",
        "grid_line_visibility": "GridLineVisibility",
        "scrollbar_options": "ScrollbarOptions",
    }

    data_options: Optional[AxisDataOptions] = None
    tick_label_options: Optional[AxisTickLabelOptions] = None
    axis_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None
    axis_line_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    grid_line_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    scrollbar_options: Optional[ScrollBarOptions] = None


@dataclass
class AxisDisplayRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_driven": "DataDriven",
        "min_max": "MinMax",
    }

    data_driven: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    min_max: Optional[AxisDisplayMinMaxRange] = None


@dataclass
class AxisLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
        "apply_to": "ApplyTo",
        "font_configuration": "FontConfiguration",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    apply_to: Optional[AxisLabelReferenceOptions] = None
    font_configuration: Optional[FontConfiguration] = None


@dataclass
class AxisLabelReferenceOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "field_id": "FieldId",
    }

    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AxisLinearScale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "step_size": "StepSize",
        "step_count": "StepCount",
    }

    step_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    step_count: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class AxisLogarithmicScale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "base": "Base",
    }

    base: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class AxisScale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logarithmic": "Logarithmic",
        "linear": "Linear",
    }

    logarithmic: Optional[AxisLogarithmicScale] = None
    linear: Optional[AxisLinearScale] = None


@dataclass
class AxisTickLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rotation_angle": "RotationAngle",
        "label_options": "LabelOptions",
    }

    rotation_angle: Optional[Union[float, Ref, GetAtt, Sub]] = None
    label_options: Optional[LabelOptions] = None


@dataclass
class BarChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "colors": "Colors",
        "values": "Values",
        "small_multiples": "SmallMultiples",
    }

    category: Optional[list[DimensionField]] = None
    colors: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None
    small_multiples: Optional[list[DimensionField]] = None


@dataclass
class BarChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "reference_lines": "ReferenceLines",
        "data_labels": "DataLabels",
        "color_label_options": "ColorLabelOptions",
        "category_label_options": "CategoryLabelOptions",
        "tooltip": "Tooltip",
        "small_multiples_options": "SmallMultiplesOptions",
        "orientation": "Orientation",
        "visual_palette": "VisualPalette",
        "value_label_options": "ValueLabelOptions",
        "bars_arrangement": "BarsArrangement",
        "category_axis": "CategoryAxis",
        "contribution_analysis_defaults": "ContributionAnalysisDefaults",
        "field_wells": "FieldWells",
        "value_axis": "ValueAxis",
        "interactions": "Interactions",
    }

    sort_configuration: Optional[BarChartSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    reference_lines: Optional[list[ReferenceLine]] = None
    data_labels: Optional[DataLabelOptions] = None
    color_label_options: Optional[ChartAxisLabelOptions] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    tooltip: Optional[TooltipOptions] = None
    small_multiples_options: Optional[SmallMultiplesOptions] = None
    orientation: Optional[Union[str, BarChartOrientation, Ref, GetAtt, Sub]] = None
    visual_palette: Optional[VisualPalette] = None
    value_label_options: Optional[ChartAxisLabelOptions] = None
    bars_arrangement: Optional[Union[str, BarsArrangement, Ref, GetAtt, Sub]] = None
    category_axis: Optional[AxisDisplayOptions] = None
    contribution_analysis_defaults: Optional[list[ContributionAnalysisDefault]] = None
    field_wells: Optional[BarChartFieldWells] = None
    value_axis: Optional[AxisDisplayOptions] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class BarChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bar_chart_aggregated_field_wells": "BarChartAggregatedFieldWells",
    }

    bar_chart_aggregated_field_wells: Optional[BarChartAggregatedFieldWells] = None


@dataclass
class BarChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "small_multiples_sort": "SmallMultiplesSort",
        "color_sort": "ColorSort",
        "color_items_limit": "ColorItemsLimit",
        "category_items_limit": "CategoryItemsLimit",
        "category_sort": "CategorySort",
        "small_multiples_limit_configuration": "SmallMultiplesLimitConfiguration",
    }

    small_multiples_sort: Optional[list[FieldSortOptions]] = None
    color_sort: Optional[list[FieldSortOptions]] = None
    color_items_limit: Optional[ItemsLimitConfiguration] = None
    category_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None
    small_multiples_limit_configuration: Optional[ItemsLimitConfiguration] = None


@dataclass
class BarChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[BarChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class BinCountOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class BinWidthOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bin_count_limit": "BinCountLimit",
        "value": "Value",
    }

    bin_count_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class BodySectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
        "style": "Style",
        "page_break_configuration": "PageBreakConfiguration",
        "section_id": "SectionId",
        "repeat_configuration": "RepeatConfiguration",
    }

    content: Optional[BodySectionContent] = None
    style: Optional[SectionStyle] = None
    page_break_configuration: Optional[SectionPageBreakConfiguration] = None
    section_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repeat_configuration: Optional[BodySectionRepeatConfiguration] = None


@dataclass
class BodySectionContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "layout": "Layout",
    }

    layout: Optional[SectionLayoutConfiguration] = None


@dataclass
class BodySectionDynamicCategoryDimensionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "sort_by_metrics": "SortByMetrics",
        "limit": "Limit",
    }

    column: Optional[ColumnIdentifier] = None
    sort_by_metrics: Optional[list[ColumnSort]] = None
    limit: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class BodySectionDynamicNumericDimensionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "sort_by_metrics": "SortByMetrics",
        "limit": "Limit",
    }

    column: Optional[ColumnIdentifier] = None
    sort_by_metrics: Optional[list[ColumnSort]] = None
    limit: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class BodySectionRepeatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_configurations": "DimensionConfigurations",
        "non_repeating_visuals": "NonRepeatingVisuals",
        "page_break_configuration": "PageBreakConfiguration",
    }

    dimension_configurations: Optional[list[BodySectionRepeatDimensionConfiguration]] = None
    non_repeating_visuals: Optional[Union[list[str], Ref]] = None
    page_break_configuration: Optional[BodySectionRepeatPageBreakConfiguration] = None


@dataclass
class BodySectionRepeatDimensionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic_numeric_dimension_configuration": "DynamicNumericDimensionConfiguration",
        "dynamic_category_dimension_configuration": "DynamicCategoryDimensionConfiguration",
    }

    dynamic_numeric_dimension_configuration: Optional[BodySectionDynamicNumericDimensionConfiguration] = None
    dynamic_category_dimension_configuration: Optional[BodySectionDynamicCategoryDimensionConfiguration] = None


@dataclass
class BodySectionRepeatPageBreakConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "after": "After",
    }

    after: Optional[SectionAfterPageBreak] = None


@dataclass
class BoxPlotAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_by": "GroupBy",
        "values": "Values",
    }

    group_by: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class BoxPlotChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "reference_lines": "ReferenceLines",
        "category_axis": "CategoryAxis",
        "primary_y_axis_label_options": "PrimaryYAxisLabelOptions",
        "category_label_options": "CategoryLabelOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "box_plot_options": "BoxPlotOptions",
        "interactions": "Interactions",
        "primary_y_axis_display_options": "PrimaryYAxisDisplayOptions",
        "visual_palette": "VisualPalette",
    }

    sort_configuration: Optional[BoxPlotSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    reference_lines: Optional[list[ReferenceLine]] = None
    category_axis: Optional[AxisDisplayOptions] = None
    primary_y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[BoxPlotFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    box_plot_options: Optional[BoxPlotOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    primary_y_axis_display_options: Optional[AxisDisplayOptions] = None
    visual_palette: Optional[VisualPalette] = None


@dataclass
class BoxPlotFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "box_plot_aggregated_field_wells": "BoxPlotAggregatedFieldWells",
    }

    box_plot_aggregated_field_wells: Optional[BoxPlotAggregatedFieldWells] = None


@dataclass
class BoxPlotOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "style_options": "StyleOptions",
        "outlier_visibility": "OutlierVisibility",
        "all_data_points_visibility": "AllDataPointsVisibility",
    }

    style_options: Optional[BoxPlotStyleOptions] = None
    outlier_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    all_data_points_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class BoxPlotSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_sort": "CategorySort",
        "pagination_configuration": "PaginationConfiguration",
    }

    category_sort: Optional[list[FieldSortOptions]] = None
    pagination_configuration: Optional[PaginationConfiguration] = None


@dataclass
class BoxPlotStyleOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fill_style": "FillStyle",
    }

    fill_style: Optional[Union[str, BoxPlotFillStyle, Ref, GetAtt, Sub]] = None


@dataclass
class BoxPlotVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[BoxPlotChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class CalculatedField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "data_set_identifier": "DataSetIdentifier",
        "name": "Name",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CalculatedMeasureField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "field_id": "FieldId",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CascadingControlConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_controls": "SourceControls",
    }

    source_controls: Optional[list[CascadingControlSource]] = None


@dataclass
class CascadingControlSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_sheet_control_id": "SourceSheetControlId",
        "column_to_match": "ColumnToMatch",
    }

    source_sheet_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_to_match: Optional[ColumnIdentifier] = None


@dataclass
class CategoricalDimensionField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_id": "HierarchyId",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
    }

    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format_configuration: Optional[StringFormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CategoricalMeasureField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
    }

    aggregation_function: Optional[Union[str, CategoricalAggregationFunction, Ref, GetAtt, Sub]] = None
    format_configuration: Optional[StringFormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CategoryDrillDownFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "category_values": "CategoryValues",
    }

    column: Optional[ColumnIdentifier] = None
    category_values: Optional[Union[list[str], Ref]] = None


@dataclass
class CategoryFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration": "Configuration",
        "column": "Column",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
    }

    configuration: Optional[CategoryFilterConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CategoryFilterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_filter_list_configuration": "CustomFilterListConfiguration",
        "custom_filter_configuration": "CustomFilterConfiguration",
        "filter_list_configuration": "FilterListConfiguration",
    }

    custom_filter_list_configuration: Optional[CustomFilterListConfiguration] = None
    custom_filter_configuration: Optional[CustomFilterConfiguration] = None
    filter_list_configuration: Optional[FilterListConfiguration] = None


@dataclass
class CategoryInnerFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration": "Configuration",
        "column": "Column",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
    }

    configuration: Optional[CategoryFilterConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None


@dataclass
class ChartAxisLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
        "sort_icon_visibility": "SortIconVisibility",
        "axis_label_options": "AxisLabelOptions",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    sort_icon_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    axis_label_options: Optional[list[AxisLabelOptions]] = None


@dataclass
class ClusterMarker(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "simple_cluster_marker": "SimpleClusterMarker",
    }

    simple_cluster_marker: Optional[SimpleClusterMarker] = None


@dataclass
class ClusterMarkerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_marker": "ClusterMarker",
    }

    cluster_marker: Optional[ClusterMarker] = None


@dataclass
class ColorScale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "colors": "Colors",
        "color_fill_type": "ColorFillType",
        "null_value_color": "NullValueColor",
    }

    colors: Optional[list[DataColor]] = None
    color_fill_type: Optional[Union[str, ColorFillType, Ref, GetAtt, Sub]] = None
    null_value_color: Optional[DataColor] = None


@dataclass
class ColorsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_colors": "CustomColors",
    }

    custom_colors: Optional[list[CustomColor]] = None


@dataclass
class ColumnConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "colors_configuration": "ColorsConfiguration",
    }

    role: Optional[Union[str, ColumnRole, Ref, GetAtt, Sub]] = None
    format_configuration: Optional[FormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    colors_configuration: Optional[ColorsConfiguration] = None


@dataclass
class ColumnHierarchy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "date_time_hierarchy": "DateTimeHierarchy",
        "explicit_hierarchy": "ExplicitHierarchy",
        "predefined_hierarchy": "PredefinedHierarchy",
    }

    date_time_hierarchy: Optional[DateTimeHierarchy] = None
    explicit_hierarchy: Optional[ExplicitHierarchy] = None
    predefined_hierarchy: Optional[PredefinedHierarchy] = None


@dataclass
class ColumnIdentifier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "data_set_identifier": "DataSetIdentifier",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColumnSort(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "sort_by": "SortBy",
        "direction": "Direction",
    }

    aggregation_function: Optional[AggregationFunction] = None
    sort_by: Optional[ColumnIdentifier] = None
    direction: Optional[Union[str, SortDirection, Ref, GetAtt, Sub]] = None


@dataclass
class ColumnTooltipItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation": "Aggregation",
        "tooltip_target": "TooltipTarget",
        "column": "Column",
        "label": "Label",
        "visibility": "Visibility",
    }

    aggregation: Optional[AggregationFunction] = None
    tooltip_target: Optional[Union[str, TooltipTarget, Ref, GetAtt, Sub]] = None
    column: Optional[ColumnIdentifier] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class ComboChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bar_values": "BarValues",
        "category": "Category",
        "colors": "Colors",
        "line_values": "LineValues",
    }

    bar_values: Optional[list[MeasureField]] = None
    category: Optional[list[DimensionField]] = None
    colors: Optional[list[DimensionField]] = None
    line_values: Optional[list[MeasureField]] = None


@dataclass
class ComboChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "reference_lines": "ReferenceLines",
        "color_label_options": "ColorLabelOptions",
        "bar_data_labels": "BarDataLabels",
        "category_label_options": "CategoryLabelOptions",
        "tooltip": "Tooltip",
        "single_axis_options": "SingleAxisOptions",
        "primary_y_axis_display_options": "PrimaryYAxisDisplayOptions",
        "visual_palette": "VisualPalette",
        "bars_arrangement": "BarsArrangement",
        "secondary_y_axis_label_options": "SecondaryYAxisLabelOptions",
        "line_data_labels": "LineDataLabels",
        "category_axis": "CategoryAxis",
        "primary_y_axis_label_options": "PrimaryYAxisLabelOptions",
        "field_wells": "FieldWells",
        "secondary_y_axis_display_options": "SecondaryYAxisDisplayOptions",
        "interactions": "Interactions",
    }

    sort_configuration: Optional[ComboChartSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    reference_lines: Optional[list[ReferenceLine]] = None
    color_label_options: Optional[ChartAxisLabelOptions] = None
    bar_data_labels: Optional[DataLabelOptions] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    tooltip: Optional[TooltipOptions] = None
    single_axis_options: Optional[SingleAxisOptions] = None
    primary_y_axis_display_options: Optional[AxisDisplayOptions] = None
    visual_palette: Optional[VisualPalette] = None
    bars_arrangement: Optional[Union[str, BarsArrangement, Ref, GetAtt, Sub]] = None
    secondary_y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    line_data_labels: Optional[DataLabelOptions] = None
    category_axis: Optional[AxisDisplayOptions] = None
    primary_y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[ComboChartFieldWells] = None
    secondary_y_axis_display_options: Optional[AxisDisplayOptions] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class ComboChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "combo_chart_aggregated_field_wells": "ComboChartAggregatedFieldWells",
    }

    combo_chart_aggregated_field_wells: Optional[ComboChartAggregatedFieldWells] = None


@dataclass
class ComboChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color_sort": "ColorSort",
        "color_items_limit": "ColorItemsLimit",
        "category_items_limit": "CategoryItemsLimit",
        "category_sort": "CategorySort",
    }

    color_sort: Optional[list[FieldSortOptions]] = None
    color_items_limit: Optional[ItemsLimitConfiguration] = None
    category_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class ComboChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[ComboChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class ComparisonConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_method": "ComparisonMethod",
        "comparison_format": "ComparisonFormat",
    }

    comparison_method: Optional[Union[str, ComparisonMethod, Ref, GetAtt, Sub]] = None
    comparison_format: Optional[ComparisonFormatConfiguration] = None


@dataclass
class ComparisonFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_display_format_configuration": "NumberDisplayFormatConfiguration",
        "percentage_display_format_configuration": "PercentageDisplayFormatConfiguration",
    }

    number_display_format_configuration: Optional[NumberDisplayFormatConfiguration] = None
    percentage_display_format_configuration: Optional[PercentageDisplayFormatConfiguration] = None


@dataclass
class Computation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "period_to_date": "PeriodToDate",
        "growth_rate": "GrowthRate",
        "top_bottom_ranked": "TopBottomRanked",
        "total_aggregation": "TotalAggregation",
        "forecast": "Forecast",
        "maximum_minimum": "MaximumMinimum",
        "period_over_period": "PeriodOverPeriod",
        "metric_comparison": "MetricComparison",
        "top_bottom_movers": "TopBottomMovers",
        "unique_values": "UniqueValues",
    }

    period_to_date: Optional[PeriodToDateComputation] = None
    growth_rate: Optional[GrowthRateComputation] = None
    top_bottom_ranked: Optional[TopBottomRankedComputation] = None
    total_aggregation: Optional[TotalAggregationComputation] = None
    forecast: Optional[ForecastComputation] = None
    maximum_minimum: Optional[MaximumMinimumComputation] = None
    period_over_period: Optional[PeriodOverPeriodComputation] = None
    metric_comparison: Optional[MetricComparisonComputation] = None
    top_bottom_movers: Optional[TopBottomMoversComputation] = None
    unique_values: Optional[UniqueValuesComputation] = None


@dataclass
class ConditionalFormattingColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gradient": "Gradient",
        "solid": "Solid",
    }

    gradient: Optional[ConditionalFormattingGradientColor] = None
    solid: Optional[ConditionalFormattingSolidColor] = None


@dataclass
class ConditionalFormattingCustomIconCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "color": "Color",
        "display_configuration": "DisplayConfiguration",
        "icon_options": "IconOptions",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_configuration: Optional[ConditionalFormattingIconDisplayConfiguration] = None
    icon_options: Optional[ConditionalFormattingCustomIconOptions] = None


@dataclass
class ConditionalFormattingCustomIconOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unicode_icon": "UnicodeIcon",
        "icon": "Icon",
    }

    unicode_icon: Optional[Union[str, Ref, GetAtt, Sub]] = None
    icon: Optional[Union[str, Icon, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionalFormattingGradientColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "color": "Color",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    color: Optional[GradientColor] = None


@dataclass
class ConditionalFormattingIcon(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_condition": "CustomCondition",
        "icon_set": "IconSet",
    }

    custom_condition: Optional[ConditionalFormattingCustomIconCondition] = None
    icon_set: Optional[ConditionalFormattingIconSet] = None


@dataclass
class ConditionalFormattingIconDisplayConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "icon_display_option": "IconDisplayOption",
    }

    icon_display_option: Optional[Union[str, ConditionalFormattingIconDisplayOption, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionalFormattingIconSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "icon_set_type": "IconSetType",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    icon_set_type: Optional[Union[str, ConditionalFormattingIconSetType, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionalFormattingSolidColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "color": "Color",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContextMenuOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class ContributionAnalysisDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "measure_field_id": "MeasureFieldId",
        "contributor_dimensions": "ContributorDimensions",
    }

    measure_field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    contributor_dimensions: Optional[list[ColumnIdentifier]] = None


@dataclass
class CurrencyDisplayFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "negative_value_configuration": "NegativeValueConfiguration",
        "decimal_places_configuration": "DecimalPlacesConfiguration",
        "number_scale": "NumberScale",
        "null_value_format_configuration": "NullValueFormatConfiguration",
        "suffix": "Suffix",
        "separator_configuration": "SeparatorConfiguration",
        "symbol": "Symbol",
        "prefix": "Prefix",
    }

    negative_value_configuration: Optional[NegativeValueConfiguration] = None
    decimal_places_configuration: Optional[DecimalPlacesConfiguration] = None
    number_scale: Optional[Union[str, NumberScale, Ref, GetAtt, Sub]] = None
    null_value_format_configuration: Optional[NullValueFormatConfiguration] = None
    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    separator_configuration: Optional[NumericSeparatorConfiguration] = None
    symbol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomActionFilterOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selected_fields_configuration": "SelectedFieldsConfiguration",
        "target_visuals_configuration": "TargetVisualsConfiguration",
    }

    selected_fields_configuration: Optional[FilterOperationSelectedFieldsConfiguration] = None
    target_visuals_configuration: Optional[FilterOperationTargetVisualsConfiguration] = None


@dataclass
class CustomActionNavigationOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "local_navigation_configuration": "LocalNavigationConfiguration",
    }

    local_navigation_configuration: Optional[LocalNavigationConfiguration] = None


@dataclass
class CustomActionSetParametersOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value_configurations": "ParameterValueConfigurations",
    }

    parameter_value_configurations: Optional[list[SetParameterValueConfiguration]] = None


@dataclass
class CustomActionURLOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_template": "URLTemplate",
        "url_target": "URLTarget",
    }

    url_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url_target: Optional[Union[str, URLTargetConfiguration, Ref, GetAtt, Sub]] = None


@dataclass
class CustomColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color": "Color",
        "field_value": "FieldValue",
        "special_value": "SpecialValue",
    }

    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    special_value: Optional[Union[str, SpecialValue, Ref, GetAtt, Sub]] = None


@dataclass
class CustomContentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_url": "ContentUrl",
        "content_type": "ContentType",
        "image_scaling": "ImageScaling",
        "interactions": "Interactions",
    }

    content_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_type: Optional[Union[str, CustomContentType, Ref, GetAtt, Sub]] = None
    image_scaling: Optional[Union[str, CustomContentImageScalingConfiguration, Ref, GetAtt, Sub]] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class CustomContentVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "data_set_identifier": "DataSetIdentifier",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[CustomContentConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomFilterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_value": "CategoryValue",
        "parameter_name": "ParameterName",
        "null_option": "NullOption",
        "match_operator": "MatchOperator",
        "select_all_options": "SelectAllOptions",
    }

    category_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    match_operator: Optional[Union[str, CategoryFilterMatchOperator, Ref, GetAtt, Sub]] = None
    select_all_options: Optional[Union[str, CategoryFilterSelectAllOptions, Ref, GetAtt, Sub]] = None


@dataclass
class CustomFilterListConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_values": "CategoryValues",
        "null_option": "NullOption",
        "match_operator": "MatchOperator",
        "select_all_options": "SelectAllOptions",
    }

    category_values: Optional[Union[list[str], Ref]] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    match_operator: Optional[Union[str, CategoryFilterMatchOperator, Ref, GetAtt, Sub]] = None
    select_all_options: Optional[Union[str, CategoryFilterSelectAllOptions, Ref, GetAtt, Sub]] = None


@dataclass
class CustomNarrativeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "narrative": "Narrative",
    }

    narrative: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomParameterValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "decimal_values": "DecimalValues",
        "integer_values": "IntegerValues",
        "string_values": "StringValues",
        "date_time_values": "DateTimeValues",
    }

    decimal_values: Optional[Union[list[float], Ref]] = None
    integer_values: Optional[Union[list[float], Ref]] = None
    string_values: Optional[Union[list[str], Ref]] = None
    date_time_values: Optional[Union[list[str], Ref]] = None


@dataclass
class CustomValuesConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_null_value": "IncludeNullValue",
        "custom_values": "CustomValues",
    }

    include_null_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    custom_values: Optional[CustomParameterValues] = None


@dataclass
class DashboardError(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "message": "Message",
        "violated_entities": "ViolatedEntities",
    }

    type_: Optional[Union[str, DashboardErrorType, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    violated_entities: Optional[list[Entity]] = None


@dataclass
class DashboardPublishOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sheet_controls_option": "SheetControlsOption",
        "data_point_drill_up_down_option": "DataPointDrillUpDownOption",
        "ad_hoc_filtering_option": "AdHocFilteringOption",
        "visual_publish_options": "VisualPublishOptions",
        "data_stories_sharing_option": "DataStoriesSharingOption",
        "visual_axis_sort_option": "VisualAxisSortOption",
        "export_with_hidden_fields_option": "ExportWithHiddenFieldsOption",
        "quick_suite_actions_option": "QuickSuiteActionsOption",
        "executive_summary_option": "ExecutiveSummaryOption",
        "export_to_csv_option": "ExportToCSVOption",
        "data_point_menu_label_option": "DataPointMenuLabelOption",
        "visual_menu_option": "VisualMenuOption",
        "data_point_tooltip_option": "DataPointTooltipOption",
        "data_qa_enabled_option": "DataQAEnabledOption",
        "sheet_layout_element_maximization_option": "SheetLayoutElementMaximizationOption",
    }

    sheet_controls_option: Optional[SheetControlsOption] = None
    data_point_drill_up_down_option: Optional[DataPointDrillUpDownOption] = None
    ad_hoc_filtering_option: Optional[AdHocFilteringOption] = None
    visual_publish_options: Optional[DashboardVisualPublishOptions] = None
    data_stories_sharing_option: Optional[DataStoriesSharingOption] = None
    visual_axis_sort_option: Optional[VisualAxisSortOption] = None
    export_with_hidden_fields_option: Optional[ExportWithHiddenFieldsOption] = None
    quick_suite_actions_option: Optional[QuickSuiteActionsOption] = None
    executive_summary_option: Optional[ExecutiveSummaryOption] = None
    export_to_csv_option: Optional[ExportToCSVOption] = None
    data_point_menu_label_option: Optional[DataPointMenuLabelOption] = None
    visual_menu_option: Optional[VisualMenuOption] = None
    data_point_tooltip_option: Optional[DataPointTooltipOption] = None
    data_qa_enabled_option: Optional[DataQAEnabledOption] = None
    sheet_layout_element_maximization_option: Optional[SheetLayoutElementMaximizationOption] = None


@dataclass
class DashboardSourceEntity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_template": "SourceTemplate",
    }

    source_template: Optional[DashboardSourceTemplate] = None


@dataclass
class DashboardSourceTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_set_references": "DataSetReferences",
        "arn": "Arn",
    }

    data_set_references: Optional[list[DataSetReference]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DashboardVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "errors": "Errors",
        "created_time": "CreatedTime",
        "description": "Description",
        "data_set_arns": "DataSetArns",
        "theme_arn": "ThemeArn",
        "arn": "Arn",
        "source_entity_arn": "SourceEntityArn",
        "version_number": "VersionNumber",
        "sheets": "Sheets",
    }

    status: Optional[Union[str, ResourceStatus, Ref, GetAtt, Sub]] = None
    errors: Optional[list[DashboardError]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_arns: Optional[Union[list[str], Ref]] = None
    theme_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_entity_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version_number: Optional[Union[float, Ref, GetAtt, Sub]] = None
    sheets: Optional[list[Sheet]] = None


@dataclass
class DashboardVersionDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "filter_groups": "FilterGroups",
        "static_files": "StaticFiles",
        "calculated_fields": "CalculatedFields",
        "data_set_identifier_declarations": "DataSetIdentifierDeclarations",
        "column_configurations": "ColumnConfigurations",
        "analysis_defaults": "AnalysisDefaults",
        "sheets": "Sheets",
        "parameter_declarations": "ParameterDeclarations",
    }

    options: Optional[AssetOptions] = None
    filter_groups: Optional[list[FilterGroup]] = None
    static_files: Optional[list[StaticFile]] = None
    calculated_fields: Optional[list[CalculatedField]] = None
    data_set_identifier_declarations: Optional[list[DataSetIdentifierDeclaration]] = None
    column_configurations: Optional[list[ColumnConfiguration]] = None
    analysis_defaults: Optional[AnalysisDefaults] = None
    sheets: Optional[list[SheetDefinition]] = None
    parameter_declarations: Optional[list[ParameterDeclaration]] = None


@dataclass
class DashboardVisualPublishOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "export_hidden_fields_option": "ExportHiddenFieldsOption",
    }

    export_hidden_fields_option: Optional[ExportHiddenFieldsOption] = None


@dataclass
class DataBarsOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "positive_color": "PositiveColor",
        "field_id": "FieldId",
        "negative_color": "NegativeColor",
    }

    positive_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    negative_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_value": "DataValue",
        "color": "Color",
    }

    data_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataFieldSeriesItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "axis_binding": "AxisBinding",
        "field_value": "FieldValue",
        "settings": "Settings",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    axis_binding: Optional[Union[str, AxisBinding, Ref, GetAtt, Sub]] = None
    field_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    settings: Optional[LineChartSeriesSettings] = None


@dataclass
class DataLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_label_types": "DataLabelTypes",
        "measure_label_visibility": "MeasureLabelVisibility",
        "position": "Position",
        "label_content": "LabelContent",
        "visibility": "Visibility",
        "totals_visibility": "TotalsVisibility",
        "overlap": "Overlap",
        "category_label_visibility": "CategoryLabelVisibility",
        "label_color": "LabelColor",
        "label_font_configuration": "LabelFontConfiguration",
    }

    data_label_types: Optional[list[DataLabelType]] = None
    measure_label_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    position: Optional[Union[str, DataLabelPosition, Ref, GetAtt, Sub]] = None
    label_content: Optional[Union[str, DataLabelContent, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    totals_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    overlap: Optional[Union[str, DataLabelOverlap, Ref, GetAtt, Sub]] = None
    category_label_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    label_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label_font_configuration: Optional[FontConfiguration] = None


@dataclass
class DataLabelType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_label_type": "MaximumLabelType",
        "data_path_label_type": "DataPathLabelType",
        "range_ends_label_type": "RangeEndsLabelType",
        "field_label_type": "FieldLabelType",
        "minimum_label_type": "MinimumLabelType",
    }

    maximum_label_type: Optional[MaximumLabelType] = None
    data_path_label_type: Optional[DataPathLabelType] = None
    range_ends_label_type: Optional[RangeEndsLabelType] = None
    field_label_type: Optional[FieldLabelType] = None
    minimum_label_type: Optional[MinimumLabelType] = None


@dataclass
class DataPathColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "element": "Element",
        "color": "Color",
        "time_granularity": "TimeGranularity",
    }

    element: Optional[DataPathValue] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None


@dataclass
class DataPathLabelType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "visibility": "Visibility",
        "field_value": "FieldValue",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    field_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPathSort(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_paths": "SortPaths",
        "direction": "Direction",
    }

    sort_paths: Optional[list[DataPathValue]] = None
    direction: Optional[Union[str, SortDirection, Ref, GetAtt, Sub]] = None


@dataclass
class DataPathType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pivot_table_data_path_type": "PivotTableDataPathType",
    }

    pivot_table_data_path_type: Optional[Union[str, PivotTableDataPathType, Ref, GetAtt, Sub]] = None


@dataclass
class DataPathValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_path_type": "DataPathType",
        "field_id": "FieldId",
        "field_value": "FieldValue",
    }

    data_path_type: Optional[DataPathType] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPointDrillUpDownOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class DataPointMenuLabelOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class DataPointTooltipOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class DataQAEnabledOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetIdentifierDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "identifier": "Identifier",
        "data_set_arn": "DataSetArn",
    }

    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_set_arn": "DataSetArn",
        "data_set_placeholder": "DataSetPlaceholder",
    }

    data_set_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_placeholder: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataStoriesSharingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class DateAxisOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "missing_date_visibility": "MissingDateVisibility",
    }

    missing_date_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class DateDimensionField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_id": "HierarchyId",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
        "date_granularity": "DateGranularity",
    }

    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format_configuration: Optional[DateTimeFormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    date_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None


@dataclass
class DateMeasureField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
    }

    aggregation_function: Optional[Union[str, DateAggregationFunction, Ref, GetAtt, Sub]] = None
    format_configuration: Optional[DateTimeFormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rolling_date": "RollingDate",
        "dynamic_value": "DynamicValue",
        "static_values": "StaticValues",
    }

    rolling_date: Optional[RollingDateConfiguration] = None
    dynamic_value: Optional[DynamicDefaultValue] = None
    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class DateTimeFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "numeric_format_configuration": "NumericFormatConfiguration",
        "null_value_format_configuration": "NullValueFormatConfiguration",
        "date_time_format": "DateTimeFormat",
    }

    numeric_format_configuration: Optional[NumericFormatConfiguration] = None
    null_value_format_configuration: Optional[NullValueFormatConfiguration] = None
    date_time_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeHierarchy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_id": "HierarchyId",
        "drill_down_filters": "DrillDownFilters",
    }

    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    drill_down_filters: Optional[list[DrillDownFilter]] = None


@dataclass
class DateTimeParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeParameterDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mapped_data_set_parameters": "MappedDataSetParameters",
        "default_values": "DefaultValues",
        "time_granularity": "TimeGranularity",
        "value_when_unset": "ValueWhenUnset",
        "name": "Name",
    }

    mapped_data_set_parameters: Optional[list[MappedDataSetParameter]] = None
    default_values: Optional[DateTimeDefaultValues] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    value_when_unset: Optional[DateTimeValueWhenUnsetConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimePickerControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
        "helper_text_visibility": "HelperTextVisibility",
        "date_icon_visibility": "DateIconVisibility",
        "date_time_format": "DateTimeFormat",
    }

    title_options: Optional[LabelOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None
    helper_text_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    date_icon_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    date_time_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeValueWhenUnsetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_when_unset_option": "ValueWhenUnsetOption",
        "custom_value": "CustomValue",
    }

    value_when_unset_option: Optional[Union[str, ValueWhenUnsetOption, Ref, GetAtt, Sub]] = None
    custom_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecimalDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic_value": "DynamicValue",
        "static_values": "StaticValues",
    }

    dynamic_value: Optional[DynamicDefaultValue] = None
    static_values: Optional[Union[list[float], Ref]] = None


@dataclass
class DecimalParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[float], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecimalParameterDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mapped_data_set_parameters": "MappedDataSetParameters",
        "default_values": "DefaultValues",
        "parameter_value_type": "ParameterValueType",
        "value_when_unset": "ValueWhenUnset",
        "name": "Name",
    }

    mapped_data_set_parameters: Optional[list[MappedDataSetParameter]] = None
    default_values: Optional[DecimalDefaultValues] = None
    parameter_value_type: Optional[Union[str, ParameterValueType, Ref, GetAtt, Sub]] = None
    value_when_unset: Optional[DecimalValueWhenUnsetConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecimalPlacesConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "decimal_places": "DecimalPlaces",
    }

    decimal_places: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DecimalValueWhenUnsetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_when_unset_option": "ValueWhenUnsetOption",
        "custom_value": "CustomValue",
    }

    value_when_unset_option: Optional[Union[str, ValueWhenUnsetOption, Ref, GetAtt, Sub]] = None
    custom_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultDateTimePickerControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "display_options": "DisplayOptions",
        "commit_mode": "CommitMode",
    }

    type_: Optional[Union[str, SheetControlDateTimePickerType, Ref, GetAtt, Sub]] = None
    display_options: Optional[DateTimePickerControlDisplayOptions] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultFilterControlConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "control_options": "ControlOptions",
        "title": "Title",
    }

    control_options: Optional[DefaultFilterControlOptions] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultFilterControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_slider_options": "DefaultSliderOptions",
        "default_relative_date_time_options": "DefaultRelativeDateTimeOptions",
        "default_text_field_options": "DefaultTextFieldOptions",
        "default_text_area_options": "DefaultTextAreaOptions",
        "default_dropdown_options": "DefaultDropdownOptions",
        "default_date_time_picker_options": "DefaultDateTimePickerOptions",
        "default_list_options": "DefaultListOptions",
    }

    default_slider_options: Optional[DefaultSliderControlOptions] = None
    default_relative_date_time_options: Optional[DefaultRelativeDateTimeControlOptions] = None
    default_text_field_options: Optional[DefaultTextFieldControlOptions] = None
    default_text_area_options: Optional[DefaultTextAreaControlOptions] = None
    default_dropdown_options: Optional[DefaultFilterDropDownControlOptions] = None
    default_date_time_picker_options: Optional[DefaultDateTimePickerControlOptions] = None
    default_list_options: Optional[DefaultFilterListControlOptions] = None


@dataclass
class DefaultFilterDropDownControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "display_options": "DisplayOptions",
        "commit_mode": "CommitMode",
        "selectable_values": "SelectableValues",
    }

    type_: Optional[Union[str, SheetControlListType, Ref, GetAtt, Sub]] = None
    display_options: Optional[DropDownControlDisplayOptions] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None
    selectable_values: Optional[FilterSelectableValues] = None


@dataclass
class DefaultFilterListControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "display_options": "DisplayOptions",
        "selectable_values": "SelectableValues",
    }

    type_: Optional[Union[str, SheetControlListType, Ref, GetAtt, Sub]] = None
    display_options: Optional[ListControlDisplayOptions] = None
    selectable_values: Optional[FilterSelectableValues] = None


@dataclass
class DefaultFreeFormLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canvas_size_options": "CanvasSizeOptions",
    }

    canvas_size_options: Optional[FreeFormLayoutCanvasSizeOptions] = None


@dataclass
class DefaultGridLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canvas_size_options": "CanvasSizeOptions",
    }

    canvas_size_options: Optional[GridLayoutCanvasSizeOptions] = None


@dataclass
class DefaultInteractiveLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "free_form": "FreeForm",
        "grid": "Grid",
    }

    free_form: Optional[DefaultFreeFormLayoutConfiguration] = None
    grid: Optional[DefaultGridLayoutConfiguration] = None


@dataclass
class DefaultNewSheetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sheet_content_type": "SheetContentType",
        "interactive_layout_configuration": "InteractiveLayoutConfiguration",
        "paginated_layout_configuration": "PaginatedLayoutConfiguration",
    }

    sheet_content_type: Optional[Union[str, SheetContentType, Ref, GetAtt, Sub]] = None
    interactive_layout_configuration: Optional[DefaultInteractiveLayoutConfiguration] = None
    paginated_layout_configuration: Optional[DefaultPaginatedLayoutConfiguration] = None


@dataclass
class DefaultPaginatedLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "section_based": "SectionBased",
    }

    section_based: Optional[DefaultSectionBasedLayoutConfiguration] = None


@dataclass
class DefaultRelativeDateTimeControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_options": "DisplayOptions",
        "commit_mode": "CommitMode",
    }

    display_options: Optional[RelativeDateTimeControlDisplayOptions] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultSectionBasedLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canvas_size_options": "CanvasSizeOptions",
    }

    canvas_size_options: Optional[SectionBasedLayoutCanvasSizeOptions] = None


@dataclass
class DefaultSliderControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "step_size": "StepSize",
        "display_options": "DisplayOptions",
        "maximum_value": "MaximumValue",
        "minimum_value": "MinimumValue",
    }

    type_: Optional[Union[str, SheetControlSliderType, Ref, GetAtt, Sub]] = None
    step_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    display_options: Optional[SliderControlDisplayOptions] = None
    maximum_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    minimum_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultTextAreaControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "display_options": "DisplayOptions",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[TextAreaControlDisplayOptions] = None


@dataclass
class DefaultTextFieldControlOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_options": "DisplayOptions",
    }

    display_options: Optional[TextFieldControlDisplayOptions] = None


@dataclass
class DestinationParameterValueConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_values_configuration": "CustomValuesConfiguration",
        "source_parameter_name": "SourceParameterName",
        "select_all_value_options": "SelectAllValueOptions",
        "source_field": "SourceField",
        "source_column": "SourceColumn",
    }

    custom_values_configuration: Optional[CustomValuesConfiguration] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    select_all_value_options: Optional[Union[str, SelectAllValueOptions, Ref, GetAtt, Sub]] = None
    source_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column: Optional[ColumnIdentifier] = None


@dataclass
class DimensionField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "date_dimension_field": "DateDimensionField",
        "numerical_dimension_field": "NumericalDimensionField",
        "categorical_dimension_field": "CategoricalDimensionField",
    }

    date_dimension_field: Optional[DateDimensionField] = None
    numerical_dimension_field: Optional[NumericalDimensionField] = None
    categorical_dimension_field: Optional[CategoricalDimensionField] = None


@dataclass
class DonutCenterOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "label_visibility": "LabelVisibility",
    }

    label_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class DonutOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "donut_center_options": "DonutCenterOptions",
        "arc_options": "ArcOptions",
    }

    donut_center_options: Optional[DonutCenterOptions] = None
    arc_options: Optional[ArcOptions] = None


@dataclass
class DrillDownFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "numeric_equality_filter": "NumericEqualityFilter",
        "time_range_filter": "TimeRangeFilter",
        "category_filter": "CategoryFilter",
    }

    numeric_equality_filter: Optional[NumericEqualityDrillDownFilter] = None
    time_range_filter: Optional[TimeRangeDrillDownFilter] = None
    category_filter: Optional[CategoryDrillDownFilter] = None


@dataclass
class DropDownControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "select_all_options": "SelectAllOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
    }

    title_options: Optional[LabelOptions] = None
    select_all_options: Optional[ListControlSelectAllOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None


@dataclass
class DynamicDefaultValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name_column": "GroupNameColumn",
        "default_value_column": "DefaultValueColumn",
        "user_name_column": "UserNameColumn",
    }

    group_name_column: Optional[ColumnIdentifier] = None
    default_value_column: Optional[ColumnIdentifier] = None
    user_name_column: Optional[ColumnIdentifier] = None


@dataclass
class EmptyVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visual_id": "VisualId",
        "actions": "Actions",
        "data_set_identifier": "DataSetIdentifier",
    }

    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    actions: Optional[list[VisualCustomAction]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Entity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExcludePeriodConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "amount": "Amount",
        "granularity": "Granularity",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    amount: Optional[Union[float, Ref, GetAtt, Sub]] = None
    granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None


@dataclass
class ExecutiveSummaryOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class ExplicitHierarchy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_id": "HierarchyId",
        "drill_down_filters": "DrillDownFilters",
        "columns": "Columns",
    }

    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    drill_down_filters: Optional[list[DrillDownFilter]] = None
    columns: Optional[list[ColumnIdentifier]] = None


@dataclass
class ExportHiddenFieldsOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class ExportToCSVOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class ExportWithHiddenFieldsOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class FieldBasedTooltip(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tooltip_fields": "TooltipFields",
        "aggregation_visibility": "AggregationVisibility",
        "tooltip_title_type": "TooltipTitleType",
    }

    tooltip_fields: Optional[list[TooltipItem]] = None
    aggregation_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    tooltip_title_type: Optional[Union[str, TooltipTitleType, Ref, GetAtt, Sub]] = None


@dataclass
class FieldLabelType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "visibility": "Visibility",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class FieldSeriesItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "axis_binding": "AxisBinding",
        "settings": "Settings",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    axis_binding: Optional[Union[str, AxisBinding, Ref, GetAtt, Sub]] = None
    settings: Optional[LineChartSeriesSettings] = None


@dataclass
class FieldSort(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "direction": "Direction",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    direction: Optional[Union[str, SortDirection, Ref, GetAtt, Sub]] = None


@dataclass
class FieldSortOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_sort": "FieldSort",
        "column_sort": "ColumnSort",
    }

    field_sort: Optional[FieldSort] = None
    column_sort: Optional[ColumnSort] = None


@dataclass
class FieldTooltipItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tooltip_target": "TooltipTarget",
        "field_id": "FieldId",
        "label": "Label",
        "visibility": "Visibility",
    }

    tooltip_target: Optional[Union[str, TooltipTarget, Ref, GetAtt, Sub]] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class FilledMapAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "geospatial": "Geospatial",
    }

    values: Optional[list[MeasureField]] = None
    geospatial: Optional[list[DimensionField]] = None


@dataclass
class FilledMapConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditional_formatting_options": "ConditionalFormattingOptions",
    }

    conditional_formatting_options: Optional[list[FilledMapConditionalFormattingOption]] = None


@dataclass
class FilledMapConditionalFormattingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "shape": "Shape",
    }

    shape: Optional[FilledMapShapeConditionalFormatting] = None


@dataclass
class FilledMapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "map_style_options": "MapStyleOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "interactions": "Interactions",
        "window_options": "WindowOptions",
    }

    sort_configuration: Optional[FilledMapSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    map_style_options: Optional[GeospatialMapStyleOptions] = None
    field_wells: Optional[FilledMapFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    window_options: Optional[GeospatialWindowOptions] = None


@dataclass
class FilledMapFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filled_map_aggregated_field_wells": "FilledMapAggregatedFieldWells",
    }

    filled_map_aggregated_field_wells: Optional[FilledMapAggregatedFieldWells] = None


@dataclass
class FilledMapShapeConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "field_id": "FieldId",
    }

    format: Optional[ShapeConditionalFormat] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilledMapSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_sort": "CategorySort",
    }

    category_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class FilledMapVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "conditional_formatting": "ConditionalFormatting",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    conditional_formatting: Optional[FilledMapConditionalFormatting] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[FilledMapConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nested_filter": "NestedFilter",
        "numeric_equality_filter": "NumericEqualityFilter",
        "numeric_range_filter": "NumericRangeFilter",
        "time_range_filter": "TimeRangeFilter",
        "relative_dates_filter": "RelativeDatesFilter",
        "top_bottom_filter": "TopBottomFilter",
        "time_equality_filter": "TimeEqualityFilter",
        "category_filter": "CategoryFilter",
    }

    nested_filter: Optional[NestedFilter] = None
    numeric_equality_filter: Optional[NumericEqualityFilter] = None
    numeric_range_filter: Optional[NumericRangeFilter] = None
    time_range_filter: Optional[TimeRangeFilter] = None
    relative_dates_filter: Optional[RelativeDatesFilter] = None
    top_bottom_filter: Optional[TopBottomFilter] = None
    time_equality_filter: Optional[TimeEqualityFilter] = None
    category_filter: Optional[CategoryFilter] = None


@dataclass
class FilterControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slider": "Slider",
        "text_area": "TextArea",
        "dropdown": "Dropdown",
        "text_field": "TextField",
        "list": "List",
        "date_time_picker": "DateTimePicker",
        "relative_date_time": "RelativeDateTime",
        "cross_sheet": "CrossSheet",
    }

    slider: Optional[FilterSliderControl] = None
    text_area: Optional[FilterTextAreaControl] = None
    dropdown: Optional[FilterDropDownControl] = None
    text_field: Optional[FilterTextFieldControl] = None
    list: Optional[FilterListControl] = None
    date_time_picker: Optional[FilterDateTimePickerControl] = None
    relative_date_time: Optional[FilterRelativeDateTimeControl] = None
    cross_sheet: Optional[FilterCrossSheetControl] = None


@dataclass
class FilterCrossSheetControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "cascading_control_configuration": "CascadingControlConfiguration",
        "source_filter_id": "SourceFilterId",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cascading_control_configuration: Optional[CascadingControlConfiguration] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterDateTimePickerControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "type_": "Type",
        "display_options": "DisplayOptions",
        "title": "Title",
        "commit_mode": "CommitMode",
        "source_filter_id": "SourceFilterId",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SheetControlDateTimePickerType, Ref, GetAtt, Sub]] = None
    display_options: Optional[DateTimePickerControlDisplayOptions] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterDropDownControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "type_": "Type",
        "display_options": "DisplayOptions",
        "cascading_control_configuration": "CascadingControlConfiguration",
        "title": "Title",
        "commit_mode": "CommitMode",
        "source_filter_id": "SourceFilterId",
        "selectable_values": "SelectableValues",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SheetControlListType, Ref, GetAtt, Sub]] = None
    display_options: Optional[DropDownControlDisplayOptions] = None
    cascading_control_configuration: Optional[CascadingControlConfiguration] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    selectable_values: Optional[FilterSelectableValues] = None


@dataclass
class FilterGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "filters": "Filters",
        "cross_dataset": "CrossDataset",
        "scope_configuration": "ScopeConfiguration",
        "filter_group_id": "FilterGroupId",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    filters: Optional[list[Filter]] = None
    cross_dataset: Optional[Union[str, CrossDatasetTypes, Ref, GetAtt, Sub]] = None
    scope_configuration: Optional[FilterScopeConfiguration] = None
    filter_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterListConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_values": "CategoryValues",
        "null_option": "NullOption",
        "match_operator": "MatchOperator",
        "select_all_options": "SelectAllOptions",
    }

    category_values: Optional[Union[list[str], Ref]] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    match_operator: Optional[Union[str, CategoryFilterMatchOperator, Ref, GetAtt, Sub]] = None
    select_all_options: Optional[Union[str, CategoryFilterSelectAllOptions, Ref, GetAtt, Sub]] = None


@dataclass
class FilterListControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "type_": "Type",
        "display_options": "DisplayOptions",
        "cascading_control_configuration": "CascadingControlConfiguration",
        "title": "Title",
        "source_filter_id": "SourceFilterId",
        "selectable_values": "SelectableValues",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SheetControlListType, Ref, GetAtt, Sub]] = None
    display_options: Optional[ListControlDisplayOptions] = None
    cascading_control_configuration: Optional[CascadingControlConfiguration] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    selectable_values: Optional[FilterSelectableValues] = None


@dataclass
class FilterOperationSelectedFieldsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selected_columns": "SelectedColumns",
        "selected_fields": "SelectedFields",
        "selected_field_options": "SelectedFieldOptions",
    }

    selected_columns: Optional[list[ColumnIdentifier]] = None
    selected_fields: Optional[Union[list[str], Ref]] = None
    selected_field_options: Optional[Union[str, SelectedFieldOptions, Ref, GetAtt, Sub]] = None


@dataclass
class FilterOperationTargetVisualsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "same_sheet_target_visual_configuration": "SameSheetTargetVisualConfiguration",
    }

    same_sheet_target_visual_configuration: Optional[SameSheetTargetVisualConfiguration] = None


@dataclass
class FilterRelativeDateTimeControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "display_options": "DisplayOptions",
        "title": "Title",
        "commit_mode": "CommitMode",
        "source_filter_id": "SourceFilterId",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[RelativeDateTimeControlDisplayOptions] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterScopeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "all_sheets": "AllSheets",
        "selected_sheets": "SelectedSheets",
    }

    all_sheets: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    selected_sheets: Optional[SelectedSheetsFilterScopeConfiguration] = None


@dataclass
class FilterSelectableValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[Union[list[str], Ref]] = None


@dataclass
class FilterSliderControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "type_": "Type",
        "step_size": "StepSize",
        "display_options": "DisplayOptions",
        "title": "Title",
        "maximum_value": "MaximumValue",
        "source_filter_id": "SourceFilterId",
        "minimum_value": "MinimumValue",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SheetControlSliderType, Ref, GetAtt, Sub]] = None
    step_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    display_options: Optional[SliderControlDisplayOptions] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class FilterTextAreaControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "delimiter": "Delimiter",
        "display_options": "DisplayOptions",
        "title": "Title",
        "source_filter_id": "SourceFilterId",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[TextAreaControlDisplayOptions] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterTextFieldControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_control_id": "FilterControlId",
        "display_options": "DisplayOptions",
        "title": "Title",
        "source_filter_id": "SourceFilterId",
    }

    filter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[TextFieldControlDisplayOptions] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FontConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "font_family": "FontFamily",
        "font_style": "FontStyle",
        "font_size": "FontSize",
        "font_decoration": "FontDecoration",
        "font_color": "FontColor",
        "font_weight": "FontWeight",
    }

    font_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    font_style: Optional[Union[str, FontStyle, Ref, GetAtt, Sub]] = None
    font_size: Optional[FontSize] = None
    font_decoration: Optional[Union[str, FontDecoration, Ref, GetAtt, Sub]] = None
    font_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    font_weight: Optional[FontWeight] = None


@dataclass
class FontSize(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "relative": "Relative",
        "absolute": "Absolute",
    }

    relative: Optional[Union[str, RelativeFontSize, Ref, GetAtt, Sub]] = None
    absolute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FontWeight(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, FontWeightName, Ref, GetAtt, Sub]] = None


@dataclass
class ForecastComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "periods_backward": "PeriodsBackward",
        "periods_forward": "PeriodsForward",
        "prediction_interval": "PredictionInterval",
        "seasonality": "Seasonality",
        "custom_seasonality_value": "CustomSeasonalityValue",
        "value": "Value",
        "time": "Time",
        "upper_boundary": "UpperBoundary",
        "computation_id": "ComputationId",
        "name": "Name",
        "lower_boundary": "LowerBoundary",
    }

    periods_backward: Optional[Union[float, Ref, GetAtt, Sub]] = None
    periods_forward: Optional[Union[float, Ref, GetAtt, Sub]] = None
    prediction_interval: Optional[Union[float, Ref, GetAtt, Sub]] = None
    seasonality: Optional[Union[str, ForecastComputationSeasonality, Ref, GetAtt, Sub]] = None
    custom_seasonality_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    value: Optional[MeasureField] = None
    time: Optional[DimensionField] = None
    upper_boundary: Optional[Union[float, Ref, GetAtt, Sub]] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lower_boundary: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ForecastConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forecast_properties": "ForecastProperties",
        "scenario": "Scenario",
    }

    forecast_properties: Optional[TimeBasedForecastProperties] = None
    scenario: Optional[ForecastScenario] = None


@dataclass
class ForecastScenario(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "what_if_range_scenario": "WhatIfRangeScenario",
        "what_if_point_scenario": "WhatIfPointScenario",
    }

    what_if_range_scenario: Optional[WhatIfRangeScenario] = None
    what_if_point_scenario: Optional[WhatIfPointScenario] = None


@dataclass
class FormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_format_configuration": "NumberFormatConfiguration",
        "date_time_format_configuration": "DateTimeFormatConfiguration",
        "string_format_configuration": "StringFormatConfiguration",
    }

    number_format_configuration: Optional[NumberFormatConfiguration] = None
    date_time_format_configuration: Optional[DateTimeFormatConfiguration] = None
    string_format_configuration: Optional[StringFormatConfiguration] = None


@dataclass
class FreeFormLayoutCanvasSizeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "screen_canvas_size_options": "ScreenCanvasSizeOptions",
    }

    screen_canvas_size_options: Optional[FreeFormLayoutScreenCanvasSizeOptions] = None


@dataclass
class FreeFormLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canvas_size_options": "CanvasSizeOptions",
        "elements": "Elements",
    }

    canvas_size_options: Optional[FreeFormLayoutCanvasSizeOptions] = None
    elements: Optional[list[FreeFormLayoutElement]] = None


@dataclass
class FreeFormLayoutElement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "element_type": "ElementType",
        "border_style": "BorderStyle",
        "height": "Height",
        "visibility": "Visibility",
        "rendering_rules": "RenderingRules",
        "y_axis_location": "YAxisLocation",
        "loading_animation": "LoadingAnimation",
        "width": "Width",
        "background_style": "BackgroundStyle",
        "element_id": "ElementId",
        "x_axis_location": "XAxisLocation",
        "selected_border_style": "SelectedBorderStyle",
    }

    element_type: Optional[Union[str, LayoutElementType, Ref, GetAtt, Sub]] = None
    border_style: Optional[FreeFormLayoutElementBorderStyle] = None
    height: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    rendering_rules: Optional[list[SheetElementRenderingRule]] = None
    y_axis_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    loading_animation: Optional[LoadingAnimation] = None
    width: Optional[Union[str, Ref, GetAtt, Sub]] = None
    background_style: Optional[FreeFormLayoutElementBackgroundStyle] = None
    element_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    x_axis_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    selected_border_style: Optional[FreeFormLayoutElementBorderStyle] = None


@dataclass
class FreeFormLayoutElementBackgroundStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color": "Color",
        "visibility": "Visibility",
    }

    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class FreeFormLayoutElementBorderStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color": "Color",
        "visibility": "Visibility",
    }

    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class FreeFormLayoutScreenCanvasSizeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "optimized_view_port_width": "OptimizedViewPortWidth",
    }

    optimized_view_port_width: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FreeFormSectionLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "elements": "Elements",
    }

    elements: Optional[list[FreeFormLayoutElement]] = None


@dataclass
class FunnelChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "values": "Values",
    }

    category: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class FunnelChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "data_label_options": "DataLabelOptions",
        "category_label_options": "CategoryLabelOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "interactions": "Interactions",
        "value_label_options": "ValueLabelOptions",
        "visual_palette": "VisualPalette",
    }

    sort_configuration: Optional[FunnelChartSortConfiguration] = None
    data_label_options: Optional[FunnelChartDataLabelOptions] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[FunnelChartFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    value_label_options: Optional[ChartAxisLabelOptions] = None
    visual_palette: Optional[VisualPalette] = None


@dataclass
class FunnelChartDataLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "measure_label_visibility": "MeasureLabelVisibility",
        "position": "Position",
        "visibility": "Visibility",
        "category_label_visibility": "CategoryLabelVisibility",
        "label_color": "LabelColor",
        "measure_data_label_style": "MeasureDataLabelStyle",
        "label_font_configuration": "LabelFontConfiguration",
    }

    measure_label_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    position: Optional[Union[str, DataLabelPosition, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    category_label_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    label_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure_data_label_style: Optional[Union[str, FunnelChartMeasureDataLabelStyle, Ref, GetAtt, Sub]] = None
    label_font_configuration: Optional[FontConfiguration] = None


@dataclass
class FunnelChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "funnel_chart_aggregated_field_wells": "FunnelChartAggregatedFieldWells",
    }

    funnel_chart_aggregated_field_wells: Optional[FunnelChartAggregatedFieldWells] = None


@dataclass
class FunnelChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_items_limit": "CategoryItemsLimit",
        "category_sort": "CategorySort",
    }

    category_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class FunnelChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[FunnelChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class GaugeChartArcConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "foreground_color": "ForegroundColor",
    }

    foreground_color: Optional[ConditionalFormattingColor] = None


@dataclass
class GaugeChartColorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "foreground_color": "ForegroundColor",
        "background_color": "BackgroundColor",
    }

    foreground_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GaugeChartConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditional_formatting_options": "ConditionalFormattingOptions",
    }

    conditional_formatting_options: Optional[list[GaugeChartConditionalFormattingOption]] = None


@dataclass
class GaugeChartConditionalFormattingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arc": "Arc",
        "primary_value": "PrimaryValue",
    }

    arc: Optional[GaugeChartArcConditionalFormatting] = None
    primary_value: Optional[GaugeChartPrimaryValueConditionalFormatting] = None


@dataclass
class GaugeChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_labels": "DataLabels",
        "field_wells": "FieldWells",
        "tooltip_options": "TooltipOptions",
        "gauge_chart_options": "GaugeChartOptions",
        "color_configuration": "ColorConfiguration",
        "interactions": "Interactions",
        "visual_palette": "VisualPalette",
    }

    data_labels: Optional[DataLabelOptions] = None
    field_wells: Optional[GaugeChartFieldWells] = None
    tooltip_options: Optional[TooltipOptions] = None
    gauge_chart_options: Optional[GaugeChartOptions] = None
    color_configuration: Optional[GaugeChartColorConfiguration] = None
    interactions: Optional[VisualInteractionOptions] = None
    visual_palette: Optional[VisualPalette] = None


@dataclass
class GaugeChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_values": "TargetValues",
        "values": "Values",
    }

    target_values: Optional[list[MeasureField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class GaugeChartOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arc": "Arc",
        "comparison": "Comparison",
        "primary_value_display_type": "PrimaryValueDisplayType",
        "arc_axis": "ArcAxis",
        "primary_value_font_configuration": "PrimaryValueFontConfiguration",
    }

    arc: Optional[ArcConfiguration] = None
    comparison: Optional[ComparisonConfiguration] = None
    primary_value_display_type: Optional[Union[str, PrimaryValueDisplayType, Ref, GetAtt, Sub]] = None
    arc_axis: Optional[ArcAxisConfiguration] = None
    primary_value_font_configuration: Optional[FontConfiguration] = None


@dataclass
class GaugeChartPrimaryValueConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_color": "TextColor",
        "icon": "Icon",
    }

    text_color: Optional[ConditionalFormattingColor] = None
    icon: Optional[ConditionalFormattingIcon] = None


@dataclass
class GaugeChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "conditional_formatting": "ConditionalFormatting",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    conditional_formatting: Optional[GaugeChartConditionalFormatting] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[GaugeChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialCategoricalColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_data_colors": "CategoryDataColors",
        "default_opacity": "DefaultOpacity",
        "null_data_visibility": "NullDataVisibility",
        "null_data_settings": "NullDataSettings",
    }

    category_data_colors: Optional[list[GeospatialCategoricalDataColor]] = None
    default_opacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    null_data_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    null_data_settings: Optional[GeospatialNullDataSettings] = None


@dataclass
class GeospatialCategoricalDataColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_value": "DataValue",
        "color": "Color",
    }

    data_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialCircleRadius(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "radius": "Radius",
    }

    radius: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialCircleSymbolStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fill_color": "FillColor",
        "stroke_width": "StrokeWidth",
        "stroke_color": "StrokeColor",
        "circle_radius": "CircleRadius",
    }

    fill_color: Optional[GeospatialColor] = None
    stroke_width: Optional[GeospatialLineWidth] = None
    stroke_color: Optional[GeospatialColor] = None
    circle_radius: Optional[GeospatialCircleRadius] = None


@dataclass
class GeospatialColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gradient": "Gradient",
        "categorical": "Categorical",
        "solid": "Solid",
    }

    gradient: Optional[GeospatialGradientColor] = None
    categorical: Optional[GeospatialCategoricalColor] = None
    solid: Optional[GeospatialSolidColor] = None


@dataclass
class GeospatialCoordinateBounds(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "west": "West",
        "south": "South",
        "north": "North",
        "east": "East",
    }

    west: Optional[Union[float, Ref, GetAtt, Sub]] = None
    south: Optional[Union[float, Ref, GetAtt, Sub]] = None
    north: Optional[Union[float, Ref, GetAtt, Sub]] = None
    east: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialDataSourceItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_file_data_source": "StaticFileDataSource",
    }

    static_file_data_source: Optional[GeospatialStaticFileSource] = None


@dataclass
class GeospatialGradientColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_opacity": "DefaultOpacity",
        "step_colors": "StepColors",
        "null_data_visibility": "NullDataVisibility",
        "null_data_settings": "NullDataSettings",
    }

    default_opacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    step_colors: Optional[list[GeospatialGradientStepColor]] = None
    null_data_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    null_data_settings: Optional[GeospatialNullDataSettings] = None


@dataclass
class GeospatialGradientStepColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_value": "DataValue",
        "color": "Color",
    }

    data_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialHeatmapColorScale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "colors": "Colors",
    }

    colors: Optional[list[GeospatialHeatmapDataColor]] = None


@dataclass
class GeospatialHeatmapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "heatmap_color": "HeatmapColor",
    }

    heatmap_color: Optional[GeospatialHeatmapColorScale] = None


@dataclass
class GeospatialHeatmapDataColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color": "Color",
    }

    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialLayerColorField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color_values_fields": "ColorValuesFields",
        "color_dimensions_fields": "ColorDimensionsFields",
    }

    color_values_fields: Optional[list[MeasureField]] = None
    color_dimensions_fields: Optional[list[DimensionField]] = None


@dataclass
class GeospatialLayerDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "point_layer": "PointLayer",
        "polygon_layer": "PolygonLayer",
        "line_layer": "LineLayer",
    }

    point_layer: Optional[GeospatialPointLayer] = None
    polygon_layer: Optional[GeospatialPolygonLayer] = None
    line_layer: Optional[GeospatialLineLayer] = None


@dataclass
class GeospatialLayerItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "layer_id": "LayerId",
        "join_definition": "JoinDefinition",
        "actions": "Actions",
        "layer_type": "LayerType",
        "layer_definition": "LayerDefinition",
        "tooltip": "Tooltip",
        "label": "Label",
        "visibility": "Visibility",
        "data_source": "DataSource",
    }

    layer_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    join_definition: Optional[GeospatialLayerJoinDefinition] = None
    actions: Optional[list[LayerCustomAction]] = None
    layer_type: Optional[Union[str, GeospatialLayerType, Ref, GetAtt, Sub]] = None
    layer_definition: Optional[GeospatialLayerDefinition] = None
    tooltip: Optional[TooltipOptions] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    data_source: Optional[GeospatialDataSourceItem] = None


@dataclass
class GeospatialLayerJoinDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color_field": "ColorField",
        "shape_key_field": "ShapeKeyField",
        "dataset_key_field": "DatasetKeyField",
    }

    color_field: Optional[GeospatialLayerColorField] = None
    shape_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataset_key_field: Optional[UnaggregatedField] = None


@dataclass
class GeospatialLayerMapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "legend": "Legend",
        "map_state": "MapState",
        "map_style": "MapStyle",
        "interactions": "Interactions",
        "map_layers": "MapLayers",
    }

    legend: Optional[LegendOptions] = None
    map_state: Optional[GeospatialMapState] = None
    map_style: Optional[GeospatialMapStyle] = None
    interactions: Optional[VisualInteractionOptions] = None
    map_layers: Optional[list[GeospatialLayerItem]] = None


@dataclass
class GeospatialLineLayer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "style": "Style",
    }

    style: Optional[GeospatialLineStyle] = None


@dataclass
class GeospatialLineStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_symbol_style": "LineSymbolStyle",
    }

    line_symbol_style: Optional[GeospatialLineSymbolStyle] = None


@dataclass
class GeospatialLineSymbolStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fill_color": "FillColor",
        "line_width": "LineWidth",
    }

    fill_color: Optional[GeospatialColor] = None
    line_width: Optional[GeospatialLineWidth] = None


@dataclass
class GeospatialLineWidth(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_width": "LineWidth",
    }

    line_width: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialMapAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "colors": "Colors",
        "values": "Values",
        "geospatial": "Geospatial",
    }

    colors: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None
    geospatial: Optional[list[DimensionField]] = None


@dataclass
class GeospatialMapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "legend": "Legend",
        "map_style_options": "MapStyleOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "interactions": "Interactions",
        "window_options": "WindowOptions",
        "point_style_options": "PointStyleOptions",
        "visual_palette": "VisualPalette",
    }

    legend: Optional[LegendOptions] = None
    map_style_options: Optional[GeospatialMapStyleOptions] = None
    field_wells: Optional[GeospatialMapFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    window_options: Optional[GeospatialWindowOptions] = None
    point_style_options: Optional[GeospatialPointStyleOptions] = None
    visual_palette: Optional[VisualPalette] = None


@dataclass
class GeospatialMapFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "geospatial_map_aggregated_field_wells": "GeospatialMapAggregatedFieldWells",
    }

    geospatial_map_aggregated_field_wells: Optional[GeospatialMapAggregatedFieldWells] = None


@dataclass
class GeospatialMapState(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bounds": "Bounds",
        "map_navigation": "MapNavigation",
    }

    bounds: Optional[GeospatialCoordinateBounds] = None
    map_navigation: Optional[Union[str, GeospatialMapNavigation, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialMapStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "base_map_style": "BaseMapStyle",
        "base_map_visibility": "BaseMapVisibility",
        "background_color": "BackgroundColor",
    }

    base_map_style: Optional[Union[str, BaseMapStyleType, Ref, GetAtt, Sub]] = None
    base_map_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialMapStyleOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "base_map_style": "BaseMapStyle",
    }

    base_map_style: Optional[Union[str, BaseMapStyleType, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialMapVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[GeospatialMapConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class GeospatialNullDataSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "symbol_style": "SymbolStyle",
    }

    symbol_style: Optional[GeospatialNullSymbolStyle] = None


@dataclass
class GeospatialNullSymbolStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fill_color": "FillColor",
        "stroke_width": "StrokeWidth",
        "stroke_color": "StrokeColor",
    }

    fill_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stroke_width: Optional[Union[float, Ref, GetAtt, Sub]] = None
    stroke_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialPointLayer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "style": "Style",
    }

    style: Optional[GeospatialPointStyle] = None


@dataclass
class GeospatialPointStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "circle_symbol_style": "CircleSymbolStyle",
    }

    circle_symbol_style: Optional[GeospatialCircleSymbolStyle] = None


@dataclass
class GeospatialPointStyleOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selected_point_style": "SelectedPointStyle",
        "cluster_marker_configuration": "ClusterMarkerConfiguration",
        "heatmap_configuration": "HeatmapConfiguration",
    }

    selected_point_style: Optional[Union[str, GeospatialSelectedPointStyle, Ref, GetAtt, Sub]] = None
    cluster_marker_configuration: Optional[ClusterMarkerConfiguration] = None
    heatmap_configuration: Optional[GeospatialHeatmapConfiguration] = None


@dataclass
class GeospatialPolygonLayer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "style": "Style",
    }

    style: Optional[GeospatialPolygonStyle] = None


@dataclass
class GeospatialPolygonStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "polygon_symbol_style": "PolygonSymbolStyle",
    }

    polygon_symbol_style: Optional[GeospatialPolygonSymbolStyle] = None


@dataclass
class GeospatialPolygonSymbolStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fill_color": "FillColor",
        "stroke_width": "StrokeWidth",
        "stroke_color": "StrokeColor",
    }

    fill_color: Optional[GeospatialColor] = None
    stroke_width: Optional[GeospatialLineWidth] = None
    stroke_color: Optional[GeospatialColor] = None


@dataclass
class GeospatialSolidColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "color": "Color",
    }

    state: Optional[Union[str, GeospatialColorState, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialStaticFileSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_file_id": "StaticFileId",
    }

    static_file_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeospatialWindowOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bounds": "Bounds",
        "map_zoom_mode": "MapZoomMode",
    }

    bounds: Optional[GeospatialCoordinateBounds] = None
    map_zoom_mode: Optional[Union[str, MapZoomMode, Ref, GetAtt, Sub]] = None


@dataclass
class GlobalTableBorderOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uniform_border": "UniformBorder",
        "side_specific_border": "SideSpecificBorder",
    }

    uniform_border: Optional[TableBorderOptions] = None
    side_specific_border: Optional[TableSideBorderOptions] = None


@dataclass
class GradientColor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stops": "Stops",
    }

    stops: Optional[list[GradientStop]] = None


@dataclass
class GradientStop(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gradient_offset": "GradientOffset",
        "data_value": "DataValue",
        "color": "Color",
    }

    gradient_offset: Optional[Union[float, Ref, GetAtt, Sub]] = None
    data_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GridLayoutCanvasSizeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "screen_canvas_size_options": "ScreenCanvasSizeOptions",
    }

    screen_canvas_size_options: Optional[GridLayoutScreenCanvasSizeOptions] = None


@dataclass
class GridLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canvas_size_options": "CanvasSizeOptions",
        "elements": "Elements",
    }

    canvas_size_options: Optional[GridLayoutCanvasSizeOptions] = None
    elements: Optional[list[GridLayoutElement]] = None


@dataclass
class GridLayoutElement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "element_type": "ElementType",
        "column_span": "ColumnSpan",
        "column_index": "ColumnIndex",
        "row_index": "RowIndex",
        "row_span": "RowSpan",
        "element_id": "ElementId",
    }

    element_type: Optional[Union[str, LayoutElementType, Ref, GetAtt, Sub]] = None
    column_span: Optional[Union[float, Ref, GetAtt, Sub]] = None
    column_index: Optional[Union[float, Ref, GetAtt, Sub]] = None
    row_index: Optional[Union[float, Ref, GetAtt, Sub]] = None
    row_span: Optional[Union[float, Ref, GetAtt, Sub]] = None
    element_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GridLayoutScreenCanvasSizeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "optimized_view_port_width": "OptimizedViewPortWidth",
        "resize_option": "ResizeOption",
    }

    optimized_view_port_width: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resize_option: Optional[Union[str, ResizeOption, Ref, GetAtt, Sub]] = None


@dataclass
class GrowthRateComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "time": "Time",
        "period_size": "PeriodSize",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    value: Optional[MeasureField] = None
    time: Optional[DimensionField] = None
    period_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HeaderFooterSectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "layout": "Layout",
        "style": "Style",
        "section_id": "SectionId",
    }

    layout: Optional[SectionLayoutConfiguration] = None
    style: Optional[SectionStyle] = None
    section_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HeatMapAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "columns": "Columns",
        "rows": "Rows",
    }

    values: Optional[list[MeasureField]] = None
    columns: Optional[list[DimensionField]] = None
    rows: Optional[list[DimensionField]] = None


@dataclass
class HeatMapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "column_label_options": "ColumnLabelOptions",
        "legend": "Legend",
        "data_labels": "DataLabels",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "color_scale": "ColorScale",
        "interactions": "Interactions",
        "row_label_options": "RowLabelOptions",
    }

    sort_configuration: Optional[HeatMapSortConfiguration] = None
    column_label_options: Optional[ChartAxisLabelOptions] = None
    legend: Optional[LegendOptions] = None
    data_labels: Optional[DataLabelOptions] = None
    field_wells: Optional[HeatMapFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    color_scale: Optional[ColorScale] = None
    interactions: Optional[VisualInteractionOptions] = None
    row_label_options: Optional[ChartAxisLabelOptions] = None


@dataclass
class HeatMapFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "heat_map_aggregated_field_wells": "HeatMapAggregatedFieldWells",
    }

    heat_map_aggregated_field_wells: Optional[HeatMapAggregatedFieldWells] = None


@dataclass
class HeatMapSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "heat_map_row_sort": "HeatMapRowSort",
        "heat_map_row_items_limit_configuration": "HeatMapRowItemsLimitConfiguration",
        "heat_map_column_items_limit_configuration": "HeatMapColumnItemsLimitConfiguration",
        "heat_map_column_sort": "HeatMapColumnSort",
    }

    heat_map_row_sort: Optional[list[FieldSortOptions]] = None
    heat_map_row_items_limit_configuration: Optional[ItemsLimitConfiguration] = None
    heat_map_column_items_limit_configuration: Optional[ItemsLimitConfiguration] = None
    heat_map_column_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class HeatMapVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[HeatMapConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class HistogramAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[list[MeasureField]] = None


@dataclass
class HistogramBinOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bin_width": "BinWidth",
        "start_value": "StartValue",
        "selected_bin_type": "SelectedBinType",
        "bin_count": "BinCount",
    }

    bin_width: Optional[BinWidthOptions] = None
    start_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    selected_bin_type: Optional[Union[str, HistogramBinType, Ref, GetAtt, Sub]] = None
    bin_count: Optional[BinCountOptions] = None


@dataclass
class HistogramConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "y_axis_display_options": "YAxisDisplayOptions",
        "data_labels": "DataLabels",
        "bin_options": "BinOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "x_axis_label_options": "XAxisLabelOptions",
        "interactions": "Interactions",
        "visual_palette": "VisualPalette",
        "x_axis_display_options": "XAxisDisplayOptions",
    }

    y_axis_display_options: Optional[AxisDisplayOptions] = None
    data_labels: Optional[DataLabelOptions] = None
    bin_options: Optional[HistogramBinOptions] = None
    field_wells: Optional[HistogramFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    x_axis_label_options: Optional[ChartAxisLabelOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    visual_palette: Optional[VisualPalette] = None
    x_axis_display_options: Optional[AxisDisplayOptions] = None


@dataclass
class HistogramFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "histogram_aggregated_field_wells": "HistogramAggregatedFieldWells",
    }

    histogram_aggregated_field_wells: Optional[HistogramAggregatedFieldWells] = None


@dataclass
class HistogramVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[HistogramConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageCustomAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "trigger": "Trigger",
        "custom_action_id": "CustomActionId",
        "name": "Name",
        "action_operations": "ActionOperations",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    trigger: Optional[Union[str, ImageCustomActionTrigger, Ref, GetAtt, Sub]] = None
    custom_action_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_operations: Optional[list[ImageCustomActionOperation]] = None


@dataclass
class ImageCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "navigation_operation": "NavigationOperation",
        "set_parameters_operation": "SetParametersOperation",
        "url_operation": "URLOperation",
    }

    navigation_operation: Optional[CustomActionNavigationOperation] = None
    set_parameters_operation: Optional[CustomActionSetParametersOperation] = None
    url_operation: Optional[CustomActionURLOperation] = None


@dataclass
class ImageInteractionOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "image_menu_option": "ImageMenuOption",
    }

    image_menu_option: Optional[ImageMenuOption] = None


@dataclass
class ImageMenuOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class ImageStaticFile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_file_id": "StaticFileId",
        "source": "Source",
    }

    static_file_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[StaticFileSource] = None


@dataclass
class InnerFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_inner_filter": "CategoryInnerFilter",
    }

    category_inner_filter: Optional[CategoryInnerFilter] = None


@dataclass
class InsightConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "computations": "Computations",
        "custom_narrative": "CustomNarrative",
        "interactions": "Interactions",
    }

    computations: Optional[list[Computation]] = None
    custom_narrative: Optional[CustomNarrativeOptions] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class InsightVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "actions": "Actions",
        "data_set_identifier": "DataSetIdentifier",
        "insight_configuration": "InsightConfiguration",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    actions: Optional[list[VisualCustomAction]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    insight_configuration: Optional[InsightConfiguration] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic_value": "DynamicValue",
        "static_values": "StaticValues",
    }

    dynamic_value: Optional[DynamicDefaultValue] = None
    static_values: Optional[Union[list[float], Ref]] = None


@dataclass
class IntegerParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[float], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerParameterDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mapped_data_set_parameters": "MappedDataSetParameters",
        "default_values": "DefaultValues",
        "parameter_value_type": "ParameterValueType",
        "value_when_unset": "ValueWhenUnset",
        "name": "Name",
    }

    mapped_data_set_parameters: Optional[list[MappedDataSetParameter]] = None
    default_values: Optional[IntegerDefaultValues] = None
    parameter_value_type: Optional[Union[str, ParameterValueType, Ref, GetAtt, Sub]] = None
    value_when_unset: Optional[IntegerValueWhenUnsetConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerValueWhenUnsetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_when_unset_option": "ValueWhenUnsetOption",
        "custom_value": "CustomValue",
    }

    value_when_unset_option: Optional[Union[str, ValueWhenUnsetOption, Ref, GetAtt, Sub]] = None
    custom_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ItemsLimitConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items_limit": "ItemsLimit",
        "other_categories": "OtherCategories",
    }

    items_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None
    other_categories: Optional[Union[str, OtherCategories, Ref, GetAtt, Sub]] = None


@dataclass
class KPIActualValueConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_color": "TextColor",
        "icon": "Icon",
    }

    text_color: Optional[ConditionalFormattingColor] = None
    icon: Optional[ConditionalFormattingIcon] = None


@dataclass
class KPIComparisonValueConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_color": "TextColor",
        "icon": "Icon",
    }

    text_color: Optional[ConditionalFormattingColor] = None
    icon: Optional[ConditionalFormattingIcon] = None


@dataclass
class KPIConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditional_formatting_options": "ConditionalFormattingOptions",
    }

    conditional_formatting_options: Optional[list[KPIConditionalFormattingOption]] = None


@dataclass
class KPIConditionalFormattingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_value": "PrimaryValue",
        "actual_value": "ActualValue",
        "comparison_value": "ComparisonValue",
        "progress_bar": "ProgressBar",
    }

    primary_value: Optional[KPIPrimaryValueConditionalFormatting] = None
    actual_value: Optional[KPIActualValueConditionalFormatting] = None
    comparison_value: Optional[KPIComparisonValueConditionalFormatting] = None
    progress_bar: Optional[KPIProgressBarConditionalFormatting] = None


@dataclass
class KPIConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "kpi_options": "KPIOptions",
        "field_wells": "FieldWells",
        "interactions": "Interactions",
    }

    sort_configuration: Optional[KPISortConfiguration] = None
    kpi_options: Optional[KPIOptions] = None
    field_wells: Optional[KPIFieldWells] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class KPIFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_values": "TargetValues",
        "trend_groups": "TrendGroups",
        "values": "Values",
    }

    target_values: Optional[list[MeasureField]] = None
    trend_groups: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class KPIOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secondary_value_font_configuration": "SecondaryValueFontConfiguration",
        "visual_layout_options": "VisualLayoutOptions",
        "trend_arrows": "TrendArrows",
        "secondary_value": "SecondaryValue",
        "comparison": "Comparison",
        "primary_value_display_type": "PrimaryValueDisplayType",
        "progress_bar": "ProgressBar",
        "primary_value_font_configuration": "PrimaryValueFontConfiguration",
        "sparkline": "Sparkline",
    }

    secondary_value_font_configuration: Optional[FontConfiguration] = None
    visual_layout_options: Optional[KPIVisualLayoutOptions] = None
    trend_arrows: Optional[TrendArrowOptions] = None
    secondary_value: Optional[SecondaryValueOptions] = None
    comparison: Optional[ComparisonConfiguration] = None
    primary_value_display_type: Optional[Union[str, PrimaryValueDisplayType, Ref, GetAtt, Sub]] = None
    progress_bar: Optional[ProgressBarOptions] = None
    primary_value_font_configuration: Optional[FontConfiguration] = None
    sparkline: Optional[KPISparklineOptions] = None


@dataclass
class KPIPrimaryValueConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_color": "TextColor",
        "icon": "Icon",
    }

    text_color: Optional[ConditionalFormattingColor] = None
    icon: Optional[ConditionalFormattingIcon] = None


@dataclass
class KPIProgressBarConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "foreground_color": "ForegroundColor",
    }

    foreground_color: Optional[ConditionalFormattingColor] = None


@dataclass
class KPISortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "trend_group_sort": "TrendGroupSort",
    }

    trend_group_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class KPISparklineOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "color": "Color",
        "tooltip_visibility": "TooltipVisibility",
        "visibility": "Visibility",
    }

    type_: Optional[Union[str, KPISparklineType, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tooltip_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class KPIVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "conditional_formatting": "ConditionalFormatting",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    conditional_formatting: Optional[KPIConditionalFormatting] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[KPIConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class KPIVisualLayoutOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "standard_layout": "StandardLayout",
    }

    standard_layout: Optional[KPIVisualStandardLayout] = None


@dataclass
class KPIVisualStandardLayout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, KPIVisualStandardLayoutType, Ref, GetAtt, Sub]] = None


@dataclass
class LabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
        "visibility": "Visibility",
        "font_configuration": "FontConfiguration",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    font_configuration: Optional[FontConfiguration] = None


@dataclass
class LayerCustomAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "trigger": "Trigger",
        "custom_action_id": "CustomActionId",
        "name": "Name",
        "action_operations": "ActionOperations",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    trigger: Optional[Union[str, LayerCustomActionTrigger, Ref, GetAtt, Sub]] = None
    custom_action_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_operations: Optional[list[LayerCustomActionOperation]] = None


@dataclass
class LayerCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "navigation_operation": "NavigationOperation",
        "set_parameters_operation": "SetParametersOperation",
        "filter_operation": "FilterOperation",
        "url_operation": "URLOperation",
    }

    navigation_operation: Optional[CustomActionNavigationOperation] = None
    set_parameters_operation: Optional[CustomActionSetParametersOperation] = None
    filter_operation: Optional[CustomActionFilterOperation] = None
    url_operation: Optional[CustomActionURLOperation] = None


@dataclass
class LayerMapVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "data_set_identifier": "DataSetIdentifier",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[GeospatialLayerMapConfiguration] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Layout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration": "Configuration",
    }

    configuration: Optional[LayoutConfiguration] = None


@dataclass
class LayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grid_layout": "GridLayout",
        "free_form_layout": "FreeFormLayout",
        "section_based_layout": "SectionBasedLayout",
    }

    grid_layout: Optional[GridLayoutConfiguration] = None
    free_form_layout: Optional[FreeFormLayoutConfiguration] = None
    section_based_layout: Optional[SectionBasedLayoutConfiguration] = None


@dataclass
class LegendOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "position": "Position",
        "value_font_configuration": "ValueFontConfiguration",
        "title": "Title",
        "visibility": "Visibility",
        "height": "Height",
        "width": "Width",
    }

    position: Optional[Union[str, LegendPosition, Ref, GetAtt, Sub]] = None
    value_font_configuration: Optional[FontConfiguration] = None
    title: Optional[LabelOptions] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    height: Optional[Union[str, Ref, GetAtt, Sub]] = None
    width: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LineChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "colors": "Colors",
        "values": "Values",
        "small_multiples": "SmallMultiples",
    }

    category: Optional[list[DimensionField]] = None
    colors: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None
    small_multiples: Optional[list[DimensionField]] = None


@dataclass
class LineChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "reference_lines": "ReferenceLines",
        "data_labels": "DataLabels",
        "tooltip": "Tooltip",
        "single_axis_options": "SingleAxisOptions",
        "small_multiples_options": "SmallMultiplesOptions",
        "primary_y_axis_display_options": "PrimaryYAxisDisplayOptions",
        "visual_palette": "VisualPalette",
        "x_axis_display_options": "XAxisDisplayOptions",
        "default_series_settings": "DefaultSeriesSettings",
        "secondary_y_axis_label_options": "SecondaryYAxisLabelOptions",
        "forecast_configurations": "ForecastConfigurations",
        "series": "Series",
        "type_": "Type",
        "primary_y_axis_label_options": "PrimaryYAxisLabelOptions",
        "contribution_analysis_defaults": "ContributionAnalysisDefaults",
        "field_wells": "FieldWells",
        "secondary_y_axis_display_options": "SecondaryYAxisDisplayOptions",
        "x_axis_label_options": "XAxisLabelOptions",
        "interactions": "Interactions",
    }

    sort_configuration: Optional[LineChartSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    reference_lines: Optional[list[ReferenceLine]] = None
    data_labels: Optional[DataLabelOptions] = None
    tooltip: Optional[TooltipOptions] = None
    single_axis_options: Optional[SingleAxisOptions] = None
    small_multiples_options: Optional[SmallMultiplesOptions] = None
    primary_y_axis_display_options: Optional[LineSeriesAxisDisplayOptions] = None
    visual_palette: Optional[VisualPalette] = None
    x_axis_display_options: Optional[AxisDisplayOptions] = None
    default_series_settings: Optional[LineChartDefaultSeriesSettings] = None
    secondary_y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    forecast_configurations: Optional[list[ForecastConfiguration]] = None
    series: Optional[list[SeriesItem]] = None
    type_: Optional[Union[str, LineChartType, Ref, GetAtt, Sub]] = None
    primary_y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    contribution_analysis_defaults: Optional[list[ContributionAnalysisDefault]] = None
    field_wells: Optional[LineChartFieldWells] = None
    secondary_y_axis_display_options: Optional[LineSeriesAxisDisplayOptions] = None
    x_axis_label_options: Optional[ChartAxisLabelOptions] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class LineChartDefaultSeriesSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_style_settings": "LineStyleSettings",
        "axis_binding": "AxisBinding",
        "marker_style_settings": "MarkerStyleSettings",
    }

    line_style_settings: Optional[LineChartLineStyleSettings] = None
    axis_binding: Optional[Union[str, AxisBinding, Ref, GetAtt, Sub]] = None
    marker_style_settings: Optional[LineChartMarkerStyleSettings] = None


@dataclass
class LineChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_chart_aggregated_field_wells": "LineChartAggregatedFieldWells",
    }

    line_chart_aggregated_field_wells: Optional[LineChartAggregatedFieldWells] = None


@dataclass
class LineChartLineStyleSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_interpolation": "LineInterpolation",
        "line_style": "LineStyle",
        "line_visibility": "LineVisibility",
        "line_width": "LineWidth",
    }

    line_interpolation: Optional[Union[str, LineInterpolation, Ref, GetAtt, Sub]] = None
    line_style: Optional[Union[str, LineChartLineStyle, Ref, GetAtt, Sub]] = None
    line_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    line_width: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LineChartMarkerStyleSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "marker_shape": "MarkerShape",
        "marker_size": "MarkerSize",
        "marker_visibility": "MarkerVisibility",
        "marker_color": "MarkerColor",
    }

    marker_shape: Optional[Union[str, LineChartMarkerShape, Ref, GetAtt, Sub]] = None
    marker_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    marker_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    marker_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LineChartSeriesSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "line_style_settings": "LineStyleSettings",
        "marker_style_settings": "MarkerStyleSettings",
    }

    line_style_settings: Optional[LineChartLineStyleSettings] = None
    marker_style_settings: Optional[LineChartMarkerStyleSettings] = None


@dataclass
class LineChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_items_limit_configuration": "CategoryItemsLimitConfiguration",
        "color_items_limit_configuration": "ColorItemsLimitConfiguration",
        "small_multiples_sort": "SmallMultiplesSort",
        "category_sort": "CategorySort",
        "small_multiples_limit_configuration": "SmallMultiplesLimitConfiguration",
    }

    category_items_limit_configuration: Optional[ItemsLimitConfiguration] = None
    color_items_limit_configuration: Optional[ItemsLimitConfiguration] = None
    small_multiples_sort: Optional[list[FieldSortOptions]] = None
    category_sort: Optional[list[FieldSortOptions]] = None
    small_multiples_limit_configuration: Optional[ItemsLimitConfiguration] = None


@dataclass
class LineChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[LineChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class LineSeriesAxisDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "missing_data_configurations": "MissingDataConfigurations",
        "axis_options": "AxisOptions",
    }

    missing_data_configurations: Optional[list[MissingDataConfiguration]] = None
    axis_options: Optional[AxisDisplayOptions] = None


@dataclass
class LinkSharingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "permissions": "Permissions",
    }

    permissions: Optional[list[ResourcePermission]] = None


@dataclass
class ListControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "search_options": "SearchOptions",
        "select_all_options": "SelectAllOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
    }

    title_options: Optional[LabelOptions] = None
    search_options: Optional[ListControlSearchOptions] = None
    select_all_options: Optional[ListControlSelectAllOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None


@dataclass
class ListControlSearchOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class ListControlSelectAllOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class LoadingAnimation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class LocalNavigationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_sheet_id": "TargetSheetId",
    }

    target_sheet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LongFormatText(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rich_text": "RichText",
        "plain_text": "PlainText",
    }

    rich_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    plain_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MappedDataSetParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_set_parameter_name": "DataSetParameterName",
        "data_set_identifier": "DataSetIdentifier",
    }

    data_set_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaximumLabelType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class MaximumMinimumComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "time": "Time",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    type_: Optional[Union[str, MaximumMinimumComputationType, Ref, GetAtt, Sub]] = None
    value: Optional[MeasureField] = None
    time: Optional[DimensionField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MeasureField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "date_measure_field": "DateMeasureField",
        "numerical_measure_field": "NumericalMeasureField",
        "categorical_measure_field": "CategoricalMeasureField",
        "calculated_measure_field": "CalculatedMeasureField",
    }

    date_measure_field: Optional[DateMeasureField] = None
    numerical_measure_field: Optional[NumericalMeasureField] = None
    categorical_measure_field: Optional[CategoricalMeasureField] = None
    calculated_measure_field: Optional[CalculatedMeasureField] = None


@dataclass
class MetricComparisonComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
        "time": "Time",
        "computation_id": "ComputationId",
        "from_value": "FromValue",
        "name": "Name",
    }

    target_value: Optional[MeasureField] = None
    time: Optional[DimensionField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    from_value: Optional[MeasureField] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MinimumLabelType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class MissingDataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "treatment_option": "TreatmentOption",
    }

    treatment_option: Optional[Union[str, MissingDataTreatmentOption, Ref, GetAtt, Sub]] = None


@dataclass
class NegativeValueConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_mode": "DisplayMode",
    }

    display_mode: Optional[Union[str, NegativeValueDisplayMode, Ref, GetAtt, Sub]] = None


@dataclass
class NestedFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "inner_filter": "InnerFilter",
        "include_inner_set": "IncludeInnerSet",
        "filter_id": "FilterId",
    }

    column: Optional[ColumnIdentifier] = None
    inner_filter: Optional[InnerFilter] = None
    include_inner_set: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NullValueFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "null_string": "NullString",
    }

    null_string: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumberDisplayFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "negative_value_configuration": "NegativeValueConfiguration",
        "decimal_places_configuration": "DecimalPlacesConfiguration",
        "number_scale": "NumberScale",
        "null_value_format_configuration": "NullValueFormatConfiguration",
        "suffix": "Suffix",
        "separator_configuration": "SeparatorConfiguration",
        "prefix": "Prefix",
    }

    negative_value_configuration: Optional[NegativeValueConfiguration] = None
    decimal_places_configuration: Optional[DecimalPlacesConfiguration] = None
    number_scale: Optional[Union[str, NumberScale, Ref, GetAtt, Sub]] = None
    null_value_format_configuration: Optional[NullValueFormatConfiguration] = None
    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    separator_configuration: Optional[NumericSeparatorConfiguration] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumberFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "format_configuration": "FormatConfiguration",
    }

    format_configuration: Optional[NumericFormatConfiguration] = None


@dataclass
class NumericAxisOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scale": "Scale",
        "range": "Range",
    }

    scale: Optional[AxisScale] = None
    range: Optional[AxisDisplayRange] = None


@dataclass
class NumericEqualityDrillDownFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "value": "Value",
    }

    column: Optional[ColumnIdentifier] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class NumericEqualityFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "column": "Column",
        "value": "Value",
        "parameter_name": "ParameterName",
        "null_option": "NullOption",
        "match_operator": "MatchOperator",
        "select_all_options": "SelectAllOptions",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
    }

    aggregation_function: Optional[AggregationFunction] = None
    column: Optional[ColumnIdentifier] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    match_operator: Optional[Union[str, NumericEqualityMatchOperator, Ref, GetAtt, Sub]] = None
    select_all_options: Optional[Union[str, NumericFilterSelectAllOptions, Ref, GetAtt, Sub]] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumericFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_display_format_configuration": "NumberDisplayFormatConfiguration",
        "currency_display_format_configuration": "CurrencyDisplayFormatConfiguration",
        "percentage_display_format_configuration": "PercentageDisplayFormatConfiguration",
    }

    number_display_format_configuration: Optional[NumberDisplayFormatConfiguration] = None
    currency_display_format_configuration: Optional[CurrencyDisplayFormatConfiguration] = None
    percentage_display_format_configuration: Optional[PercentageDisplayFormatConfiguration] = None


@dataclass
class NumericRangeFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "column": "Column",
        "include_maximum": "IncludeMaximum",
        "range_minimum": "RangeMinimum",
        "null_option": "NullOption",
        "select_all_options": "SelectAllOptions",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
        "range_maximum": "RangeMaximum",
        "include_minimum": "IncludeMinimum",
    }

    aggregation_function: Optional[AggregationFunction] = None
    column: Optional[ColumnIdentifier] = None
    include_maximum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    range_minimum: Optional[NumericRangeFilterValue] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    select_all_options: Optional[Union[str, NumericFilterSelectAllOptions, Ref, GetAtt, Sub]] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_maximum: Optional[NumericRangeFilterValue] = None
    include_minimum: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class NumericRangeFilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
        "parameter": "Parameter",
    }

    static_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    parameter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumericSeparatorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "decimal_separator": "DecimalSeparator",
        "thousands_separator": "ThousandsSeparator",
    }

    decimal_separator: Optional[Union[str, NumericSeparatorSymbol, Ref, GetAtt, Sub]] = None
    thousands_separator: Optional[ThousandSeparatorOptions] = None


@dataclass
class NumericalAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "percentile_aggregation": "PercentileAggregation",
        "simple_numerical_aggregation": "SimpleNumericalAggregation",
    }

    percentile_aggregation: Optional[PercentileAggregation] = None
    simple_numerical_aggregation: Optional[Union[str, SimpleNumericalAggregationFunction, Ref, GetAtt, Sub]] = None


@dataclass
class NumericalDimensionField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_id": "HierarchyId",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
    }

    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format_configuration: Optional[NumberFormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumericalMeasureField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
    }

    aggregation_function: Optional[NumericalAggregationFunction] = None
    format_configuration: Optional[NumberFormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PaginationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "page_size": "PageSize",
        "page_number": "PageNumber",
    }

    page_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    page_number: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PanelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "border_thickness": "BorderThickness",
        "border_style": "BorderStyle",
        "gutter_spacing": "GutterSpacing",
        "background_visibility": "BackgroundVisibility",
        "border_visibility": "BorderVisibility",
        "border_color": "BorderColor",
        "title": "Title",
        "gutter_visibility": "GutterVisibility",
        "background_color": "BackgroundColor",
    }

    border_thickness: Optional[Union[str, Ref, GetAtt, Sub]] = None
    border_style: Optional[Union[str, PanelBorderStyle, Ref, GetAtt, Sub]] = None
    gutter_spacing: Optional[Union[str, Ref, GetAtt, Sub]] = None
    background_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    border_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    border_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[PanelTitleOptions] = None
    gutter_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PanelTitleOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
        "font_configuration": "FontConfiguration",
        "horizontal_text_alignment": "HorizontalTextAlignment",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    font_configuration: Optional[FontConfiguration] = None
    horizontal_text_alignment: Optional[Union[str, HorizontalTextAlignment, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slider": "Slider",
        "text_area": "TextArea",
        "dropdown": "Dropdown",
        "text_field": "TextField",
        "list": "List",
        "date_time_picker": "DateTimePicker",
    }

    slider: Optional[ParameterSliderControl] = None
    text_area: Optional[ParameterTextAreaControl] = None
    dropdown: Optional[ParameterDropDownControl] = None
    text_field: Optional[ParameterTextFieldControl] = None
    list: Optional[ParameterListControl] = None
    date_time_picker: Optional[ParameterDateTimePickerControl] = None


@dataclass
class ParameterDateTimePickerControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_control_id": "ParameterControlId",
        "display_options": "DisplayOptions",
        "source_parameter_name": "SourceParameterName",
        "title": "Title",
    }

    parameter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[DateTimePickerControlDisplayOptions] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "string_parameter_declaration": "StringParameterDeclaration",
        "date_time_parameter_declaration": "DateTimeParameterDeclaration",
        "decimal_parameter_declaration": "DecimalParameterDeclaration",
        "integer_parameter_declaration": "IntegerParameterDeclaration",
    }

    string_parameter_declaration: Optional[StringParameterDeclaration] = None
    date_time_parameter_declaration: Optional[DateTimeParameterDeclaration] = None
    decimal_parameter_declaration: Optional[DecimalParameterDeclaration] = None
    integer_parameter_declaration: Optional[IntegerParameterDeclaration] = None


@dataclass
class ParameterDropDownControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_control_id": "ParameterControlId",
        "type_": "Type",
        "display_options": "DisplayOptions",
        "source_parameter_name": "SourceParameterName",
        "cascading_control_configuration": "CascadingControlConfiguration",
        "title": "Title",
        "commit_mode": "CommitMode",
        "selectable_values": "SelectableValues",
    }

    parameter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SheetControlListType, Ref, GetAtt, Sub]] = None
    display_options: Optional[DropDownControlDisplayOptions] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cascading_control_configuration: Optional[CascadingControlConfiguration] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    commit_mode: Optional[Union[str, CommitMode, Ref, GetAtt, Sub]] = None
    selectable_values: Optional[ParameterSelectableValues] = None


@dataclass
class ParameterListControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_control_id": "ParameterControlId",
        "type_": "Type",
        "display_options": "DisplayOptions",
        "source_parameter_name": "SourceParameterName",
        "cascading_control_configuration": "CascadingControlConfiguration",
        "title": "Title",
        "selectable_values": "SelectableValues",
    }

    parameter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, SheetControlListType, Ref, GetAtt, Sub]] = None
    display_options: Optional[ListControlDisplayOptions] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cascading_control_configuration: Optional[CascadingControlConfiguration] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    selectable_values: Optional[ParameterSelectableValues] = None


@dataclass
class ParameterSelectableValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "link_to_data_set_column": "LinkToDataSetColumn",
        "values": "Values",
    }

    link_to_data_set_column: Optional[ColumnIdentifier] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class ParameterSliderControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_control_id": "ParameterControlId",
        "step_size": "StepSize",
        "display_options": "DisplayOptions",
        "source_parameter_name": "SourceParameterName",
        "title": "Title",
        "maximum_value": "MaximumValue",
        "minimum_value": "MinimumValue",
    }

    parameter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    step_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    display_options: Optional[SliderControlDisplayOptions] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    minimum_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterTextAreaControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_control_id": "ParameterControlId",
        "delimiter": "Delimiter",
        "display_options": "DisplayOptions",
        "source_parameter_name": "SourceParameterName",
        "title": "Title",
    }

    parameter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[TextAreaControlDisplayOptions] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterTextFieldControl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_control_id": "ParameterControlId",
        "display_options": "DisplayOptions",
        "source_parameter_name": "SourceParameterName",
        "title": "Title",
    }

    parameter_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    display_options: Optional[TextFieldControlDisplayOptions] = None
    source_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Parameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "string_parameters": "StringParameters",
        "decimal_parameters": "DecimalParameters",
        "integer_parameters": "IntegerParameters",
        "date_time_parameters": "DateTimeParameters",
    }

    string_parameters: Optional[list[StringParameter]] = None
    decimal_parameters: Optional[list[DecimalParameter]] = None
    integer_parameters: Optional[list[IntegerParameter]] = None
    date_time_parameters: Optional[list[DateTimeParameter]] = None


@dataclass
class PercentVisibleRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
    }

    from_: Optional[Union[float, Ref, GetAtt, Sub]] = None
    to: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PercentageDisplayFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "negative_value_configuration": "NegativeValueConfiguration",
        "decimal_places_configuration": "DecimalPlacesConfiguration",
        "null_value_format_configuration": "NullValueFormatConfiguration",
        "suffix": "Suffix",
        "separator_configuration": "SeparatorConfiguration",
        "prefix": "Prefix",
    }

    negative_value_configuration: Optional[NegativeValueConfiguration] = None
    decimal_places_configuration: Optional[DecimalPlacesConfiguration] = None
    null_value_format_configuration: Optional[NullValueFormatConfiguration] = None
    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    separator_configuration: Optional[NumericSeparatorConfiguration] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PercentileAggregation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "percentile_value": "PercentileValue",
    }

    percentile_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PeriodOverPeriodComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "time": "Time",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    value: Optional[MeasureField] = None
    time: Optional[DimensionField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PeriodToDateComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "period_time_granularity": "PeriodTimeGranularity",
        "value": "Value",
        "time": "Time",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    period_time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    value: Optional[MeasureField] = None
    time: Optional[DimensionField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PieChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "values": "Values",
        "small_multiples": "SmallMultiples",
    }

    category: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None
    small_multiples: Optional[list[DimensionField]] = None


@dataclass
class PieChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "data_labels": "DataLabels",
        "contribution_analysis_defaults": "ContributionAnalysisDefaults",
        "category_label_options": "CategoryLabelOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "donut_options": "DonutOptions",
        "small_multiples_options": "SmallMultiplesOptions",
        "interactions": "Interactions",
        "value_label_options": "ValueLabelOptions",
        "visual_palette": "VisualPalette",
    }

    sort_configuration: Optional[PieChartSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    data_labels: Optional[DataLabelOptions] = None
    contribution_analysis_defaults: Optional[list[ContributionAnalysisDefault]] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[PieChartFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    donut_options: Optional[DonutOptions] = None
    small_multiples_options: Optional[SmallMultiplesOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    value_label_options: Optional[ChartAxisLabelOptions] = None
    visual_palette: Optional[VisualPalette] = None


@dataclass
class PieChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pie_chart_aggregated_field_wells": "PieChartAggregatedFieldWells",
    }

    pie_chart_aggregated_field_wells: Optional[PieChartAggregatedFieldWells] = None


@dataclass
class PieChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "small_multiples_sort": "SmallMultiplesSort",
        "category_items_limit": "CategoryItemsLimit",
        "category_sort": "CategorySort",
        "small_multiples_limit_configuration": "SmallMultiplesLimitConfiguration",
    }

    small_multiples_sort: Optional[list[FieldSortOptions]] = None
    category_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None
    small_multiples_limit_configuration: Optional[ItemsLimitConfiguration] = None


@dataclass
class PieChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[PieChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class PivotFieldSortOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_by": "SortBy",
        "field_id": "FieldId",
    }

    sort_by: Optional[PivotTableSortBy] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "columns": "Columns",
        "rows": "Rows",
    }

    values: Optional[list[MeasureField]] = None
    columns: Optional[list[DimensionField]] = None
    rows: Optional[list[DimensionField]] = None


@dataclass
class PivotTableCellConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "scopes": "Scopes",
        "field_id": "FieldId",
        "text_format": "TextFormat",
    }

    scope: Optional[PivotTableConditionalFormattingScope] = None
    scopes: Optional[list[PivotTableConditionalFormattingScope]] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_format: Optional[TextConditionalFormat] = None


@dataclass
class PivotTableConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditional_formatting_options": "ConditionalFormattingOptions",
    }

    conditional_formatting_options: Optional[list[PivotTableConditionalFormattingOption]] = None


@dataclass
class PivotTableConditionalFormattingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cell": "Cell",
    }

    cell: Optional[PivotTableCellConditionalFormatting] = None


@dataclass
class PivotTableConditionalFormattingScope(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
    }

    role: Optional[Union[str, PivotTableConditionalFormattingScopeRole, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "paginated_report_options": "PaginatedReportOptions",
        "table_options": "TableOptions",
        "field_wells": "FieldWells",
        "field_options": "FieldOptions",
        "interactions": "Interactions",
        "total_options": "TotalOptions",
    }

    sort_configuration: Optional[PivotTableSortConfiguration] = None
    paginated_report_options: Optional[PivotTablePaginatedReportOptions] = None
    table_options: Optional[PivotTableOptions] = None
    field_wells: Optional[PivotTableFieldWells] = None
    field_options: Optional[PivotTableFieldOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    total_options: Optional[PivotTableTotalOptions] = None


@dataclass
class PivotTableDataPathOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_path_list": "DataPathList",
        "width": "Width",
    }

    data_path_list: Optional[list[DataPathValue]] = None
    width: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableFieldCollapseStateOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "state": "State",
    }

    target: Optional[PivotTableFieldCollapseStateTarget] = None
    state: Optional[Union[str, PivotTableFieldCollapseState, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableFieldCollapseStateTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "field_data_path_values": "FieldDataPathValues",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_data_path_values: Optional[list[DataPathValue]] = None


@dataclass
class PivotTableFieldOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
        "field_id": "FieldId",
        "visibility": "Visibility",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableFieldOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "collapse_state_options": "CollapseStateOptions",
        "data_path_options": "DataPathOptions",
        "selected_field_options": "SelectedFieldOptions",
    }

    collapse_state_options: Optional[list[PivotTableFieldCollapseStateOption]] = None
    data_path_options: Optional[list[PivotTableDataPathOption]] = None
    selected_field_options: Optional[list[PivotTableFieldOption]] = None


@dataclass
class PivotTableFieldSubtotalOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pivot_table_aggregated_field_wells": "PivotTableAggregatedFieldWells",
    }

    pivot_table_aggregated_field_wells: Optional[PivotTableAggregatedFieldWells] = None


@dataclass
class PivotTableOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "row_field_names_style": "RowFieldNamesStyle",
        "row_header_style": "RowHeaderStyle",
        "collapsed_row_dimensions_visibility": "CollapsedRowDimensionsVisibility",
        "rows_layout": "RowsLayout",
        "metric_placement": "MetricPlacement",
        "default_cell_width": "DefaultCellWidth",
        "column_names_visibility": "ColumnNamesVisibility",
        "rows_label_options": "RowsLabelOptions",
        "single_metric_visibility": "SingleMetricVisibility",
        "column_header_style": "ColumnHeaderStyle",
        "toggle_buttons_visibility": "ToggleButtonsVisibility",
        "cell_style": "CellStyle",
        "row_alternate_color_options": "RowAlternateColorOptions",
    }

    row_field_names_style: Optional[TableCellStyle] = None
    row_header_style: Optional[TableCellStyle] = None
    collapsed_row_dimensions_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    rows_layout: Optional[Union[str, PivotTableRowsLayout, Ref, GetAtt, Sub]] = None
    metric_placement: Optional[Union[str, PivotTableMetricPlacement, Ref, GetAtt, Sub]] = None
    default_cell_width: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_names_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    rows_label_options: Optional[PivotTableRowsLabelOptions] = None
    single_metric_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    column_header_style: Optional[TableCellStyle] = None
    toggle_buttons_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    cell_style: Optional[TableCellStyle] = None
    row_alternate_color_options: Optional[RowAlternateColorOptions] = None


@dataclass
class PivotTablePaginatedReportOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "overflow_column_header_visibility": "OverflowColumnHeaderVisibility",
        "vertical_overflow_visibility": "VerticalOverflowVisibility",
    }

    overflow_column_header_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    vertical_overflow_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableRowsLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
        "visibility": "Visibility",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTableSortBy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "data_path": "DataPath",
        "column": "Column",
    }

    field: Optional[FieldSort] = None
    data_path: Optional[DataPathSort] = None
    column: Optional[ColumnSort] = None


@dataclass
class PivotTableSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_sort_options": "FieldSortOptions",
    }

    field_sort_options: Optional[list[PivotFieldSortOptions]] = None


@dataclass
class PivotTableTotalOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_subtotal_options": "ColumnSubtotalOptions",
        "row_subtotal_options": "RowSubtotalOptions",
        "row_total_options": "RowTotalOptions",
        "column_total_options": "ColumnTotalOptions",
    }

    column_subtotal_options: Optional[SubtotalOptions] = None
    row_subtotal_options: Optional[SubtotalOptions] = None
    row_total_options: Optional[PivotTotalOptions] = None
    column_total_options: Optional[PivotTotalOptions] = None


@dataclass
class PivotTableVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "conditional_formatting": "ConditionalFormatting",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    conditional_formatting: Optional[PivotTableConditionalFormatting] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[PivotTableConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PivotTotalOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_aggregation_options": "TotalAggregationOptions",
        "custom_label": "CustomLabel",
        "value_cell_style": "ValueCellStyle",
        "scroll_status": "ScrollStatus",
        "placement": "Placement",
        "total_cell_style": "TotalCellStyle",
        "totals_visibility": "TotalsVisibility",
        "metric_header_cell_style": "MetricHeaderCellStyle",
    }

    total_aggregation_options: Optional[list[TotalAggregationOption]] = None
    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_cell_style: Optional[TableCellStyle] = None
    scroll_status: Optional[Union[str, TableTotalsScrollStatus, Ref, GetAtt, Sub]] = None
    placement: Optional[Union[str, TableTotalsPlacement, Ref, GetAtt, Sub]] = None
    total_cell_style: Optional[TableCellStyle] = None
    totals_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    metric_header_cell_style: Optional[TableCellStyle] = None


@dataclass
class PluginVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "plugin_arn": "PluginArn",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    plugin_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[PluginVisualConfiguration] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PluginVisualConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "visual_options": "VisualOptions",
        "field_wells": "FieldWells",
    }

    sort_configuration: Optional[PluginVisualSortConfiguration] = None
    visual_options: Optional[PluginVisualOptions] = None
    field_wells: Optional[list[PluginVisualFieldWell]] = None


@dataclass
class PluginVisualFieldWell(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unaggregated": "Unaggregated",
        "axis_name": "AxisName",
        "measures": "Measures",
        "dimensions": "Dimensions",
    }

    unaggregated: Optional[list[UnaggregatedField]] = None
    axis_name: Optional[Union[str, PluginVisualAxisName, Ref, GetAtt, Sub]] = None
    measures: Optional[list[MeasureField]] = None
    dimensions: Optional[list[DimensionField]] = None


@dataclass
class PluginVisualItemsLimitConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items_limit": "ItemsLimit",
    }

    items_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PluginVisualOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visual_properties": "VisualProperties",
    }

    visual_properties: Optional[list[PluginVisualProperty]] = None


@dataclass
class PluginVisualProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PluginVisualSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "plugin_visual_table_query_sort": "PluginVisualTableQuerySort",
    }

    plugin_visual_table_query_sort: Optional[PluginVisualTableQuerySort] = None


@dataclass
class PluginVisualTableQuerySort(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items_limit_configuration": "ItemsLimitConfiguration",
        "row_sort": "RowSort",
    }

    items_limit_configuration: Optional[PluginVisualItemsLimitConfiguration] = None
    row_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class PredefinedHierarchy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_id": "HierarchyId",
        "drill_down_filters": "DrillDownFilters",
        "columns": "Columns",
    }

    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    drill_down_filters: Optional[list[DrillDownFilter]] = None
    columns: Optional[list[ColumnIdentifier]] = None


@dataclass
class ProgressBarOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class QuickSuiteActionsOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class RadarChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "color": "Color",
        "values": "Values",
    }

    category: Optional[list[DimensionField]] = None
    color: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class RadarChartAreaStyleSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class RadarChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "shape": "Shape",
        "base_series_settings": "BaseSeriesSettings",
        "color_label_options": "ColorLabelOptions",
        "category_label_options": "CategoryLabelOptions",
        "axes_range_scale": "AxesRangeScale",
        "visual_palette": "VisualPalette",
        "alternate_band_colors_visibility": "AlternateBandColorsVisibility",
        "start_angle": "StartAngle",
        "category_axis": "CategoryAxis",
        "field_wells": "FieldWells",
        "color_axis": "ColorAxis",
        "alternate_band_odd_color": "AlternateBandOddColor",
        "interactions": "Interactions",
        "alternate_band_even_color": "AlternateBandEvenColor",
    }

    sort_configuration: Optional[RadarChartSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    shape: Optional[Union[str, RadarChartShape, Ref, GetAtt, Sub]] = None
    base_series_settings: Optional[RadarChartSeriesSettings] = None
    color_label_options: Optional[ChartAxisLabelOptions] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    axes_range_scale: Optional[Union[str, RadarChartAxesRangeScale, Ref, GetAtt, Sub]] = None
    visual_palette: Optional[VisualPalette] = None
    alternate_band_colors_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    start_angle: Optional[Union[float, Ref, GetAtt, Sub]] = None
    category_axis: Optional[AxisDisplayOptions] = None
    field_wells: Optional[RadarChartFieldWells] = None
    color_axis: Optional[AxisDisplayOptions] = None
    alternate_band_odd_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    interactions: Optional[VisualInteractionOptions] = None
    alternate_band_even_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RadarChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "radar_chart_aggregated_field_wells": "RadarChartAggregatedFieldWells",
    }

    radar_chart_aggregated_field_wells: Optional[RadarChartAggregatedFieldWells] = None


@dataclass
class RadarChartSeriesSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "area_style_settings": "AreaStyleSettings",
    }

    area_style_settings: Optional[RadarChartAreaStyleSettings] = None


@dataclass
class RadarChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color_sort": "ColorSort",
        "color_items_limit": "ColorItemsLimit",
        "category_items_limit": "CategoryItemsLimit",
        "category_sort": "CategorySort",
    }

    color_sort: Optional[list[FieldSortOptions]] = None
    color_items_limit: Optional[ItemsLimitConfiguration] = None
    category_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class RadarChartVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[RadarChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class RangeEndsLabelType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class ReferenceLine(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "data_configuration": "DataConfiguration",
        "label_configuration": "LabelConfiguration",
        "style_configuration": "StyleConfiguration",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    data_configuration: Optional[ReferenceLineDataConfiguration] = None
    label_configuration: Optional[ReferenceLineLabelConfiguration] = None
    style_configuration: Optional[ReferenceLineStyleConfiguration] = None


@dataclass
class ReferenceLineCustomLabelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReferenceLineDataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic_configuration": "DynamicConfiguration",
        "axis_binding": "AxisBinding",
        "series_type": "SeriesType",
        "static_configuration": "StaticConfiguration",
    }

    dynamic_configuration: Optional[ReferenceLineDynamicDataConfiguration] = None
    axis_binding: Optional[Union[str, AxisBinding, Ref, GetAtt, Sub]] = None
    series_type: Optional[Union[str, ReferenceLineSeriesType, Ref, GetAtt, Sub]] = None
    static_configuration: Optional[ReferenceLineStaticDataConfiguration] = None


@dataclass
class ReferenceLineDynamicDataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "measure_aggregation_function": "MeasureAggregationFunction",
        "calculation": "Calculation",
    }

    column: Optional[ColumnIdentifier] = None
    measure_aggregation_function: Optional[AggregationFunction] = None
    calculation: Optional[NumericalAggregationFunction] = None


@dataclass
class ReferenceLineLabelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "horizontal_position": "HorizontalPosition",
        "value_label_configuration": "ValueLabelConfiguration",
        "custom_label_configuration": "CustomLabelConfiguration",
        "font_color": "FontColor",
        "font_configuration": "FontConfiguration",
        "vertical_position": "VerticalPosition",
    }

    horizontal_position: Optional[Union[str, ReferenceLineLabelHorizontalPosition, Ref, GetAtt, Sub]] = None
    value_label_configuration: Optional[ReferenceLineValueLabelConfiguration] = None
    custom_label_configuration: Optional[ReferenceLineCustomLabelConfiguration] = None
    font_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    font_configuration: Optional[FontConfiguration] = None
    vertical_position: Optional[Union[str, ReferenceLineLabelVerticalPosition, Ref, GetAtt, Sub]] = None


@dataclass
class ReferenceLineStaticDataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ReferenceLineStyleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
        "color": "Color",
    }

    pattern: Optional[Union[str, ReferenceLinePatternType, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReferenceLineValueLabelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "format_configuration": "FormatConfiguration",
        "relative_position": "RelativePosition",
    }

    format_configuration: Optional[NumericFormatConfiguration] = None
    relative_position: Optional[Union[str, ReferenceLineValueLabelRelativePosition, Ref, GetAtt, Sub]] = None


@dataclass
class RelativeDateTimeControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
        "date_time_format": "DateTimeFormat",
    }

    title_options: Optional[LabelOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None
    date_time_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RelativeDatesFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "relative_date_value": "RelativeDateValue",
        "column": "Column",
        "relative_date_type": "RelativeDateType",
        "time_granularity": "TimeGranularity",
        "parameter_name": "ParameterName",
        "null_option": "NullOption",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
        "anchor_date_configuration": "AnchorDateConfiguration",
        "minimum_granularity": "MinimumGranularity",
        "exclude_period_configuration": "ExcludePeriodConfiguration",
    }

    relative_date_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    column: Optional[ColumnIdentifier] = None
    relative_date_type: Optional[Union[str, RelativeDateType, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    anchor_date_configuration: Optional[AnchorDateConfiguration] = None
    minimum_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    exclude_period_configuration: Optional[ExcludePeriodConfiguration] = None


@dataclass
class ResourcePermission(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "principal": "Principal",
    }

    actions: Optional[Union[list[str], Ref]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RollingDateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "data_set_identifier": "DataSetIdentifier",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RowAlternateColorOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "use_primary_background_color": "UsePrimaryBackgroundColor",
        "row_alternate_colors": "RowAlternateColors",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    use_primary_background_color: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    row_alternate_colors: Optional[Union[list[str], Ref]] = None


@dataclass
class SameSheetTargetVisualConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_visual_options": "TargetVisualOptions",
        "target_visuals": "TargetVisuals",
    }

    target_visual_options: Optional[Union[str, TargetVisualOptions, Ref, GetAtt, Sub]] = None
    target_visuals: Optional[Union[list[str], Ref]] = None


@dataclass
class SankeyDiagramAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
        "weight": "Weight",
    }

    destination: Optional[list[DimensionField]] = None
    source: Optional[list[DimensionField]] = None
    weight: Optional[list[MeasureField]] = None


@dataclass
class SankeyDiagramChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "data_labels": "DataLabels",
        "field_wells": "FieldWells",
        "interactions": "Interactions",
    }

    sort_configuration: Optional[SankeyDiagramSortConfiguration] = None
    data_labels: Optional[DataLabelOptions] = None
    field_wells: Optional[SankeyDiagramFieldWells] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class SankeyDiagramFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sankey_diagram_aggregated_field_wells": "SankeyDiagramAggregatedFieldWells",
    }

    sankey_diagram_aggregated_field_wells: Optional[SankeyDiagramAggregatedFieldWells] = None


@dataclass
class SankeyDiagramSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "weight_sort": "WeightSort",
        "source_items_limit": "SourceItemsLimit",
        "destination_items_limit": "DestinationItemsLimit",
    }

    weight_sort: Optional[list[FieldSortOptions]] = None
    source_items_limit: Optional[ItemsLimitConfiguration] = None
    destination_items_limit: Optional[ItemsLimitConfiguration] = None


@dataclass
class SankeyDiagramVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[SankeyDiagramChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScatterPlotCategoricallyAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "size": "Size",
        "label": "Label",
        "x_axis": "XAxis",
        "y_axis": "YAxis",
    }

    category: Optional[list[DimensionField]] = None
    size: Optional[list[MeasureField]] = None
    label: Optional[list[DimensionField]] = None
    x_axis: Optional[list[MeasureField]] = None
    y_axis: Optional[list[MeasureField]] = None


@dataclass
class ScatterPlotConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "y_axis_label_options": "YAxisLabelOptions",
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "y_axis_display_options": "YAxisDisplayOptions",
        "data_labels": "DataLabels",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "x_axis_label_options": "XAxisLabelOptions",
        "interactions": "Interactions",
        "visual_palette": "VisualPalette",
        "x_axis_display_options": "XAxisDisplayOptions",
    }

    y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    sort_configuration: Optional[ScatterPlotSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    y_axis_display_options: Optional[AxisDisplayOptions] = None
    data_labels: Optional[DataLabelOptions] = None
    field_wells: Optional[ScatterPlotFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    x_axis_label_options: Optional[ChartAxisLabelOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    visual_palette: Optional[VisualPalette] = None
    x_axis_display_options: Optional[AxisDisplayOptions] = None


@dataclass
class ScatterPlotFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scatter_plot_unaggregated_field_wells": "ScatterPlotUnaggregatedFieldWells",
        "scatter_plot_categorically_aggregated_field_wells": "ScatterPlotCategoricallyAggregatedFieldWells",
    }

    scatter_plot_unaggregated_field_wells: Optional[ScatterPlotUnaggregatedFieldWells] = None
    scatter_plot_categorically_aggregated_field_wells: Optional[ScatterPlotCategoricallyAggregatedFieldWells] = None


@dataclass
class ScatterPlotSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scatter_plot_limit_configuration": "ScatterPlotLimitConfiguration",
    }

    scatter_plot_limit_configuration: Optional[ItemsLimitConfiguration] = None


@dataclass
class ScatterPlotUnaggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "size": "Size",
        "label": "Label",
        "x_axis": "XAxis",
        "y_axis": "YAxis",
    }

    category: Optional[list[DimensionField]] = None
    size: Optional[list[MeasureField]] = None
    label: Optional[list[DimensionField]] = None
    x_axis: Optional[list[DimensionField]] = None
    y_axis: Optional[list[DimensionField]] = None


@dataclass
class ScatterPlotVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[ScatterPlotConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class ScrollBarOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visible_range": "VisibleRange",
        "visibility": "Visibility",
    }

    visible_range: Optional[VisibleRangeOptions] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class SecondaryValueOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class SectionAfterPageBreak(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, SectionPageBreakStatus, Ref, GetAtt, Sub]] = None


@dataclass
class SectionBasedLayoutCanvasSizeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "paper_canvas_size_options": "PaperCanvasSizeOptions",
    }

    paper_canvas_size_options: Optional[SectionBasedLayoutPaperCanvasSizeOptions] = None


@dataclass
class SectionBasedLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canvas_size_options": "CanvasSizeOptions",
        "footer_sections": "FooterSections",
        "body_sections": "BodySections",
        "header_sections": "HeaderSections",
    }

    canvas_size_options: Optional[SectionBasedLayoutCanvasSizeOptions] = None
    footer_sections: Optional[list[HeaderFooterSectionConfiguration]] = None
    body_sections: Optional[list[BodySectionConfiguration]] = None
    header_sections: Optional[list[HeaderFooterSectionConfiguration]] = None


@dataclass
class SectionBasedLayoutPaperCanvasSizeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "paper_margin": "PaperMargin",
        "paper_size": "PaperSize",
        "paper_orientation": "PaperOrientation",
    }

    paper_margin: Optional[Spacing] = None
    paper_size: Optional[Union[str, PaperSize, Ref, GetAtt, Sub]] = None
    paper_orientation: Optional[Union[str, PaperOrientation, Ref, GetAtt, Sub]] = None


@dataclass
class SectionLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "free_form_layout": "FreeFormLayout",
    }

    free_form_layout: Optional[FreeFormSectionLayoutConfiguration] = None


@dataclass
class SectionPageBreakConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "after": "After",
    }

    after: Optional[SectionAfterPageBreak] = None


@dataclass
class SectionStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "padding": "Padding",
        "height": "Height",
    }

    padding: Optional[Spacing] = None
    height: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelectedSheetsFilterScopeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sheet_visual_scoping_configurations": "SheetVisualScopingConfigurations",
    }

    sheet_visual_scoping_configurations: Optional[list[SheetVisualScopingConfiguration]] = None


@dataclass
class SeriesItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_series_item": "FieldSeriesItem",
        "data_field_series_item": "DataFieldSeriesItem",
    }

    field_series_item: Optional[FieldSeriesItem] = None
    data_field_series_item: Optional[DataFieldSeriesItem] = None


@dataclass
class SetParameterValueConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_parameter_name": "DestinationParameterName",
        "value": "Value",
    }

    destination_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[DestinationParameterValueConfiguration] = None


@dataclass
class ShapeConditionalFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "background_color": "BackgroundColor",
    }

    background_color: Optional[ConditionalFormattingColor] = None


@dataclass
class Sheet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sheet_id": "SheetId",
        "name": "Name",
    }

    sheet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetControlInfoIconLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
        "info_icon_text": "InfoIconText",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    info_icon_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetControlLayout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration": "Configuration",
    }

    configuration: Optional[SheetControlLayoutConfiguration] = None


@dataclass
class SheetControlLayoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grid_layout": "GridLayout",
    }

    grid_layout: Optional[GridLayoutConfiguration] = None


@dataclass
class SheetControlsOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility_state": "VisibilityState",
    }

    visibility_state: Optional[Union[str, DashboardUIState, Ref, GetAtt, Sub]] = None


@dataclass
class SheetDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "parameter_controls": "ParameterControls",
        "text_boxes": "TextBoxes",
        "content_type": "ContentType",
        "layouts": "Layouts",
        "sheet_id": "SheetId",
        "filter_controls": "FilterControls",
        "images": "Images",
        "sheet_control_layouts": "SheetControlLayouts",
        "title": "Title",
        "visuals": "Visuals",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_controls: Optional[list[ParameterControl]] = None
    text_boxes: Optional[list[SheetTextBox]] = None
    content_type: Optional[Union[str, SheetContentType, Ref, GetAtt, Sub]] = None
    layouts: Optional[list[Layout]] = None
    sheet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter_controls: Optional[list[FilterControl]] = None
    images: Optional[list[SheetImage]] = None
    sheet_control_layouts: Optional[list[SheetControlLayout]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visuals: Optional[list[Visual]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetElementConfigurationOverrides(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class SheetElementRenderingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "configuration_overrides": "ConfigurationOverrides",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_overrides: Optional[SheetElementConfigurationOverrides] = None


@dataclass
class SheetImage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "sheet_image_id": "SheetImageId",
        "tooltip": "Tooltip",
        "scaling": "Scaling",
        "interactions": "Interactions",
        "source": "Source",
        "image_content_alt_text": "ImageContentAltText",
    }

    actions: Optional[list[ImageCustomAction]] = None
    sheet_image_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tooltip: Optional[SheetImageTooltipConfiguration] = None
    scaling: Optional[SheetImageScalingConfiguration] = None
    interactions: Optional[ImageInteractionOptions] = None
    source: Optional[SheetImageSource] = None
    image_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetImageScalingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scaling_type": "ScalingType",
    }

    scaling_type: Optional[Union[str, SheetImageScalingType, Ref, GetAtt, Sub]] = None


@dataclass
class SheetImageSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sheet_image_static_file_source": "SheetImageStaticFileSource",
    }

    sheet_image_static_file_source: Optional[SheetImageStaticFileSource] = None


@dataclass
class SheetImageStaticFileSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_file_id": "StaticFileId",
    }

    static_file_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetImageTooltipConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
        "tooltip_text": "TooltipText",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    tooltip_text: Optional[SheetImageTooltipText] = None


@dataclass
class SheetImageTooltipText(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "plain_text": "PlainText",
    }

    plain_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetLayoutElementMaximizationOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class SheetTextBox(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sheet_text_box_id": "SheetTextBoxId",
        "content": "Content",
    }

    sheet_text_box_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetVisualScopingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "sheet_id": "SheetId",
        "visual_ids": "VisualIds",
    }

    scope: Optional[Union[str, FilterVisualScope, Ref, GetAtt, Sub]] = None
    sheet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visual_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ShortFormatText(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rich_text": "RichText",
        "plain_text": "PlainText",
    }

    rich_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    plain_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SimpleClusterMarker(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "color": "Color",
    }

    color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleAxisOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "y_axis_options": "YAxisOptions",
    }

    y_axis_options: Optional[YAxisOptions] = None


@dataclass
class SliderControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
    }

    title_options: Optional[LabelOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None


@dataclass
class SmallMultiplesAxisProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "placement": "Placement",
        "scale": "Scale",
    }

    placement: Optional[Union[str, SmallMultiplesAxisPlacement, Ref, GetAtt, Sub]] = None
    scale: Optional[Union[str, SmallMultiplesAxisScale, Ref, GetAtt, Sub]] = None


@dataclass
class SmallMultiplesOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_visible_rows": "MaxVisibleRows",
        "panel_configuration": "PanelConfiguration",
        "max_visible_columns": "MaxVisibleColumns",
        "x_axis": "XAxis",
        "y_axis": "YAxis",
    }

    max_visible_rows: Optional[Union[float, Ref, GetAtt, Sub]] = None
    panel_configuration: Optional[PanelConfiguration] = None
    max_visible_columns: Optional[Union[float, Ref, GetAtt, Sub]] = None
    x_axis: Optional[SmallMultiplesAxisProperties] = None
    y_axis: Optional[SmallMultiplesAxisProperties] = None


@dataclass
class Spacing(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "left": "Left",
        "top": "Top",
        "right": "Right",
        "bottom": "Bottom",
    }

    left: Optional[Union[str, Ref, GetAtt, Sub]] = None
    top: Optional[Union[str, Ref, GetAtt, Sub]] = None
    right: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bottom: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpatialStaticFile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "static_file_id": "StaticFileId",
        "source": "Source",
    }

    static_file_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[StaticFileSource] = None


@dataclass
class StaticFile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "image_static_file": "ImageStaticFile",
        "spatial_static_file": "SpatialStaticFile",
    }

    image_static_file: Optional[ImageStaticFile] = None
    spatial_static_file: Optional[SpatialStaticFile] = None


@dataclass
class StaticFileS3SourceOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "object_key": "ObjectKey",
        "region": "Region",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StaticFileSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_options": "UrlOptions",
        "s3_options": "S3Options",
    }

    url_options: Optional[StaticFileUrlSourceOptions] = None
    s3_options: Optional[StaticFileS3SourceOptions] = None


@dataclass
class StaticFileUrlSourceOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url": "Url",
    }

    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StringDefaultValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic_value": "DynamicValue",
        "static_values": "StaticValues",
    }

    dynamic_value: Optional[DynamicDefaultValue] = None
    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class StringFormatConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "numeric_format_configuration": "NumericFormatConfiguration",
        "null_value_format_configuration": "NullValueFormatConfiguration",
    }

    numeric_format_configuration: Optional[NumericFormatConfiguration] = None
    null_value_format_configuration: Optional[NullValueFormatConfiguration] = None


@dataclass
class StringParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StringParameterDeclaration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mapped_data_set_parameters": "MappedDataSetParameters",
        "default_values": "DefaultValues",
        "parameter_value_type": "ParameterValueType",
        "value_when_unset": "ValueWhenUnset",
        "name": "Name",
    }

    mapped_data_set_parameters: Optional[list[MappedDataSetParameter]] = None
    default_values: Optional[StringDefaultValues] = None
    parameter_value_type: Optional[Union[str, ParameterValueType, Ref, GetAtt, Sub]] = None
    value_when_unset: Optional[StringValueWhenUnsetConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StringValueWhenUnsetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_when_unset_option": "ValueWhenUnsetOption",
        "custom_value": "CustomValue",
    }

    value_when_unset_option: Optional[Union[str, ValueWhenUnsetOption, Ref, GetAtt, Sub]] = None
    custom_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubtotalOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
        "field_level_options": "FieldLevelOptions",
        "value_cell_style": "ValueCellStyle",
        "total_cell_style": "TotalCellStyle",
        "totals_visibility": "TotalsVisibility",
        "field_level": "FieldLevel",
        "metric_header_cell_style": "MetricHeaderCellStyle",
        "style_targets": "StyleTargets",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_level_options: Optional[list[PivotTableFieldSubtotalOptions]] = None
    value_cell_style: Optional[TableCellStyle] = None
    total_cell_style: Optional[TableCellStyle] = None
    totals_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    field_level: Optional[Union[str, PivotTableSubtotalLevel, Ref, GetAtt, Sub]] = None
    metric_header_cell_style: Optional[TableCellStyle] = None
    style_targets: Optional[list[TableStyleTarget]] = None


@dataclass
class TableAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_by": "GroupBy",
        "values": "Values",
    }

    group_by: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class TableBorderOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "thickness": "Thickness",
        "color": "Color",
        "style": "Style",
    }

    thickness: Optional[Union[float, Ref, GetAtt, Sub]] = None
    color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    style: Optional[Union[str, TableBorderStyle, Ref, GetAtt, Sub]] = None


@dataclass
class TableCellConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_id": "FieldId",
        "text_format": "TextFormat",
    }

    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_format: Optional[TextConditionalFormat] = None


@dataclass
class TableCellImageSizingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_cell_image_scaling_configuration": "TableCellImageScalingConfiguration",
    }

    table_cell_image_scaling_configuration: Optional[Union[str, TableCellImageScalingConfiguration, Ref, GetAtt, Sub]] = None


@dataclass
class TableCellStyle(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vertical_text_alignment": "VerticalTextAlignment",
        "visibility": "Visibility",
        "height": "Height",
        "font_configuration": "FontConfiguration",
        "border": "Border",
        "text_wrap": "TextWrap",
        "horizontal_text_alignment": "HorizontalTextAlignment",
        "background_color": "BackgroundColor",
    }

    vertical_text_alignment: Optional[Union[str, VerticalTextAlignment, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    height: Optional[Union[float, Ref, GetAtt, Sub]] = None
    font_configuration: Optional[FontConfiguration] = None
    border: Optional[GlobalTableBorderOptions] = None
    text_wrap: Optional[Union[str, TextWrap, Ref, GetAtt, Sub]] = None
    horizontal_text_alignment: Optional[Union[str, HorizontalTextAlignment, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conditional_formatting_options": "ConditionalFormattingOptions",
    }

    conditional_formatting_options: Optional[list[TableConditionalFormattingOption]] = None


@dataclass
class TableConditionalFormattingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "row": "Row",
        "cell": "Cell",
    }

    row: Optional[TableRowConditionalFormatting] = None
    cell: Optional[TableCellConditionalFormatting] = None


@dataclass
class TableConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "paginated_report_options": "PaginatedReportOptions",
        "table_options": "TableOptions",
        "table_inline_visualizations": "TableInlineVisualizations",
        "field_wells": "FieldWells",
        "field_options": "FieldOptions",
        "interactions": "Interactions",
        "total_options": "TotalOptions",
    }

    sort_configuration: Optional[TableSortConfiguration] = None
    paginated_report_options: Optional[TablePaginatedReportOptions] = None
    table_options: Optional[TableOptions] = None
    table_inline_visualizations: Optional[list[TableInlineVisualization]] = None
    field_wells: Optional[TableFieldWells] = None
    field_options: Optional[TableFieldOptions] = None
    interactions: Optional[VisualInteractionOptions] = None
    total_options: Optional[TotalOptions] = None


@dataclass
class TableFieldCustomIconContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "icon": "Icon",
    }

    icon: Optional[Union[str, TableFieldIconSetType, Ref, GetAtt, Sub]] = None


@dataclass
class TableFieldCustomTextContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "font_configuration": "FontConfiguration",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    font_configuration: Optional[FontConfiguration] = None


@dataclass
class TableFieldImageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sizing_options": "SizingOptions",
    }

    sizing_options: Optional[TableCellImageSizingConfiguration] = None


@dataclass
class TableFieldLinkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "content": "Content",
    }

    target: Optional[Union[str, URLTargetConfiguration, Ref, GetAtt, Sub]] = None
    content: Optional[TableFieldLinkContentConfiguration] = None


@dataclass
class TableFieldLinkContentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_icon_content": "CustomIconContent",
        "custom_text_content": "CustomTextContent",
    }

    custom_icon_content: Optional[TableFieldCustomIconContent] = None
    custom_text_content: Optional[TableFieldCustomTextContent] = None


@dataclass
class TableFieldOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_label": "CustomLabel",
        "url_styling": "URLStyling",
        "field_id": "FieldId",
        "visibility": "Visibility",
        "width": "Width",
    }

    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url_styling: Optional[TableFieldURLConfiguration] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    width: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableFieldOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "order": "Order",
        "pinned_field_options": "PinnedFieldOptions",
        "transposed_table_options": "TransposedTableOptions",
        "selected_field_options": "SelectedFieldOptions",
    }

    order: Optional[Union[list[str], Ref]] = None
    pinned_field_options: Optional[TablePinnedFieldOptions] = None
    transposed_table_options: Optional[list[TransposedTableOption]] = None
    selected_field_options: Optional[list[TableFieldOption]] = None


@dataclass
class TableFieldURLConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "link_configuration": "LinkConfiguration",
        "image_configuration": "ImageConfiguration",
    }

    link_configuration: Optional[TableFieldLinkConfiguration] = None
    image_configuration: Optional[TableFieldImageConfiguration] = None


@dataclass
class TableFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_unaggregated_field_wells": "TableUnaggregatedFieldWells",
        "table_aggregated_field_wells": "TableAggregatedFieldWells",
    }

    table_unaggregated_field_wells: Optional[TableUnaggregatedFieldWells] = None
    table_aggregated_field_wells: Optional[TableAggregatedFieldWells] = None


@dataclass
class TableInlineVisualization(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_bars": "DataBars",
    }

    data_bars: Optional[DataBarsOptions] = None


@dataclass
class TableOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header_style": "HeaderStyle",
        "cell_style": "CellStyle",
        "orientation": "Orientation",
        "row_alternate_color_options": "RowAlternateColorOptions",
    }

    header_style: Optional[TableCellStyle] = None
    cell_style: Optional[TableCellStyle] = None
    orientation: Optional[Union[str, TableOrientation, Ref, GetAtt, Sub]] = None
    row_alternate_color_options: Optional[RowAlternateColorOptions] = None


@dataclass
class TablePaginatedReportOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "overflow_column_header_visibility": "OverflowColumnHeaderVisibility",
        "vertical_overflow_visibility": "VerticalOverflowVisibility",
    }

    overflow_column_header_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    vertical_overflow_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class TablePinnedFieldOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pinned_left_fields": "PinnedLeftFields",
    }

    pinned_left_fields: Optional[Union[list[str], Ref]] = None


@dataclass
class TableRowConditionalFormatting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_color": "TextColor",
        "background_color": "BackgroundColor",
    }

    text_color: Optional[ConditionalFormattingColor] = None
    background_color: Optional[ConditionalFormattingColor] = None


@dataclass
class TableSideBorderOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "left": "Left",
        "top": "Top",
        "inner_horizontal": "InnerHorizontal",
        "right": "Right",
        "bottom": "Bottom",
        "inner_vertical": "InnerVertical",
    }

    left: Optional[TableBorderOptions] = None
    top: Optional[TableBorderOptions] = None
    inner_horizontal: Optional[TableBorderOptions] = None
    right: Optional[TableBorderOptions] = None
    bottom: Optional[TableBorderOptions] = None
    inner_vertical: Optional[TableBorderOptions] = None


@dataclass
class TableSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "row_sort": "RowSort",
        "pagination_configuration": "PaginationConfiguration",
    }

    row_sort: Optional[list[FieldSortOptions]] = None
    pagination_configuration: Optional[PaginationConfiguration] = None


@dataclass
class TableStyleTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cell_type": "CellType",
    }

    cell_type: Optional[Union[str, StyledCellType, Ref, GetAtt, Sub]] = None


@dataclass
class TableUnaggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[list[UnaggregatedField]] = None


@dataclass
class TableVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "conditional_formatting": "ConditionalFormatting",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    conditional_formatting: Optional[TableConditionalFormatting] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[TableConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TextAreaControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "placeholder_options": "PlaceholderOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
    }

    title_options: Optional[LabelOptions] = None
    placeholder_options: Optional[TextControlPlaceholderOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None


@dataclass
class TextConditionalFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_color": "TextColor",
        "icon": "Icon",
        "background_color": "BackgroundColor",
    }

    text_color: Optional[ConditionalFormattingColor] = None
    icon: Optional[ConditionalFormattingIcon] = None
    background_color: Optional[ConditionalFormattingColor] = None


@dataclass
class TextControlPlaceholderOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class TextFieldControlDisplayOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title_options": "TitleOptions",
        "placeholder_options": "PlaceholderOptions",
        "info_icon_label_options": "InfoIconLabelOptions",
    }

    title_options: Optional[LabelOptions] = None
    placeholder_options: Optional[TextControlPlaceholderOptions] = None
    info_icon_label_options: Optional[SheetControlInfoIconLabelOptions] = None


@dataclass
class ThousandSeparatorOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "symbol": "Symbol",
        "visibility": "Visibility",
        "grouping_style": "GroupingStyle",
    }

    symbol: Optional[Union[str, NumericSeparatorSymbol, Ref, GetAtt, Sub]] = None
    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    grouping_style: Optional[Union[str, DigitGroupingStyle, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedForecastProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "periods_backward": "PeriodsBackward",
        "periods_forward": "PeriodsForward",
        "prediction_interval": "PredictionInterval",
        "seasonality": "Seasonality",
        "upper_boundary": "UpperBoundary",
        "lower_boundary": "LowerBoundary",
    }

    periods_backward: Optional[Union[float, Ref, GetAtt, Sub]] = None
    periods_forward: Optional[Union[float, Ref, GetAtt, Sub]] = None
    prediction_interval: Optional[Union[float, Ref, GetAtt, Sub]] = None
    seasonality: Optional[Union[float, Ref, GetAtt, Sub]] = None
    upper_boundary: Optional[Union[float, Ref, GetAtt, Sub]] = None
    lower_boundary: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TimeEqualityFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "rolling_date": "RollingDate",
        "value": "Value",
        "time_granularity": "TimeGranularity",
        "parameter_name": "ParameterName",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
    }

    column: Optional[ColumnIdentifier] = None
    rolling_date: Optional[RollingDateConfiguration] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeRangeDrillDownFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column": "Column",
        "range_minimum": "RangeMinimum",
        "time_granularity": "TimeGranularity",
        "range_maximum": "RangeMaximum",
    }

    column: Optional[ColumnIdentifier] = None
    range_minimum: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    range_maximum: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeRangeFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "range_minimum_value": "RangeMinimumValue",
        "column": "Column",
        "range_maximum_value": "RangeMaximumValue",
        "include_maximum": "IncludeMaximum",
        "time_granularity": "TimeGranularity",
        "null_option": "NullOption",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
        "include_minimum": "IncludeMinimum",
        "exclude_period_configuration": "ExcludePeriodConfiguration",
    }

    range_minimum_value: Optional[TimeRangeFilterValue] = None
    column: Optional[ColumnIdentifier] = None
    range_maximum_value: Optional[TimeRangeFilterValue] = None
    include_maximum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    null_option: Optional[Union[str, FilterNullOption, Ref, GetAtt, Sub]] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_minimum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclude_period_configuration: Optional[ExcludePeriodConfiguration] = None


@dataclass
class TimeRangeFilterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rolling_date": "RollingDate",
        "static_value": "StaticValue",
        "parameter": "Parameter",
    }

    rolling_date: Optional[RollingDateConfiguration] = None
    static_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TooltipItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field_tooltip_item": "FieldTooltipItem",
        "column_tooltip_item": "ColumnTooltipItem",
    }

    field_tooltip_item: Optional[FieldTooltipItem] = None
    column_tooltip_item: Optional[ColumnTooltipItem] = None


@dataclass
class TooltipOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selected_tooltip_type": "SelectedTooltipType",
        "tooltip_visibility": "TooltipVisibility",
        "field_based_tooltip": "FieldBasedTooltip",
    }

    selected_tooltip_type: Optional[Union[str, SelectedTooltipType, Ref, GetAtt, Sub]] = None
    tooltip_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    field_based_tooltip: Optional[FieldBasedTooltip] = None


@dataclass
class TopBottomFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_sort_configurations": "AggregationSortConfigurations",
        "column": "Column",
        "time_granularity": "TimeGranularity",
        "parameter_name": "ParameterName",
        "limit": "Limit",
        "default_filter_control_configuration": "DefaultFilterControlConfiguration",
        "filter_id": "FilterId",
    }

    aggregation_sort_configurations: Optional[list[AggregationSortConfiguration]] = None
    column: Optional[ColumnIdentifier] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    limit: Optional[Union[float, Ref, GetAtt, Sub]] = None
    default_filter_control_configuration: Optional[DefaultFilterControlConfiguration] = None
    filter_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TopBottomMoversComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "category": "Category",
        "value": "Value",
        "sort_order": "SortOrder",
        "time": "Time",
        "mover_size": "MoverSize",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    type_: Optional[Union[str, TopBottomComputationType, Ref, GetAtt, Sub]] = None
    category: Optional[DimensionField] = None
    value: Optional[MeasureField] = None
    sort_order: Optional[Union[str, TopBottomSortOrder, Ref, GetAtt, Sub]] = None
    time: Optional[DimensionField] = None
    mover_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TopBottomRankedComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "category": "Category",
        "result_size": "ResultSize",
        "value": "Value",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    type_: Optional[Union[str, TopBottomComputationType, Ref, GetAtt, Sub]] = None
    category: Optional[DimensionField] = None
    result_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    value: Optional[MeasureField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TotalAggregationComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    value: Optional[MeasureField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TotalAggregationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "simple_total_aggregation_function": "SimpleTotalAggregationFunction",
    }

    simple_total_aggregation_function: Optional[Union[str, SimpleTotalAggregationFunction, Ref, GetAtt, Sub]] = None


@dataclass
class TotalAggregationOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_aggregation_function": "TotalAggregationFunction",
        "field_id": "FieldId",
    }

    total_aggregation_function: Optional[TotalAggregationFunction] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TotalOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_aggregation_options": "TotalAggregationOptions",
        "custom_label": "CustomLabel",
        "scroll_status": "ScrollStatus",
        "placement": "Placement",
        "total_cell_style": "TotalCellStyle",
        "totals_visibility": "TotalsVisibility",
    }

    total_aggregation_options: Optional[list[TotalAggregationOption]] = None
    custom_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scroll_status: Optional[Union[str, TableTotalsScrollStatus, Ref, GetAtt, Sub]] = None
    placement: Optional[Union[str, TableTotalsPlacement, Ref, GetAtt, Sub]] = None
    total_cell_style: Optional[TableCellStyle] = None
    totals_visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class TransposedTableOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_width": "ColumnWidth",
        "column_index": "ColumnIndex",
        "column_type": "ColumnType",
    }

    column_width: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_index: Optional[Union[float, Ref, GetAtt, Sub]] = None
    column_type: Optional[Union[str, TransposedColumnType, Ref, GetAtt, Sub]] = None


@dataclass
class TreeMapAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sizes": "Sizes",
        "colors": "Colors",
        "groups": "Groups",
    }

    sizes: Optional[list[MeasureField]] = None
    colors: Optional[list[MeasureField]] = None
    groups: Optional[list[DimensionField]] = None


@dataclass
class TreeMapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "data_labels": "DataLabels",
        "color_label_options": "ColorLabelOptions",
        "size_label_options": "SizeLabelOptions",
        "field_wells": "FieldWells",
        "tooltip": "Tooltip",
        "color_scale": "ColorScale",
        "interactions": "Interactions",
        "group_label_options": "GroupLabelOptions",
    }

    sort_configuration: Optional[TreeMapSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    data_labels: Optional[DataLabelOptions] = None
    color_label_options: Optional[ChartAxisLabelOptions] = None
    size_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[TreeMapFieldWells] = None
    tooltip: Optional[TooltipOptions] = None
    color_scale: Optional[ColorScale] = None
    interactions: Optional[VisualInteractionOptions] = None
    group_label_options: Optional[ChartAxisLabelOptions] = None


@dataclass
class TreeMapFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tree_map_aggregated_field_wells": "TreeMapAggregatedFieldWells",
    }

    tree_map_aggregated_field_wells: Optional[TreeMapAggregatedFieldWells] = None


@dataclass
class TreeMapSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tree_map_sort": "TreeMapSort",
        "tree_map_group_items_limit_configuration": "TreeMapGroupItemsLimitConfiguration",
    }

    tree_map_sort: Optional[list[FieldSortOptions]] = None
    tree_map_group_items_limit_configuration: Optional[ItemsLimitConfiguration] = None


@dataclass
class TreeMapVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[TreeMapConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class TrendArrowOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None


@dataclass
class UnaggregatedField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "format_configuration": "FormatConfiguration",
        "column": "Column",
        "field_id": "FieldId",
    }

    format_configuration: Optional[FormatConfiguration] = None
    column: Optional[ColumnIdentifier] = None
    field_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UniqueValuesComputation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "computation_id": "ComputationId",
        "name": "Name",
    }

    category: Optional[DimensionField] = None
    computation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValidationStrategy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, ValidationStrategyMode, Ref, GetAtt, Sub]] = None


@dataclass
class VisibleRangeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "percent_range": "PercentRange",
    }

    percent_range: Optional[PercentVisibleRange] = None


@dataclass
class Visual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "funnel_chart_visual": "FunnelChartVisual",
        "box_plot_visual": "BoxPlotVisual",
        "layer_map_visual": "LayerMapVisual",
        "geospatial_map_visual": "GeospatialMapVisual",
        "scatter_plot_visual": "ScatterPlotVisual",
        "radar_chart_visual": "RadarChartVisual",
        "combo_chart_visual": "ComboChartVisual",
        "word_cloud_visual": "WordCloudVisual",
        "sankey_diagram_visual": "SankeyDiagramVisual",
        "gauge_chart_visual": "GaugeChartVisual",
        "filled_map_visual": "FilledMapVisual",
        "waterfall_visual": "WaterfallVisual",
        "custom_content_visual": "CustomContentVisual",
        "pie_chart_visual": "PieChartVisual",
        "kpi_visual": "KPIVisual",
        "histogram_visual": "HistogramVisual",
        "plugin_visual": "PluginVisual",
        "table_visual": "TableVisual",
        "pivot_table_visual": "PivotTableVisual",
        "bar_chart_visual": "BarChartVisual",
        "heat_map_visual": "HeatMapVisual",
        "tree_map_visual": "TreeMapVisual",
        "insight_visual": "InsightVisual",
        "line_chart_visual": "LineChartVisual",
        "empty_visual": "EmptyVisual",
    }

    funnel_chart_visual: Optional[FunnelChartVisual] = None
    box_plot_visual: Optional[BoxPlotVisual] = None
    layer_map_visual: Optional[LayerMapVisual] = None
    geospatial_map_visual: Optional[GeospatialMapVisual] = None
    scatter_plot_visual: Optional[ScatterPlotVisual] = None
    radar_chart_visual: Optional[RadarChartVisual] = None
    combo_chart_visual: Optional[ComboChartVisual] = None
    word_cloud_visual: Optional[WordCloudVisual] = None
    sankey_diagram_visual: Optional[SankeyDiagramVisual] = None
    gauge_chart_visual: Optional[GaugeChartVisual] = None
    filled_map_visual: Optional[FilledMapVisual] = None
    waterfall_visual: Optional[WaterfallVisual] = None
    custom_content_visual: Optional[CustomContentVisual] = None
    pie_chart_visual: Optional[PieChartVisual] = None
    kpi_visual: Optional[KPIVisual] = None
    histogram_visual: Optional[HistogramVisual] = None
    plugin_visual: Optional[PluginVisual] = None
    table_visual: Optional[TableVisual] = None
    pivot_table_visual: Optional[PivotTableVisual] = None
    bar_chart_visual: Optional[BarChartVisual] = None
    heat_map_visual: Optional[HeatMapVisual] = None
    tree_map_visual: Optional[TreeMapVisual] = None
    insight_visual: Optional[InsightVisual] = None
    line_chart_visual: Optional[LineChartVisual] = None
    empty_visual: Optional[EmptyVisual] = None


@dataclass
class VisualAxisSortOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class VisualCustomAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "trigger": "Trigger",
        "custom_action_id": "CustomActionId",
        "name": "Name",
        "action_operations": "ActionOperations",
    }

    status: Optional[Union[str, WidgetStatus, Ref, GetAtt, Sub]] = None
    trigger: Optional[Union[str, VisualCustomActionTrigger, Ref, GetAtt, Sub]] = None
    custom_action_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_operations: Optional[list[VisualCustomActionOperation]] = None


@dataclass
class VisualCustomActionOperation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "navigation_operation": "NavigationOperation",
        "set_parameters_operation": "SetParametersOperation",
        "filter_operation": "FilterOperation",
        "url_operation": "URLOperation",
    }

    navigation_operation: Optional[CustomActionNavigationOperation] = None
    set_parameters_operation: Optional[CustomActionSetParametersOperation] = None
    filter_operation: Optional[CustomActionFilterOperation] = None
    url_operation: Optional[CustomActionURLOperation] = None


@dataclass
class VisualInteractionOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "context_menu_option": "ContextMenuOption",
        "visual_menu_option": "VisualMenuOption",
    }

    context_menu_option: Optional[ContextMenuOption] = None
    visual_menu_option: Optional[VisualMenuOption] = None


@dataclass
class VisualMenuOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_status": "AvailabilityStatus",
    }

    availability_status: Optional[Union[str, DashboardBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class VisualPalette(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "chart_color": "ChartColor",
        "color_map": "ColorMap",
    }

    chart_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    color_map: Optional[list[DataPathColor]] = None


@dataclass
class VisualSubtitleLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
        "format_text": "FormatText",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    format_text: Optional[LongFormatText] = None


@dataclass
class VisualTitleLabelOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "visibility": "Visibility",
        "format_text": "FormatText",
    }

    visibility: Optional[Union[str, Visibility, Ref, GetAtt, Sub]] = None
    format_text: Optional[ShortFormatText] = None


@dataclass
class WaterfallChartAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "categories": "Categories",
        "breakdowns": "Breakdowns",
        "values": "Values",
    }

    categories: Optional[list[DimensionField]] = None
    breakdowns: Optional[list[DimensionField]] = None
    values: Optional[list[MeasureField]] = None


@dataclass
class WaterfallChartColorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_color_configuration": "GroupColorConfiguration",
    }

    group_color_configuration: Optional[WaterfallChartGroupColorConfiguration] = None


@dataclass
class WaterfallChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_axis_label_options": "CategoryAxisLabelOptions",
        "sort_configuration": "SortConfiguration",
        "legend": "Legend",
        "data_labels": "DataLabels",
        "primary_y_axis_label_options": "PrimaryYAxisLabelOptions",
        "field_wells": "FieldWells",
        "waterfall_chart_options": "WaterfallChartOptions",
        "color_configuration": "ColorConfiguration",
        "interactions": "Interactions",
        "category_axis_display_options": "CategoryAxisDisplayOptions",
        "primary_y_axis_display_options": "PrimaryYAxisDisplayOptions",
        "visual_palette": "VisualPalette",
    }

    category_axis_label_options: Optional[ChartAxisLabelOptions] = None
    sort_configuration: Optional[WaterfallChartSortConfiguration] = None
    legend: Optional[LegendOptions] = None
    data_labels: Optional[DataLabelOptions] = None
    primary_y_axis_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[WaterfallChartFieldWells] = None
    waterfall_chart_options: Optional[WaterfallChartOptions] = None
    color_configuration: Optional[WaterfallChartColorConfiguration] = None
    interactions: Optional[VisualInteractionOptions] = None
    category_axis_display_options: Optional[AxisDisplayOptions] = None
    primary_y_axis_display_options: Optional[AxisDisplayOptions] = None
    visual_palette: Optional[VisualPalette] = None


@dataclass
class WaterfallChartFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "waterfall_chart_aggregated_field_wells": "WaterfallChartAggregatedFieldWells",
    }

    waterfall_chart_aggregated_field_wells: Optional[WaterfallChartAggregatedFieldWells] = None


@dataclass
class WaterfallChartGroupColorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "negative_bar_color": "NegativeBarColor",
        "total_bar_color": "TotalBarColor",
        "positive_bar_color": "PositiveBarColor",
    }

    negative_bar_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    total_bar_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    positive_bar_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WaterfallChartOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_bar_label": "TotalBarLabel",
    }

    total_bar_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WaterfallChartSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "breakdown_items_limit": "BreakdownItemsLimit",
        "category_sort": "CategorySort",
    }

    breakdown_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class WaterfallVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[WaterfallChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class WhatIfPointScenario(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "date": "Date",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    date: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WhatIfRangeScenario(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start_date": "StartDate",
        "value": "Value",
        "end_date": "EndDate",
    }

    start_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    end_date: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WordCloudAggregatedFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_by": "GroupBy",
        "size": "Size",
    }

    group_by: Optional[list[DimensionField]] = None
    size: Optional[list[MeasureField]] = None


@dataclass
class WordCloudChartConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sort_configuration": "SortConfiguration",
        "category_label_options": "CategoryLabelOptions",
        "field_wells": "FieldWells",
        "word_cloud_options": "WordCloudOptions",
        "interactions": "Interactions",
    }

    sort_configuration: Optional[WordCloudSortConfiguration] = None
    category_label_options: Optional[ChartAxisLabelOptions] = None
    field_wells: Optional[WordCloudFieldWells] = None
    word_cloud_options: Optional[WordCloudOptions] = None
    interactions: Optional[VisualInteractionOptions] = None


@dataclass
class WordCloudFieldWells(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "word_cloud_aggregated_field_wells": "WordCloudAggregatedFieldWells",
    }

    word_cloud_aggregated_field_wells: Optional[WordCloudAggregatedFieldWells] = None


@dataclass
class WordCloudOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "word_orientation": "WordOrientation",
        "word_scaling": "WordScaling",
        "cloud_layout": "CloudLayout",
        "maximum_string_length": "MaximumStringLength",
        "word_casing": "WordCasing",
        "word_padding": "WordPadding",
    }

    word_orientation: Optional[Union[str, WordCloudWordOrientation, Ref, GetAtt, Sub]] = None
    word_scaling: Optional[Union[str, WordCloudWordScaling, Ref, GetAtt, Sub]] = None
    cloud_layout: Optional[Union[str, WordCloudCloudLayout, Ref, GetAtt, Sub]] = None
    maximum_string_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    word_casing: Optional[Union[str, WordCloudWordCasing, Ref, GetAtt, Sub]] = None
    word_padding: Optional[Union[str, WordCloudWordPadding, Ref, GetAtt, Sub]] = None


@dataclass
class WordCloudSortConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "category_items_limit": "CategoryItemsLimit",
        "category_sort": "CategorySort",
    }

    category_items_limit: Optional[ItemsLimitConfiguration] = None
    category_sort: Optional[list[FieldSortOptions]] = None


@dataclass
class WordCloudVisual(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subtitle": "Subtitle",
        "visual_id": "VisualId",
        "chart_configuration": "ChartConfiguration",
        "actions": "Actions",
        "title": "Title",
        "visual_content_alt_text": "VisualContentAltText",
        "column_hierarchies": "ColumnHierarchies",
    }

    subtitle: Optional[VisualSubtitleLabelOptions] = None
    visual_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chart_configuration: Optional[WordCloudChartConfiguration] = None
    actions: Optional[list[VisualCustomAction]] = None
    title: Optional[VisualTitleLabelOptions] = None
    visual_content_alt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_hierarchies: Optional[list[ColumnHierarchy]] = None


@dataclass
class YAxisOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "y_axis": "YAxis",
    }

    y_axis: Optional[Union[str, SingleYAxisOption, Ref, GetAtt, Sub]] = None

