"""PropertyTypes for AWS::IoTSiteWise::AssetModel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssetModelCompositeModel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "parent_asset_model_composite_model_external_id": "ParentAssetModelCompositeModelExternalId",
        "type_": "Type",
        "description": "Description",
        "composed_asset_model_id": "ComposedAssetModelId",
        "external_id": "ExternalId",
        "composite_model_properties": "CompositeModelProperties",
        "id": "Id",
        "name": "Name",
    }

    path: Optional[Union[list[str], Ref]] = None
    parent_asset_model_composite_model_external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    composed_asset_model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    composite_model_properties: Optional[list[AssetModelProperty]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetModelHierarchy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logical_id": "LogicalId",
        "external_id": "ExternalId",
        "id": "Id",
        "child_asset_model_id": "ChildAssetModelId",
        "name": "Name",
    }

    logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    child_asset_model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetModelProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "logical_id": "LogicalId",
        "external_id": "ExternalId",
        "data_type_spec": "DataTypeSpec",
        "data_type": "DataType",
        "id": "Id",
        "unit": "Unit",
        "name": "Name",
    }

    type_: Optional[PropertyType] = None
    logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type_spec: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Attribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnforcedAssetModelInterfacePropertyMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interface_asset_model_property_external_id": "InterfaceAssetModelPropertyExternalId",
        "asset_model_property_logical_id": "AssetModelPropertyLogicalId",
        "asset_model_property_external_id": "AssetModelPropertyExternalId",
    }

    interface_asset_model_property_external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    asset_model_property_logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    asset_model_property_external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnforcedAssetModelInterfaceRelationship(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interface_asset_model_id": "InterfaceAssetModelId",
        "property_mappings": "PropertyMappings",
    }

    interface_asset_model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_mappings: Optional[list[EnforcedAssetModelInterfacePropertyMapping]] = None


@dataclass
class ExpressionVariable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[VariableValue] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Metric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "window": "Window",
        "expression": "Expression",
    }

    variables: Optional[list[ExpressionVariable]] = None
    window: Optional[MetricWindow] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricWindow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tumbling": "Tumbling",
    }

    tumbling: Optional[TumblingWindow] = None


@dataclass
class PropertyPathDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PropertyType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_name": "TypeName",
        "attribute": "Attribute",
        "metric": "Metric",
        "transform": "Transform",
    }

    type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute: Optional[Attribute] = None
    metric: Optional[Metric] = None
    transform: Optional[Transform] = None


@dataclass
class Transform(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "expression": "Expression",
    }

    variables: Optional[list[ExpressionVariable]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TumblingWindow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "interval": "Interval",
        "offset": "Offset",
    }

    interval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VariableValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "property_external_id": "PropertyExternalId",
        "hierarchy_id": "HierarchyId",
        "property_logical_id": "PropertyLogicalId",
        "hierarchy_logical_id": "HierarchyLogicalId",
        "property_path": "PropertyPath",
        "hierarchy_external_id": "HierarchyExternalId",
        "property_id": "PropertyId",
    }

    property_external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_path: Optional[list[PropertyPathDefinition]] = None
    hierarchy_external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

