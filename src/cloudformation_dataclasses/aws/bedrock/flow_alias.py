"""PropertyTypes for AWS::Bedrock::FlowAlias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FlowAliasConcurrencyConfiguration(PropertyType):
    TYPE = "Type"
    MAX_CONCURRENCY = "MaxConcurrency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "max_concurrency": "MaxConcurrency",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_concurrency: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class FlowAliasRoutingConfigurationListItem(PropertyType):
    FLOW_VERSION = "FlowVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_version": "FlowVersion",
    }

    flow_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

