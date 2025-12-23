"""PropertyTypes for AWS::IoTTwinMaker::ComponentType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CompositeComponentType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "component_type_id": "ComponentTypeId",
    }

    component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataConnector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_native": "IsNative",
        "lambda_": "Lambda",
    }

    is_native: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    lambda_: Optional[LambdaFunction] = None


@dataclass
class DataType(PropertyType):
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
class Error(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Function(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "required_properties": "RequiredProperties",
        "implemented_by": "ImplementedBy",
    }

    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required_properties: Optional[Union[list[str], Ref]] = None
    implemented_by: Optional[DataConnector] = None


@dataclass
class LambdaFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PropertyDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "is_external_id": "IsExternalId",
        "is_stored_externally": "IsStoredExternally",
        "is_time_series": "IsTimeSeries",
        "is_required_in_entity": "IsRequiredInEntity",
        "data_type": "DataType",
        "configurations": "Configurations",
    }

    default_value: Optional[DataValue] = None
    is_external_id: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_stored_externally: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_time_series: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_required_in_entity: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_type: Optional[DataType] = None
    configurations: Optional[dict[str, str]] = None


@dataclass
class PropertyGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_type": "GroupType",
        "property_names": "PropertyNames",
    }

    group_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_names: Optional[Union[list[str], Ref]] = None


@dataclass
class Relationship(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "relationship_type": "RelationshipType",
        "target_component_type_id": "TargetComponentTypeId",
    }

    relationship_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RelationshipValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_component_name": "TargetComponentName",
        "target_entity_id": "TargetEntityId",
    }

    target_component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Status(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "error": "Error",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error: Optional[Error] = None

