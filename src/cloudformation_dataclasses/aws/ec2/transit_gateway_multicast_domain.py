"""PropertyTypes for AWS::EC2::TransitGatewayMulticastDomain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Options(PropertyType):
    STATIC_SOURCES_SUPPORT = "StaticSourcesSupport"
    AUTO_ACCEPT_SHARED_ASSOCIATIONS = "AutoAcceptSharedAssociations"
    IGMPV2_SUPPORT = "Igmpv2Support"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_sources_support": "StaticSourcesSupport",
        "auto_accept_shared_associations": "AutoAcceptSharedAssociations",
        "igmpv2_support": "Igmpv2Support",
    }

    static_sources_support: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_accept_shared_associations: Optional[Union[str, Ref, GetAtt, Sub]] = None
    igmpv2_support: Optional[Union[str, Ref, GetAtt, Sub]] = None

