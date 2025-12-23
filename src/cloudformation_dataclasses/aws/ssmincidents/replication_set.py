"""PropertyTypes for AWS::SSMIncidents::ReplicationSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RegionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_kms_key_id": "SseKmsKeyId",
    }

    sse_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationRegion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "region_configuration": "RegionConfiguration",
        "region_name": "RegionName",
    }

    region_configuration: Optional[RegionConfiguration] = None
    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

