"""PropertyTypes for AWS::Bedrock::AgentAlias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AgentAliasHistoryEvent(PropertyType):
    START_DATE = "StartDate"
    ROUTING_CONFIGURATION = "RoutingConfiguration"
    END_DATE = "EndDate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start_date": "StartDate",
        "routing_configuration": "RoutingConfiguration",
        "end_date": "EndDate",
    }

    start_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    routing_configuration: Optional[list[AgentAliasRoutingConfigurationListItem]] = None
    end_date: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentAliasRoutingConfigurationListItem(PropertyType):
    AGENT_VERSION = "AgentVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_version": "AgentVersion",
    }

    agent_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

