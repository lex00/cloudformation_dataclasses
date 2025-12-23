"""PropertyTypes for AWS::Route53RecoveryControl::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ClusterEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "region": "Region",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None

