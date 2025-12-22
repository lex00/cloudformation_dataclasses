"""PropertyTypes for AWS::Events::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApiDestinationHttpMethod:
    """ApiDestinationHttpMethod enum values."""

    POST = "POST"
    GET = "GET"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ApiDestinationState:
    """ApiDestinationState enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ArchiveState:
    """ArchiveState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"


class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ConnectionAuthorizationType:
    """ConnectionAuthorizationType enum values."""

    BASIC = "BASIC"
    OAUTH_CLIENT_CREDENTIALS = "OAUTH_CLIENT_CREDENTIALS"
    API_KEY = "API_KEY"


class ConnectionOAuthHttpMethod:
    """ConnectionOAuthHttpMethod enum values."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class ConnectionState:
    """ConnectionState enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    AUTHORIZED = "AUTHORIZED"
    DEAUTHORIZED = "DEAUTHORIZED"
    AUTHORIZING = "AUTHORIZING"
    DEAUTHORIZING = "DEAUTHORIZING"
    ACTIVE = "ACTIVE"
    FAILED_CONNECTIVITY = "FAILED_CONNECTIVITY"


class EndpointState:
    """EndpointState enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


class EventSourceState:
    """EventSourceState enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class IncludeDetail:
    """IncludeDetail enum values."""

    NONE = "NONE"
    FULL = "FULL"


class LaunchType:
    """LaunchType enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class Level:
    """Level enum values."""

    OFF = "OFF"
    ERROR = "ERROR"
    INFO = "INFO"
    TRACE = "TRACE"


class PlacementConstraintType:
    """PlacementConstraintType enum values."""

    DISTINCTINSTANCE = "distinctInstance"
    MEMBEROF = "memberOf"


class PlacementStrategyType:
    """PlacementStrategyType enum values."""

    RANDOM = "random"
    SPREAD = "spread"
    BINPACK = "binpack"


class PropagateTags:
    """PropagateTags enum values."""

    TASK_DEFINITION = "TASK_DEFINITION"


class ReplayState:
    """ReplayState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    CANCELLING = "CANCELLING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class ReplicationState:
    """ReplicationState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RuleState:
    """RuleState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS = "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS"


@dataclass
class EndpointEventBus(PropertyType):
    EVENT_BUS_ARN = "EventBusArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bus_arn": "EventBusArn",
    }

    event_bus_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FailoverConfig(PropertyType):
    SECONDARY = "Secondary"
    PRIMARY = "Primary"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secondary": "Secondary",
        "primary": "Primary",
    }

    secondary: Optional[Secondary] = None
    primary: Optional[Primary] = None


@dataclass
class Primary(PropertyType):
    HEALTH_CHECK = "HealthCheck"

    _property_mappings: ClassVar[dict[str, str]] = {
        "health_check": "HealthCheck",
    }

    health_check: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationConfig(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, ReplicationState, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingConfig(PropertyType):
    FAILOVER_CONFIG = "FailoverConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "failover_config": "FailoverConfig",
    }

    failover_config: Optional[FailoverConfig] = None


@dataclass
class Secondary(PropertyType):
    ROUTE = "Route"

    _property_mappings: ClassVar[dict[str, str]] = {
        "route": "Route",
    }

    route: Optional[Union[str, Ref, GetAtt, Sub]] = None

