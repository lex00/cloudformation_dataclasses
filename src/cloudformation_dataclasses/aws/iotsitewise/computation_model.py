"""PropertyTypes for AWS::IoTSiteWise::ComputationModel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnomalyDetectionComputationModelConfiguration(PropertyType):
    RESULT_PROPERTY = "ResultProperty"
    INPUT_PROPERTIES = "InputProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "result_property": "ResultProperty",
        "input_properties": "InputProperties",
    }

    result_property: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_properties: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetModelPropertyBindingValue(PropertyType):
    ASSET_MODEL_ID = "AssetModelId"
    PROPERTY_ID = "PropertyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "asset_model_id": "AssetModelId",
        "property_id": "PropertyId",
    }

    asset_model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetPropertyBindingValue(PropertyType):
    ASSET_ID = "AssetId"
    PROPERTY_ID = "PropertyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "asset_id": "AssetId",
        "property_id": "PropertyId",
    }

    asset_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComputationModelConfiguration(PropertyType):
    ANOMALY_DETECTION = "AnomalyDetection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "anomaly_detection": "AnomalyDetection",
    }

    anomaly_detection: Optional[AnomalyDetectionComputationModelConfiguration] = None


@dataclass
class ComputationModelDataBindingValue(PropertyType):
    ASSET_PROPERTY = "AssetProperty"
    ASSET_MODEL_PROPERTY = "AssetModelProperty"
    LIST = "List"

    _property_mappings: ClassVar[dict[str, str]] = {
        "asset_property": "AssetProperty",
        "asset_model_property": "AssetModelProperty",
        "list": "List",
    }

    asset_property: Optional[AssetPropertyBindingValue] = None
    asset_model_property: Optional[AssetModelPropertyBindingValue] = None
    list: Optional[list[ComputationModelDataBindingValue]] = None

