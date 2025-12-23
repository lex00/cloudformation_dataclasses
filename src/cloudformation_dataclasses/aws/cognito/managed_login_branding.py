"""PropertyTypes for AWS::Cognito::ManagedLoginBranding."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssetType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "extension": "Extension",
        "bytes": "Bytes",
        "category": "Category",
        "resource_id": "ResourceId",
        "color_mode": "ColorMode",
    }

    extension: Optional[Union[str, AssetExtensionType, Ref, GetAtt, Sub]] = None
    bytes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, AssetCategoryType, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    color_mode: Optional[Union[str, ColorSchemeModeType, Ref, GetAtt, Sub]] = None

