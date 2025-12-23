"""PropertyTypes for AWS::EC2::RouteServerPeer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BgpOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "peer_liveness_detection": "PeerLivenessDetection",
        "peer_asn": "PeerAsn",
    }

    peer_liveness_detection: Optional[Union[str, Ref, GetAtt, Sub]] = None
    peer_asn: Optional[Union[int, Ref, GetAtt, Sub]] = None

