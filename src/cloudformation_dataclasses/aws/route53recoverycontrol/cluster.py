"""PropertyTypes for AWS::Route53RecoveryControl::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class NetworkType:
    """NetworkType enum values."""

    IPV4 = "IPV4"
    DUALSTACK = "DUALSTACK"


class RuleType:
    """RuleType enum values."""

    ATLEAST = "ATLEAST"
    AND = "AND"
    OR = "OR"


class Status:
    """Status enum values."""

    PENDING = "PENDING"
    DEPLOYED = "DEPLOYED"
    PENDING_DELETION = "PENDING_DELETION"


@dataclass
class ClusterEndpoint(PropertyType):
    ENDPOINT = "Endpoint"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "region": "Region",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None

