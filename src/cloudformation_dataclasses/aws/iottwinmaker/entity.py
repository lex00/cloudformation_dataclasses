"""PropertyTypes for AWS::IoTTwinMaker::Entity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Component(PropertyType):
    STATUS = "Status"
    DESCRIPTION = "Description"
    DEFINED_IN = "DefinedIn"
    PROPERTY_GROUPS = "PropertyGroups"
    COMPONENT_TYPE_ID = "ComponentTypeId"
    COMPONENT_NAME = "ComponentName"
    PROPERTIES = "Properties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "description": "Description",
        "defined_in": "DefinedIn",
        "property_groups": "PropertyGroups",
        "component_type_id": "ComponentTypeId",
        "component_name": "ComponentName",
        "properties": "Properties",
    }

    status: Optional[Status] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    defined_in: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_groups: Optional[dict[str, Any]] = None
    component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    properties: Optional[dict[str, Any]] = None


@dataclass
class CompositeComponent(PropertyType):
    STATUS = "Status"
    COMPONENT_PATH = "ComponentPath"
    DESCRIPTION = "Description"
    PROPERTY_GROUPS = "PropertyGroups"
    COMPONENT_TYPE_ID = "ComponentTypeId"
    COMPONENT_NAME = "ComponentName"
    PROPERTIES = "Properties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "component_path": "ComponentPath",
        "description": "Description",
        "property_groups": "PropertyGroups",
        "component_type_id": "ComponentTypeId",
        "component_name": "ComponentName",
        "properties": "Properties",
    }

    status: Optional[Status] = None
    component_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_groups: Optional[dict[str, Any]] = None
    component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    properties: Optional[dict[str, Any]] = None


@dataclass
class DataType(PropertyType):
    TYPE = "Type"
    ALLOWED_VALUES = "AllowedValues"
    UNIT_OF_MEASURE = "UnitOfMeasure"
    RELATIONSHIP = "Relationship"
    NESTED_TYPE = "NestedType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "allowed_values": "AllowedValues",
        "unit_of_measure": "UnitOfMeasure",
        "relationship": "Relationship",
        "nested_type": "NestedType",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[list[DataValue]] = None
    unit_of_measure: Optional[Union[str, Ref, GetAtt, Sub]] = None
    relationship: Optional[Relationship] = None
    nested_type: Optional[DataType] = None


@dataclass
class DataValue(PropertyType):
    DOUBLE_VALUE = "DoubleValue"
    EXPRESSION = "Expression"
    BOOLEAN_VALUE = "BooleanValue"
    INTEGER_VALUE = "IntegerValue"
    LIST_VALUE = "ListValue"
    LONG_VALUE = "LongValue"
    MAP_VALUE = "MapValue"
    RELATIONSHIP_VALUE = "RelationshipValue"
    STRING_VALUE = "StringValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "double_value": "DoubleValue",
        "expression": "Expression",
        "boolean_value": "BooleanValue",
        "integer_value": "IntegerValue",
        "list_value": "ListValue",
        "long_value": "LongValue",
        "map_value": "MapValue",
        "relationship_value": "RelationshipValue",
        "string_value": "StringValue",
    }

    double_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    boolean_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    integer_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    list_value: Optional[list[DataValue]] = None
    long_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    map_value: Optional[dict[str, Any]] = None
    relationship_value: Optional[RelationshipValue] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Definition(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    IS_IMPORTED = "IsImported"
    IS_INHERITED = "IsInherited"
    CONFIGURATION = "Configuration"
    IS_EXTERNAL_ID = "IsExternalId"
    IS_STORED_EXTERNALLY = "IsStoredExternally"
    IS_TIME_SERIES = "IsTimeSeries"
    IS_REQUIRED_IN_ENTITY = "IsRequiredInEntity"
    DATA_TYPE = "DataType"
    IS_FINAL = "IsFinal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "is_imported": "IsImported",
        "is_inherited": "IsInherited",
        "configuration": "Configuration",
        "is_external_id": "IsExternalId",
        "is_stored_externally": "IsStoredExternally",
        "is_time_series": "IsTimeSeries",
        "is_required_in_entity": "IsRequiredInEntity",
        "data_type": "DataType",
        "is_final": "IsFinal",
    }

    default_value: Optional[DataValue] = None
    is_imported: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_inherited: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    configuration: Optional[dict[str, str]] = None
    is_external_id: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_stored_externally: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_time_series: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_required_in_entity: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_type: Optional[DataType] = None
    is_final: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Error(PropertyType):
    MESSAGE = "Message"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Property(PropertyType):
    DEFINITION = "Definition"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
        "value": "Value",
    }

    definition: Optional[Definition] = None
    value: Optional[DataValue] = None


@dataclass
class PropertyGroup(PropertyType):
    GROUP_TYPE = "GroupType"
    PROPERTY_NAMES = "PropertyNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_type": "GroupType",
        "property_names": "PropertyNames",
    }

    group_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_names: Optional[Union[list[str], Ref]] = None


@dataclass
class Relationship(PropertyType):
    RELATIONSHIP_TYPE = "RelationshipType"
    TARGET_COMPONENT_TYPE_ID = "TargetComponentTypeId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "relationship_type": "RelationshipType",
        "target_component_type_id": "TargetComponentTypeId",
    }

    relationship_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RelationshipValue(PropertyType):
    TARGET_COMPONENT_NAME = "TargetComponentName"
    TARGET_ENTITY_ID = "TargetEntityId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_component_name": "TargetComponentName",
        "target_entity_id": "TargetEntityId",
    }

    target_component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Status(PropertyType):
    STATE = "State"
    ERROR = "Error"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "error": "Error",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error: Optional[Error] = None

