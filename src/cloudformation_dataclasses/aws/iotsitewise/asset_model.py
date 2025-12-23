"""PropertyTypes for AWS::IoTSiteWise::AssetModel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssetModelCompositeModel(PropertyType):
    PATH = "Path"
    PARENT_ASSET_MODEL_COMPOSITE_MODEL_EXTERNAL_ID = "ParentAssetModelCompositeModelExternalId"
    TYPE = "Type"
    DESCRIPTION = "Description"
    COMPOSED_ASSET_MODEL_ID = "ComposedAssetModelId"
    EXTERNAL_ID = "ExternalId"
    COMPOSITE_MODEL_PROPERTIES = "CompositeModelProperties"
    ID = "Id"
    NAME = "Name"

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
    LOGICAL_ID = "LogicalId"
    EXTERNAL_ID = "ExternalId"
    ID = "Id"
    CHILD_ASSET_MODEL_ID = "ChildAssetModelId"
    NAME = "Name"

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
    TYPE = "Type"
    LOGICAL_ID = "LogicalId"
    EXTERNAL_ID = "ExternalId"
    DATA_TYPE_SPEC = "DataTypeSpec"
    DATA_TYPE = "DataType"
    ID = "Id"
    UNIT = "Unit"
    NAME = "Name"

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
    DEFAULT_VALUE = "DefaultValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnforcedAssetModelInterfacePropertyMapping(PropertyType):
    INTERFACE_ASSET_MODEL_PROPERTY_EXTERNAL_ID = "InterfaceAssetModelPropertyExternalId"
    ASSET_MODEL_PROPERTY_LOGICAL_ID = "AssetModelPropertyLogicalId"
    ASSET_MODEL_PROPERTY_EXTERNAL_ID = "AssetModelPropertyExternalId"

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
    INTERFACE_ASSET_MODEL_ID = "InterfaceAssetModelId"
    PROPERTY_MAPPINGS = "PropertyMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interface_asset_model_id": "InterfaceAssetModelId",
        "property_mappings": "PropertyMappings",
    }

    interface_asset_model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_mappings: Optional[list[EnforcedAssetModelInterfacePropertyMapping]] = None


@dataclass
class ExpressionVariable(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[VariableValue] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Metric(PropertyType):
    VARIABLES = "Variables"
    WINDOW = "Window"
    EXPRESSION = "Expression"

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
    TUMBLING = "Tumbling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tumbling": "Tumbling",
    }

    tumbling: Optional[TumblingWindow] = None


@dataclass
class PropertyPathDefinition(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PropertyType(PropertyType):
    TYPE_NAME = "TypeName"
    ATTRIBUTE = "Attribute"
    METRIC = "Metric"
    TRANSFORM = "Transform"

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
    VARIABLES = "Variables"
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "expression": "Expression",
    }

    variables: Optional[list[ExpressionVariable]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TumblingWindow(PropertyType):
    INTERVAL = "Interval"
    OFFSET = "Offset"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval": "Interval",
        "offset": "Offset",
    }

    interval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VariableValue(PropertyType):
    PROPERTY_EXTERNAL_ID = "PropertyExternalId"
    HIERARCHY_ID = "HierarchyId"
    PROPERTY_LOGICAL_ID = "PropertyLogicalId"
    HIERARCHY_LOGICAL_ID = "HierarchyLogicalId"
    PROPERTY_PATH = "PropertyPath"
    HIERARCHY_EXTERNAL_ID = "HierarchyExternalId"
    PROPERTY_ID = "PropertyId"

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

