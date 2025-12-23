"""PropertyTypes for AWS::IoTFleetWise::SignalCatalog."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Actuator(PropertyType):
    DESCRIPTION = "Description"
    ALLOWED_VALUES = "AllowedValues"
    MIN = "Min"
    MAX = "Max"
    FULLY_QUALIFIED_NAME = "FullyQualifiedName"
    ASSIGNED_VALUE = "AssignedValue"
    DATA_TYPE = "DataType"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "allowed_values": "AllowedValues",
        "min": "Min",
        "max": "Max",
        "fully_qualified_name": "FullyQualifiedName",
        "assigned_value": "AssignedValue",
        "data_type": "DataType",
        "unit": "Unit",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[Union[list[str], Ref]] = None
    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    assigned_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Attribute(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    DESCRIPTION = "Description"
    ALLOWED_VALUES = "AllowedValues"
    MIN = "Min"
    MAX = "Max"
    FULLY_QUALIFIED_NAME = "FullyQualifiedName"
    ASSIGNED_VALUE = "AssignedValue"
    DATA_TYPE = "DataType"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "description": "Description",
        "allowed_values": "AllowedValues",
        "min": "Min",
        "max": "Max",
        "fully_qualified_name": "FullyQualifiedName",
        "assigned_value": "AssignedValue",
        "data_type": "DataType",
        "unit": "Unit",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[Union[list[str], Ref]] = None
    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    assigned_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Branch(PropertyType):
    DESCRIPTION = "Description"
    FULLY_QUALIFIED_NAME = "FullyQualifiedName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "fully_qualified_name": "FullyQualifiedName",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Node(PropertyType):
    ATTRIBUTE = "Attribute"
    BRANCH = "Branch"
    SENSOR = "Sensor"
    ACTUATOR = "Actuator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "branch": "Branch",
        "sensor": "Sensor",
        "actuator": "Actuator",
    }

    attribute: Optional[Attribute] = None
    branch: Optional[Branch] = None
    sensor: Optional[Sensor] = None
    actuator: Optional[Actuator] = None


@dataclass
class NodeCounts(PropertyType):
    TOTAL_ACTUATORS = "TotalActuators"
    TOTAL_NODES = "TotalNodes"
    TOTAL_ATTRIBUTES = "TotalAttributes"
    TOTAL_BRANCHES = "TotalBranches"
    TOTAL_SENSORS = "TotalSensors"

    _property_mappings: ClassVar[dict[str, str]] = {
        "total_actuators": "TotalActuators",
        "total_nodes": "TotalNodes",
        "total_attributes": "TotalAttributes",
        "total_branches": "TotalBranches",
        "total_sensors": "TotalSensors",
    }

    total_actuators: Optional[Union[float, Ref, GetAtt, Sub]] = None
    total_nodes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    total_attributes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    total_branches: Optional[Union[float, Ref, GetAtt, Sub]] = None
    total_sensors: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Sensor(PropertyType):
    DESCRIPTION = "Description"
    ALLOWED_VALUES = "AllowedValues"
    MIN = "Min"
    MAX = "Max"
    FULLY_QUALIFIED_NAME = "FullyQualifiedName"
    DATA_TYPE = "DataType"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "allowed_values": "AllowedValues",
        "min": "Min",
        "max": "Max",
        "fully_qualified_name": "FullyQualifiedName",
        "data_type": "DataType",
        "unit": "Unit",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[Union[list[str], Ref]] = None
    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None

