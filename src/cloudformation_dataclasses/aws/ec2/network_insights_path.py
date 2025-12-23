"""PropertyTypes for AWS::EC2::NetworkInsightsPath."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FilterPortRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PathFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_address": "SourceAddress",
        "destination_port_range": "DestinationPortRange",
        "source_port_range": "SourcePortRange",
        "destination_address": "DestinationAddress",
    }

    source_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_port_range: Optional[FilterPortRange] = None
    source_port_range: Optional[FilterPortRange] = None
    destination_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

