"""PropertyTypes for AWS::SecurityHub::AutomationRuleV2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutomationRulesActionV2(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "external_integration_configuration": "ExternalIntegrationConfiguration",
        "finding_fields_update": "FindingFieldsUpdate",
    }

    type_: Optional[Union[str, AutomationRulesActionTypeV2, Ref, GetAtt, Sub]] = None
    external_integration_configuration: Optional[ExternalIntegrationConfiguration] = None
    finding_fields_update: Optional[AutomationRulesFindingFieldsUpdateV2] = None


@dataclass
class AutomationRulesFindingFieldsUpdateV2(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "status_id": "StatusId",
        "severity_id": "SeverityId",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    severity_id: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BooleanFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CompositeFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "string_filters": "StringFilters",
        "boolean_filters": "BooleanFilters",
        "date_filters": "DateFilters",
        "number_filters": "NumberFilters",
        "map_filters": "MapFilters",
    }

    operator: Optional[Union[str, AllowedOperators, Ref, GetAtt, Sub]] = None
    string_filters: Optional[list[OcsfStringFilter]] = None
    boolean_filters: Optional[list[OcsfBooleanFilter]] = None
    date_filters: Optional[list[OcsfDateFilter]] = None
    number_filters: Optional[list[OcsfNumberFilter]] = None
    map_filters: Optional[list[OcsfMapFilter]] = None


@dataclass
class Criteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ocsf_finding_criteria": "OcsfFindingCriteria",
    }

    ocsf_finding_criteria: Optional[OcsfFindingFilters] = None


@dataclass
class DateFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "date_range": "DateRange",
        "start": "Start",
        "end": "End",
    }

    date_range: Optional[DateRange] = None
    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, DateRangeUnit, Ref, GetAtt, Sub]] = None


@dataclass
class ExternalIntegrationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_arn": "ConnectorArn",
    }

    connector_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MapFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
        "key": "Key",
    }

    comparison: Optional[Union[str, MapFilterComparison, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumberFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gte": "Gte",
        "eq": "Eq",
        "lte": "Lte",
    }

    gte: Optional[Union[float, Ref, GetAtt, Sub]] = None
    eq: Optional[Union[float, Ref, GetAtt, Sub]] = None
    lte: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfBooleanFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[BooleanFilter] = None
    field_name: Optional[Union[str, OcsfBooleanField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfDateFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[DateFilter] = None
    field_name: Optional[Union[str, OcsfDateField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfFindingFilters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "composite_filters": "CompositeFilters",
        "composite_operator": "CompositeOperator",
    }

    composite_filters: Optional[list[CompositeFilter]] = None
    composite_operator: Optional[Union[str, AllowedOperators, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfMapFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[MapFilter] = None
    field_name: Optional[Union[str, OcsfMapField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfNumberFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[NumberFilter] = None
    field_name: Optional[Union[str, OcsfNumberField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfStringFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[StringFilter] = None
    field_name: Optional[Union[str, OcsfStringField, Ref, GetAtt, Sub]] = None


@dataclass
class StringFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
    }

    comparison: Optional[Union[str, StringFilterComparison, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None

