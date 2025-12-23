"""PropertyTypes for AWS::SecurityHub::AutomationRuleV2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutomationRulesActionV2(PropertyType):
    TYPE = "Type"
    EXTERNAL_INTEGRATION_CONFIGURATION = "ExternalIntegrationConfiguration"
    FINDING_FIELDS_UPDATE = "FindingFieldsUpdate"

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
    COMMENT = "Comment"
    STATUS_ID = "StatusId"
    SEVERITY_ID = "SeverityId"

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
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CompositeFilter(PropertyType):
    OPERATOR = "Operator"
    STRING_FILTERS = "StringFilters"
    BOOLEAN_FILTERS = "BooleanFilters"
    DATE_FILTERS = "DateFilters"
    NUMBER_FILTERS = "NumberFilters"
    MAP_FILTERS = "MapFilters"

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
    OCSF_FINDING_CRITERIA = "OcsfFindingCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ocsf_finding_criteria": "OcsfFindingCriteria",
    }

    ocsf_finding_criteria: Optional[OcsfFindingFilters] = None


@dataclass
class DateFilter(PropertyType):
    DATE_RANGE = "DateRange"
    START = "Start"
    END = "End"

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
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, DateRangeUnit, Ref, GetAtt, Sub]] = None


@dataclass
class ExternalIntegrationConfiguration(PropertyType):
    CONNECTOR_ARN = "ConnectorArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_arn": "ConnectorArn",
    }

    connector_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MapFilter(PropertyType):
    COMPARISON = "Comparison"
    VALUE = "Value"
    KEY = "Key"

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
    GTE = "Gte"
    EQ = "Eq"
    LTE = "Lte"

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
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[BooleanFilter] = None
    field_name: Optional[Union[str, OcsfBooleanField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfDateFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[DateFilter] = None
    field_name: Optional[Union[str, OcsfDateField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfFindingFilters(PropertyType):
    COMPOSITE_FILTERS = "CompositeFilters"
    COMPOSITE_OPERATOR = "CompositeOperator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "composite_filters": "CompositeFilters",
        "composite_operator": "CompositeOperator",
    }

    composite_filters: Optional[list[CompositeFilter]] = None
    composite_operator: Optional[Union[str, AllowedOperators, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfMapFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[MapFilter] = None
    field_name: Optional[Union[str, OcsfMapField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfNumberFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[NumberFilter] = None
    field_name: Optional[Union[str, OcsfNumberField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfStringFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[StringFilter] = None
    field_name: Optional[Union[str, OcsfStringField, Ref, GetAtt, Sub]] = None


@dataclass
class StringFilter(PropertyType):
    COMPARISON = "Comparison"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
    }

    comparison: Optional[Union[str, StringFilterComparison, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None

