"""PropertyTypes for AWS::IoTSiteWise::Asset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssetHierarchy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logical_id": "LogicalId",
        "external_id": "ExternalId",
        "id": "Id",
        "child_asset_id": "ChildAssetId",
    }

    logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    child_asset_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssetProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logical_id": "LogicalId",
        "alias": "Alias",
        "external_id": "ExternalId",
        "id": "Id",
        "unit": "Unit",
        "notification_state": "NotificationState",
    }

    logical_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_state: Optional[Union[str, Ref, GetAtt, Sub]] = None

