"""PropertyTypes for AWS::AmplifyUIBuilder::Component."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "anchor": "Anchor",
        "target": "Target",
        "fields": "Fields",
        "state": "State",
        "model": "Model",
        "id": "Id",
        "url": "Url",
        "global_": "Global",
    }

    type_: Optional[ComponentProperty] = None
    anchor: Optional[ComponentProperty] = None
    target: Optional[ComponentProperty] = None
    fields: Optional[dict[str, Any]] = None
    state: Optional[MutationActionSetStateParameter] = None
    model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[ComponentProperty] = None
    url: Optional[ComponentProperty] = None
    global_: Optional[ComponentProperty] = None


@dataclass
class ComponentBindingPropertiesValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "type_": "Type",
        "binding_properties": "BindingProperties",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    binding_properties: Optional[ComponentBindingPropertiesValueProperties] = None


@dataclass
class ComponentBindingPropertiesValueProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "default_value": "DefaultValue",
        "bucket": "Bucket",
        "user_attribute": "UserAttribute",
        "model": "Model",
        "predicates": "Predicates",
        "slot_name": "SlotName",
        "key": "Key",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    predicates: Optional[list[Predicate]] = None
    slot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentChild(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "component_type": "ComponentType",
        "events": "Events",
        "source_id": "SourceId",
        "children": "Children",
        "properties": "Properties",
        "name": "Name",
    }

    component_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    events: Optional[dict[str, Any]] = None
    source_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    children: Optional[list[ComponentChild]] = None
    properties: Optional[dict[str, Any]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentConditionProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "field": "Field",
        "operand": "Operand",
        "operand_type": "OperandType",
        "else_": "Else",
        "then": "Then",
        "property": "Property",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    operand: Optional[Union[str, Ref, GetAtt, Sub]] = None
    operand_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    else_: Optional[ComponentProperty] = None
    then: Optional[ComponentProperty] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentDataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model": "Model",
        "sort": "Sort",
        "identifiers": "Identifiers",
        "predicate": "Predicate",
    }

    model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sort: Optional[list[SortProperty]] = None
    identifiers: Optional[Union[list[str], Ref]] = None
    predicate: Optional[Predicate] = None


@dataclass
class ComponentEvent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "parameters": "Parameters",
        "binding_event": "BindingEvent",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[ActionParameters] = None
    binding_event: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "user_attribute": "UserAttribute",
        "imported_value": "ImportedValue",
        "binding_properties": "BindingProperties",
        "bindings": "Bindings",
        "configured": "Configured",
        "concat": "Concat",
        "default_value": "DefaultValue",
        "type_": "Type",
        "value": "Value",
        "model": "Model",
        "collection_binding_properties": "CollectionBindingProperties",
        "event": "Event",
        "component_name": "ComponentName",
        "property": "Property",
    }

    condition: Optional[ComponentConditionProperty] = None
    user_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    imported_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    binding_properties: Optional[ComponentPropertyBindingProperties] = None
    bindings: Optional[dict[str, Any]] = None
    configured: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    concat: Optional[list[ComponentProperty]] = None
    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    collection_binding_properties: Optional[ComponentPropertyBindingProperties] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentPropertyBindingProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "property": "Property",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentVariant(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variant_values": "VariantValues",
        "overrides": "Overrides",
    }

    variant_values: Optional[dict[str, str]] = None
    overrides: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class FormBindingElement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "element": "Element",
        "property": "Property",
    }

    element: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MutationActionSetStateParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "set": "Set",
        "component_name": "ComponentName",
        "property": "Property",
    }

    set: Optional[ComponentProperty] = None
    component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Predicate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "field": "Field",
        "or_": "Or",
        "and_": "And",
        "operand": "Operand",
        "operand_type": "OperandType",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    or_: Optional[list[Predicate]] = None
    and_: Optional[list[Predicate]] = None
    operand: Optional[Union[str, Ref, GetAtt, Sub]] = None
    operand_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SortProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "direction": "Direction",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    direction: Optional[Union[str, Ref, GetAtt, Sub]] = None

