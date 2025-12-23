"""PropertyTypes for AWS::MediaPackage::Asset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EgressEndpoint(PropertyType):
    PACKAGING_CONFIGURATION_ID = "PackagingConfigurationId"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "packaging_configuration_id": "PackagingConfigurationId",
        "url": "Url",
    }

    packaging_configuration_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None

