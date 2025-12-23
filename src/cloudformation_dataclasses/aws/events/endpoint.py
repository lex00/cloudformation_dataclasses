"""PropertyTypes for AWS::Events::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EndpointEventBus(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bus_arn": "EventBusArn",
    }

    event_bus_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FailoverConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secondary": "Secondary",
        "primary": "Primary",
    }

    secondary: Optional[Secondary] = None
    primary: Optional[Primary] = None


@dataclass
class Primary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "health_check": "HealthCheck",
    }

    health_check: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, ReplicationState, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "failover_config": "FailoverConfig",
    }

    failover_config: Optional[FailoverConfig] = None


@dataclass
class Secondary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "route": "Route",
    }

    route: Optional[Union[str, Ref, GetAtt, Sub]] = None

